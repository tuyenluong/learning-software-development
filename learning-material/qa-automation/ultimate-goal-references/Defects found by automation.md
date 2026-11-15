---
Creation_date: 2026-11-16 01:05
Modification_date: Monday 16th November 2026 01:05:00
Indexes:
  - "[[permanent_notes]]"
  - "[[QA_Automation]]"
  - "[[Playwright]]"
Source: ISTQB CT-TAS Syllabus v1.0, sections 3.1.1, 3.1.3, 4.1.1, 4.1.2, 5.2.1; ISTQB CTAL-TAE Syllabus v2.0, sections 1.1.1, 3.1.4, 6.1.2, 6.1.3; ISTQB Glossary v4.8.1, escaped defect, defect detection percentage
---

----
# Defects found by automation

Goal wording this note unpacks: "what automation caught before release, compared with what escaped to production."

## Definition

That comparison is not a classified metric in CT-TAS v1.0 section 5.2.1, and CTAL-TAE v2.0 does not define it either. There is no syllabus formula for "defects found by automation" or for "escaped to production."

What the syllabi do say about defects and automation:

- CT-TAS 4.1.1: quality gates built on automation find defects earlier, which shortens time to market. The section defines a quality gate as "an enforced measure built into your process that the software needs to meet before it can proceed to the next phase."
- CT-TAS 4.1.2: after a fix, confirmation testing checks that a reported defect is gone. Defects come back in later releases, so confirmation tests are good candidates for automation and belong in the regression suite. "Tracking automated confirmation tests allows for reporting the time and the number of test cycles expended in resolving defects."
- CT-TAS 3.1.3: shift-right testing, with observability, aims to "identify defects in production early", and to help decide whether a release candidate can go out or must be rolled back.
- CT-TAS 3.1.1: an ice-cream distribution (too little component testing) finds defects later. An umbrella of UI tests means slow defect turnaround.
- CT-TAS 5.2.1: count how many automated tests fail per defect, and why. See [Pass-fail and stability](Pass-fail%20and%20stability.md). This is failures per defect, not defects found versus defects escaped.
- CTAL-TAE 6.1.3: dashboards can show "defect clusters" and "increase/decrease in defect propagation to certain test environments."
- CTAL-TAE 3.1.4: test-driven development "reduces defect propagation to higher test levels."
- CTAL-TAE 1.1.1: one disadvantage of automation is "introduction of additional defects by test automation." Those are defects in the solution, not product defects the suite found.
- CTAL-TAE 6.1.2: when the system state does not match the expected result, log a defect with the logs that justify it.

The glossary (v4.8.1) has the words the goal is reaching for, and the syllabi do not teach them as automation metrics:

- **Escaped defect:** "a defect that is not detected by a test activity that is supposed to find it."
- **Defect detection percentage (DDP),** synonym Fault Detection Percentage: "the number of defects found by a test level, divided by the number found by that test level and any other means afterwards."

DDP is per test level, not "automation versus production." An escaped defect is one a test activity should have found, which may be a level, a type, or a suite, not automatically "production." Cite these as glossary terms. Do not cite them as CTAL-TAE or CT-TAS section text.

## How to measure

No formula in either syllabus.

The numbers the syllabi do tell you to report in this neighbourhood:

- Time and number of test cycles spent resolving defects, from automated confirmation tests (CT-TAS 4.1.2).
- Failures per defect, with a reason (CT-TAS 5.2.1).
- Defect clusters, and whether defects are propagating into later environments (CTAL-TAE 6.1.3).
- Defects seen in production under a shift-right approach (CT-TAS 3.1.3), as an aim of that approach, not as a formula against pre-release finds.

If you use the glossary's DDP, the formula is the one quoted above, and the denominator is "that test level and any other means afterwards." Substituting "found by the Playwright suite before release" and "found later in production" is an adaptation. Label it as an adaptation of the glossary definition, not as a syllabus metric.

## How to collect and report

CTAL-TAE 6.1.2: the automation logs are the primary data; system logs are secondary. A correlation id (also called a trace id) logged by the solution lets you follow one request through the system. When you file the defect, attach the logs that show the mismatch.

CT-TAS 4.1.2: once you know the steps that reproduce a reported defect, add a narrow automated confirmation test and keep it in the regression suite. Track how many cycles and how much time the fix took.

CTAL-TAE 6.1.3: publish a test progress report, and keep the history so frequent regressions show up as a trend. Dashboards are where defect clusters and cross-environment propagation belong. Management reads trends; technical readers need the step and the logs.

CT-TAS 3.1.3: production (or pre-production) monitoring is a different stream from the pre-release suite. The syllabus presents it as shift-right, including canary releases, not as the same count as the CI suite.

A before-and-after story for a client can still be told from these pieces: confirmation tests added, cycles to fix, clusters, and defects that showed up only after release. The syllabi do not collapse those into one escaped-defect percentage. See [Baseline and after reporting](Baseline%20and%20after%20reporting.md).

## Pitfalls

- Counting failed tests as found defects. Many tests can fail for one defect (CT-TAS 5.2.1).
- Counting TAS failures and environment outages as product defects (CTAL-TAE 6.1.1 and 6.1.2).
- Assuming every production defect is an escape from the suite. The glossary's escaped defect is a defect a specific test activity was supposed to find. A defect outside that activity's scope is not, on that definition, an escape from it.
- Using DDP as if CTAL-TAE v2.0 required it. It does not.
- Ignoring defects the automation itself added (CTAL-TAE 1.1.1).

## Example (Playwright and CI)

This example is practice. The ratio at the end is an adaptation of the glossary's DDP, not a formula from either syllabus.

When a Playwright assertion fails and the API body does not match the contract, file a defect and put the trace and the response log on it. Tag the defect `found-by-automation` and record the build URL. When a confirmation test is added for a bug that was reported another way, tag that test and record the cycles until it stayed green (CT-TAS 4.1.2).

Once a release is in production, tag newly found product defects `found-after-release` for that version. For a single test level, the glossary DDP is defects that level found, divided by (those defects plus defects found afterwards). A team report can show the same shape for the suite:

`suite DDP (team adaptation) = found-by-automation / (found-by-automation + found-after-release)`

for one release, counting defects, not failed tests. Write "team adaptation of glossary DDP" on the report so it is not read as CT-TAS 5.2.1.

## Sources

- ISTQB CT-TAS Syllabus v1.0 (2024/05/03), sections 3.1.1, 3.1.3, 4.1.1, 4.1.2, 5.2.1. [PDF](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CT-TAS_Syllabus_v1.0.pdf)
- ISTQB CTAL-TAE Syllabus v2.0 (2024/05/03), sections 1.1.1, 3.1.4, 6.1.2, 6.1.3. [PDF](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTAL-TAE_Syllabus_v2.0.pdf)
- ISTQB Glossary v4.8.1 (26 October 2026), terms "escaped defect" and "defect detection percentage". [glossary.istqb.org](https://glossary.istqb.org/), export [nstqb.org/istqbGlossary.pdf](https://nstqb.org/istqbGlossary.pdf)
