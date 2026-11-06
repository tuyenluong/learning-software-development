# Job Market 2026-11-06: QE / SDET / QA Automation

**Date:** 6 Nov 2026
**Purpose:** QA / QE automation market facts. This report covers QA, SDET and test automation roles only.
**Coverage:** weekly report. Window covered: **30 Oct – 6 Nov 2026**. The previous report's window ended on 30 Oct, so **30 Oct overlaps**; only **31 Oct – 6 Nov** is new in the job-alert sample.
**Builds on:** [job-market-2026-10-30.md](job-market-2026-10-30.md) (previous weekly report) and [qe-job-market-2026.md](qe-job-market-2026.md) (baseline, 21 Oct 2026).

> **How to read the numbers**
> - **Skillenai** = a job-posting index (90-day rolling window, ending 5 Nov 2026). It shows how often a skill shows up in postings, not total hiring. Its SDET sample is small (105 postings), so a move of one or two points is within noise.
> - **ITviec counts** = live listing counts pulled from itviec.com tag pages on **6 Nov 2026**. Snapshot only.
> - **ROLIVA** = a job board that reads employers' careers pages. Counts are its 2,000 most recently confirmed QA and test engineer listings on 6 Nov 2026, so percentages describe *that board*, not the whole market. A mention is not necessarily a requirement.
> - **Jobpedia.AI** = a posting aggregator that publishes per-role skill shares over 90-day windows (here, 90 days to 6 Nov 2026).
> - **Codecaf** = a one-time count of 552 QA / SDET / automation postings collected 30–31 Oct 2026 from ATS and job boards.
> - **AssertHired** = a multi-country board of QA postings (here, last seen 15 Sep – 6 Nov 2026). Framework shares are over the subset that name a browser-automation tool, not every posting.
> - **JobRemotely**, **AutomationDataCamp (ADC)**, **Mentorpiece** and **CoderPad** were not re-published this week; their figures are carried over from earlier reports and marked *carried over*.
> - Anything marked **(est.)** is an estimate or conversion made for this report. VND→USD uses about **26,000 VND/USD**, which is approximate.
> - **Job-alert sample** = aggregate counts from a sample of job-alert emails (LinkedIn digests, one Glassdoor digest, one ITviec digest), mostly job titles. No personal data, recruiter names or contacts are included.

---

## Top skills at a glance (6 Nov 2026)

**QE / automation — learn these first**
1. **CI/CD** — 59.0% of SDET postings ([Skillenai SDET](https://skillenai.com/data/role/software-development-engineer-in-test-sdet)); required in 40% of QA-engineer roles ([Jobpedia](https://jobpedia.ai/roles/qa-engineer)); named in 60% of Codecaf's 552 postings.
2. **Python**, then **Java** — Python 53.3%, Java 41.0% of SDET postings; Python is still the most-mentioned skill on ROLIVA (25% of 2,000 QA listings). Codecaf puts Python first at 43% of 552 postings.
3. **Playwright and Selenium are near-tied outside the SDET-title sample** — Playwright 46.7% vs Selenium 34.3% in Skillenai SDET; Codecaf's broader QA sample is Selenium 47% vs Playwright 46%; AssertHired (framework-named subset) puts Playwright at 64% vs Selenium 60%.
4. **API testing** — 23.8% of SDET postings; required in 25% of QA-engineer roles (Jobpedia); mentioned in **68%** of Codecaf's 552 postings.
5. **SQL** — required in 20% of QA-engineer roles (Jobpedia), 13% of ROLIVA's QA listings; 24% of Codecaf postings.

---

## What changed this week (30 Oct → 6 Nov 2026)

**Job-alert sample: 19 alerts dated 30 Oct – 6 Nov**, of which **17 are new since the previous report** (31 Oct – 6 Nov; 30 Oct overlaps). Digests came from LinkedIn job alerts, one Glassdoor digest and one ITviec digest. None came from a named recruiter.

**The changes worth acting on**

| # | Change | 30 Oct | 6 Nov | Read |
|---|---|---|---|---|
| 1 | **Playwright 1.65 shipped** (5 Nov 2026) | 1.64.1 was current | **1.65.0:** Bun as a test-runner runtime (`bunx --bun playwright test`); built-in `-exclusive-` lock (nothing else runs while that test runs); `failures` reporter and `onlyFailures` on HTML/JSON/JUnit; Node.js 20 dropped ([releases](https://github.com/microsoft/playwright/releases)) | Exclusive lock closes the gap noted in the previous teaching note. New note: [Playwright 1.65 exclusive lock and failure reporters](../../learning-material/qa-automation/Playwright%201.65%20exclusive%20lock%20and%20failure%20reporters.md). |
| 2 | **Broader samples put Playwright and Selenium near a tie; SDET-title sample still favours Playwright** | Skillenai SDET: Playwright 48.3%, Selenium 33.3% (gap 15.0 pts) | Skillenai SDET: Playwright **46.7%**, Selenium **34.3%** (gap **12.4 pts**); **Codecaf** (552 postings): Selenium **47%** vs Playwright **46%**; **AssertHired** (1,214 framework-named): Playwright **64%** vs Selenium **60%** | Tool choice depends on the sample. SDET-title postings still lean Playwright; mixed QA boards are nearly tied. Learn one deeply and expect to meet the other. |
| 3 | **"AI Quality Engineer" with stated pay, and AI+Playwright lead titles on ITviec** | AI-augmented titles in LinkedIn digests; Capgemini AI QE/SDET posting | ITviec digest: **AI Quality Engineer** at a HCMC employer, skills QA QC / Automation Test / Python / API / LLM / AI, **stated pay up to 1,250 USD net**; ITviec also lists Money Forward **Automation QA QC Test Lead/Manager (SDET, AI)** with Playwright + LLM, and a Principal/Lead Fullstack QA (Auto, AI) title | AI-in-testing keeps moving from survey talk into named local titles and a stated pay band. |
| 4 | **SDET posting sample shrank again; CI/CD and Java rose** | Skillenai SDET: 120 postings; CI/CD 57.5%; Java 37.5% | **105** postings (−12.5%); CI/CD **59.0%**; Java **41.0%**; TypeScript fell 31.7% → **28.6%** | On a ~100-posting sample, share moves of a few points are noise. Direction that repeats: CI/CD stays #1, Java is closing on the language race behind Python. |

**Cloud ordering flipped again on ROLIVA.** On 30 Oct, Azure led AWS (197 vs 171 of 2,000). On 6 Nov, **AWS 9% (184) and Azure 9% (170)** — AWS slightly ahead inside the same rounded share. See §1B.

**SDET shares, 30 Oct → 6 Nov** (Skillenai SDET; postings 120 → 105, −12.5%; window ending 5 Nov 2026):

| Skill | 30 Oct | 6 Nov | Skill | 30 Oct | 6 Nov |
|---|---|---|---|---|---|
| CI/CD | 57.5% | 59.0% | TypeScript | 31.7% | 28.6% |
| Python | 52.5% | 53.3% | Kubernetes | 22.5% | 23.8% |
| Playwright | 48.3% | 46.7% | GitHub Actions | 24.2% | 22.9% |
| JavaScript | 35.8% | 36.2% | API testing | 22.5% | 23.8% |
| Selenium | 33.3% | 34.3% | Docker | 21.7% | 21.9% |
| Java | 37.5% | 41.0% | Performance testing | 20.0% | 22.9% |
| Jenkins | 30.8% | 31.4% | Cypress | 30.8% | 30.5% |
| Test automation | 34.2% | 38.1% | | | |

*With 15 fewer postings, Java (+3.5 pts) and test automation (+3.9 pts) rose the most. Playwright and TypeScript fell; Selenium ticked up.*

**ITviec Vietnam, 30 Oct → 6 Nov 2026** (live listing counts, same tag pages):

| Tag | 30 Oct | 6 Nov |
|---|---|---|
| tester | 60 | **57** |
| automation test | 40 | **40** |
| playwright | 13 | **11** |
| sdet | 11 | **11** |

([tester](https://itviec.com/it-jobs/tester), [automation-test](https://itviec.com/it-jobs/automation-test), [playwright](https://itviec.com/it-jobs/playwright), [sdet](https://itviec.com/it-jobs/sdet))

**Job-alert sample (aggregate, 30 Oct – 6 Nov):**
- **19 alerts in 8 days**, mostly with Ho Chi Minh City locations.
- **6 of 19 subjects (~32%)** were testing-titled (QA / SDET / Quality Assurance / QC), below the ~50% share in the previous two reports. Several digests whose subject said only "Automation Engineer" still listed software QA / SDET cards in the body (and some listed industrial / SCADA / RPA roles — those are excluded from the testing count).
- Recurring QA titles: Senior QA Automation Engineer, Senior QA Engineer (Remote), Quality Assurance Automation Engineer, SDET / Sr Automation Engineer, Lead QA Automation Engineer, Full-stack Test Engineer, AI Quality Engineer, Test Automation Engineer, QC Automation Engineer (ServiceNow).
- **One alert stated pay** this window: AI Quality Engineer "Up to 1250 usd net". The previous report had one local VND band ("up to 30M").

---

## 0. Bottom line

1. **Same skill core.** CI/CD ~59%, Python ~53%, Playwright ~47%, Java ~41% top SDET postings. API testing is the quieter constant: 68% of Codecaf's broader QA sample mention it.
2. **Playwright vs Selenium depends on the sample.** SDET-title indexes still favour Playwright; Codecaf's mixed QA sample is a near-tie; AssertHired's framework-named subset puts Playwright slightly ahead. Learning one deeply remains the right move.
3. **AI-in-testing is a local hiring label now.** An "AI Quality Engineer" role with a stated USD net band, plus Money Forward SDET/Lead titles naming Playwright and LLM on ITviec.
4. **Playwright 1.65 matters for suite design.** Exclusive lock and failure-only reporters are practical CI tools, not just release notes.
5. **Pay data is mostly unchanged.** ITviec 5–8 yr medians still 25.3M VND (Tester) and 29.75M (QA-QC). New stated alert: up to **1,250 USD net** for an AI Quality Engineer role. Jobpedia median stated pay eased to **$120k/yr**.

---

## 1. Most-demanded skills, with frequency signals

### A. QE / Automation / SDET

**Global: Skillenai, SDET title, 105 postings, 90 days to 5 Nov 2026** ([source](https://skillenai.com/data/role/software-development-engineer-in-test-sdet))

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
- Top metro in this window: Pune. Top companies by indexed SDET postings: Veeam 8, CrowdStrike 8, Fiserv 4, Keeper Security 4.

**QA-engineer roles across all levels: Jobpedia.AI, 402 roles, 330 employers, 90 days to 6 Nov 2026** ([source](https://jobpedia.ai/roles/qa-engineer)) — required skills:

| Skill | Share | Skill | Share |
|---|---|---|---|
| CI/CD | 40% (160) | TypeScript | 21% (85) |
| Python | 37% (149) | Git | 21% (85) |
| Test automation | 37% (147) | Agile | 21% (84) |
| API testing | 25% (99) | JavaScript | 20% (82) |
| | | SQL | 20% (81) |
| | | Java | 19% (75) |

- Preferred skills: CI/CD 13%, test automation 11%, Docker 9%, Jira 9%, Agile 8%, AWS 8%, Python 8%, **AI 7%**, Git 6%, Kubernetes 6%.
- **79% remote** (was 76%), median stated pay **$120k** (was $123.2k; 136 of 402 state pay). 45% of roles stating years ask 5–7 years; 60% ask at least 5.
- 20% require a degree; another 22% accept experience instead; 54% don't mention one.

**Codecaf, 552 QA / automation / SDET postings, collected 30–31 Oct 2026** ([source](https://codecaf.com/research/qa-hiring-statistics/)):

| Signal | Share |
|---|---|
| Selenium | 47% (262/552) |
| Playwright | 46% (255/552) |
| Cypress | 33% (183/552) |
| Python | 43% (240/552) |
| JavaScript | 37% (203/552) |
| Java | 36% (200/552) |
| API testing mentioned | 68% (374/552) |
| CI/CD or delivery tooling | 60% (332/552) |
| Any cloud platform | 26% (143/552) |
| ISTQB mentioned | 9% (49/552) |
| Degree stated | 41% (225/552) |
| Salary range published | 29% (158/552) |

Median stated experience minimum: **4 years**. 64% of postings ask for 3+ years.

**AssertHired, framework-named subset, 15 Sep – 6 Nov 2026** ([source](https://www.asserthired.com/qa-jobs/market)): of 1,214 postings that name a browser-automation framework, Playwright **64%**, Selenium **60%**, Cypress **15%**. Country split (same subset): UK Playwright 79% / Selenium 34%; US 67% / 66%; Canada Selenium leads 77% / Playwright 38%.

### B. Cloud platforms for QA roles

| Cloud | ROLIVA 30 Oct | ROLIVA 6 Nov | JobRemotely (remote listings, 1 Oct, *carried over*) | Codecaf (30–31 Oct) |
|---|---|---|---|---|
| **AWS** | 9% (171) | **9% (184)** | **53** of 687 (53 of the 64 that name a cloud) | 21% (117/552) |
| **Azure** | 10% (197) | **9% (170)** | 23 | 12% (67/552) |
| **GCP** | 3% (68) | **3% (69)** | 31 | 8% (44/552) |

Sources: [ROLIVA QA-engineer skill insights](https://rolivajobs.com/insights/skills/qa-engineer) (2,000 of 3,649 open QA and test engineer listings, 276 employers, 61 countries, as of 6 Nov 2026); [JobRemotely cloud-jobs analysis](https://jobremotely.io/blog/cloud-jobs-aws-azure-gcp); [Codecaf](https://codecaf.com/research/qa-hiring-statistics/).

**Read:**
- **On ROLIVA, AWS and Azure are tied at 9% this week** (AWS 184, Azure 170). Last week's Azure lead flipped inside the rounding. Codecaf's broader sample puts AWS clearly first among clouds that are mentioned at all.
- What every source still agrees on: **GCP is third**, and cloud is mentioned in a minority of QA listings. One cloud well is enough.

Other ROLIVA signals (6 Nov): Python **25% (498)**, Agile 16%, Java 14%, SQL 13%, Jira 13%, JavaScript 8%, TypeScript 6%, Docker 5%, Kubernetes 4%, **Kafka 2% (39)**, **LLM 2% (39)**. Vietnam is **25 of the 2,000 listings (1%)**. ROLIVA now publishes a month-over-month column; Agile (+3 pts) and Jira (+3 pts) rose the most vs its Oct snapshot.

---

## 2. Must-have vs nice-to-have vs differentiator (mid → senior)

*Largely unchanged. Additions this week are marked.*

| Level | Must-have | Nice-to-have | Differentiator |
|---|---|---|---|
| Mid | One browser framework deeply (Playwright *or* Selenium), API testing, CI/CD basics, one language (Python or Java), Git, SQL | Cypress familiarity, Docker, JMeter/k6, cloud basics | Contract tests, Testcontainers, flaky-test control in CI |
| Senior | Framework design, pipeline ownership, mentoring, risk-based strategy | Kubernetes, performance ownership, multi-cloud | Messaging/async testing, reviewing AI-generated tests against a written spec, exclusive/parallel-safe suite design *(updated for Playwright 1.65)* |

Nothing in this window moved the mid/senior boundary. Codecaf's experience bar (median 4 years stated minimum) reinforces that most advertised roles are mid-level and up.

---

## 3. Testing messaging and distributed systems: why it matters for a QE

- **Messaging is still not a standard QE requirement.** Kafka is 2% of ROLIVA's QA listings and absent from the SDET top 15. That keeps it a differentiator.
- **New this week, on the test-runner side:** Playwright 1.65's built-in `-exclusive-` lock is the strongest form of mutual exclusion in the suite (no other test runs at all while that test holds it). Use it for true global resources; prefer named locks or per-test data for everything else. See [Playwright 1.65 exclusive lock and failure reporters](../../learning-material/qa-automation/Playwright%201.65%20exclusive%20lock%20and%20failure%20reporters.md).
- Interview framing is unchanged (*carried over*): "How would you test a Kafka consumer?", duplicate charges, DLQ after a schema change, idempotency keys on POST.

---

## 4. Salary ranges

**No new ITviec salary survey this window.** The survey figures below are unchanged. New stated figures from alerts and Jobpedia are noted.

### Vietnam local: ITviec 2025–2026 report, median **gross VND / month**
([ITviec report](https://itviec.com/report/vietnam-it-salary-and-recruitment-market), 1,839 respondents, surveyed May–Nov 2025)

| Role | <1 yr | 1–2 yr | 3–4 yr | 5–8 yr | >8 yr | Overall |
|---|---|---|---|---|---|---|
| Tester | 14.15M | 14.2M | 20.7M | 25.3M (≈$970) | 36.5M (≈$1,400) | 28.8M |
| QA-QC | – | 18M | 24.4M | 29.75M (≈$1,140) | 38.5M (≈$1,480) | 31.2M |

- **Stated in this window's alerts:** one AI Quality Engineer role "Up to 1250 usd net" (≈$1,250 net). A single alert, not survey data. On ITviec listing pages, one Quality engineer/Tester role shows "Upto 28M net".

### Remote / international
- **Jobpedia** (global QA-engineer roles that state pay): median **$120k/yr** (136 of 402 roles).
- Vendor and France figures (*carried over*): Second Talent senior QA automation remote from Vietnam **$3,900–5,600/mo**; ADC France median **€42,500/yr**.
- InterviewStack SDET board (*carried over* from Jul 2026 sample of 1,027 listings): median US base **$130,000** across 181 postings with US salary disclosed.
- **Read (est., unchanged):** a senior QA automation engineer working remotely from Vietnam lands around **$4–5.5K/mo**.

---

## 5. Typical interview formats and common topics

*Carried over; no new interview-format survey was published this window.* CoderPad 2026 (about 650 respondents): technical discussion and live coding best predict the job (60% each); 46% of companies allow AI in interviews in some form, and when they do, catching and fixing AI mistakes (66%) is the top signal ([source](https://coderpad.io/survey-reports/coderpad-state-of-tech-hiring-2026/)). The SDET loop (coding screen → framework design → API testing practical → test strategy → behavioural) is unchanged.

---

## 6. Trends

**Playwright 1.65 (5 Nov 2026): exclusive lock, failure-only reporters, Bun**
- Built-in lock name `-exclusive-`: that test runs only when no other tests are running; everything else still parallelises with each other.
- New `failures` reporter streams failures (and successful retries) live; HTML/JSON/JUnit gain `onlyFailures` to keep unexpected / flaky / interrupted tests only.
- Test runner runs under Bun via `bunx --bun playwright test` (Bun transpiles TS; watch mode and some stack-trace details differ).
- Actions now wait for elements to be not inert; Node.js 20 is no longer tested. ([releases](https://github.com/microsoft/playwright/releases/tag/v1.65.0))
- **Implication:** exclusive lock is for rare global resources; named locks (1.63) remain the default for shared accounts. Failure-only reporters shrink CI artifacts when suites are large.

**Playwright vs Selenium: three samples, three shades of the same story**
- Skillenai SDET-title: Playwright ahead (46.7% vs 34.3%).
- Codecaf mixed QA: near-tie (Selenium 47%, Playwright 46%).
- AssertHired framework-named: Playwright ahead (64% vs 60%), with large country splits (UK strongly Playwright; Canada strongly Selenium).
- UK permanent ads (*carried over* framing from Alex Staff / IT Jobs Watch, six months to 23 Oct 2026): Playwright 253 ads (up from 133 YoY), Selenium 186 (down from 467). Absolute counts, not shares of all IT ads.
- **Implication:** pick one framework deeply; treat the other as transferable skill, not a second full stack.

**AI-in-testing stays in job titles**
- Local: AI Quality Engineer (Python, API, LLM, AI) with stated USD net pay; Money Forward SDET/Lead titles naming Playwright + LLM / Generative AI on ITviec.
- Preferred-skill share for AI on Jobpedia remains **7%** — a plus, not a gate.
- Spec-driven testing evidence from the previous report (*carried over*): arXiv 2608.17177 (+9.8 pp more bugs vs code-only baseline).

**Carried over from earlier reports:** manual QA contracting decline (Mentorpiece), Playwright ahead of Selenium in French QA ads, and the "boring five" (CI/CD, API testing, one language, Git, SQL) co-occurring in 60%+ of automation ads (TestDino).

**SDET career moves** ([Skillenai SDET](https://skillenai.com/data/role/software-development-engineer-in-test-sdet)): 43 same-role moves; **QA Automation Engineer → SDET 13 moves**, Software Engineer → SDET 9, SDET → Software Engineer 2. Unchanged path into the title.

---

## 7. Recommended QA / automation skill priority list

*Order largely unchanged; changes are marked.*

1. **API testing in depth** (Playwright `request` + REST Assured): auth, schema, negative cases, idempotent methods. *(23.8% of SDET; 25% of Jobpedia QA roles; 68% of Codecaf.)*
2. **SQL + PostgreSQL transactions:** isolation levels, lost update and write skew, locking. Reproduce a race condition in a test.
3. **Testcontainers** (Java and Go) with Postgres + Kafka + RabbitMQ in CI. *(CI/CD is 59.0% of SDET postings.)*
4. **Testing async/event flows:** eventual consistency without sleep, duplicates, out-of-order, DLQ, contract tests (Pact).
5. **AI-in-testing literacy**, including **spec-driven review**: every assertion in an AI-written test should trace to a requirement.
6. **Parallel-safe suites:** unique test data per test; named Playwright locks for shared resources; `-exclusive-` only for true globals. *(updated for 1.65)*
7. **One cloud, well.** AWS or Azure are both defensible on current data; Codecaf leans AWS among postings that name a cloud.

---

## 8. Key resources (official docs and primary sources)

1. **Playwright: parallelism and test locks**: https://playwright.dev/docs/test-parallel
2. **Playwright 1.65.0 release notes**: https://github.com/microsoft/playwright/releases/tag/v1.65.0
3. **Codecaf QA hiring statistics (552 postings)**: https://codecaf.com/research/qa-hiring-statistics/
4. **AssertHired QA job market (by country)**: https://www.asserthired.com/qa-jobs/market
5. **Skillenai SDET skills**: https://skillenai.com/data/role/software-development-engineer-in-test-sdet
6. **Spec-driven test generation study (arXiv 2608.17177)**: https://arxiv.org/abs/2608.17177
7. **Playwright API testing**: https://playwright.dev/docs/api-testing
8. **PostgreSQL: transaction isolation**: https://www.postgresql.org/docs/current/transaction-iso.html

*(URLs checked for HTTP 200 on 6 Nov 2026.)*

---

## Caveats

- **Window overlap:** this report's alert window (30 Oct – 6 Nov) overlaps the previous one on 30 Oct. Only alerts from 31 Oct – 6 Nov are new.
- **Skillenai** measures posting mix, not hiring volume. The SDET sample shrank to 105, so shares move a point or two on a handful of postings.
- **ROLIVA** counts its own board and caps at 2,000 listings per role; employer count fell from 303 to 276 between the previous snapshot and today, which alone can shift percentages.
- **Codecaf** is a two-day snapshot (30–31 Oct), English-language and ATS-heavy; LinkedIn/Indeed are under-represented there.
- **AssertHired** framework shares are over the subset that name a framework (~28% of its tracked postings carry any tool tag), so they are not comparable one-to-one with Skillenai or Codecaf percentages of *all* postings.
- **JobRemotely, ADC, Mentorpiece, TestDino, InterviewStack and CoderPad** figures are carried over, not re-checked this week.
- **Jobpedia's** pay median covers only the 136 roles that state pay.
- **The spec-driven study** is one paper on one company's codebase, and its head-to-head comparisons were judged by an LLM. Treat it as early evidence.
- **ITviec counts** are a one-day snapshot (6 Nov 2026). **ITviec salaries** are self-reported 2025 survey medians.
- **The VND→USD conversion** (≈26,000) is approximate.
- **Job-alert data** is alert titles and listed job cards only, from a sample of 19 alerts. Industrial / SCADA / RPA "Automation Engineer" roles are excluded from the testing-title count. No personal data, recruiter names or contacts are included.
