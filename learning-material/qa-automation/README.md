# QA automation

QA automation notes for testing messaging and transaction edge cases. Every note is written from official docs, with links and versions checked as of the date in its frontmatter. The backend engineering notes ([messaging-and-transactions/](../backend-engineering/messaging-and-transactions/)) explain why these edge cases happen.

North star: [Ultimate Goal for QA Automation](ULTIMATE-GOAL.md) — what a QA automation engineer or consultant should achieve.

ISTQB reference notes for the points in that goal: [ultimate-goal-references/](ultimate-goal-references/).

## QA Module 1: QA Automation for Edge Cases
Overview: [Module 1 - QA Automation for Edge Cases](module-1/Module%201%20-%20QA%20Automation%20for%20Edge%20Cases.md)

1. [Test design for messaging and transaction edge cases](module-1/Test%20design%20for%20messaging%20and%20transaction%20edge%20cases.md): the five invariants to assert for duplicates, retries, DLQ, out-of-order and races, plus where pyramid/trophy and Pact fit.
2. [Playwright API testing (APIRequestContext)](module-1/Playwright%20API%20testing%20(APIRequestContext).md): request fixture, auth, idempotency-key tests (same key twice, different payload, concurrent), schema checks.
3. [Framework structure: fixtures and test data](module-1/Framework%20structure%20-%20fixtures%20and%20test%20data.md): Playwright `test.extend` fixtures, JUnit extensions, test data builders, deterministic data (unique ids, seeds, clocks).
4. [Testcontainers for Kafka and RabbitMQ (Java and Go)](module-1/Testcontainers%20for%20Kafka%20and%20RabbitMQ%20(Java%20and%20Go).md): Testcontainers 2.x changes, Spring Boot `@ServiceConnection` as beans, testcontainers-go, DLT/DLQ and duplicate tests, reuse, Docker in GitHub Actions and Jenkins.
5. [Async waits without sleeps](module-1/Async%20waits%20without%20sleeps.md): Awaitility (incl. `during` for "stays at 1"), Playwright `expect.poll`/`toPass`, Testcontainers wait strategies, testify `EventuallyWithT`.
6. [CI with flaky-test control](module-1/CI%20with%20flaky-test%20control.md): causes of flakiness, Surefire reruns/flakes, TestNG retry, Playwright retries/traces/`--fail-on-flaky-tests`, quarantine, Jenkins and GitHub Actions examples.

## Related notes
- [Playwright test locks for shared resources](Playwright%20test%20locks%20for%20shared%20resources.md): named `lock` on tests (1.63+) so tests sharing an account or setting never overlap, when to lock vs isolate data, and an exercise.
- [Playwright 1.65 exclusive lock and failure reporters](Playwright%201.65%20exclusive%20lock%20and%20failure%20reporters.md): built-in `-exclusive-` lock, `failures` / `onlyFailures` reporters, Bun runner notes, and an exercise.
- [Pact / contract testing (TypeScript)](pact/): six short lessons on consumer-driven contract testing with `@pact-foundation/pact` 17.1.4 — consumer tests, matchers, provider verification, Pact Broker, and CI.
- [Playwright 1.65 API request changes: cookies and query params](Playwright%201.65%20API%20request%20changes%20-%20cookies%20and%20query%20params.md): RFC 6265 cookie domain/path matching, `params` appended to an existing query, an upgrade checklist for API suites, and an exercise.
- [Concurrent debit tests with k6: lost updates and double spends](Concurrent%20debit%20tests%20with%20k6%20-%20lost%20updates%20and%20double%20spends.md): `http.batch()` bursts with `batchPerHost`, a balance invariant that catches lost updates, `count==1` thresholds that fail CI, and an exercise.
- [Testing payment webhooks: duplicates, out-of-order events and signatures](Testing%20payment%20webhooks%20-%20duplicates%2C%20out-of-order%20events%20and%20signatures.md): PSP retries, duplicate and out-of-order deliveries, HMAC signature and replay checks, Playwright tests with `expect.poll` and a "stays at" check, run against a safe and an unsafe service, and an exercise.
