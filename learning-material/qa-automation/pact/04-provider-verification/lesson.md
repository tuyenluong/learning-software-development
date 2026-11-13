---
Creation_date: 2026-11-13
Modification_date: Friday 13th November 2026
Indexes:
  - "[[permanent_notes]]"
  - "[[QA_Automation]]"
  - "[[Pact contract testing]]"
Source: docs — https://docs.pact.io/implementation_guides/javascript/docs/provider; @pact-foundation/pact 17.1.4 Verifier API; checked 2026-11-13
---

# Provider verification

## What is the topic?

Provider verification is the second half of a Pact test. The provider process is running for real; a verifier reads interactions from a pact file (or a broker) and replays each request against that process. If the real responses satisfy the matchers, the provider honours the contract.

In JavaScript you construct `new Verifier({ ... })` and `await` `verifyProvider()`. There are no `@State` annotations; you pass a `stateHandlers` map instead.

## What does it do?

- Replays each recorded request against `providerBaseUrl`.
- Runs a state handler before an interaction that has a `given`, so the provider is in the promised state.
- Optionally publishes the verification result back to a Pact Broker — and that flag belongs **only in CI**.
- Selects which contracts to verify when you use a broker (`mainBranch`, `deployedOrReleased`, `matchingBranch`, plus pending and WIP pacts).

You point the verifier at **either** local files (`pactUrls`) **or** a broker (`pactBrokerUrl`), not both.

## How does it work?

Minimum shape (this is a map of the options, not a passing test):

```ts
import { Verifier } from '@pact-foundation/pact';

// await new Verifier({ ... }).verifyProvider()
//
// provider, providerBaseUrl     — required; the real service
// pactUrls  XOR  pactBrokerUrl  — never both
// providerVersion, providerVersionBranch
// publishVerificationResult     — true only in CI
// consumerVersionSelectors      — mainBranch, deployedOrReleased, matchingBranch
// enablePending, includeWipPactsSince
// stateHandlers                 — keys must match given() exactly
```

State handler names must match the consumer's `given()` text **exactly**, even when the consumer is written in another language. `'order 42 exists'` and `'Order 42 exists'` are different states.

A handler may be an async function that receives params and **returns values** for `fromProviderState`, or an object `{ setup, teardown }`.

Deprecated — do not use:

- `providerBranch` → use `providerVersionBranch`
- `providerStatesSetupUrl` → use `stateHandlers`

When you verify from a broker, typical consumer version selectors are `mainBranch`, `deployedOrReleased`, and `matchingBranch`. Also set `enablePending` and, on the provider's main branch, `includeWipPactsSince`, so new consumer work does not block a provider release until it is ready.

The verifier waits up to 30 seconds by default. Jest's default test timeout is 5 seconds — raise it. Always `await` `verifyProvider()`. Use `testEnvironment: 'node'`.

## Step-by-step: how do I achieve the goal?

1. Start the real OrderService on a known local URL (test instance, not production).
2. Decide the contract source: a local file under `./pacts` while you are learning, or `pactBrokerUrl` once a broker exists (lesson 5). Do not set both.
3. Create a provider test that constructs a `Verifier` with `provider`, `providerBaseUrl`, and that source.
4. Set `providerVersion` and `providerVersionBranch`. Keep `publishVerificationResult` false on your laptop; turn it on only in CI.
5. Add a `stateHandlers` entry for every `given` string in the pact file. Open the pact file and copy the state names — do not retype them from memory.
6. In each handler, set up (and optionally tear down) the data that state describes. If the consumer used `fromProviderState`, return the values the expression expects.
7. Raise the Jest timeout, `await verifyProvider()`, and read the verifier output for the first failing interaction. Fix the provider or the state handler, not the pact file, unless the contract itself was wrong — in which case the change starts on the consumer side.

## What is its usage?

- Locally, `pactUrls` against a file the consumer just wrote, to debug one interaction.
- In CI, `pactBrokerUrl` with selectors, pending/WIP flags, and `publishVerificationResult: true`, so `can-i-deploy` can see the result (lesson 5).
- `requestFilter` is for adding auth headers the consumer did not put in the contract, not for rewriting the interaction.

## Examples / code

This verifier is incomplete on purpose. It should not be copy-run as a passing test.

```ts
import { Verifier } from '@pact-foundation/pact';
import path from 'path';

// YOUR TURN: start (or import a helper that starts) OrderService first.
// What URL will providerBaseUrl point at?

describe('OrderService pact verification', () => {
  // YOUR TURN: raise this timeout. Why is the default 5s not enough?

  it('honours the CheckoutWeb contract', async () => {
    const verifier = new Verifier({
      provider: 'OrderService',
      providerBaseUrl: /* YOUR TURN */,
      // YOUR TURN: pick ONE of pactUrls or pactBrokerUrl. Why not both?
      pactUrls: [
        path.resolve(process.cwd(), 'pacts/CheckoutWeb-OrderService.json'),
      ],
      // pactBrokerUrl: process.env.PACT_BROKER_BASE_URL,
      providerVersion: /* YOUR TURN */,
      providerVersionBranch: /* YOUR TURN */,
      publishVerificationResult: /* YOUR TURN: what is the only safe value on a laptop? */,
      consumerVersionSelectors: [
        // YOUR TURN: mainBranch, deployedOrReleased, matchingBranch
      ],
      enablePending: /* YOUR TURN: true or false, and when? */,
      // includeWipPactsSince: /* YOUR TURN: when does this belong? */,
      stateHandlers: {
        'order 42 exists': async (params) => {
          // YOUR TURN: insert or stub order 42.
          // Return values if the consumer used fromProviderState.
          // params are whatever the consumer passed as given()'s second argument.
        },
        // YOUR TURN: add a handler for every other given() in the pact file.
        // What happens if this key is even slightly different from given()?
      },
    });

    // YOUR TURN: await the call. What do you do with the result?
    // verifier.verifyProvider()
  });
});
```

Optional shape for a state that needs cleanup:

```ts
stateHandlers: {
  'order 42 is cancellable': {
    setup: async () => {
      // YOUR TURN
    },
    teardown: async () => {
      // YOUR TURN
    },
  },
},
```

## Check yourself

1. Why is it an error to set `pactUrls` and `pactBrokerUrl` on the same verifier?
2. When is `publishVerificationResult` allowed to be true, and what two version fields should accompany it?
3. A consumer in another language wrote `given('order 42 exists')`. What must your handler key be?
4. Which two Verifier options are deprecated, and what replaced them?
5. Why might a provider test pass locally and fail in CI (or the other way around) if you forget `enablePending` / `includeWipPactsSince`?

## Flashcards

Q:: How do you verify a provider in Pact JS?
A:: `await new Verifier({ ... }).verifyProvider()`. Use `pactUrls` or `pactBrokerUrl`, not both.

Q:: What is a state handler?
A:: A function or `{setup, teardown}` keyed by the exact `given()` string, used to put the provider into the promised state. It may return values for `fromProviderState`.

Q:: When do you publish verification results?
A:: Only in CI, with `providerVersion` and `providerVersionBranch` set.
