---
Creation_date: 2026-10-21 15:47
Modification_date: Wednesday 21st October 2026 15:47:35
Indexes:
  - "[[literature_notes]]"
  - "[[anonystick]]"
  - "[[Transactions_and_Concurrency]]"
  - "[[Databases]]"
Source: https://www.youtube.com/watch?v=VWXZUWzT46U
Author: anonystick (Tips Javascript)
Language: Vietnamese
Video_id: VWXZUWzT46U
---

----
# Mastering MySQL (Section 112): the 4 transaction isolation levels, demoed with two sessions

**Video:** https://www.youtube.com/watch?v=VWXZUWzT46U (26:10, ~2024–25, ~6.8K views). Part of the "Làm chủ MySQL" (Mastering MySQL) series; the previous episode is ACID (ylidVS4HvtE), the next is MVCC ([[WKGIz5ViT7Y]], transcript fetched, no note yet).
**Credit:** [anonystick on YouTube](https://www.youtube.com/@anonystick). Written from Vietnamese auto-captions, which are rough: "trans / tron / tression / transition" = transaction or session, "comic / commic / mic" = commit, "RBC / runback" = rollback, "repeat table / RCK table" = REPEATABLE READ, "realizable / izable" = SERIALIZABLE. **He makes two technical mistakes** (READ COMMITTED "waits", SERIALIZABLE "table lock"); see the corrections.

## What it teaches
Using two MySQL sessions (user A and user B) on a `test_player` table (Pepe, Ronaldo, Messi), he shows `START TRANSACTION` / `COMMIT` / `ROLLBACK`, savepoints, and what session B sees at each isolation level while A has uncommitted changes.

## Key concepts and steps
1. **Basics:** autocommit is on by default; group statements with `START TRANSACTION … COMMIT/ROLLBACK`. Each session's open transaction doesn't affect another session until it commits. [00:32](https://www.youtube.com/watch?v=VWXZUWzT46U&t=32s), [01:02](https://www.youtube.com/watch?v=VWXZUWzT46U&t=62s), [01:32](https://www.youtube.com/watch?v=VWXZUWzT46U&t=92s)
2. **Demo:** A updates Ronaldo → CR7 and deletes Messi without committing. A sees its own changes; B still sees the old data until A commits. [03:10](https://www.youtube.com/watch?v=VWXZUWzT46U&t=190s), [04:51](https://www.youtube.com/watch?v=VWXZUWzT46U&t=291s), [05:24](https://www.youtube.com/watch?v=VWXZUWzT46U&t=324s)
3. **[[Savepoint]]s:** `SAVEPOINT update_name; … ROLLBACK TO update_name;` undoes the delete but keeps the update. He says businesses rarely use partial rollback because it's hard to control. [05:54](https://www.youtube.com/watch?v=VWXZUWzT46U&t=354s), [06:25](https://www.youtube.com/watch?v=VWXZUWzT46U&t=385s), [07:00](https://www.youtube.com/watch?v=VWXZUWzT46U&t=420s), [08:41](https://www.youtube.com/watch?v=VWXZUWzT46U&t=521s)
4. **The 4 levels:** READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, SERIALIZABLE. Set them with `SET SESSION TRANSACTION ISOLATION LEVEL …`. [09:44](https://www.youtube.com/watch?v=VWXZUWzT46U&t=584s), [10:48](https://www.youtube.com/watch?v=VWXZUWzT46U&t=648s)
5. **READ UNCOMMITTED → [[Dirty Read]]:** A sets CR9 → CR00 without committing; B reads CR00. A rolls back to CR9, but B has already used CR00 for other work. Fast, but no consistency. [11:19](https://www.youtube.com/watch?v=VWXZUWzT46U&t=679s), [12:23](https://www.youtube.com/watch?v=VWXZUWzT46U&t=743s), [12:56](https://www.youtube.com/watch?v=VWXZUWzT46U&t=776s), [13:59](https://www.youtube.com/watch?v=VWXZUWzT46U&t=839s)
6. **READ COMMITTED:** A updates CR9 → CR10 without committing; B still reads CR9. After A commits, B reads CR10. He claims B "has to wait" for A, so performance is poor. [14:31](https://www.youtube.com/watch?v=VWXZUWzT46U&t=871s), [15:39](https://www.youtube.com/watch?v=VWXZUWzT46U&t=939s), [16:11](https://www.youtube.com/watch?v=VWXZUWzT46U&t=971s), [16:45](https://www.youtube.com/watch?v=VWXZUWzT46U&t=1005s) *(wrong; see the corrections)*
7. **REPEATABLE READ:** A changes CR10 → CR11 and commits; B, inside its own still-open transaction, keeps reading **CR10** until B ends its transaction. That's the difference from READ COMMITTED, and it's the MySQL default. [17:16](https://www.youtube.com/watch?v=VWXZUWzT46U&t=1036s), [18:17](https://www.youtube.com/watch?v=VWXZUWzT46U&t=1097s), [18:54](https://www.youtube.com/watch?v=VWXZUWzT46U&t=1134s), [24:45](https://www.youtube.com/watch?v=VWXZUWzT46U&t=1485s)
8. **SERIALIZABLE:** while A has an uncommitted UPDATE, B's plain SELECT **blocks** (the "spinner") until A commits, then returns CR12/CR15. Two concurrent UPDATEs also block. Strongest and slowest. He says it takes a **table-level lock** and is "like a mutex". [19:27](https://www.youtube.com/watch?v=VWXZUWzT46U&t=1167s), [19:57](https://www.youtube.com/watch?v=VWXZUWzT46U&t=1197s), [22:03](https://www.youtube.com/watch?v=VWXZUWzT46U&t=1323s), [23:07](https://www.youtube.com/watch?v=VWXZUWzT46U&t=1387s), [23:41](https://www.youtube.com/watch?v=VWXZUWzT46U&t=1421s) *(the table-lock part is wrong; see the corrections)*
9. **Trade-off:** many projects skip SERIALIZABLE for performance; the next video covers locking reads for high concurrency. [24:12](https://www.youtube.com/watch?v=VWXZUWzT46U&t=1452s), [25:15](https://www.youtube.com/watch?v=VWXZUWzT46U&t=1515s)

## Corrections (checked against the MySQL 8.4 manual)
- **READ COMMITTED readers don't wait.** In InnoDB, a plain SELECT is a *consistent nonlocking read*: under READ COMMITTED each SELECT reads a **fresh snapshot of the last committed data** (via MVCC/undo logs), so B gets CR9 **immediately**, not after waiting for A. Only locking reads (`FOR UPDATE/SHARE`) and writes wait on A's row lock. READ COMMITTED is generally *faster* than REPEATABLE READ (fewer gap locks). ([InnoDB isolation levels](https://dev.mysql.com/doc/refman/8.4/en/innodb-transaction-isolation-levels.html), [Consistent nonlocking reads](https://dev.mysql.com/doc/refman/8.4/en/innodb-consistent-read.html))
- **SERIALIZABLE doesn't take a table lock in InnoDB.** It's REPEATABLE READ plus: with autocommit off, every plain SELECT is turned into `SELECT … FOR SHARE`. B blocked because its shared **row** lock conflicted with A's exclusive row lock, not because of a table lock. Unrelated rows still run in parallel.
- **REPEATABLE READ's snapshot is for SELECTs only.** UPDATE/DELETE in InnoDB act on the **latest committed** row, not the snapshot, which is how a [[Lost Update]] can still happen in MySQL REPEATABLE READ with app-side read-modify-write (see [[GLqyIqWtRiA]]).
- The demos show dirty reads and non-repeatable reads but **no phantom or write-skew demo**. For the full anomaly table, MySQL vs PostgreSQL, see [[Isolation levels and anomalies (Postgres vs MySQL)]].

## How it maps to the learning focus
- **Core focus:** isolation levels, dirty and non-repeatable reads, locking vs MVCC, the cost of stronger isolation.
- **QA angle:** this two-terminal demo *is* a test technique. Reproduce concurrency bugs by hand with two DB sessions (or two threads with a latch) and step through statements in a set order. Write the sequence down as a test case: "T1 BEGIN; T1 UPDATE; T2 SELECT → expect X; T1 COMMIT; T2 SELECT → expect Y".
- **Spring Boot:** `@Transactional(isolation = Isolation.READ_COMMITTED)`; note that MySQL's default is REPEATABLE READ and Postgres's is READ COMMITTED, so the same code behaves differently. **Go:** `db.BeginTx(ctx, &sql.TxOptions{Isolation: sql.LevelRepeatableRead})`.

## Related
[[Isolation Level]] · [[Dirty Read]] · [[Non-repeatable Read]] · [[MVCC]] · [[Savepoint]] · [[GLqyIqWtRiA]] · [[Isolation levels and anomalies (Postgres vs MySQL)]] · [[Module 1 - Messaging and Transactions]]

---
## Flash cards section
What's a dirty read and which level allows it?::Reading another transaction's uncommitted change (which may be rolled back). Allowed only at READ UNCOMMITTED (and Postgres doesn't allow it even there).
READ COMMITTED vs REPEATABLE READ in InnoDB?::RC: each SELECT sees a fresh committed snapshot. RR (the MySQL default): all plain SELECTs in a transaction see the snapshot from the first read.
Does a READ COMMITTED SELECT wait for another transaction's uncommitted update in InnoDB?::No. It reads the last committed version via MVCC. Only locking reads and writes wait for the row lock.
How does InnoDB implement SERIALIZABLE?::Like REPEATABLE READ, but plain SELECTs become SELECT ... FOR SHARE when autocommit is off, so reads take shared row locks and block conflicting writers.
What does SAVEPOINT / ROLLBACK TO do?::Undoes only the statements after the savepoint, keeping the rest of the transaction open.
