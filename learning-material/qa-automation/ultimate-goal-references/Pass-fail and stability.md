---
Creation_date: 2026-11-16 01:05
Modification_date: Monday 16th November 2026 01:05:00
Indexes:
  - "[[permanent_notes]]"
  - "[[QA_Automation]]"
  - "[[Playwright]]"
Source: ISTQB CT-TAS Syllabus v1.0, sections 3.1.1, 5.1.1, 5.2.1, 5.4.1; ISTQB CTAL-TAE Syllabus v2.0, sections 6.1.1, 6.1.2, 6.1.3, 7.1.2, 7.1.3, 8.1.1; ISTQB Glossary v4.8.1, false-positive result
---

----
# Pass/fail and stability

Goal wording this note unpacks: "the share of failures that are real bugs versus flaky tests or environment noise (the false-failure rate)."

## Definition

Two classified metrics in CT-TAS v1.0, section 5.2.1, and one status in CTAL-TAE v2.0, section 6.1.1, are what the syllabi actually give you.

**Pass-fail ratio.** "The pass-fail ratio = the number of tests that passed / the number of tests that failed."

**Ratio of failures to defects.** Many automated tests can fail for one defect in the system under test. "Measuring the number of automated tests that fail for a given defect can help indicate where this may be a problem." Also "collect the number of failures per defect and track the reason for failure: defect in the sub-system, in the whole system, issue with the test data, or infrastructure."

**TAS failure.** CTAL-TAE 6.1.1: test execution status "can be either passed, failed, or a TAS failure." A status "can sometimes be inconclusive", and the organisation should define the statuses in a clear and consistent way. "A TAS failure is applied to situations where the defect is not in the SUT."

The phrase **false-failure rate** does not appear in CTAL-TAE v2.0 or CT-TAS v1.0, and neither syllabus gives a formula for it. The word **flaky** does not appear either. The syllabus language for the same worry is: TAS failure, a failure whose reason is test data or infrastructure, an inconclusive result, and a test that does not give a reliable result.

The glossary (v4.8.1) still has the older term. A **false-positive result**, synonym **false-fail result**, is "a test result in which a defect is reported although no such defect actually exists in the test object." A **false-negative result**, synonym **false-pass result**, is "a test result which fails to identify a defect that is actually present in a test object." Those are glossary definitions of a single result. They are not a rate, and they are not learning objectives in these two syllabi. Use them so the words in the goal have an official meaning. Do not report a "false-failure rate" as if section 5.2.1 had defined one.

**Stability** is used in CT-TAS 3.1.1 for one situation: when lower-level cases are not technically possible and the distribution stays an umbrella of UI tests, the focus includes "improving stability." That sentence does not define a stability percentage.

CT-TAS 5.1.1 also lists "percentage of failed automated test scripts" as an input to investment in the ROI calculation. It does not define that percentage further. It is not the false-failure rate.

## How to measure

The only formula written out is:

`pass-fail ratio = number of tests that passed / number of tests that failed`

(CT-TAS 5.2.1). It is passed divided by failed, not passed divided by the total number of tests. The syllabus does not discuss what to do when the number of failures is zero.

For the ratio of failures to defects, the syllabus does not write an algebraic formula. It tells you to count, per defect, how many automated tests failed, and to record one of four reasons: subsystem, whole system, test data, or infrastructure.

A practical reading of the goal's "share of failures that are real bugs" is the split of those reasons: failures whose reason is the subsystem or the whole system, against failures whose reason is test data, infrastructure, or a TAS failure. That split is supported by the reason list and by the TAS-failure status. The syllabi do not multiply it out into a rate called false-failure rate. If you publish such a share, label it as your definition.

CTAL-TAE 6.1.1 also mentions "changes in the test success rate" as an example of a trend a report should be able to highlight. It does not define test success rate.

## How to collect and report

CTAL-TAE 6.1.1: the framework should report status (passed, failed, or TAS failure), not only the log line. On a failure, store what you need to analyse it: screenshots, crash dumps, stack traces, and logs that would otherwise be overwritten. Record the test case, its start and end, and the significant steps.

CTAL-TAE 6.1.2 gives the analysis order:

1. Did this same failure happen on earlier runs? It may be a known defect in the system or in the solution. Keeping history on the test case helps.
2. If it is new, identify the test case and what it is testing.
3. Find the test step where it failed.
4. Compare the logged state of the system (screenshots, API and network logs) with the expected result.
5. If the system state is wrong, log a defect, with the logs that show it.

The same section says a failure can happen while the actual result still matches the expected result. In that case the defect is most likely in the test automation solution, or there is a mismatch you cannot see. It also says that when the environment is down, or partly down, every test can fail, sometimes with the same defect and sometimes looking like real product failures. System logs show whether the environment was down at that time.

CTAL-TAE 6.1.3: management looks at changes in the pass-fail ratio and at the reliability of the solution and of the system. Keep a history so you can see cases and suites with frequent regressions. CT-TAS 5.4.1: use the report to spot trends and do root-cause analysis, and to decide whether effort should move to maintenance.

CTAL-TAE 7.1.2: a repeated test should always give the same result. A case that does not (the example given is a race condition) should leave the active suite and be analysed on its own. Otherwise every run spends time on the same failure.

CTAL-TAE 7.1.3: if a script fails or passes unexpectedly, do root-cause analysis of the logs, performance data, and setup and teardown. Intermittent failures are harder. The defect may be in the test case, the system, the framework, the hardware, or the network. Missing assertions can make a result inconclusive.

CTAL-TAE 8.1.1: a test histogram of results, exception logs, error messages and screenshots helps you pick fragile cases to refactor.

## Pitfalls

- Reading pass-fail ratio as "percent passed." The written formula is passed divided by failed.
- One product defect failing many tests, so the pass-fail ratio looks like a wide outage. That is why section 5.2.1 asks for failures per defect.
- Counting an environment outage as many product defects. Section 6.1.2 says the system logs are how you tell.
- Leaving intermittent cases in the blocking suite (section 7.1.2).
- Calling Playwright's "flaky" result a false-failure rate. See the example.
- Quoting the glossary's false-fail definition as if CTAL-TAE v2.0 had set a target rate. It has not.

## Example (Playwright and CI)

This example is practice. Playwright's result names are Playwright's, documented in [CI with flaky-test control](../module-1/CI%20with%20flaky-test%20control.md). They are not ISTQB terms.

On a run, take the JSON reporter and count passed, failed, and flaky (failed, then passed on a retry). Publish:

- pass-fail ratio = passed / failed, and omit the ratio when failed is 0 (the syllabus formula does not cover that case)
- a reason on every failure, using the four reasons in CT-TAS 5.2.1, plus TAS failure when the product state matched the expectation or the health check showed the environment was down (CTAL-TAE 6.1.1 and 6.1.2)

Playwright marks a test flaky when a retry passes. That is evidence the result was not repeatable, which is the situation CTAL-TAE 7.1.2 tells you to take out of the active suite and analyse. It is not, by itself, a false-fail result: a retry can also pass because a real defect is intermittent. Someone still has to do the analysis in section 6.1.2.

Do not compute "flaky / failed" and call it the ISTQB false-failure rate. If the team wants that share, name it as a team metric and say which statuses went into it.

## Sources

- ISTQB CT-TAS Syllabus v1.0 (2024/05/03), sections 3.1.1, 5.1.1, 5.2.1, 5.4.1. [PDF](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CT-TAS_Syllabus_v1.0.pdf)
- ISTQB CTAL-TAE Syllabus v2.0 (2024/05/03), sections 6.1.1, 6.1.2, 6.1.3, 7.1.2, 7.1.3, 8.1.1. [PDF](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTAL-TAE_Syllabus_v2.0.pdf)
- ISTQB Glossary v4.8.1 (26 October 2026), terms "false-positive result" (synonym "false-fail result") and "false-negative result" (synonym "false-pass result"). [glossary.istqb.org](https://glossary.istqb.org/), export [nstqb.org/istqbGlossary.pdf](https://nstqb.org/istqbGlossary.pdf)
