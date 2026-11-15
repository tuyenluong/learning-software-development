---
Creation_date: 2026-11-16 01:05
Modification_date: Monday 16th November 2026 01:05:00
Indexes:
  - "[[permanent_notes]]"
  - "[[QA_Automation]]"
  - "[[Playwright]]"
Source: ISTQB CT-TAS Syllabus v1.0, sections 1.1.3, 4.2.2, 4.3.1, 5.1.1, 5.2.1, 6.2.1; ISTQB CTAL-TAE Syllabus v2.0, sections 4.3.1, 6.1.2, 6.1.3, 8.1.2, 8.1.3
---

----
# Maintenance effort

Goal wording this note unpacks: "time spent fixing tests per change, and time to diagnose a failure."

## Definition

The syllabi treat maintenance as time and cost spent keeping the test automation solution in step with the system, not as a single named metric called "maintenance effort."

The quantities they name:

- CT-TAS v1.0, section 5.1.1, lists **average maintenance time of an automated test script** as an input to investment in the ROI calculation. See [Cost against benefit](Cost%20against%20benefit.md).
- Section 6.2.1 says to keep track of "how many hours are spent developing the TAS, how many hours are spent fixing the TAS, and how much time savings do the testers realize compared to manual testing." "An indicator that something is wrong is if the TAS maintenance time is greater than the manual testing time."
- Section 1.1.3 lists **maintenance cost** as an investment criterion: a solution built from scratch takes time to set up and then has to be maintained.
- Section 4.2.2 lists project risks that are maintenance in another shape: "unplanned TAS maintenance due to SUT updates that cause the TAS to operate incorrectly", delays updating the solution after system changes, and "staffing issues: getting the right people to maintain the test automation may be difficult."
- Section 4.3.1: overcomplicating the environment "may result in hours of unwanted time fixing defects in the TAF instead of benefiting from the solution."
- Section 5.2.1: one decision the metrics support is "maintainability of test automation because of defects found in the TAS." That is a use of the metrics, not a formula for maintainability.

CTAL-TAE v2.0, section 4.3.1, explains what makes a solution maintainable (naming, structure, no hardcoding, design patterns, logging, static analysis, a branching strategy). It does not define a time metric. The factors are written up in [Handover and maintainability](Handover%20and%20maintainability.md).

**Time to diagnose a failure** is not a named metric. CTAL-TAE 6.1.2 describes the analysis steps. Section 6.1.3 says automated analysis of logs "helps the TAE reduce time spent finding broken locators, analyzing the reason for test failures (i.e., is it a defect in the SUT or in the TAS?)" That is a benefit, not a metric definition. "Per change" is not the unit the syllabi use. They use time per automated script (5.1.1) and hours fixing the solution (6.2.1).

## How to measure

No formula beyond the two quantities above.

- Average maintenance time of an automated test script: section 5.1.1 names it and does not say how to average it (per script per sprint, per run, or per change).
- Hours developing the TAS, hours fixing the TAS, and tester time saved against manual testing: section 6.2.1 names the three tracks. The comparison it treats as a warning is maintenance time greater than manual testing time.

Diagnosing a failure follows the five steps in CTAL-TAE 6.1.2 (same failure as last time or not, which test, which step, does the logged system state match, and only then a product defect). You can time that work. The syllabus does not tell you to, and it does not call the duration a metric.

## How to collect and report

CT-TAS 5.2.1: automate collection where you can, so measuring stays cheap. Feed average maintenance time into the ROI model (section 5.1.1) rather than publishing it only as a raw total.

CT-TAS 6.2.1 is the report that shows whether maintenance has got out of hand: hours fixing versus hours building, and versus the manual time the suite is supposed to save. CT-TAS 5.4.1 says one decision from report data is to "shift test automation efforts to maintenance" when that is what the trend shows, and another is to move effort into improving the framework.

CTAL-TAE 8.1.2: when you do spend the maintenance time, spend it where it pays. Upgrade scripting for the tests that "involve the greatest amount of maintenance effort." Move repeated steps into a library function. Move repeated setup into setup and teardown so a change is made once, "which results in decreased maintenance efforts."

CTAL-TAE 8.1.3: after a system change, update the solution in small steps, measure the impact with a limited run, then a full regression. Retire scripts that rarely or never run, so you maintain less.

CTAL-TAE 6.1.1 and 6.1.2: diagnosis depends on the log, the step, screenshots, and the correlation id. Without those, "time to diagnose" grows for reasons the reporting chapter already covers. Publish the frequent-regression history (section 6.1.3) so the same failure is not diagnosed from scratch every run.

## Pitfalls

- Reporting "hours fixing tests" without saying whether you mean the section 5.1.1 average per script or the section 6.2.1 hours fixing the whole solution. They answer different questions.
- Ignoring the section 6.2.1 warning: if maintenance time exceeds the manual testing time you saved, the solution is not paying for itself. That comparison belongs with [Cost against benefit](Cost%20against%20benefit.md).
- Hardcoding test data. CTAL-TAE 4.3.1 says hardcoding is faster to write and expensive to keep, because the data changes. Data-driven tests put that data in one place.
- Keyword and behaviour-driven layers that look easy to write and are costly to keep. CTAL-TAE 3.1.4 says implementing and maintaining keywords is a complex task, and that natural-language steps that are too complex make debugging "a difficult and costly activity."
- Calling diagnosis time an ISTQB metric. It is a duration you may choose to record around the section 6.1.2 procedure.

## Example (Playwright and CI)

This example is practice. The syllabi do not define the spreadsheet columns.

For each sprint, record three numbers in the same units (hours):

- hours changing the Playwright suite and its fixtures because the product changed (the team's reading of "fixing the TAS")
- hours adding new tests (developing)
- hours a tester would have spent running the automated cases by hand, using the manual times already collected for ROI

If the first number exceeds the third, that is the warning in CT-TAS 6.2.1. Say so in the sprint note. Do not divide fixing hours by the number of product changes and call the result an ISTQB "per change" metric.

For diagnosis time, the useful artefact is the one section 6.1.2 asks for, not a stopwatch target: the HTML report and trace uploaded from CI, the failing step, and a one-line reason (product, test data, infrastructure, or TAS failure). The time from the red run to that one-line reason is a team measurement of the analysis. Label it as a team measurement.

## Sources

- ISTQB CT-TAS Syllabus v1.0 (2024/05/03), sections 1.1.3, 4.2.2, 4.3.1, 5.1.1, 5.2.1, 5.4.1, 6.2.1. [PDF](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CT-TAS_Syllabus_v1.0.pdf)
- ISTQB CTAL-TAE Syllabus v2.0 (2024/05/03), sections 3.1.4, 4.3.1, 6.1.1, 6.1.2, 6.1.3, 8.1.2, 8.1.3. [PDF](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTAL-TAE_Syllabus_v2.0.pdf)
