---
Creation_date: 2026-11-16 01:05
Modification_date: Monday 16th November 2026 01:20:00
Indexes:
  - "[[permanent_notes]]"
  - "[[QA_Automation]]"
  - "[[Playwright]]"
Source: ISTQB CTAL-TAE Syllabus v2.0, sections 2.2.1, 3.1.1 to 3.1.5; ISTQB CT-TAS Syllabus v1.0, sections 1.1.1, 1.1.3, 2.2.1, 3.1.1 to 3.1.3, 3.3.1, 3.3.3, 5.3.2; ISTQB Glossary v4.8.1, generic test automation architecture, test adaptation layer
---

----
# Automation strategy and architecture

Goal wording this note unpacks: "a test automation strategy and architecture fitted to their stack, covering what to automate, at which level (API, UI or unit), and what not to automate."

The four patterns named on the next bullet of the goal (bad data, data-driven tests, reusable steps, a driver layer) are used by the suite. They are covered in [Suite as a CI release gate](Suite%20as%20a%20CI%20release%20gate.md), with the architecture sections cited here.

## Definition

CT-TAS v1.0, section 1.1.1, says a strategy has to address: the intended purpose, the risks, the scope, the stakeholders, the tools, the test automation architecture (TAA), and the environments.

Objectives listed in that section include improved efficiency, broader and deeper coverage, better quality of the system, lower total cost and time to market, tests people cannot run by hand, shorter test execution time, and higher test frequency.

Section 1.1.2's technical success factors include a system that can be tested, a strategy that stays achievable inside time and cost and is kept up to date, a clear TAA (it points to CTAL-TAE 3.1.1), and a framework that is easy to use, documented and maintainable (it points to CTAL-TAE 3.1.3).

CTAL-TAE v2.0, section 3.1.2: a test automation solution (TAS) comes from the functional, non-functional and technical requirements of the system. The TAA is the technical design of that solution: tools and libraries, plugins, connectivity (including mocks, stubs, queues and protocols), links to test management and defect management, and version control.

### The generic test automation architecture (gTAA)

CTAL-TAE 3.1.1. The gTAA is "a high-level design concept that provides an abstract view of the communication between test automation and the systems that test automation is connected to, i.e., the SUT, project management, test management, and configuration management." It is also the list of capabilities to cover when you design a TAA. The glossary (v4.8.1) defines gTAA as "a representation of the layers, components, and interfaces that allows for a structured and modular approach to implement test automation."

Interfaces in section 3.1.1:

- **SUT interface:** the connection between the system under test and the test automation framework.
- **Project management interface:** progress of the automation development.
- **Test management interface:** mapping of test-case definitions to automated test cases.
- **Configuration management interface:** the CI/CD pipelines, the environments, and the testware.

Capabilities in the same section:

- **Test generation** (optional): automated design of cases from a test model.
- **Test definition:** defining and implementing cases and suites, separated from the system and from the tools, including high-level and low-level tests, test data, test cases and test libraries.
- **Test execution:** running the selected tests, plus logging and reporting.
- **Test adaptation:** adapting automated tests to the components or interfaces of the system, with different adaptors for APIs, protocols and services.

The glossary defines the **test adaptation layer** as "the layer in a test automation architecture which provides the necessary code to adapt test scripts on an abstract level to the various components, configuration or interfaces of the SUT." Section 3.1.1 describes that capability. The suite note covers the single driver.

### Layers of the framework

CTAL-TAE 3.1.3. The framework is the foundation of the solution and often includes a test harness (test runner), test libraries, test scripts and test suites. Keep the number of layers low. The three the section describes:

- **Test scripts:** the repository of cases and suite annotations. They call the business-logic layer (test steps, user flows, or API calls). They do not call core libraries directly.
- **Business logic:** libraries that depend on this system. They inherit or wrap the core libraries.
- **Core libraries:** libraries that do not depend on any one system, reused by any project on the same stack.

### What to automate, and at which level

ISTQB does not use "unit" for the bottom of the pyramid. CT-TAS 3.1.1: Mike Cohn's pyramid has three levels, "unit (the ISTQB calls this component), service, and UI." The service level is split, in that section, into component integration testing, contract testing, and API testing. UI testing is end-to-end testing through the GUI. So the goal's "API, UI or unit" is, in syllabus language, API (and contract, and component integration) at the service level, UI, and component testing where the goal says unit.

Section 3.1.1 asks you to draw the current distribution and a target. The pyramid (more testing at the bottom, stable and quicker) is the usual target when time and people allow. The ice-cream cone, hourglass and umbrella are unbalanced shapes the section describes so you can see what is missing. Section 3.1.2: the pyramid is not always reachable in one step. A realistic next shape (umbrella toward hourglass, for example) is a valid target. Mainframe and microservices systems do not offer the same levels.

Section 3.1.3: once current and target are drawn, the roadmap says what to test with automation (the scope) and how (the strategy), with a prioritised backlog and entry criteria. If code coverage is low, write component tests first. Test doubles move UI and API checks earlier, off real services, which is more consistent and easier to put in a pipeline.

CTAL-TAE 2.2.1 asks the scope questions in a form you can take to stakeholders: which activities (management, design, generation, execution), which levels, which types, which roles, which products, which systems must be compatible, whether the test data is good enough, and how to emulate cases you cannot reach (third parties).

CT-TAS 3.3.1 is the case-by-case filter:

- Can it be automated, and is the team able to do it?
- Does the coding effort have an adequate ROI? (section 5.1.1)
- Is there value in running it often?
- Is it functional or non-functional, and does it belong in smoke, regression, or confirmation?
- Is it repeatable?
- Will it stay easy to maintain when the system changes?
- Does it cover a business workflow people actually use?
- Does it overlap other tests, so steps and data can be reused?

CT-TAS 2.2.1: 100% automation coverage is not achievable. Prioritise the conditions with the most impact for the business and the investment, using risk assessment. That is the syllabus link to "risk." It is not a coverage-by-risk metric. See [Automation coverage](Automation%20coverage.md).

### What not to automate

CT-TAS 3.3.3 lists conditions that are difficult or impossible:

- Design and look-and-feel, including visual consistency across platforms. That judgement is subjective and needs a person.
- Cases with a lot of human interaction. The example is a loan application where an agent has to apply a regulation, make a decision, or call the customer.
- Technical blocks, such as an operating system that will not let a UI tool read a native text message outside the system under test.
- Long time dependencies that you cannot shorten (mocks, server responses, or changing the clock). The example is waiting two hours for a session timeout. Automating that is "not advised."

CTAL-TAE 1.1.1 states the limits in general: not every manual test can be automated; automation only checks what it was programmed to check; some quality characteristics are not machine-interpretable; and you need an automated test oracle.

CT-TAS 6.1.1 adds a sequencing rule: do not automate a manual regression test that does not already run correctly. It may be badly written, on invalid data, out of date, or failing because of a product defect. Automating it first produces a useless automated test.

CT-TAS 3.2.3: manual effort that remains is aimed at exploratory testing and end-user feedback, as a complement to automation, not as a leftover to be ashamed of.

## How to measure

A strategy is not one of the section 5.2.1 metrics. You can tell whether it is holding by the metrics it causes: functional coverage and code coverage, execution time, pass-fail ratio, maintenance hours, and ROI. Those notes are linked from the [folder index](README.md).

CT-TAS 3.1.1's baseline drawing (how much testing at each level, manual or automated, now and as a target) is the picture that shows "at which level." It is a distribution, not a percentage defined in section 5.2.1.

## How to collect and report

CT-TAS 1.1.1 and 5.3.2: the strategy is a document for the people who pay for it. It names purpose, risks, scope, tools, architecture and environments, and it shows the milestones automation is supposed to hit. Section 1.1.3 says the person responsible for choosing the approach and the tools is a test architect or a test manager with automation knowledge. Section 2.2.1 says the test automation engineer cooperates with test analysts and other stakeholders on the objectives.

CTAL-TAE 3.1.1's project-management interface is where development progress of the automation is reported. The test-management interface is where defined cases map to automated cases, which is also the traceability CT-TAS 1.1.2 asks for.

Review the distribution when you review coverage. A rise in UI tests with flat component coverage is the ice-cream or umbrella shape section 3.1.1 warns about.

## Pitfalls

- Calling the bottom of the pyramid "unit" in an ISTQB report. The syllabus name is component testing.
- Starting at the UI because that is what the users see. Section 3.1.3 says to repair a thin bottom first. Section 5.1.1 says the pyramid is also how you protect ROI.
- Automating the conditions in section 3.3.3 because they are in the manual pack.
- A framework with a layer per technical concern. Section 3.1.3 says to keep the layer count low.
- Test scripts that call core libraries directly. Section 3.1.3 puts the business-logic layer between them.
- Assuming one shape fits a mainframe and a microservice system (section 3.1.2).

## Example (Playwright and CI)

This example is practice. It places Playwright inside the gTAA. It is not a syllabus diagram.

For an API-plus-UI product:

- Component tests stay in the application's own test tool, in the build job. That is the level ISTQB calls component, where the goal says unit. Playwright is not that layer.
- Service level: Playwright's API client calls the real service for API tests, and a contract test (see the Pact notes in this folder) covers the consumer-provider agreement. CT-TAS 3.1.1 names both.
- UI level: a thin Playwright project for the journeys section 3.3.1 would keep (frequent, repeatable, worth running often).
- Business-logic layer: functions such as "place order" that the API tests and the UI tests both call.
- Core library: polling helpers and reporting hooks that do not mention this product.
- Test adaptation: one module that constructs the Playwright request context or browser. Tests do not import Playwright themselves. That is the practical reading of test adaptation and of the single driver in CTAL-TAE 3.1.5. The syllabus does not say what that buys you beyond the adaptor.

What this example leaves manual, following section 3.3.3: visual review of a redesigned screen, and any step that needs a person to apply a business exception.

## Sources

- ISTQB CTAL-TAE Syllabus v2.0 (2024/05/03), sections 1.1.1, 2.2.1, 3.1.1, 3.1.2, 3.1.3, 3.1.4, 3.1.5. [PDF](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTAL-TAE_Syllabus_v2.0.pdf)
- ISTQB CT-TAS Syllabus v1.0 (2024/05/03), sections 1.1.1, 1.1.2, 1.1.3, 2.2.1, 3.1.1, 3.1.2, 3.1.3, 3.2.3, 3.3.1, 3.3.3, 5.1.1, 5.3.2, 6.1.1. [PDF](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CT-TAS_Syllabus_v1.0.pdf)
- ISTQB Glossary v4.8.1 (26 October 2026), terms "generic test automation architecture" and "test adaptation layer". [glossary.istqb.org](https://glossary.istqb.org/), export [nstqb.org/istqbGlossary.pdf](https://nstqb.org/istqbGlossary.pdf)
