---
Creation_date: 2026-10-21 15:47
Modification_date: Wednesday 21st October 2026 15:47:35
Indexes:
  - "[[literature_notes]]"
  - "[[anonystick]]"
  - "[[Kafka]]"
Source: https://www.youtube.com/watch?v=yiXL052rNNI
Author: anonystick (Tips Javascript)
Language: Vietnamese
Video_id: yiXL052rNNI
---

----
# Kafka (05): the message-order mistake, when multi-threading a partition breaks ordering

**Video:** https://www.youtube.com/watch?v=yiXL052rNNI (6:03, ~2025, ~5.6K views). A short holiday episode that only **states the problem**. His three-level solution is in the follow-ups "Kafka (06) ONE PARTITION vs MULTI THREAD" (fZafqe9yZNI) and "Kafka (09) HASH KEY PARTITIONS" (NrM4ldZHZ2E), which look **members-only** (hidden view count), so they aren't covered.
**Credit:** [anonystick on YouTube](https://www.youtube.com/@anonystick). Written from Vietnamese auto-captions, which are poor for names: "KFK" = Kafka, "pin lock / pinlock / inlock" = binlog, "phân vùng / practition" = partition, "gooting" = goroutine, "thick / trick" = thread, "máy Queo/MyQL" = MySQL. The first 30 s is a teaser from 02:38.

## What it teaches
Why ordering matters (create order → pay → ship), how Kafka gives you order (**per partition, by key**), and the trap senior devs fall into: making a consumer faster by processing one partition's records on several threads, which silently **destroys the order**.

## Key concepts and steps
1. **Setup:** MySQL binlog changes (order, payment, shipping rows) are streamed into Kafka (CDC). Order must hold: you can't pay before the order exists, otherwise data is "messy" and a human has to fix it. [01:04](https://www.youtube.com/watch?v=yiXL052rNNI&t=64s), [01:34](https://www.youtube.com/watch?v=yiXL052rNNI&t=94s), [02:05](https://www.youtube.com/watch?v=yiXL052rNNI&t=125s)
2. **Each step takes 2 s,** so one order's flow takes 6 s if processed in sequence. Can it be 2 s and still ordered? [02:05](https://www.youtube.com/watch?v=yiXL052rNNI&t=125s), [02:38](https://www.youtube.com/watch?v=yiXL052rNNI&t=158s)
3. **Topic with 3 partitions** for throughput. To keep one order's events in sequence they must go to **one partition**, chosen by **order id** as the key. Within a partition the consumer reads in order. [02:38](https://www.youtube.com/watch?v=yiXL052rNNI&t=158s), [03:13](https://www.youtube.com/watch?v=yiXL052rNNI&t=193s), [03:43](https://www.youtube.com/watch?v=yiXL052rNNI&t=223s)
4. **The complaint:** one partition is consumed by one thread, so the 3 steps take 6 s and a powerful server sits idle. [04:16](https://www.youtube.com/watch?v=yiXL052rNNI&t=256s)
5. **The mistake:** hand the partition's records to 3 goroutines or threads (Go, or a Spring thread pool). It's fast (2 s), but the threads don't know the records are a sequence, so "payment" can finish before "create order". **Fast but wrong.** [04:48](https://www.youtube.com/watch?v=yiXL052rNNI&t=288s), [05:22](https://www.youtube.com/watch?v=yiXL052rNNI&t=322s)
6. A solution "with three levels" is promised for the next video. [05:52](https://www.youtube.com/watch?v=yiXL052rNNI&t=352s)

## Edge cases / pitfalls (and the missing solution, from docs)
- **His mapping "order 1 → partition 1, 2 → 2, 3 → 3" is a simplification.** The default partitioner hashes the key (murmur2) modulo the partition count, so you can't pick partitions by id, and **adding partitions later remaps keys**, which breaks per-key order across the change.
- **The usual fix for "parallel but ordered"** is to parallelise **across keys, not within a key**: inside one partition, route each record to a worker by `hash(order_id) % N` (each worker is a single-threaded queue), so different orders run in parallel and one order's events stay in sequence. Commit an offset only once every record before it is done. Confluent's Parallel Consumer library does this ("key-ordered" mode). Or simply add partitions and consumers.
- **Ordering can also break before the consumer:** producer retries with `enable.idempotence=false` and `max.in.flight.requests.per.connection > 1` can reorder batches. With idempotence on (the default since 3.0) order is kept for up to 5 in-flight requests ([Kafka producer configs](https://kafka.apache.org/43/configuration/producer-configs/)). Non-blocking retry topics (`@RetryableTopic`) also give up ordering. See [[Spring Kafka retries and dead-letter topics]].
- Rebalances can cause **re-delivery**, which looks like out-of-order (an old event arrives again after newer ones). Consumers should reject stale events by version. See [[Out-of-order messages and consumer rebalancing]].

## How it connects to the core topics
- **Core focus:** out-of-order messages, partition keys, consumer concurrency.
- **QA tests to design:** publish create → pay → ship for 1,000 orders interleaved, with artificial random delay per step, then assert every order's final state is "shipped" and no "paid before created" error appears in logs. Run it with consumer concurrency 1 and N. Then add a partition mid-test and watch what breaks.
- **Spring Boot:** `kafkaTemplate.send(topic, orderId, event)` (key = order id). `ConcurrentKafkaListenerContainerFactory.setConcurrency(n)` adds consumers (one per partition, which keeps order), **not** threads inside a partition; don't hand records to an `@Async` executor. **Go:** with franz-go/sarama, one goroutine per partition, or a key-hashed worker pool per partition.

## Related
[[Kafka Partition]] · [[Message Ordering]] · [[Partition Key]] · [[Out-of-order messages and consumer rebalancing]] · [[DQN0pRV8RnU]] · [[Messaging and Transactions]]

---
## Flash cards section
What ordering guarantee does Kafka give?::Order within a single partition only. Records with the same key go to the same partition (while the partition count doesn't change).
Why does processing one partition's records on several threads break ordering?::The threads run concurrently, so a later record (payment) can finish before an earlier one (create order).
How do you parallelise a consumer without breaking per-order sequence?::Parallelise across keys: route each record to a worker by hash(key) so one key always goes to the same single-threaded worker, and commit offsets only up to the lowest unfinished record.
What happens to key→partition mapping when you add partitions?::It changes (hash mod N), so new events for a key can land on a different partition than its older events, and ordering across the change breaks.
