---
Creation_date: 2026-10-21 15:47
Modification_date: Wednesday 21st October 2026 15:47:35
Indexes:
  - "[[literature_notes]]"
  - "[[anonystick]]"
  - "[[Kafka]]"
  - "[[Idempotency_and_Distributed_Transactions]]"
Source: https://www.youtube.com/watch?v=A9gqa8q-l1w
Author: anonystick (Tips Java / Tips Javascript)
Language: Vietnamese
Video_id: A9gqa8q-l1w
---

----
# Stripe-style idempotency, part 1: why `enable.idempotence=true` doesn't make your Kafka consumer idempotent

**Video:** https://www.youtube.com/watch?v=A9gqa8q-l1w (13:09, ~Jun 2026, ~3.4K views). The title promises "how to implement Stripe's idempotency", but **this video only sets up the problem**. The Stripe-inspired fix (a unique key in the DB) is in the next video, [[G4-_ckYTtvo]].
**Credit:** [anonystick on YouTube](https://www.youtube.com/@anonystick). Written from Vietnamese auto-captions, which are fair. He says *tính bất biến* (immutability) for idempotency; the right term is *tính lũy đẳng* (see [[REVIEW-jacob-batch1|Jacob's review]]). "PID" here is the producer ID. "Redis JSON try lock" is probably **Redisson** `tryLock` *(unclear in captions)*.

## What it teaches
After the outbox fixed lost orders on the producer side ([[2TBqQBEI56A]], [[DQN0pRV8RnU]]), duplicates are now the **consumer's** problem. At ~3,000 orders/s, the outbox can re-send the same event (crash, retry), and several copies can reach consumers at the same moment. He clears up the most common misconception, then shows why the "obvious" fixes break.

## Key concepts and steps
1. **Context:** producer → broker → consumer. The outbox and CDC stopped missed orders, but duplicates still reach the consumer, because the outbox retries after crashes. [01:33](https://www.youtube.com/watch?v=A9gqa8q-l1w&t=93s), [02:39](https://www.youtube.com/watch?v=A9gqa8q-l1w&t=159s), [03:10](https://www.youtube.com/watch?v=A9gqa8q-l1w&t=190s)
2. **Goal of consumer idempotency:** no paying twice for the same order, and one order per person in a flash sale. [02:39](https://www.youtube.com/watch?v=A9gqa8q-l1w&t=159s), [03:10](https://www.youtube.com/watch?v=A9gqa8q-l1w&t=190s)
3. **Low-traffic systems** can dedupe with a front-end token checked again in a middle layer (his earlier video [[inUimYVAGv0]]). A high-concurrency Kafka consumer with several services is harder. [03:40](https://www.youtube.com/watch?v=A9gqa8q-l1w&t=220s), [04:12](https://www.youtube.com/watch?v=A9gqa8q-l1w&t=252s)
4. **Misconception: "`enable.idempotence=true` solves it."** No. It's a **producer** setting and only protects the **producer ↔ broker** boundary. [04:12](https://www.youtube.com/watch?v=A9gqa8q-l1w&t=252s), [04:45](https://www.youtube.com/watch?v=A9gqa8q-l1w&t=285s), [05:15](https://www.youtube.com/watch?v=A9gqa8q-l1w&t=315s)
5. **How producer idempotence works:** with it off, a lost broker ack makes the producer retry and the partition ends up with **two copies**. With it on, the broker gives the producer a **producer ID (PID)** and each message carries an increasing **sequence number**. If a retry arrives with a sequence the broker already has (e.g. 100), it's **discarded**, so the partition keeps one copy. [05:15](https://www.youtube.com/watch?v=A9gqa8q-l1w&t=315s), [06:16](https://www.youtube.com/watch?v=A9gqa8q-l1w&t=376s), [07:18](https://www.youtube.com/watch?v=A9gqa8q-l1w&t=438s), [07:52](https://www.youtube.com/watch?v=A9gqa8q-l1w&t=472s), [08:25](https://www.youtube.com/watch?v=A9gqa8q-l1w&t=505s)
6. **The real requirement:** each message must change MySQL **once and only once**, and producer idempotence says nothing about that. [08:57](https://www.youtube.com/watch?v=A9gqa8q-l1w&t=537s)
7. **"Fresher" fix 1, check whether the token exists, then process:** the logic is right but it's a race. Thread A and thread B both check, both get "not processed", and both process. That's **TOCTOU (time-of-check to time-of-use)**. [09:30](https://www.youtube.com/watch?v=A9gqa8q-l1w&t=570s), [10:34](https://www.youtube.com/watch?v=A9gqa8q-l1w&t=634s), [11:07](https://www.youtube.com/watch?v=A9gqa8q-l1w&t=667s), [11:40](https://www.youtube.com/watch?v=A9gqa8q-l1w&t=700s)
8. **Fix 2, a distributed lock (Redisson `tryLock` in Java, a mutex in Go):** this works, but what if the JVM runs out of memory or Redis crashes and the lock disappears? [11:40](https://www.youtube.com/watch?v=A9gqa8q-l1w&t=700s), [12:10](https://www.youtube.com/watch?v=A9gqa8q-l1w&t=730s)
9. **Teaser:** Stripe's idea is a unique key, which he calls an "immutable key" (it's an **idempotency key**). The implementation comes in the next episode. [12:10](https://www.youtube.com/watch?v=A9gqa8q-l1w&t=730s), [12:41](https://www.youtube.com/watch?v=A9gqa8q-l1w&t=761s)

## Edge cases / pitfalls (and corrections)
- **Producer idempotence scope (from the docs):** it removes duplicates caused by **producer retries within one producer session**. It does *not* dedupe a message your outbox relay sends twice after a restart, because that's a new send from the app, possibly from a new producer instance with a new PID. Default since Kafka 3.0: `enable.idempotence=true`, `acks=all` ([Kafka producer configs](https://kafka.apache.org/43/configuration/producer-configs/), [KIP-679](https://cwiki.apache.org/confluence/display/KAFKA/KIP-679%3A+Producer+will+enable+the+strongest+delivery+guarantee+by+default)).
- **Kafka transactions / exactly-once semantics** (`transactional.id`, `isolation.level=read_committed`) give exactly-once only for **Kafka → Kafka** (read-process-write within Kafka). Once a consumer writes to MySQL or Postgres or calls an API, you're back to at-least-once and need consumer-side dedup. (Not in the video; standard Kafka guidance.)
- **Distributed locks** have one more failure mode he doesn't mention: a lock **lease can expire** while a slow consumer (GC pause) is still working, so a second consumer gets the lock too. A lock lowers the chance of duplicates; a DB unique constraint makes them impossible.
- He calls Stripe "PayPal of Elon Musk". That's wrong: Stripe was founded by Patrick and John Collison. In **Stripe's own design** the *client* generates the idempotency key (e.g. a V4 UUID, up to 255 chars) and sends it in an `Idempotency-Key` header. Stripe stores the first response for that key and returns it on retries, keys can be pruned after 24 h, and reusing a key with different parameters returns an error. Source: [Stripe API: Idempotent requests](https://docs.stripe.com/api/idempotent_requests).

## How it maps to the learning focus
- **Core focus:** duplicate messages, at-least-once vs exactly-once, idempotent consumers, race conditions (TOCTOU), timeouts and retries.
- **QA tests to design:** (1) publish the same event twice (same business key) and check one DB effect. (2) Publish 2 copies **concurrently** to 2 consumer threads; this is the test that catches check-then-act code. (3) Kill the consumer after the DB write but before the offset commit, restart, and check no second effect. (4) Restart the outbox relay mid-batch and count side effects (emails, payments). (5) If a Redis lock is used, kill Redis mid-flow.
- **Spring Boot:** `spring.kafka.producer.properties.enable.idempotence=true` (already the default); consumer dedup in the same `@Transactional` as the business write (see [[G4-_ckYTtvo]]). **Go:** watch the client defaults. franz-go turns producer idempotence on by default, but librdkafka-based `confluent-kafka-go` defaults to `enable.idempotence=false`, so set it explicitly ([librdkafka CONFIGURATION.md](https://github.com/confluentinc/librdkafka/blob/master/CONFIGURATION.md)). Do consumer dedup via a unique key in the same `tx`.

## Related
[[Idempotency]] · [[Idempotent Consumer]] · [[TOCTOU]] · [[Distributed Lock]] · [[Transactional Outbox]] · [[G4-_ckYTtvo]] · [[inUimYVAGv0]] · [[Module 1 - Messaging and Transactions]]

---
## Flash cards section
What does Kafka's enable.idempotence=true protect against?::Duplicate records in a partition caused by producer retries (the broker discards a repeated producer ID + sequence number). It's a producer↔broker guarantee only.
Why doesn't producer idempotence make a consumer idempotent?::Consumers still get redeliveries (crash before the offset commit, rebalance) and app-level re-sends (outbox retries). The DB side effect must be deduplicated by the consumer.
Why is "check if the token exists, then process" unsafe at high concurrency?::TOCTOU: two threads can both check before either writes, and both process.
What's the weakness of a Redis distributed lock for dedup?::Redis can crash, or the lease can expire during a long GC pause, so two workers proceed. A DB unique constraint is the real guard.
Who generates a Stripe idempotency key and what does Stripe do with it?::The client generates it (e.g. a UUID v4). Stripe saves the first response for that key and returns it on retries; a reused key with different parameters is an error.
