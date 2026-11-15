---
Creation_date: 2026-11-16 01:05
Modification_date: Monday 16th November 2026 01:20:00
Indexes:
  - "[[permanent_notes]]"
  - "[[QA_Automation]]"
  - "[[Playwright]]"
Source: ISTQB CTAL-TAE Syllabus v2.0, sections 4.3.1, 6.1.3, 8.1.2, 8.1.3; ISTQB CT-TAS Syllabus v1.0, sections 1.1.2, 2.1.1, 2.2.1, 5.3.2, 6.1.1, 6.2.1
---

----
# Handover and maintainability

Goal wording this note unpacks: "a handover, meaning docs and coaching so their team owns the suite."

The time you spend maintaining the suite is [Maintenance effort](Maintenance%20effort.md). The architecture of the suite is in [Automation strategy and architecture](Automation%20strategy%20and%20architecture.md) and [Suite as a CI release gate](Suite%20as%20a%20CI%20release%20gate.md).

## Definition

"Handover" does not appear in either syllabus. The work the goal is pointing at does, in pieces: the team can run and change the solution, the solution is documented, people are trained, and ownership sits inside the organisation.

**Ownership.** CT-TAS v1.0, section 2.1.1, compares three arrangements. An in-house solution keeps "all costs, resources, risks, and governance" inside the organisation, and it needs test automation engineers who can develop it, hired or trained. A vendor tool shares ownership according to the contract, and the organisation's testers need the vendor's training. Outsourcing leaves the work, the cost and the tool ownership with the outsource company. The section says that last option fits when the organisation will not hire automation engineers. It also says the contract then needs measurable expectations and metrics, so progress stays visible. A goal that says "their team owns the suite" is the in-house arrangement in that section, not the outsource one.

**Coaching.** Section 2.2.1: someone has to "train, motivate, and build the team." A test automation engineer cooperates with test analysts and other stakeholders on the objectives. The same section says 100% automation coverage is not achievable, so the team has to be able to prioritise. Training that only shows which button to press, and not how to choose the next case, misses that part.

**Docs.** CT-TAS 1.1.2 lists a framework that is "easy to use, well documented and maintainable", "documented automated test cases", traceability from automated tests to case definitions and requirements, and "easy troubleshooting." CTAL-TAE v2.0, section 8.1.2, under documentation: "what the test automation code does, and how it should be used", user documentation for the solution, and the reports and logs the solution produces.

**Maintainability of the code.** CTAL-TAE 4.3.1. Maintainability depends on programming standards and on what the automation engineers expect of each other. The section's rule of thumb is the clean-code principles in Robert C. Martin, *Clean Code* (2008), which it summarises as:

- a common naming convention, with meaningful names
- a logical, common project structure
- avoid hardcoding
- avoid too many parameters
- avoid long, complex methods
- use logging
- use design patterns where they help
- focus on testability

Hardcoding "reduces development time" and is "time consuming to maintain" once the data changes. Data-driven testing, or constants for values that rarely change, keeps the places you must edit small. Design patterns, as in section 3.1.5, support maintainable code when they are used properly. Static analysers and formatters protect readability. An agreed branching strategy (features, releases, defect fixes) makes the history understandable.

Section 8.1.2 adds the structural habits that lower maintenance: one library function for a repeated step, setup and teardown for repeated configuration, standard verification helpers, and a pilot before everyone moves to a new core-library version. Section 8.1.3: naming of new code stays consistent with section 4.3.1, and scripts that rarely run are candidates to remove so there is less to maintain.

**Who owns the tools, and where the driver sits.** Playwright is not named in either syllabus. What the syllabi do say:

- In-house ownership, so the team is not stuck on a vendor timeline for a defect in the tool (CT-TAS 2.1.1).
- Open-source tools as a licensing choice: no licence fee, and most open-source licences allow the tool to be modified (CT-TAS 2.1.2). That is a licence point.
- Core libraries independent of one system, a business-logic layer, and a single driver, so product tests do not call the tool directly (CTAL-TAE 3.1.3 and 3.1.5).
- CT-TAS 6.1.2: when the solution itself is updated, the suites, the stubs and drivers, and the infrastructure have to be changed and tested before you deploy the update. Release notes of known defects go to the automation engineers and the other stakeholders.

## How to measure

Handover is not a section 5.2.1 metric. The syllabus signals that the team really owns the solution when these are true:

- CT-TAS 6.2.1: hours fixing the solution are not greater than the manual testing time saved. A team that owns the suite and still spends more time repairing it than they save has not been handed a maintainable solution.
- CT-TAS 1.1.2: cases are documented and traceable, and troubleshooting is easy. You can check the first by the traceability matrix ([Automation coverage](Automation%20coverage.md)). You can check the second by whether a failure can be diagnosed from the published report ([Pass-fail and stability](Pass-fail%20and%20stability.md)).
- CT-TAS 2.1.1: if a supplier is still in the picture, the contract's metrics are defined. If the team is in-house, those metrics are the same ones the folder already tracks, and the team can produce them without the original author.

CTAL-TAE 7.1.4 (static analysis of the automation code) is the quality check section 4.3.1 is pointing at: analysers on the test code, not only on the product, including secrets accidentally stored in scripts. That is a maintainability and security check, not a handover metric.

## How to collect and report

CTAL-TAE 8.1.2 lists documentation as an area you can improve, alongside scripting and the framework. Treat the docs as part of the solution, in the same repository, and say in them how to run the suite, how to add a data-driven case, and how to read a failure. Section 8.1.2 warns that features nobody uses add complexity and reduce reliability and maintainability. The same warning applies to a long guide nobody can follow. CT-TAS 1.1.2 wants the framework easy to use.

CT-TAS 5.3.2: test managers often build a competency and skill matrix, then close the gaps with training and with implementation tasks. CT-TAS 2.2.1 says the team has to be trained, motivated and built, not only staffed. A handover in which only the original author can add a test has not met those sections.

CT-TAS 6.2.1: "ensure knowledge and awareness of reusable components and consistent utilization." The coaching content is the library you already have (the login, the order flow), not a new framework.

Publish the handover the way CTAL-TAE 6.1.3 publishes any other test report: to the people who will own the next change. Include the known defects of the solution, which is the release-note habit in CT-TAS 6.1.2.

## Pitfalls

- Outsourcing the build and calling the last week a handover. CT-TAS 2.1.1 says that in an outsource arrangement the ownership of the tools stays with the outsource company.
- Documentation that describes the tool, and not "what the test automation code does, and how it should be used" (CTAL-TAE 8.1.2).
- A coding style the next person cannot extend: hardcoded data, copied steps, no logging (CTAL-TAE 4.3.1).
- Test scripts that call the tool directly. CTAL-TAE 3.1.3 puts a business-logic layer between the scripts and the core libraries, and section 3.1.5 uses one driver to talk to the system under test. CT-TAS 6.1.2 says to test a changed driver before you deploy the updated solution.
- Training that never covers what not to automate. The team will otherwise automate the conditions in CT-TAS 3.3.3. See [Automation strategy and architecture](Automation%20strategy%20and%20architecture.md).

## Example (Playwright and CI)

This example is practice. It is not an ISTQB procedure.

The repository the team keeps after the engagement contains:

- `README`: how to install, how CI chooses the smoke project and the nightly project, and how to read the HTML report and the trace. That is the "how it should be used" document from CTAL-TAE 8.1.2.
- `flows/`: the reusable steps (place order, log in). Tests call these. CT-TAS 6.2.1 wants the team to know they exist and to use them.
- `driver/`: the only module that imports Playwright and builds a request context or a browser. Product flows do not import Playwright. That is the single driver in CTAL-TAE 3.1.5.

Coaching, following section 2.2.1, is a working session in which a team member adds one data row and one negative case that the syllabus would leave manual, and says which is which. The session is done when they can do that without the original author, and when the static-analysis job (CTAL-TAE 7.1.4) still passes on the test code.

## Sources

- ISTQB CT-TAS Syllabus v1.0 (2024/05/03), sections 1.1.2, 2.1.1, 2.1.2, 2.2.1, 5.3.2, 6.1.1, 6.1.2, 6.2.1. [PDF](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CT-TAS_Syllabus_v1.0.pdf)
- ISTQB CTAL-TAE Syllabus v2.0 (2024/05/03), sections 3.1.3, 3.1.5, 4.3.1, 6.1.3, 7.1.4, 8.1.2, 8.1.3. [PDF](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTAL-TAE_Syllabus_v2.0.pdf)
