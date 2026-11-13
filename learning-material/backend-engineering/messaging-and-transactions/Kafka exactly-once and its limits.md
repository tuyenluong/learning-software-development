---
Creation_date: 2026-11-13 22:30
Modification_date: Friday 13th November 2026 22:30:00
Indexes:
  - "[[permanent_notes]]"
  - "[[Kafka]]"
  - "[[Messaging and Transactions]]"
Source: docs (Apache Kafka 4.3 design "Message Delivery Semantics" and consumer configs, Spring for Apache Kafka reference "Exactly Once Semantics" and "Transactions")
---

----
# Kafka exactly-once and its limits

> **Source type: official docs only.** Kafka design docs ([delivery semantics](https://kafka.apache.org/43/design/design/), [consumer configs](https://kafka.apache.org/43/configuration/consumer-configs/)) and the Spring for Apache Kafka reference ([exactly-once](https://docs.spring.io/spring-kafka/reference/kafka/exactly-once.html), [transactions](https://docs.spring.io/spring-kafka/reference/kafka/transactions.html)). Market signal: a senior backend posting in the [13 Nov 2026 backend report](../../../job-market/backend-engineer/backend-job-market-2026-11-13.md) lists "the limits of exactly-once semantics" next to the transactional outbox, idempotency keys and deduplication as written requirements.

## Part A: what "exactly-once" in Kafka actually covers
Kafka's guarantee is narrower than the name suggests. From the design docs: the **transactional producer plus consumers reading with `read_committed`** give exactly-once for a **read → process → write** loop **on Kafka topics** (and Kafka Streams builds on the same primitives). "Exactly-once delivery for other destination systems generally requires cooperation with such systems." Otherwise Kafka is **at-least-once by default**.

The pieces:
1. **Idempotent producer** (`enable.idempotence`, on by default since Kafka 3.0): the broker drops duplicates caused by producer retries **within one producer session**. It does **not** dedupe two separate `send()` calls of the same business event, and it does nothing for consumers.
2. **Transactional producer** (`transactional.id`): the output records **and the consumed offsets** (`sendOffsetsToTransaction`) commit or abort together. A restarted instance with the same id fences the old "zombie".
3. **`read_committed` consumers downstream.** `isolation.level` **defaults to `read_uncommitted`**, which returns records from **aborted** transactions too. Without `read_committed` on every downstream consumer, the guarantee is gone. `read_committed` consumers also stop at the last stable offset, so a long open transaction delays them.

Spring for Apache Kafka says the same thing plainly: for `read → process → write` the sequence completes exactly once, but **"the read and process have at least once semantics."** If the listener throws, the transaction rolls back and the record is redelivered, so any side effect inside "process" can run again.

## Part B: where it stops
Anything outside Kafka is **not** in the Kafka transaction:
| Side effect in the listener | What happens on a rollback or crash | What to use instead |
|---|---|---|
| Insert/update in PostgreSQL or MySQL | The DB commit is separate; it may commit while the Kafka transaction aborts (or the other way round), and the record is processed again | **Idempotent consumer:** a processed-event table (`event_id` primary key) written in the **same DB transaction** as the business change; or store the consumer offset in the DB with the output (the "store the offset in the same place as the output" approach from the Kafka docs) |
| HTTP call to a payment provider | Called again on redelivery | **Idempotency key** sent to the provider; reconcile on timeouts |
| Email / push notification | Sent twice | Dedupe table or an outbox row with a unique key |
| Producing an event after a DB write (no Kafka-side consume) | Dual write: DB commits, Kafka send fails (or the reverse) | **Transactional outbox** (row in the same DB transaction, relayed to Kafka by a poller or CDC) |

**Spring transaction synchronization is "best effort", not atomic.** With `@Transactional` + a `DataSourceTransactionManager` and a transactional `KafkaTemplate`, the docs describe the order: the **database commits first, then Kafka** (nest the methods to reverse it). If the second commit fails after the first succeeded, Spring (since 2.5.17 / 2.6.12 / 2.7.9 / 2.8.0) throws to the caller, and "applications should take remedial action, if necessary, to compensate". So a crash between the two commits still needs an idempotent consumer or an outbox. `ChainedKafkaTransactionManager` has been deprecated since 2.7.

## Part C: settings that matter
- **Spring Boot:** `spring.kafka.producer.transaction-id-prefix=tx-` makes Boot create a `KafkaTransactionManager` and wire it into the listener container. The prefix **must be unique per application instance**. Spring for Apache Kafka 3.0+ supports only `EOSMode.V2` (KIP-447 fetch-offset-request fencing), which needs brokers **2.5+**.
- **Downstream consumers:** `spring.kafka.consumer.isolation-level=read_committed` (plain client: `isolation.level=read_committed`).
- **Retries:** non-blocking retries (`@RetryableTopic`) **cannot be combined with container transactions**: the container transaction commits and the record goes to the retry topic. Pick one model (see [[Spring Kafka retries and dead-letter topics]]).
- **Batch listeners:** on failure the whole batch is rolled back and redelivered unless records are handled one at a time.
- **Go (franz-go):** `kgo.TransactionalID(...)` on the client, `kgo.FetchIsolationLevel(kgo.ReadCommitted())` on consumers, and `kgo.NewGroupTransactSession` for the consume-transform-produce loop. The same limits apply: anything written outside Kafka needs its own idempotency.

## How it connects to the core topics
- **Core focus:** duplicates, dual writes, at-least-once consumers, transactions across a database and a broker.
- **Rule of thumb:** Kafka transactions make **Kafka-to-Kafka** pipelines exactly-once. For **Kafka-to-database** or **database-to-Kafka**, design for at-least-once and make the effect idempotent (processed-event table, unique keys, version checks), or use the outbox.
- **QA tests to design:**
  1. **Crash between commits:** in a listener that writes to PostgreSQL and produces to Kafka, kill the process after the DB commit and before the Kafka commit. Assert the redelivered record does **not** create a second DB row or a second downstream event effect.
  2. **Aborted transaction visibility:** produce inside a transaction, then abort. Assert a `read_committed` consumer never sees the records and a `read_uncommitted` consumer does (this is the default trap).
  3. **Zombie fencing:** run two instances with the **same** `transaction-id-prefix`; observe `ProducerFencedException`. Then give each a unique prefix and confirm normal operation.
  4. **Retry model:** combine container transactions with `@RetryableTopic` in a test configuration and assert where a failing record ends up (retry topic, with the original transaction committed).
  5. **Rebalance mid-transaction:** force a rebalance during processing (stop one consumer). Assert no duplicate side effects outside Kafka (see [[Out-of-order messages and consumer rebalancing]]).

## Related
[[DQN0pRV8RnU]] · [[2TBqQBEI56A]] · [[G4-_ckYTtvo]] · [[A9gqa8q-l1w]] · [[Out-of-order messages and consumer rebalancing]] · [[Spring Kafka retries and dead-letter topics]] · [[Idempotent Consumer]] · [[Messaging and Transactions]]

---
## Flash cards section
What does Kafka "exactly-once" guarantee?::A read → process → write loop on Kafka topics commits output records and consumed offsets atomically (transactional producer + read_committed consumers). Not side effects in other systems.
What is the default consumer isolation.level, and why does it matter?::read_uncommitted: consumers also see records from aborted transactions, which breaks exactly-once downstream. Set read_committed.
Does the idempotent producer stop duplicate business events?::No. It only drops duplicates from producer retries within one session; two send() calls of the same event are two records.
In Spring, @Transactional with a DataSourceTransactionManager and a transactional KafkaTemplate: which commits first?::The database, then Kafka (nest the methods to reverse it). A failure between the two commits is not rolled back, so consumers still need idempotency or an outbox.
Why must transaction-id-prefix be unique per instance?::Transactional ids fence "zombie" producers; two instances sharing a prefix fence each other (ProducerFencedException).
Can @RetryableTopic be combined with container transactions?::No. The container transaction commits and the failed record is sent to the retry topic.
How do you get exactly-once into a database?::Write the business change and a processed-event row (or the consumer offset) in the same DB transaction, so a redelivered record is detected and skipped.
