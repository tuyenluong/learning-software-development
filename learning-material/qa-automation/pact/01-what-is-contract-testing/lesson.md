---
Creation_date: 2026-11-13
Modification_date: Friday 13th November 2026
Indexes:
  - "[[permanent_notes]]"
  - "[[QA_Automation]]"
  - "[[Pact contract testing]]"
Source: docs — https://docs.pact.io/consumer; @pact-foundation/pact 17.1.4 (Node >=22), @pact-foundation/pact-cli 18.10.9; checked 2026-11-13
---

# What is contract testing?

## What is the topic?

Contract testing is a way to check that two services agree on the shape of the messages they exchange — typically HTTP requests and responses — without standing up both services and every dependency in one end-to-end environment.

Pact is a consumer-driven contract-testing tool. The *consumer* (the client) writes a test against a mock provider, and that test produces a *pact file*: a JSON contract that records the expected request and the expected response. The *provider* (the API) later replays those requests against the real service and checks that the real responses still match the contract.

This pack uses TypeScript and `@pact-foundation/pact` 17.1.4 (Node 22 or newer). If you must stay on Node 20, use the 16.x line of the same package; version 17 dropped Node 20. The library depends on `pact-core`; do not install `pact-core` yourself.

If you have seen Pact on the JVM: `@PactTestFor` defaults to specification V3, tests use annotations, and pact files land under `target/pacts` (or `build/pacts`). In JavaScript, `Pact` is the same class as `PactV4`, the default specification is V4, the API is a fluent chain, and pact files land under `./pacts`. Matcher names also differ (`integer` here, `integerType` on the JVM). The idea is the same.

## What does it do?

A contract test answers a narrower question than an end-to-end test:

- End-to-end: "Does checkout still work when the web app, the order service, the database, and the payment provider are all running together?"
- Contract: "If the web app sends *this* request, does the order service still reply with a response this client knows how to read?"

Pact checks **message shape**, not business logic. It will catch a renamed field, a missing header, or a status code change. It will not catch "the order total is wrong" or "the stock count is stale." Those stay in functional API tests (lesson 6).

Because the consumer writes the contract, the pact only includes the data and operations that consumer actually uses. The official [consumer docs](https://docs.pact.io/consumer) put it this way: "Only include data and operations used by the consumer."

## How does it work?

Three artefacts, in order:

1. **Consumer test.** The consumer test starts a Pact mock server, describes an interaction (`given` / `uponReceiving` / `withRequest` / `willRespondWith`), and calls the real client against `mockServer.url`. If the client sends the expected request and can handle the mocked response, Pact writes `./pacts/{consumer}-{provider}.json`. The pact file is written only when that callback passes.
2. **Provider verification.** The provider test reads that pact file (from disk or from a broker) and sends the recorded requests to the real provider. Provider *state handlers* set up the data the interaction assumed — for example, "order 42 exists."
3. **Broker (optional but usual in a team).** A Pact Broker stores contracts and verification results, and answers `can-i-deploy` before a release. The open-source broker is the Docker image `pactfoundation/pact-broker` (pin `3.0.0-pactbroker2.121.2`, port 9292). PactFlow is the hosted commercial broker. Bi-directional contract testing exists only on PactFlow; this pack stays on consumer-driven Pact.

```
Consumer test  -->  pact file  -->  provider verification
                       |
                       v
                  Pact Broker  -->  can-i-deploy
```

## Step-by-step: how do I achieve the goal?

Before you write any test, decide whether a contract belongs here at all.

1. Pick one consumer and one provider. Name them the way they will appear in the pact file, for example `CheckoutWeb` and `OrderService`.
2. List one real call the consumer already makes (method, path, headers it sends, fields it reads from the body). Ignore fields the consumer never touches.
3. Write down the provider state in a short sentence, for example `order 42 exists`. The provider will later have to implement a handler with that exact name.
4. Ask: would a failure here mean "the two sides no longer agree on the message," or "the business rule is wrong"? Only the first belongs in Pact.
5. Only then open a consumer test (lesson 2). Do not start with the provider, and do not start with a broker.

Fill this in for a service you already know. Leave any line blank if you cannot answer it yet — that is the point.

```
Consumer name:            __________________
Provider name:            __________________
HTTP method + path:       __________________
Headers the client sends: __________________
Fields the client reads:  __________________
Provider state sentence:  __________________
Is this shape, or business logic?  __________________
```

## What is its usage?

Use Pact when:

- Two teams (or two repos) share an HTTP API and you want a cheaper check than a full end-to-end environment.
- You want to know, before release, whether a provider change would break a known consumer.
- You want the contract to reflect what the consumer actually uses, not the provider's entire schema.

Do not use Pact when:

- You are testing calculations, authorisation rules, or workflows. That is functional testing.
- There is no real consumer yet and you are inventing a contract "for later." Consumer-driven means the consumer exists.
- You need bi-directional or schema-first contract testing. That is a PactFlow feature, not part of open-source Pact.

## Examples / code

This is a sketch, not a passing test. Do not try to run it yet. Circle what would belong in a contract and what would not.

```ts
// A checkout client reads an order. Which of these belong in a Pact
// interaction, and which belong in a functional API test?

// GET /orders/42
// Response:
// {
//   "id": 42,
//   "status": "PAID",
//   "items": [{ "sku": "SKU-1", "qty": 1 }],
//   "internalAuditRef": "AUD-99",   // the web app never reads this
//   "total": "19.99"
// }

// YOUR TURN: tick each line — contract, functional, or neither?
// [ ] status code 200
// [ ] Content-Type: application/json
// [ ] field `id`
// [ ] field `status`
// [ ] field `items[].sku` and `items[].qty`
// [ ] field `internalAuditRef`
// [ ] "total equals 19.99 for this fixture"
// [ ] "a PAID order cannot be cancelled"
```

When you have ticked those, write one sentence that could go in `given(...)`. Do not look ahead to lesson 2 for a finished example.

```
given('________________________________')
```

## Check yourself

1. What question does a contract test answer that an end-to-end test does not need to answer, and what does it *refuse* to answer?
2. When is the pact file written — as soon as you describe the interaction, or at some later point?
3. Why must the provider-state sentence be chosen carefully, even before any code is written?
4. `@pact-foundation/pact` 17.1.4 needs which Node version? What do you do if you are on Node 20?
5. Name one difference between the JavaScript Pact API and the JVM API that would surprise you if you copied a Java example.

## Flashcards

Q:: What is a pact file?
A:: A JSON contract, usually at `./pacts/{consumer}-{provider}.json`, recording the interactions a consumer expects from a provider.

Q:: What does Pact check, and what does it not check?
A:: Message shape (requests and responses the consumer uses). Not business logic.

Q:: What is consumer-driven contract testing?
A:: The consumer writes the contract from the calls it actually makes; the provider later verifies that contract against the real service.

Q:: Pact vs PactFlow?
A:: Pact is the open-source contract-testing tool and OSS broker. PactFlow is the hosted commercial broker; bi-directional contract testing exists only there.
