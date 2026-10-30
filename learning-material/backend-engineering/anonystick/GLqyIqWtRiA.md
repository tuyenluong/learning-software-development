---
Creation_date: 2026-10-21 15:33
Modification_date: Wednesday 21st October 2026 15:51:01
Indexes:
  - "[[literature_notes]]"
  - "[[anonystick]]"
  - "[[Transactions_and_Concurrency]]"
  - "[[Databases]]"
Source: https://www.youtube.com/watch?v=GLqyIqWtRiA
Author: anonystick (Tips Javascript)
Language: Vietnamese
Video_id: GLqyIqWtRiA
---

----
# How senior devs explain and handle high concurrency: Race condition | MySQL ACID

**Video:** https://www.youtube.com/watch?v=GLqyIqWtRiA (18:51, ~Mar 2026, ~10K views)
**Credit:** [anonystick on YouTube](https://www.youtube.com/@anonystick). Written from Vietnamese auto-captions. The first ~2.5 minutes are career talk about layoffs at 35–40 and aren't covered here. [00:00](https://www.youtube.com/watch?v=GLqyIqWtRiA&t=0s)

## What it teaches
A viewer asked about a system with **500–1000 concurrent requests**: do you really need Redis+Lua, distributed locks or MQ to stop overselling stock? The answer is **no**. Plain MySQL done right is enough at that scale ("don't use a buffalo knife to kill a chicken", *dao mổ trâu giết gà*). The video works through levels 1 → 2 for stock deduction (*trừ tồn kho*).

## Key concepts and steps
1. **Level 1, read-check-write:** read the stock, compare it with the quantity, then deduct, create the order and so on. This is **not atomic** (*tính nguyên tử*), because it's two separate operations. [05:14](https://www.youtube.com/watch?v=GLqyIqWtRiA&t=314s), [05:46](https://www.youtube.com/watch?v=GLqyIqWtRiA&t=346s)
2. **[[Consistency]] (*tính nhất quán*):** all copies show the same value. **Weak consistency** is OK for Facebook likes (998 shown vs 1000 real). **Strong consistency** is required for stock, otherwise you oversell and lose money. [06:19](https://www.youtube.com/watch?v=GLqyIqWtRiA&t=379s), [07:24](https://www.youtube.com/watch?v=GLqyIqWtRiA&t=444s), [07:58](https://www.youtube.com/watch?v=GLqyIqWtRiA&t=478s)
3. **The viewer's code uses `SELECT ... FOR UPDATE`.** That's a row lock: only one connection reads and modifies the row at a time, so it **is correct** for a few hundred connections. [09:00](https://www.youtube.com/watch?v=GLqyIqWtRiA&t=540s), [09:30](https://www.youtube.com/watch?v=GLqyIqWtRiA&t=570s)
4. **Common misconception:** "it's inside a transaction, so it's safe." Wrong. MySQL's default [[Isolation Level]] is REPEATABLE READ, and plain SELECTs don't lock. Each transaction belongs to its own connection, so two transactions can read the same stock at once, which is a [[Race Condition]]. [09:30](https://www.youtube.com/watch?v=GLqyIqWtRiA&t=570s), [10:02](https://www.youtube.com/watch?v=GLqyIqWtRiA&t=602s), [10:34](https://www.youtube.com/watch?v=GLqyIqWtRiA&t=634s), [11:05](https://www.youtube.com/watch?v=GLqyIqWtRiA&t=665s)
5. **Level 2, a single [[Atomic Update]]:** merge the read and the write into one conditional statement and let InnoDB's row lock do the work:
   `UPDATE product SET stock = stock - :qty WHERE id = :id AND stock >= :qty;` and check affected rows (0 means out of stock). [12:06](https://www.youtube.com/watch?v=GLqyIqWtRiA&t=726s), [12:38](https://www.youtube.com/watch?v=GLqyIqWtRiA&t=758s), [13:12](https://www.youtube.com/watch?v=GLqyIqWtRiA&t=792s), [13:43](https://www.youtube.com/watch?v=GLqyIqWtRiA&t=823s)
   He says this is optimal for systems doing tens to hundreds of QPS, and needs no `FOR UPDATE` and no extra locking. [14:15](https://www.youtube.com/watch?v=GLqyIqWtRiA&t=855s)
6. **[[Optimistic Locking]] with a `version` column:** `UPDATE ... SET stock=stock-:qty, version=version+1 WHERE id=:id AND version=:v`. Reads don't block, and on a conflict the losers get 0 rows and retry. [15:20](https://www.youtube.com/watch?v=GLqyIqWtRiA&t=920s), [16:24](https://www.youtube.com/watch?v=GLqyIqWtRiA&t=984s), [16:56](https://www.youtube.com/watch?v=GLqyIqWtRiA&t=1016s)
7. **Where it stops scaling:** under heavy contention, both approaches pile up waiting and retrying requests, and CPU spikes. The next levels are cache (Redis) and Kafka/MQ, covered in other videos. [17:29](https://www.youtube.com/watch?v=GLqyIqWtRiA&t=1049s), [17:59](https://www.youtube.com/watch?v=GLqyIqWtRiA&t=1079s)
8. He announces a new **Spring Boot 4.0** series for Java beginners. [18:32](https://www.youtube.com/watch?v=GLqyIqWtRiA&t=1112s)

## PostgreSQL version of the same story (added after review; not in the video)
- **Different default:** PostgreSQL defaults to **READ COMMITTED**, not REPEATABLE READ. Each statement sees a fresh snapshot, so read-check-write in the app is still a race (two transactions both read `stock = 1`, both write `0`, two orders). The name for this bug is a **[[Lost Update]]**: the second write overwrites the first without seeing it.
- **The single conditional UPDATE is still safe in Postgres.** If another transaction has already updated the row, the second `UPDATE ... WHERE id = :id AND stock >= :qty` **waits** for the row lock, then **re-evaluates the WHERE clause against the newly committed row**. If the stock is now too low, it matches 0 rows. That's why the level-2 fix works on both databases.
- At Postgres **REPEATABLE READ** or **SERIALIZABLE**, the same conflict doesn't wait-and-recheck. The second transaction fails with `ERROR: could not serialize access due to concurrent update` (SQLSTATE 40001), and the app must **retry the whole transaction**.
- Source: [PostgreSQL docs, 13.2 Transaction Isolation](https://www.postgresql.org/docs/current/transaction-iso.html). For the full anomaly-by-level comparison see [[Isolation levels and anomalies (Postgres vs MySQL)]].

## Code / tools
DDD ticket project (application / controller / domain / infrastructure / start); MySQL InnoDB; `SELECT ... FOR UPDATE`; conditional `UPDATE ... WHERE stock >= qty`; a version column.

## Edge cases / pitfalls
- "In a transaction" ≠ "safe from races". Isolation level and locking reads decide that.
- Always check **affected rows**. Ignoring 0 rows means oversold or phantom orders.
- An optimistic lock with retries under a hot item can cause a retry storm and high CPU. Bound the retries.
- The atomic UPDATE only protects the **stock row**. The order insert, payment and so on still need to sit in the same DB transaction, or be compensated (see [[Saga Pattern]]).
- He calls the `version` approach "optimistic" and the single conditional UPDATE "update using optimistic" too. Strictly speaking, the single UPDATE relies on InnoDB's implicit row lock (a *pessimistic* lock held only for that statement) (my clarification).

## How it connects to the core topics
- **Transaction problems:** isolation levels, lost updates, read-check-write races, atomic conditional updates. This is the foundation for the idempotency and outbox notes.
- **QA angle:** seed stock = 5, fire 50 concurrent buy-1 requests, then assert stock == 0, orders == 5 and no negative stock. Repeat with `qty` > 1 and mixed quantities. That's an easy, high-value test to add to an API suite.
- **Spring Boot:** `@Modifying @Query("update Product p set p.stock = p.stock - :q where p.id = :id and p.stock >= :q")` and check the returned int; JPA `@Version` for optimistic locking. **Go:** `res, _ := db.Exec(...)` then `res.RowsAffected()`.

## Related
[[Race Condition]] · [[Atomic Update]] · [[Optimistic Locking]] · [[Pessimistic Locking]] · [[Isolation Level]] · [[ACID]]

---
## Flash cards section
Why is read-check-write stock deduction unsafe under concurrency?::It's two operations, so two requests can read the same stock before either writes. That's a race condition and you oversell.
Does wrapping read-check-write in a transaction prevent the race in MySQL by default?::No. With REPEATABLE READ, plain SELECTs don't lock, so concurrent transactions can read the same value.
Write a single atomic stock-deduction statement.::UPDATE product SET stock = stock - :qty WHERE id = :id AND stock >= :qty, and treat 0 affected rows as out of stock.
What is the read-check-write overselling bug called?::A lost update: two transactions read the same value and the later write overwrites the earlier one.
Is UPDATE ... SET stock = stock - :q WHERE id = :id AND stock >= :q safe under PostgreSQL's default READ COMMITTED?::Yes. A concurrent updater waits for the row lock, then re-checks the WHERE against the committed row, so it updates 0 rows if stock ran out.
Downside of optimistic locking under heavy contention?::Many requests conflict and retry, which wastes CPU and can turn into a retry storm.
