# QA automation (priority 1)

Tuyen's QA automation track, taught by Jacob from notes researched by Jake. Every note is written from official docs, with links and versions checked as of the date in its frontmatter. Backend engineering notes ([module-1/](../module-1/)) are background reading for now.

## QA Module 1: QA Automation for Edge Cases
Overview: [Module 1 - QA Automation for Edge Cases](module-1/Module%201%20-%20QA%20Automation%20for%20Edge%20Cases.md)

1. [Test design for messaging and transaction edge cases](module-1/Test%20design%20for%20messaging%20and%20transaction%20edge%20cases.md): the five invariants to assert for duplicates, retries, DLQ, out-of-order and races, plus where pyramid/trophy and Pact fit.
2. [Playwright API testing (APIRequestContext)](module-1/Playwright%20API%20testing%20(APIRequestContext).md): request fixture, auth, idempotency-key tests (same key twice, different payload, concurrent), schema checks.
3. Framework structure: fixtures and test data *(coming)*
4. Testcontainers for Kafka and RabbitMQ, Java and Go *(coming)*
5. Async waits without sleeps *(coming)*
6. CI with flaky-test control *(coming)*
