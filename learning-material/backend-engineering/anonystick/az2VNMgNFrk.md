---
Creation_date: 2026-10-21 15:33
Modification_date: Wednesday 21st October 2026 15:51:01
Indexes:
  - "[[literature_notes]]"
  - "[[anonystick]]"
  - "[[Message_Queues]]"
Source: https://www.youtube.com/watch?v=az2VNMgNFrk
Author: anonystick (Tips Javascript)
Language: Vietnamese
Video_id: az2VNMgNFrk
---

----
# RabbitMQ (4): Solving reliability problems in a queue (noAck, TTL, durable, persistent)

**Video:** https://www.youtube.com/watch?v=az2VNMgNFrk (17:27, ~2023, ~12K views). Stack: Node.js + `amqplib`, RabbitMQ in Docker.
**Credit:** [anonystick on YouTube](https://www.youtube.com/@anonystick). Written from Vietnamese auto-captions, which are **poor** in this video: "acc/axit" = ack, "phone" = false, "tru/chu" = true, "đuôi bò/doreboard" = durable, "khuya/Qatar" = queue. **The captions have gaps at ~07:00–08:10 and ~10:25–11:30** (on-screen Docker demo without speech). Details in those sections are *(unclear)*.

## What it teaches
The three settings that decide whether a RabbitMQ message survives: consumer **acknowledgement**, message **[[TTL]]**, and **durable queue + persistent message**. These are the answers to "message loss", the drawback raised in the "when to use MQ" video ([[DQRj7I3PcuM]]).

## Key concepts and steps
1. **[[Message Acknowledgement]] (ack):** the consumer tells RabbitMQ "processed". Only then is the message removed from the queue. If it isn't acked, RabbitMQ keeps it and **redelivers** it, e.g. to another consumer or after a restart. [01:06](https://www.youtube.com/watch?v=az2VNMgNFrk&t=66s), [01:38](https://www.youtube.com/watch?v=az2VNMgNFrk&t=98s), [02:11](https://www.youtube.com/watch?v=az2VNMgNFrk&t=131s)
2. **Demo:** with acknowledgements not completed, "Hello 1" keeps coming back to every consumer that connects, even after restarting consumers. Once acks are on, it's consumed once and gone. [03:17](https://www.youtube.com/watch?v=az2VNMgNFrk&t=197s), [03:51](https://www.youtube.com/watch?v=az2VNMgNFrk&t=231s)
3. **Open question he raises:** what if the handler *always* fails? The message never leaves and the queue fills up. He defers this to the dead-letter video ([[hrSP7UocdJ8]]). [02:45](https://www.youtube.com/watch?v=az2VNMgNFrk&t=165s)
4. **Message [[TTL]] (expiration):** set an expiration on publish, e.g. `expiration: 10*1000` ms, and an unconsumed message disappears after 10 s. [04:53](https://www.youtube.com/watch?v=az2VNMgNFrk&t=293s), [05:28](https://www.youtube.com/watch?v=az2VNMgNFrk&t=328s), [06:31](https://www.youtube.com/watch?v=az2VNMgNFrk&t=391s)
5. **[[Durable Queue]]:** restart the RabbitMQ container and a non-durable queue and its messages are gone ("customer data we already received… lost!"). `durable: true` keeps the queue definition across a broker restart. [08:12](https://www.youtube.com/watch?v=az2VNMgNFrk&t=492s), [11:33](https://www.youtube.com/watch?v=az2VNMgNFrk&t=693s), [12:04](https://www.youtube.com/watch?v=az2VNMgNFrk&t=724s)
6. **Durable alone isn't enough.** After the restart the queue exists but holds 0 messages, because he forgot **`persistent: true`** on the message, which writes it to disk. With both set, the message survives the restart (count = 1) and is consumed afterwards. The consumer must declare the queue with the same `durable` setting. [13:41](https://www.youtube.com/watch?v=az2VNMgNFrk&t=821s), [14:12](https://www.youtube.com/watch?v=az2VNMgNFrk&t=852s), [15:13](https://www.youtube.com/watch?v=az2VNMgNFrk&t=913s), [15:47](https://www.youtube.com/watch?v=az2VNMgNFrk&t=947s)
7. **Recap:** reliability means (1) surviving broker restarts, (2) handling consumers that don't ack or keep failing, (3) TTL. Next up: publish/subscribe. [16:52](https://www.youtube.com/watch?v=az2VNMgNFrk&t=1012s)

## Code (amqplib, reconstructed, so check it against the docs)
```js
await ch.assertQueue('q2', { durable: true });
ch.sendToQueue('q2', Buffer.from(msg), { persistent: true, expiration: '10000' });
ch.consume('q2', m => { /* work */ ch.ack(m); }, { noAck: false });
```

## Edge cases / pitfalls (and clarifications)
- **The naming trap:** in amqplib, `noAck: true` means *auto-ack*. The message counts as delivered the moment it's sent, so a consumer crash **loses** it. The safe setting is `noAck: false` plus an explicit `ch.ack(m)` *after* the work. The captions blur "ack true/false", so rely on this rule rather than the wording.
- Manual ack gives **at-least-once** delivery. A crash after the work but before the ack causes a redelivery, so the consumer must be an [[Idempotent Consumer]].
- `nack` with requeue on a permanently failing message is a **poison-message loop**. Fix it with reject-to-DLX plus a retry limit ([[hrSP7UocdJ8]]).
- TTL silently **drops** messages unless a dead-letter exchange is configured.
- **Spring AMQP's `AUTO` is not amqplib's `noAck: true`** (fix from [[REVIEW-jacob-batch1|Jacob's review]], checked against the docs). Spring has three modes: `NONE` is RabbitMQ's real auto-ack (what amqplib calls `noAck: true`); `MANUAL` means you call `basicAck()`; `AUTO`, **the default**, means *the container* acks after your listener returns normally, and if the listener throws, it rejects the message. Because `defaultRequeueRejected` defaults to `true`, that rejected message is **requeued**, redelivered, fails again, and loops forever: a poison-message loop. Fixes: set `spring.rabbitmq.listener.simple.default-requeue-rejected=false` (rejected messages are dropped or go to the queue's DLX), throw `AmqpRejectAndDontRequeueException` for errors you know won't heal, or add retry with `RetryInterceptorBuilder.stateless().maxRetries(n)...recoverer(new RejectAndDontRequeueRecoverer())` (Spring Boot: `spring.rabbitmq.listener.simple.retry.enabled=true`, whose default recoverer is `RejectAndDontRequeueRecoverer`) and give the queue a DLX. Sources: [Spring AMQP container attributes (acknowledgeMode, defaultRequeueRejected)](https://docs.spring.io/spring-amqp/reference/amqp/containerAttributes.html), [Spring AMQP exception handling](https://docs.spring.io/spring-amqp/reference/amqp/exception-handling.html), [Spring AMQP retry and recoverers](https://docs.spring.io/spring-amqp/reference/amqp/resilience-recovering-from-errors-and-broker-failures.html), [Spring Boot AMQP retry](https://docs.spring.io/spring-boot/reference/messaging/amqp.html).
- **Quorum queues are always durable** and persist every message to disk regardless of delivery mode, so the "forgot `persistent: true`" trap in the demo only applies to classic queues. Since RabbitMQ 4.0 quorum queues also have a default `delivery-limit` of 20, after which a message is dropped or dead-lettered. Don't treat that as your poison-message fix, though: from RabbitMQ 4.3 only some returns count toward the limit (`basic.reject` does, `basic.nack` doesn't). Configure retry + DLX explicitly. Source: [RabbitMQ quorum queues](https://www.rabbitmq.com/docs/quorum-queues).
- Even durable + persistent can lose messages written just before a crash. Use **publisher confirms** (and quorum queues in modern RabbitMQ) for real guarantees. This isn't in the video; check the RabbitMQ reliability docs.

## How it maps to the learning focus
- **Core focus:** lost messages, at-least-once delivery, poison messages, broker restarts.
- **QA tests to design:** restart the broker mid-flow (durable/persistent check); kill the consumer before the ack (check redelivery, and no duplicate side effect); publish with a short TTL while consumers are down (check the expiry, or the DLX); a permanently failing message (check it doesn't loop forever).
- **Spring Boot:** `spring.rabbitmq.listener.simple.acknowledge-mode=none|manual|auto` (`auto` is the default and is *not* fire-and-forget; see the pitfall above), `default-requeue-rejected=false` plus `retry.enabled=true` to stop poison loops, `durable` queues via `QueueBuilder.durable()`, `MessageDeliveryMode.PERSISTENT` (the Spring default). **Go:** `amqp091-go` `ch.Consume(..., autoAck=false)` then `d.Ack(false)`.

## Related
[[RabbitMQ]] · [[Message Acknowledgement]] · [[Durable Queue]] · [[TTL]] · [[Dead Letter Queue]] · [[Idempotent Consumer]] · [[DQRj7I3PcuM]] · [[hrSP7UocdJ8]]

---
## Flash cards section
When does RabbitMQ delete a message from a queue (manual ack mode)?::Only after the consumer acks it. Unacked messages are redelivered if the consumer's channel closes.
In amqplib, does noAck:true make delivery safer?::No. noAck:true is auto-ack, so a consumer crash loses the message. Use noAck:false and ack after the work.
Why can a durable queue still come back empty after a restart?::durable only keeps the queue definition. Messages must also be published with persistent:true (delivery mode 2).
What delivery guarantee does manual ack give, and what does that require of consumers?::At-least-once, so consumers must be idempotent.
In Spring AMQP's default AUTO ack mode, what happens when the listener throws?::The container rejects the message and, because defaultRequeueRejected=true, requeues it, so a poison message loops forever unless you set default-requeue-rejected=false, use retry with RejectAndDontRequeueRecoverer, and configure a DLX.
Which Spring AMQP acknowledge mode matches amqplib noAck:true?::NONE (RabbitMQ "autoack"). AUTO means the container acks after the listener returns successfully.
