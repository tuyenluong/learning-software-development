---
Creation_date: 2026-10-21 15:33
Modification_date: Wednesday 21st October 2026 15:40:14
Indexes:
  - "[[literature_notes]]"
  - "[[anonystick]]"
  - "[[Transactions_and_Concurrency]]"
  - "[[Java_Spring]]"
Source: https://www.youtube.com/watch?v=9kpISaXHBvM
Author: anonystick (Tips Javascript)
Language: Vietnamese
Video_id: 9kpISaXHBvM
---

----
# Why do banking jobs always ask senior backend developers how to detect and fix deadlocks in multithreaded code?

**Video:** https://www.youtube.com/watch?v=9kpISaXHBvM (16:27, ~Jun 2026, ~4.7K views)
**Credit:** [anonystick on YouTube](https://www.youtube.com/@anonystick). Written from Vietnamese auto-captions. "GPS" = `jps`, "J stack" = `jstack`, "dump trick" = thread dump, "retain lock" = `ReentrantLock`.

## What it teaches
An interview-style walkthrough of a Java [[Deadlock]] (*khóa chết*), set against a bank job ad that asks for 1000–2000 concurrent transactions. It covers why deadlocks happen, how to **find** one in production, and how to **fix** it. The example: two archers, one holding the bow and waiting for the arrow, the other holding the arrow and waiting for the bow.

## Key concepts and steps
1. **What interviewers want:** (a) the conditions for a deadlock, (b) how you'd detect it and find the line and lock id, (c) how you'd prevent it. [01:02](https://www.youtube.com/watch?v=9kpISaXHBvM&t=62s), [01:34](https://www.youtube.com/watch?v=9kpISaXHBvM&t=94s)
2. **Conditions he names:** mutual exclusion (*loại trừ lẫn nhau*), where only one thread holds a lock; and **hold and wait**, where a thread holds one lock and asks for another. [02:37](https://www.youtube.com/watch?v=9kpISaXHBvM&t=157s), [03:09](https://www.youtube.com/watch?v=9kpISaXHBvM&t=189s). Later he also uses "no preemption" and the circular wait (see the fixes below). The full Coffman list is: mutual exclusion, hold-and-wait, no preemption, circular wait.
3. **Production symptoms:** traffic keeps coming in but nothing responds, and **CPU is LOW** because the threads are blocked, not working. High CPU usually points somewhere else, often the DB. Dashboards like Grafana/Prometheus show it. [03:40](https://www.youtube.com/watch?v=9kpISaXHBvM&t=220s), [04:10](https://www.youtube.com/watch?v=9kpISaXHBvM&t=250s), [04:40](https://www.youtube.com/watch?v=9kpISaXHBvM&t=280s)
4. **Repro:** archer 1 locks the bow, sleeps 100 ms, then wants the arrow; archer 2 locks the arrow and wants the bow, so both hang forever. [05:41](https://www.youtube.com/watch?v=9kpISaXHBvM&t=341s)
5. **Detection, option 1:** IntelliJ IDEA's thread-dump (camera) button shows both threads in red, the lock ids (e.g. 7048 / 7038) and the source lines (line 16, …). [06:13](https://www.youtube.com/watch?v=9kpISaXHBvM&t=373s), [06:44](https://www.youtube.com/watch?v=9kpISaXHBvM&t=404s), [07:16](https://www.youtube.com/watch?v=9kpISaXHBvM&t=436s)
6. **Detection, option 2 (no IDE):** `jps -l` to find the Java PID, then `jstack <pid>`, which reports the deadlock with the same threads, lines and lock ids. JConsole and Grafana alerts are also options. [07:49](https://www.youtube.com/watch?v=9kpISaXHBvM&t=469s), [08:21](https://www.youtube.com/watch?v=9kpISaXHBvM&t=501s), [08:54](https://www.youtube.com/watch?v=9kpISaXHBvM&t=534s), [09:24](https://www.youtube.com/watch?v=9kpISaXHBvM&t=564s)
7. **Fix 1, [[Lock Ordering]]:** every thread takes locks in the same global order, which breaks the circular wait. For objects without an id, order them by `System.identityHashCode`/`hashCode` and lock the smaller one first. [09:55](https://www.youtube.com/watch?v=9kpISaXHBvM&t=595s), [10:56](https://www.youtube.com/watch?v=9kpISaXHBvM&t=656s), [11:29](https://www.youtube.com/watch?v=9kpISaXHBvM&t=689s)
8. **Fix 2, [[ReentrantLock]] `tryLock` with a timeout:** if a thread can't get the second lock in time, it releases what it holds and tries again. This breaks "hold forever". He recommends it most. [12:34](https://www.youtube.com/watch?v=9kpISaXHBvM&t=754s), [13:06](https://www.youtube.com/watch?v=9kpISaXHBvM&t=786s), [13:37](https://www.youtube.com/watch?v=9kpISaXHBvM&t=817s)
9. **Follow-up interview questions:** DB deadlocks (see his MySQL deadlock video); deadlock vs [[Livelock]] (with livelock the threads aren't blocked but keep retrying and failing, e.g. each politely giving way to the other); and the fact that `synchronized` can't detect deadlocks *(correction: misleading. `jstack` and `ThreadMXBean.findDeadlockedThreads()` detect deadlocks on `synchronized` monitors too. The real limitation is that a thread waiting to enter `synchronized` can't time out or be interrupted, which is why `ReentrantLock.tryLock(timeout)` / `lockInterruptibly()` help)*. [14:42](https://www.youtube.com/watch?v=9kpISaXHBvM&t=882s), [15:12](https://www.youtube.com/watch?v=9kpISaXHBvM&t=912s), [15:44](https://www.youtube.com/watch?v=9kpISaXHBvM&t=944s)

## Commands / tools
`jps -l`, `jstack <pid>`, IntelliJ thread dump, JConsole, Prometheus + Grafana; `java.util.concurrent.locks.ReentrantLock#tryLock(timeout, unit)`.

## Edge cases / pitfalls
- `hashCode` ordering can **tie**. The textbook fix adds a tie-breaker lock (Goetz, *Java Concurrency in Practice*). He hints at this with "and hash table, research it yourself" (my clarification).
- `tryLock` retries with no backoff or jitter can turn a deadlock into a **livelock**, which is exactly his follow-up question.
- The same idea applies in the **database**. Two transactions updating rows A→B and B→A deadlock, and InnoDB kills one. Consistent update order is the fix there too (see his "Section 116: When do DEADLOCKS happen" video, JDCbKBhmrC4).

## How it connects to the core topics
- **Transaction problems:** lock ordering is also how you avoid DB deadlocks in money transfers (always lock the lower account id first).
- **QA angle:** a deadlock shows up as a timeout with low CPU. Under load tests, watch for "requests piling up, CPU flat". Grab a `jstack` (or `kill -3`) during the hang and attach it to the bug report. To reproduce, run two concurrent transfers in opposite directions in a loop.
- **Backend:** Spring `@Transactional` methods that update two aggregates in different orders; in Go, the runtime reports "all goroutines are asleep – deadlock!" only when *every* goroutine is blocked.

## Related
[[Deadlock]] · [[Livelock]] · [[Lock Ordering]] · [[ReentrantLock]] · [[Race Condition]] · [[Pessimistic Locking]]

---
## Flash cards section
What are the four Coffman conditions for a deadlock?::Mutual exclusion, hold and wait, no preemption, circular wait.
Production symptom that points to a deadlock rather than overload?::Requests keep arriving but none complete, while CPU stays low because threads are blocked, not working.
How do you find a Java deadlock without an IDE?::Run `jps -l` to get the PID, then `jstack <pid>`. It reports the deadlocked threads, the locks they hold and wait on, and the source lines.
Simplest fix for a two-lock deadlock?::Always take locks in the same global order (e.g. by id, or identityHashCode with a tie-breaker).
How does ReentrantLock.tryLock(timeout) help?::A thread that can't get the next lock in time releases what it holds and retries, which breaks hold-and-wait / no-preemption.
Deadlock vs livelock?::Deadlock: threads are blocked forever. Livelock: threads keep running and retrying but never make progress.
