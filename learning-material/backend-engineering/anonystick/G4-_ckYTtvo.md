---
Creation_date: 2026-10-21 15:47
Modification_date: Wednesday 21st October 2026 15:47:35
Indexes:
  - "[[literature_notes]]"
  - "[[anonystick]]"
  - "[[Idempotency_and_Distributed_Transactions]]"
  - "[[Databases]]"
Source: https://www.youtube.com/watch?v=G4-_ckYTtvo
Author: anonystick (Tips Java / Tips Javascript)
Language: Vietnamese
Video_id: G4-_ckYTtvo
---

----
# Stripe-style idempotency, part 2: INSERT INTO vs INSERT IGNORE for an idempotent Kafka consumer

**Video:** https://www.youtube.com/watch?v=G4-_ckYTtvo (14:49, ~Jun 2026, ~2.4K views). This is the follow-up to [[A9gqa8q-l1w]] and has the actual fix.
**Credit:** [anonystick on YouTube](https://www.youtube.com/@anonystick). Written from Vietnamese auto-captions, which are fair. "about button / enable button" at the end probably means "outbox pattern / enable idempotence" *(unclear)*. "hai concurrency" = listener **concurrency** setting. The blog he shows at [10:30](https://www.youtube.com/watch?v=G4-_ckYTtvo&t=630s) isn't named in the captions *(unclear which one)*.

## What it teaches
Let the **database's unique constraint** do the deduplication, with no Redis and no check-then-insert. Store an idempotency key with a `PRIMARY KEY`/`UNIQUE` constraint, then use `INSERT IGNORE` and **check affected rows**: 1 means first time, 0 means duplicate.

## Key concepts and steps
1. **Stripe flow as he describes it:** the client opens the payment page, gets an idempotency key, sends it with the payment, and Stripe checks whether the key exists; if it does, no second charge. He calls the key "unique and managed by the server". [01:02](https://www.youtube.com/watch?v=G4-_ckYTtvo&t=62s), [01:32](https://www.youtube.com/watch?v=G4-_ckYTtvo&t=92s) *(see the correction below)*
2. **The idea:** keep the key in the DB behind a **unique** constraint, using ACID guarantees, so the consumer is idempotent without Redis or an existence check. [02:03](https://www.youtube.com/watch?v=G4-_ckYTtvo&t=123s), [02:36](https://www.youtube.com/watch?v=G4-_ckYTtvo&t=156s)
3. **Demo table:** `idempotency_key(token VARCHAR PRIMARY KEY)`. [04:43](https://www.youtube.com/watch?v=G4-_ckYTtvo&t=283s)
4. **`INSERT INTO` a duplicate** fails with `Duplicate entry ... for key PRIMARY`. In Spring that's an exception you have to catch, which he calls "painful". [05:45](https://www.youtube.com/watch?v=G4-_ckYTtvo&t=345s), [06:17](https://www.youtube.com/watch?v=G4-_ckYTtvo&t=377s)
5. **`INSERT IGNORE`** never throws for the duplicate. It returns affected rows **1** (new key, go ahead) or **0** (already seen, skip), plus a *warning* instead of an error. He prefers it. [06:49](https://www.youtube.com/watch?v=G4-_ckYTtvo&t=409s), [09:57](https://www.youtube.com/watch?v=G4-_ckYTtvo&t=597s), [10:30](https://www.youtube.com/watch?v=G4-_ckYTtvo&t=630s)
6. **"Doesn't that make the DB a bottleneck?"** No: listener concurrency (3, 10, 20 threads) caps how many DB connections are active at once, and HikariCP's pool covers it. Scale further with ProxySQL. [07:19](https://www.youtube.com/watch?v=G4-_ckYTtvo&t=439s), [07:52](https://www.youtube.com/watch?v=G4-_ckYTtvo&t=472s), [08:55](https://www.youtube.com/watch?v=G4-_ckYTtvo&t=535s), [09:25](https://www.youtube.com/watch?v=G4-_ckYTtvo&t=565s)
7. **"What if two inserts arrive at the same nanosecond?"** The SQL layer (parser, optimizer, executor) may run them at the same time, but in the storage engine (InnoDB: B-tree index, locks, MVCC) the unique index check is serialised, "like a post office with one mailbox slot", so one wins and the other sees the duplicate. [11:34](https://www.youtube.com/watch?v=G4-_ckYTtvo&t=694s), [12:08](https://www.youtube.com/watch?v=G4-_ckYTtvo&t=728s), [12:40](https://www.youtube.com/watch?v=G4-_ckYTtvo&t=760s), [13:15](https://www.youtube.com/watch?v=G4-_ckYTtvo&t=795s)
8. The code is applied and published in the next video. [14:18](https://www.youtube.com/watch?v=G4-_ckYTtvo&t=858s)

## Edge cases / pitfalls (and corrections)
- **Put the key insert and the business write in the SAME transaction.** If you insert the key, commit, then crash before the business update, the retry sees "duplicate" and skips it, so **the message is lost**. The video doesn't say this out loud. The safe shape is `BEGIN; INSERT IGNORE key; if affected == 1 → do the business write; COMMIT;`, then commit the Kafka offset after the DB commit.
- **`INSERT IGNORE` ignores more than duplicates.** It turns other "ignorable" errors into warnings too (e.g. bad values for a column in strict mode, partition-match errors), so a broken row can be silently skipped. Use a dedicated key table with only the key column (+ timestamp), or use `INSERT ... ON DUPLICATE KEY UPDATE id = id`. In **PostgreSQL** the equivalent is `INSERT ... ON CONFLICT (key) DO NOTHING` and checking the row count. Sources: [MySQL INSERT (IGNORE)](https://dev.mysql.com/doc/refman/8.4/en/insert.html), [PostgreSQL INSERT ON CONFLICT](https://www.postgresql.org/docs/current/sql-insert.html#SQL-ON-CONFLICT).
- **Catching the exception isn't wrong either.** With `INSERT INTO` you catch Spring's `DuplicateKeyException` (a `DataIntegrityViolationException`). In Postgres a failed statement **aborts the whole transaction**, so either use `ON CONFLICT DO NOTHING` or a savepoint.
- **Stripe correction:** in Stripe's API the **client generates** the key (V4 UUID recommended) and sends it as the `Idempotency-Key` header. Stripe saves the status code and body of the first request and replays them for retries (including 500s), keys can be pruned after 24 h, and reusing a key with different parameters errors. So it's not "issued by the server". Source: [Stripe API: Idempotent requests](https://docs.stripe.com/api/idempotent_requests). For a Kafka consumer, use a key that's stable across re-sends: the event id from the outbox row, or a business key like `order_id + action`. Not the Kafka offset, which changes if the event is re-published.
- **Retention:** a key table grows forever, so purge keys older than your maximum redelivery window (Stripe uses 24 h).
- **"One mailbox slot":** the correct idea is that InnoDB takes a lock on the unique index entry, so the second inserter **waits** for the first to commit or roll back. If the first rolls back, the second succeeds. The "CPU can't do two things at once" explanation isn't accurate (multi-core CPUs can), but the conclusion holds.

## How it connects to the core topics
- **Core focus:** duplicate messages, idempotent consumers, atomicity of "dedup + effect", race conditions.
- **QA tests to design:** (1) send the same event id 2× concurrently, then assert 1 business row and 1 key row. (2) Inject a failure *after* the key insert and *before* the business write; on retry the effect must still happen once (catches split transactions). (3) Same key, different payload: decide and test the policy (Stripe errors). (4) Send a malformed field and check it isn't silently swallowed by `INSERT IGNORE`. (5) Load-test with listener concurrency 3 vs 20 and watch the Hikari pool metrics.
- **Spring Boot:** `@Transactional` listener method; `jdbcTemplate.update("INSERT IGNORE INTO processed_event(id) VALUES (?)", id)` returns an `int`; for Postgres `INSERT ... ON CONFLICT DO NOTHING`. `spring.kafka.listener.concurrency` ≤ Hikari `maximum-pool-size`. **Go:** `res, _ := tx.ExecContext(ctx, "INSERT ... ON CONFLICT DO NOTHING", id)`; `n, _ := res.RowsAffected()`; if `n == 0` skip, else do the work in the same `tx`.

## Related
[[Idempotent Consumer]] · [[Idempotency Key]] · [[Unique Constraint]] · [[A9gqa8q-l1w]] · [[inUimYVAGv0]] · [[2TBqQBEI56A]] · [[Module 1 - Messaging and Transactions]]

---
## Flash cards section
How does INSERT IGNORE give you idempotency?::With a UNIQUE/PRIMARY key on the idempotency key, a duplicate insert affects 0 rows (warning, no exception), so 1 means process and 0 means skip.
Why must the dedup-key insert and the business write share one transaction?::Otherwise a crash after the key commit but before the work makes the retry look like a duplicate and the work is lost.
PostgreSQL equivalent of MySQL INSERT IGNORE for dedup?::INSERT ... ON CONFLICT (key) DO NOTHING, then check the affected row count.
What's the hidden risk of INSERT IGNORE?::It downgrades other ignorable errors to warnings too, so bad data can be silently dropped.
What key should a Kafka consumer dedupe on?::A stable event id (e.g. the outbox row id) or a business key like order_id+action. Not the offset, which changes on re-publish.
