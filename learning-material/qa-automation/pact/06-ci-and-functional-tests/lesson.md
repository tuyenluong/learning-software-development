---
Creation_date: 2026-11-13
Modification_date: Friday 13th November 2026
Indexes:
  - "[[permanent_notes]]"
  - "[[QA_Automation]]"
  - "[[Pact contract testing]]"
Source: docs — https://docs.pact.io/pact_broker, https://docs.pact.io/consumer; @pact-foundation/pact 17.1.4, @pact-foundation/pact-cli 18.10.9, GitHub Action pact-foundation/pact-cli; checked 2026-11-13
---

# CI and functional tests

## What is the topic?

Contract tests only pay off when they run in CI, on every relevant change, and when their results feed `can-i-deploy`. This lesson covers how to wire Pact into a GitHub Actions pipeline, how the broker tells the provider to re-verify, and why contract tests do **not** replace functional API tests.

The CLI in CI is the same `@pact-foundation/pact-cli` you met in lesson 5. On GitHub Actions, use the `pact-foundation/pact-cli` action, **pinned to a version**.

## What does it do?

A typical pair of pipelines:

- **Consumer CI:** install dependencies, run consumer tests, publish `./pacts` with version and branch, then `can-i-deploy` before deploying, then `record-deployment`.
- **Provider CI:** install dependencies, start the provider, run `verifyProvider` against the broker with `publishVerificationResult: true`, then the same deploy gate.

When a new or changed contract lands on the broker and needs a provider to verify it, the broker can fire a webhook. The event to use is `contract_requiring_verification_published`. It replaces `contract_content_changed`. That webhook can trigger the provider pipeline, for example through GitHub `repository_dispatch`.

## How does it work?

Two integration details that surprise people:

**The native engine is an optional dependency.** `@pact-foundation/pact` (and the CLI) pull a platform binary through optional dependencies. Installing with `--omit=optional` (or a lockfile / container setup that drops optional deps) breaks Pact. Alpine Linux is officially unsupported — use a glibc-based image (Debian/Ubuntu, or the action above).

**Jest needs a node environment.** Set `testEnvironment: 'node'`, not jsdom. The `Pact` class is not thread-safe: run `--runInBand`, or give each test its own `Pact` instance. Always `await` `executeTest` and `verifyProvider`. Raise Jest's 5 second timeout for provider verification; the verifier waits up to 30 seconds.

Pact checks **shape**, not business logic. A green contract suite means the two sides still agree on the messages the consumer uses. It does not mean the order total is correct, that cancellation rules hold, or that an authenticated user cannot see someone else's order. Those remain functional API tests (Playwright `APIRequestContext`, REST Assured, Supertest, or whatever you already use).

## Step-by-step: how do I achieve the goal?

1. Pin Node 22+ on the CI image (or stay on `@pact-foundation/pact` 16.x if the image is Node 20). Do not use Alpine. Do not pass `--omit=optional`.
2. Consumer job: run the consumer tests, then `pact broker publish` with `--consumer-app-version` and `--branch` (lesson 5).
3. Provider job: start the service, run the Verifier with `pactBrokerUrl`, selectors, `enablePending`, `providerVersion`, `providerVersionBranch`, and `publishVerificationResult: true`.
4. Pin `pact-foundation/pact-cli` in the workflow. Use it for `publish`, `can-i-deploy`, and `record-deployment`.
5. Configure a broker webhook for `contract_requiring_verification_published` that triggers the provider workflow (for example `repository_dispatch`). Do not configure the retired `contract_content_changed` event on new work.
6. Keep a separate job (or suite) of functional API tests. A contract change that is still "in shape" can break behaviour; a behaviour test can pass while the contract is already wrong. You want both.

## What is its usage?

- The deploy job of each pacticipant: `can-i-deploy --to-environment production --retry-while-unknown`, then deploy, then `record-deployment`.
- A webhook-triggered provider verification when a consumer publishes a contract that an environment needs checked.
- A reminder in code review: a new interaction is not "covered" until the provider has verified it and the result is on the broker.

## Examples / code

A workflow skeleton, not a ready-to-run pipeline. Fill every blank and do not invent a green build from this file alone.

```yaml
# .github/workflows/consumer.yml  (skeleton)
name: CheckoutWeb
on: [push]
jobs:
  test-and-publish:
    runs-on: ubuntu-latest   # YOUR TURN: why not an Alpine-based container?
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '22'
          # YOUR TURN: would npm ci --omit=optional be safe here? Why not?
      - run: npm ci
      - run: npm test -- --runInBand
        # YOUR TURN: which Jest testEnvironment must be set, and why
        # --runInBand?
      - uses: pact-foundation/pact-cli@/* YOUR TURN: pin a version. Why pin? */
        with:
          # YOUR TURN: the publish command from lesson 5.
          # Which env vars does it need?
      # YOUR TURN: where do can-i-deploy and record-deployment belong
      # relative to the actual deploy step?
```

```yaml
# Provider webhook trigger (sketch)
# Broker webhook event:
#   contract_requiring_verification_published
# YOUR TURN: why this event, not contract_content_changed?
# YOUR TURN: how would the webhook call GitHub repository_dispatch,
# and what would the provider workflow need to verify (version, branch,
# pact URL or selector)?
```

Functional tests still have a job:

```ts
// Not a Pact test. YOUR TURN: write one assertion that Pact would
// not catch even if the contract is green.
//
// Example situations — pick one and fill in a test outline:
// - order totals / rounding
// - "a PAID order cannot be cancelled"
// - authz: user A cannot GET user B's order
//
// describe('Order API — behaviour', () => {
//   it('/* YOUR TURN */', async () => {
//     // call the real API (or a test instance), not the Pact mock
//   });
// });
```

## Check yourself

1. Which GitHub Action do you use for broker commands, and what must you do to its version?
2. Which broker webhook event should trigger provider verification, and which older event does it replace?
3. Name two install or image choices that will break the native Pact binary.
4. What Jest settings matter for Pact, and why is the default 5s timeout a problem on the provider side?
5. Why do functional API tests stay in the pipeline after Pact is green?

## Flashcards

Q:: Which webhook event should a Pact Broker use to request provider verification?
A:: `contract_requiring_verification_published`. It replaces `contract_content_changed`.

Q:: Why can `--omit=optional` break Pact?
A:: The native engine is delivered through optional dependencies.

Q:: Why keep functional API tests after adding Pact?
A:: Pact checks message shape, not business logic.
