---
Creation_date: 2026-11-06 22:30
Modification_date: Friday 6th November 2026 22:30:00
Indexes:
  - "[[permanent_notes]]"
  - "[[QA_Automation]]"
  - "[[Playwright]]"
Source: docs (Playwright 1.65.0 release notes; docs/src/test-parallel-js.md patterns from 1.63/1.64 locks)
---

----
# Playwright 1.65 exclusive lock and failure reporters

> **Source type: official release notes**, checked 2026-11-06: Playwright **1.65.0** (5 Nov 2026). Builds on named test locks from 1.63 / 1.64 — see [Playwright test locks for shared resources](Playwright%20test%20locks%20for%20shared%20resources.md).

## What 1.65 adds for suite design

Three runner features matter for CI and flaky-test control:

1. **Built-in `-exclusive-` lock** — a test that holds it runs only when no other tests are running.
2. **`failures` reporter** and **`onlyFailures`** on HTML / JSON / JUnit — keep unexpected, flaky and interrupted outcomes, drop the quiet passes.
3. **Bun as a test-runner runtime** — `bunx --bun playwright test` (Bun transpiles TypeScript; watch mode and some stack details differ).

## Exclusive lock vs named lock

| Kind | Behaviour | Use when |
|---|---|---|
| Named lock (`{ lock: 'user-settings' }`) | Tests that share the name never overlap; everything else stays parallel | Shared account, shared feature flag, one third-party sandbox |
| `-exclusive-` | **No other test runs at all** while this one runs | Restarting a shared server, mutating a global env that every worker sees, one-shot teardown of a shared cluster |

```ts
test('restart the shared test server', { lock: '-exclusive-' }, async () => {
  // No other test runs while this one is running.
});
```

Named locks still compose (`{ lock: ['db', 'billing-sandbox'] }`). Prefer isolating data (`testInfo.testId`) before either kind of lock. Exclusive is the blunt instrument: it serialises the whole suite around one test.

## Failure-only reporters

```ts
// playwright.config.ts
import { defineConfig } from '@playwright/test';

export default defineConfig({
  reporter: [
    ['failures'], // streams failures and successful retries as they occur
    ['html', { onlyFailures: true }],
    ['junit', { onlyFailures: true }],
  ],
});
```

`onlyFailures` keeps unexpected outcomes, flaky tests and interrupted tests. Large CI artifacts shrink when most of the suite is green. Pair with existing retries / `--fail-on-flaky-tests` from the Module 1 CI note.

## Bun runtime (optional)

```bash
bunx --bun playwright test
```

Without `--bun`, `bunx playwright test` still runs on Node.js. CI for the Playwright project itself runs the runner tests under Bun 1.4.3 on Linux. Differences called out in the release notes: no watch mode; Bun loads modules itself (`--tsconfig` / custom ESM loaders unsupported); stack traces omit async frames and class names on API steps; console output of a test does not enter the trace / UI mode.

## Other 1.65 runner notes worth knowing

- `test.skip()` / `fixme()` / `fail()` / `slow()` now take **only a description** (recorded as an annotation).
- Actions such as `click` / `fill` wait for the element to be **not inert**.
- Node.js **20 is no longer tested**; use 22, 24 or 26.
- Class-field initialisers follow `useDefineForClassFields` from `tsconfig.json` (same as `tsc`) — move locator fields that read constructor params into the constructor if they break.

## Exercise

1. Add one test that must not overlap any other work (for example a suite-wide seed reset) with `{ lock: '-exclusive-' }`, and two ordinary tests with a shared named lock. Run with `--workers=4 --repeat-each=10`.
2. Confirm wall-clock time: exclusive stretches the suite more than a named lock; named locks only serialise their own group.
3. Turn on `['html', { onlyFailures: true }]` and force one flaky retry. Check that the HTML report keeps the flaky path and drops quiet passes.

## Sources
- [Playwright 1.65.0 release notes](https://github.com/microsoft/playwright/releases/tag/v1.65.0)
- [Playwright: Parallelism and test locks](https://playwright.dev/docs/test-parallel)
- Related note: [Playwright test locks for shared resources](Playwright%20test%20locks%20for%20shared%20resources.md)
