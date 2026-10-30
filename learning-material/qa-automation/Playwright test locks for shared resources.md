---
Creation_date: 2026-10-30 22:30
Modification_date: Friday 30th October 2026 22:30:00
Indexes:
  - "[[permanent_notes]]"
  - "[[QA_Automation]]"
  - "[[Playwright]]"
Source: docs (Playwright 1.63.0 and 1.64.0 release notes, docs/src/test-parallel-js.md at tags v1.63.0 and v1.64.0)
---

----
# Playwright test locks for shared resources

> **Source type: official docs and release notes**, checked 2026-10-30: Playwright **1.63.0** (added test locks) and **1.64.0** (added `test.describe.configure({ lock })`). Current release is 1.64.1.

## The problem
Playwright runs tests in parallel worker processes. Each test gets its own browser context, so cookies, storage and in-memory state are already isolated. What is *not* isolated is state outside the test: one shared test account, a global feature flag, a third-party sandbox that allows one session at a time.

Two parallel tests that both change the same account's settings race exactly like two transactions doing a lost update: test A writes "dark mode on", test B writes "language: French", test A asserts dark mode and reads B's version of the row. The test fails only when the two happen to overlap, so it shows up as a flaky test.

## Fix order
1. **Remove the sharing first.** Give each test its own data, for example an id derived from `testInfo.testId`, or a per-worker account. This keeps full parallelism.
2. **Lock only what can't be isolated.** When the resource is truly single (one sandbox account, one global setting), declare a named lock.
3. **Serial mode is the last resort.** `test.describe.configure({ mode: 'serial' })` also orders tests and skips the rest after a failure; a lock only prevents overlap.

## Test locks (1.63+)
Tests that share a lock name never run at the same time, across files, workers and projects. Everything else keeps running in parallel.

```ts
// settings.spec.ts
import { test, expect } from '@playwright/test';

test('update user settings', { lock: 'user-settings' }, async ({ page }) => {
  // ...
});
```

```ts
// profile.spec.ts
// Never runs concurrently with 'update user settings', even in another project.
test('rename user', { lock: 'user-settings' }, async ({ page }) => {
  // ...
});
```

- **Several locks:** `{ lock: ['database', 'external-api'] }`. The test starts only when all of them are free.
- **A whole group:** `test.describe('settings', { lock: 'user-settings' }, () => { ... })`.
- **File or group level (1.64+):** `test.describe.configure({ lock: 'user-settings' })`. Repeated calls add locks.
- Playwright takes all of a test's locks before it starts and releases them when it finishes.
- **Watch out:** in the default and serial modes, all tests in a file run together in order, so a lock declared on any test in that file is held for the whole file. With `fullyParallel` the lock covers just that test.
- The docs on the main branch also describe a built-in `exclusive` lock (runs a test with nothing else running). As of 1.64.1 it is not in a released version's docs, so check the release notes before relying on it.

## Link to transactions
A lock name is a mutual-exclusion key, the same idea as `SELECT ... FOR UPDATE` on one row or a distributed lock on one key. The same trade-off applies: a lock fixes the race but serializes the work behind it, so keep lock names narrow (`'account-42-settings'`, not `'database'`).

## Exercise
1. Write two tests that change different settings on the same test account and assert their own change. Run with `--workers=4 --repeat-each=20` and count failures.
2. Add `{ lock: 'account-settings' }` to both and rerun. Failures should drop to zero, and the total run time should grow by roughly the length of one test per overlap.
3. Replace the lock with one account per test (derived from `testInfo.testId`) and compare run time again.

## Sources
- [Playwright: Parallelism, test locks](https://playwright.dev/docs/test-parallel)
- [Playwright release notes](https://github.com/microsoft/playwright/releases) (v1.63.0, 4 Sep 2026; v1.64.0, 7 Oct 2026)
