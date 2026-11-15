---
Creation_date: 2026-11-16 01:05
Modification_date: Monday 16th November 2026 01:05:00
Indexes:
  - "[[permanent_notes]]"
  - "[[QA_Automation]]"
  - "[[Playwright]]"
Source: ISTQB CTAL-TAE Syllabus v2.0, sections 6.1.1, 6.1.2, 6.1.3; ISTQB CT-TAS Syllabus v1.0, sections 3.1.1, 5.1.1, 5.2.1, 5.4.1; ISTQB Glossary v4.8.1, test progress report, test progress
---

----
# Baseline and after reporting

Goal wording this note unpacks: "a baseline report and an after report, measured on the metrics below."

The metrics themselves are the other notes in this folder. This note is about the two reports, and about what "before and after" means in the syllabi.

## Definition

The names "baseline report" and "after report" do not appear in CTAL-TAE v2.0 or CT-TAS v1.0. The syllabi do require a baseline, a report, and a comparison over time. Those are three different sentences:

- CT-TAS v1.0, section 3.1.1: "It is helpful to draw the current state of testing as a baseline and the target state." The drawing shows how much testing sits at each level, and whether it is manual or automated. The target depends on the time available. The pyramid is the target when you can reach it.
- The glossary (v4.8.1) defines **test progress** as "the progress of testing against a baseline," and a **test progress report** (synonym test status report) as "a type of periodic test report that includes the progress of test activities against a baseline, risks, and alternatives requiring a decision."
- CTAL-TAE v2.0, section 6.1.3, is the learning objective for how that report is built and published. The report contains the test results, information about the system under test, and documentation of the environment, in a form that fits each stakeholder. Test logs are not a substitute: "the test logs alone cannot provide a good overview of the overall test results."

CTAL-TAE 6.1.1: reporting across a series of runs needs an analysis feature that looks at previous runs "so it can highlight trends, such as changes in the test success rate." Section 6.1.2 tells you to "compare test results of previous test executions." Section 6.1.3 tells you to keep a history of reports so you can gather statistics on cases and suites with frequent regressions.

CT-TAS 5.1.1 is the before-and-after picture for money and time: an ROI graph across sprints, read at the sprint where the investment has been returned. See [Cost against benefit](Cost%20against%20benefit.md).

CT-TAS 5.4.1: the same data, read later, is allowed to change the content and format of future reports. An "after" report that adds a metric the stakeholders started using is in that section. A fixed pair of engagement documents is the goal's structure, not the syllabus's.

The goal's pitch says to measure false-failure rate, escaped defects and feedback time before and after. Those three names are not the section 5.2.1 list. A before-and-after that follows the syllabi uses the metrics the syllabi name (pass-fail ratio, failures per defect and their reasons, execution time including TAS build time, functional coverage, code coverage, the count of automated cases, maintenance hours, ROI), plus the distribution drawing from section 3.1.1. You can add the goal's three as team metrics if you define them in the report. Say they are team metrics.

## How to measure

There is no formula for "the baseline" or "the after."

Take the same definitions on both dates, or the comparison is not a comparison:

- Functional coverage and code coverage, kept as separate numbers ([Automation coverage](Automation%20coverage.md)).
- Test automation execution time, including TAS build time ([Execution time](Execution%20time.md)).
- Pass-fail ratio, and failures per defect with a reason ([Pass-fail and stability](Pass-fail%20and%20stability.md)).
- Hours fixing the solution against manual time saved, and ROI = Savings / Investment ([Maintenance effort](Maintenance%20effort.md), [Cost against benefit](Cost%20against%20benefit.md)).
- The level distribution, manual versus automated (CT-TAS 3.1.1).

CTAL-TAE 6.1.3 says management in particular watches "how many test cases were added since the last test run, changes in the pass-fail ratio and the reliability of the TAS and SUT." Those are the deltas. They assume you stored the previous report.

"Test success rate" is named in section 6.1.1 as an example of a trend. It is not given a formula. Do not silently reuse the pass-fail ratio under that name. The pass-fail ratio is passed divided by failed.

## How to collect and report

CTAL-TAE 6.1.1 is the collection side. Sources include system logs (UI, API, application, web server, database), framework logs, build logs, deployment logs, production monitoring, and screenshots or recordings. The framework should record start and end time, status (passed, failed, or TAS failure), and enough on a failure to analyse it later. Results can be exported to the test-management tool, a spreadsheet, XML, or a database. Summarise with charts. The section suggests traffic-light icons for the overall status, because management decides from the summary and drills down only when it needs to.

CTAL-TAE 6.1.3, content and publication:

- Results, system identity, and the environment the tests ran in.
- Which tests failed, and why. History of the test, and who created or last updated it, so the right person investigates, files the defect, follows the fix, and checks the fix.
- The report is also how you diagnose failures of framework components.
- Publish it to the people who should act: upload it, mail it, or post it to chat. Subscription is how you get it read.
- Keep the history for trend analysis.

Stakeholders in that section, and what they read:

- Management (architect, delivery or programme manager, test manager or director): trends, including new cases since last run, pass-fail movement, reliability of the solution and the system.
- Operational (product owner, business representative, business analyst): metrics about product use.
- Technical (team lead, scrum master, administrators, test automation engineer, tester, developer): lower-level detail.

CT-TAS 5.4.1 says to pick the key metrics for those people, and lists what the data can justify afterwards: trend and root-cause work, a shift of effort onto maintenance or onto the framework, new capabilities, more shift-left or shift-right, wider functional coverage, attention to defect clusters, advice to developers, advice on the lifecycle, and a change to the report itself. CTAL-TAE 6.1.3's dashboards add defect clusters, defect propagation across environments, performance degradation, and reliability of builds.

A baseline report, in this goal's sense, is the first of those periodic reports plus the section 3.1.1 drawing: current distribution, the metric values, the environment, and the risks that need a decision (the glossary's test progress report includes risks and alternatives). An after report is a later issue of the same report, with the deltas section 6.1.3 names, not a different kind of document.

## Pitfalls

- Two reports that do not define the metrics the same way. A pass rate (passed / total) in the after report cannot be subtracted from a pass-fail ratio (passed / failed) in the baseline.
- A log dump in place of the progress report. Section 6.1.3 says the logs do not give the overview.
- One report for every audience. The section says content and detail vary. Management gets trends. Technical readers get the step and the logs.
- Declaring victory from the count of automated cases. Section 5.2.1 says that count is not coverage. The after report should show functional coverage and code coverage as well.
- An after report that drops the environment description. Results from a different environment are not the comparison section 6.1.2 is asking for.
- Treating the goal's three pitch metrics as the syllabus list. Put them in an appendix if the client wants them, with the definitions from [Pass-fail and stability](Pass-fail%20and%20stability.md), [Defects found by automation](Defects%20found%20by%20automation.md) and [Execution time](Execution%20time.md).

## Example (Playwright and CI)

This example is practice. The two filenames are the goal's names, not syllabus names.

On the day the suite first blocks the pull-request pipeline, archive one report and call it the baseline. Build it from the CI artefacts, not from memory:

- Playwright JSON reporter: passed, failed, duration, and the list of projects (smoke versus regression).
- The workflow's own timing for `npm ci` and the browser install, added to the duration, because execution time includes TAS build time.
- The requirements matrix count from [Automation coverage](Automation%20coverage.md).
- A short table of component / API / UI, manual versus automated, which is the section 3.1.1 drawing in text form.
- The git revision and the environment URL, because section 6.1.3 wants the environment in the report.

Store that file next to the HTML report. At the end of the engagement, publish the same sections again and add the three deltas section 6.1.3 highlights: cases added, change in the pass-fail ratio, and whether failures are still TAS failures or product failures. Link each failure to its trace. That second file is the goal's after report. In syllabus terms it is the next test progress report, compared with the previous one.

Post both to the channel the team already reads. Section 6.1.3 treats publication as part of the report, not as a courtesy.

## Sources

- ISTQB CTAL-TAE Syllabus v2.0 (2024/05/03), sections 6.1.1, 6.1.2, 6.1.3. [PDF](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTAL-TAE_Syllabus_v2.0.pdf)
- ISTQB CT-TAS Syllabus v1.0 (2024/05/03), sections 3.1.1, 5.1.1, 5.2.1, 5.4.1. [PDF](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CT-TAS_Syllabus_v1.0.pdf)
- ISTQB Glossary v4.8.1 (26 October 2026), terms "test progress" and "test progress report". [glossary.istqb.org](https://glossary.istqb.org/), export [nstqb.org/istqbGlossary.pdf](https://nstqb.org/istqbGlossary.pdf)
