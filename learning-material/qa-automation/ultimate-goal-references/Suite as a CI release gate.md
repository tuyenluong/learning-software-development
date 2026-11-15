---
Creation_date: 2026-11-16 01:05
Modification_date: Monday 16th November 2026 01:20:00
Indexes:
  - "[[permanent_notes]]"
  - "[[QA_Automation]]"
  - "[[Playwright]]"
Source: ISTQB CTAL-TAE Syllabus v2.0, sections 3.1.4, 3.1.5, 4.2.1, 5.1.1, 5.1.2, 7.1.2; ISTQB CT-TAS Syllabus v1.0, sections 3.2.3, 3.3.2, 4.1.1, 4.2.1, 6.1.1, 6.1.2, 6.2.1; ISTQB Glossary v4.8.1, quality gate
---

----
# Suite as a CI release gate

Goal wording this note unpacks: "a stable, reliable suite running in their CI as a release gate, built on these patterns: catching bad test data before anything runs, data-driven tests, reusable steps, and a driver layer so they can change tools later."

Architecture, levels, and what not to automate are in [Automation strategy and architecture](Automation%20strategy%20and%20architecture.md). Reliability of the results is in [Pass-fail and stability](Pass-fail%20and%20stability.md). Duration is in [Execution time](Execution%20time.md).

## Definition

The goal says "release gate." The syllabi say **quality gate**.

CT-TAS v1.0, section 4.1.1: "A quality gate is an enforced measure built into your process that the software needs to meet before it can proceed to the next phase." Gates based on automation speed up deployment to pre-production or production, because defects are found earlier. The glossary (v4.8.1) defines quality gate as "a milestone at which a decision about proceeding to the next phase is taken based on predefined quality criteria." Use the sentence in section 4.1.1 when you are talking about this syllabus. The glossary wording is a milestone and a decision. The syllabus wording is an enforced measure the software has to meet.

CTAL-TAE v2.0, section 5.1.1, places test levels in the pipeline and says which of them are gates:

- Configuration tests of the framework, during its build, check that the files the scripts need exist at the paths the scripts use.
- Component tests run in the build step and "act as quality gates for the pipeline."
- Component integration tests can sit in the same continuous-integration pipeline when they are low-level.
- System tests "can often be integrated into a continuous deployment pipeline, where they act as the last quality gate of the delivered SUT."
- System integration tests "are often part of a continuous delivery pipeline as quality gates."

The same section gives two ways to attach system, system-integration and acceptance tests, and they do not both gate the release:

1. Run them in the deployment phase. A bad result can fail the deployment and roll it back. Rerunning the tests means deploying again.
2. Run them as a separate pipeline, triggered by a successful deployment. "In this case, tests do not act as a quality gate." Rolling back then takes a separate, usually manual, action. A few small deployment checks can still confirm the system is up. Those checks "do not verify functional suitability in a broad manner."

So a suite "in CI" is a release gate only when failing it stops the next phase. A nightly or post-deploy suite that does not block is still valuable (section 5.1.1's nightly regression). It is not the gate.

CT-TAS 3.3.2: one reason to automate at all is that "test results need to be available in a pipeline." CT-TAS 3.2.3: where you can, run automation in the same pipeline that builds the system, and trigger different suites after local change, pull request, merge, and deploy. CT-TAS 6.1.2: continuous testing runs suites as soon as the change is in the environment.

CTAL-TAE 4.2.1 uses the same idea in the pilot: the conditions around the suite (network, resources) have to be good enough "to provide reliable and beneficial quality gates."

### The four patterns in the goal

**Data-driven tests.** This pattern is in the syllabus. CTAL-TAE 3.1.4: data-driven testing builds on structured scripting. Scripts read test data (the examples are csv, xlsx, and database dumps) so the same script runs many times with different data. Pros: cases grow through the data, the cost of a new automated test can fall, and a test analyst can specify cases by filling in data. Con: you may need proper test-data management. CTAL-TAE 4.3.1 recommends data-driven testing specifically to avoid hardcoding.

**Reusable steps.** This pattern is in the syllabus. CTAL-TAE 3.1.4, structured scripting: test libraries hold reusable elements, test steps, or user journeys, and business logic is separated from the scripts. Section 3.1.5, flow model: user actions live in a facade over the page objects, "as test steps can be reused in multiple test scripts." Section 8.1.2: similar steps should become one library function. CT-TAS 6.1.1: functional overlap (the example is a login copied into every case) should become one component that every case calls. CT-TAS 3.3.1 asks whether tests overlap enough for steps and data to be reused.

**A driver layer so they can change tools later.** The syllabus has the pieces, and it does not state the "change tools later" purpose.

- CTAL-TAE 3.1.5: the singleton pattern "is often used to make sure that there is only one driver that communicates with the SUT."
- CTAL-TAE 3.1.1: test adaptation supplies different adaptors for APIs, protocols and services.
- The glossary's test adaptation layer is the code that adapts abstract scripts to the system's components, configuration, or interfaces.
- CT-TAS 4.3.1: a framework includes "driver scripts."
- CT-TAS 6.1.2, when moving to continuous testing: "stubs, drivers, and interfaces used in testing need to change to fit with the updated TAS."
- CTAL-TAE 3.1.3: core libraries do not depend on one system. Test scripts call the business-logic layer, not the core libraries.

**Catching bad test data before anything runs.** That sentence is not in the syllabi. The nearest instructions:

- CT-TAS 6.1.1, test-execution preconditions: understand what must already exist (users, roles, table values) before you automate a case. "The strategy can be enhanced by automating the creation of preconditions prior to the real test cases running." That may be a precondition script through the UI, or a batch load into a database.
- CT-TAS 6.2.1: implement preconditions, and automate the initialisation steps, "when these steps cannot be missed prior to executing the tests."
- CT-TAS 6.1.1, executable tests: if the manual test fails because it "uses invalid test data", fix that before you automate it. Automating it first creates a non-functioning automated test.
- CT-TAS 4.2.1: good design avoids static data where it can. Where it cannot, either preload the data or generate it with a setup script before the real scripts. Both need maintenance.
- CTAL-TAE 4.2.1: test fixtures control the environment and the data, and they "enable the creation of automated tests that are repeatable and atomic."
- CTAL-TAE 7.1.1: before using the system, check connectivity and other preconditions, so the solution is actually installed and configured.
- CTAL-TAE 8.1.4: a setup script can create the data (the example is registering users through a web service) so the right data is present in a new environment.

A check that refuses to start the suite when the data is already wrong is general practice on top of those sections. The sections tell you to create the preconditions, and to refuse to automate a test whose data is already invalid. They do not describe a pre-flight assertion that aborts the pipeline.

## How to measure

A gate is an enforced measure (CT-TAS 4.1.1). The syllabus does not define a "gate health" percentage. You measure the suite with the metrics in the other notes, and you record whether a failure of this suite stopped the next phase or only produced a report.

CT-TAS 6.2.1: if the suite makes the pipeline queue, reduce the integrated tests to a smoke suite, and run the wider regression separately or on demand. That is a design change driven by [Execution time](Execution%20time.md).

CTAL-TAE 7.1.2: cases that do not give the same result when repeated come out of the active suite. A gate made of those cases is not the "stable, reliable suite" in the goal.

## How to collect and report

CTAL-TAE 5.1.1 and 5.1.2: say, in the pipeline definition, which suite runs at which phase, on which environment, and whether it can fail the deployment. Keep environment configuration, test data, and the suite identity in configuration management. Feature toggles or matching version tags tie the suite to the release it is allowed to judge.

CT-TAS 3.2.3: name the suites per phase (local, pull request, merge, deploy) so "the CI suite" is not one undifferentiated job.

The test progress report (CTAL-TAE 6.1.3) is how the gate's result reaches people who were not watching the job. See [Baseline and after reporting](Baseline%20and%20after%20reporting.md).

## Pitfalls

- A post-deploy job that everyone calls a release gate, while section 5.1.1 says a separate pipeline does not act as a quality gate unless something else stops the release.
- Deployment-only smoke checks presented as functional coverage. Section 5.1.1 says those checks do not verify functional suitability broadly.
- A blocking UI suite long enough to queue the pipeline (CT-TAS 6.2.1), instead of a smoke gate plus a separate regression.
- Copying login, or any other overlap, into every script (CT-TAS 6.1.1).
- One Playwright import in every test. Put construction of the driver in one place (CTAL-TAE 3.1.5). The syllabus does not say that this, by itself, lets you replace the tool.
- Automating a case whose data is already invalid (CT-TAS 6.1.1).

## Example (Playwright and CI)

This example is practice. Job names are not from the syllabus.

Three GitHub Actions jobs, matching the split in CTAL-TAE 5.1.1 and CT-TAS 3.2.3:

1. **Build gate.** The application's component tests. A failure fails the workflow. Playwright is not in this job.
2. **Pull-request gate.** `npx playwright test --project=smoke` against the deployed preview. The workflow needs this job to succeed before merge. That is a quality gate in the sense of CT-TAS 4.1.1. The smoke project is the shrink recommended by CT-TAS 6.2.1.
3. **Nightly regression.** `npx playwright test --project=regression`. It publishes a report and does not block a release that already passed job 2. By section 5.1.1, this job is not a quality gate.

Inside the Playwright project, still as practice:

- A setup project creates the users and the seed orders through the API, then the tests run. That follows CT-TAS 6.1.1 (automate preconditions before the real cases). An extra check that aborts when the seed file has a duplicate order id is the goal's "catch bad data before anything runs." It is not a syllabus step.
- Cases that only differ by amount and currency read those values from a table. That is data-driven testing as section 3.1.4 describes it.
- "Place order" is one function used by the API case and the UI case. That is the reusable step in sections 3.1.4 and 3.1.5.
- Only the setup project imports Playwright and builds the request context. Tests call the business-logic functions. That is the single driver and the adaptation boundary in CTAL-TAE 3.1.5 and 3.1.1.

## Sources

- ISTQB CT-TAS Syllabus v1.0 (2024/05/03), sections 3.2.3, 3.3.1, 3.3.2, 4.1.1, 4.2.1, 4.3.1, 6.1.1, 6.1.2, 6.2.1. [PDF](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CT-TAS_Syllabus_v1.0.pdf)
- ISTQB CTAL-TAE Syllabus v2.0 (2024/05/03), sections 3.1.1, 3.1.3, 3.1.4, 3.1.5, 4.2.1, 4.3.1, 5.1.1, 5.1.2, 7.1.1, 7.1.2, 8.1.2, 8.1.4. [PDF](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTAL-TAE_Syllabus_v2.0.pdf)
- ISTQB Glossary v4.8.1 (26 October 2026), term "quality gate". [glossary.istqb.org](https://glossary.istqb.org/), export [nstqb.org/istqbGlossary.pdf](https://nstqb.org/istqbGlossary.pdf)
