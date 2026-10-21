# Teaching material index

Newest first. One dated file per night, top skills listed at the top of each.

- 2026-10-21 (update): **Module 1: Messaging & Transactions, curriculum** -> [module-1/Module 1 - Messaging and Transactions.md](module-1/Module%201%20-%20Messaging%20and%20Transactions.md). Jacob's batch-1 fixes applied to 7 notes (RabbitMQ Spring AMQP AUTO ack, outbox SKIP LOCKED + Kafka 3.0 defaults, Postgres READ COMMITTED, DLX vs DB table, deadlock/synchronized, idempotency terms, share groups GA in 4.2), each checked against the official docs. New channel notes (🎥): [Saga + Outbox part 1](anonystick/2TBqQBEI56A.md), [Stripe-style idempotency part 1](anonystick/A9gqa8q-l1w.md), [part 2: INSERT IGNORE](anonystick/G4-_ckYTtvo.md), [Kafka message-order mistake](anonystick/yiXL052rNNI.md), [MySQL 4 isolation levels](anonystick/VWXZUWzT46U.md). New docs-based notes (📘, not from the channel): [Spring Kafka retries and dead-letter topics](module-1/Spring%20Kafka%20retries%20and%20dead-letter%20topics.md), [Out-of-order messages and consumer rebalancing](module-1/Out-of-order%20messages%20and%20consumer%20rebalancing.md), [Isolation levels and anomalies (Postgres vs MySQL)](module-1/Isolation%20levels%20and%20anomalies%20(Postgres%20vs%20MySQL).md). Jacob's review: [anonystick/REVIEW-jacob-batch1.md](anonystick/REVIEW-jacob-batch1.md).
- 2026-10-21: **anonystick YouTube channel (Vietnamese backend), first pass**. Obsidian literature notes with timestamped links and flash cards. Folder: [anonystick/](anonystick/). Full catalogue (786 videos, 14 topic areas): [video-list.md](anonystick/video-list.md). Status and how to resume: [PROGRESS.md](anonystick/PROGRESS.md). Topic index notes: [anonystick/indexes/](anonystick/indexes/). Notes so far (suggested reading order):
  1. [When to use a message queue](anonystick/DQRj7I3PcuM.md): decoupling, async, peak shaving; pros and cons; RabbitMQ vs Kafka
  2. [RabbitMQ reliability: ack, TTL, durable, persistent](anonystick/az2VNMgNFrk.md): how messages get lost and how to keep them
  3. [RabbitMQ dead-letter exchange for failed messages](anonystick/hrSP7UocdJ8.md): DLX, retries with limits, TTL vs processing failure
  4. [Race conditions and MySQL stock deduction](anonystick/GLqyIqWtRiA.md): read-check-write vs atomic UPDATE vs optimistic lock
  5. [Deadlocks in Java multithreading](anonystick/9kpISaXHBvM.md): Coffman conditions, jstack, lock ordering, tryLock
  6. [Idempotency for duplicate payments](anonystick/inUimYVAGv0.md): sources of duplicates; FOR UPDATE, version column, unique key
  7. [Kafka + Outbox + Saga, part 2](anonystick/DQN0pRV8RnU.md): who marks the outbox row published; producer acks vs consumer offset commits
  8. [Kafka 4.0 share groups ("queues for Kafka")](anonystick/aJ5kLfn8AtI.md): queue semantics on Kafka; ack ≠ delete; lock timeout
- 2026-10-21: QE + backend job market baseline -> [qe-backend-job-market-2026.md](qe-backend-job-market-2026.md)
