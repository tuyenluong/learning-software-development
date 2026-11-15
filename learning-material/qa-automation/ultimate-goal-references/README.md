---
Creation_date: 2026-11-16 01:05
Modification_date: Monday 16th November 2026 01:05:00
Indexes:
  - "[[permanent_notes]]"
  - "[[QA_Automation]]"
Source: ISTQB CTAL-TAE Syllabus v2.0 (2024/05/03); ISTQB CT-TAS Syllabus v1.0 (2024/05/03); ISTQB Glossary v4.8.1 (2026/10/26) where a term is named
---

----
# Ultimate-goal references (ISTQB)

Notes that unpack [Ultimate Goal for QA Automation](../ULTIMATE-GOAL.md) against the current ISTQB test-automation syllabi. The goal file is the north star. These notes do not change it.

Checked on 16 November 2026 (Vietnam, UTC+7). On that date the certification pages on istqb.org still offered CTAL-TAE v2.0 and CT-TAS v1.0, with no newer syllabus version listed.

The goal says its metric list is the kind of thing CTAL-TAE asks you to collect, and that the list is a summary to check against the current syllabus. That check is what this folder is. In v2.0, CTAL-TAE tells you how to collect, analyse and publish automation data (chapter 6). The named metrics and the return-on-investment formula live in CT-TAS v1.0, chapter 5. Where the goal's wording is tighter or different from either syllabus, the note says so.

## Sources

| Document | Version in the file | Date printed on the file | URL |
|---|---|---|---|
| Certified Tester Advanced Level Test Automation Engineering (CTAL-TAE) Syllabus | 2.0 | 2024/05/03 (GA) | [PDF](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTAL-TAE_Syllabus_v2.0.pdf), [certification page](https://istqb.org/certifications/certified-tester-advanced-level-test-automation-engineering-ctal-tae-v2-0/) |
| Certified Tester Test Automation Strategy (CT-TAS) Syllabus | 1.0 | 2024/05/03 (GA) | [PDF](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CT-TAS_Syllabus_v1.0.pdf), [certification page](https://istqb.org/certifications/certified-tester-test-automation-strategy-ct-tas/) |
| ISTQB Glossary of Terms | 4.8.1, Quality and testing terms | 26 October 2026 | [glossary.istqb.org](https://glossary.istqb.org/), export read for this folder: [nstqb.org/istqbGlossary.pdf](https://nstqb.org/istqbGlossary.pdf) |

Both syllabi point at the glossary for terms. A glossary definition is cited only when the syllabus uses the idea and does not define it. It is never treated as a syllabus section.

Public release announcement (12 June 2024), confirming this pair of syllabi: [ISTQB has released two new syllabi for test automation](https://istqb.org/istqb-has-released-two-new-syllabi-for-test-automation/).

## How a note is organised

Each note has the same parts: the definition as the syllabus gives it; how to measure it, with a formula only when the syllabus writes one; how to collect and report it; pitfalls; a short Playwright and CI example, marked as an example; and the sources, with syllabus name, version, section and URL.

## Map to the goal

### The goal (opening)

| Goal wording | Note | In the syllabi? |
|---|---|---|
| Ship faster | [Suite as a CI release gate](Suite%20as%20a%20CI%20release%20gate.md) | CT-TAS 4.1.1: automation shortens time to market by cutting test-cycle time and by quality gates that find defects earlier. |
| Fewer escaped bugs | [Defects found by automation](Defects%20found%20by%20automation.md) | The comparison "caught before release versus escaped to production" is not a metric in either syllabus. See that note. |
| Automation they trust | [Pass-fail and stability](Pass-fail%20and%20stability.md) | Trust maps to repeatable results, a TAS-failure status, and the pass-fail ratio. "False-failure rate" is not a syllabus metric. |
| Afford to maintain | [Maintenance effort](Maintenance%20effort.md), [Cost against benefit](Cost%20against%20benefit.md) | Maintenance time is an input to ROI. ROI has a formula. |

### The result

| Goal wording | Note |
|---|---|
| Strategy and architecture: what to automate, at which level, what not to automate, gTAA | [Automation strategy and architecture](Automation%20strategy%20and%20architecture.md) |
| A stable suite in CI as a release gate, including the four patterns named in the goal | [Suite as a CI release gate](Suite%20as%20a%20CI%20release%20gate.md) |
| A baseline report and an after report on the metrics | [Baseline and after reporting](Baseline%20and%20after%20reporting.md) |
| Handover: docs and coaching so the team owns the suite | [Handover and maintainability](Handover%20and%20maintainability.md) |

### The metrics

| Goal metric | Note | Syllabus home |
|---|---|---|
| Automation coverage | [Automation coverage](Automation%20coverage.md) | CT-TAS 5.2.1 (functional coverage, code coverage, number of automated test cases) |
| Execution time | [Execution time](Execution%20time.md) | CT-TAS 5.2.1 (test automation execution time) |
| Pass/fail and stability | [Pass-fail and stability](Pass-fail%20and%20stability.md) | CT-TAS 5.2.1 (pass-fail ratio, ratio of failures to defects); CTAL-TAE 6.1.1 (TAS failure) |
| Defects found by automation | [Defects found by automation](Defects%20found%20by%20automation.md) | Not a classified metric. Nearest syllabus text is CT-TAS 4.1.2 and 3.1.3. |
| Maintenance effort | [Maintenance effort](Maintenance%20effort.md) | CT-TAS 5.1.1 and 6.2.1 |
| Cost against benefit (ROI) | [Cost against benefit](Cost%20against%20benefit.md) | CT-TAS 5.1.1, `ROI = Savings / Investment` |

The goal's pitch line says to lead with three numbers, measured before and after: false-failure rate, escaped defects, and feedback time. Those three names are not the metric list in CT-TAS 5.2.1. The nearest syllabus measures are the pass-fail ratio (and the reasons failures are not product defects), defect information the syllabi do collect, and test automation execution time. "Before and after" matches reporting against a baseline and comparing later runs, which is [Baseline and after reporting](Baseline%20and%20after%20reporting.md).

## Wording in the goal that is not in either syllabus

Stated here so a reader can see the whole gap in one place. Each note repeats the gap that belongs to it.

- **False-failure rate.** Neither syllabus defines this rate or gives a formula. CT-TAS 5.2.1 defines pass-fail ratio as passed tests divided by failed tests, and asks you to count how many automated tests fail for one defect, with a reason (subsystem, whole system, test data, or infrastructure). CTAL-TAE 6.1.1 adds a status called TAS failure, for a defect that is not in the system under test. The glossary still defines false-fail result as a synonym of false-positive result. That definition is not a rate, and it is not a learning objective in these two syllabi.
- **Escaped defects versus defects found by automation.** Neither syllabus defines that comparison or a formula for it. The glossary defines escaped defect and defect detection percentage (DDP). DDP is not taught in CTAL-TAE v2.0 or CT-TAS v1.0.
- **Feedback time, and "fits inside the CI window".** The named metric is test automation execution time, and it includes the build time of the test automation solution. The syllabi also compare suite time with the planned test-execution time of the test cycle, and they tell you to shrink a suite to smoke tests when it queues the pipeline. They do not define a metric called feedback time or CI window. Quicker feedback is described as a benefit.
- **Automation coverage as "the share of in-scope tests, tracked per risk area".** Functional coverage in CT-TAS 5.2.1 is the percentage of functional requirements covered by automated test cases. The same section says the count of automated test cases does not show coverage. There is no instruction to track coverage per risk area. Risk is used to choose which conditions to automate first (CT-TAS 2.2.1).
- **Maintenance as "time spent fixing tests per change" and "time to diagnose a failure".** The syllabi ask for average maintenance time of an automated test script, hours spent fixing the test automation solution, and a comparison of that maintenance time with manual testing time. They describe how to diagnose a failure. They do not name "per change" or "time to diagnose" as metrics.
- **A baseline report and an after report**, as two engagement deliverables. CT-TAS 3.1.1 says to draw the current state of testing as a baseline and a target state. The glossary defines a test progress report as progress against a baseline. CTAL-TAE 6.1.3 says to keep a history of reports and watch trends, including changes in the pass-fail ratio. The pair of document names is this goal's, not the syllabus's.
- **Catching bad test data before anything runs**, as a named pattern. The nearest text is to automate preconditions before the real test cases run (CT-TAS 6.1.1 and 6.2.1), and to refuse to automate a manual test that already fails because its data is invalid (CT-TAS 6.1.1). A pre-suite data check that aborts the run is general practice.
- **A driver layer so the team can change tools later, Helix as an internal accelerator, and an eject path to plain Playwright.** The syllabi describe a test-adaptation capability, a single driver that talks to the system under test (singleton), core libraries that do not depend on one system, and in-house ownership of the solution. They do not mention Helix, Playwright, or an eject path.
- **Unit** as a test level name. Where the goal says unit, CT-TAS 3.1.1 says ISTQB calls Mike Cohn's unit level component testing.

ROI itself is in the syllabus. The formula is `ROI = Savings / Investment`. The syllabus lists the inputs and does not expand them into one longer equation. That limit is written out in [Cost against benefit](Cost%20against%20benefit.md).
