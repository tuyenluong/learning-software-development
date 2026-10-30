---
Creation_date: 2026-10-21 16:30
Modification_date: Wednesday 21st October 2026 16:30:00
Indexes:
  - "[[permanent_notes]]"
  - "[[QA_Automation]]"
  - "[[Message_Queues]]"
  - "[[Module 1 - QA Automation for Edge Cases]]"
Source: docs (Apache Kafka 4.3 design docs, RabbitMQ 4.x DLX + quorum queue docs, Spring for Apache Kafka 4.1.1, Spring AMQP 4.1, Pact docs, Fowler's Practical Test Pyramid)
---

----
# QA Lesson 1: Test design for edge cases (duplicates, retries, dead letters, races): what to assert

> **Source type: official docs, not the channel.** QA Module 1, lesson 1. The backend notes in [[Module 1 - Messaging and Transactions]] explain *why* these failures happen; this note is about *what a test must check* when they do. Verified 2026-10-21 against the docs linked below. Tools and code come in later lessons; this one is about test design.

## The idea in one paragraph
Happy-path tests check "it worked". Edge-case tests check **invariants**: things that must stay true *however many times* a message arrives, *in whatever order*, *however many retries happen*, and *whoever wins a race*. Kafka and RabbitMQ both give you **at-least-once** delivery in normal setups, so duplicates are expected behaviour, not a rare bug. The Kafka design docs say it plainly: the default is at-least-once, and a consumer that crashes after processing but before committing its offset **will process the same records again** ([Kafka 4.3 design: message delivery semantics](https://kafka.apache.org/43/design/design/)). Your job as QA is to turn "should be safe" into assertions.

## The five invariants to assert (memorise these)
| # | Invariant | Typical assertion |
|---|---|---|
| 1 | **Effect count**: the business effect happens exactly once | 1 row in `payments`, balance moved once, 1 email in the fake SMTP |
| 2 | **Final state**: the end state is right regardless of order or retries | order status = `SHIPPED`, not rolled back to `PAID` by a late event |
| 3 | **Outputs**: downstream messages are emitted the right number of times | exactly 1 `PaymentCompleted` event on the output topic (or each duplicate is harmless and carries the same id) |
| 4 | **Failure routing**: a bad message ends up in the right place, once, with evidence | 1 record in `orders-dlt` (Spring Kafka 3.3+ default; `.DLT` on 3.2 and older) or the RabbitMQ DLQ, with headers saying why |
| 5 | **Liveness**: the system keeps going after the bad thing | the next message on the same partition/queue is processed; consumer lag returns to 0 |

A test that only checks #1 passes while the consumer is stuck forever on a poison message (#5 fails). Always pair a "bad thing" test with a "and then a good message still works" check.

## Edge case → what to inject → what to assert
### Duplicates
- **Inject:** publish the *same* message twice (same message id / business key), or make the consumer crash after the DB commit but before the ack/offset commit, then restart it.
- **Assert:** invariants 1 and 3. Also assert that the second delivery is *recognised* (a `dedup_hits` metric, a log line, or a row in the `processed_messages` table), so you know the guard ran and you weren't just lucky.
- **Kafka note:** producer idempotence (`enable.idempotence=true`, default since Kafka 3.0) stops duplicates *caused by producer retries* inside one producer session. It does **not** stop a consumer reprocessing after a crash, or an app that publishes the same event twice. Consumer-side idempotency is still yours to test ([[A9gqa8q-l1w]], [[G4-_ckYTtvo]]).

### Retries
- **Inject:** make a dependency fail N times then succeed (a fake HTTP server returning 503 twice, a DB that's paused for a moment).
- **Assert:** the effect happens once (retry + partial work = classic double effect), the number of attempts matches the configured policy, and the total retry time stays under the consumer's limits. For Spring Kafka, the `DefaultErrorHandler` default is **10 attempts with no back-off, then log and skip** ([Spring Kafka 4.1 Handling Exceptions](https://docs.spring.io/spring-kafka/reference/kafka/annotation-error-handling.html)). A test that expects a DLT record will fail on an app that never configured a recoverer, and that's a real bug: silent loss.
- **RabbitMQ / Spring AMQP note:** by default a listener exception **requeues** the message (`defaultRequeueRejected=true`); throw `AmqpRejectAndDontRequeueException` (or use `RejectAndDontRequeueRecoverer` after retries) to reject without requeue so it dead-letters ([Spring AMQP: Exception Handling](https://docs.spring.io/spring-amqp/reference/amqp/exception-handling.html)). Test both: "transient error → retried then succeeds" and "permanent error → not requeued forever".

### Dead letters (poison messages)
- **Inject:** a message that can never succeed: bad JSON, a missing required field, an unknown enum value.
- **Assert (invariant 4):** exactly one copy in the DLQ/DLT, original payload intact, and the "why" headers present:
  - Spring Kafka DLT: `DLT_EXCEPTION_FQCN`, `DLT_EXCEPTION_MESSAGE`, `DLT_ORIGINAL_TOPIC`, `DLT_ORIGINAL_PARTITION`, `DLT_ORIGINAL_OFFSET` (same Spring Kafka page).
  - RabbitMQ: an `x-death` header array (fields `queue`, `reason`, `count`, `exchange`, `routing-keys`) plus `x-first-death-reason` / `x-last-death-reason`. `reason` is one of `rejected`, `expired`, `maxlen`, `delivery_limit` ([RabbitMQ: Dead Letter Exchanges](https://www.rabbitmq.com/docs/dlx)).
- **Then assert invariant 5:** a good message sent right after is processed.
- **RabbitMQ quorum queues:** since RabbitMQ 4.0 the **delivery limit defaults to 20**. A message returned more often than that is **dropped, or dead-lettered if a DLX is configured** ([RabbitMQ: Quorum Queues → Poison Message Handling](https://www.rabbitmq.com/docs/quorum-queues)). So a test for "poison message on a quorum queue with no DLX" should expect it to *disappear*: that's message loss, and worth a bug report. Since 4.3, only real failures (`basic.reject`, a crashed channel) count toward the limit; `basic.nack` with requeue doesn't (same page). Check which broker version your env runs.
- **Gotcha to test:** if the DLX exchange doesn't exist when the message is dead-lettered, RabbitMQ **silently drops** the message (DLX page). A config test that asserts "the DLX and DLQ exist and are bound" is cheap and catches it.

### Out-of-order messages
- **Inject:** for one key, send `v2` before `v1` (e.g. `OrderShipped` then `OrderPaid`), or force a retry of event 1 while event 2 goes through.
- **Assert (invariant 2):** the final state is the newest one; the stale event is ignored or parked. See [[Out-of-order messages and consumer rebalancing]] for the version-check fix you're testing.

### Races (concurrent requests or consumers)
- **Inject:** N parallel requests for the last item in stock; two consumers getting the same message; two API calls with the same idempotency key at the same moment.
- **Assert:** the invariant holds for *every* run: stock never below 0, exactly one winner, the losers get a clean, documented error (409 / "already processing"), not a 500. Race tests are statistical: run the scenario many times in a loop (e.g. 50 rounds) and start all threads together with a latch, or you'll rarely hit the window. See [[GLqyIqWtRiA]] and [[Isolation levels and anomalies (Postgres vs MySQL)]].

## Small concrete example (JUnit 5 + AssertJ, framework-agnostic)
The shape of every edge-case test: **arrange → inject the bad thing → wait for the system to settle → assert the invariants**. The helpers (`publish`, `db`, `dlq`) come in lessons 3–5.

```java
@Test
void duplicatePaymentMessageIsAppliedOnce() {
    var msg = PaymentRequested.of("pay-123", "order-42", 100_00);

    publish("payments", msg);           // first delivery
    publish("payments", msg);           // duplicate: same message id

    await().atMost(Duration.ofSeconds(10)).untilAsserted(() -> {        // lesson 5: no Thread.sleep
        assertThat(db.count("select count(*) from payments where payment_id = 'pay-123'")).isEqualTo(1); // 1. effect once
        assertThat(db.balance("order-42")).isEqualTo(100_00);            // 2. final state
        assertThat(outputEvents("payment-completed", "pay-123")).hasSize(1);   // 3. outputs once
        assertThat(db.count("select count(*) from processed_messages where id = 'pay-123'")).isEqualTo(1); // guard ran
    });
}

@Test
void poisonMessageGoesToDltOnceAndConsumerKeepsGoing() {
    publishRaw("payments", "pay-bad", "{not json");
    publish("payments", PaymentRequested.of("pay-ok", "order-43", 50_00));

    await().atMost(Duration.ofSeconds(15)).untilAsserted(() -> {
        var dead = dlt("payments-dlt");                                   // Spring Kafka 3.3+ default suffix
        assertThat(dead).hasSize(1);                                       // 4. routed once
        assertThat(dead.get(0).header("kafka_dlt-original-topic")).isEqualTo("payments");
        assertThat(db.exists("payments", "pay-ok")).isTrue();              // 5. liveness
    });
}

@RepeatedTest(50)   // races are statistical: repeat
void lastItemCannotBeSoldTwice() throws Exception {
    db.setStock("sku-1", 1);
    var start = new CountDownLatch(1);
    try (var pool = Executors.newFixedThreadPool(10)) {
        var results = IntStream.range(0, 10)
            .mapToObj(i -> pool.submit(() -> { start.await(); return api.buy("sku-1"); }))
            .toList();
        start.countDown();                                                 // release all threads at once
        var codes = results.stream().map(f -> uncheckedGet(f).status()).toList();
        assertThat(codes).filteredOn(c -> c == 201).hasSize(1);            // exactly one winner
        assertThat(codes).allMatch(c -> c == 201 || c == 409);             // losers fail cleanly, no 500s
    }
    assertThat(db.stock("sku-1")).isZero();                                // never negative
}
```
Header name check: Spring Kafka exposes the DLT headers as constants on `KafkaHeaders` (`KafkaHeaders.DLT_ORIGINAL_TOPIC` = `"kafka_dlt-original-topic"`, verified in the [KafkaHeaders source](https://github.com/spring-projects/spring-kafka/blob/main/spring-kafka/src/main/java/org/springframework/kafka/support/KafkaHeaders.java)). Use the constant in real code, not the string.

## What breaks / how to test it (checklist)
- **"Passes alone, fails together":** dedup works for sequential duplicates but not for two copies processed *at the same time* by two consumers → send duplicates concurrently too.
- **Dedup marker in a different transaction from the effect** → the crash between them causes a double effect or a lost one. Test by killing the consumer between the two steps (a fault-injection hook, or stopping the container in lesson 4).
- **Retry re-does the partial work** (charged the card, then failed to write the row) → assert on the *external* side effect (fake payment provider call count), not just your DB.
- **DLQ exists but nothing reads it** → assert there's an alert/metric on DLQ depth, or at least file it as a risk.
- **Upgrade changes the DLT name** (`.DLT` → `-dlt` in Spring Kafka 3.3) → a test that asserts the exact DLT topic name catches it before production does.

## Where this fits in a test strategy (pyramid vs trophy, Pact)
- **Pyramid** ([Fowler, The Practical Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)): many fast unit tests, fewer integration/service tests, very few end-to-end UI tests. **Trophy** ([Kent C. Dodds](https://kentcdodds.com/blog/the-testing-trophy-and-testing-classifications)): put most effort in integration tests, because they give the most confidence per test.
- For **message-driven services, the edge cases in this note live at the integration level**: a real broker and a real DB in containers (lesson 4), driven through the service's real entry points. Unit tests can check the dedup function itself; only an integration test proves the broker + transaction + ack ordering is right.
- **Contract tests (Pact)** answer a different question: "does the producer's message/response still match what the consumer expects?" Pact supports both HTTP and **message** (queue) contracts ([Pact docs](https://docs.pact.io/), [How Pact works](https://docs.pact.io/getting_started/how_pact_works)). They catch a renamed field before it becomes a poison message, but they don't test duplicates, retries or races.
- **What to automate first** (highest risk per effort): (1) duplicate delivery → effect once; (2) poison message → DLQ once + consumer keeps going; (3) concurrent same-idempotency-key API calls; (4) retry after a transient failure → effect once; (5) out-of-order for one key.

## How it connects to the core topics
- **Core focus:** duplicates, retries and idempotency, poison messages and DLQ, out-of-order messages, races. This lesson is the "what to check" layer over all of [[Module 1 - Messaging and Transactions]].
- **In practice:** when writing a test plan for an event-driven feature, add a row per invariant (effect / state / outputs / routing / liveness) for each edge case above.

## Related
[[Module 1 - QA Automation for Edge Cases]] · [[Spring Kafka retries and dead-letter topics]] · [[hrSP7UocdJ8]] · [[inUimYVAGv0]] · [[G4-_ckYTtvo]] · [[Out-of-order messages and consumer rebalancing]] · [[GLqyIqWtRiA]] · [[Idempotent Consumer]] · [[Dead Letter Queue]]

---
## Flash cards section
What are the five invariants to assert in a messaging edge-case test?::Effect count (happens once), final state, outputs (downstream messages), failure routing (DLQ once, with why-headers), and liveness (the next message still gets processed).
Why are duplicates expected with Kafka and RabbitMQ, not a rare bug?::Both are at-least-once in normal setups. A consumer that crashes after processing but before acking/committing the offset gets the same message again.
Does Kafka producer idempotence remove the need for consumer-side dedup tests?::No. It only stops duplicates from producer retries within a session. Consumer reprocessing after a crash and app-level double publishes still happen.
What happens to a poison message on a RabbitMQ 4.x quorum queue with no DLX?::After the delivery limit (default 20 since 4.0) it is dropped, which is silent message loss. With a DLX it's dead-lettered with reason delivery_limit.
Which RabbitMQ header tells you why a message was dead-lettered?::x-death (array with queue, reason, count, exchange, routing-keys), plus x-first-death-reason and x-last-death-reason. Reasons: rejected, expired, maxlen, delivery_limit.
Why repeat a race-condition test many times and start threads with a latch?::Races are timing-dependent. A latch releases all threads at once to widen the window, and repetition makes a rare interleaving show up.
