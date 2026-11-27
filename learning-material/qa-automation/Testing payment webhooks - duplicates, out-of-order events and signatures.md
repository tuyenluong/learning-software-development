---
Creation_date: 2026-11-27 22:30
Modification_date: Friday 27th November 2026 22:30:00
Indexes:
  - "[[permanent_notes]]"
  - "[[QA_Automation]]"
  - "[[Playwright]]"
Source: docs (Stripe "Receive Stripe events in your webhook endpoint"; Playwright docs for APIRequestContext, expect.poll and webServer)
---

----
# Testing payment webhooks: duplicates, out-of-order events and signatures

> **Source type: official docs**, checked 2026-11-27 against the [Stripe webhooks guide](https://docs.stripe.com/webhooks) and **Playwright 1.65.1**. The tests below were run against a small local merchant service in two modes (unsafe: every delivery moves money and the last event wins; safe: event-id dedupe and forward-only status). Builds on [Test design for messaging and transaction edge cases](module-1/Test%20design%20for%20messaging%20and%20transaction%20edge%20cases.md), [Playwright API testing (APIRequestContext)](module-1/Playwright%20API%20testing%20(APIRequestContext).md) and [Async waits without sleeps](module-1/Async%20waits%20without%20sleeps.md).

## Why this matters

A payment provider (PSP) tells the merchant system what happened by calling its webhook endpoint. That call is a message, so it has the same problems as a queue consumer: it can arrive twice, late, or out of order. Payments QA postings now ask for this directly: "API testing patterns (Authentication, Idempotency, Retries, Webhooks)", "mock services/stubs for external PSPs, banking rails, and webhooks", "settlement, reconciliation".

What the Stripe guide says a receiver must cope with ([source](https://docs.stripe.com/webhooks)):

| Behaviour | What the docs say | What to test |
|---|---|---|
| **Retries** | live mode retries delivery "for up to three days with an exponential back off"; sandbox retries three times over a few hours | a redelivery hours later must not move money again |
| **Duplicates** | endpoints "might occasionally receive the same event more than once"; log processed event IDs and skip them. Sometimes two separate Event objects are sent: then match on `data.object` id + `event.type` | same event id twice, also in parallel → one ledger movement |
| **Ordering** | Stripe "doesn't guarantee the delivery of events in the order that they're generated"; don't use `created` to order events (several can share a second) | refund before success → final state is still "refunded" |
| **Signatures** | the `Stripe-Signature` header holds `t=<timestamp>` and one or more `v1=<HMAC-SHA256>` over `<t>.<raw body>`; verify on the **raw** body; ignore other schemes | wrong secret → 4xx, no side effect; a changed body → 4xx |
| **Replays** | libraries reject a timestamp older than **5 minutes** by default; a tolerance of 0 disables the check; each retry gets a new timestamp and signature | old timestamp with a valid signature → 4xx |
| **Fast 2xx** | return 2xx "before any complex logic that could cause a timeout" | the endpoint answers first, so the test must **poll** for the effect |

The last row is why webhook tests are async tests: a 200 only means "received". The money moves later.

## The tests (Playwright Test, TypeScript)

The service under test exposes `POST /webhooks/psp` (header `psp-signature: t=...,v1=...`, the same scheme as Stripe) and `GET /payments/:id` returning `{ status, ledger }`. The test signs its own events with the shared test secret, so no PSP sandbox is needed in CI.

```typescript
import { test, expect, APIRequestContext } from '@playwright/test';
import crypto from 'node:crypto';

const SECRET = process.env.WEBHOOK_SECRET ?? 'whsec_test';

function signedHeaders(body: string, t = Math.floor(Date.now() / 1000), secret = SECRET) {
  const v1 = crypto.createHmac('sha256', secret).update(`${t}.${body}`).digest('hex');
  return { 'content-type': 'application/json', 'psp-signature': `t=${t},v1=${v1}` };
}

function event(type: 'payment.succeeded' | 'payment.refunded', paymentId: string, amount = 5000) {
  return { id: `evt_${crypto.randomUUID()}`, type, data: { object: { id: paymentId, amount } } };
}

async function deliver(request: APIRequestContext, evt: object, headers?: Record<string, string>) {
  const body = JSON.stringify(evt);                // send these exact bytes; they are what is signed
  return request.post('/webhooks/psp', { data: body, headers: headers ?? signedHeaders(body) });
}

async function payment(request: APIRequestContext, id: string) {
  const r = await request.get(`/payments/${id}`);
  return r.ok() ? r.json() : null;
}

// Fails as soon as one read in the window differs (a "stays at" check, like Awaitility's during()).
async function expectStays(read: () => Promise<unknown>, expected: unknown, windowMs = 500) {
  const end = Date.now() + windowMs;
  while (Date.now() < end) {
    expect(await read()).toEqual(expected);
    await new Promise(r => setTimeout(r, 100));
  }
}

test('a duplicate delivery moves money once', async ({ request }) => {
  const pay = `pay_${crypto.randomUUID()}`;
  const evt = event('payment.succeeded', pay);
  // Same event id three times: two retries in parallel, one late redelivery.
  const answers = await Promise.all([deliver(request, evt), deliver(request, evt)]);
  answers.push(await deliver(request, evt));
  for (const a of answers) expect(a.status()).toBe(200);
  await expect.poll(() => payment(request, pay)).toEqual({ status: 'succeeded', ledger: 5000 });
  // Keep reading for a short window: a late duplicate must not move money after the poll passed.
  await expectStays(() => payment(request, pay), { status: 'succeeded', ledger: 5000 });
});

test('refund delivered before success still ends refunded', async ({ request }) => {
  const pay = `pay_${crypto.randomUUID()}`;
  expect((await deliver(request, event('payment.refunded', pay))).status()).toBe(200);
  expect((await deliver(request, event('payment.succeeded', pay))).status()).toBe(200);
  await expect.poll(() => payment(request, pay)).toEqual({ status: 'refunded', ledger: 0 });
});

test('a bad signature is rejected and changes nothing', async ({ request }) => {
  const pay = `pay_${crypto.randomUUID()}`;
  const evt = event('payment.succeeded', pay);
  const body = JSON.stringify(evt);
  const r = await deliver(request, evt, signedHeaders(body, undefined, 'whsec_wrong'));
  expect(r.status()).toBe(400);
  await expectStays(() => payment(request, pay), null); // nothing may appear later either
});

test('a replayed delivery with an old timestamp is rejected', async ({ request }) => {
  const pay = `pay_${crypto.randomUUID()}`;
  const evt = event('payment.succeeded', pay);
  const body = JSON.stringify(evt);
  const tenMinutesAgo = Math.floor(Date.now() / 1000) - 600;
  const r = await deliver(request, evt, signedHeaders(body, tenMinutesAgo));
  expect(r.status()).toBe(400);
  await expectStays(() => payment(request, pay), null); // nothing may appear later either
});
```

```typescript
// playwright.config.ts
import { defineConfig } from '@playwright/test';
export default defineConfig({
  testDir: 'tests',
  use: { baseURL: process.env.BASE_URL ?? 'http://localhost:3100' },
  webServer: { command: 'node server.mjs', port: 3100, reuseExistingServer: false },
});
```

| Piece | Why | Doc |
|---|---|---|
| `request.post(url, { data: body })` with `body` a **string** | a string is sent as is; an object would be re-serialised by Playwright, and the signature must cover the exact bytes | [APIRequestContext.post](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-post) |
| `Promise.all([deliver(), deliver()])` | two copies of one event at the same moment, like two overlapping retries | – |
| `expect.poll(...)` | waits for the async effect instead of a sleep | [expect.poll](https://playwright.dev/docs/test-assertions#expectpoll) |
| `expectStays(...)` | a "stays at" check: `expect.poll` passes on the first good read, so a late duplicate could still slip in after it | – |
| `webServer.port` | starts the service before the tests; `port` is used because the service has no health URL that returns 2xx | [webServer](https://playwright.dev/docs/test-webserver) |

## Run results (27 Nov 2026, Playwright 1.65.1, Node 24)

| Test | unsafe service | safe service |
|---|---|---|
| duplicate delivery moves money once | **fails**: ledger **15000**, expected 5000 (all three copies applied) | passes |
| refund before success ends refunded | **fails**: status **"succeeded"**, ledger 0 | passes |
| bad signature rejected | passes | passes |
| old timestamp rejected | passes | passes |

The ordering bug is the instructive one: the ledger is correct (0), only the status is wrong, because the late `payment.succeeded` overwrote `refunded`. A test that checks only the money would pass. Assert on **both** the ledger and the state.

## Design notes

- **Dedupe on the event id, in the same transaction as the effect.** An in-memory `Set` works in a single-process demo; a real service needs a unique constraint (e.g. a `processed_events(event_id)` table) written in the same database transaction as the ledger row, or two parallel deliveries can both pass the "seen?" check.
- **Make state transitions forward-only.** Rank the states (`pending < succeeded < refunded`) and ignore an event that would move backwards, or re-read the object from the PSP API when an event arrives, as the Stripe guide suggests for missing objects.
- **Duplicates without the same event id.** Stripe notes that sometimes two separate events are sent for one change; add a test with two different event ids for the same `data.object` id and type, and decide with the team what the expected result is.
- **Test the verifier on the raw body.** A framework that parses JSON before verification breaks signatures. Send a body with extra whitespace or reordered keys, signed as sent: it must pass. Change one byte after signing: it must fail.
- **Keep the signing secret out of the test code.** Read it from an environment variable that holds a test-only secret, as above.

## Exercise

1. Build the two-endpoint service (or point the tests at a real one) and run the four tests in unsafe mode first. Confirm the two failures above.
2. Fix dedupe and ordering, and confirm all four pass three runs in a row.
3. Add a test: one event with **two** `v1` signatures, one made with an old secret and one with the current secret (the secret-rolling case in the Stripe guide). Expect 200.
4. Add a test: the endpoint takes 2 s to process. Assert the webhook answer still arrives in under 500 ms and the effect appears later.
5. Move dedupe into a database with a unique key and rerun test 1 with ten parallel copies.

## Sources
- [Stripe: Receive Stripe events in your webhook endpoint](https://docs.stripe.com/webhooks) (automatic retries, event ordering, duplicate events, signature verification, replay attacks, quick 2xx)
- [Playwright: APIRequestContext.post](https://playwright.dev/docs/api/class-apirequestcontext#api-request-context-post)
- [Playwright: expect.poll](https://playwright.dev/docs/test-assertions#expectpoll)
- [Playwright: web server](https://playwright.dev/docs/test-webserver)
- Related note: [Concurrent debit tests with k6: lost updates and double spends](Concurrent%20debit%20tests%20with%20k6%20-%20lost%20updates%20and%20double%20spends.md) (same invariants for parallel API requests)
