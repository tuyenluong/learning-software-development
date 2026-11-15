---
Creation_date: 2026-11-16 01:05
Modification_date: Monday 16th November 2026 01:05:00
Indexes:
  - "[[permanent_notes]]"
  - "[[QA_Automation]]"
  - "[[Playwright]]"
Source: ISTQB CT-TAS Syllabus v1.0, sections 1.1.3, 2.1.3, 3.3.1, 5.1.1, 6.2.1; ISTQB CTAL-TAE Syllabus v2.0, section 1.1.1
---

----
# Cost against benefit

Goal wording this note unpacks: "build and maintenance effort compared with the manual effort saved, which is how you show return on investment."

## Definition

This one is in the syllabus. CT-TAS v1.0, section 5.1.1, is the learning objective "show the return on investment of building a test automation solution."

"The ROI calculation can provide meaningful feedback at any given moment in a project lifecycle by demonstrating the return for an activity for the effort invested." It "can be further adjusted by including both manual tester costs and TAE costs by simply multiplying the time spent with their respective labor costs."

To calculate ROI, determine the investment (time and cost) and the savings:

`ROI = Savings / Investment`

"The savings and the investment can be calculated considering different metrics and data, in different measures and units." In this syllabus "a simple model is used to demonstrate the approach, with time units and not the cost." If an activity is known only as a cost, "that amount can be converted to time using a rate specific to the project."

The syllabus says savings exist because the same tests run in much less time than by hand, so they can run more often, and more tests can be executed.

CTAL-TAE v2.0, section 1.1.1, lists the same trade-off in words and without a formula: automation is more efficient in the use of test resources and gives quicker feedback, and the disadvantages include the initial investment, the cost of a test automation engineer, hardware and training, and "time to develop and maintain a test automation solution."

CT-TAS 1.1.3 is the go / no-go before you start: cost of introduction (people, hardware, training), how early in the lifecycle you are, how long the project will last, and maintenance cost. A short project may not have time for automation to pay back.

## How to measure

The only formula the syllabus writes is `ROI = Savings / Investment`.

It does not expand Savings or Investment into a longer equation. It lists the metrics to consider.

Savings:

- Time to run a test case manually
- Time to run an automated test case
- Number of test cases
- Number of test runs

Investment:

- Time to set up test automation
- Average time to develop automated test scripts
- Number of automated test scripts implemented
- Average maintenance time of an automated test script
- Time to run an automated test script
- Percentage of failed automated test scripts
- Number of test cases defined
- Number of test runs

Any arithmetic that multiplies those lists together is an example, not section 5.1.1. The section also says the simple model uses time. Money comes in by multiplying time by labour cost, or by converting a money cost into time with a project rate.

Section 5.1.1 adds two connections between the metrics:

- If the planned project duration is shorter than the point where the investment is paid back, do not introduce automation. Running the tests manually saves time and effort.
- Because investment depends heavily on automated execution time, "applying the test pyramid and implementing test cases at the right test level can reduce this execution time and improve ROI."

The section illustrates payback with a graph of sprints (figure 2 in the syllabus): the sprint at which automation has returned its investment. The graph is an illustration. The syllabus does not publish the data behind it, so this note does not invent those sprint numbers.

CT-TAS 3.3.1 asks, when you choose cases, "does the coding effort provide an adequate ROI?" and points back to section 5.1.1. CT-TAS 6.2.1 gives a related warning in hours: something is wrong if TAS maintenance time is greater than the manual testing time.

## How to collect and report

Collect the lists above in one unit, normally hours (section 5.1.1). Automate what you can: CI already has execution time, including TAS build time ([Execution time](Execution%20time.md)), and the failure percentage is the failed-script input. Manual time, setup time, development time and maintenance time still need a human record ([Maintenance effort](Maintenance%20effort.md)).

Recalculate at any moment in the lifecycle, not only at the end. On an Agile project, the syllabus says to forecast sprints and to read the payback sprint off that forecast.

CT-TAS 2.1.3 says the budget for a strategy also includes tools, licences, hardware and training, and the cost of integrating results into test management. Those are costs of introduction (section 1.1.3). The simple ROI model does not list licences as a separate variable. Convert them to time with the project rate if you want them inside `ROI = Savings / Investment`, and say that you did.

CT-TAS 5.3.2: a proposal to management should state the gaps, the future costs, the recommendations, the business value and the cost reductions. That is the audience for this number. CT-TAS 5.4.1 adds that different stakeholders need different metrics emphasised. ROI is a management metric. The pass-fail ratio and the logs are not a substitute for it.

## Pitfalls

- Publishing a long ROI formula as if it were printed in section 5.1.1. Only `ROI = Savings / Investment` is printed.
- Mixing hours and money in the same fraction without the conversion the section allows.
- Ignoring failed scripts. They are an investment input, so a suite that fails often costs more than its execution time suggests. The syllabus does not say how to fold the percentage into Investment.
- Automating a short project that ends before the payback sprint (sections 5.1.1 and 1.1.3).
- Putting almost all tests at UI level and then wondering why ROI is poor. Section 5.1.1 ties better ROI to the test pyramid and to shorter execution.
- Forgetting maintenance. A setup-only investment overstates the return. Section 6.2.1 is the check: maintenance time against manual time saved.
- Treating "more tests" as the benefit. The savings story in section 5.1.1 is time, frequency, and the extra runs that frequency allows.

## Example (Playwright and CI)

This example is practice. The arithmetic that turns the lists into Savings and Investment is assumed here so the syllabus formula can be applied to made-up hours. Section 5.1.1 does not specify this arithmetic.

Assume one API suite in Playwright:

| Input from section 5.1.1 | Assumed value |
|---|---|
| Time to run one case manually | 6 minutes |
| Time to run one automated case | 4 seconds |
| Number of test cases, and of automated scripts | 40 |
| Number of test runs | 30 (about one a weekday for six weeks) |
| Time to set up the TAS | 40 hours |
| Average time to develop one script | 1 hour |
| Average maintenance time of one script, over those six weeks | 0.25 hours |

Example arithmetic, stated as an assumption:

- Savings hours = (6/60 − 4/3600) × 40 × 30 = 118.7 hours
- Investment hours = 40 + (1 × 40) + (0.25 × 40) = 90 hours
- The automated run time and the percentage of failed scripts are in the syllabus investment list. This example leaves them out of the sum and would have to say so if they were material.
- ROI = 118.7 / 90 = 1.3

On these assumed numbers the suite has returned the time invested inside the six weeks. If the engagement ended in week two, section 5.1.1 says manual execution would have been the better choice, because payback would still be in the future. Replace every assumed cell with measured hours before you show this to a client. Labour cost, if you need money, is those hours times the tester rate and the automation-engineer rate, which is the adjustment the section allows.

## Sources

- ISTQB CT-TAS Syllabus v1.0 (2024/05/03), sections 1.1.3, 2.1.3, 3.3.1, 5.1.1, 5.3.2, 5.4.1, 6.2.1. [PDF](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CT-TAS_Syllabus_v1.0.pdf)
- ISTQB CTAL-TAE Syllabus v2.0 (2024/05/03), section 1.1.1. [PDF](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTAL-TAE_Syllabus_v2.0.pdf)
