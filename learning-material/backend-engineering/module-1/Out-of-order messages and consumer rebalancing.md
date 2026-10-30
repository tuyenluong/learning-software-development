---
Creation_date: 2026-10-21 15:47
Modification_date: Wednesday 21st October 2026 15:47:35
Indexes:
  - "[[permanent_notes]]"
  - "[[Kafka]]"
  - "[[Module 1 - Messaging and Transactions]]"
Source: docs (Apache Kafka 4.3 producer/consumer configs, KIP-848, Spring for Apache Kafka 4.1.x) + channel video yiXL052rNNI
---

----
# Out-of-order messages and consumer rebalancing (Kafka)

> **Source type: mostly official docs.** The channel part is [[yiXL052rNNI]] (Kafka 05, the multi-threading order mistake). His solution videos (fZafqe9yZNI, NrM4ldZHZ2E) and "7 things about topics, partitions and consumers" (a7lmP5hdgB0) weren't usable: the first two look members-only, and a7lmP5hdgB0 was rate-limited (HTTP 429) and should be retried. Everything else is from the docs linked inline.

## Part A: why messages arrive out of order
Kafka guarantees order **only within one partition**. Events for one entity arrive out of order when:
1. **They don't share a key,** so they go to different partitions and different consumers. **Fix:** key every event by the aggregate id (`orderId`). The default partitioner hashes the key, so the same key goes to the same partition.
2. **The partition count changes.** `hash(key) % N` changes, so new events for a key land on a new partition while old ones are still unread on the old one. **Fix:** size partitions up front; if you must grow, drain first or accept a reordering window.
3. **Producer retries reorder batches.** With `enable.idempotence=false` and `max.in.flight.requests.per.connection` > 1, a failed batch that's retried can land after a later batch. **Fix:** keep idempotence on (the default since 3.0), which keeps order with up to 5 in-flight requests. ([producer configs](https://kafka.apache.org/43/configuration/producer-configs/))
4. **Several outbox pollers** publish one aggregate's rows in parallel (see [[DQN0pRV8RnU]]). **Fix:** one publisher per aggregate, in id order.
5. **The consumer parallelises inside a partition** (thread pool, `@Async`, goroutines); this is [[yiXL052rNNI]]. **Fix:** parallelise across keys (hash the key to a fixed single-threaded worker) and only commit offsets once everything before them is done.
6. **Non-blocking retry topics** (`@RetryableTopic`) move a failed event aside while later ones carry on (see [[Spring Kafka retries and dead-letter topics]]).
7. **Redelivery after a rebalance or crash:** an old event is processed **again** after newer ones (Part B).

**Defensive consumer (works for every cause above):** store a `version` or sequence per aggregate and apply an event only if `event.version == current + 1` (or `>`, for "latest state wins"). Park or retry early arrivals, and drop stale or duplicate ones. `UPDATE orders SET status = :s, version = :v WHERE id = :id AND version < :v` does this atomically.

## Part B: consumer rebalancing
A **rebalance** reassigns partitions among the consumers in a group. Triggers: a consumer joins or leaves (deploys, autoscaling), a consumer misses heartbeats for `session.timeout.ms` (default 45 s), a consumer doesn't call `poll()` within **`max.poll.interval.ms` (default 300000 ms = 5 min)**, for example because a batch is too slow, or the partition count or subscription changes. ([consumer configs](https://kafka.apache.org/43/configuration/consumer-configs/))

**What goes wrong:**
- **Duplicates:** records processed but **not yet committed** when a partition moves are processed again by the new owner. This is normal at-least-once behaviour, so consumers must be idempotent ([[G4-_ckYTtvo]]).
- **Pauses:** with the classic *eager* protocol every consumer gives up **all** partitions on every rebalance (stop-the-world), so lag spikes during each rolling deploy.
- **Rebalance storms:** a slow handler exceeds `max.poll.interval.ms`, gets kicked out, rejoins, a rebalance starts, and it repeats. Reduce `max.poll.records` (default 500), speed up processing, or raise the interval.

**Fixes and settings:**
| Tool | What it does | Where |
|---|---|---|
| **Commit on revoke** | In `ConsumerRebalanceListener.onPartitionsRevoked`, commit offsets for finished work before giving up the partition. Spring Kafka's container commits pending offsets during revocation, and `ConsumerAwareRebalanceListener` gives you `onPartitionsRevokedBeforeCommit` / `AfterCommit`. You **can't** commit in `onPartitionsLost` (ownership is already gone). | [Kafka ConsumerRebalanceListener](https://kafka.apache.org/43/javadoc/org/apache/kafka/clients/consumer/ConsumerRebalanceListener.html), [Spring rebalance listeners](https://docs.spring.io/spring-kafka/reference/kafka/receiving-messages/rebalance-listeners.html) |
| **Cooperative-sticky assignor** | Incremental rebalancing: only the partitions that actually move are revoked, and the others keep consuming. The default list is `[RangeAssignor, CooperativeStickyAssignor]`, so you're on Range until you remove it with a rolling bounce. | `partition.assignment.strategy` |
| **Static membership** | Set `group.instance.id` (plus a larger session timeout), so a restarting pod comes back as "the same member" and **no rebalance** happens if it returns within the timeout. Spring suffixes the id with `-1`, `-2`, … per concurrent child consumer. | `group.instance.id`, [Spring container docs](https://docs.spring.io/spring-kafka/reference/kafka/receiving-messages/message-listener-container.html) |
| **New consumer group protocol** (KIP-848) | The broker drives incremental assignment, with no global sync barrier. Opt in with `group.protocol=consumer`; the client default is still `classic`. | [KIP-848](https://cwiki.apache.org/confluence/display/KAFKA/KIP-848%3A+The+Next+Generation+of+the+Consumer+Rebalance+Protocol) |
| **Share groups** (KIP-932, GA in 4.2) | Queue semantics with per-record acks, when you **don't** need ordering ([[aJ5kLfn8AtI]]). | group type `share` |

## How it connects to the core topics
- **Core focus:** out-of-order and duplicate messages, consumer lag, rebalancing, timeouts.
- **QA tests to design:**
  1. **Ordering soak:** 1,000 orders × (create, pay, ship) with random processing delays. Assert every order ends "shipped" and no transition was rejected. Repeat with consumer concurrency 1 vs N, and while adding a partition.
  2. **Rebalance duplicates:** during a steady load, kill one consumer pod (`kill -9`) and start another. Assert no **double side effects** (payments, emails) and no lost records (count in = count out).
  3. **Rolling deploy:** measure p99 end-to-end latency and lag during a deploy with eager vs cooperative-sticky vs static membership.
  4. **Slow handler:** make one record take longer than `max.poll.interval.ms` and watch the logs for repeated "rebalance"/"member left" messages, a storm.
  5. **Stale event:** publish v3 then v2 for one aggregate. Assert v2 is ignored.
- **Spring Boot:** `spring.kafka.consumer.properties.partition.assignment.strategy=org.apache.kafka.clients.consumer.CooperativeStickyAssignor`, `spring.kafka.consumer.properties.group.instance.id=${HOSTNAME}`, `spring.kafka.consumer.max-poll-records`, `spring.kafka.listener.concurrency` (consumers, one per partition). **Go:** franz-go `kgo.Balancers(kgo.CooperativeStickyBalancer())`, `kgo.InstanceID(...)`, `kgo.OnPartitionsRevoked(func(...){ cl.CommitMarkedOffsets(...) })`.

## Related
[[yiXL052rNNI]] · [[DQN0pRV8RnU]] · [[Spring Kafka retries and dead-letter topics]] · [[aJ5kLfn8AtI]] · [[Idempotent Consumer]] · [[Module 1 - Messaging and Transactions]]

---
## Flash cards section
Name four causes of out-of-order events in Kafka.::No shared key (different partitions), a partition-count change, producer retries with idempotence off and >1 in-flight request, parallel processing inside a partition (also: retry topics, redelivery after a rebalance).
How can a consumer defend against out-of-order or stale events whatever the cause?::Keep a version per aggregate and apply an event only if it's newer (UPDATE ... WHERE id = :id AND version < :v); park early ones and drop stale ones.
Why do rebalances cause duplicates?::Records processed but not yet committed are re-read by the partition's new owner. Commit on revoke and make consumers idempotent.
What does static membership (group.instance.id) buy you?::A restarted consumer rejoins as the same member, so no rebalance happens if it comes back within session.timeout.ms.
Eager vs cooperative rebalancing?::Eager revokes all partitions from everyone (stop-the-world). Cooperative-sticky only revokes the partitions that move.
What triggers a rebalance when a handler is slow?::Not calling poll() within max.poll.interval.ms (default 5 min); the consumer is removed from the group.
