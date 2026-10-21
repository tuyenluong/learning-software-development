---
Creation_date: 2026-10-21 18:20
Modification_date: Wednesday 21st October 2026 18:20:00
Indexes:
  - "[[permanent_notes]]"
  - "[[QA_Automation]]"
  - "[[Playwright]]"
  - "[[Module 1 - QA Automation for Edge Cases]]"
Source: docs (Playwright 1.64 Retries, CLI, Test options, Annotations; Maven Surefire 3.6.0 "Rerun Failing Tests"; Jenkins Flaky Test Handler + JUnit plugins; GitHub Actions runner images; TestNG docs)
---

----
# QA Lesson 6: CI with flaky-test control (GitHub Actions and Jenkins)

> **Source type: official docs**, checked 2026-10-21: Playwright **1.64.1**, Maven Surefire **3.6.0**, TestNG **7.12.0**, Jenkins JUnit plugin **1442.vb_b_a_467df2767** and Flaky Test Handler **1.3.172**, GitHub actions `checkout@v7`, `setup-java@v6`, `setup-node@v7`, `upload-artifact@v7`. Lessons 3–5 *prevent* flakiness; this one is about *detecting, reporting and containing* what's left, in Jenkins (your daily CI) and GitHub Actions.

## The idea
A flaky test is one that passes and fails on the same code. It's worse than a failing test: people learn to click "rebuild", and then real failures get ignored too. The policy that works:
1. **Retry, but report.** Retries keep the pipeline moving; the "passed on retry" result must be **visible** (counted, listed), never silently green.
2. **Quarantine, with an owner and a deadline.** Move a known-flaky test out of the blocking suite into a non-blocking job, file a ticket, fix or delete it.
3. **Fix the cause.** Almost always one of the causes below, not "the CI is slow".

## Common causes (and the lesson that fixes them)
| Cause | Typical symptom | Fix |
|---|---|---|
| **Timing / fixed sleeps** | Fails only on busy CI agents | Poll with a timeout ([[Async waits without sleeps]]) |
| **Async not ready** (consumer hasn't got partitions yet) | First test in a class fails, rest pass | Wait for assignment / readiness (lesson 5) |
| **Shared state** (same user, same order, same topic) | Fails only in parallel or after another test | Per-test data and unique names ([[Framework structure - fixtures and test data]]) |
| **Order dependence** | Passes in the IDE, fails with sharding/shuffle | Each test creates its own data |
| **Fixed ports / shared infra** | "Address already in use", tests collide across jobs | Random mapped ports with Testcontainers ([[Testcontainers for Kafka and RabbitMQ (Java and Go)]]) |
| **Unseeded random / wall-clock time / time zones** | Fails at midnight, end of month, or on the UTC agent only | Seed + log, inject the clock |
| **Unordered results** (no `ORDER BY`, many partitions) | Assertion on list order fails sometimes | Assert sets or sort first |
| **Real external services** | Fails when a sandbox is down | Fake them (WireMock container) or isolate those tests |

## Detection: Java (Maven Surefire / TestNG)
- **Surefire reruns:** `mvn -Dsurefire.rerunFailingTestsCount=2 verify`. Supported for **JUnit 4.12+, JUnit 5 and TestNG**. A test that passes on a rerun is counted as a **flake**: the build stays green and the summary shows `Flakes: 1`; the XML report gets `<flakyFailure>` / `<flakyError>` elements for each failed run ([Surefire: Rerun Failing Tests](https://maven.apache.org/surefire/maven-surefire-plugin/examples/rerun-failing-tests.html)). (Surefire 3.6.0; Failsafe has the same option for `*IT` tests.)
- **TestNG:** implement `IRetryAnalyzer` (`boolean retry(ITestResult result)`) and attach it with `@Test(retryAnalyzer = ...)` or an annotation transformer. Log every retry so it's visible ([TestNG docs](https://testng.org/)).
- **Jenkins:** publish the XML with the `junit` step (JUnit plugin). The **Flaky Test Handler** plugin reads Surefire's `rerunFailingTestsCount` data, aggregates passes/fails/flakes over Git revisions, and can re-run only the failed tests at the same revision ([plugin page](https://plugins.jenkins.io/flaky-test-handler/)).
- **Quarantine in Java:** tag it, `@Tag("quarantine")` (JUnit) or `@Test(groups = "quarantine")` (TestNG), and exclude it from the blocking job with Surefire `excludedGroups=quarantine`; run it in a separate non-blocking job with `groups=quarantine`.

## Detection: Playwright
From [Retries](https://playwright.dev/docs/test-retries) and the [CLI](https://playwright.dev/docs/test-cli):
- `retries: process.env.CI ? 2 : 0` in the config. Results are **passed** (first run), **flaky** (failed, then passed on retry), **failed** (failed all retries). On a failure Playwright **throws away the whole worker process** and starts a new one, so a retry gets clean worker state.
- `testInfo.retry` tells a test or fixture it's a retry (e.g. to clean server state first).
- **`--fail-on-flaky-tests`** fails the run if any test was flaky (default false). Use it on the main branch once the suite is clean.
- **`--repeat-each=N`** runs each test N times: the fastest way to prove a fix (`--repeat-each=50 -g "idempotency"`). `--last-failed` re-runs only the last failures.
- **Traces:** `trace: 'on-first-retry'` records a trace (actions, network, console, DOM snapshots) only when a test is retried, which is cheap and gives you evidence for exactly the flaky runs ([Test options](https://playwright.dev/docs/test-use-options)). Upload `test-results/` as a CI artifact and open it with `npx playwright show-trace`.
- **Quarantine:** tag it, `test('...', { tag: '@quarantine' }, ...)` ([Annotations](https://playwright.dev/docs/test-annotations)), run the blocking job with `--grep-invert @quarantine` and a non-blocking job with `--grep @quarantine`. `test.fixme()` is for tests you know are broken and don't want to run at all.
- For Jenkins, add the JUnit reporter: `reporter: [['junit', { outputFile: 'results/junit.xml' }], ['html']]`.

## Parallelism isolation
- Parallel runs expose shared state. Rules: unique data per test, no fixed ports, one Playwright instance per thread in Java, per-worker slots via `testInfo.parallelIndex` (lesson 3).
- **Separate jobs ≠ separate infra.** Two Jenkins builds hitting one shared test DB/Kafka collide. Testcontainers per job, or Jenkins `lock` (Lockable Resources plugin) around shared environments.
- **Sharding** (`npx playwright test --shard=1/4`) spreads files over machines; it only works if tests don't depend on each other.

## Example: GitHub Actions (Java + Testcontainers, then Playwright)
```yaml
name: tests
on: [push, pull_request]
jobs:
  integration:
    runs-on: ubuntu-latest            # Ubuntu 24.04, Docker preinstalled → Testcontainers works
    steps:
      - uses: actions/checkout@v7
      - uses: actions/setup-java@v6
        with: { distribution: temurin, java-version: '21', cache: maven }
      - run: mvn -B verify -Dsurefire.rerunFailingTestsCount=2 -DexcludedGroups=quarantine
      - if: always()
        uses: actions/upload-artifact@v7
        with: { name: surefire-reports, path: '**/target/surefire-reports/' }

  api-e2e:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v7
      - uses: actions/setup-node@v7
        with: { node-version: 22 }
      - run: npm ci && npx playwright test --grep-invert @quarantine
        env: { CI: 'true' }           # retries: 2 in the config
      - if: always()
        uses: actions/upload-artifact@v7
        with: { name: playwright-traces, path: test-results/ }
```

## Example: Jenkins (declarative pipeline)
```groovy
pipeline {
  agent { label 'docker' }                       // agent must reach a Docker daemon (lesson 4)
  stages {
    stage('Integration (blocking)') {
      steps { sh 'mvn -B verify -Dsurefire.rerunFailingTestsCount=2 -DexcludedGroups=quarantine' }
    }
    stage('Quarantine (non-blocking)') {
      steps {
        catchError(buildResult: 'SUCCESS', stageResult: 'UNSTABLE') {
          sh 'mvn -B verify -Dgroups=quarantine'
        }
      }
    }
  }
  post {
    always {
      junit testResults: '**/target/surefire-reports/*.xml', allowEmptyResults: true
      archiveArtifacts artifacts: 'test-results/**', allowEmptyArchive: true   // Playwright traces, if any
    }
  }
}
```

## What breaks / how to test it
- **Retries hide real bugs.** A race condition in the code (lesson 1's double-charge) *looks* flaky. If a test is flaky, first ask "could production hit this too?" before calling it a test problem.
- **Retrying non-idempotent setup** (a retry re-creates the same order id) → the retry fails for a different reason. Fixtures must be safe to run again (unique data each attempt).
- **Quarantine as a graveyard** → keep a list with owner and date; delete tests that stay quarantined for, say, two sprints.
- **Green builds with a growing flake count** → track the flake count per week (Surefire `Flakes:`, Playwright "flaky", Flaky Test Handler stats) and treat a rise as a bug.
- **Prove the fix:** run the fixed test 50–100 times (`--repeat-each`, `@RepeatedTest`, TestNG `invocationCount`) on CI, not just once locally.

## How it maps to the learning focus
- **Core focus:** timeouts, races and async messaging are the top causes of flaky integration tests; a flaky messaging test is often a real duplicate/ordering bug.
- **Your QA work:** in your Jenkins jobs, turn on `rerunFailingTestsCount`, add a quarantine group, and look at the flake count after a week. That's a concrete improvement you can show at work.

## Related
[[Module 1 - QA Automation for Edge Cases]] · [[Async waits without sleeps]] · [[Framework structure - fixtures and test data]] · [[Testcontainers for Kafka and RabbitMQ (Java and Go)]] · [[Test design for messaging and transaction edge cases]]

---
## Flash cards section
How does Playwright classify a test that failed once and passed on retry?::"flaky" (vs "passed" on the first run, "failed" if all retries fail). --fail-on-flaky-tests makes such runs fail.
What does Surefire do with a test that passes on a rerun?::Counts it as a flake: the build stays green, the summary shows Flakes: N, and the XML gets flakyFailure/flakyError elements.
Why use trace: 'on-first-retry'?::It records a full trace only when a test is retried, so you get evidence for exactly the flaky runs at low cost.
How do you quarantine a test without deleting it?::Tag it (@Tag("quarantine"), TestNG groups, or a Playwright @quarantine tag), exclude it from the blocking job, run it in a non-blocking job, and give it an owner and deadline.
Before blaming the test for flakiness in a messaging test, what should you ask?::Could production hit the same thing? Races, duplicates and ordering issues look flaky but are often real bugs.
