---
Creation_date: 2026-11-13
Modification_date: Friday 13th November 2026
Indexes:
  - "[[permanent_notes]]"
  - "[[QA_Automation]]"
  - "[[Pact contract testing]]"
Source: docs — https://docs.pact.io/pact_broker; @pact-foundation/pact-cli 18.10.9, pactfoundation/pact-broker:3.0.0-pactbroker2.121.2; checked 2026-11-13
---

# Pact Broker

## What is the topic?

The Pact Broker is a store for pact files and verification results. Instead of copying JSON contracts between repos, each side publishes to the broker, and the broker answers the release question: can this version of a service go out without breaking a known partner?

The CLI is `@pact-foundation/pact-cli` 18.10.9. The command to learn is `pact broker ...`. The older hyphenated `pact-broker` binary still runs, but it prints a deprecation warning. The package `pact-node` is discontinued. There is no npm package named `pact-broker-client`.

For a self-hosted broker, pin the Docker image `pactfoundation/pact-broker:3.0.0-pactbroker2.121.2` and use port 9292. PactFlow is the paid hosted broker. Bi-directional contract testing exists only on PactFlow; this lesson stays on the consumer-driven flow.

## What does it do?

Three commands cover the release path:

1. **publish** — the consumer uploads contracts, tagged with an application version and a branch.
2. **can-i-deploy** — asks whether this version is compatible with what is already in a named *environment* (for example `production`).
3. **record-deployment** — after a successful deploy, tells the broker that this version is now in that environment.

Without `record-deployment`, `can-i-deploy --to-environment production` has no record of what production actually is.

## How does it work?

Versions and **branches** identify builds. **Environments** identify where a build is running. The older model of *tags* and `can-i-deploy --to <tag>` has been replaced by branches and environments. Do not start a new pipeline on tags.

`can-i-deploy` succeeds only when the broker can see a successful verification between this version and the versions recorded in the target environment. `--retry-while-unknown` exists because the provider pipeline may still be running when the consumer asks.

For libraries (things that are released but not deployed as a running service), use `record-release` instead of `record-deployment`. Create each environment once with `create-environment`.

The OSS broker typically uses basic auth. PactFlow uses a bearer token (`PACT_BROKER_TOKEN`).

## Step-by-step: how do I achieve the goal?

1. Run a broker (Docker pin above, port 9292) or use an existing one. Set `PACT_BROKER_BASE_URL`.
2. Create the environments you need, once: `production`, and usually a staging environment too.
3. After a passing consumer test, publish the `./pacts` directory with `--consumer-app-version` and `--branch`. Use the git commit and the git branch, not a handmade label.
4. Let the provider verify those contracts from the broker and publish the verification result (lesson 4 and 6).
5. Before deploying, run `can-i-deploy` with `--to-environment` and `--retry-while-unknown`.
6. Only if the deploy succeeds, run `record-deployment` for that same version and environment.

If step 5 fails, do not skip it and deploy anyway — the broker is telling you a partner has not successfully verified this contract.

## What is its usage?

- Multi-repo teams, where the consumer and provider do not share a filesystem.
- A release gate in CI: publish on the consumer pipeline, verify on the provider pipeline, `can-i-deploy` on both before production.
- Recording what is in each environment so the next build compares against reality, not against "latest."

## Examples / code

These are the real command shapes. They are not a complete pipeline. Fill the blanks and answer the questions before you glue them into CI (lesson 6).

```bash
# 1. Publish consumer contracts
pact broker publish ./pacts \
  --consumer-app-version "$GIT_COMMIT" \
  --branch "$GIT_BRANCH" \
  --broker-base-url "$PACT_BROKER_BASE_URL"

# YOUR TURN: what goes wrong if you publish without --branch?
# YOUR TURN: why is the version the git commit, not "latest"?
```

```bash
# 2. Release gate
pact broker can-i-deploy \
  --pacticipant CheckoutWeb \
  --version "$GIT_COMMIT" \
  --to-environment production \
  --retry-while-unknown 30 \
  --retry-interval 10

# YOUR TURN: what is a "pacticipant"? Why CheckoutWeb here and not OrderService?
# (When would you run the same command for OrderService?)
# YOUR TURN: why retry-while-unknown, and what happens if you omit it
# and the provider job is still running?
```

```bash
# 3. After a successful production deploy
pact broker record-deployment \
  --pacticipant CheckoutWeb \
  --version "$GIT_COMMIT" \
  --environment production

# YOUR TURN: record-deployment or record-release — which one for a
# shared library that is published to npm, and why?
# YOUR TURN: if you forget this step, what does the next can-i-deploy
# compare against?
```

One-time setup (do not put this in the per-build job without thinking):

```bash
# YOUR TURN: fill the environment name and a short display name.
# When do you run this — every build, or once?
pact broker create-environment \
  --name /* YOUR TURN */ \
  --display-name /* YOUR TURN */ \
  --broker-base-url "$PACT_BROKER_BASE_URL"
```

A command you should not start new work with:

```bash
# Deprecated shape — tags / --to <tag> have been replaced by
# branches and environments.
# pact broker can-i-deploy --pacticipant CheckoutWeb --version "$GIT_COMMIT" --to prod
# YOUR TURN: rewrite this with --to-environment. What else has to
# have happened for the environment name to mean something?
```

## Check yourself

1. Which CLI package and which command form should you use in 2026, and which old command still works but is deprecated?
2. What are the three release-path commands, and in what order do they run relative to a production deploy?
3. Why were tags and `--to <tag>` replaced, and what do you use instead?
4. When do you use `record-release` rather than `record-deployment`?
5. What Docker image and tag would you pin for a self-hosted broker, and which port does it listen on?

## Flashcards

Q:: What is a Pact Broker?
A:: A store for contracts and verification results that can answer `can-i-deploy` for a version and environment.

Q:: What CLI do you use to talk to the broker?
A:: `@pact-foundation/pact-cli` (18.10.9): `pact broker ...`. Not `pact-node`, and not an npm package called `pact-broker-client`.

Q:: `record-deployment` vs `record-release`?
A:: `record-deployment` is for a running service in an environment. `record-release` is for libraries.
