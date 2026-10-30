---
Creation_date: 2026-10-21 16:55
Modification_date: Wednesday 21st October 2026 16:55:00
Indexes:
  - "[[permanent_notes]]"
  - "[[QA_Automation]]"
  - "[[Playwright]]"
  - "[[Module 1 - QA Automation for Edge Cases]]"
Source: docs (Playwright 1.64 API testing guide, Playwright for Java 1.63 API testing + JUnit integration, APIRequestContext + APIResponseAssertions reference, Authentication guide; IETF Idempotency-Key draft-07; Stripe idempotent requests)
---

----
# QA Lesson 2: Playwright API testing (APIRequestContext): auth, fixtures, idempotency keys, contract checks

> **Source type: official docs.** Written from the Playwright docs and checked 2026-10-21: **Playwright for Java 1.63.0** (Maven `com.microsoft.playwright:playwright`) and **Playwright for Node 1.64.1** (`@playwright/test`, 2026-10-14; Java usually trails Node by a release). API tests need **no browser at all**, which makes them fast and a good place to hit the edge cases from [[Test design for messaging and transaction edge cases]]. Java first (your daily stack), TypeScript second.

## Coming from Selenium + Java + TestNG
| You know (Selenium world) | Playwright equivalent |
|---|---|
| REST Assured / HttpClient next to WebDriver | `APIRequestContext`: same library for UI and API, shares cookies with a browser context if you want |
| `WebDriver` session per test | `BrowserContext` per test (cheap, isolated cookies/storage); API-only tests skip the browser entirely |
| Explicit waits (`WebDriverWait`, `ExpectedConditions`) | Auto-waiting actions + web-first assertions (`assertThat(locator).isVisible()` retries until timeout). Lesson 5 |
| TestNG `@BeforeClass` / `@AfterClass`, `ITestContext` | Java: JUnit `@BeforeAll`/`@AfterAll` or the JUnit `@UsePlaywright` fixtures (experimental). Node: `test.extend` fixtures. Lesson 3 |
| Login via UI, then reuse cookies | `storageState` saved once and reused |
| Selenium Grid for parallel runs | Node runner: built-in workers and `--shard`. Java: JUnit/TestNG parallelism, **one Playwright instance per thread** (not thread-safe) |
| Screenshots on failure | Trace viewer (`trace: 'on-first-retry'`): actions, network, DOM snapshots. Lesson 6 |
| Cucumber step defs | Still possible on top of Playwright Java; keep the HTTP client in a fixture, not in the steps |

Playwright for Java has **no test runner of its own**: you bring JUnit or TestNG. The JUnit integration (`@UsePlaywright`, which injects `Page`, `BrowserContext`, `APIRequestContext`, etc. as test parameters) is marked **experimental**, and the docs warn it's **not safe to use the same Playwright objects from multiple threads**, so with parallel JUnit/TestNG create one `Playwright` per thread ([Playwright Java: JUnit](https://playwright.dev/java/docs/junit)). TestNG works the same way with your own `@BeforeClass` setup.

## The idea
Playwright Test has a built-in **`request` fixture**: an `APIRequestContext` that sends HTTP requests and **respects `baseURL` and `extraHTTPHeaders`** from your config. Behind the scenes it calls `apiRequest.newContext()`, and you can call that yourself (`playwright.request.newContext({...})`) when you need a separately configured client, e.g. a second user or no auth ([API testing guide](https://playwright.dev/docs/api-testing)). Each context has its own **isolated cookie storage**.

Useful request options (per call, on `get/post/put/patch/delete/fetch`) from the [APIRequestContext reference](https://playwright.dev/docs/api/class-apirequestcontext):
- `data`: string, Buffer or a serialisable object (JSON-encoded for you). `form` / `multipart` for forms.
- `headers`, `params` (query string).
- `failOnStatusCode`: throw on non-2xx/3xx instead of returning the response.
- `timeout`: **default 30000 ms**; `0` disables it.
- `maxRedirects` (since 1.26), `maxRetries` (since 1.46: retries **network errors only**, currently just `ECONNRESET`, never HTTP status codes; default 0).

Assertion: `await expect(response).toBeOK()` checks the status is **200–299** ([APIResponseAssertions](https://playwright.dev/docs/api/class-apiresponseassertions)). It prints the response body on failure, which beats `expect(res.status()).toBe(200)`.


## Java example (Playwright for Java + JUnit; TestNG is the same with @BeforeClass/@AfterClass)
From the [Java API testing guide](https://playwright.dev/java/docs/api-testing): create `Playwright`, then `playwright.request().newContext(new APIRequest.NewContextOptions().setBaseURL(...).setExtraHTTPHeaders(headers))`. Per-request options go in `RequestOptions.create().setData(...).setHeader(...).setQueryParam(...)` ([RequestOptions](https://playwright.dev/java/docs/api/class-requestoptions)). Assertion: `assertThat(response).isOK()` (200–299, from `PlaywrightAssertions`; [APIResponseAssertions](https://playwright.dev/java/docs/api/class-apiresponseassertions)).

```java
import com.google.gson.*;
import com.microsoft.playwright.*;
import com.microsoft.playwright.options.RequestOptions;
import org.junit.jupiter.api.*;
import java.util.*;
import static com.microsoft.playwright.assertions.PlaywrightAssertions.assertThat;
import static org.junit.jupiter.api.Assertions.assertEquals;

@TestInstance(TestInstance.Lifecycle.PER_CLASS)
class PaymentIdempotencyTest {
    Playwright playwright;
    APIRequestContext api;

    @BeforeAll void setUp() {
        playwright = Playwright.create();
        api = playwright.request().newContext(new APIRequest.NewContextOptions()
            .setBaseURL(System.getenv().getOrDefault("API_URL", "http://localhost:8080"))
            .setExtraHTTPHeaders(Map.of("Authorization", "Bearer " + System.getenv("API_TOKEN"))));
    }
    @AfterAll void tearDown() { api.dispose(); playwright.close(); }

    APIResponse pay(String key, Map<String, Object> body) {
        return api.post("/payments", RequestOptions.create().setData(body).setHeader("Idempotency-Key", key));
    }

    @Test void sameKeyTwiceGivesSameResultAndOneCharge() {
        String key = UUID.randomUUID().toString();                     // unique per test: parallel-safe
        Map<String, Object> body = Map.of("orderId", "order-" + key, "amount", 10000, "currency", "VND");

        APIResponse first = pay(key, body);
        assertThat(first).isOK();
        APIResponse second = pay(key, body);
        assertThat(second).isOK();

        assertEquals(first.status(), second.status());                // same result
        assertEquals(json(first).get("paymentId"), json(second).get("paymentId"));

        APIResponse list = api.get("/payments", RequestOptions.create().setQueryParam("orderId", "order-" + key));
        assertEquals(1, JsonParser.parseString(list.text()).getAsJsonArray().size());   // no double effect
    }

    @Test void sameKeyDifferentPayloadIsRejected() {
        String key = UUID.randomUUID().toString();
        pay(key, Map.of("orderId", "o-1", "amount", 100));
        assertEquals(422, pay(key, Map.of("orderId", "o-1", "amount", 999)).status());   // or your API's documented code
    }

    static JsonObject json(APIResponse r) { return JsonParser.parseString(r.text()).getAsJsonObject(); }
}
```
For the concurrent same-key test in Java, fire the calls from an `ExecutorService` with a `CountDownLatch` (pattern in lesson 1), **each thread using its own `Playwright` + `APIRequestContext`** because Playwright objects aren't thread-safe. In TypeScript (below) `Promise.all` on one context is fine because Node is single-threaded.

## TypeScript (Playwright Test): config and auth
```ts
// playwright.config.ts
import { defineConfig } from '@playwright/test';
export default defineConfig({
  use: {
    baseURL: process.env.API_URL ?? 'http://localhost:8080',
    extraHTTPHeaders: { Accept: 'application/json', Authorization: `Bearer ${process.env.API_TOKEN}` },
  },
});
```
- **Token auth:** put it in `extraHTTPHeaders` (above) or per request in `headers`.
- **Cookie/session auth:** log in once, save `await request.storageState({ path: 'state.json' })`, and reuse it via `newContext({ storageState: 'state.json' })`. The [Authentication guide](https://playwright.dev/docs/auth) recommends a **setup project**: authenticate once in a project that all test projects depend on, save the state, and start each test already logged in.
- **Two users** (needed for "user A can't see B's order" tests): two contexts, each created with `playwright.request.newContext({ extraHTTPHeaders: { Authorization: ... } })`. Dispose them with `await ctx.dispose()`.

## TypeScript example: testing an idempotency key
Rules from the [IETF Idempotency-Key draft-07](https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/) (note: **an expired Internet-Draft, not an RFC**, so treat it as a common convention, and check your own API's spec): missing key on an endpoint that needs one → **400**; same key with a **different payload → 422**; same key while the first request is **still processing → 409**. Stripe's real-world version: retries with the same key **return the saved status code and body** (even a 500), keys are up to 255 chars, may be pruned after **24 hours**, and a different payload with the same key is an error ([Stripe: Idempotent requests](https://docs.stripe.com/api/idempotent_requests)).

```ts
// tests/payments.idempotency.spec.ts
import { test, expect } from '@playwright/test';
import { randomUUID } from 'node:crypto';

test('same Idempotency-Key twice → same result, one charge', async ({ request }) => {
  const key = randomUUID();                      // unique per test → safe in parallel
  const body = { orderId: `order-${key}`, amount: 10000, currency: 'VND' };

  const first = await request.post('/payments', { data: body, headers: { 'Idempotency-Key': key } });
  await expect(first).toBeOK();
  const second = await request.post('/payments', { data: body, headers: { 'Idempotency-Key': key } });
  await expect(second).toBeOK();

  // Same result: same status and the same resource id.
  expect(second.status()).toBe(first.status());
  expect((await second.json()).paymentId).toBe((await first.json()).paymentId);

  // No double effect: check the *effect*, not just the response.
  const list = await request.get('/payments', { params: { orderId: body.orderId } });
  expect(await list.json()).toHaveLength(1);
});

test('same key, different payload → 422', async ({ request }) => {
  const key = randomUUID();
  await request.post('/payments', { data: { orderId: 'o-1', amount: 100 }, headers: { 'Idempotency-Key': key } });
  const res = await request.post('/payments', { data: { orderId: 'o-1', amount: 999 }, headers: { 'Idempotency-Key': key } });
  expect(res.status()).toBe(422);               // or whatever your API spec says
});

test('concurrent requests with one key → one effect', async ({ request }) => {
  const key = randomUUID();
  const body = { orderId: `order-${key}`, amount: 5000 };
  const results = await Promise.all(
    Array.from({ length: 5 }, () => request.post('/payments', { data: body, headers: { 'Idempotency-Key': key } })),
  );
  const codes = results.map(r => r.status());
  expect(codes.every(c => c === 201 || c === 200 || c === 409)).toBe(true);   // no 500s
  const list = await request.get('/payments', { params: { orderId: body.orderId } });
  expect(await list.json()).toHaveLength(1);                                // the real invariant
});
```
The concurrent test is the one that finds real bugs (check-then-insert without a unique constraint: [[A9gqa8q-l1w]], [[G4-_ckYTtvo]]). `Promise.all` on one context sends the requests in parallel.

## Contract-style checks (cheap, inside Playwright)
Playwright has **no built-in JSON-schema validation**, so add a validator library. **Java:** validate `response.text()` against the JSON Schema from your OpenAPI file with e.g. networknt `json-schema-validator` (current 3.0.8; its API changed in 3.x, so follow its README), or keep the record-mapping approach: parse into a Java record with Gson/Jackson set to fail on unknown/missing fields. **TypeScript:** two common ones: **zod 4.x** (current 4.6.7) or **ajv 8.x** (current 8.20.0, validates real JSON Schema, e.g. from your OpenAPI file).
```ts
import { z } from 'zod';
const Payment = z.object({ paymentId: z.string(), status: z.enum(['PENDING', 'COMPLETED', 'FAILED']), amount: z.number().int() });

test('GET /payments/:id matches the contract', async ({ request }) => {
  const res = await request.get('/payments/pay-123');
  await expect(res).toBeOK();
  expect(res.headers()['content-type']).toContain('application/json');
  Payment.parse(await res.json());              // throws with a readable diff if a field is renamed or retyped
});
```
This is **provider-side schema checking**: it catches a renamed field or a new enum value. It isn't consumer-driven contract testing; for that, see Pact in lesson 1's strategy section.

## What breaks / how to test it
- **Only asserting the response**: the second call returns 200 with the same id, but a second row or second charge was still written → always assert the effect (list endpoint, DB, or fake downstream call count).
- **Hard-coded idempotency keys or order ids**: tests collide when run in parallel or re-run against a shared env → generate with `randomUUID()` per test (lesson 3 covers test data).
- **Key reuse with a changed payload silently accepted**: the server returns the old result for a new request → test for 422 (or your API's documented code).
- **Concurrent same-key requests**: race between "check key" and "store key" → the `Promise.all` test above; repeat it (`--repeat-each=20`) when hunting a race.
- **Key expiry**: a retry after the key was pruned (Stripe: ≥24 h) creates a new payment → document it; test it with a test-only TTL override if the service has one.
- **Leaking auth between tests**: one shared context with cookies from an earlier test → use per-test `request` (default) or dispose your own contexts.

## How it connects to the core topics
- **Core focus:** retries and idempotency, duplicates, races, contract drift that turns into poison messages.
- **In practice:** pick one POST endpoint that should be idempotent and write the three tests above against a test env.

## Related
[[Module 1 - QA Automation for Edge Cases]] · [[Test design for messaging and transaction edge cases]] · [[A9gqa8q-l1w]] · [[G4-_ckYTtvo]] · [[inUimYVAGv0]] · [[Idempotent Consumer]]

---
## Flash cards section
Does Playwright for Java have its own test runner?::No. You use JUnit or TestNG. The JUnit @UsePlaywright fixtures are experimental, and Playwright objects aren't thread-safe, so use one Playwright instance per thread in parallel runs.
What replaces Selenium explicit waits in Playwright?::Auto-waiting actions plus web-first assertions (assertThat(locator)...) that retry until a timeout.
What is Playwright's request fixture (Node)?::A built-in APIRequestContext that respects baseURL and extraHTTPHeaders from the config. It calls apiRequest.newContext() behind the scenes.
What does expect(response).toBeOK() check?::That the status is in 200–299. On failure it shows the response, which is more useful than comparing status codes.
How do you test that an idempotency key prevents a double effect?::Send the same request with the same key twice (and concurrently), assert the same status and resource id, then assert the effect happened once (e.g. the list endpoint returns 1 payment).
In the IETF Idempotency-Key draft, what codes are suggested for missing key, different payload, and still-processing?::400 missing, 422 same key with a different payload, 409 retried while the original is still processing. It's an expired draft, so follow your API's own spec.
What's the default timeout of an APIRequestContext request, and what does maxRetries retry?::30 s (0 disables it). maxRetries (since 1.46) retries network errors only, not HTTP error statuses.
