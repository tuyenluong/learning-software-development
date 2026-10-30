# Jacob's review of anonystick batch 1 (2026-10-21)

Verdict: all 8 notes are accurate enough to teach from. Jake's own corrections are right. Fixes below.

## Corrections to add
- 9kpISaXHBvM (deadlocks): "synchronized can't detect deadlocks" is misleading. jstack detects deadlocks on synchronized monitors too. The real limitation is that a thread waiting on synchronized can't time out or be interrupted, which is why tryLock helps.
- DQN0pRV8RnU (outbox): a producer ack means the message is in the leader's/ISR replicas' log (page cache), not necessarily fsynced to disk. Since Kafka 3.0 the producer defaults are acks=all and enable.idempotence=true. Missing: running several outbox pollers at once needs SELECT ... FOR UPDATE SKIP LOCKED (or one leader), and publish order per aggregate matters, or consumers see out-of-order events.
- GLqyIqWtRiA (stock race): MySQL-specific. PostgreSQL defaults to READ COMMITTED, not REPEATABLE READ. The single conditional UPDATE is still safe there because Postgres re-checks the WHERE after waiting on the row lock. Add one line on lost update as the name of the read-check-write bug.
- az2VNMgNFrk (RabbitMQ reliability): Spring AMQP's acknowledge-mode=auto is NOT amqplib's noAck:true. Spring's container acks after the listener returns, and on an exception it requeues by default, which loops a poison message forever unless default-requeue-rejected=false or a DLX plus retry is set. Quorum queues are always durable.
- hrSP7UocdJ8 (DLX): his "save failures to a DB table and resend" anti-pattern is too strong. For payments or anything that must not be lost, a DB table (outbox / parking table) is the right tool. DLX retry suits cheap, losable work like notifications.
- inUimYVAGv0 (duplicate payments): "tinh bat bien" is immutability, not idempotency; "tinh luy dang" is the right term. DELETE is idempotent in state, but the second response can differ (404), so tests should check state, not the status code alone.
- aJ5kLfn8AtI (share groups): check the current Kafka docs for share-group status. It was early access in 4.0 and its status has changed in later releases.

## Gaps for the Messaging and Transactions module
- Kafka consumer-side retries and dead-letter topics (Spring Kafka DefaultErrorHandler + DeadLetterPublishingRecoverer), as a full note.
- Out-of-order messages and partition keys, and consumer rebalancing.
- Isolation levels as a table of anomalies (dirty read, non-repeatable read, phantom, lost update) for MySQL vs Postgres.
- Channel videos to do next: Saga part 1 (2TBqQBEI56A), Stripe-style idempotency keys (A9gqa8q-l1w), MySQL deadlocks (JDCbKBhmrC4), Debezium CDC (KqLzls2xCnQ).

## Module 1 order (agreed with Jake's)
1 DQRj7I3PcuM, 2 az2VNMgNFrk, 3 hrSP7UocdJ8, 4 GLqyIqWtRiA, 5 9kpISaXHBvM, 6 inUimYVAGv0, 7 DQN0pRV8RnU, 8 aJ5kLfn8AtI.
