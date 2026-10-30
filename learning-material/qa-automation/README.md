# QA automation

QA automation notes for testing messaging and transaction edge cases. Every note is written from official docs, with links and versions checked as of the date in its frontmatter. The backend engineering notes ([module-1/](../backend-engineering/module-1/)) explain why these edge cases happen.

## QA Module 1: QA Automation for Edge Cases
Overview: [Module 1 - QA Automation for Edge Cases](module-1/Module%201%20-%20QA%20Automation%20for%20Edge%20Cases.md)

1. [Test design for messaging and transaction edge cases](module-1/Test%20design%20for%20messaging%20and%20transaction%20edge%20cases.md): the five invariants to assert for duplicates, retries, DLQ, out-of-order and races, plus where pyramid/trophy and Pact fit.
2. [Playwright API testing (APIRequestContext)](module-1/Playwright%20API%20testing%20(APIRequestContext).md): request fixture, auth, idempotency-key tests (same key twice, different payload, concurrent), schema checks.
3. [Framework structure: fixtures and test data](module-1/Framework%20structure%20-%20fixtures%20and%20test%20data.md): Playwright `test.extend` fixtures, JUnit extensions, test data builders, deterministic data (unique ids, seeds, clocks).
4. [Testcontainers for Kafka and RabbitMQ (Java and Go)](module-1/Testcontainers%20for%20Kafka%20and%20RabbitMQ%20(Java%20and%20Go).md): Testcontainers 2.x changes, Spring Boot `@ServiceConnection` as beans, testcontainers-go, DLT/DLQ and duplicate tests, reuse, Docker in GitHub Actions and Jenkins.
5. [Async waits without sleeps](module-1/Async%20waits%20without%20sleeps.md): Awaitility (incl. `during` for "stays at 1"), Playwright `expect.poll`/`toPass`, Testcontainers wait strategies, testify `EventuallyWithT`.
6. [CI with flaky-test control](module-1/CI%20with%20flaky-test%20control.md): causes of flakiness, Surefire reruns/flakes, TestNG retry, Playwright retries/traces/`--fail-on-flaky-tests`, quarantine, Jenkins and GitHub Actions examples.
