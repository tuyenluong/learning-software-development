---
Creation_date: 2026-11-16 01:05
Modification_date: Monday 16th November 2026 01:05:00
Indexes:
  - "[[permanent_notes]]"
  - "[[QA_Automation]]"
  - "[[Playwright]]"
Source: ISTQB CT-TAS Syllabus v1.0, sections 2.2.1, 3.1.3, 5.2.1, 5.4.1, 6.1.1, 6.2.1; ISTQB CTAL-TAE Syllabus v2.0, sections 2.2.1, 3.1.4, 6.1.3; ISTQB Glossary v4.8.1, coverage
---

----
# Automation coverage

Goal wording this note unpacks: "the share of in-scope tests or requirements that are automated, tracked per risk area."

## Definition

CT-TAS v1.0, section 5.2.1, classifies three different numbers. Only two of them are coverage.

**Functional coverage of test automation** "indicates the percentage of functional requirements covered by automated test cases."

**Code coverage** "tracks how many lines of code is exercised by lower level (i.e., component) tests." The same paragraph says there is no absolute percentage that means coverage is adequate, and that 100% code coverage is often hard to reach except on the simplest software. More coverage is treated as better because it raises confidence in the system under test. Adding low-level automated tests is expected to raise code coverage.

**Number of automated test cases** shows progress of the automation project. The syllabus says this count "does not reveal much information; for example, it does not indicate the level of coverage."

The glossary (v4.8.1) defines coverage, also called test coverage, as "the degree to which specified coverage items are exercised by a test suite, expressed as a percentage." That is the general term. The automation-specific definitions above are the ones in CT-TAS 5.2.1.

Two further limits are in the same syllabus:

- Section 2.2.1: exhaustive testing is not achievable, and "100% test automation coverage is not achievable." Choose the conditions that matter most for the business and for the investment, using risk assessment.
- Section 6.1.1: automating 100% of the existing manual test cases is not the same as 100% of the test cases that could be automated. As manual execution time comes back, use it to find further tests and raise coverage.

Section 6.2.1 separates the two coverage checks in practice. Code-coverage tools show how much code the component suite exercises, and where the gaps are. Functional coverage of the system is found with a requirements traceability matrix, which shows functionality that no test case covers yet. The matrix sentence says "any test cases", not only automated ones. Section 5.2.1 is the sentence that ties functional coverage to automated test cases. Keep those two counts apart.

## How to measure

The syllabus calls functional coverage a percentage. It does not write an algebraic formula. It does not define a numerator or a denominator beyond "functional requirements covered by automated test cases."

It describes code coverage as how many lines lower-level tests exercise. It then discusses that number as a percentage ("no absolute percentage", "100% code coverage") without writing a formula.

It does not define "share of in-scope tests" as coverage. That share is closer to the count of automated test cases, which section 5.2.1 says is not coverage, or to the share of manual cases converted, which section 6.1.1 says is not full coverage either.

It does not say to track coverage per risk area. Risk shows up when you choose what to automate (section 2.2.1, and the suitability questions in section 3.3.1, covered in [Automation strategy and architecture](Automation%20strategy%20and%20architecture.md)). CT-TAS 5.4.1 does say report data can be used to "expand the functional coverage of test automation in future sprints" and to "focus more on defect clusters." That is a planning use of the numbers, not a per-risk coverage formula.

CTAL-TAE v2.0, section 2.2.1, asks which test levels and test types the solution must support. That is scope, not a coverage percentage. Section 3.1.4 says test-driven development makes a desired code coverage easier to reach, and that automated behaviour-driven scenarios "ensure coverage of specifications." Neither sentence is a formula.

## How to collect and report

CT-TAS 5.2.1: keep the cost of measuring low, usually by automating collection and reporting. Use the numbers to decide whether the solution still fits the project, whether it can take new test conditions, and whether it is maintainable.

CT-TAS 6.2.1 is the collection method the syllabus names: a code-coverage tool on the component suite, and a requirements traceability matrix for functional gaps. CT-TAS 1.1.2 lists "traceable automated tests to test case definitions and requirements" as a success factor, which is what makes the matrix possible.

CTAL-TAE 6.1.3: a test progress report goes to management, operational and technical stakeholders. Management looks at trends, including how many test cases were added since the last run. Publish the report where those people already look (a site, a mailing list, a chat message, or the test-management tool). CT-TAS 5.4.1 says to emphasise the metrics the audience actually uses, and that one use of the data is to expand functional coverage in later sprints.

A useful report therefore has three lines, because the syllabus treats them as different: functional requirements covered by automated cases, lines exercised by component tests, and the count of automated cases (labelled as progress, not as coverage).

## Pitfalls

- Treating the count of automated tests as coverage. Section 5.2.1 forbids that reading.
- Treating "we automated every manual case" as complete coverage. Section 6.1.1 forbids that reading.
- Chasing 100% code coverage. The syllabus says that percentage is often unreachable and that no percentage is defined as enough.
- Mixing the traceability matrix (any test case) with functional coverage of automation (automated test cases).
- Slicing coverage by risk area and presenting the slice as an ISTQB metric. Prioritising by risk is in the syllabus. A coverage-by-risk formula is not.
- Counting UI tests and component tests in one percentage. Code coverage in section 5.2.1 is about lower-level, component tests. CT-TAS 3.1.3 says low code coverage is a sign that component cases are missing.

## Example (Playwright and CI)

This example is practice in this repo's stack. It is not an ISTQB procedure, and the threshold below is not from the syllabus.

Keep a small matrix in the test repo, one row per functional requirement that is in scope for automation: requirement id, risk rank used to order the work, and the Playwright test title that covers it (or empty). A CI step counts rows whose test title is non-empty, and prints:

- functional coverage of automation = covered rows / rows in the matrix
- automated test count = the Playwright list-test count, reported on its own line so it is not called coverage

Do not use that Playwright count, or a UI-suite count, as code coverage. Code coverage comes from the component-test job (the language's coverage tool), which is the level section 5.2.1 is talking about.

The risk rank on the row is how this team orders the backlog. It is not a syllabus coverage metric. See [Automation strategy and architecture](Automation%20strategy%20and%20architecture.md).

## Sources

- ISTQB CT-TAS Syllabus v1.0 (2024/05/03), sections 1.1.2, 2.2.1, 3.1.3, 5.2.1, 5.4.1, 6.1.1, 6.2.1. [PDF](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CT-TAS_Syllabus_v1.0.pdf)
- ISTQB CTAL-TAE Syllabus v2.0 (2024/05/03), sections 2.2.1, 3.1.4, 6.1.3. [PDF](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTAL-TAE_Syllabus_v2.0.pdf)
- ISTQB Glossary v4.8.1 (26 October 2026), term "coverage". [glossary.istqb.org](https://glossary.istqb.org/), export [nstqb.org/istqbGlossary.pdf](https://nstqb.org/istqbGlossary.pdf)
