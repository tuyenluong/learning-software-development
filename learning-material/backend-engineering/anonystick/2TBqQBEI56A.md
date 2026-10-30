---
Creation_date: 2026-10-21 15:47
Modification_date: Wednesday 21st October 2026 15:47:35
Indexes:
  - "[[literature_notes]]"
  - "[[anonystick]]"
  - "[[Kafka]]"
  - "[[Idempotency_and_Distributed_Transactions]]"
Source: https://www.youtube.com/watch?v=2TBqQBEI56A
Author: anonystick (Tips Java / Tips Javascript)
Language: Vietnamese
Video_id: 2TBqQBEI56A
---

----
# Saga + Outbox, part 1: why async ordering with Kafka needs Saga *and* Outbox (and why CDC beats polling)

**Video:** https://www.youtube.com/watch?v=2TBqQBEI56A (16:51, ~May 2026, ~5.3K views). YouTube's English title: "ULTIMATE solution for system errors when switching from SAGA-OUTBOX Pattern to SAGA-CDC...". This is **part 1**; part 2 is [[DQN0pRV8RnU]].
**Credit:** [anonystick on YouTube](https://www.youtube.com/@anonystick). Written from Vietnamese auto-captions, which are fair here. The opening 30 s is a teaser clip repeated from 07:20. **00:33–02:06 is career talk** (AI and the job market, accepting lower pay at 35+) and isn't covered. Caption terms: "public" = publish, "phone" = `false`, "actin" = worker *(unclear)*, "outbox memory" at 07:53 is probably "out of memory" *(unclear)*.

## What it teaches
He reviews his own async order flow from the high-concurrency ticket project (the "session 31" code), shows three ways it breaks in production, and builds up to **Saga + [[Transactional Outbox]]**, then recommends **[[Change Data Capture]]** (Debezium on the MySQL binlog) over a polling outbox. The core point: *high QPS doesn't mean the system is safe*.

## Key concepts and steps
1. **The original flow (no Saga, no Outbox), 5 steps:** (1) check stock in the Redis cache with a Lua script; (2) snapshot the event price; (3) insert a **pending** order into a temp table; (4) push to Kafka for async processing, whose consumer later sets the order to **success**; (5) return to the user right away. Low latency, tests pass. [03:11](https://www.youtube.com/watch?v=2TBqQBEI56A&t=191s), [03:43](https://www.youtube.com/watch?v=2TBqQBEI56A&t=223s), [04:14](https://www.youtube.com/watch?v=2TBqQBEI56A&t=254s)
2. **Dead point 1, the Kafka send fails after the DB insert:** no message reaches the consumer, so the order stays **pending forever**, stuck with nobody to process it. This is the [[Dual Write]] problem. [04:44](https://www.youtube.com/watch?v=2TBqQBEI56A&t=284s), [05:16](https://www.youtube.com/watch?v=2TBqQBEI56A&t=316s)
3. **Dead point 2, the DB insert fails after stock was taken in Redis:** for example a lock problem throws, and the ticket "evaporates" because nothing gives the stock back. [05:16](https://www.youtube.com/watch?v=2TBqQBEI56A&t=316s), [05:46](https://www.youtube.com/watch?v=2TBqQBEI56A&t=346s)
4. **Dead point 3, no [[Idempotency]]:** fast double clicks, and organised bots ("mafia") reselling flash-sale tickets. Summary: **no rollback, no retry, no idempotency**. [05:46](https://www.youtube.com/watch?v=2TBqQBEI56A&t=346s), [06:17](https://www.youtube.com/watch?v=2TBqQBEI56A&t=377s)
5. **[[Saga Pattern]] fixes rollback:** wrap steps 1–4; if a later step fails, run compensations for the earlier ones (e.g. put the stock back). He points to his two Saga videos (Java and Go). [06:49](https://www.youtube.com/watch?v=2TBqQBEI56A&t=409s), [07:20](https://www.youtube.com/watch?v=2TBqQBEI56A&t=440s)
6. **But Saga can't recall a message that's already published.** If the app crashes *after* the Kafka message went out, Saga rolls back the DB and Redis, but the consumer is already sending the SMS or email "order placed". Saga only controls its own area; once a message has left, it can't be undone. [07:20](https://www.youtube.com/watch?v=2TBqQBEI56A&t=440s), [08:26](https://www.youtube.com/watch?v=2TBqQBEI56A&t=506s), [08:56](https://www.youtube.com/watch?v=2TBqQBEI56A&t=536s)
7. **Outbox:** instead of publishing directly, insert an `outbox_event` row (`published = false`) **in the same DB transaction** as the pending order. Both commit or neither does. Saga now only has to compensate two steps. [09:29](https://www.youtube.com/watch?v=2TBqQBEI56A&t=569s), [10:00](https://www.youtube.com/watch?v=2TBqQBEI56A&t=600s), [10:30](https://www.youtube.com/watch?v=2TBqQBEI56A&t=630s)
8. **A separate worker relays the outbox** every few ms or seconds: `SELECT ... FROM outbox_event WHERE published = false`, publish to the `order-processing` topic, then mark the row published. [11:00](https://www.youtube.com/watch?v=2TBqQBEI56A&t=660s), [11:32](https://www.youtube.com/watch?v=2TBqQBEI56A&t=692s), [12:02](https://www.youtube.com/watch?v=2TBqQBEI56A&t=722s)
9. **What it buys:** after a power cut, crash or OOM, the row is still in the DB, so the worker re-reads unpublished rows on restart and pushes them: **retry + crash recovery**, and the dual write is solved. He insists the order insert and the outbox insert must be in one transaction, "never separate". [12:34](https://www.youtube.com/watch?v=2TBqQBEI56A&t=754s), [13:07](https://www.youtube.com/watch?v=2TBqQBEI56A&t=787s), [13:39](https://www.youtube.com/watch?v=2TBqQBEI56A&t=819s), [14:10](https://www.youtube.com/watch?v=2TBqQBEI56A&t=850s)
10. **Interview tip:** bring Saga and Outbox into your self-introduction so the interviewer asks about them. [14:10](https://www.youtube.com/watch?v=2TBqQBEI56A&t=850s), [14:42](https://www.youtube.com/watch?v=2TBqQBEI56A&t=882s)
11. **CDC instead of a polling outbox:** Debezium reads the MySQL binlog (or MongoDB change streams) continuously, so there's almost no latency versus a cron or worker polling every 0.5–2 s. He recommends CDC. [15:13](https://www.youtube.com/watch?v=2TBqQBEI56A&t=913s), [15:46](https://www.youtube.com/watch?v=2TBqQBEI56A&t=946s), [16:17](https://www.youtube.com/watch?v=2TBqQBEI56A&t=977s)

## Edge cases / pitfalls (and corrections)
- **Who sets `published = true`?** At [12:02](https://www.youtube.com/watch?v=2TBqQBEI56A&t=722s)–[12:34](https://www.youtube.com/watch?v=2TBqQBEI56A&t=754s) he draws the **consumer** updating the flag. That contradicts his own part 2 ([[DQN0pRV8RnU]]), where the **producer-side relay** marks the row after the broker ack and the consumer never touches the producer's table. Teach the part 2 version.
- **The outbox gives at-least-once, not exactly-once.** The relay can crash after sending but before marking the row, so it sends again. Consumers must deduplicate (see [[A9gqa8q-l1w]] and [[G4-_ckYTtvo]]).
- **Redis isn't in the transaction.** The outbox makes "DB row + event" atomic, but the step-1 Redis stock decrement is still a separate write. A crash between Redis and the DB commit still needs compensation (Saga) or a reconciliation job.
- **Multiple relay workers** need `FOR UPDATE SKIP LOCKED` or a single leader, and per-aggregate ordering (key = order id). See the corrections in [[DQN0pRV8RnU]].
- **CDC caveats** (not in the video): it needs binlog/replication access and a Kafka Connect cluster to run, schema changes flow through to consumers, and Debezium's usual guarantee is also at-least-once. Many teams use CDC *on the outbox table* (the hybrid in part 2) so they publish clean events instead of raw table changes.

## How it maps to the learning focus
- **Core focus:** partial failures and dual writes, distributed transactions (Saga with compensation), outbox, at-least-once delivery, crash recovery.
- **QA tests to design:** (1) make Kafka unavailable at step 4, then check no order is stuck in pending (or that a sweeper fixes it). (2) Kill the app between the DB commit and the publish, restart, and check the event is published exactly once *from the consumer's point of view*. (3) Make step 3 fail after the Redis decrement and check the stock is restored. (4) Double-submit the same order concurrently and check there's one order. (5) Measure end-to-end latency with polling vs CDC.
- **Spring Boot:** `@Transactional` service writes `orders` + `outbox_event`; a `@Scheduled` relay or Debezium connector; the Spring Modulith event publication registry is a ready-made outbox. **Go:** `tx := db.BeginTx(...)` for both inserts, and a relay goroutine with `SELECT ... FOR UPDATE SKIP LOCKED`.

## Related
[[Saga Pattern]] · [[Transactional Outbox]] · [[Change Data Capture]] · [[Dual Write]] · [[Idempotent Consumer]] · [[DQN0pRV8RnU]] · [[A9gqa8q-l1w]] · [[Module 1 - Messaging and Transactions]]

---
## Flash cards section
What is the dual-write problem in "insert order, then send to Kafka"?::The two writes aren't atomic. If the send fails after the DB commit, the order is stuck pending; if you send first and the DB fails, consumers act on an order that doesn't exist.
What does Saga fix and what can't it fix here?::Saga compensates earlier local steps (rollback). It can't recall a Kafka message that a consumer has already acted on.
How does a transactional outbox remove the dual write?::Insert the event row in the same DB transaction as the business row, then a separate relay publishes unpublished rows. Both rows commit or neither does.
Why does an outbox relay give at-least-once delivery?::It can crash after publishing but before marking the row published, so it publishes again on restart.
Polling outbox vs CDC (Debezium)?::Polling adds latency and DB load from repeated SELECT/UPDATE. CDC tails the binlog continuously with near-zero latency but needs connector infrastructure.
