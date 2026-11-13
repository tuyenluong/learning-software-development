# Pact / contract testing (TypeScript)

This pack is a short, self-paced introduction to consumer-driven contract testing with Pact in TypeScript. Each lesson explains what the topic is, what it does, how it works, and how to use it, then leaves incomplete examples for you to finish. It does not replace the official Pact docs; it is a guided path through them.

## Suggested order

**Day 1 — consumer side**

1. [What is contract testing?](01-what-is-contract-testing/lesson.md)
2. [Writing a consumer test](02-consumer-test/lesson.md)
3. [Matchers](03-matchers/lesson.md)

**Day 2 — provider side and the release gate**

4. [Provider verification](04-provider-verification/lesson.md)
5. [Pact Broker](05-pact-broker/lesson.md)
6. [CI and functional tests](06-ci-and-functional-tests/lesson.md)

## Prerequisites

- Node 22 or newer. `@pact-foundation/pact` 17.1.4 dropped Node 20; stay on the 16.x line of the library if you must remain on Node 20.
- npm
- Basic TypeScript
- Familiarity with HTTP APIs (methods, paths, headers, JSON bodies, status codes)

Do not install `pact-core` directly; it comes in as a dependency of `@pact-foundation/pact`. The package `pact-node` is discontinued. There is no npm package named `pact-broker-client`. The CLI to learn is `@pact-foundation/pact-cli` 18.10.9, using `pact broker ...` (the hyphenated `pact-broker` command still runs but is deprecated).

## Official docs

- Consumer: https://docs.pact.io/consumer
- JavaScript provider: https://docs.pact.io/implementation_guides/javascript/docs/provider
- Pact Broker: https://docs.pact.io/pact_broker
