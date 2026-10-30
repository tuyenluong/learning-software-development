---
Creation_date: 2026-10-21 15:35
Modification_date: Wednesday 21st October 2026 15:40:14
Indexes:
  - "[[literature_notes]]"
  - "[[anonystick]]"
  - "[[Idempotency_and_Distributed_Transactions]]"
  - "[[Transactions_and_Concurrency]]"
Source: https://www.youtube.com/watch?v=inUimYVAGv0
Author: anonystick (Tips Javascript)
Language: Vietnamese
Video_id: inUimYVAGv0
---

----
# System Design: How is idempotency implemented when duplicate payments happen at the same time under high concurrency?

**Video:** https://www.youtube.com/watch?v=inUimYVAGv0 (18:31, ~Apr 2026, ~7.2K views)
**Credit:** [anonystick on YouTube](https://www.youtube.com/@anonystick). Written from Vietnamese auto-captions. "Idempotent" comes out as "indem button / item button" and "unique" as "unit". The public video stops after method 3 and says the higher-level code is members-only. [18:19](https://www.youtube.com/watch?v=inUimYVAGv0&t=1099s)

## What it teaches
What [[Idempotency]] (*tính lũy đẳng*; he also says *tính bất biến*, but that means **immutability**, a different idea) means, where duplicates come from in real systems, and three DB-level ways to stop a payment from being recorded twice. The demo uses the channel's DDD "Tết train ticket" project (*vé tàu Tết*) with VNPay.

## Key concepts and steps
1. **Definition:** f(f(x)) = f(x). However many times you send the same request, you get one result and no extra records. `DELETE` is naturally idempotent *(in **state**: the resource is gone either way. The **response** can differ: the first call may return 200/204, a repeat 404. So tests should assert on state, not the status code alone)*. [02:05](https://www.youtube.com/watch?v=inUimYVAGv0&t=125s), [03:08](https://www.youtube.com/watch?v=inUimYVAGv0&t=188s)
2. **Where duplicates come from:**
   - double-clicks, and front-end button disabling isn't enough [03:08](https://www.youtube.com/watch?v=inUimYVAGv0&t=188s)
   - backend [[Retry]] logic, and redelivery in [[RabbitMQ]]/[[Kafka]] [04:16](https://www.youtube.com/watch?v=inUimYVAGv0&t=256s)
   - payment-gateway [[Webhook]]/IPN callbacks, which keep calling until your system confirms [04:47](https://www.youtube.com/watch?v=inUimYVAGv0&t=287s)
   - client [[Timeout]]s: the request may actually have succeeded, so the client retries [05:19](https://www.youtube.com/watch?v=inUimYVAGv0&t=319s)
3. **Which DB operations are at risk:** INSERT (duplicate rows) and UPDATE with arithmetic. Example: 100 points, deduct 50 twice, now 0. [06:23](https://www.youtube.com/watch?v=inUimYVAGv0&t=383s)
4. **Demo of the bug:** order status 0 = pending, and the order is held for 15 minutes. Paying the same order twice creates payment rows #13 and #14 for one order number, a duplicate. [09:35](https://www.youtube.com/watch?v=inUimYVAGv0&t=575s), [11:17](https://www.youtube.com/watch?v=inUimYVAGv0&t=677s)
5. **Method 1, check-then-insert (junior level):** check the order exists, check status == 0, then insert. This fails under concurrency because several threads pass the check in the same instant. It's a [[Race Condition]]. [11:47](https://www.youtube.com/watch?v=inUimYVAGv0&t=707s), [12:54](https://www.youtube.com/watch?v=inUimYVAGv0&t=774s)
6. **Method 2a, [[Pessimistic Locking]] (`SELECT ... FOR UPDATE`, *khóa bi quan*):** this is correct, but it serialises requests and holds connections. 1000 waiting requests means 1000 held connections and pool exhaustion. [13:24](https://www.youtube.com/watch?v=inUimYVAGv0&t=804s), [13:54](https://www.youtube.com/watch?v=inUimYVAGv0&t=834s)
7. **Method 2b, [[Optimistic Locking]] (*khóa lạc quan*) with a `version` column:** `UPDATE ... SET amount=amount+10, version=version+1 WHERE id=? AND version=1`. Only one request matches, and the others get `affected rows = 0`. [14:24](https://www.youtube.com/watch?v=inUimYVAGv0&t=864s), [15:29](https://www.youtube.com/watch?v=inUimYVAGv0&t=929s), [16:00](https://www.youtube.com/watch?v=inUimYVAGv0&t=960s)
8. **Method 3, [[Unique Constraint]]:** add a unique key, e.g. (user_id, order_id) or the order number, on the payment-transaction table. The second insert fails with "Duplicate entry". [16:34](https://www.youtube.com/watch?v=inUimYVAGv0&t=994s), [17:48](https://www.youtube.com/watch?v=inUimYVAGv0&t=1068s)
9. He says the unique-key method "works but isn't good enough" (he doesn't say why in the public part), and the next level is members-only. [18:19](https://www.youtube.com/watch?v=inUimYVAGv0&t=1099s)

## Code / tools mentioned
- Spring Boot DDD project (application/controller/domain layers), `PaymentController.paymentOrder`, VNPay sandbox, Docker, MySQL.
- SQL: `SELECT ... FOR UPDATE`; version-based `UPDATE ... WHERE version = ?`; `ALTER TABLE payment_transaction ADD UNIQUE KEY ...`.

## Edge cases / pitfalls
- Disabling a front-end button doesn't make anything idempotent.
- A timeout doesn't mean failure. The first call may have succeeded.
- With optimistic locking, losers get `affected rows = 0`. The code must treat that as "already done", not as an error that triggers *another* retry.
- With a unique constraint, the duplicate-key exception must become an idempotent success response, not a 500 (my addition).
- Likely reasons he calls method 3 "not enough" (my inference): it only protects that one table; side effects such as a call to the payment gateway or a sent email aren't covered; and the caller needs the *original* response back. That's why systems use an [[Idempotency Key]] table that stores the response (Stripe-style). The channel has a follow-up: "How to implement Stripe's simple and effective API Idempotency" (A9gqa8q-l1w).

## How it connects to the core topics
- **Transaction problems:** race conditions, pessimistic vs optimistic locking, unique constraints as the last line of defence.
- **Messaging problems:** redelivery and retries cause duplicates. This is the same reasoning as [[Idempotent Consumer]].
- **QA angle:** fire N parallel identical payment requests (k6/JMeter, or a Playwright API test with `Promise.all`), then assert exactly one payment row and one charge. Replay the webhook. Simulate a client timeout followed by a retry.
- **Spring Boot:** `@Version` (JPA optimistic locking), `@Lock(PESSIMISTIC_WRITE)`, handling `DataIntegrityViolationException`.

## Related
[[Idempotency]] · [[Idempotency Key]] · [[Optimistic Locking]] · [[Pessimistic Locking]] · [[Race Condition]] · [[Idempotent Consumer]]

---
## Flash cards section
What is idempotency, in one line?::Doing the same operation many times has the same effect as doing it once: f(f(x)) = f(x).
Name four real sources of duplicate payment requests.::Double clicks, backend retries, MQ redelivery, gateway webhook/IPN retries, and client timeouts followed by a retry.
Why does check-then-insert fail under concurrency?::Two requests can both pass the "not paid yet" check before either inserts. That's a race condition.
Downside of SELECT ... FOR UPDATE under high load?::It serialises requests and holds DB connections while they wait, which can exhaust the connection pool.
How does optimistic locking stop a duplicate update?::UPDATE ... WHERE id=? AND version=? and bump the version. Only one request matches, and the others get 0 affected rows.
What does a unique constraint give you that app-level checks don't?::The database itself rejects the second insert, even when two requests race past the app's checks.
