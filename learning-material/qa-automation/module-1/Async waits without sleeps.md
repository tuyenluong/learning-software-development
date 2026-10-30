---
Creation_date: 2026-10-21 18:00
Modification_date: Wednesday 21st October 2026 18:00:00
Indexes:
  - "[[permanent_notes]]"
  - "[[QA_Automation]]"
  - "[[Playwright]]"
  - "[[Module 1 - QA Automation for Edge Cases]]"
Source: docs (Awaitility 4.3.0 usage wiki, Playwright 1.64 assertions, Testcontainers Java 2.0.5 "Waiting for containers to start", testcontainers-go v0.44.0 wait package, testify v1.12.1, spring-kafka-test 4.1.1)
---

----
# QA Lesson 5: Async waits without sleeps (Awaitility, Playwright expect.poll / toPass, Testcontainers wait strategies)

> **Source type: official docs and source**, checked 2026-10-21: **Awaitility 4.3.0**, Playwright **1.64.1** (Node) / **1.63.0** (Java), Testcontainers Java **2.0.5**, testcontainers-go **v0.44.0**, testify **v1.12.1**. Every messaging test in lessons 1 and 4 has a gap between "I published" and "the consumer did the work". This lesson is how to wait across that gap without `Thread.sleep`.

## The idea
`Thread.sleep(5000)` is wrong twice: **too long** when the system is fast (slow suite) and **too short** when CI is slow (flaky test). Instead, **poll for the condition with a timeout**: check every 100 ms, pass as soon as it's true, fail with a clear message if it's still false at the deadline. You already know this from Selenium's `WebDriverWait` + `ExpectedConditions`; the tools below are the same idea for databases, queues and APIs.

There are three different waits, and mixing them up is a common source of flakiness:
1. **Infrastructure ready**: the container/broker accepts connections → Testcontainers wait strategies.
2. **App ready**: your consumer has joined the group and got its partitions → framework hooks (`ContainerTestUtils.waitForAssignment`).
3. **Outcome reached**: the row exists, the DLT has 1 record → Awaitility / `expect.poll` / `toPass` / `EventuallyWithT`.

## 1. Java: Awaitility (first choice on the JVM)
From the [Awaitility usage guide](https://github.com/awaitility/awaitility/wiki/Usage):
- **Defaults:** timeout **10 s**, poll interval **100 ms**, poll delay **100 ms** (same as the interval unless you set it). Change globally with `Awaitility.setDefaultTimeout(...)` or `-Dawaitility.defaultTimeout=PT5S`.
- `untilAsserted(() -> { assertThat(...)... })` reuses normal AssertJ/JUnit/TestNG assertions; the last failure message is shown on timeout (`ConditionTimeoutException`).
- `ignoreExceptions()` for conditions that throw until ready (e.g. a 404 before the record exists).
- `await("payment saved")` names the wait, so the failure tells you *which* one timed out.
- **`during(...)`** (since 4.0.2) asserts a condition **stays true** for a period. This is the tool for "no second effect" in duplicate tests.

```java
import static org.awaitility.Awaitility.await;

// Outcome reached: the row exists (passes as soon as it does)
await("payment saved").atMost(Duration.ofSeconds(15)).pollInterval(Duration.ofMillis(200))
    .untilAsserted(() -> assertThat(repo.count("pay-123")).isEqualTo(1));

// Duplicate test: it must STAY at 1, not just reach 1.
// Without this, the test can pass before the duplicate has even been consumed.
await().during(Duration.ofSeconds(2)).atMost(Duration.ofSeconds(5))
    .until(() -> repo.count("pay-123"), count -> count == 1);
```
Better still for duplicates: send a **marker message after the duplicate** on the same partition/queue and wait until the marker is processed. Then you *know* the duplicate was handled (ordering guarantees it) and you don't depend on a fixed `during` window.

**App ready (Spring Kafka):** wait for partition assignment before publishing, or the first message can be missed with `auto.offset.reset=latest`:
```java
@Autowired KafkaListenerEndpointRegistry registry;
@BeforeEach void consumersReady() {
    registry.getListenerContainers().forEach(c -> ContainerTestUtils.waitForAssignment(c, 3)); // 3 = partitions
}
```
(`ContainerTestUtils` and `KafkaTestUtils.getRecords(consumer, timeout, minRecords)` are in `spring-kafka-test`.)

**Playwright for Java:** locator assertions (`assertThat(locator).isVisible()`) auto-retry, but there's **no `expect.poll` in Java**. For API or DB outcomes in Playwright-Java tests, use Awaitility around the `APIRequestContext` call.

## 2. TypeScript: Playwright `expect.poll` and `toPass`
From [Playwright assertions](https://playwright.dev/docs/test-assertions):
- **`expect.poll(fn, { timeout, intervals, message })`** turns a sync assertion into a polling one. Default timeout **5 s** (`0` disables it); default intervals **`[100, 250, 500, 1000]`** ms.
- **`expect(async () => { ...several asserts... }).toPass({ timeout, intervals })`** retries a whole block. **By default `toPass` has timeout 0 (no limit) and ignores the custom expect timeout**, so always pass a `timeout`, or a broken test hangs until the test timeout.

```ts
await expect.poll(async () => {
  const res = await request.get('/payments', { params: { orderId } });
  return (await res.json()).length;
}, { message: 'payment row created', timeout: 15_000 }).toBe(1);

await expect(async () => {
  const res = await request.get(`/orders/${orderId}`);
  await expect(res).toBeOK();
  expect((await res.json()).status).toBe('SHIPPED');
}).toPass({ timeout: 15_000, intervals: [250, 500, 1000] });
```

## 3. Infrastructure: Testcontainers wait strategies
- **Java default:** wait up to **60 s** for the container's first mapped port to listen; change with `withStartupTimeout(...)`, or replace via `waitingFor(...)` ([Waiting for containers](https://java.testcontainers.org/features/startup_and_waits/)). The `Wait` class offers `forListeningPort()`, `forHttp(path).forStatusCode(200)`, `forLogMessage(regex, times)`, `forHealthcheck()`, `forSuccessfulCommand(cmd)`. The Kafka/RabbitMQ/Postgres modules already set sensible strategies; you mostly need this for `GenericContainer` (your own service image, a fake API).
- **Go (`wait` package):** `wait.ForLog("ready").WithOccurrence(2).WithStartupTimeout(...)`, `wait.ForListeningPort("5672/tcp")`, `wait.ForHTTP("/health")`, `wait.ForSQL(...)`, `wait.ForHealthCheck()`, `wait.ForAll(...)`. `postgres.BasicWaitStrategies()` waits for the "ready" log line twice plus the port (Postgres restarts once during init).
- **Port open ≠ ready.** Postgres opens its port during init and restarts; RabbitMQ accepts TCP before the vhost is ready. That's why the modules wait for log lines too.

```java
GenericContainer<?> fakePaymentProvider = new GenericContainer<>("wiremock/wiremock:3.9.1")
    .withExposedPorts(8080)
    .waitingFor(Wait.forHttp("/__admin/health").forStatusCode(200))
    .withStartupTimeout(Duration.ofSeconds(90));
```
(Pin your own image tag; the tag above is an example.)

## 4. Go outcomes: testify `EventuallyWithT`
```go
require.EventuallyWithT(t, func(c *assert.CollectT) {
    assert.Equal(c, 1, countPayments(t, db, "pay-123"))
}, 15*time.Second, 200*time.Millisecond)
```
`EventuallyWithT` collects assertion failures per tick and reports the last one; plain `Eventually` only takes a `func() bool` and gives a vague message.

## What breaks / how to test it
- **`sleep` instead of polling** → slow when fast, flaky when slow. Grep the suite for `Thread.sleep`, `waitForTimeout`, `time.Sleep`.
- **"Reached" instead of "stays"** for negative/duplicate checks → passes before the duplicate is consumed. Use `during(...)` or a marker message.
- **Waiting for the wrong thing**: polling the DB while the consumer hasn't joined the group yet → you poll for 15 s and fail. Wait for assignment first.
- **Unbounded waits** (`toPass` without timeout) → hung CI jobs instead of red tests.
- **Timeouts tuned to a laptop** → CI is 2–5× slower. Set timeouts from CI measurements, keep the poll interval short.
- **Polling something with side effects** (a POST in the poll) → you create the duplicates you're testing for. Poll with GETs/reads only.

## How it connects to the core topics
- **Core focus:** async consumers, consumer lag and rebalancing (assignment waits), duplicates (the "stays at 1" assertion).
- **In practice:** AWS Step Functions and Lambda checks are the same problem. Awaitility around `DescribeExecution` or a DynamoDB `GetItem` replaces fixed sleeps there too.

## Related
[[Module 1 - QA Automation for Edge Cases]] · [[Testcontainers for Kafka and RabbitMQ (Java and Go)]] · [[Test design for messaging and transaction edge cases]] · [[Out-of-order messages and consumer rebalancing]]

---
## Flash cards section
What are Awaitility's defaults?::Timeout 10 s, poll interval 100 ms, poll delay 100 ms (same as the interval unless set).
How do you assert "the duplicate didn't create a second row" without a sleep?::Awaitility during(...) to require count == 1 for a period, or better, send a marker message after the duplicate and wait until the marker is processed.
expect.poll vs toPass in Playwright?::expect.poll polls one value (default 5 s timeout, intervals 100/250/500/1000 ms). toPass retries a whole block, and its default timeout is 0 (no limit), so always set one.
What's the Testcontainers Java default startup wait?::Up to 60 s for the first mapped port to listen. Override with withStartupTimeout() or waitingFor(Wait.forHttp/forLogMessage/forHealthcheck…).
Why wait for Kafka partition assignment before publishing in a test?::With auto.offset.reset=latest, a consumer that joins after the message was sent starts past it and never sees it. ContainerTestUtils.waitForAssignment avoids that.
