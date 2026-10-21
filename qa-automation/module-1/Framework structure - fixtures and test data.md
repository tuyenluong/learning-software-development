---
Creation_date: 2026-10-21 17:10
Modification_date: Wednesday 21st October 2026 17:10:00
Indexes:
  - "[[permanent_notes]]"
  - "[[QA_Automation]]"
  - "[[Playwright]]"
  - "[[Module 1 - QA Automation for Edge Cases]]"
Source: docs (Playwright 1.64 Fixtures, TestInfo, Parallelism; JUnit 6.1 user guide; Faker.js 10.x)
---

----
# QA Lesson 3: Framework structure: fixtures and test data

> **Source type: official docs.** Checked 2026-10-21 against Playwright **1.64.1**, JUnit **6.1.3** (JUnit 6 is the current major; Jupiter API is the same `org.junit.jupiter.api`), AssertJ **3.27.7**, Faker.js **10.6.0**. Builds on lesson 2's tests: same idea, organised so 200 tests stay readable and don't step on each other.

## The idea
A good test framework has three layers:
1. **Fixtures**: *how a test gets what it needs* (an API client logged in as a user, a clean order, a Kafka consumer on the output topic) and *how it's cleaned up*.
2. **Test data builders**: *what the data looks like*, with sensible defaults so each test only states what matters ("an order with amount 0").
3. **Tests**: arrange → act → assert the invariants from [[Test design for messaging and transaction edge cases]]. No setup noise.

The rule that ties them together: **every test creates its own data and owns it.** No test depends on data another test created, and nothing depends on run order. That's what makes parallel runs and retries safe (lesson 6).

## Playwright fixtures (`test.extend`)
From the [Fixtures guide](https://playwright.dev/docs/test-fixtures):
- A fixture is a function: code **before `await use(value)` is setup, code after it is teardown**. Teardown runs even if the test fails.
- Fixtures are **on demand**: only set up if a test (or another fixture) asks for them.
- **Test-scoped** (default) = fresh per test. **Worker-scoped** (`{ scope: 'worker' }`, tuple syntax) = once per worker process, good for expensive things like a DB connection pool.
- **`{ auto: true }`** = runs for every test even if not listed (e.g. attach logs on failure).
- `testInfo.workerIndex` is unique per worker process; `testInfo.parallelIndex` is between 0 and workers−1 and is **guaranteed different for workers running at the same time** ([TestInfo](https://playwright.dev/docs/api/class-testinfo)). Use `parallelIndex` to give each worker its own slot (e.g. its own tenant or DB schema).
- Default parallelism: **test files run in parallel; tests inside one file run in order in the same worker** unless you set `fullyParallel: true` ([Parallelism](https://playwright.dev/docs/test-parallel)).

```ts
// fixtures.ts
import { test as base, expect, APIRequestContext } from '@playwright/test';
import { randomUUID } from 'node:crypto';

type Order = { id: string; amount: number };
type Fixtures = { runId: string; order: Order; asOtherUser: APIRequestContext };

export const test = base.extend<Fixtures>({
  runId: async ({}, use) => { await use(randomUUID().slice(0, 8)); },        // unique per test

  order: async ({ request, runId }, use) => {
    const res = await request.post('/orders', { data: { ref: `qa-${runId}`, amount: 10000 } });
    await expect(res).toBeOK();
    const order = await res.json();
    await use(order);                                                         // ← test runs here
    await request.delete(`/orders/${order.id}`);                              // teardown, even on failure
  },

  asOtherUser: async ({ playwright, baseURL }, use) => {
    const ctx = await playwright.request.newContext({
      baseURL, extraHTTPHeaders: { Authorization: `Bearer ${process.env.OTHER_USER_TOKEN}` },
    });
    await use(ctx);
    await ctx.dispose();
  },
});
export { expect };

// orders.spec.ts
import { test, expect } from './fixtures';
test('another user cannot read my order', async ({ order, asOtherUser }) => {
  expect((await asOtherUser.get(`/orders/${order.id}`)).status()).toBe(404);
});
```

## JUnit 6 / Java side
JUnit has no `use()`; the same ideas map to:
- `@BeforeEach` / `@AfterEach` for per-test setup/teardown; `@BeforeAll` (static) for per-class.
- **Extensions** (`@ExtendWith`, `BeforeEachCallback`, `ParameterResolver`) for reusable fixtures that inject objects into test parameters, which is how Testcontainers and Spring's test support plug in (lesson 4).
- `@TempDir` for throw-away files; `@RepeatedTest(n)` for race tests ([JUnit User Guide](https://docs.junit.org/current/user-guide/)).

**Test data builder** (plain Java, works with any framework):
```java
class PaymentBuilder {
    private String id = "pay-" + UUID.randomUUID();      // unique by default
    private String orderId = "order-" + UUID.randomUUID();
    private long amount = 100_00;
    private String currency = "VND";
    static PaymentBuilder aPayment() { return new PaymentBuilder(); }
    PaymentBuilder withAmount(long a) { this.amount = a; return this; }
    PaymentBuilder withId(String id) { this.id = id; return this; }   // reuse an id to build a duplicate
    PaymentRequested build() { return new PaymentRequested(id, orderId, amount, currency); }
}

// The test states only what matters:
var msg = aPayment().withAmount(0).build();
var dup = aPayment().withId(msg.id()).build();           // same id = a duplicate delivery
```

## Deterministic test data
- **Unique, not random-and-forgotten.** Ids should be unique per test (UUID, or `runId` + counter) so parallel tests and re-runs never collide. Put the run id into names (`qa-${runId}`) so you can find and clean up leftovers.
- **Random content must be reproducible.** If you use Faker, set a seed: `faker.seed(1234)` makes the same values come out every run ([Faker API](https://fakerjs.dev/api/faker.html)). Log the seed; when a test fails, re-run with that seed. Random data with no seed = a flaky test you can't reproduce.
- **Time is test data too.** "Expires in 24 h", "end of month", time zones (Tuyen's env is UTC+7, CI is usually UTC). Inject a clock (`java.time.Clock` in Java) or pass the timestamp in the data; never compare against `now()` taken in a different place.
- **Order is test data too.** `SELECT` without `ORDER BY`, a `HashMap`, or Kafka records across partitions have no guaranteed order. Assert on sets/sorted lists, or sort before comparing.
- **Seed shared reference data once** (currencies, products) in a worker fixture or a migration, read-only. Anything a test changes must be created by that test.

## What breaks / how to test it
- **Shared mutable data** (`user1` used by 30 tests): passes alone, fails in parallel → per-test fixtures with unique ids.
- **Order-dependent tests** (test B reads what test A created): pass in the IDE, fail with sharding or `fullyParallel` → each test creates its own data. Find them by running with `--fully-parallel` and a shuffled order, or a single test alone with `-g`.
- **Teardown that never runs** (cleanup at the end of the test body, skipped when an assertion fails) → teardown goes after `await use()` or in `@AfterEach`.
- **Leaky worker fixtures**: a worker-scoped object holding per-test state (cookies, a consumer offset) → keep worker fixtures stateless or reset them.
- **Unseeded randomness / wall-clock time** → seed + log, inject the clock.
- **Messaging-specific:** a test consumer on a shared topic picks up *another* test's messages → filter by your test's `runId` in the key or a header, or give each test its own topic/queue (cheap with Testcontainers, lesson 4).

## How it maps to the learning focus
- **Core focus:** duplicates (builders make "same id twice" a one-liner), races (`@RepeatedTest`, unique data per thread), test isolation for messaging.
- **Your QA work:** look at your current framework. Is there any test that only passes after another one? Any hard-coded user shared by many tests? Those are your flaky-test candidates for lesson 6.

## Related
[[Module 1 - QA Automation for Edge Cases]] · [[Playwright API testing (APIRequestContext)]] · [[Test design for messaging and transaction edge cases]]

---
## Flash cards section
In a Playwright fixture, what runs before and after await use()?::Before is setup, after is teardown. Teardown runs even when the test fails.
Test-scoped vs worker-scoped fixture?::Test-scoped (default) is created fresh for each test. Worker-scoped ({ scope: 'worker' }) is created once per worker process, for expensive shared things.
workerIndex vs parallelIndex?::workerIndex is unique per worker process (a restarted worker gets a new one). parallelIndex is 0..workers-1 and differs between workers running at the same time, so it's good for per-worker slots.
How do you keep Faker data reproducible?::Call faker.seed(n), log the seed, and re-run with the same seed when a test fails.
What's the core rule for test data in parallel suites?::Each test creates and owns its data, with unique ids. No test depends on another test's data or on run order.
