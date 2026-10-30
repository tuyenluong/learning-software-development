---
Creation_date: 2026-10-21 15:40
Modification_date: Wednesday 21st October 2026 15:51:01
Indexes:
  - "[[literature_notes]]"
  - "[[anonystick]]"
  - "[[Kafka]]"
  - "[[Idempotency_and_Distributed_Transactions]]"
Source: https://www.youtube.com/watch?v=DQN0pRV8RnU
Author: anonystick (Tips Java / Tips Javascript)
Language: Vietnamese
Video_id: DQN0pRV8RnU
---

----
# 100K QPS with Kafka + Outbox + Saga: how senior backend engineers prevent data loss (Part 2)

**Video:** https://www.youtube.com/watch?v=DQN0pRV8RnU (11:56, ~Jun 2026, ~3.5K views)
**Credit:** [anonystick on YouTube](https://www.youtube.com/@anonystick). Written from Vietnamese auto-captions. The public captions end at about 11:31, just as the code walkthrough starts, so the implementation part isn't covered here.

## What it teaches
This is part 2 of the DDD "transaction & concurrency" series. It compares three ways to get events out reliably ([[Transactional Outbox]], [[Change Data Capture]], and a hybrid), answers *"who marks an outbox row as published, and when?"*, and explains that Kafka has **two different kinds of acknowledgement**, which people coming from RabbitMQ often mix up.

## Key concepts and steps
1. **Three designs:** (1) an outbox table plus a scheduled poller; (2) [[Change Data Capture]], reading the MySQL binlog (*bin log*); (3) a hybrid where you write an outbox event and stream from the outbox via CDC, so there's no polling SELECT and no UPDATE of a `published` flag. The hybrid is the best and the most complex. [01:04](https://www.youtube.com/watch?v=DQN0pRV8RnU&t=64s), [01:37](https://www.youtube.com/watch?v=DQN0pRV8RnU&t=97s)
2. **Weaknesses of a polling outbox:** constant inserts make the DB a bottleneck, and the DB is shared with business traffic; polling every 1 s adds latency and creates bursts of thousands of rows; and you must flip `published = true`, otherwise rows get re-sent forever, which is where [[Idempotency]] comes in. [02:10](https://www.youtube.com/watch?v=DQN0pRV8RnU&t=130s), [02:40](https://www.youtube.com/watch?v=DQN0pRV8RnU&t=160s), [03:13](https://www.youtube.com/watch?v=DQN0pRV8RnU&t=193s)
3. **Who updates `published = true`?** The **producer** side does. The consumer is another service. If it wrote to the producer's outbox table, it would break the [[Service Boundary]] (a shared-database [[Anti-pattern]]). [03:44](https://www.youtube.com/watch?v=DQN0pRV8RnU&t=224s), [04:47](https://www.youtube.com/watch?v=DQN0pRV8RnU&t=287s), [05:19](https://www.youtube.com/watch?v=DQN0pRV8RnU&t=319s)
4. **When?** When the **producer ack** arrives, meaning the broker has received the message and written it to disk *(correction: an ack means the record is in the leader's log, or in all in-sync replicas' logs with `acks=all`, which can still be the OS page cache and not yet fsynced. Kafka's durability comes from replication, not fsync)*. That has nothing to do with the consumer. [05:51](https://www.youtube.com/watch?v=DQN0pRV8RnU&t=351s), [06:22](https://www.youtube.com/watch?v=DQN0pRV8RnU&t=382s), [06:52](https://www.youtube.com/watch?v=DQN0pRV8RnU&t=412s)
5. **"But what if the consumer fails after we set published = true?"** The message isn't lost. The consumer hasn't committed its offset, so processing resumes from the last committed offset. The outbox doesn't need to care. [07:23](https://www.youtube.com/watch?v=DQN0pRV8RnU&t=443s), [07:55](https://www.youtube.com/watch?v=DQN0pRV8RnU&t=475s)
6. **Producer `acks` setting:** `acks=0` means no waiting and the highest throughput, but you can lose data if the broker crashes; `acks=1` waits for the leader only, so data can be lost if the leader dies before followers copy it; `acks=all` waits for all in-sync replicas, which is the safest for production and slowest. [08:26](https://www.youtube.com/watch?v=DQN0pRV8RnU&t=506s), [08:58](https://www.youtube.com/watch?v=DQN0pRV8RnU&t=538s), [09:28](https://www.youtube.com/watch?v=DQN0pRV8RnU&t=568s)
7. **Consumer ack = [[Offset Commit]]:** Kafka doesn't ack each message like RabbitMQ does. The consumer commits an offset ("done up to 31, send me 32"). [09:28](https://www.youtube.com/watch?v=DQN0pRV8RnU&t=568s), [09:59](https://www.youtube.com/watch?v=DQN0pRV8RnU&t=599s), [11:00](https://www.youtube.com/watch?v=DQN0pRV8RnU&t=660s)
8. The context is asynchronous order placement with Kafka in a high-concurrency flash-sale project. [11:31](https://www.youtube.com/watch?v=DQN0pRV8RnU&t=691s)

## Tools / concepts mentioned
Kafka producer `acks` (0 / 1 / all), consumer offset commit, MySQL binlog CDC (the channel has a Debezium video: KqLzls2xCnQ), a scheduled outbox poller, the Saga pattern (covered in Part 1: 2TBqQBEI56A, and the "JAVA DDD (24/25) SAGA" videos).

## Edge cases / pitfalls (and corrections)
- **Wording correction:** at [07:55](https://www.youtube.com/watch?v=DQN0pRV8RnU&t=475s) he says the *broker* "retries/resends". Kafka doesn't push. The consumer *pulls*, and after a crash or [[Rebalancing]] it re-reads from the last **committed** offset. The effect is the same (at-least-once delivery).
- **Crash window in the outbox:** if the poller sends to Kafka and crashes *before* setting `published=true`, the event is sent again, so the outbox gives **at-least-once**, and consumers must be [[Idempotent Consumer]]s (consistent with his idempotency point).
- **Defaults changed in Kafka 3.0 ([KIP-679](https://cwiki.apache.org/confluence/display/KAFKA/KIP-679%3A+Producer+will+enable+the+strongest+delivery+guarantee+by+default)):** the producer now defaults to `acks=all` and `enable.idempotence=true` (before 3.0 it was `acks=1`, idempotence off). Idempotence is silently turned off if you set a conflicting config (e.g. `acks=1`, or `max.in.flight.requests.per.connection` > 5) without explicitly enabling it. So "choose acks=all for production" is already the default; the risk is someone overriding it. Source: [Kafka producer configs](https://kafka.apache.org/43/configuration/producer-configs/).
- `acks=all` only protects you if it's paired with the topic/broker setting `min.insync.replicas` ≥ 2 (default 1), otherwise "all in-sync replicas" can be just the leader.
- **Several outbox pollers at once** (e.g. 3 pods running the same scheduler) will grab the same unpublished rows and send duplicates. Either run one leader-elected poller, or claim rows with `SELECT ... FROM outbox WHERE published = false ORDER BY id LIMIT 100 FOR UPDATE SKIP LOCKED` so each poller locks a different batch ([PostgreSQL SELECT: SKIP LOCKED](https://www.postgresql.org/docs/current/sql-select.html#SQL-FOR-UPDATE-SHARE); MySQL 8.0+ supports it too: [InnoDB locking reads](https://dev.mysql.com/doc/refman/8.4/en/innodb-locking-reads.html)).
- **Order per aggregate:** SKIP LOCKED can hand event 2 of order #42 to poller B while poller A is still sending event 1, so consumers see "paid" before "created". Keep publish order per aggregate: send events for one aggregate from one poller in id order (e.g. partition pollers by `hash(aggregate_id)`), and use the **aggregate id as the Kafka message key** so all of its events land on the same partition, where Kafka keeps order. See [[Out-of-order messages and consumer rebalancing]].
- If you commit offsets *before* processing (e.g. auto-commit), a crash can lose a message. If you commit *after*, a crash can duplicate it.

## How it maps to the learning focus
- **Core focus:** lost vs duplicate messages, the outbox pattern, at-least-once vs exactly-once, producer vs consumer acknowledgements, offset commits.
- **QA angle:** kill the outbox publisher between "sent" and "marked published", then check the duplicate is harmless. Kill the consumer between "processed" and "offset committed", then check nothing is double-applied. Stop a broker while producing with `acks=1` vs `acks=all` and compare what gets lost.
- **Spring Boot / Go:** Spring Kafka `AckMode` (RECORD/BATCH/MANUAL), `@Transactional` outbox write together with the business row; in Go, `franz-go`/`sarama` with manual commit.

## Related
[[Transactional Outbox]] · [[Saga Pattern]] · [[Change Data Capture]] · [[Offset Commit]] · [[Idempotent Consumer]] · [[Kafka]]

---
## Flash cards section
In a transactional outbox, which side should mark an event as published?::The producer service, after the broker acks. Letting the consumer touch the producer's DB breaks service boundaries.
What does a Kafka producer ack mean?::The broker (leader, or all in-sync replicas with acks=all) has written the message. It says nothing about consumers.
What is a Kafka consumer's "ack"?::Committing an offset: "I've processed up to N, give me N+1." It isn't a per-message ack like RabbitMQ's.
Why does a polling outbox give at-least-once rather than exactly-once delivery?::The publisher can crash after sending but before marking the row published, so the row is sent again.
What are the Kafka producer defaults for acks and enable.idempotence since 3.0?::acks=all and enable.idempotence=true (KIP-679). Before 3.0 they were acks=1 and false.
How do several outbox pollers avoid sending the same rows twice?::Use one leader poller, or claim rows with SELECT ... FOR UPDATE SKIP LOCKED so each poller locks a different batch, and keep per-aggregate order (Kafka key = aggregate id).
