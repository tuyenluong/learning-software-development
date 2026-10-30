---
Creation_date: 2026-10-21 15:30
Modification_date: Wednesday 21st October 2026 15:40:14
Indexes:
  - "[[literature_notes]]"
  - "[[anonystick]]"
  - "[[Kafka]]"
  - "[[Message_Queues]]"
Source: https://www.youtube.com/watch?v=aJ5kLfn8AtI
Author: anonystick (Tips Java / Tips Javascript)
Language: Vietnamese
Video_id: aJ5kLfn8AtI
---

----
# Kafka (10): Kafka 4.0 Queues, Share Groups & critical notes

**Video:** https://www.youtube.com/watch?v=aJ5kLfn8AtI (15:06, uploaded ~Oct 2026, the channel's newest video)
**Credit:** [anonystick on YouTube](https://www.youtube.com/@anonystick). Study note written in English from Vietnamese auto-captions. Captions mangle names a lot ("KFK", "KK" = Kafka, "Rebic MQ"/"RMQ" = RabbitMQ, "S group"/"xe group" = share group). Parts marked *(unclear)* couldn't be read reliably.

## What it teaches
Kafka 4.0 adds [[Share Groups]] (KIP-932, "Queues for Kafka"), an early-access feature. With it, many consumers can work on one [[Kafka Partition]] together, the way a [[RabbitMQ]] or [[Amazon SQS]] queue works. The author's main point is that Kafka is still a [[Commit Log]] underneath. Acknowledging a message in a share group does **not** delete it.

## Key concepts and steps
1. **Classic queue vs Kafka.** In RabbitMQ/SQS, consumers take whichever message is next, "whoever's free grabs the work" (*ai rảnh thì nhào vô lấy*). A processed message disappears from the queue. [00:31](https://www.youtube.com/watch?v=aJ5kLfn8AtI&t=31s), [01:01](https://www.youtube.com/watch?v=aJ5kLfn8AtI&t=61s)
2. **Classic [[Consumer Group]] rule:** inside one group, each partition goes to exactly one consumer. To get 10-way parallelism you need 10 partitions. With 3 partitions and 5 consumers, 2 consumers sit idle. [01:34](https://www.youtube.com/watch?v=aJ5kLfn8AtI&t=94s), [02:08](https://www.youtube.com/watch?v=aJ5kLfn8AtI&t=128s)
3. **Demo setup.** He runs a single-broker Kafka cluster in Docker with the share-group feature switched on (it shows an "early access, not for production" warning). He creates a topic with **1 partition** and **replication factor 1** to cut out noise. [03:14](https://www.youtube.com/watch?v=aJ5kLfn8AtI&t=194s), [03:44](https://www.youtube.com/watch?v=aJ5kLfn8AtI&t=224s)
4. **Classic group on 1 partition:** he sends messages 1..10, and consumer 1 gets all of them while consumer 2 gets nothing. [04:44](https://www.youtube.com/watch?v=aJ5kLfn8AtI&t=284s), [05:24](https://www.youtube.com/watch?v=aJ5kLfn8AtI&t=324s)
5. **Share group on the same setup:** using the share consumer (`kafka-console-share-consumer`), both consumers receive messages and the work is split between them, even though there's still only one partition. [05:57](https://www.youtube.com/watch?v=aJ5kLfn8AtI&t=357s), [06:30](https://www.youtube.com/watch?v=aJ5kLfn8AtI&t=390s)
6. **Is the message deleted after ack? No.** Kafka keeps acknowledgement state in an internal topic, `__share_group_state`. He reads it and finds the record's delivery state = 2, which he takes to mean "acknowledged" (he says there are about five states, 0–4; *(unclear, the exact numbering isn't clearly stated)*). [09:39](https://www.youtube.com/watch?v=aJ5kLfn8AtI&t=579s), [10:09](https://www.youtube.com/watch?v=aJ5kLfn8AtI&t=609s), [10:45](https://www.youtube.com/watch?v=aJ5kLfn8AtI&t=645s)
7. **Proof:** reading the topic again with a brand-new consumer group still returns "Hello Kafka". The log is append-only. Ack state is just "a note in the margin, not a torn-out page", and data only goes away through retention settings. [11:18](https://www.youtube.com/watch?v=aJ5kLfn8AtI&t=678s), [11:49](https://www.youtube.com/watch?v=aJ5kLfn8AtI&t=709s)
8. **Lock timeout ≈ SQS [[Visibility Timeout]]:** if a share consumer takes a record and hangs, after about 30 s Kafka hands the record to another consumer. His summary is that share groups combine RabbitMQ's queue model with SQS's visibility timeout. [12:50](https://www.youtube.com/watch?v=aJ5kLfn8AtI&t=770s), [13:22](https://www.youtube.com/watch?v=aJ5kLfn8AtI&t=802s)
9. **Open question for the next video:** Kafka still has no native [[Dead Letter Queue]] like RabbitMQ (*hàng đợi thư chết*). [14:23](https://www.youtube.com/watch?v=aJ5kLfn8AtI&t=863s)

## Tools / commands mentioned
- Kafka cluster in Docker with the share-group feature flag enabled (he offers the config to channel members).
- `kafka-topics` with `--partitions 1 --replication-factor 1`; `kafka-console-consumer --group classic-demo`; the share-consumer console tool; reading the internal `__share_group_state` topic.

## Edge cases / pitfalls
- In Kafka 4.0, share groups are **early access, not for production**. **Status update (checked 2026-10-21):** they were a preview in 4.1 (per [Conduktor's summary](https://www.conduktor.io/glossary/kafka-share-groups)) and are **production-ready (GA) in Kafka 4.2** ([Kafka 4.2 upgrade notes](https://kafka.apache.org/42/getting-started/upgrade/), [4.2.0 release announcement](https://kafka.apache.org/blog/2026/02/17/apache-kafka-4.2.0-release-announcement/)). Use 4.2.1 or later: per the upgrade notes, 4.2.1 fixes a critical deadlock in the share-group path (KAFKA-20505). The current release line is 4.3. The video's 4.0 demo flags and warnings are out of date.
- A share group gives up **per-partition ordering**, because records from one partition are processed by several consumers at once. It's a different guarantee from a classic group (my addition, implied by the demo).
- Lock timeout means **redelivery**: a slow consumer, not only a crashed one, can cause the same record to be processed twice, so consumers still need to be [[Idempotent Consumer]]s (my addition).
- No DLQ yet. Per KIP-932, records that keep failing are retried up to a delivery-count limit and then archived, so poison messages can be dropped quietly (my addition, verify on the current docs).

## How it connects to the core topics
- **Messaging problems:** at-least-once delivery, redelivery after a timeout, poison messages and DLQs, consumer scaling vs partition count, [[Consumer Lag]].
- **QA angle:** to test a share-group consumer, kill or freeze a consumer mid-message and check the record is redelivered and processed exactly once *in effect*. Also check ordering assumptions, since a classic group keeps order per key and a share group doesn't.
- **Backend (Spring Boot / Go):** Spring Kafka and Go clients may lag behind on share-consumer support. Check before using it.

## Related
[[Kafka]] · [[RabbitMQ]] · [[Consumer Group]] · [[Idempotent Consumer]] · [[Dead Letter Queue]]

---
## Flash cards section
In a classic Kafka consumer group, how many consumers can read one partition at a time?::Exactly one consumer per partition per group, so parallelism is capped by the partition count.
What do Kafka 4.0 share groups (KIP-932) change?::Several consumers in a share group can process records from the same partition together, like a RabbitMQ/SQS queue.
Does acknowledging a record in a share group delete it from Kafka?::No. The log is append-only. Ack state is kept separately (`__share_group_state`), and data is removed only by retention.
What happens if a share consumer takes a record and hangs?::After the acquisition lock times out (~30 s by default) the record is released and can be delivered to another consumer, like SQS's visibility timeout.
What guarantee do you lose with share groups compared with classic groups?::Per-partition ordering, because records from one partition are processed by several consumers at once.
