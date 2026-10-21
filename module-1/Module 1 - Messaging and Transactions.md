---
Creation_date: 2026-10-21 15:47
Modification_date: Wednesday 21st October 2026 15:47:35
Indexes:
  - "[[home]]"
  - "[[permanent_notes]]"
---

----
# Module 1: Messaging & Transactions (curriculum)

Status: **lessons 1–8 locked by Jacob** (review: [[REVIEW-jacob-batch1]]), in Jake's batch-1 reading order, with his corrections applied. Lessons with a letter (4a, 6a, 7a…) are **new, added 2026-10-21 to fill the gaps Jacob listed, and still need Jacob's check**. Each is placed right after the lesson it builds on.

Legend: 🎥 = anonystick video note (Vietnamese, timestamped) · 📘 = permanent note written from official docs (not from the channel).

| # | Lesson | Type | Core-focus topics |
|---|---|---|---|
| 1 | [[DQRj7I3PcuM]]: when to use a message queue | 🎥 | decoupling, async, peak shaving, RabbitMQ vs Kafka |
| 2 | [[az2VNMgNFrk]]: RabbitMQ reliability (ack, TTL, durable, persistent) | 🎥 | lost messages, at-least-once, **Spring AMQP AUTO ≠ noAck** |
| 3 | [[hrSP7UocdJ8]]: RabbitMQ dead-letter exchange | 🎥 | poison messages, DLX, retry limits, **when a DB table beats DLX** |
| 4 | [[GLqyIqWtRiA]]: race conditions and stock deduction | 🎥 | read-check-write, lost update, atomic UPDATE, **Postgres RC behaviour** |
| 4a | [[VWXZUWzT46U]]: MySQL's 4 isolation levels, two-session demo | 🎥 (new) | dirty / non-repeatable reads, savepoints (2 errors corrected) |
| 4b | [[Isolation levels and anomalies (Postgres vs MySQL)]] | 📘 (new) | anomaly × level table, lost update, write skew, retries |
| 5 | [[9kpISaXHBvM]]: deadlocks in Java | 🎥 | Coffman conditions, jstack, lock ordering, tryLock |
| 6 | [[inUimYVAGv0]]: idempotency for duplicate payments | 🎥 | duplicates, FOR UPDATE, version column, unique key |
| 6a | [[2TBqQBEI56A]]: Saga + Outbox, part 1 | 🎥 (new) | dual write, Saga compensation, outbox, CDC |
| 7 | [[DQN0pRV8RnU]]: Kafka + Outbox + Saga, part 2 | 🎥 | who marks published, producer acks vs offset commits, **SKIP LOCKED, per-aggregate order, 3.0 defaults** |
| 7a | [[A9gqa8q-l1w]]: Stripe-style idempotency, part 1 | 🎥 (new) | producer idempotence ≠ consumer idempotence, TOCTOU, lock pitfalls |
| 7b | [[G4-_ckYTtvo]]: Stripe-style idempotency, part 2 (INSERT IGNORE) | 🎥 (new) | unique-key dedup in the same transaction |
| 7c | [[yiXL052rNNI]]: Kafka message-order mistake | 🎥 (new) | per-partition order, keys, multi-threading trap |
| 7d | [[Out-of-order messages and consumer rebalancing]] | 📘 (new) | causes of reordering, version checks, rebalancing, static membership, cooperative-sticky |
| 7e | [[Spring Kafka retries and dead-letter topics]] | 📘 (new) | DefaultErrorHandler, DeadLetterPublishingRecoverer, @RetryableTopic, ordering trade-off |
| 8 | [[aJ5kLfn8AtI]]: Kafka share groups ("queues for Kafka") | 🎥 | queue semantics on Kafka; **GA since 4.2** |

## Gap coverage (Jacob's list)
- Spring Kafka retries + dead-letter topics → **7e (docs)**. No public channel video found.
- Out-of-order messages and rebalancing → **7c (channel)** for the problem, plus **7d (docs)** for causes, fixes and rebalancing. The channel's solution videos look members-only, and "7 things about topics/partitions/consumers" (a7lmP5hdgB0) was rate-limited and is queued for retry.
- Isolation-level anomalies table → **4a (channel, MySQL only)** plus **4b (docs, MySQL vs Postgres)**.
- Saga part 1 (2TBqQBEI56A) and Stripe idempotency (A9gqa8q-l1w) → **6a, 7a**, plus 7b because A9gqa8q-l1w only sets up the problem.

## Still open / candidates for Module 1
- Jacob's "MySQL deadlocks (JDCbKBhmrC4)": that id isn't in the catalogue. The matching video is **JDbKCDj3pMs** ("Section 116: When do DEADLOCKS happen?"), whose hidden view count suggests it's members-only. Same for **Debezium CDC (KqLzls2xCnQ)**. They're queued; the fetcher will mark them if they're locked.
- Transcripts already fetched that could extend the module: retries from the client side, "Retry API carefully" (gyaoxeCKkRY) and "retryable / retryDelay" (uuaST5OhCx4); MVCC in MySQL (WKGIz5ViT7Y), the follow-up to 4a.

## Suggested pacing (for Jacob)
One lesson per noon slot. 4a+4b and 7a+7b work as pairs. Each note ends with flash cards for the night quiz.
