---
Creation_date: 2026-11-13
Modification_date: Friday 13th November 2026
Indexes:
  - "[[permanent_notes]]"
  - "[[QA_Automation]]"
  - "[[Pact contract testing]]"
Source: docs — https://docs.pact.io/consumer; @pact-foundation/pact 17.1.4 (Pact === PactV4, default spec V4); checked 2026-11-13
---

# Writing a consumer test

## What is the topic?

A Pact consumer test is an automated test that runs on the *client* side. It starts a mock provider, states one interaction, and points your real HTTP client at that mock. If the client sends the request you described and can handle the mocked response, Pact writes a pact file.

In `@pact-foundation/pact` 17.1.4, `Pact` is the same class as `PactV4`. The default specification is V4. You do not set a specification version unless you are deliberately targeting an older one.

## What does it do?

- Replaces the real provider with a mock server for the duration of the test.
- Records the interaction into `./pacts/{consumer}-{provider}.json` — but only when the `executeTest` callback passes and the expected request arrived.
- Forces you to use the mock's real address. The mock server binds a **random port**, so you must always read `mockServer.url` (or the host/port on that object). Hard-coding `localhost:1234` will flake.

The pact file is the artefact the provider will verify later. If the callback fails, there is no new pact file to publish. That is deliberate: a failing client should not emit a contract.

## How does it work?

The fluent chain, in this order:

```
addInteraction()
  .given(...)
  .uponReceiving(...)
  .withRequest(method, path, builder)
  .willRespondWith(status, builder)
  .executeTest(async mockServer => { ... })
```

- `given` is the provider state (optional second argument: params). The provider must later register a `stateHandlers` entry with this exact string.
- `uponReceiving` is a human-readable name for the interaction. Together with `given`, it must be unique.
- `withRequest` describes what the client will send.
- `willRespondWith` describes what the mock will return, usually with matchers (lesson 3).
- `executeTest` runs your client against `mockServer.url`. Always `await` it.

The `Pact` class is not thread-safe. Give each parallel test its own instance, or run Jest with `--runInBand`. Use `testEnvironment: 'node'` (not jsdom). There is no official Vitest guide.

Do not install `pact-core` directly. The native engine arrives through optional dependencies of `@pact-foundation/pact`.

Compared with Pact JVM: Java tests typically use `@Pact` / `@PactTestFor` annotations and default to specification V3; JavaScript uses this fluent chain and defaults to V4. Output here is `./pacts`, not `target/pacts`.

## Step-by-step: how do I achieve the goal?

1. Install `@pact-foundation/pact` 17.1.4 on Node 22+. Confirm `node -v` is 22 or newer.
2. Create a test file. Import `Pact` and `Matchers` from `@pact-foundation/pact`.
3. Construct `new Pact({ consumer, provider, dir })`. Set `dir` to `path.resolve(process.cwd(), 'pacts')` so the file lands in `./pacts`.
4. Chain one interaction as above. Keep `given` and `uponReceiving` specific.
5. In `willRespondWith`, add headers and a JSON body. Use matchers for any value that should not be compared literally. Leave the exact matcher choices for lesson 3 if you are unsure — but do not paste a complete body from a tutorial and call it done.
6. In `executeTest`, configure your *real* client with `mockServer.url` and make the call. Assert only what the client does with the response.
7. Run the test. If it passes, open `./pacts/{consumer}-{provider}.json` and check that the interaction is there. If the file is missing, the callback did not pass, or the expected request never arrived.

## What is its usage?

Write one consumer test per interaction (or a small cluster of closely related ones on a single Pact instance, sequentially). Typical cases:

- `GET` a resource the UI already renders.
- `POST` a payload the client already builds, and the status / body it already handles.
- A 404 or 409 the client already has a branch for — if the client uses that response, it belongs in the contract.

The consumer name and provider name become the pact file name. Pick stable names; renaming them later looks like a new pair of services to the broker.

## Examples / code

Scaffolding only. Fill in the blanks. This should not pass if you run it unchanged.

```ts
import { Pact, Matchers } from '@pact-foundation/pact';
import path from 'path';

const { like, integer, eachLike } = Matchers;

// YOUR TURN: import (or write) the real checkout client, not a raw
// fetch copy-pasted into the test.
// import { OrderClient } from '../src/orderClient';

const pact = new Pact({
  consumer: 'CheckoutWeb',
  provider: 'OrderService',
  dir: path.resolve(process.cwd(), 'pacts'),
});

await pact
  .addInteraction()
  .given('order 42 exists')
  .uponReceiving('a request for order 42')
  .withRequest('GET', '/orders/42', (b) =>
    b.headers({ Accept: 'application/json' }),
  )
  .willRespondWith(200, (b) => {
    // YOUR TURN: headers + jsonBody with matchers
    // Use like / integer / eachLike for values the client should
    // not pin to a single literal. Which fields does CheckoutWeb
    // actually read? Do not add fields it ignores.
    //
    // b.headers({ ... })
    // b.jsonBody({ ... })
  })
  .executeTest(async (mockServer) => {
    // YOUR TURN: call real client with mockServer.url
    // Random port — do not hard-code a URL. Assert only what
    // the client uses from the response.
    //
    // Why would `await fetch('http://localhost:1234/orders/42')` be wrong?
  });
```

A second interaction, started for you. Finish the request side this time.

```ts
await pact
  .addInteraction()
  .given('order 42 is cancellable')
  .uponReceiving(/* YOUR TURN: a short description */)
  .withRequest(/* YOUR TURN: method, path, and a builder for headers/body */)
  .willRespondWith(/* YOUR TURN: status + builder */)
  .executeTest(async (mockServer) => {
    // YOUR TURN: call the client's cancel method against mockServer.url
  });
```

After a passing run, you should find `pacts/CheckoutWeb-OrderService.json`. If the file is absent, write down which of these failed before you change the test: the request did not match, the client assertion failed, or `executeTest` was not awaited.

## Check yourself

1. Why must the client use `mockServer.url` instead of a fixed localhost port?
2. If `executeTest` throws, what happens to the pact file, and why is that the rule?
3. What two strings must be unique together on a Pact instance, and who else has to reuse one of them later?
4. Why is `testEnvironment: 'jsdom'` a bad idea for these tests, and what do you use instead?
5. Where does the pact file land for the `CheckoutWeb` / `OrderService` pair?

## Flashcards

Q:: What is `Pact` in `@pact-foundation/pact` 17.x?
A:: The same class as `PactV4`. The default specification is V4.

Q:: When is a pact file written?
A:: Only when the `executeTest` callback passes and the expected requests arrived. Path: `./pacts/{consumer}-{provider}.json`.

Q:: Why is the Pact class not run in parallel with a shared instance?
A:: It is not thread-safe. Use a separate instance per test, or Jest `--runInBand`.
