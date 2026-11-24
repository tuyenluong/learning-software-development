---
Creation_date: 2026-11-24 22:30
Modification_date: Tuesday 24th November 2026 22:30:00
Indexes:
  - "[[permanent_notes]]"
  - "[[Kafka]]"
  - "[[Messaging and Transactions]]"
Source: docs (Confluent Schema Registry "Schema Evolution and Compatibility", including "Order of upgrading clients")
---

----
# Backward-compatible event changes during rolling and canary deploys

> **Source type: official docs, plus one general practice marked as such.** Compatibility rules and upgrade order are from the Confluent Schema Registry docs ([schema evolution and compatibility](https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html)). Market signal: a mid-level backend posting in the [24 Nov 2026 backend report](../../../job-market/backend-engineer/backend-job-market-2026-11-24.md) asks for "backward-compatible changes while different service versions coexist" during canary releases, next to Kafka delivery guarantees and idempotency; another names Schema Registry.

## Part A: why this is a messaging problem
During a rolling or canary deploy, **old and new versions of a service run at the same time**. With a broker in between, the overlap is longer than the deploy itself:
- messages written by the **old producer** are still in the topic or queue when the **new consumer** starts (retention, consumer lag, DLQ replays);
- messages written by the **new producer** can be read by **old consumers** that have not been upgraded yet;
- a rollback puts old code back in front of messages the new code already wrote.

So every event change has to be safe in **both directions for as long as the versions overlap**, not just at the moment of the switch.

## Part B: compatibility types (Schema Registry)
| Type | Guarantee | Typical allowed change (Avro) | Who to upgrade first |
|---|---|---|---|
| **BACKWARD** (default) | Consumers on the **new** schema can read data written with the **last** schema | Add an optional field (with a default), delete a field | **Consumers first**, then start producing new events |
| **FORWARD** | Consumers on the **last** schema can read data written with the **new** schema | Add a field, delete an optional field | **Producers first**; make sure old-schema data is no longer read; then consumers |
| **FULL** | Both of the above | Add or remove **optional** fields only | Either side, independently |
| **…_TRANSITIVE** | Same rule checked against **all** earlier versions, not just the last | – | Needed when old data can be replayed from far back |
| **NONE** | No checks | Anything | Coordinate by hand |

Key details from the docs:
- `BACKWARD` only promises the **last** version. If a topic can still hold data from two or more versions ago (long retention, replay from a DLQ), use `BACKWARD_TRANSITIVE`.
- Removing a field stays compatible only if the field was **optional or had a default** in the original version. In Avro, "optional" means a union with `null` and `"default": null`.
- **Kafka Streams** apps also read old data from their state stores and changelogs, so only `BACKWARD` (and `FULL`, `FULL_TRANSITIVE`, `BACKWARD_TRANSITIVE`) are supported, and **the Streams app must be upgraded before the upstream producer**.
- For a truly incompatible change (for example a field type from number to string), the docs suggest upgrading all producers and consumers at once or, more often, **a new topic** and migrating applications to it.

## Part C: the same idea without a registry (general practice)
For JSON events on RabbitMQ or Kafka without Schema Registry, nothing enforces the rules, so the team has to follow them by convention:
1. **Expand, then contract.** Release 1 adds the new field (optional) and consumers that tolerate both shapes. Release 2 makes producers fill it. Release 3, after every old message is gone, removes the old field.
2. **Tolerant consumers.** Ignore unknown fields (in Jackson: `FAIL_ON_UNKNOWN_PROPERTIES = false`, which Spring Boot already sets by default for its auto-configured `ObjectMapper`) and give missing fields a safe default.
3. **Never reuse a field name with a new meaning or type.** Add a new field instead.
4. **Version in the payload or a header** when the meaning changes, so a consumer can route or reject explicitly instead of failing on deserialization and sending the message to the DLQ.

## How it connects to the core topics
- **Core focus:** a message that cannot be deserialized after a deploy is a **poison message**; it ends in the DLQ or blocks a partition (see [[Spring Kafka retries and dead-letter topics]]). Compatibility rules prevent that class of failure.
- **Idempotency still applies:** a rollback or a replay after a fix redelivers messages; handlers must stay idempotent across versions (see [[Kafka exactly-once and its limits]]).
- **QA tests to design:**
  1. **Old producer → new consumer:** publish an event with the previous schema; assert the new consumer processes it with the default for the new field.
  2. **New producer → old consumer:** run the previous consumer build against an event with the added field; assert it is processed, not dead-lettered.
  3. **Registry check in CI:** register the candidate schema against the subject's compatibility setting (test registry or the Schema Registry Maven plugin) and fail the build on an incompatible change.
  4. **Replay across versions:** with `BACKWARD` (not transitive), replay data from two versions back and observe whether the consumer fails; switch to `BACKWARD_TRANSITIVE` and confirm the registry now blocks the risky change.
  5. **Rollback drill:** deploy the new producer, write events, roll back the consumer; assert nothing lands in the DLQ.

## Related
[[Spring Kafka retries and dead-letter topics]] · [[Kafka exactly-once and its limits]] · [[Out-of-order messages and consumer rebalancing]] · [[Messaging and Transactions]]

---
## Flash cards section
What does BACKWARD compatibility guarantee?::Consumers using the new schema can read data written with the last schema. It is Schema Registry's default.
With BACKWARD compatibility, which side do you upgrade first?::Consumers first, then start producing events with the new schema.
With FORWARD compatibility, which side do you upgrade first?::Producers first, make sure old-schema data is no longer consumed, then upgrade consumers.
When do you need BACKWARD_TRANSITIVE instead of BACKWARD?::When consumers may read data from more than one version back (long retention, replays), because BACKWARD only checks against the last version.
Which compatibility does Kafka Streams need, and what is upgraded first?::BACKWARD (or a stronger setting that includes it), because it also reads old data from state and changelogs; upgrade the Streams app before the upstream producer.
How do you make a truly incompatible event change?::Upgrade all producers and consumers together or, usually, create a new topic and migrate applications to it.
What is expand-then-contract for events?::Add the new field as optional with tolerant consumers, then make producers fill it, and remove the old field only after no old messages remain.
