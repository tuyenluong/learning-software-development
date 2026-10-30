# Job Market 2026: QE / SDET / QA Automation (baseline)

**Prepared by:** Jake (Research) for Tuyen Luong and Jacob (Teacher)  **Date:** 21 Oct 2026
**Purpose:** QA / QE automation market facts for Tuyen's QA learning plan. This report covers QA, SDET and test automation roles only; backend engineer findings are in [../backend-engineer/](../backend-engineer/).
**Builds on:** `software-tech-briefing-2026-10.md`, `jeremyluong-keyword-research.md`, `blog-post-briefs.md` (inbox aggregate).

> **How to read the numbers**
> - **Skillenai** = a job-posting index (90-day windows ending 14–20 Oct 2026). It shows how often a skill shows up in postings, not total hiring. Its SDET sample is small (140 postings).
> - **ITviec counts** = live listing counts I pulled from itviec.com tag pages on **21 Oct 2026**. They are a snapshot and move week to week.
> - **vitX** = a Vietnam hiring-pulse report built on ITviec/TopDev listings, 4 weeks to 15 Oct 2026. vitX is a staffing vendor.
> - **Second Talent** = a staffing vendor's rate cards. Its remote pay numbers are **vendor estimates**, not survey data.
> - Anything marked **(est.)** is my own estimate or conversion. VND→USD uses about **26,000 VND/USD**, which is approximate.
> - **Inbox (Jobs label)** = aggregate only. These are LinkedIn/Glassdoor alert digests, mostly job titles. No personal data is included, and nothing was sent or changed.

---

## 0. Bottom line (for Jacob)

1. **The QE market rewards an SDET who codes, not a tester.** CI/CD (57%), Python (51%), Playwright (47%), Java (36%) and API testing (21%) top SDET postings. AI shows up in job titles more and more.
2. **QA pay rises with automation and seniority.** In Vietnam, ITviec medians at 5–8 years are about **25.3M VND for Tester and 29.75M for QA-QC**, and automation and AI skills add roughly +20–40% over manual testing at the same seniority (secondary source). Remote QA automation rate cards for Vietnam-based engineers run about **$2,500–3,900/mo at mid and $3,900–5,600 at senior** (vendor estimates).
3. **Messaging and distributed systems are not in the SDET top 15, which makes them a differentiator.** A "backend-aware" QE who can test Kafka/RabbitMQ flows, retries, idempotency and DLQs stands out, especially for backend/integration QE roles at fintechs, which fits Tuyen's banking/fintech job alerts.
4. **SDET interviews are practical.** Framework design, API testing, flaky-test strategy and "how would you test it" questions on event-driven flows are the standard rounds, and more companies now allow AI in interviews.

---

## 1. Most-demanded skills, with frequency signals

**Global: Skillenai, SDET title, 140 postings, 90 days to 14 Oct 2026** ([source](https://skillenai.com/data/role/software-development-engineer-in-test-sdet))

| Skill | Share of postings |
|---|---|
| CI/CD | 57.1% |
| Python | 50.7% |
| Playwright | 47.1% |
| JavaScript | 36.4% |
| Selenium | 35.7% |
| Java | 35.7% |
| Jenkins | 32.9% |
| Cypress | 32.1% |
| TypeScript | 28.6% |
| Kubernetes | 22.9% |
| GitHub Actions | 22.1% |
| API testing | 21.4% |
| Docker | 20.0% |
| Performance testing | 20.0% |

- **Playwright:** 2,793 postings in 90 days, and it appears in 49.2% of QA Automation Engineer postings ([Skillenai](https://skillenai.com/data/skill/playwright)).
- **Open-job mentions:** Selenium 11,445, Playwright 7,208, API testing 6,917 ([QATestingJobs, Mar 2026](https://qatestingjobs.com/blog/what-testing-skills-should-you-learn-in-2026)).
- **Messaging, Kafka and distributed systems are *not* in the SDET top 15.** For a QE, they are a **differentiator**, especially for "backend/integration QE" roles at fintechs.

**Vietnam: ITviec live counts, 21 Oct 2026:** "tester" 58, "automation test" 36, "playwright" 12, "sdet" 11, "selenium" 10 ([itviec.com/it-jobs/tester](https://itviec.com/it-jobs/tester), [/automation-test](https://itviec.com/it-jobs/automation-test), [/playwright](https://itviec.com/it-jobs/playwright)).
- **vitX (3 Sep census):** QA and testing had **72 of 469** engineering roles (about 15%), and QA ads stay up a median of **31 days**, among the longest of any discipline ([vitX Oct 2026](https://www.vitx.global/reports/vitx-vietnam-it-hiring-pulse-2026-10.pdf)).

**Inbox (Jobs label, aggregate):**
- About 50% of alerts are QA/automation roles. About 40% of QA titles are "Senior".
- Titles are converging on **SDET / Software Engineer in Test / Quality Engineer**.
- At least 8 QA titles name AI ("AI-Augmented Testing (Playwright, TypeScript)", "Software Engineer in Test (Agentic AI)", "QA Automation (MLOps)").
- About 10 roles are **banking/fintech**.

---

## 2. Must-have vs nice-to-have vs differentiator (mid → senior)

*This synthesis is my own, based on the frequencies above and the interview sources in §5.*

| Level | Must-have | Nice-to-have | Differentiator (gets the remote or senior offer) |
|---|---|---|---|
| **Mid** | One language done properly (TS or Java/Python); Playwright (or Selenium for Java shops); API testing (REST, auth, schema, negative cases); Git; CI (GitHub Actions/Jenkins); test design techniques; SQL basics | Docker; Cypress/Selenium migration; performance basics (k6/JMeter); mobile (Appium) | Contract testing (Pact); Testcontainers; testing async/event flows |
| **Senior** | Framework architecture (fixtures vs POM, data isolation, parallelism and sharding, reporting); flaky-test strategy; test strategy and risk-based planning; CI at scale; mentoring | Kubernetes test grids; observability (OTel traces in tests); security testing basics | **Backend-aware QE:** testing Kafka/RabbitMQ flows, idempotency, retries, DLQs, eventual consistency, DB isolation/race conditions; **AI-in-testing** (Playwright agents/MCP, evaluating LLM features); quality metrics with DORA language |

---

## 3. Testing messaging and distributed systems: why it matters for a QE

- **Messaging is not a standard SDET requirement.** Kafka, messaging and distributed systems are absent from the SDET top 15 above, which is exactly why they are a differentiator for a QE.
- **Where it shows up in QA hiring:** senior and fintech SDET loops ask "How would you test a Kafka consumer?", and backend/integration QE titles appear in Tuyen's alerts.

### How it's tested in SDET interviews
*Sources: interview-prep sites. The topic lists are secondary-source consensus, not employer data.*

In SDET loops, messaging and transaction topics arrive as **"how would you test it"**:
- test strategy for an event-driven flow
- contract tests between services
- Testcontainers with a real broker
- asserting eventual consistency without `sleep`
- fault injection

Typical failure scenarios to be ready to test: "users get charged twice", "messages end up in the DLQ after a schema change", "two requests withdraw from the same account at once", and idempotency of POST requests.

**This maps directly onto Jacob's core focus.** Each lesson can follow "what breaks → how to reproduce and test it as a QE".

---

## 4. Salary ranges

### Vietnam local: ITviec 2025–2026 report, median **gross VND / month**
([ITviec report](https://itviec.com/report/vietnam-it-salary-and-recruitment-market), 1,839 respondents, surveyed May–Nov 2025)

| Role | <1 yr | 1–2 yr | 3–4 yr | 5–8 yr | >8 yr | Overall |
|---|---|---|---|---|---|---|
| Tester | 14.15M | 14.2M | 20.7M | 25.3M (≈$970) | 36.5M (≈$1,400) | 28.8M |
| QA-QC | – | 18M | 24.4M | 29.75M (≈$1,140) | 38.5M (≈$1,480) | 31.2M |

- **Inbox anecdote (posted range in an alert title):** a QA Automation role "up to $2.1K/month", consistent with the medians above.
- An industry blog citing ITviec says automation and AI skills add about +20–40% over manual testing at the same seniority ([itlearn.vn](https://itlearn.vn/blog/luong-tester)). This is secondary and directional.

### Remote / international (Vietnam-based engineer, USD / month)
| Source | QA Automation | Notes |
|---|---|---|
| [Second Talent, Vietnam rates 2026](https://www.secondtalent.com/resources/true-cost-outsource-software-development-vietnam/) (vendor) | Mid **$2,500–3,900** · Senior **$3,900–5,600** · Lead $5,600–7,700 | "remote rates are 40–100% higher than local salaries"; English is the biggest differentiator |
| Global reference ([SO 2026 comp](https://survey.stackoverflow.co/2026/work/data/compensation)) | QA/test median not published (<100 resp.) | Mostly US/EU respondents |
| Freelance QA consulting (from keyword report) | Audits **$1,000–2,400**, migrations from **€4,500**, retainers **~$1,800/mo** | Solo consultants' public pricing |

**Read (est.):** a senior QA automation engineer working remotely from Vietnam lands around **$4–5.5K/mo**.

---

## 5. Typical interview formats and common topics

**Market-wide (CoderPad 2026, about 650 respondents)** ([source](https://coderpad.io/survey-reports/coderpad-state-of-tech-hiring-2026/)):
- **Exercises used:** algorithmic 43%, real-world scenarios 38%, system design 38%, pair programming 30%, code review 21%, debugging 19%.
- **What best predicts the job:** technical discussion (60% of recruiters) and live coding (60%). Take-homes score only 12%.
- **AI in interviews:** 34% ban it, **46% allow it** (broadly or with constraints), 20% decide case by case. When AI is allowed, the signals of real skill are **catching and fixing AI mistakes (66%)** and **explaining trade-offs (56%)**.
- **Top cheating concern:** agent-generated solutions (52%). This pushes companies toward live, multi-file, realistic tasks.

**SDET loop (typical, from prep guides):** recruiter screen → coding screen (Java/Python/TS: strings, maps, edge cases) → **framework design** (fixtures/POM, data isolation, parallel CI, reporting, retries and flake quarantine) → **API testing practical** (status codes, idempotency of methods, auth/JWT, schema and negative tests, contract tests) → test strategy (risk-based, test pyramid) → behavioral ([TechScreen 2026](https://techscreen.app/articles/sdet-qa-automation-interview-guide-2026), [SoftwareTestPilot](https://softwaretestpilot.com/blog/career-interview-prep/how-to-prepare-for-sdet-interview-at-faang)).
- Common questions:
  - "Design a framework for X."
  - "How do you handle flaky tests?"
  - "Test a payment API."
  - "What's in your CI pipeline?"
  - "How would you test a Kafka consumer?" (senior/fintech)

**Vietnam specifics (est., from market structure):** outsourcing and service firms (about 36 international IT services firms per vitX) often run a shorter loop: tech interview + English check + sometimes a test. Foreign in-house centres (57% senior roles) and remote employers run fuller loops with system design. **English is a gate** for remote roles.

---

## 6. Trends

**AI in testing**
- **World Quality Report 2025-26:** 43% of organisations are experimenting with GenAI in QA, but only **15% have scaled it** enterprise-wide. **GenAI is the top-ranked skill for quality engineers (63%)**, ahead of core QE skills (60%). Synthetic test data use rose from 14% to 25% ([Capgemini WQR](https://www.capgemini.com/insights/research-library/world-quality-report-2025-26/)). OpenText's press release also reports an average 19% productivity gain, with a third seeing minimal gains; I couldn't re-verify this because the fetch was blocked ([OpenText](https://www.opentext.com/about/press-releases/world-quality-report-2025-ai-adoption-surges-in-quality-engineering-but-enterprise-level-scaling-remains-elusive)).
- **SO 2026:** 58.1% of AI users use it for writing or improving tests. 73% use coding agents daily, but only 48% trust output that isn't easy to check ([SO 2026 AI](https://survey.stackoverflow.co/2026/ai)).
- **Framework-native agents are now free:** Playwright Test Agents (planner, generator, healer) and MCP, Cypress `cy.prompt`, WebdriverIO v10 (see `software-tech-briefing-2026-10.md`).
- **Vietnam:** 13.7% of ITviec IT roles ask for AI, up from 11.3% in Aug ([vitX](https://www.vitx.global/reports/vitx-vietnam-it-hiring-pulse-2026-10.pdf)). The inbox shows at least 8 QA titles naming AI.
- **Implication:** the QE value shifts to **verifying AI-written code and tests**: oracles, contracts, determinism, and evaluating LLM features.

**SDET career moves**
- Skillenai career flows show SDETs mostly move to **other SDET roles** (46 same-role moves), with only 2 observed SDET→Software Engineer moves vs 10 SE→SDET ([Skillenai SDET](https://skillenai.com/data/role/software-development-engineer-in-test-sdet)).
- A QA title that already appears in Tuyen's alerts is **"backend-focused SDET / Quality Engineer – Core Services"**.

---

## 7. Recommended QA / automation skill priority list

*Time estimates assume about 6–8 hrs/week and are my estimates. Jacob should confirm Tuyen's actual weekly time.*

### Strengthen the QE base and become a "backend-aware SDET" (months 0–3)
1. **API testing in depth** (Playwright `request` + REST Assured in Java): auth, schema, negative cases, idempotent methods. *(21% of SDET postings; it's the bridge skill.)*
2. **SQL + PostgreSQL transactions:** isolation levels, lost update and write skew, locking. Reproduce a race condition in a test. *(Core focus.)*
3. **Testcontainers** (Java and Go) with Postgres + Kafka + RabbitMQ in CI (GitHub Actions). *(CI/CD is 57% of SDET postings.)*
4. **Testing async/event flows:** asserting eventual consistency (polling and awaitility, not sleep), duplicate and out-of-order injection, DLQ assertions, contract tests (Pact). *(Differentiator.)*
5. **AI-in-testing literacy:** Playwright agents/MCP, reviewing AI-generated tests. *(AI titles are rising.)*

**Why this order:** it starts with the skills most SDET postings ask for (API testing, CI), then adds the messaging and transaction testing that sets a QE apart, which is also Jacob's core teaching focus.

---

## 8. Key resources (official docs and courses)

1. **Playwright API testing**: https://playwright.dev/docs/api-testing
2. **Testcontainers guides** (Java/Go, Kafka/Postgres/RabbitMQ): https://testcontainers.com/guides/
3. **PostgreSQL: transaction isolation** (for reproducing race conditions in tests): https://www.postgresql.org/docs/current/transaction-iso.html

*(All URLs returned HTTP 200 on 21 Oct 2026.)*

---

## Caveats
- **Skillenai** measures posting mix, not hiring volume. The SDET sample is small (140).
- **ITviec counts** are a one-day snapshot.
- **Remote pay numbers** come from staffing vendors (Second Talent). They are directional, not survey-grade.
- **ITviec salaries** are self-reported medians from 2025 survey waves.
- **The VND→USD conversion** (≈26,000) is approximate.
- **Interview topic lists** come from prep sites (secondary). CoderPad is a vendor survey of about 650 people.
- **Inbox data** is alert titles only. No personal data, recruiter names or contacts are included. No email was sent, drafted or changed.
