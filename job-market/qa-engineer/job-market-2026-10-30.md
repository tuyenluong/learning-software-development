# Job Market 2026-10-30: QE / SDET / QA Automation

**Date:** 30 Oct 2026
**Purpose:** QA / QE automation market facts. This report covers QA, SDET and test automation roles only.
**Coverage:** weekly report. Window covered: **23–30 Oct 2026**. The previous report's window ended on 28 Oct, so **23–28 Oct overlaps**; only 29–30 Oct is new in the job-alert sample.
**Builds on:** [job-market-2026-10-28.md](job-market-2026-10-28.md) (previous weekly report) and [qe-job-market-2026.md](qe-job-market-2026.md) (baseline, 21 Oct 2026).

> **How to read the numbers**
> - **Skillenai** = a job-posting index (90-day rolling window, ending 29 Oct 2026). It shows how often a skill shows up in postings, not total hiring. Its SDET sample is small (120 postings), so a move of one or two points is within noise.
> - **ITviec counts** = live listing counts pulled from itviec.com tag pages on **30 Oct 2026**. Snapshot only.
> - **ROLIVA** = a job board that reads employers' careers pages. Counts are its 2,000 most recently confirmed QA and test engineer listings on 30 Oct 2026, so percentages describe *that board*, not the whole market. A mention is not necessarily a requirement.
> - **Jobpedia.AI** = a posting aggregator that publishes per-role skill shares over 90-day windows (here, 90 days to 30 Oct 2026).
> - **JobRemotely**, **AutomationDataCamp (ADC)**, **Mentorpiece** and **CoderPad** were not re-published this week; their figures are carried over from the previous report and marked *carried over*.
> - Anything marked **(est.)** is an estimate or conversion made for this report. VND→USD uses about **26,000 VND/USD**, which is approximate.
> - **Job-alert sample** = aggregate counts from a sample of LinkedIn/Glassdoor job-alert emails, mostly job titles. No personal data, recruiter names or contacts are included.

---

## Top skills at a glance (30 Oct 2026)

**QE / automation — learn these first**
1. **CI/CD** — 57.5% of SDET postings ([Skillenai SDET](https://skillenai.com/data/role/software-development-engineer-in-test-sdet)); required in 39% of QA-engineer roles ([Jobpedia](https://jobpedia.ai/roles/qa-engineer)).
2. **Python**, then **Java** — Python 52.5%, Java 37.5% of SDET postings; Python is also the most-mentioned skill on ROLIVA (25% of 2,000 QA listings).
3. **Playwright** — 48.3% of SDET postings, the widest lead over Selenium (33.3%) in any of these weekly reports.
4. **API testing** — 22.5% of SDET postings, required in 23% of QA-engineer roles ([Jobpedia](https://jobpedia.ai/roles/qa-engineer)).
5. **SQL** — required in 21% of QA-engineer roles (Jobpedia), 13% of ROLIVA's QA listings.

---

## What changed this week (28 Oct → 30 Oct 2026)

**Job-alert sample: 18 alerts dated 23–30 Oct**, of which **5 are new since the previous report** (29–30 Oct; 4 of those 5 were testing roles). All 18 were automated digest emails from LinkedIn job alerts and one from Glassdoor. None came from a named recruiter.

**The changes worth acting on**

| # | Change | 28 Oct | 30 Oct | Read |
|---|---|---|---|---|
| 1 | **"AI-augmented" and "spec-driven" testing appear in job titles in Ho Chi Minh City** | AI-QA seen only in survey data (Mentorpiece AI-QA 5.1% of companies) | Two alert titles from one HCMC vendor: **"Senior Test Engineer (AI-Augmented & Spec-Driven Testing)"** and **"Senior Full-stack Test Engineer (AI-Augmented Test)"**; a Capgemini "AI QE/SDET Engineer" posting asks for Playwright or Selenium plus LLM agent frameworks ([posting](https://apply.workable.com/j/450A631495)) | The AI-in-testing trend has reached local job titles. See §6 for what "spec-driven testing" means and the first controlled study of it. |
| 2 | **Playwright's lead over Selenium widened** in SDET postings | Playwright 47.0%, Selenium 34.8% (gap 12.2 pts) | Playwright **48.3%**, Selenium **33.3%** (gap **15.0 pts**) | Same direction for a third week. On a 120-posting sample this is a trend, not a precise number. |
| 3 | **SDET listings in Vietnam recovered, and alerts showed an SDET cluster** | ITviec sdet 9; no stated pay in alerts | ITviec sdet **11**; the 30 Oct digest listed SDET-titled roles at 4 HCMC employers (a digital banking platform vendor ×2, a digital bank, a GPU maker ×2, a construction-software firm). First stated pay in an alert: **"Test Engineer - Automotive - up to 30M"** | SDET as a title is still rare in Vietnam (11 listings) but no longer shrinking. 30M is in line with the QA-QC 5–8 yr median of 29.75M. |
| 4 | **Playwright shipped test locks (1.63) and WebMCP testing (1.64)** | 1.64.1 noted as current | **1.63:** named `lock` on tests so tests sharing a resource never run at once; **1.64:** `page.webmcp` to test tools a page registers for AI agents ([releases](https://github.com/microsoft/playwright/releases)) | Test locks are a direct answer to "two tests race on the same account". New teaching note: [Playwright test locks for shared resources](../../learning-material/qa-automation/Playwright%20test%20locks%20for%20shared%20resources.md). |

**Correction to the previous report's cloud reading.** On 28 Oct, ROLIVA already showed **Azure 208 vs AWS 190** of 2,000 listings (both rounded to 10%), and today it shows **Azure 10% (197) vs AWS 9% (171)**. So "AWS first" rests on the JobRemotely remote-board count alone (carried over, 1 Oct). On ROLIVA's QA board, Azure is ahead in both snapshots. See §1B.

**SDET shares, 28 Oct → 30 Oct** (Skillenai SDET; postings 132 → 120, −9.1%):

| Skill | 28 Oct | 30 Oct | Skill | 28 Oct | 30 Oct |
|---|---|---|---|---|---|
| CI/CD | 56.1% | 57.5% | TypeScript | 29.5% | 31.7% |
| Python | 51.5% | 52.5% | Kubernetes | 24.2% | 22.5% |
| Playwright | 47.0% | 48.3% | GitHub Actions | 22.7% | 24.2% |
| JavaScript | 34.8% | 35.8% | API testing | 22.0% | 22.5% |
| Selenium | 34.8% | 33.3% | Docker | 21.2% | 21.7% |
| Java | 35.6% | 37.5% | Performance testing | 19.7% | 20.0% |
| Jenkins | 31.8% | 30.8% | Cypress | 31.1% | 30.8% |
| Test automation | 33.3% | 34.2% | | | |

*With 12 fewer postings in the window, most shares rose slightly. Only Selenium, Jenkins, Cypress and Kubernetes fell.*

**ITviec Vietnam, 28 Oct → 30 Oct 2026** (live listing counts, same tag pages):

| Tag | 28 Oct | 30 Oct |
|---|---|---|
| tester | 61 | **60** |
| automation test | 40 | **40** |
| playwright | 13 | **13** |
| sdet | 9 | **11** |

([tester](https://itviec.com/it-jobs/tester), [automation-test](https://itviec.com/it-jobs/automation-test), [playwright](https://itviec.com/it-jobs/playwright), [sdet](https://itviec.com/it-jobs/sdet))

**Job-alert sample (aggregate, 23–30 Oct):**
- **18 alerts in 8 days**, all with Ho Chi Minh City locations.
- **9 of 18 (50%)** had testing-titled subjects, the same share as the previous two reports.
- Recurring QA titles: Senior SDET, Senior QA Automation Engineer, Software QA Engineer, Senior Quality Engineer (Automation), QC Auto (twice), QA Tester, Test Engineer.
- **One alert stated pay** ("up to 30M", a test engineer role in automotive). The previous report had none.

---

## 0. Bottom line

1. **Same skill core, sharper Playwright lead.** CI/CD 57.5%, Python 52.5%, Playwright 48.3%, Java 37.5% top SDET postings. Playwright now leads Selenium by 15 points in this sample.
2. **AI-in-testing has moved from surveys into Vietnamese job titles.** Two "AI-augmented" test-engineer titles in HCMC this week, one naming **spec-driven testing**. A controlled study at Google ([arXiv 2608.17177](https://arxiv.org/abs/2608.17177)) found spec-driven test generation caught more real bugs than a code-only baseline.
3. **Cloud ordering is less settled than last week's report said.** ROLIVA's QA board puts Azure slightly ahead of AWS (197 vs 171 of 2,000); the remote board (carried over) puts AWS well ahead. Learn one cloud well; which one is a coin toss on current data.
4. **Pay data is unchanged.** ITviec 5–8 yr medians are still 25.3M VND (Tester) and 29.75M (QA-QC). The one stated alert range (up to 30M) fits them.

---

## 1. Most-demanded skills, with frequency signals

### A. QE / Automation / SDET

**Global: Skillenai, SDET title, 120 postings, 90 days to 29 Oct 2026** ([source](https://skillenai.com/data/role/software-development-engineer-in-test-sdet))

| Skill | Share of postings |
|---|---|
| CI/CD | 57.5% |
| Python | 52.5% |
| Playwright | 48.3% |
| Java | 37.5% |
| JavaScript | 35.8% |
| Test automation | 34.2% |
| Selenium | 33.3% |
| TypeScript | 31.7% |
| Cypress | 30.8% |
| Jenkins | 30.8% |
| GitHub Actions | 24.2% |
| Kubernetes | 22.5% |
| API testing | 22.5% |
| Docker | 21.7% |
| Performance testing | 20.0% |

- **Messaging, Kafka and distributed systems are still absent from the SDET top 15.** For a QE they remain a **differentiator**, not a requirement.
- Top metro in this window: Pune.

**QA-engineer roles across all levels: Jobpedia.AI, 337 roles, 277 employers, 90 days to 30 Oct 2026** ([source](https://jobpedia.ai/roles/qa-engineer)) — required skills:

| Skill | Share | Skill | Share |
|---|---|---|---|
| CI/CD | 39% (132) | TypeScript | 21% (71) |
| Python | 38% (127) | Git | 21% (70) |
| Test automation | 35% (118) | SQL | 21% (70) |
| API testing | 23% (76) | JavaScript | 20% (67) |
| Agile | 21% (72) | Java | 19% (64) |

- Preferred skills: CI/CD 13%, test automation 11%, Python 9%, Agile 9%, Docker 9%, Jira 8%, **AI 7%**, AWS 7%.
- **76% remote** (was 74%), median stated pay **$123.2k** (was $125k; 116 of 337 state pay). 45% of roles stating years ask 5–7 years; 61% ask at least 5.
- 23% require a degree; another 24% accept experience instead; 50% don't mention one.

### B. Cloud platforms for QA roles

| Cloud | ROLIVA 28 Oct | ROLIVA 30 Oct | JobRemotely (remote listings, 1 Oct, *carried over*) |
|---|---|---|---|
| **AWS** | 10% (190) | **9% (171)** | **53** of 687 (53 of the 64 that name a cloud) |
| **Azure** | 10% (208) | **10% (197)** | 23 |
| **GCP** | 4% (77) | **3% (68)** | 31 |

Sources: [ROLIVA QA-engineer skill insights](https://rolivajobs.com/insights/skills/qa-engineer) (2,000 of 3,609 open QA and test engineer listings, 303 employers, 65 countries, as of 30 Oct 2026); [JobRemotely cloud-jobs analysis](https://jobremotely.io/blog/cloud-jobs-aws-azure-gcp).

**Read:**
- **On ROLIVA, Azure is ahead of AWS in both snapshots.** The previous report's "AWS first" relied on the remote board. The two sources now point different ways at the top, not only below it.
- What both agree on: **GCP is third** on ROLIVA and second on the remote board, and all three are mentioned in a small minority of QA listings (3–10%). Cloud is not a core QA requirement; one cloud well is enough.

Other ROLIVA signals (30 Oct): Python **25% (509)**, Agile 15%, Java 14%, SQL 13%, Jira 12%, JavaScript 8%, TypeScript 6%, Docker 5%, Kubernetes 5%, **Kafka 2% (44)**, **LLM 2% (33)**. Vietnam is **25 of the 2,000 listings (1%)**. ROLIVA notes that no earlier month is stored yet, so it publishes no change column itself; the 28 Oct column above is from the previous report.

---

## 2. Must-have vs nice-to-have vs differentiator (mid → senior)

*Unchanged from the previous report. Nothing in this window's data moved the mid/senior boundary.* One addition to the senior differentiator column: **reviewing AI-generated tests against a written spec** (see §6, spec-driven testing).

---

## 3. Testing messaging and distributed systems: why it matters for a QE

- **Messaging is still not a standard QE requirement.** Kafka is 2% of ROLIVA's QA listings and absent from the SDET top 15. That keeps it a differentiator.
- **New this week, on the test-runner side:** Playwright 1.63's test locks address a classic shared-resource race inside the test suite itself (two parallel tests editing the same account or settings). It is the test-suite version of the "two requests withdraw from the same account" problem. See the teaching note [Playwright test locks for shared resources](../../learning-material/qa-automation/Playwright%20test%20locks%20for%20shared%20resources.md).
- Interview framing is unchanged (*carried over*): "How would you test a Kafka consumer?", duplicate charges, DLQ after a schema change, idempotency keys on POST.

---

## 4. Salary ranges

**No new survey this window.** The figures below are the ITviec 2025–2026 survey, unchanged.

### Vietnam local: ITviec 2025–2026 report, median **gross VND / month**
([ITviec report](https://itviec.com/report/vietnam-it-salary-and-recruitment-market), 1,839 respondents, surveyed May–Nov 2025)

| Role | <1 yr | 1–2 yr | 3–4 yr | 5–8 yr | >8 yr | Overall |
|---|---|---|---|---|---|---|
| Tester | 14.15M | 14.2M | 20.7M | 25.3M (≈$970) | 36.5M (≈$1,400) | 28.8M |
| QA-QC | – | 18M | 24.4M | 29.75M (≈$1,140) | 38.5M (≈$1,480) | 31.2M |

- **Stated in this window's alerts:** one test engineer role (automotive) "up to 30M" (≈$1,150, est.). A single alert, not survey data.

### Remote / international
- **Jobpedia** (global QA-engineer roles that state pay): median **$123.2k/yr** (116 of 337 roles).
- Vendor and France figures (*carried over*): Second Talent senior QA automation remote from Vietnam **$3,900–5,600/mo**; ADC France median **€42,500/yr**.
- **Read (est., unchanged):** a senior QA automation engineer working remotely from Vietnam lands around **$4–5.5K/mo**.

---

## 5. Typical interview formats and common topics

*Carried over; no new interview-format survey was published this window.* CoderPad 2026 (about 650 respondents): technical discussion and live coding best predict the job (60% each); 46% of companies allow AI in interviews in some form, and when they do, catching and fixing AI mistakes (66%) is the top signal ([source](https://coderpad.io/survey-reports/coderpad-state-of-tech-hiring-2026/)). The SDET loop (coding screen → framework design → API testing practical → test strategy → behavioural) is unchanged.

---

## 6. Trends

**Spec-driven testing: the first controlled numbers**
- A paper at ACM SpecOps '26 ([arXiv 2608.17177](https://arxiv.org/abs/2608.17177), 4 Oct 2026) compared an LLM agent that writes tests from a specification with one that writes tests from the code alone, on real production bugs at Google. The spec-driven agent found **+9.8 percentage points more bugs** (p = 0.0352) and **+2.5 points more branch coverage**. Judged by an LLM, its tests beat the baseline's in **77.8%** of cases and human-written tests in **56.7%**.
- **Why it works:** a test generated from the code tends to assert what the code does, bugs included. A test generated from the spec asserts what the code *should* do, which is the only way a test can catch a bug.
- **Tooling gap:** a [qa.tech analysis](https://qa.tech/blog/spec-driven-development-verification) points out that spec-driven development kits such as GitHub Spec Kit and Kiro generate code from specs but do not verify the result against the spec. It argues for an independent verifier with three verdicts: pass, fail and **unverified** (the spec says something no test checks).
- **Implication:** "spec-driven" is the AI-era name for an old QA skill, writing tests from requirements rather than from the implementation. The new part is reviewing AI-written tests for whether each assertion traces back to a spec line.

**Playwright keeps adding parallel-safety and agent-testing features**
- **1.63 (4 Sep 2026):** test locks; `frameLocator()` without a selector searches all frames; `locator.visible()` replaces the `:visible` pseudo-class; step `subtitle` and `params` for reporters; aria and screen snapshots in traces.
- **1.64 (7 Oct 2026):** `page.webmcp` / `frame.webmcp` to test the tools a page registers for AI agents through WebMCP; Playwright MCP supports WebMCP by default. 1.64.1 (14 Oct) is bug fixes. ([releases](https://github.com/microsoft/playwright/releases))
- **Implication:** "test the AI-facing surface of a web app" is becoming a concrete Playwright task, not only an LLM-evaluation task.

**Carried over from the previous report:** manual QA contracting (Mentorpiece: companies with open manual QA roles 14.1% → 9.5%, Mar → Sep 2026), Playwright ahead of Selenium in French QA ads (24.2% vs 21.7%), and the "boring five" (CI/CD, API testing, one language, Git, SQL) co-occurring in 60%+ of automation ads (TestDino).

**SDET career moves** ([Skillenai SDET](https://skillenai.com/data/role/software-development-engineer-in-test-sdet)): 43 same-role moves; **QA Automation Engineer → SDET 13 moves**, Software Engineer → SDET 9, SDET → Software Engineer 2. The automation-engineer-to-SDET path is the most common way into the title in this sample.

---

## 7. Recommended QA / automation skill priority list

*Order unchanged from the previous report; changes are marked.*

1. **API testing in depth** (Playwright `request` + REST Assured): auth, schema, negative cases, idempotent methods. *(22.5% of SDET postings; 23% of QA roles.)*
2. **SQL + PostgreSQL transactions:** isolation levels, lost update and write skew, locking. Reproduce a race condition in a test.
3. **Testcontainers** (Java and Go) with Postgres + Kafka + RabbitMQ in CI. *(CI/CD is 57.5% of SDET postings.)*
4. **Testing async/event flows:** eventual consistency without sleep, duplicates, out-of-order, DLQ, contract tests (Pact).
5. **AI-in-testing literacy**, now including **spec-driven review**: every assertion in an AI-written test should trace to a requirement. *(changed)*
6. **Parallel-safe suites:** unique test data per test, and Playwright test locks for the few resources that can't be isolated. *(new)*
7. **One cloud, well.** *(changed: the data no longer clearly says which one; AWS or Azure are both defensible.)*

---

## 8. Key resources (official docs and primary sources)

1. **Playwright: parallelism and test locks**: https://playwright.dev/docs/test-parallel
2. **Playwright release notes**: https://github.com/microsoft/playwright/releases
3. **Spec-driven test generation study (arXiv 2608.17177)**: https://arxiv.org/abs/2608.17177
4. **Playwright API testing**: https://playwright.dev/docs/api-testing
5. **PostgreSQL: transaction isolation**: https://www.postgresql.org/docs/current/transaction-iso.html

*(URLs checked for HTTP 200 on 30 Oct 2026.)*

---

## Caveats

- **Window overlap:** this report's alert window (23–30 Oct) overlaps the previous one (17–28 Oct) for 23–28 Oct. Only 5 alerts (29–30 Oct) are new.
- **Skillenai** measures posting mix, not hiring volume. The SDET sample shrank to 120, so shares move a point or two on a handful of postings.
- **ROLIVA** counts its own board and caps at 2,000 listings per role; employer count fell from 325 to 303 between snapshots, which alone can shift percentages.
- **JobRemotely, ADC, Mentorpiece, TestDino and CoderPad** figures are carried over, not re-checked this week.
- **Jobpedia's** pay median covers only the 116 roles that state pay.
- **The spec-driven study** is one paper on one company's codebase, and its head-to-head comparisons were judged by an LLM. Treat it as early evidence.
- **ITviec counts** are a one-day snapshot (30 Oct 2026). **ITviec salaries** are self-reported 2025 survey medians.
- **The VND→USD conversion** (≈26,000) is approximate.
- **Job-alert data** is alert titles only, from a sample of 18 alerts. No personal data, recruiter names or contacts are included.
