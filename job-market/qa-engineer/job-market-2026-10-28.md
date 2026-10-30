# Job Market 2026-10-28: QE / SDET / QA Automation

**Date:** 28 Oct 2026
**Purpose:** QA / QE automation market facts. This report covers QA, SDET and test automation roles only; backend engineer findings from this window are in [../backend-engineer/backend-job-market-2026-10-30.md](../backend-engineer/backend-job-market-2026-10-30.md#earlier-data-21-oct-and-28-oct).
**Coverage:** catch-up for the weekly run that failed on **Fri 23 Oct 2026**. Window covered: **17–28 Oct 2026**.
**Builds on:** [qe-job-market-2026.md](qe-job-market-2026.md) (baseline, 21 Oct 2026).

> **How to read the numbers**
> - **Skillenai** = a job-posting index (90-day rolling windows, ending 18–27 Oct 2026). It shows how often a skill shows up in postings, not total hiring. Its SDET sample is small (132 postings). Its headline "demand vs prior 4 weeks" is a *share* change, so a rising share on a small posting count is noise.
> - **ITviec counts** = live listing counts pulled from itviec.com tag pages on **28 Oct 2026**. Snapshot only; they move week to week.
> - **ROLIVA** = a QA/test-specific job board. Counts are its own live listings on 28 Oct 2026 (2,000 QA and test engineer listings), so percentages describe *that board*, not the whole market.
> - **JobRemotely** = a remote-job board, snapshot dated 1 Oct 2026 (687 listings). US-weighted.
> - **Jobpedia.AI** = a posting aggregator that publishes per-role skill shares over 90-day windows.
> - **AutomationDataCamp (ADC)** = a French QA training company's public barometer of French job ads (405 "QA"-titled + 1,180 "test"-titled). European and French-language, so read it for direction, not for Vietnam.
> - **Mentorpiece Vacy Index** (reported via Habr) = share of tech companies with at least one open role of a given type. Company-level, not posting-level.
> - Anything marked **(est.)** is an estimate or conversion made for this report. VND→USD uses about **26,000 VND/USD**, which is approximate.
> - **Job-alert sample** = aggregate counts from a sample of LinkedIn/Glassdoor job-alert emails, mostly job titles. No personal data, recruiter names or contacts are included.

---

## Top skills at a glance (28 Oct 2026)

**QE / automation — learn these first**
1. **CI/CD** — 56.1% of SDET postings ([Skillenai SDET](https://skillenai.com/data/role/software-development-engineer-in-test-sdet)); 35.1% of French QA ads ([ADC](https://www.automationdatacamp.com/blog-post-barometre-competences-qa)).
2. **Python**, then **Java** as the second language — Python 51.5%, Java 35.6% of SDET postings.
3. **Playwright** — 47.0% of SDET postings, and now **#1 in French QA ads at 24.2%, ahead of Selenium at 21.7%**. Playwright has crossed over.
4. **API testing** — 22.0% of SDET postings, 21% of QA-engineer roles ([Jobpedia](https://jobpedia.ai/roles/qa-engineer)); Postman named in 20% and REST Assured in 15.3% of French QA ads.
5. **SQL** — 21% of QA-engineer roles ([Jobpedia](https://jobpedia.ai/roles/qa-engineer)), 14.8% of French QA ads.

---

## What changed this week (21 Oct → 28 Oct 2026)

**Job-alert sample: 28 new alerts.** A sample of 28 job-alert emails dated 17–28 Oct was counted. All 28 were automated digest emails from LinkedIn job alerts and Glassdoor. None came from a named recruiter and none stated a salary range.

**The changes worth acting on**

| # | Change | 21 Oct (baseline) | 28 Oct | Read |
|---|---|---|---|---|
| 1 | **Cloud platforms now have real numbers** | "AWS is most common", no QA-specific count | QA postings: **AWS 10%, Azure 10%, GCP 4%** (ROLIVA, 2,000 listings); remote listings: **AWS 53, GCP 31, Azure 23 of 687** (JobRemotely) | AWS first. Below AWS the two sources disagree, so the ordering is soft. See §1B. |
| 2 | **Playwright overtook Selenium** in French QA ads | Playwright 47.1% of SDET postings, Selenium 35.7% | Playwright **24.2% vs Selenium 21.7%** of QA ads; in SDET postings Playwright 47.0% vs Selenium 34.8% | Playwright is no longer the challenger. Teach it as the default, Selenium as legacy maintenance. |
| 3 | **Manual QA is shrinking faster than automation** | — | Companies with open **manual QA** roles 14.1% → **9.5%** (−33%); automation QA 18.6% → 17.5% (−6%); **AI-QA 3.9% → 5.1%** (+31%) (Mentorpiece Vacy Index, Oct 2026) | The manual-to-automation move is now a survival move, not a pay-rise move. |
| 4 | **Vietnam testing listings ticked up** | ITviec: tester 58, automation test 36, playwright 12, sdet 11 | ITviec: **tester 61, automation test 40, playwright 13, sdet 9** | Small but consistent gain in automation-flavoured listings; SDET as a title is still rare in Vietnam. |

**SDET shares, 21 Oct → 28 Oct** (Skillenai SDET; postings 140 → 132, −5.7%):

| Skill | 21 Oct | 28 Oct | Skill | 21 Oct | 28 Oct |
|---|---|---|---|---|---|
| CI/CD | 57.1% | 56.1% | TypeScript | 28.6% | 29.5% |
| Python | 50.7% | 51.5% | Kubernetes | 22.9% | 24.2% |
| Playwright | 47.1% | 47.0% | GitHub Actions | 22.1% | 22.7% |
| JavaScript | 36.4% | 34.8% | API testing | 21.4% | 22.0% |
| Selenium | 35.7% | 34.8% | Docker | 20.0% | 21.2% |
| Java | 35.7% | 35.6% | Performance testing | 20.0% | 19.7% |
| Jenkins | 32.9% | 31.8% | Cypress | 32.1% | 31.1% |

**ITviec Vietnam, 21 Oct → 28 Oct 2026** (live listing counts, same tag pages):

| Tag | 21 Oct | 28 Oct |
|---|---|---|
| tester | 58 | **61** |
| automation test | 36 | **40** |
| playwright | 12 | **13** |
| sdet | 11 | **9** |

([tester](https://itviec.com/it-jobs/tester), [automation-test](https://itviec.com/it-jobs/automation-test), [playwright](https://itviec.com/it-jobs/playwright), [sdet](https://itviec.com/it-jobs/sdet))

**Job-alert sample (aggregate, 17–28 Oct):**
- **28 alerts in 11 days** — roughly the same daily rate as the baseline's 6-month sample.
- About **50%** of alerts were QA/automation roles, the same as the baseline.
- Recurring QA titles: Senior QA Engineer, SDET, Automation Test Engineer (Middle/Senior), QC Auto, QA Analyst.
- **No salary ranges were stated in any of the 28 alerts.** Salary figures in §4 come from the ITviec survey and posted ranges on live listings, not from this window's job alerts.

---

## 0. Bottom line

1. **The QE market keeps moving toward "engineer who tests".** CI/CD 56.1%, Python 51.5%, Playwright 47.0%, Java 35.6% top SDET postings, and **Playwright has now overtaken Selenium** in an independent European ad survey (24.2% vs 21.7%). Meanwhile the share of companies with open *manual* QA roles fell **33%** in six months.
2. **Cloud is settled at the top and unsettled below it.** AWS leads on both sources: **10% of QA postings** (ROLIVA) and **53 of 64** cloud-naming remote listings (JobRemotely). Azure and GCP swap places between the two (Azure 10% vs GCP 4% on one; GCP 31 vs Azure 23 on the other), so **anything below AWS is a soft ordering**.
3. **QA pay data is unchanged.** ITviec 5–8 year medians are still **25.3M VND for Tester and 29.75M for QA-QC**; no new salary survey appeared this window. Live ITviec listings showed a manual-plus-automation tester role "up to 28M net" and a QC Manager role "up to 55M".
4. **AI in testing is now native tooling, and review discipline is the skill.** Playwright ships agents and an MCP server, 20.7% of French QA ads mention AI, and AI-QA is the only QA role type growing (+31%, from a small base).

---

## 1. Most-demanded skills, with frequency signals

### A. QE / Automation / SDET

**Global: Skillenai, SDET title, 132 postings, 90 days to 22 Oct 2026** ([source](https://skillenai.com/data/role/software-development-engineer-in-test-sdet))

| Skill | Share of postings |
|---|---|
| CI/CD | 56.1% |
| Python | 51.5% |
| Playwright | 47.0% |
| Java | 35.6% |
| Selenium | 34.8% |
| JavaScript | 34.8% |
| Test automation | 33.3% |
| Jenkins | 31.8% |
| Cypress | 31.1% |
| TypeScript | 29.5% |
| Kubernetes | 24.2% |
| GitHub Actions | 22.7% |
| API testing | 22.0% |
| Docker | 21.2% |
| Performance testing | 19.7% |

- **Playwright vs Selenium is now a dead heat in this sample** (47.0% vs 34.8%), and Playwright has a clear lead in the French ad survey (24.2% vs 21.7%).
- **Messaging, Kafka and distributed systems are still absent from the SDET top 15.** For a QE they remain a **differentiator**, not a requirement.

**QA-engineer roles across all levels: Jobpedia.AI, 313 roles, 260 employers, 90 days to 27 Oct 2026** ([source](https://jobpedia.ai/roles/qa-engineer))

| Skill | Share | Skill | Share |
|---|---|---|---|
| CI/CD | 38% | SQL | 21% |
| Python | 38% | Git | 20% |
| Test automation | 34% | TypeScript | 20% |
| Agile | 22% | JavaScript | 20% |
| API testing | 21% | Java | 19% |

- Preferred skills: CI/CD 13%, test automation 13%, Docker 8%, **AI 8%**, AWS 7%.
- **74% remote**, median pay **$125k** (109 of 313 state pay). 45% ask 5–7 years, 26% ask 3–4 years.

### B. Cloud platforms for QA roles

This is the section the baseline could not answer. Two independent counts, both taken this month:

| Cloud | ROLIVA (QA and test engineer listings) | JobRemotely (remote listings) |
|---|---|---|
| **AWS** | **10%** (190 of 2,000) | **53** of 687 (7.7%; 53 of the 64 that name a cloud) |
| **Azure** | **10%** (208 of 2,000) | 23 (3.3%) |
| **GCP** | **4%** (77 of 2,000) | 31 (4.5%) |

Sources: [ROLIVA QA-engineer skill insights](https://rolivajobs.com/insights/skills/qa-engineer) (2,000 QA and test engineer listings, 325 employers, 67 countries, as of 28 Oct 2026); [JobRemotely cloud-jobs board analysis](https://jobremotely.io/blog/cloud-jobs-aws-azure-gcp) (687 open listings, 64 naming a cloud, 1 Oct 2026).

**Read:**
- **AWS first.** It is the only cloud both sources agree on, and it leads the remote board by a wide margin (53 vs 31).
- **Treat the ordering below AWS as soft.** ROLIVA puts **Azure at 10% and GCP at 4%**; JobRemotely puts **GCP at 31 and Azure at 23**. The two disagree on which is second, and by a lot. What is safe to say: Azure and GCP are each roughly a third to a half of AWS, and neither is the one to learn first.
- JobRemotely adds a useful nuance: **Azure is rarely named alone** — only 4 listings named Azure and nothing else, and 70% of the listings naming Azure named all three clouds. So "Azure" in a posting often means "we are multi-cloud", not "we are an Azure shop".
- **Teaching consequence:** learn one cloud, AWS, well enough to run and debug tests against services deployed there. Azure and GCP are a comparison lesson, not a track.

Other cloud-adjacent signals from ROLIVA's QA snapshot: **Docker 6% (114)**, **Kubernetes 6% (112)**, **Kafka 2% (47)**, **LLM 2% (39)**, **PostgreSQL 1% (22)**. Python leads the whole board at **27% (544)**, then Agile 16%, Java **15% (301)**, SQL 14%, Jira 13%. Vietnam appears as **24 of the 2,000 listings (1%)**.

**Vietnam: ITviec, 28 Oct 2026:** posted ranges visible on the same day's testing listings: a manual-plus-automation tester role "up to 28M net" and a QC Manager role "up to 55M". Single listings, not survey data. One bank senior quality engineer role was in this window's ITviec sample.

---

## 2. Must-have vs nice-to-have vs differentiator (mid → senior)

*Synthesis based on the frequencies above and the interview sources in §5.*

| Level | Must-have | Nice-to-have | Differentiator (gets the remote or senior offer) |
|---|---|---|---|
| **Mid** | One language done properly (TS or Java/Python); Playwright (or Selenium for Java shops); API testing (REST, auth, schema, negative cases); Git; CI (GitHub Actions/Jenkins); test design techniques; SQL basics | Docker; Cypress/Selenium migration; performance basics (k6/JMeter); mobile (Appium) | Contract testing (Pact); Testcontainers; testing async/event flows |
| **Senior** | Framework architecture (fixtures vs POM, data isolation, parallelism and sharding, reporting); flaky-test strategy; test strategy and risk-based planning; CI at scale; mentoring | Kubernetes test grids; observability (OTel traces in tests); security testing basics | **Backend-aware QE:** testing Kafka/RabbitMQ flows, idempotency, retries, DLQs, eventual consistency, DB isolation/race conditions; **AI-in-testing** (Playwright agents/MCP, evaluating LLM features); quality metrics with DORA language |

*Unchanged from the baseline. Nothing in this window's data moved the mid/senior boundary.*

---

## 3. Testing messaging and distributed systems: why it matters for a QE

- **For QE roles, messaging is still not a standard requirement.** Kafka is 2% of ROLIVA's QA listings and absent from the SDET top 15. That is what makes it a differentiator.
- **Where it shows up in QA hiring:** senior and fintech SDET loops ask "How would you test a Kafka consumer?".

### How it's tested in SDET interviews
*Unchanged from the baseline — no new interview-format survey was published in this window. Sources are prep sites, so treat the topic lists as secondary consensus, not employer data.*

In SDET loops, messaging and transaction topics arrive as "how would you test it": test strategy for an event-driven flow, contract tests, Testcontainers with a real broker, asserting eventual consistency without `sleep`, fault injection. Failure scenarios worth being able to test: "users get charged twice", "messages land in the DLQ after a schema change", "two requests withdraw from the same account", idempotency keys on POST.

**This maps directly onto the transaction and messaging focus of the learning notes.** Each lesson can follow "what breaks → how to reproduce and test it as a QE".

---

## 4. Salary ranges

**No new salary data this window.** The job alerts contained no stated ranges, and ITviec has not published a new survey. The figures below are the 2025–2026 survey, re-read on 28 Oct 2026 and unchanged.

### Vietnam local: ITviec 2025–2026 report, median **gross VND / month**
([ITviec report](https://itviec.com/report/vietnam-it-salary-and-recruitment-market), 1,839 respondents, surveyed May–Nov 2025)

| Role | <1 yr | 1–2 yr | 3–4 yr | 5–8 yr | >8 yr | Overall |
|---|---|---|---|---|---|---|
| Tester | 14.15M | 14.2M | 20.7M | 25.3M (≈$970) | 36.5M (≈$1,400) | 28.8M |
| QA-QC | – | 18M | 24.4M | 29.75M (≈$1,140) | 38.5M (≈$1,480) | 31.2M |

- **Posted ranges on live ITviec testing listings, 28 Oct:** manual-plus-automation tester "up to 28M net"; QC Manager "up to 55M". Consistent with the medians.

### Remote / international (Vietnam-based engineer, USD / month)

| Source | QA Automation | Notes |
|---|---|---|
| [Second Talent, Vietnam rates 2026](https://www.secondtalent.com/resources/true-cost-outsource-software-development-vietnam/) (vendor) | Mid **$2,500–3,900** · Senior **$3,900–5,600** · Lead $5,600–7,700 | Remote rates 40–100% above local; English is the biggest differentiator |
| [ADC France barometer, 2 Oct 2026](https://www.automationdatacamp.com/blog-post-barometre-competences-qa) | Median **€42,500** gross/yr; senior/lead **€50,000** (229 of 605 ads state pay) | French market, for comparison |
| Global reference ([SO 2026 comp](https://survey.stackoverflow.co/2026/work/data/compensation)) | QA/test median not published (<100 resp.) | Mostly US/EU respondents |

**Read (est.):** a senior QA automation engineer working remotely from Vietnam lands around **$4–5.5K/mo**.

---

## 5. Typical interview formats and common topics

**Market-wide (CoderPad 2026, about 650 respondents)** ([source](https://coderpad.io/survey-reports/coderpad-state-of-tech-hiring-2026/)) — *not re-surveyed this window; baseline figures*:
- **Exercises used:** algorithmic 43%, real-world scenarios 38%, system design 38%, pair programming 30%, code review 21%, debugging 19%.
- **What best predicts the job:** technical discussion (60% of recruiters) and live coding (60%). Take-homes score only 12%.
- **AI in interviews:** 34% ban it, **46% allow it** (broadly or with constraints), 20% decide case by case. When AI is allowed, the signals of real skill are **catching and fixing AI mistakes (66%)** and **explaining trade-offs (56%)**.
- **Top cheating concern:** agent-generated solutions (52%). This pushes companies toward live, multi-file, realistic tasks.

**SDET loop (typical, from prep guides):** recruiter screen → coding screen (Java/Python/TS: strings, maps, edge cases) → **framework design** (fixtures/POM, data isolation, parallel CI, reporting, retries and flake quarantine) → **API testing practical** (status codes, idempotency of methods, auth/JWT, schema and negative tests, contract tests) → test strategy (risk-based, test pyramid) → behavioural ([TechScreen 2026](https://techscreen.app/articles/sdet-qa-automation-interview-guide-2026), [SoftwareTestPilot](https://softwaretestpilot.com/blog/career-interview-prep/how-to-prepare-for-sdet-interview-at-faang)).
- Common questions: "Design a framework for X." · "How do you handle flaky tests?" · "Test a payment API." · "What's in your CI pipeline?" · "How would you test a Kafka consumer?" (senior/fintech).

**Vietnam specifics (est., from market structure):** outsourcing and service firms often run a shorter loop — tech interview, English check, sometimes a test. Foreign in-house centres and remote employers run fuller loops. **English is a gate** for remote roles.

---

## 6. Trends

**Manual QA is contracting, automation is holding, AI-QA is growing from a small base**
- **Mentorpiece Vacy Index** (via [Habr, 1 Oct 2026](https://habr.com/en/articles/1088696/)), share of tech companies with an open role of each type, Mar → Sep 2026: **manual QA 14.1% → 9.5% (−33%)**; **automation QA / senior QA 18.6% → 17.5% (−6%)**; **AI-QA / ML-evaluation 3.9% → 5.1% (+31%)**.
- **Read:** the absolute number of traditional QA roles lost is much larger than the AI-QA roles gained. AI-QA is a direction, not yet a lifeboat. The safe reading is **automation plus AI-tooling literacy**, not "pivot to AI QA".
- **Implication:** the manual-to-automation move is no longer a pay-rise move; it is the move that keeps the role.

**Playwright has crossed over**
- **ADC France barometer** ([2 Oct 2026](https://www.automationdatacamp.com/blog-post-barometre-competences-qa)), 405 "QA"-titled ads: **Playwright 24.2% > Selenium 21.7% > Cypress 15.1%**. In the broader 1,180 "test"-titled ads Playwright and Selenium are level (6.9% vs 7.1%), with Robot Framework at 5%.
- **Skillenai SDET:** Playwright 47.0%, Selenium 34.8%.
- **Implication:** teach Playwright as the default, and treat Selenium as "read and maintain legacy suites". A candidate who can only do Selenium is now the one being migrated.

**AI in testing: the tooling is native, and review discipline is the skill**
- **ADC AI-in-testing survey** ([5 Oct 2026](https://www.automationdatacamp.com/en/blog-post-ai-testing-trends-2026)): Playwright Test Agents (planner/generator/healer) since 1.56; CLI debugging and trace analysis for agents in 1.59; an **MCP server bundled in 1.62**; ISTQB CT-AI v2.0 (Apr 2026) and CT-GenAI v1.1; the EU AI Act high-risk deadline moved to **2 Dec 2027**.
- **20.7% of French QA ads mention AI**, and only 2.1% of ads say "junior" while 14.5% say senior/lead.
- Seven review checks before merging an AI-generated test: a real business assertion, accessible locators, isolated data, no secrets, never against production, limited scope, and the test must have been **seen failing once**.
- **Implication:** the QE value shifts to **reviewing** AI-written code and tests — oracles, contracts, determinism, and evaluating LLM features. That is a teachable checklist, not a vibe.

**What job ads actually require, by co-occurrence**
- **TestDino Test Automation Jobs Report 2026** ([source](https://testdino.com/blog/test-automation-jobs)): in 60%+ of ads, CI/CD, API testing, a programming language, Git and SQL appear together; 30–60% add Docker, Agile/Scrum, Cucumber/BDD, performance (JMeter, k6) and cloud; emerging mentions are AI/ML tooling, Kubernetes, Playwright MCP, security testing and observability.
- JetBrains 2025 CI/CD survey, cited there: **62% use GitHub Actions personally**, 41% organisationally.
- **Implication:** the "boring five" — CI/CD, API testing, one language, Git, SQL — are not optional and are cheap to prove in a portfolio.

**SDET career moves**
- Skillenai career flows: SDETs mostly move to **other SDET roles** (46 same-role moves). Only 2 observed SDET→Software Engineer moves vs 10 SE→SDET ([Skillenai SDET](https://skillenai.com/data/role/software-development-engineer-in-test-sdet)).

---

## 7. Recommended QA / automation skill priority list

*Time estimates assume about 6–8 hrs/week of study and are estimates. Order unchanged from the baseline; additions are marked **new**.*

### Strengthen the QE base and become a "backend-aware SDET" (months 0–3)
1. **API testing in depth** (Playwright `request` + REST Assured in Java): auth, schema, negative cases, idempotent methods. *(22% of SDET postings; it is the bridge skill.)*
2. **SQL + PostgreSQL transactions:** isolation levels, lost update and write skew, locking. Reproduce a race condition in a test. *(Core focus.)*
3. **Testcontainers** (Java and Go) with Postgres + Kafka + RabbitMQ in CI (GitHub Actions). *(CI/CD is 56% of SDET postings.)*
4. **Testing async/event flows:** asserting eventual consistency (polling and awaitility, not sleep), duplicate and out-of-order injection, DLQ assertions, contract tests (Pact). *(Differentiator.)*
5. **AI-in-testing literacy:** Playwright agents/MCP, and the seven review checks before merging an AI-generated test. *(20.7% of French QA ads mention AI.)*
6. **new** — **One cloud, and make it AWS.** Running and debugging tests against one real AWS deployment beats a tour of three consoles, and AWS is the only cloud both sources put first.

**Why this order (unchanged):** it starts with the skills most SDET postings ask for (API testing, CI), then adds the messaging and transaction testing that sets a QE apart, which is also the core focus of the learning notes.

---

## 8. Key resources (official docs and courses)

1. **Playwright Test Agents** (planner, generator, healer) and the MCP server: https://playwright.dev/docs/test-agents
2. **Playwright API testing**: https://playwright.dev/docs/api-testing
3. **Testcontainers guides** (Java/Go, Kafka/Postgres/RabbitMQ): https://testcontainers.com/guides/
4. **PostgreSQL: transaction isolation** (for reproducing race conditions in tests): https://www.postgresql.org/docs/current/transaction-iso.html

*(All URLs returned HTTP 200 on 28 Oct 2026.)*

---

## Caveats

- **This is a catch-up report.** It covers 17–28 Oct after the 23 Oct run failed, so the "week" is 11 days and the deltas against the baseline are 7-day comparisons from 21 Oct to 28 Oct.
- **Skillenai** measures posting mix, not hiring volume. The SDET sample is small (132).
- **ROLIVA** counts its own board (2,000 QA/test listings). It is the best QA-specific cloud count available, but it is one board, not the market.
- **JobRemotely** is US-weighted (566 of 687 listings) and its cloud subsample is 64 listings. Treat its percentages as directional.
- **The two cloud sources disagree on Azure versus GCP.** ROLIVA puts Azure 10% and GCP 4%; JobRemotely puts GCP 31 and Azure 23. Only the AWS-first finding is supported by both.
- **Jobpedia** counts its own 90-day sample (313 QA-engineer roles); its pay median covers only the 109 roles that state pay.
- **Mentorpiece** measures companies with an open role, not postings, so a single large employer can move the number.
- **AutomationDataCamp** covers the French market only. It is used for direction (Playwright over Selenium, AI mentions), not for Vietnam numbers.
- **ITviec counts** are a one-day snapshot (28 Oct 2026).
- **ITviec salaries** are self-reported medians from 2025 survey waves; no new salary data appeared in this window.
- **The VND→USD conversion** (≈26,000) is approximate.
- **Interview topic lists** come from prep sites (secondary). CoderPad is a vendor survey of about 650 people and was not re-run this window.
- **Job-alert data** is alert titles only, from a sample of 28 alerts. No personal data, recruiter names or contacts are included.
