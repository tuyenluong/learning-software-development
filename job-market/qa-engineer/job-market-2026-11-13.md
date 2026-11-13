# Job Market 2026-11-13: QE / SDET / QA Automation

**Date:** 13 Nov 2026
**Purpose:** QA / QE automation market facts. This report covers QA, SDET and test automation roles only.
**Coverage:** weekly report. Window covered: **6 – 13 Nov 2026**. The previous report's window ended on 6 Nov, so **6 Nov overlaps**; only **7 – 13 Nov** is new in the job-alert sample.
**Builds on:** [job-market-2026-11-06.md](job-market-2026-11-06.md) (previous weekly report) and [qe-job-market-2026.md](qe-job-market-2026.md) (baseline, 21 Oct 2026).

> **How to read the numbers**
> - **Skillenai** = a job-posting index (90-day rolling window). Its SDET page was **not refreshed this week** (still 90 days ending 5 Nov 2026, 105 postings), so its figures are unchanged from the previous report.
> - **ITviec counts** = live listing counts pulled from itviec.com tag pages on **13 Nov 2026**. Snapshot only.
> - **ROLIVA** = a job board that reads employers' careers pages. Counts are its 2,000 most recently confirmed QA and test engineer listings on 13 Nov 2026, so percentages describe *that board*, not the whole market. A mention is not necessarily a requirement.
> - **Jobpedia.AI** = a posting aggregator that publishes per-role skill shares over 90-day windows (here, 90 days to 12 Nov 2026).
> - **Codecaf** = a one-time count of 552 QA / SDET / automation postings collected 30–31 Oct 2026 (annual edition; unchanged).
> - **AssertHired** = a multi-country board of QA postings (here, last seen 15 Sep – 13 Nov 2026). Framework, language and tool shares are over the subset that name a tool in that table, not every posting.
> - **JobRemotely**, **AutomationDataCamp (ADC)**, **Mentorpiece** and **CoderPad** were not re-published this week; their figures are carried over from earlier reports and marked *carried over*.
> - Anything marked **(est.)** is an estimate or conversion made for this report. VND→USD uses about **26,000 VND/USD**, which is approximate.
> - **Job-alert sample** = aggregate counts from a sample of job-alert emails (LinkedIn digests, one Glassdoor digest, two freelance-board digests), mostly job titles. No personal data, recruiter names or contacts are included.

---

## Top skills at a glance (13 Nov 2026)

**QE / automation — learn these first**
1. **CI/CD** — required in **41%** of QA-engineer roles ([Jobpedia](https://jobpedia.ai/roles/qa-engineer), 178 of 437); 59.0% of SDET postings ([Skillenai SDET](https://skillenai.com/data/role/software-development-engineer-in-test-sdet), unchanged); named in 60% of Codecaf's 552 postings.
2. **Python**, then **Java** — Python is 48% vs Java 45% of AssertHired postings that name a language ([AssertHired](https://www.asserthired.com/qa-jobs/market)); Python 24% of ROLIVA's 2,000 QA listings; Python 53.3% / Java 41.0% of SDET postings.
3. **Playwright, with Selenium close behind** — AssertHired framework-named subset: Playwright **66%** vs Selenium **59%** (was 64% vs 60%); Skillenai SDET 46.7% vs 34.3%; Codecaf 46% vs 47%.
4. **API testing** — required in 25% of QA-engineer roles (Jobpedia, 110 of 437); 68% of Codecaf postings. Postman (59%) and REST Assured (55%) lead the AssertHired API-tool subset.
5. **SQL** — required in 20% of QA-engineer roles (Jobpedia, 86 of 437); 12% of ROLIVA's QA listings.

---

## What changed this week (6 Nov → 13 Nov 2026)

**Job-alert sample: 21 alerts dated 6 – 13 Nov**, of which **20 are new since the previous report** (7 – 13 Nov; 6 Nov overlaps). Digests came from LinkedIn job alerts, one Glassdoor digest and two freelance-board digests. None came from a named recruiter.

**The changes worth acting on**

| # | Change | 6 Nov | 13 Nov | Read |
|---|---|---|---|---|
| 1 | **"Spec-driven testing" reached a local job title** | Spec-driven review was a research result (arXiv 2608.17177) and an "AI Quality Engineer" title | LinkedIn digest card: **Senior Test Engineer (AI-Augmented & Spec-Driven Testing)** at KMS Technology, HCMC; also **AI Platform – (Senior) QA/QC** at Galaxy FinX | Reviewing AI-written tests against a written spec is moving from paper to job description in HCMC. |
| 2 | **Playwright 1.65 changed API-request behaviour; the Python port shipped on 9 Nov** | 1.65 noted for exclusive lock and failure reporters | Cookie matching now follows **RFC 6265** for `browserContext.cookies()` / `apiRequestContext.cookies()`; string `params` are **appended** to an existing URL query instead of replacing it ([Node 1.65.0](https://github.com/microsoft/playwright/releases/tag/v1.65.0), [Python 1.65.0](https://github.com/microsoft/playwright-python/releases/tag/v1.65.0)) | API tests that set cookies or build query strings can change behaviour on upgrade. New note: [Playwright 1.65 API request changes: cookies and query params](../../learning-material/qa-automation/Playwright%201.65%20API%20request%20changes%20-%20cookies%20and%20query%20params.md). |
| 3 | **Azure back ahead of AWS on ROLIVA; employer base grew** | AWS 9% (184), Azure 9% (170); 276 employers | **Azure 9% (183), AWS 7% (140)**; **347** employers | The cloud lead keeps flipping on one board as its employer mix changes. One cloud well is still enough. |
| 4 | **Cypress 16.3 targets AI agents running the tool** | Cypress not in the release log | **Cypress 16.3.0** (10 Nov): `cypress open` skips the welcome screen and prints config errors to the terminal so an agent can read them ([release](https://www.cypress.io/releases/16-3-0)) | All three big browser tools now ship agent-facing features (Playwright `"ai"` aria snapshots, Cypress 16.3, Selenium's MCP server work in nightly builds). |

**Jobpedia QA-engineer roles, 6 Nov → 13 Nov** ([source](https://jobpedia.ai/roles/qa-engineer); 90-day windows):

| Signal | 6 Nov | 13 Nov |
|---|---|---|
| Roles counted | 402 | **437** |
| Employers | 330 | **355** |
| CI/CD required | 40% | **41%** |
| Test automation required | 37% | **38%** |
| Python required | 37% | **36%** |
| API testing required | 25% | **25%** |
| SQL required | 20% | **20%** |
| Remote | 79% | **81%** |
| Median stated pay | $120k | **$120.1k** (145 of 437 state pay) |

*Skill order is unchanged; the sample grew by 35 roles.*

**ITviec Vietnam, 6 Nov → 13 Nov 2026** (live listing counts, same tag pages):

| Tag | 6 Nov | 13 Nov |
|---|---|---|
| tester | 57 | **57** |
| automation test | 40 | **40** |
| playwright | 11 | **12** |
| sdet | 11 | **10** |

([tester](https://itviec.com/it-jobs/tester), [automation-test](https://itviec.com/it-jobs/automation-test), [playwright](https://itviec.com/it-jobs/playwright), [sdet](https://itviec.com/it-jobs/sdet))

**Job-alert sample (aggregate, 6 – 13 Nov):**
- **21 alerts in 8 days**, almost all with Ho Chi Minh City locations.
- **7 of 21 subjects (~33%)** were testing-titled (QA / Quality Assurance / Automation Tester), about the same as the previous report's ~32%. Two "Automation Engineer III" alerts were industrial automation and are excluded. Most of the rest were backend or Java developer alerts and are out of scope here.
- Recurring QA titles in subjects and digest cards: Senior QA Automation Engineer, QA Automation Engineer, Senior QA Engineer (Automation), Remote Senior QA Engineer (Automation & Manual), QC Engineer (Automation), Senior QC Engineer (Automation), Automation Tester, Junior Test Automation Engineer, QA Lead/Manager (Automation & Manual), QA Lead (Performance & Data Testing), Test Developer, Senior Quality Engineer.
- **AI in titles:** Senior Test Engineer (AI-Augmented & Spec-Driven Testing); AI Platform – (Senior) QA/QC.
- **One remote title** (Senior QA Engineer, Automation & Manual, Vietnam-remote). One mobile-app automation role (QA Automation Engineer, mobile app setup).
- **No alert stated pay** this window. The previous report had one ("up to 1,250 USD net").

---

## 0. Bottom line

1. **Same skill core.** CI/CD (41% of Jobpedia QA roles), Python, Playwright, API testing and SQL. Nothing moved the order this week.
2. **Playwright's lead in the framework-named subset widened slightly** (AssertHired 66% vs 59%), while Codecaf's one-off sample stays a near-tie. Learn one deeply and expect to meet the other.
3. **Spec-driven, AI-augmented testing is now a local job title**, not just research.
4. **Upgrading Playwright to 1.65 can change API tests**: RFC 6265 cookie matching and appended query params.
5. **Pay data is unchanged.** No stated pay in this window's alerts; Jobpedia median **$120.1k/yr**; ITviec survey medians as before.

---

## 1. Most-demanded skills, with frequency signals

### A. QE / Automation / SDET

**Global: Skillenai, SDET title, 105 postings, 90 days to 5 Nov 2026** ([source](https://skillenai.com/data/role/software-development-engineer-in-test-sdet)) — *not refreshed this week; same as the previous report.*

| Skill | Share of postings |
|---|---|
| CI/CD | 59.0% |
| Python | 53.3% |
| Playwright | 46.7% |
| Java | 41.0% |
| Test automation | 38.1% |
| JavaScript | 36.2% |
| Selenium | 34.3% |
| Jenkins | 31.4% |
| Cypress | 30.5% |
| TypeScript | 28.6% |
| Kubernetes | 23.8% |
| API testing | 23.8% |
| GitHub Actions | 22.9% |
| Performance testing | 22.9% |
| Docker | 21.9% |

- **Messaging, Kafka and distributed systems are still absent from the SDET top 15.** For a QE they remain a **differentiator**, not a requirement.

**QA-engineer roles across all levels: Jobpedia.AI, 437 roles, 355 employers, 90 days to 12 Nov 2026** ([source](https://jobpedia.ai/roles/qa-engineer)) — required skills:

| Skill | Share | Skill | Share |
|---|---|---|---|
| CI/CD | 41% (178) | Git | 21% (92) |
| Test automation | 38% (164) | Agile | 21% (91) |
| Python | 36% (158) | JavaScript | 21% (90) |
| API testing | 25% (110) | SQL | 20% (86) |
| TypeScript | 21% (93) | Java | 19% (82) |

- Preferred skills: CI/CD 14%, test automation 11%, Jira 9%, Agile 8%, Docker 8%, AWS 8%, Python 8%, **AI 7%**, Git 6%, Kubernetes 6%.
- **81% remote** (was 79%). 46% of roles stating years ask 5–7 years; 60% ask at least 5.
- 19% require a degree; another 22% accept experience instead; 56% don't mention one.

**AssertHired, 7,271 QA postings across 18 countries, last seen 15 Sep – 13 Nov 2026** ([source](https://www.asserthired.com/qa-jobs/market)):

| Table (subset that names a tool) | Result |
|---|---|
| Browser frameworks (1,203 postings) | Playwright **66%**, Selenium **59%**, Cypress 14%, WebdriverIO 1.7% |
| Languages (1,480 postings) | Python **48%**, Java **45%**, JavaScript 17%, TypeScript 17%, C# 14% |
| API tools (268 postings) | Postman 59%, REST Assured 55% |
| Performance tools (74 postings) | JMeter 89%, Gatling 23%, k6 11% |
| Seniority (all 7,271) | Entry 3.1%, Mid 64%, Senior 24%, Lead/manager 8.8%; remote 4.0% |

Country split for frameworks: UK Playwright 78% / Selenium 33%; US 70% / 65%; India 68% / 51%; Canada Selenium leads 71% / Playwright 44%. In the US, REST Assured (74%) leads Postman (43%) in the API-tool subset.

**Codecaf, 552 QA / automation / SDET postings, collected 30–31 Oct 2026** ([source](https://codecaf.com/research/qa-hiring-statistics/)) — *annual edition, unchanged:* Selenium 47%, Playwright 46%, Cypress 33%; Python 43%, JavaScript 37%, Java 36%; API testing 68%; CI/CD or delivery tooling 60%; Postman 29%, RestAssured 19%; JMeter 16%, Appium 15%; ISTQB 9%; median stated experience minimum 4 years.

### B. Cloud platforms for QA roles

| Cloud | ROLIVA 6 Nov | ROLIVA 13 Nov | JobRemotely (remote listings, 1 Oct, *carried over*) | Codecaf (30–31 Oct) |
|---|---|---|---|---|
| **AWS** | 9% (184) | **7% (140)** | **53** of 687 (53 of the 64 that name a cloud) | 21% (117/552) |
| **Azure** | 9% (170) | **9% (183)** | 23 | 12% (67/552) |
| **GCP** | 3% (69) | **3% (50)** | 31 | 8% (44/552) |

Sources: [ROLIVA QA-engineer skill insights](https://rolivajobs.com/insights/skills/qa-engineer) (2,000 of 3,631 open QA and test engineer listings, 347 employers, 57 countries, as of 13 Nov 2026); [JobRemotely cloud-jobs analysis](https://jobremotely.io/blog/cloud-jobs-aws-azure-gcp); [Codecaf](https://codecaf.com/research/qa-hiring-statistics/).

**Read:**
- **On ROLIVA, Azure leads AWS again** (183 vs 140), after a tie last week. The employer count jumped from 276 to 347, which alone can shift these shares. Codecaf's broader sample still puts AWS first among postings that name a cloud.
- What every source still agrees on: **GCP is third**, and cloud is mentioned in a minority of QA listings. One cloud well is enough.

Other ROLIVA signals (13 Nov): Python **24% (475)**, Agile 16%, Jira 12%, Java 12%, SQL 12%, Excel 9%, JavaScript 9%, Scrum 7%, TypeScript 6%, Docker 5%, Kubernetes 4%, **LLM 2% (45)**, **Kafka 2% (31)**. Vietnam is **19 of the 2,000 listings (0.9%)**. Against its October snapshot, Agile (+3 pts), Jira (+2) and Excel (+2) rose; AWS (−2) fell.

---

## 2. Must-have vs nice-to-have vs differentiator (mid → senior)

*Largely unchanged. Additions this week are marked.*

| Level | Must-have | Nice-to-have | Differentiator |
|---|---|---|---|
| Mid | One browser framework deeply (Playwright *or* Selenium), API testing, CI/CD basics, one language (Python or Java), Git, SQL | Cypress familiarity, Docker, JMeter/k6, cloud basics, Postman *and* REST Assured | Contract tests, Testcontainers, flaky-test control in CI, knowing how HTTP cookies scope by domain and path *(new)* |
| Senior | Framework design, pipeline ownership, mentoring, risk-based strategy | Kubernetes, performance ownership, multi-cloud | Messaging/async testing, spec-driven review of AI-generated tests *(now in a local title)*, exclusive/parallel-safe suite design |

AssertHired's seniority mix (64% mid, 24% senior) and Jobpedia's experience bar (60% of roles stating years ask 5+) both say most advertised roles are mid-level and up.

---

## 3. Testing messaging and distributed systems: why it matters for a QE

- **Messaging is still not a standard QE requirement.** Kafka is 2% (31) of ROLIVA's QA listings and absent from the SDET top 15. That keeps it a differentiator.
- **New this week, on the API side:** session and idempotency tests often rely on cookies. Playwright 1.65 now matches cookies by RFC 6265 domain and path rules, so a test that relied on a `Path=/api` cookie leaking to `/apiv2`, or a host-only cookie reaching a subdomain, will now see the request go out without it. That is closer to what a real browser does, and a better base for duplicate-request and session tests. See [Playwright 1.65 API request changes: cookies and query params](../../learning-material/qa-automation/Playwright%201.65%20API%20request%20changes%20-%20cookies%20and%20query%20params.md).
- Interview framing is unchanged (*carried over*): "How would you test a Kafka consumer?", duplicate charges, DLQ after a schema change, idempotency keys on POST.

---

## 4. Salary ranges

**No new ITviec salary survey this window, and no alert stated pay.** The survey figures below are unchanged.

### Vietnam local: ITviec 2025–2026 report, median **gross VND / month**
([ITviec report](https://itviec.com/report/vietnam-it-salary-and-recruitment-market), 1,839 respondents, surveyed May–Nov 2025)

| Role | <1 yr | 1–2 yr | 3–4 yr | 5–8 yr | >8 yr | Overall |
|---|---|---|---|---|---|---|
| Tester | 14.15M | 14.2M | 20.7M | 25.3M (≈$970) | 36.5M (≈$1,400) | 28.8M |
| QA-QC | – | 18M | 24.4M | 29.75M (≈$1,140) | 38.5M (≈$1,480) | 31.2M |

- Previous window's single stated alert (*carried over*): AI Quality Engineer "up to 1,250 USD net".

### Remote / international
- **Jobpedia** (global QA-engineer roles that state pay): median **$120.1k/yr** (145 of 437 roles).
- Vendor and France figures (*carried over*): Second Talent senior QA automation remote from Vietnam **$3,900–5,600/mo**; ADC France median **€42,500/yr**.
- InterviewStack SDET board (*carried over* from Jul 2026 sample of 1,027 listings): median US base **$130,000** across 181 postings with US salary disclosed.
- **Read (est., unchanged):** a senior QA automation engineer working remotely from Vietnam lands around **$4–5.5K/mo**.

---

## 5. Typical interview formats and common topics

*Carried over; no new interview-format survey was published this window.* CoderPad 2026 (about 650 respondents): technical discussion and live coding best predict the job (60% each); 46% of companies allow AI in interviews in some form, and when they do, catching and fixing AI mistakes (66%) is the top signal ([source](https://coderpad.io/survey-reports/coderpad-state-of-tech-hiring-2026/)). The SDET loop (coding screen → framework design → API testing practical → test strategy → behavioural) is unchanged. A likely new API-practical question after this week's releases: "Why did this cookie not get sent?" (domain and path scoping).

---

## 6. Trends

**Playwright 1.65 API-request changes (Node 5 Nov, Python 9 Nov 2026)**
- Cookie matching follows RFC 6265: with a URL, `cookies()` no longer returns host-only cookies for subdomains or `Path=/api` cookies for `/apiv2`, and a `Path=/foo/` cookie does not match `/foo`.
- `params` values (string, and `URLSearchParams` in Node) are appended to a query the URL already has, instead of replacing it.
- `APIRequestContext` sends a nameless cookie as `Cookie: x` and stores `Set-Cookie: token` as a cookie without a name.
- Python: proxy credentials now answer only proxy challenges; use `http_credentials` for site auth. The Python client is now a line-by-line port of the Node client. ([Node release](https://github.com/microsoft/playwright/releases/tag/v1.65.0), [Python release](https://github.com/microsoft/playwright-python/releases/tag/v1.65.0))
- **Implication:** read the cookie and query assertions in API suites before upgrading; a red test after the upgrade may be the old behaviour hiding a real scoping bug.

**Agent-facing features in all three browser tools**
- Cypress 16.3.0 (10 Nov): agent-friendly `cypress open` (no welcome screen, config errors to terminal); every registered Node event handler now runs in order, not only the last ([release](https://www.cypress.io/releases/16-3-0)).
- Playwright Python 1.65: `locator.normalize()` converts to Python code, for turning an element an agent picked from an `"ai"` aria snapshot into test code.
- Selenium 4.52 (29 Oct) is the latest stable release (TLS validation in Selenium Manager, faster BiDi in Python and Ruby) ([blog](https://www.selenium.dev/blog/2026/selenium-4-52-released/)); its nightly builds added an MCP server for coding agents, now moved to its own repository ([nightly](https://github.com/SeleniumHQ/selenium/releases/tag/nightly)). Pre-release only.

**Playwright vs Selenium: same story, slightly wider in one sample**
- AssertHired framework-named: Playwright 66% vs Selenium 59% (was 64% vs 60%); leads in the US, India, Poland and the UK; Selenium leads in Canada and South Africa.
- Skillenai SDET-title (unchanged): Playwright 46.7% vs Selenium 34.3%.
- Codecaf mixed QA (unchanged): Selenium 47% vs Playwright 46%.
- **Implication:** pick one framework deeply; treat the other as transferable skill.

**AI-in-testing in local titles**
- New this week: Senior Test Engineer (AI-Augmented & Spec-Driven Testing); AI Platform – (Senior) QA/QC. Last week: AI Quality Engineer with a stated band.
- Preferred-skill share for AI on Jobpedia stays **7%** (30 of 437), and LLM is 2% of ROLIVA QA listings: a plus, not a gate.

**Carried over from earlier reports:** manual QA contracting decline (Mentorpiece), Playwright ahead of Selenium in French QA ads, and the "boring five" (CI/CD, API testing, one language, Git, SQL) co-occurring in 60%+ of automation ads (TestDino).

**SDET career moves** ([Skillenai SDET](https://skillenai.com/data/role/software-development-engineer-in-test-sdet), unchanged): 43 same-role moves; **QA Automation Engineer → SDET 13 moves**, Software Engineer → SDET 9.

---

## 7. Recommended QA / automation skill priority list

*Order unchanged; changes are marked.*

1. **API testing in depth** (Playwright `request` + REST Assured, Postman for exploration): auth, schema, negative cases, idempotent methods, **cookie domain/path scoping and query building** *(new for 1.65)*. *(25% of Jobpedia QA roles; 68% of Codecaf.)*
2. **SQL + PostgreSQL transactions:** isolation levels, lost update and write skew, locking. Reproduce a race condition in a test.
3. **Testcontainers** (Java and Go) with Postgres + Kafka + RabbitMQ in CI. *(CI/CD is required in 41% of Jobpedia QA roles.)*
4. **Testing async/event flows:** eventual consistency without sleep, duplicates, out-of-order, DLQ, contract tests (Pact).
5. **AI-in-testing literacy, including spec-driven review** *(now in a local job title)*: every assertion in an AI-written test should trace to a requirement.
6. **Parallel-safe suites:** unique test data per test; named Playwright locks for shared resources; `-exclusive-` only for true globals.
7. **One cloud, well.** AWS or Azure are both defensible; the lead flips between boards and weeks.

---

## 8. Key resources (official docs and primary sources)

1. **Playwright 1.65.0 release notes (Node)**: https://github.com/microsoft/playwright/releases/tag/v1.65.0
2. **Playwright for Python 1.65.0 release notes**: https://github.com/microsoft/playwright-python/releases/tag/v1.65.0
3. **Playwright API testing**: https://playwright.dev/docs/api-testing
4. **RFC 6265: HTTP State Management (cookies)**: https://www.rfc-editor.org/rfc/rfc6265
5. **Cypress 16.3.0 release notes**: https://www.cypress.io/releases/16-3-0
6. **AssertHired QA job market (by country)**: https://www.asserthired.com/qa-jobs/market
7. **Jobpedia QA-engineer roles**: https://jobpedia.ai/roles/qa-engineer
8. **ROLIVA QA-engineer skill insights**: https://rolivajobs.com/insights/skills/qa-engineer

*(URLs checked for HTTP 200 on 13 Nov 2026.)*

---

## Caveats

- **Window overlap:** this report's alert window (6 – 13 Nov) overlaps the previous one on 6 Nov. Only alerts from 7 – 13 Nov are new.
- **Skillenai** did not refresh its SDET page this week; its figures are repeated, not re-measured.
- **ROLIVA** counts its own board and caps at 2,000 listings per role; its employer count rose from 276 to 347 this week, which alone can shift percentages, including the AWS/Azure order.
- **AssertHired** shares are over the subset that name a tool in each table (28% of its tracked postings carry any tool tag), so they are not comparable one-to-one with Skillenai or Codecaf percentages of *all* postings. Its performance-tool subset is small (74 postings).
- **Codecaf** is a two-day snapshot (30–31 Oct), English-language and ATS-heavy, refreshed annually.
- **JobRemotely, ADC, Mentorpiece, TestDino, InterviewStack and CoderPad** figures are carried over, not re-checked this week.
- **Jobpedia's** pay median covers only the 145 roles that state pay.
- **ITviec counts** are a one-day snapshot (13 Nov 2026). **ITviec salaries** are self-reported 2025 survey medians.
- **The VND→USD conversion** (≈26,000) is approximate.
- **Job-alert data** is alert titles and listed job cards only, from a sample of 21 alerts. Industrial "Automation Engineer" roles and backend/developer alerts are excluded from the testing-title count. No personal data, recruiter names or contacts are included.
