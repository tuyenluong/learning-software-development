---
Creation_date: 2026-10-21 16:35
Modification_date: Wednesday 21st October 2026 16:35:00
Indexes:
  - "[[home]]"
  - "[[permanent_notes]]"
  - "[[QA_Automation]]"
---

----
# QA Module 1: QA Automation for Edge Cases (curriculum)

Status: **new 2026-10-21**, written from official docs. The backend notes in [[Messaging and Transactions]] explain *why* the edge cases happen, and this module teaches *how to test them*.

Legend: 📘 = permanent note written from official docs. All 6 lessons written 2026-10-21; Java examples first (for Java, Selenium, TestNG/Cucumber and Jenkins shops), TypeScript Playwright second.

| # | Lesson | Type | What you'll be able to do |
|---|---|---|---|
| 1 | [[Test design for messaging and transaction edge cases]] | 📘 | Pick the right assertions (effect, state, outputs, routing, liveness) for duplicates, retries, dead letters, out-of-order and races; where pyramid/trophy and Pact fit |
| 2 | [[Playwright API testing (APIRequestContext)]] | 📘 | Auth, fixtures, idempotency-key tests, contract-style response checks |
| 3 | [[Framework structure - fixtures and test data]] | 📘 | Build reusable fixtures and deterministic, isolated test data |
| 4 | [[Testcontainers for Kafka and RabbitMQ (Java and Go)]] | 📘 | Real brokers + Postgres in tests, Spring Boot `@ServiceConnection`, testcontainers-go |
| 5 | [[Async waits without sleeps]] | 📘 | Awaitility, Playwright `expect.poll` / `toPass`, Testcontainers wait strategies |
| 6 | [[CI with flaky-test control]] | 📘 | GitHub Actions + Docker, retries with reporting, quarantine, traces |

## Suggested pacing
One lesson per study session. Each lesson ends with a "how you'd automate this" part and flash cards for review. Lessons 4–6 build on 1–3: lesson 1's invariants are what lessons 4 and 5 automate.

## Versions checked (2026-10-21)
Spring Boot 4.1.1 · JUnit 6.1.3 · AssertJ 3.27.7 · Spring for Apache Kafka 4.1.1 · Spring AMQP 4.1.1 · Testcontainers for Java 2.0.5 · testcontainers-go v0.44.0 · Playwright 1.64.1 (Node) / 1.63.0 (Java) · TestNG 7.12.0 · Awaitility 4.3.0 · Maven Surefire 3.6.0 · testify v1.12.1 · Apache Kafka 4.3.2 (image `apache/kafka:4.3.2`) · RabbitMQ 4.4.0 (released 2026-10-19; 4.3.x still maintained).
