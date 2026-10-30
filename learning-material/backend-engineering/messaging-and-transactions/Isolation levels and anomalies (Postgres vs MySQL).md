---
Creation_date: 2026-10-21 15:47
Modification_date: Wednesday 21st October 2026 15:51:01
Indexes:
  - "[[permanent_notes]]"
  - "[[Transactions_and_Concurrency]]"
  - "[[Databases]]"
  - "[[Messaging and Transactions]]"
Source: docs (PostgreSQL 18 §13.2, MySQL 8.4 InnoDB manual) + channel videos VWXZUWzT46U, GLqyIqWtRiA
---

----
# Isolation levels and anomalies: PostgreSQL vs MySQL InnoDB

> **Source type: official docs, plus the channel for intuition.** The channel's isolation demo is [[VWXZUWzT46U]] (MySQL only, with two errors corrected in that note); the stock race is [[GLqyIqWtRiA]]. The table below comes from the [PostgreSQL docs §13.2](https://www.postgresql.org/docs/current/transaction-iso.html) and the [MySQL 8.4 InnoDB isolation levels](https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-isolation-levels.html) and [consistent read](https://dev.mysql.com/doc/refman/8.4/en/innodb-consistent-read.html) pages. Lost update and write skew aren't in the SQL standard; their definitions come from Berenson et al., ["A Critique of ANSI SQL Isolation Levels" (1995)](https://www.microsoft.com/en-us/research/publication/a-critique-of-ansi-sql-isolation-levels/), the paper the Postgres docs cite.

## The anomalies (plain words)
- **[[Dirty Read]]:** you read another transaction's *uncommitted* change, which may be rolled back.
- **[[Non-repeatable Read]]:** you read a row twice in one transaction and get different values, because someone committed in between.
- **[[Phantom Read]]:** you re-run a `WHERE` query and get a different *set* of rows (someone inserted or deleted a matching row).
- **[[Lost Update]]:** two transactions read the same value, both compute a new value in the app and write it, and the second write silently overwrites the first (stock 1 → two orders).
- **[[Write Skew]]:** two transactions read an overlapping condition, then each updates a *different* row, and together they break a rule neither broke alone (e.g. "at least one doctor on call": both doctors see 2 on call and both go off call).

## The table
✅ = prevented, ❌ = can happen. Defaults are in **bold**. Each DB is assumed to use plain `SELECT`s unless the cell says otherwise.

| Anomaly | PG Read Committed (**default**) | PG Repeatable Read | PG Serializable | MySQL Read Committed | MySQL Repeatable Read (**default**) | MySQL Serializable (autocommit **off**, i.e. inside `BEGIN … COMMIT`) |
|---|---|---|---|---|---|---|
| Dirty read | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Non-repeatable read | ❌ | ✅ | ✅ | ❌ | ✅ (snapshot from the first read) | ✅ |
| Phantom read | ❌ | ✅ (stricter than the standard requires) | ✅ | ❌ (no gap locks) | ✅ for plain reads (snapshot); locking reads use next-key locks to block inserts | ✅ |
| Lost update (app read-modify-write) | ❌ | ✅: the 2nd writer gets `could not serialize access due to concurrent update` (40001), so **retry** | ✅ (40001, retry) | ❌ | **❌**: InnoDB UPDATE works on the latest committed row, not your snapshot, and doesn't raise an error | ✅: plain SELECTs become `FOR SHARE` (only with autocommit off), so the 2nd writer blocks or deadlocks (1213), so retry |
| Write skew | ❌ | **❌** (snapshot isolation allows it) | ✅: SSI detects it and aborts one (40001) | ❌ | ❌ | ✅ (shared locks on the rows read) |

Notes:
- **MySQL SERIALIZABLE only adds locking inside explicit transactions** (point added after review). The MySQL 8.4 manual says: *"SERIALIZABLE: This level is like REPEATABLE READ, but InnoDB implicitly converts all plain SELECT statements to SELECT ... FOR SHARE if autocommit is disabled. If autocommit is enabled, the SELECT is its own transaction. It therefore is known to be read only and can be serialized if performed as a consistent (nonlocking) read and need not block for other transactions. (To force a plain SELECT to block if other transactions have modified the selected rows, disable autocommit.)"* ([InnoDB transaction isolation levels](https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-isolation-levels.html)). So the ✅ marks in that column assume the reads and writes run in one transaction (`START TRANSACTION`, or Spring `@Transactional`, which turns autocommit off). A standalone autocommitted SELECT is still a snapshot read, doesn't block, and protects nothing that happens later.
- PG **Read Uncommitted** behaves exactly like Read Committed, so Postgres never allows dirty reads. MySQL READ UNCOMMITTED *does* allow them (the CR00 demo in [[VWXZUWzT46U]]).
- The biggest surprise for people switching databases: **at the same "Repeatable Read" name, Postgres prevents lost updates (with an error) and MySQL doesn't.** Code that's "safe" in one can be broken in the other.
- InnoDB warns against mixing locking statements (`UPDATE`, `SELECT … FOR UPDATE`) with plain SELECTs in one REPEATABLE READ transaction: the plain SELECT shows the snapshot while the locking one acts on the latest data.
- Serialization and deadlock errors are **normal** at the stricter levels. The app must retry the whole transaction (PG SQLSTATE `40001`, MySQL error `1213`/`1205`).

## Fixes that work at any level
| Problem | Fix |
|---|---|
| Lost update on a counter or stock | One atomic statement: `UPDATE … SET stock = stock - :q WHERE id = :id AND stock >= :q`, then check affected rows. Safe in both DBs at the default level, because a blocked updater re-checks the WHERE against the new row (PG docs §13.2.1) ([[GLqyIqWtRiA]]) |
| Lost update on a read-then-write in app code | `SELECT … FOR UPDATE` (pessimistic) or a `version` column with `WHERE version = :v` (optimistic, retry on 0 rows) |
| Duplicate inserts | A **unique constraint** plus `ON CONFLICT DO NOTHING` / `INSERT IGNORE` ([[G4-_ckYTtvo]]) |
| Write skew | Lock the rows the rule depends on (`SELECT … FOR UPDATE` on *all* of them), materialise the conflict in one row you can lock, or use **Serializable + retry** |
| Job/outbox queue with several workers | `SELECT … FOR UPDATE SKIP LOCKED` ([[DQN0pRV8RnU]]) |

## How it connects to the core topics
- **Core focus:** isolation levels, race conditions, lost updates, retries after serialization failures.
- **QA technique:** two sessions and a written step order (see [[VWXZUWzT46U]]). For automated tests, two threads plus a `CountDownLatch` (Java) or `sync.WaitGroup`/channels (Go) to force the interleaving "T1 read, T2 read, T1 write, T2 write". Run each test against **both** DBs if the product supports both, and at the isolation level production actually uses (check `SHOW transaction_isolation;` in Postgres or `SELECT @@transaction_isolation;` in MySQL).
- **Test cases to write:** (1) a lost-update test: 2 concurrent "read stock, write stock-1" → expect stock decreased twice, or one error that gets retried. (2) A write-skew test: the on-call rule with 2 concurrent "go off call" → expect the rule to hold. (3) A retry test: force a 40001/1213 and check the service retries and succeeds, rather than returning 500.
- **Spring Boot:** `@Transactional(isolation = Isolation.SERIALIZABLE)` plus retry on `CannotAcquireLockException` / `PessimisticLockingFailureException` / `ConcurrencyFailureException` (e.g. Spring's `@Retryable`). JPA `@Version` for optimistic locking, `@Lock(PESSIMISTIC_WRITE)` for FOR UPDATE. **Go:** `sql.TxOptions{Isolation: sql.LevelSerializable}`, with a retry loop on pgx error code `40001`.

## Related
[[VWXZUWzT46U]] · [[GLqyIqWtRiA]] · [[9kpISaXHBvM]] · [[Isolation Level]] · [[MVCC]] · [[Lost Update]] · [[Write Skew]] · [[Messaging and Transactions]]

---
## Flash cards section
Default isolation level in PostgreSQL vs MySQL InnoDB?::PostgreSQL: Read Committed. MySQL InnoDB: Repeatable Read.
At Repeatable Read, which DB prevents a lost update and how?::PostgreSQL: the second updater fails with "could not serialize access due to concurrent update" (40001) and must retry. MySQL InnoDB RR doesn't prevent it.
What is write skew and which level prevents it in Postgres?::Two transactions read an overlapping condition and update different rows, together breaking a rule. Only Serializable (SSI) prevents it; Repeatable Read allows it.
Does PostgreSQL ever allow dirty reads?::No. Read Uncommitted behaves like Read Committed.
How does InnoDB Serializable differ from Repeatable Read?::With autocommit off, plain SELECTs become SELECT ... FOR SHARE, so reads take shared locks and block or deadlock conflicting writers. With autocommit on, a lone SELECT stays a nonlocking snapshot read.
What must an app do when it uses Serializable?::Retry the whole transaction on serialization or deadlock errors (PG 40001, MySQL 1213).
