---
Creation_date: 2026-10-21 15:47
Modification_date: Wednesday 21st October 2026 15:51:01
Indexes:
  - "[[permanent_notes]]"
  - "[[Kafka]]"
  - "[[Java_Spring]]"
  - "[[Messaging and Transactions]]"
Source: docs (Spring for Apache Kafka 4.1.x reference, Apache Kafka 4.3 docs)
---

----
# Spring Kafka retries and dead-letter topics (DefaultErrorHandler, DeadLetterPublishingRecoverer, @RetryableTopic)

> **Source type: official docs, not the channel.** No public anonystick video covers consumer-side retries on Kafka (his DLQ video [[hrSP7UocdJ8]] is RabbitMQ). Written from the Spring for Apache Kafka **4.1.1** reference and Kafka 4.3 docs, links inline. Check the version you run, because defaults changed between 3.x and 4.x.

## The problem
Kafka has no broker-side "reject → DLX" like RabbitMQ ([[hrSP7UocdJ8]]). A consumer that throws has three options: retry in place, move the record aside and keep going, or stop. Spring Kafka gives you all three. Without a configured strategy you get **10 quick attempts and then the record is just logged and skipped**, which is a silent loss.

## 1. Blocking retries: `DefaultErrorHandler`
- When a listener throws, the `DefaultErrorHandler` **seeks back** to the failed offset so the record is re-polled and retried, per a `BackOff`. **Default: 10 delivery attempts with no delay, then the record is logged at ERROR and skipped.** ([Handling Exceptions](https://docs.spring.io/spring-kafka/reference/kafka/annotation-error-handling.html))
- While it retries, **the whole partition waits**. Order is kept, but lag grows behind a poison record.
- Keep the total back-off below `max.poll.interval.ms` (default 300000 ms = 5 min), or the consumer is kicked out and a rebalance starts. For long delays use `ContainerPausingBackOffHandler`, which pauses the container instead of sleeping. ([Kafka consumer configs](https://kafka.apache.org/43/configuration/consumer-configs/))
- **Not retried (fatal by default):** `DeserializationException`, `MessageConversionException`, `ConversionException`, `MethodArgumentResolutionException`, `NoSuchMethodException`, `ClassCastException`; these go straight to the recoverer. Add your own with `addNotRetryableExceptions(...)` (e.g. validation errors that will never succeed).
- **What reaches the error handler: `Exception` yes, `Error` no** (corrected after review). The docs say *"The `DefaultErrorHandler` only processes exceptions that inherit from `RuntimeException`. Exceptions inheriting from `Error` bypass the error handler entirely, causing the consumer to terminate immediately…"* ([Handling Exceptions](https://docs.spring.io/spring-kafka/reference/kafka/annotation-error-handling.html)). That doesn't mean checked exceptions are ignored. Whatever your `@KafkaListener` method throws (checked or unchecked) is **wrapped in a `ListenerExecutionFailedException`** ("the exception that was thrown by the listener, which is wrapped in a `ListenerExecutionFailedException`", same page), and that class is a `RuntimeException` (`ListenerExecutionFailedException extends KafkaException extends NestedRuntimeException` in the [source](https://github.com/spring-projects/spring-kafka/blob/main/spring-kafka/src/main/java/org/springframework/kafka/listener/ListenerExecutionFailedException.java)). So a checked `IOException` from your listener **is** retried and recovered like any other failure. The real split is **`Exception` vs `Error`**: the listener adapter rethrows `Error`s unwrapped, and the container logs "Stopping container due to an Error" and stops ([KafkaMessageListenerContainer source](https://github.com/spring-projects/spring-kafka/blob/main/spring-kafka/src/main/java/org/springframework/kafka/listener/KafkaMessageListenerContainer.java)). A `java.lang.Error` (e.g. `OutOfMemoryError`, `StackOverflowError`, an `AssertionError` from a stray `assert`) therefore **kills the consumer**, and the app may still report healthy, so alert on container-stopped events and consumer lag.
- **Poison pills that can't even be deserialised:** wrap your deserializer in `ErrorHandlingDeserializer` so the failure reaches the error handler (and the DLT) instead of looping in `poll()`.

## 2. Send it aside: `DeadLetterPublishingRecoverer`
```java
@Bean
DefaultErrorHandler errorHandler(KafkaTemplate<Object, Object> template) {
    var recoverer = new DeadLetterPublishingRecoverer(template);    // -> <topic>-dlt (since 3.3; .DLT before), same partition
    var handler = new DefaultErrorHandler(recoverer, new FixedBackOff(1000L, 2L)); // 3 attempts total
    handler.addNotRetryableExceptions(IllegalArgumentException.class);
    return handler;  // Spring Boot wires a single CommonErrorHandler bean into the listener container factory
}
```
- Default destination: **`<originalTopic>-dlt`, same partition number**, so the DLT needs **at least as many partitions** as the source topic. **The default changed in Spring Kafka 3.3** (re-verified 2026-10-21):
  - Current docs (4.1.1; 3.3, 4.0 and 4.2-SNAPSHOT say the same): *"By default, the dead-letter record is sent to a topic named `<originalTopic>-dlt` (the original topic name suffixed with `-dlt`) and to the same partition as the original record."* ([4.1 Handling Exceptions → Publishing Dead-letter Records](https://docs.spring.io/spring-kafka/reference/kafka/annotation-error-handling.html), [3.3 page](https://docs.spring.io/spring-kafka/reference/3.3/kafka/annotation-error-handling.html))
  - 3.2 docs: *"By default, the dead-letter record is sent to a topic named `<originalTopic>.DLT` (the original topic name suffixed with `.DLT`) and to the same partition as the original record."* ([3.2 page](https://docs.spring.io/spring-kafka/reference/3.2/kafka/annotation-error-handling.html))
  - 3.3 "What's New": *"DLT Topic Naming Convention: The naming convention for DLT topics has been standardized to use the "-dlt" suffix consistently. This change ensures compatibility and avoids conflicts when transitioning between different retry solutions. Users who wish to retain the ".DLT" suffix behavior need to opt-in explicitly by setting the appropriate DLT name property."* ([What's New in 3.3](https://docs.spring.io/spring-kafka/reference/3.3/whats-new.html))
  - Source confirms it: `DEFAULT_DESTINATION_RESOLVER = (cr, e) -> new TopicPartition(cr.topic() + "-dlt", cr.partition())` on the `3.3.x` and `main` branches, `+ ".DLT"` on `3.2.x` ([DeadLetterPublishingRecoverer.java](https://github.com/spring-projects/spring-kafka/blob/main/spring-kafka/src/main/java/org/springframework/kafka/listener/DeadLetterPublishingRecoverer.java)).
  - So both the recoverer and `@RetryableTopic` now default to `-dlt`. **On Spring Kafka ≤ 3.2 (Spring Boot ≤ 3.3) it's `.DLT`.** Upgrading past 3.2 silently moves dead letters to a new topic unless you pass your own destination resolver, so check existing `.DLT` topics, consumers and alerts. To keep the old name: `new DeadLetterPublishingRecoverer(template, (r, e) -> new TopicPartition(r.topic() + ".DLT", r.partition()))`.
- DLT records carry headers for debugging and replay: `DLT_EXCEPTION_FQCN`, `DLT_EXCEPTION_MESSAGE`, `DLT_EXCEPTION_STACKTRACE`, `DLT_ORIGINAL_TOPIC`, `DLT_ORIGINAL_PARTITION`, `DLT_ORIGINAL_OFFSET`, `DLT_ORIGINAL_CONSUMER_GROUP`, …
- With `AckMode.MANUAL_IMMEDIATE`, set `commitRecovered=true` so the recovered offset is committed.
- **The DLT is not the end of the story:** something must alert on it and a person or job must replay or fix it. For payments, keep the record in a DB parking table too (see the correction in [[hrSP7UocdJ8]]).

## 3. Non-blocking retries: `@RetryableTopic`
```java
@RetryableTopic(attempts = "4", backOff = @BackOff(delay = 1000, multiplier = 2))
@KafkaListener(topics = "orders")
void on(OrderEvent e) { ... }

@DltHandler
void dlt(OrderEvent e) { /* alert, park, etc. */ }
```
- A failure is **forwarded to a retry topic** with a due timestamp, and the main partition **keeps flowing**. With 4 attempts and 1 s ×2 back-off, Spring creates `orders-retry-1000`, `orders-retry-2000`, `orders-retry-4000` and `orders-dlt`, plus their consumers. Default suffixes are `-retry` and `-dlt`. ([How the pattern works](https://docs.spring.io/spring-kafka/reference/retrytopic/how-the-pattern-works.html), [Topic naming](https://docs.spring.io/spring-kafka/reference/retrytopic/topic-naming.html), [Features](https://docs.spring.io/spring-kafka/reference/retrytopic/features.html))
- **Trade-off, from the docs: "By using this strategy you lose Kafka's ordering guarantees for that topic."** Event 2 of an order can be processed while event 1 is waiting in a retry topic.
- `AckMode.RECORD` is suggested. By default it retries on all exceptions except the global fatal list above.
- In 4.x the annotation attribute is `backOff = @BackOff(...)`; 3.x used `backoff = @Backoff(...)` from Spring Retry.

## Which one when?
| Situation | Use |
|---|---|
| Per-key order matters (order state machine, ledger) | **Blocking** `DefaultErrorHandler` with a short, bounded back-off + DLT; alert on lag |
| Independent events (emails, analytics, notifications) and a slow downstream | **Non-blocking** `@RetryableTopic` |
| Error that will never heal (bad payload, validation) | Not-retryable → DLT straight away |
| Downstream fully down (DB outage) | Don't burn retries; pause the container or stop and alert (a circuit breaker) |

## How it connects to the core topics
- **Core focus:** poison messages, dead-letter topics, retries with limits and back-off, consumer lag, ordering vs availability.
- **QA tests to design:** (1) publish a record that always throws: assert N attempts (count logs or metrics), then exactly one record in `-dlt` with the original topic/partition/offset headers, and that later records on the same partition were processed. (2) A record that fails twice then succeeds: assert one side effect, so retries must be idempotent ([[G4-_ckYTtvo]]). (3) Send bytes that can't be deserialised and check they reach the DLT and don't loop. (4) With `@RetryableTopic`, send create → update for one key where create fails once, and check whether your consumer copes with the update arriving first (it will). (5) A back-off longer than `max.poll.interval.ms`: watch for a rebalance storm.
- **Go:** no framework does this for you. With franz-go or segmentio/kafka-go you write it yourself: retry in-process with a bounded back-off, then produce to `<topic>-retry` / `<topic>-dlt` with error headers, and commit the original offset only after that produce is acked.

## Related
[[hrSP7UocdJ8]] · [[Out-of-order messages and consumer rebalancing]] · [[Dead Letter Queue]] · [[Poison Message]] · [[Idempotent Consumer]] · [[Messaging and Transactions]]

---
## Flash cards section
What does Spring Kafka's DefaultErrorHandler do by default when a listener keeps throwing?::It retries 10 times with no back-off (by seeking back), then logs the record at ERROR and skips it. Without a recoverer, that's a silent loss.
Where does DeadLetterPublishingRecoverer send a record by default?::To <originalTopic>-dlt on the same partition number since Spring Kafka 3.3 (<originalTopic>.DLT in 3.2 and earlier), so the DLT needs at least as many partitions.
Blocking retries vs @RetryableTopic?::Blocking keeps per-partition order but stalls the partition. Non-blocking moves failures to retry topics so the main topic flows, but loses ordering.
Does a checked exception thrown from a @KafkaListener reach the DefaultErrorHandler?::Yes. It's wrapped in ListenerExecutionFailedException (a RuntimeException). Only java.lang.Error bypasses the handler and stops the container.
Which exceptions skip retries by default?::Deserialization, message conversion, conversion, method-argument resolution, NoSuchMethod and ClassCast exceptions. They go straight to the recoverer.
