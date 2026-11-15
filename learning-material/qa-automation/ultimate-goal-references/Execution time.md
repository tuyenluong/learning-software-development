---
Creation_date: 2026-11-16 01:05
Modification_date: Monday 16th November 2026 01:05:00
Indexes:
  - "[[permanent_notes]]"
  - "[[QA_Automation]]"
  - "[[Playwright]]"
Source: ISTQB CT-TAS Syllabus v1.0, sections 1.1.1, 4.1.1, 4.2.2, 4.2.3, 5.1.1, 5.2.1, 6.1.2, 6.2.1; ISTQB CTAL-TAE Syllabus v2.0, sections 1.1.1, 5.1.1, 6.1.1, 8.1.2
---

----
# Execution time

Goal wording this note unpacks: "how long the suite takes to give feedback, and whether it fits inside the CI window."

## Definition

CT-TAS v1.0, section 5.2.1, names the metric **test automation execution time**: "the time it takes to execute the automated tests." It says this may not matter at the start of a solution, and that it matters once the number of automated cases grows. "This metric includes the build time of the TAS" (the test automation solution).

Reduced test execution time is also an objective of a strategy (section 1.1.1), and "time to run an automated test case" is both a savings input and an investment input in the ROI model (section 5.1.1). See [Cost against benefit](Cost%20against%20benefit.md).

The syllabi talk about feedback as a benefit, not as a second metric with its own definition:

- CTAL-TAE v2.0, section 1.1.1: automation "provides quicker feedback regarding SUT quality."
- CT-TAS 4.1.1: automation "provides quick feedback to developers."
- CT-TAS 3.1.3: component tests with test doubles give "early feedback that is easy to integrate into CI/CD pipelines."
- CT-TAS 6.1.2: continuous testing, running suites as soon as code changes are available, "helps provide immediate feedback."

"CI window" does not appear. The closest planning limit is in CT-TAS 4.2.3: on a first deployment, "total test execution time of the test suite may be longer than the planned test execution time for the test cycle." The response given there is to plan enough time for the whole suite before the next cycle starts.

## How to measure

Section 5.2.1 does not write a formula. Measure the time to execute the automated tests, and include TAS build time in that same metric.

Related times the same syllabus tells you to look at, which are not the same number:

- Planned test execution time for the test cycle, compared with the suite's total time (section 4.2.3).
- Time wasted by outdated cases left in the suite (section 4.2.2).
- Time saved by parallel execution and by shift-left (section 4.1.1). Section 5.1.1 says ROI improves when cases sit at the right test level, because execution time is a large part of the investment.

CTAL-TAE 6.1.1 says the testware can record the start and end time of execution so the timing applies to every test. That is the collection hook, not a formula.

## How to collect and report

Record start and end from the framework (CTAL-TAE 6.1.1) and include TAS build time (CT-TAS 5.2.1). Log timing of significant steps as well (CTAL-TAE 6.1.1), so a slow step can be separated from a slow suite.

Put the duration in the test progress report with the pass-fail trend (CTAL-TAE 6.1.3). Management stakeholders are the audience for trends. CT-TAS 5.4.1 says to highlight the metrics those stakeholders use.

When the suite is too slow for the pipeline, the syllabi name these responses:

- CTAL-TAE 5.1.1: run a long regression suite on a schedule (the example given is nightly) so the team sees quality in the morning, and run non-functional suites separately from the delivery pipeline.
- CTAL-TAE 8.1.2: if a regression suite does not finish because execution takes too long, run parts at the same time on different environments where that is possible, or split the suite into parts that each finish in a defined period (the example given is a single night). In CI/CD, run batch jobs in parallel. Also remove duplicated coverage, which shortens execution.
- CT-TAS 6.2.1: if automation makes the pipeline queue, cut the integrated tests down to the most critical ones (a smoke suite). Run the larger regression suite separately, or on demand.
- CT-TAS 3.2.3: run lower-level suites in the same pipeline as the build, and run larger UI and API suites separately when the team can support them.

Report both numbers when you talk about a "window": the section 5.2.1 metric (execution plus TAS build), and the comparison with the planned cycle time or with the pipeline stage you are willing to block. The second comparison is a use of the metric. It is not a separate ISTQB definition called feedback time.

## Pitfalls

- Omitting TAS build time. Section 5.2.1 includes it.
- Calling a green nightly job "fast feedback." CT-TAS 6.1.2 reserves immediate feedback for suites that run as soon as the change is available. A nightly suite is the pattern CTAL-TAE 5.1.1 gives for long regression.
- Leaving obsolete cases in the suite. Section 4.2.2 calls that wasted execution time.
- Speeding up the suite by deleting lower-level tests and keeping only UI tests. Section 5.1.1 says the opposite: the test pyramid, with cases at the right level, shortens execution and improves ROI. CT-TAS 3.1.1 says an umbrella distribution is completely dependent on costly UI tests. When lower-level cases are not technically possible, the work that remains is to shorten UI execution and improve stability.
- Hard-coded waits. CTAL-TAE 8.1.2 says a fixed wait of a certain number of milliseconds is a root cause of automation defects, and that it wastes time. Prefer polling with a timeout, or the system's own events, again with a timeout.

## Example (Playwright and CI)

This example is practice. The minute budgets are not from the syllabus.

In GitHub Actions, time two spans and publish both in the job summary:

1. TAS build: `npm ci` plus the Playwright browser install. This is the part section 5.2.1 says to include.
2. Suite execution: `npx playwright test`, using the duration in Playwright's JSON reporter (the `duration` field on the run).

For a pull-request pipeline, run the smoke project only, and fail the job if that span exceeds the planned time you agreed for that cycle (the comparison in CT-TAS 4.2.3). Run the full project nightly, which is the long-suite pattern in CTAL-TAE 5.1.1. If the pull-request job starts queueing, that is the signal in CT-TAS 6.2.1 to keep the blocking suite at smoke and leave the rest on the nightly job.

Playwright's own "did this fit the CI window" is not an ISTQB metric. The ISTQB metric is the execution time, including TAS build time.

## Sources

- ISTQB CT-TAS Syllabus v1.0 (2024/05/03), sections 1.1.1, 3.1.1, 3.1.3, 3.2.3, 4.1.1, 4.2.2, 4.2.3, 5.1.1, 5.2.1, 6.1.2, 6.2.1. [PDF](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CT-TAS_Syllabus_v1.0.pdf)
- ISTQB CTAL-TAE Syllabus v2.0 (2024/05/03), sections 1.1.1, 5.1.1, 6.1.1, 8.1.2. [PDF](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTAL-TAE_Syllabus_v2.0.pdf)
