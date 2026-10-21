---
Creation_date: 2026-10-21 16:00
Modification_date: Wednesday 21st October 2026 16:00:00
Indexes:
  - "[[literature_notes]]"
  - "[[anonystick]]"
  - "[[Message_Queues]]"
Source: https://www.youtube.com/watch?v=DQRj7I3PcuM
Author: anonystick (Tips Javascript)
Language: Vietnamese
Video_id: DQRj7I3PcuM
---

----
# When exactly should I use a message queue? (Series RabbitMQ + Node.js)

**Video:** https://www.youtube.com/watch?v=DQRj7I3PcuM (23:57, ~2022, ~58K views, the channel's most-watched MQ video)
**Credit:** [anonystick on YouTube](https://www.youtube.com/@anonystick). Written from Vietnamese auto-captions, which are rough here ("remix MQ"/"repe Q" = RabbitMQ, "kfk"/"KFC"/"cáp ca" = Kafka). The captions have a gap from about 02:30 to 03:30. The last ~4 minutes are career advice.

## What it teaches
The **foundation lesson** of the MQ series. It's built around three interview questions: (1) Why use a [[Message Queue]]? (2) What are its pros and cons? (3) When would you pick [[RabbitMQ]], [[Kafka]], ActiveMQ or RocketMQ? [01:04](https://www.youtube.com/watch?v=DQRj7I3PcuM&t=64s), [01:37](https://www.youtube.com/watch?v=DQRj7I3PcuM&t=97s)

## Key concepts and steps
The example is a bánh mì shop (*tiệm bánh mì*) with customers CR7 and Messi.
1. **Don't use MQ just because it's on your CV.** Interviewers want to know *why* you used it. Each broker has strengths, so learn two well (Kafka + RabbitMQ). [02:08](https://www.youtube.com/watch?v=DQRj7I3PcuM&t=128s), [04:05](https://www.youtube.com/watch?v=DQRj7I3PcuM&t=245s)
2. **Benefit 1, [[Decoupling]] (*tách*):** the shop delivers bread to *one* place (the broker), and whoever wants it subscribes. Adding or removing a consumer doesn't change the producer. [05:11](https://www.youtube.com/watch?v=DQRj7I3PcuM&t=311s), [05:46](https://www.youtube.com/watch?v=DQRj7I3PcuM&t=346s), [06:18](https://www.youtube.com/watch?v=DQRj7I3PcuM&t=378s)
3. **Benefit 2, [[Asynchronous Processing]] (*không đồng bộ*):** after an order, send mail (200 ms), add loyalty points (400 ms) and update rankings (300 ms). Done synchronously, that's ~1000 ms per order. Publish the event and return in ~100 ms, and the side tasks run afterwards. [06:52](https://www.youtube.com/watch?v=DQRj7I3PcuM&t=412s), [07:22](https://www.youtube.com/watch?v=DQRj7I3PcuM&t=442s), [07:57](https://www.youtube.com/watch?v=DQRj7I3PcuM&t=477s)
4. **Benefit 3, [[Peak Shaving]] / load levelling (*cắt đỉnh*):** normally 50 req/s, but a 13:00 promo spikes to 5000 req/s while MySQL handles ~2000 req/s. Put the requests in a queue and consumers *pull* 2000/s, so the system never falls over. The backlog drains after the peak. And for a limited promo (2000 items), the extra requests don't matter for the business anyway. [09:00](https://www.youtube.com/watch?v=DQRj7I3PcuM&t=540s), [10:09](https://www.youtube.com/watch?v=DQRj7I3PcuM&t=609s), [11:26](https://www.youtube.com/watch?v=DQRj7I3PcuM&t=686s), [12:32](https://www.youtube.com/watch?v=DQRj7I3PcuM&t=752s), [13:35](https://www.youtube.com/watch?v=DQRj7I3PcuM&t=815s)
5. **Drawbacks:** (a) more system complexity; (b) messages can be **lost** (*mất tin nhắn*), which is a real headache; (c) **consistency** problems between services. [14:40](https://www.youtube.com/watch?v=DQRj7I3PcuM&t=880s), [15:12](https://www.youtube.com/watch?v=DQRj7I3PcuM&t=912s), [15:46](https://www.youtube.com/watch?v=DQRj7I3PcuM&t=946s)
6. **Comparison (from memory, rough):** RabbitMQ handles ~10K msg/s per node, an order of magnitude below Kafka, with very low (sub-millisecond-class) latency, high availability and reliable delivery. Kafka has the highest throughput and a strong distributed design, with latency in milliseconds. Learn ActiveMQ / RabbitMQ / RocketMQ / Kafka. [16:59](https://www.youtube.com/watch?v=DQRj7I3PcuM&t=1019s), [17:31](https://www.youtube.com/watch?v=DQRj7I3PcuM&t=1051s), [18:10](https://www.youtube.com/watch?v=DQRj7I3PcuM&t=1090s)
7. Next in the series: RabbitMQ exchange types (direct, fanout, topic, headers). [19:19](https://www.youtube.com/watch?v=DQRj7I3PcuM&t=1159s)

## Edge cases / pitfalls
- The numbers (10K/s, latency) are rough 2022-era figures quoted without a source. Treat them as orders of magnitude, not benchmarks.
- Peak shaving moves the problem into **[[Consumer Lag]] / backlog**. You need queue-depth monitoring and a business answer for "how stale is OK?"
- "Return 100 ms then process later" means the user sees *accepted*, not *done*. The UI and API need a pending state and a way to report a later failure.
- His drawback (b), message loss, is the subject of RabbitMQ (4) on acks, durable and persistent ([[az2VNMgNFrk]]). Drawback (c) leads to outbox and saga ([[DQN0pRV8RnU]]).

## How it maps to the learning focus
- **Messaging foundations:** this is the "why" before Jacob's lessons on lost, duplicate and out-of-order messages.
- **QA angle:** async flows need different tests. Poll or await eventual state (Playwright `expect.poll`, Awaitility in Java), test the *pending* state, load-test the spike and watch queue depth and drain time, and kill a consumer during the spike.
- **Architecture:** you can only explain a broker choice through tradeoffs (throughput vs latency vs routing flexibility vs replay).

## Related
[[Message Queue]] · [[RabbitMQ]] · [[Kafka]] · [[Decoupling]] · [[Peak Shaving]] · [[Consumer Lag]] · [[az2VNMgNFrk]] · [[hrSP7UocdJ8]]

---
## Flash cards section
Three classic reasons to introduce a message queue?::Decoupling producers from consumers, asynchronous processing (faster responses), and peak shaving / load levelling.
How does a queue protect a DB that handles 2000 req/s from a 5000 req/s spike?::Requests are buffered, and consumers pull at most what the DB can handle. The backlog drains after the peak.
Three drawbacks of adding an MQ?::More system complexity, possible message loss, and data consistency problems across services.
What should you test differently once a flow becomes asynchronous?::Eventual results (poll/await), the pending state, failures reported later, backlog/lag under load, and consumer crashes.
