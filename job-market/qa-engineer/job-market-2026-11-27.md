# Job Market 2026-11-27: QE / SDET / QA Automation

**Date:** 27 Nov 2026
**Purpose:** QA / QE automation market facts. This report covers QA, SDET and test automation roles only.
**Coverage:** weekly report. Window covered: **20 – 27 Nov 2026**. The previous report's window ended on 20 Nov, so **20 Nov overlaps**; only **21 – 27 Nov** is new in the job-alert sample.
**Builds on:** [job-market-2026-11-20.md](job-market-2026-11-20.md) (previous weekly report) and [qe-job-market-2026.md](qe-job-market-2026.md) (baseline, 21 Oct 2026).

> **How to read the numbers**
> - **Skillenai** = a job-posting index (90-day rolling window). Its SDET page **was refreshed this week** (90 days ending 25 Nov 2026, **61 postings**, down from 81), so shares can move on a small base.
> - **ITviec counts** = live listing counts from itviec.com tag pages, **refreshed this week** (27 Nov 2026; the 20 Nov report had to carry the 13 Nov counts over).
> - **ROLIVA** = a job board that reads employers' careers pages. Counts are its 2,000 most recently confirmed QA and test engineer listings on 27 Nov 2026, so percentages describe *that board*, not the whole market. A mention is not necessarily a requirement.
> - **Jobpedia.AI** = a posting aggregator that publishes per-role skill shares over 90-day windows (here, 90 days to 27 Nov 2026).
> - **Codecaf** = a one-time count of 552 QA / SDET / automation postings collected 30–31 Oct 2026 (annual edition; unchanged).
> - **AssertHired** = a multi-country board of QA postings (here, last seen 15 Sep – 27 Nov 2026). Framework, language and tool shares are over the subset that name a tool in that table, not every posting.
> - **Local posting texts** = **34** full LinkedIn job pages for the testing roles in the job-alert sample, read on 27 Nov 2026. Counts are keyword mentions ("named in N of 34"), not weighted requirements.
> - **JobRemotely**, **AutomationDataCamp (ADC)**, **Mentorpiece** and **CoderPad** were not re-published this week; their figures are carried over from earlier reports and marked *carried over*.
> - Anything marked **(est.)** is an estimate or conversion made for this report. VND→USD uses about **26,000 VND/USD**, which is approximate.
> - **Job-alert sample** = aggregate counts from a sample of job-alert emails (LinkedIn digests and recommendations, one Glassdoor digest, one freelance-board digest), mostly job titles. No personal data, recruiter names or contacts are included.

---

## Top skills at a glance (27 Nov 2026)

**QE / automation — learn these first**
1. **CI/CD** — required in **40%** of QA-engineer roles ([Jobpedia](https://jobpedia.ai/roles/qa-engineer), 211 of 521); 59.0% of SDET postings ([Skillenai SDET](https://skillenai.com/data/role/software-development-engineer-in-test-sdet)); named in **26 of 34** local posting texts.
2. **Python, then Java** — AssertHired language subset: Python **48%**, Java **46%** (was level at 47% / 47%) ([AssertHired](https://www.asserthired.com/qa-jobs/market)); Python 38% of Jobpedia QA roles (197 of 521) and 24% of ROLIVA's 2,000 QA listings; in local posting texts Python 20 and Java 11 of 34.
3. **Playwright, ahead of Selenium again** — AssertHired framework-named subset: Playwright **66%** vs Selenium **61%**; Skillenai SDET 42.6% vs 31.1%; local posting texts **23 vs 19** of 34 (was 18 vs 18 of 33).
4. **API testing** — required in 24% of QA-engineer roles (Jobpedia, 127 of 521); named in **24 of 34** local posting texts. Postman (59%) and REST Assured (55%) lead the AssertHired API-tool subset.
5. **SQL** — required in 19% of QA-engineer roles (Jobpedia, 98 of 521); 11% of ROLIVA's QA listings.

**Rising this week:** payment and transaction-flow testing (idempotency, retries, webhooks, settlement, concurrency). **Idempotency** is named in **5 of 34** local posting texts (1 of 33 last week), and **k6** in 6 of 34 (3 of 33).

---

## What changed this week (20 Nov → 27 Nov 2026)

**Job-alert sample: 18 alerts dated 20 – 27 Nov**, of which **15 are new since the previous report** (21 – 27 Nov; 20 Nov overlaps). New digests came from LinkedIn job alerts and recommendations (13), one Glassdoor digest and one freelance-board digest. Two of the 15 were backend alerts and are out of scope here, so **13 alerts** feed the testing counts. None came from a named recruiter.

**The changes worth acting on**

| # | Change | 20 Nov | 27 Nov | Read |
|---|---|---|---|---|
| 1 | **Playwright pulled ahead of Selenium in local postings** | 18 vs 18 of 33 local posting texts | **23 vs 19 of 34**; Cypress 13; AssertHired Playwright 66% vs Selenium 61% (was 65% vs 60%) | The local tie was one week. Playwright leads on every board this week except Codecaf's annual count. |
| 2 | **Payment and transaction testing spread from one ad to several** | One local ad (VORTECH) named wallets, idempotency and races | **Idempotency 5 of 34**, concurrency or race conditions 3, wallet / payment / transaction 9, k6 6. The VORTECH wallet text now appears in 3 postings (two VORTECH titles plus an anonymous "Client Company (Game Industry)" page). **Hello Clever** (payments fintech) asks for API testing of "Authentication, Idempotency, Retries, Webhooks", mock PSPs and webhooks, settlement and reconciliation | Webhook delivery is now part of the transaction-testing set. New note: [Testing payment webhooks: duplicates, out-of-order events and signatures](../../learning-material/qa-automation/Testing%20payment%20webhooks%20-%20duplicates%2C%20out-of-order%20events%20and%20signatures.md). |
| 3 | **Product companies became the largest hiring type** | Outsourcing 12 of 36 (33%), product 10 (28%) | **Product 12 of 31 (39%)**, outsourcing 9 (29%); consultancy 6 → 3, staffing 3 → 1 | 14 of the 31 companies are new this week (banking platforms, payments, hardware, EdTech). See [Hiring companies](#hiring-companies-job-alert-sample-21--27-nov). |
| 4 | **Vietnam listing counts fell** | ITviec (13 Nov, carried over): tester 57, automation test 40, playwright 12, sdet 10 | **Tester 54, automation test 29, playwright 9, sdet 6** | A two-week drop on ITviec, while the job-alert sample held steady. One board, one snapshot. |
| 5 | **Cypress added a headless mode for coding agents; Appium 4 is out** | Cypress 16.3, Appium 3.x | **Cypress 16.4** (25 Nov): `cypress open --headless` so a `cypress tap` session runs without taking focus, "such as when an AI coding agent runs your tests" ([changelog](https://docs.cypress.io/app/references/changelog#16-4-0)). **Appium 4.0.0** (15 Nov) with breaking server changes; 4.0.1 (23 Nov) and 4.0.2 (27 Nov) fixes ([4.0.0](https://github.com/appium/appium/releases/tag/appium%404.0.0)) | Mobile suites that pin Appium 3 need a planned upgrade; removed server flags (e.g. `--strict-caps`) break old launch scripts. |

**Jobpedia QA-engineer roles, 20 Nov → 27 Nov** ([source](https://jobpedia.ai/roles/qa-engineer); 90-day windows):

| Signal | 20 Nov | 27 Nov |
|---|---|---|
| Roles counted | 487 | **521** |
| Employers | 396 | **424** |
| CI/CD required | 40% | **40%** (211) |
| Test automation required | 38% | **39%** (201) |
| Python required | 38% | **38%** (197) |
| API testing required | 25% | **24%** (127) |
| SQL required | 19% | **19%** (98) |
| Remote | 81% | **82%** |
| Median stated pay | $121.7k | **$120k** (173 of 521 state pay) |

*Test automation (201) moved ahead of Python (197) behind CI/CD; the sample grew by 34 roles.*

**ITviec Vietnam, 27 Nov** (refreshed): tester **54**, automation test **29**, playwright **9**, sdet **6** ([tester](https://itviec.com/it-jobs/tester), [automation-test](https://itviec.com/it-jobs/automation-test), [playwright](https://itviec.com/it-jobs/playwright), [sdet](https://itviec.com/it-jobs/sdet)). 13 Nov: 57 / 40 / 12 / 10.

**Job-alert sample (aggregate, 20 – 27 Nov):**
- **18 alerts in 8 days**, almost all with Ho Chi Minh City locations (the freelance listing is in Hà Nội).
- **6 of 15 new subjects (40%)** were testing-titled (QA / QC / QA Automation), down from 50% in the previous report. Five were "automation engineer" alerts whose subject job was not testing (workflow automation, logistics, industrial), two were backend alerts and two had generic subjects.
- **48 testing job cards** across the digests, **43 distinct postings**, from **31 companies** plus one unnamed freelance listing. Workflow / RPA "automation", industrial PLC, hardware module test, DevOps and quality-auditor cards are excluded.
- **Seniority from titles:** 24 of 48 cards are senior or lead; 1 is early-career; the rest give no level. LinkedIn's own field marks 3 postings as entry level (FPT, ISB Vietnam, the anonymous game-industry page).
- **Work mode:** 2 postings state fully remote (Kake, Colonist); the rest are on-site or hybrid in HCMC.
- **Stated pay this window:** JDI (recruiter) Senior QA Automation Engineer (Python), hybrid HCMC, **up to $2,500 gross/month**; freelance board: Senior Tester (Japanese-speaking, manual UI/API), Hà Nội, 20–45M VND (≈$770–1,730, est.), the same listing as the previous window. Kake and Colonist state "paid in USD" without a figure.

---

## Hiring companies (job-alert sample, 21 – 27 Nov)

Each company is classified from its own website or its LinkedIn company page. "–" means the source does not state it. Types: **product** company; **consultancy or agency**; **outsourcing or offshore service**; **staffing or recruiter** posting for an unnamed client; **other** (bank, insurer, retailer, in-house IT); **unclear** where sources conflict or say nothing. Sizes are LinkedIn bands unless stated otherwise.

| Company | Type | Industry | Size | HQ | Roles posted (testing cards) | Source |
|---|---|---|---|---|---|---|
| Orient Software | Outsourcing or offshore service | Software development outsourcing | – | Vietnam | [HCM/DN] Senior Automation Test Engineer | [site](https://www.orientsoftware.com/) |
| VORTECH | Outsourcing or offshore service | B2B software outsourcing | 201–500 | – | Senior Quality Control Engineer (2 cards); Senior QA Engineer | [LinkedIn](https://www.linkedin.com/company/vortech-entertainment/) |
| FPT Software | Outsourcing or offshore service | IT services | 10,001+ | Vietnam | Automation Test (early career) | [LinkedIn](https://www.linkedin.com/company/fsoft-academy/), [site](https://fptsoftware.com/) |
| DXC Technology | Outsourcing or offshore service | Enterprise IT services | – | – | Quality Engineering; Senior Automation Test; Quality Engineer (Auto+Manual) | [LinkedIn](https://www.linkedin.com/company/dxctechnology/), [site](https://dxc.com/) |
| Kake | Outsourcing or offshore service (Teams as a Service) | IT services | 201–500 | – (remote-first) | Senior QA Engineer – Remote (contract) | [LinkedIn](https://www.linkedin.com/company/kake/) |
| CODE LEAP | Outsourcing or offshore service (roles for named client JTL-Software) | IT services, Germany–Vietnam dev teams | 51–200 | Germany / Vietnam | Senior QA Automation Engineer – DC34; Senior QA Automation Engineer (Shipping) – DC34 | [LinkedIn](https://www.linkedin.com/company/codeleapag/), [site](https://codeleap.de/) |
| ISB Vietnam (IVC) | Outsourcing or offshore service (offshore development centre set up by ISB Group, Japan, in 2003) | Outsourcing and offshoring | 501–1,000 | Vietnam (parent in Japan) | Quality Assurance Automation Engineer | [LinkedIn](https://www.linkedin.com/company/isb-vietnam-co.-limited/), [site](https://isb-vietnam.com.vn/) |
| Elisoft (Elinext Alliance) | Outsourcing or offshore service (custom software for international clients) | Software development | 51–200 | – (group offices in USA, Singapore, Hong Kong, Vietnam) | [HCM – Onsite] Senior QA Automation | [LinkedIn](https://www.linkedin.com/company/elisoft/) |
| GTEMAS | Outsourcing or offshore service (dedicated teams and embedded specialists; also permanent recruitment) | Engineering partner and talent services | – | Vietnam (Hà Nội office) | QA Engineer (remote / hybrid) | [site](https://gtemas.com/), [careers](https://gtemas.com/careers/qa-engineer) |
| Amaris Consulting | Consultancy or agency | Technology consulting | 7,600 people | – | Data Quality Control Analyst (Manual/Automation) (same card as previous window) | [site](https://amaris.com/) |
| Astek Vietnam | Consultancy or agency | Engineering and technology consulting | 5,001–10,000 (group 7,500+) | France (group) | Senior Quality Assurance Engineer (2 cards) | [LinkedIn](https://www.linkedin.com/company/astek-vietnam/) |
| Vinova | Consultancy or agency | Software development for clients | 201–500 | Singapore | Senior Automation QA | [LinkedIn](https://www.linkedin.com/company/vinova-sg/) |
| Motorola Solutions | Product company | Public-safety networks, video security | 10,001+ | US (Chicago) | QA Automation Engineer; Test Engineer (vehicle software); QA Automation Engineer (MLOps) | [LinkedIn](https://www.linkedin.com/company/motorolasolutions/) |
| Backbase | Product company | Banking software platform | 1,001–5,000 | Netherlands (Amsterdam) | Senior Software Development Engineer in Test (2 cards) | [LinkedIn](https://www.linkedin.com/company/backbase/) |
| Safetrust | Product company | Physical access software | 51–200 | – | QA Automation Engineer Lead | [LinkedIn](https://www.linkedin.com/company/safetrust-inc-/) |
| Hello Clever | Product company | Payments and loyalty fintech | 51–200 | Australia (Sydney) | QA Automation Engineer; QA Engineer – Manual | [LinkedIn](https://www.linkedin.com/company/helloclever/), [site](https://helloclever.co/) |
| Datalogic | Product company | Barcode readers, mobile computers, sensors | 1,001–5,000 | Italy (Bologna area) | Automation SW Test Engineer (SDET) | [LinkedIn](https://www.linkedin.com/company/datalogic/) |
| Corsair | Product company | Gaming hardware and peripherals | 1,001–5,000 | US (Milpitas, CA) | Software QA Engineer (2 cards); Automation Engineer (software test); Test Engineer, Fanatec (firmware validation) | [LinkedIn](https://www.linkedin.com/company/corsair/) |
| Aquariux Fintech | Product company (white-label trading platforms and payment gateways, sold as a service) | Fintech | 11–50 | Singapore | Senior QA Automation Engineer (2 cards) | [LinkedIn](https://www.linkedin.com/company/aquariux-fintech/) |
| Qualgo Technologies | Product company | Cybersecurity products | 201–500 | – | Senior QA Engineer | [LinkedIn](https://www.linkedin.com/company/qualgotech/) |
| Colonist | Product company | Online multiplayer games | 11–50 | Remote | QA Engineer (fully remote) | [LinkedIn](https://www.linkedin.com/company/colonist/), [site](https://colonist.io/) |
| STYL Solutions | Product company | Payment terminals and IoT | – | Singapore | Senior QA Automation Engineer | [site](https://styl.com.sg/about-us/) |
| Innovation in Technology Pty Ltd | Product company (Binder Education SaaS, built by its HCMC team JC Computing VN) | EdTech | – | Australia (VIC, per ABN record) | QA Analyst (Glassdoor) | [ABN record](https://abr.business.gov.au/ABN/View?id=59649004820), [App Store](https://apps.apple.com/us/app/binder-education/id6757095278) |
| VinFast | Product company (vehicle maker; in-house vehicle software) | Electric vehicles | 5,001–10,000 | Vietnam (Hai Phong) | Software Test Engineer | [LinkedIn](https://www.linkedin.com/company/vinfast/) |
| JDI (Talent JDI) | Staffing or recruiter (unnamed client) | IT recruitment, employer-of-record and venture services | 51–200 | Singapore | Senior QA Automation Engineer (Python) | [LinkedIn](https://www.linkedin.com/company/jdi-group/), [site](https://talentjdi.com/) |
| Galaxy FinX | Other (technology company that built a digital bank; role is for a group-wide AI platform) | Financial services, digital banking | 51–200 | Vietnam (HCMC) | Senior QA/QC (AI Platform) (2 cards) | [LinkedIn](https://www.linkedin.com/company/galaxy-finx/) |
| GoTymeX | Other (in-house technology hub of a digital-banking group) | Digital banking | 501–1,000 | Vietnam hub; group HQ Singapore | Quality Automation Engineer | [LinkedIn](https://www.linkedin.com/company/lifeatgotymex/), [site](https://vietnam.tyme.com/) |
| SCC Vietnam | Other (service centre for a UK / French IT group) | IT services, group-internal | 201–500 | UK / France (group) | Software Test Engineer (Automation) | [LinkedIn](https://www.linkedin.com/company/scc-vn/) |
| Zeya Labs AI | Other (in-house lab of an operating group) | AI and data for a diversified group | 11–50 | Vietnam | Senior QA Engineer (Automation) | [LinkedIn](https://www.linkedin.com/company/zeya-labs-ai/) |
| Colonial Surety Company | Other (insurer) | Insurance | 11–50 | US | QA Engineer – Manual/Visual and automation (2 cards) | [LinkedIn](https://www.linkedin.com/company/colonial-surety-company/) |
| "Client Company (Game Industry)" | Unclear (anonymous company page with no description; the posting text matches VORTECH's wallet-testing posting word for word) | Information services (LinkedIn label) | 51–200 | – | QA Automation Engineer | [LinkedIn](https://www.linkedin.com/company/client-company-game-industry/) |

**Split by type (31 companies):** product **12 (39%)** · outsourcing or offshore **9 (29%)** · other **5 (16%)** · consultancy or agency **3 (10%)** · staffing or recruiter **1 (3%)** · unclear **1 (3%)**. By testing cards (47 with a named company): product 20 (43%), outsourcing 14 (30%), other 7 (15%), consultancy 4 (9%), staffing 1 (2%), unclear 1 (2%).
**Week over week ([20 Nov](job-market-2026-11-20.md), 36 companies):** outsourcing 12 (33%) → **9 (29%)** · product 10 (28%) → **12 (39%)** · consultancy 6 (17%) → **3 (10%)** · other 4 (11%) → **5 (16%)** · staffing 3 (8%) → **1 (3%)** · unclear 1 (3%) → **1 (3%)**. 17 companies appear in both weeks; 14 are new.

**Read:** product companies now lead on both company count and card count, helped by banking and payments platforms (Backbase, Hello Clever, Aquariux) and hardware makers (Corsair 4 cards, Motorola 3, Datalogic). Outsourcing firms still post several cards each (VORTECH 3, DXC 3). Only one recruiter post for an unnamed client this week.

---

## 0. Bottom line

1. **Same skill core.** CI/CD (40% of Jobpedia QA roles), test automation, Python and Java, Playwright, API testing and SQL.
2. **Playwright leads again in local postings** (23 vs 19 of 34) and in AssertHired's multi-country subset (66% vs 61%). Selenium is still named in more than half of local texts.
3. **Transaction-flow testing is no longer a one-off.** Idempotency, retries, webhooks and race conditions show up in 5 local postings across 3 employers (VORTECH, Hello Clever and an anonymous game-industry page), with k6 named for load.
4. **Product companies are the largest hiring type this week** (39% of companies, 43% of cards), up from 28%.
5. **Pay:** Jobpedia median **$120k/yr**; one local recruiter band of **up to $2,500 gross/month** for a senior Python automation role; ITviec survey medians unchanged.

---

## 1. Most-demanded skills, with frequency signals

### A. QE / Automation / SDET

**Global: Skillenai, SDET title, 61 postings, 90 days to 25 Nov 2026** ([source](https://skillenai.com/data/role/software-development-engineer-in-test-sdet)) — *refreshed this week (was 81 postings to 19 Nov).*

| Skill | Share of postings | 19 Nov |
|---|---|---|
| CI/CD | 59.0% | 59.3% |
| Python | 55.7% | 54.3% |
| Playwright | 42.6% | 46.9% |
| Test automation | 41.0% | 39.5% |
| Java | 41.0% | 39.5% |
| Jenkins | 32.8% | 33.3% |
| Selenium | 31.1% | 33.3% |
| JavaScript | 31.1% | 33.3% |
| Kubernetes | **27.9%** | 23.5% |
| API testing | 26.2% | 29.6% |
| GitHub Actions | 26.2% | 24.7% |
| TypeScript | 26.2% | 28.4% |
| Git | 24.6% | 24.7% |
| Cypress | 24.6% | 30.9% |
| Docker | 23.0% | – (not in top 15) |

- Performance testing (21.0% on 19 Nov) dropped out of the top 15; Docker came back. Kubernetes gained most, on a sample that shrank by a quarter.
- **Messaging, Kafka and distributed systems are still absent from the SDET top 15.** For a QE they remain a **differentiator**, not a requirement.

**QA-engineer roles across all levels: Jobpedia.AI, 521 roles, 424 employers, 90 days to 27 Nov 2026** ([source](https://jobpedia.ai/roles/qa-engineer)) — required skills:

| Skill | Share | Skill | Share |
|---|---|---|---|
| CI/CD | 40% (211) | TypeScript | 21% (109) |
| Test automation | 39% (201) | Agile | 21% (107) |
| Python | 38% (197) | JavaScript | 21% (107) |
| API testing | 24% (127) | Java | 19% (100) |
| Git | 21% (109) | SQL | 19% (98) |

- Preferred skills: CI/CD 15%, test automation 11%, Jira 9%, Docker 9%, AWS 8%, Agile 8%, Git 7%, Python 7%, **AI 7%** (36 of 521), API testing 6%.
- **82% remote.** 46% of roles stating years ask 5–7 years; 60% ask at least 5.
- 18% require a degree; another 22% accept experience instead; 57% don't mention one.
- By level: junior 43, mid 157, senior 199, staff 20, principal 10, lead 16 roles.

**AssertHired, 6,623 QA postings across 18 countries, last seen 15 Sep – 27 Nov 2026** ([source](https://www.asserthired.com/qa-jobs/market)):

| Table (subset that names a tool) | Result | 20 Nov |
|---|---|---|
| Browser frameworks (1,074 postings) | Playwright **66%**, Selenium **61%**, Cypress 15%, WebdriverIO 1.9% | 65% / 60% / 14% / 1.7% |
| Languages (1,351 postings) | Python **48%**, Java **46%**, JavaScript 18%, TypeScript 15%, C# 15% | 47% / 47% / 18% / 16% / 14% |
| API tools (244 postings) | Postman 59%, REST Assured 55% | 60% / 55% |
| Performance tools (80 postings) | JMeter 95%, Gatling 24%, k6 13% | 93% / 24% / 11% |
| Seniority (all 6,623) | Entry 3.1%, Mid 64%, Senior 25%, Lead/manager 8.6%; remote 4.2% | 3.1 / 64 / 24 / 8.7; 4.1% |

Country split for frameworks: UK Playwright 74% / Selenium 38%; US 73% / 65%; India 72% / 50%; Poland 64% / 57%; Canada Selenium leads 76% / Playwright 47%; South Africa Selenium 70% / Playwright 49%. In the US, REST Assured (69%) leads Postman (44%) in the API-tool subset.

**Local posting texts: 34 testing roles from the job-alert sample, read in full on 27 Nov 2026** (LinkedIn job pages; keyword mentions):

| Named in … of 34 | Skills / tools |
|---|---|
| 26 | CI/CD (incl. "pipeline") |
| 24 | API testing |
| 23 | Playwright |
| 20 | Python |
| 19 | Selenium |
| 16 | TypeScript |
| 15 | JavaScript; performance, load or stress testing (k6, JMeter, Gatling, Locust or the words) |
| 14 | Postman |
| 13 | Cypress; mobile app testing (iOS / Android); AI coding agents / AI-assisted testing |
| 11 | Java; Jenkins; Git |
| 10 | Jira |
| 9 | Wallet, payment or transaction flows |
| 8 | Appium; GitHub Actions; GitLab CI |
| 7 | C# / .NET; REST Assured; Docker; Azure |
| 6 | k6; message queues or event-driven systems |
| 5 | Kubernetes; idempotency |
| 4 | pytest |
| 3 | Concurrency or race conditions; SQL; AWS; flaky-test control |
| 2 | JMeter; Kafka; contract testing (Pact named by Hello Clever); Robot Framework; BDD / Cucumber |
| 1 | GCP; RabbitMQ; ISTQB |

**Codecaf, 552 QA / automation / SDET postings, collected 30–31 Oct 2026** ([source](https://codecaf.com/research/qa-hiring-statistics/)) — *annual edition, unchanged:* Selenium 47%, Playwright 46%, Cypress 33%; Python 43%, JavaScript 37%, Java 36%; API testing 68%; CI/CD or delivery tooling 60%; Postman 29%, RestAssured 19%; JMeter 16%, Appium 15%; ISTQB 9%; median stated experience minimum 4 years.

### B. Cloud platforms for QA roles

| Cloud | ROLIVA 20 Nov | ROLIVA 27 Nov | JobRemotely (remote listings, 1 Oct, *carried over*) | Codecaf (30–31 Oct) |
|---|---|---|---|---|
| **AWS** | 9% (170) | **8% (155)** | **53** of 687 (53 of the 64 that name a cloud) | 21% (117/552) |
| **Azure** | 11% (219) | **11% (212)** | 23 | 12% (67/552) |
| **GCP** | 3% (55) | **3% (57)** | 31 | 8% (44/552) |

Sources: [ROLIVA QA-engineer skill insights](https://rolivajobs.com/insights/skills/qa-engineer) (2,000 of 3,410 open QA and test engineer listings, 364 employers, 61 countries, as of 27 Nov 2026); [JobRemotely cloud-jobs analysis](https://jobremotely.io/blog/cloud-jobs-aws-azure-gcp); [Codecaf](https://codecaf.com/research/qa-hiring-statistics/).

**Read:**
- **Azure stays ahead of AWS on ROLIVA** (11% vs 8%). In local posting texts Azure (7) also leads AWS (3), on a small base. Codecaf's broader sample still puts AWS first.
- What every source still agrees on: **GCP is third**, and cloud is mentioned in a minority of QA listings.

Other ROLIVA signals (27 Nov): Python **24% (488)**, Agile **17%**, Java 13%, Jira 13%, SQL 11%, Excel 10%, JavaScript 8%, Scrum 8%, TypeScript 6%, Docker 5%, Kubernetes 5%, machine learning 3%, **LLM 3% (50)**, **Kafka 2% (33)**. Vietnam is **16 of the 2,000 listings (0.8%)**.

---

## 2. Must-have vs nice-to-have vs differentiator (mid → senior)

*Largely unchanged. Additions this week are marked.*

| Level | Must-have | Nice-to-have | Differentiator |
|---|---|---|---|
| Mid | One browser framework deeply (Playwright *or* Selenium), API testing, CI/CD basics, one language (Python or Java), Git, SQL | Cypress familiarity, Docker, JMeter/k6, cloud basics, Postman *and* REST Assured, mobile basics (Appium) | Contract tests, Testcontainers, flaky-test control in CI, cookie scoping by domain and path |
| Senior | Framework design, pipeline ownership, mentoring, risk-based strategy, working with AI coding agents and reviewing their output | Kubernetes, performance ownership, multi-cloud, mobile framework from scratch, **evaluating AI-native test platforms** *(new: named in a payments posting)* | Messaging/async testing, race and double-spend tests on transaction APIs, **webhook tests: duplicates, retries, out-of-order delivery, signature checks** *(new)*, parallel-safe suite design |

AssertHired's seniority mix (64% mid, 25% senior) and Jobpedia's experience bar (60% of roles stating years ask 5+) both say most advertised roles are mid-level and up. In the local sample, 24 of 48 testing cards are senior or lead.

---

## 3. Testing messaging and distributed systems: why it matters for a QE

- **Messaging is still not a standard QE requirement.** Kafka is 2% (33) of ROLIVA's QA listings, absent from the SDET top 15, and named in 2 of 34 local posting texts (Orient Software: "event driven architecture such as Kafka, service bus"; ISB Vietnam: "event-driven or real-time streaming architectures (e.g., Apache Kafka, RabbitMQ, WebSockets)").
- **Message queues and async flows appear more often as context:** 6 of 34 local texts mention message queues or event-driven systems (Colonial Surety, VORTECH ×2, the anonymous game-industry page, ISB Vietnam, Hello Clever).
- **New this week, on the payments side:** Hello Clever asks for "API testing patterns (Authentication, Idempotency, Retries, Webhooks) and validating asynchronous/event-driven architectures", mock services and stubs for "external PSPs, banking rails, and webhooks", and experience with "settlement, reconciliation, and transaction lifecycles". Its manual QA posting asks to "validate payment lifecycle/failure handling (refunds, settlement, retries, idempotency, webhooks)".
- **How to test a webhook consumer:** a payment provider retries deliveries (Stripe: up to three days with exponential back-off in live mode), may send the same event more than once, and does not guarantee order ([Stripe webhooks](https://docs.stripe.com/webhooks)). So the tests are: send the same event id twice and in parallel and expect **one** ledger movement; send `refunded` before `succeeded` and expect the final state `refunded`; send a bad signature or an old timestamp and expect a 4xx with **no** side effect. Worked example with Playwright and run results: [Testing payment webhooks: duplicates, out-of-order events and signatures](../../learning-material/qa-automation/Testing%20payment%20webhooks%20-%20duplicates%2C%20out-of-order%20events%20and%20signatures.md).
- Interview framing is unchanged (*carried over*): "How would you test a Kafka consumer?", duplicate charges, DLQ after a schema change, idempotency keys on POST.

---

## 4. Salary ranges

**No new ITviec salary survey this window.** The survey figures below are unchanged. Stated pay in this window's alerts is listed in "What changed this week".

### Vietnam local: ITviec 2025–2026 report, median **gross VND / month**
([ITviec report](https://itviec.com/report/vietnam-it-salary-and-recruitment-market), 1,839 respondents, surveyed May–Nov 2025)

| Role | <1 yr | 1–2 yr | 3–4 yr | 5–8 yr | >8 yr | Overall |
|---|---|---|---|---|---|---|
| Tester | 14.15M | 14.2M | 20.7M | 25.3M (≈$970) | 36.5M (≈$1,400) | 28.8M |
| QA-QC | – | 18M | 24.4M | 29.75M (≈$1,140) | 38.5M (≈$1,480) | 31.2M |

**Local stated bands, 21 – 27 Nov (job-alert sample):**

| Role | Company type | Stated pay | USD (est.) |
|---|---|---|---|
| Senior QA Automation Engineer (Python), hybrid HCMC, 4+ years | Recruiter | up to $2,500 gross / month | — |
| Senior Tester (Japanese-speaking, manual UI/API), Hà Nội, freelance board (same listing as previous window) | – | 20–45M VND | ≈$770–1,730 |

- **Read:** the recruiter band sits above the ITviec >8-year QA-QC median (≈$1,480) for a 4+ year role, and below the previous window's principal band ($2,500–3,200). One band is a data point, not a market rate.

### Remote / international
- **Jobpedia** (global QA-engineer roles that state pay): median **$120k/yr** (173 of 521 roles; was $121.7k on 163 of 487).
- Vendor and France figures (*carried over*): Second Talent senior QA automation remote from Vietnam **$3,900–5,600/mo**; ADC France median **€42,500/yr**.
- InterviewStack SDET board (*carried over* from Jul 2026 sample of 1,027 listings): median US base **$130,000** across 181 postings with US salary disclosed.
- **Read (est., unchanged):** a senior QA automation engineer working remotely from Vietnam lands around **$4–5.5K/mo**.

---

## 5. Typical interview formats and common topics

*Survey data carried over; no new interview-format survey was published this window.* CoderPad 2026 (about 650 respondents): technical discussion and live coding best predict the job (60% each); 46% of companies allow AI in interviews in some form, and when they do, catching and fixing AI mistakes (66%) is the top signal ([source](https://coderpad.io/survey-reports/coderpad-state-of-tech-hiring-2026/)). The SDET loop (coding screen → framework design → API testing practical → test strategy → behavioural) is unchanged.

**One stated loop this week:** Hello Clever's QA automation posting lists phone screen → virtual technical chat → **take-home exercise on automation framework skills** → meet the team.

Likely new practical questions after this week's postings:
- "The payment provider sends the same `payment.succeeded` event three times, two of them at once. What do you assert, and where?"
- "A refund event arrives before the payment-succeeded event. What should the final state be, and how do you test it?"
- "How do you stub a PSP so a webhook test is deterministic?"

---

## 6. Trends

**Cypress 16.4.0 (25 Nov 2026)** ([changelog](https://docs.cypress.io/app/references/changelog#16-4-0), [release](https://github.com/cypress-io/cypress/releases/tag/v16.4.0))
- `cypress open --headless` starts a session for `cypress tap` without taking focus from other apps, "such as when an AI coding agent runs your tests"; needs `--e2e` or `--component` and a browser. `cypress tap status` now reports config-load and spec-load errors.
- Faster start-up and lower memory in `cypress open` and `cypress run`; `cy.intercept()` stubs with a fixture or static body respond faster.
- Fixes a 16.0.0 regression where Chromium-based tests ran slower on pages loading large files; `forceHttp1: true` is no longer needed as a workaround.

**Selenium 4.54.0 (23 Nov 2026)** ([release](https://github.com/SeleniumHQ/selenium/releases/tag/selenium-4.54.0)) — a maintenance release six days after 4.53: Grid no longer fails Node status when a session stops mid-read; Java quits the Safari driver without an extra 10-second wait; Firefox picks its own BiDi websocket port in .NET, Python and JavaScript; Java removes the deprecated `Debug.getDebugLogLevel()`.

**Appium 4.0.0 (15 Nov 2026)**, then 4.0.1 (23 Nov) and 4.0.2 (27 Nov) ([4.0.0](https://github.com/appium/appium/releases/tag/appium%404.0.0), [4.0.2](https://github.com/appium/appium/releases/tag/appium%404.0.2))
- Breaking: server arguments `--callback-address`, `--callback-port`, `--debug-log-spacing`, `--strict-caps` and `--trace-dir` are removed; standard capability names match case-sensitively; a POST body must be a JSON object.
- `locale`, `language`, `autoWebview`, `orientation` and `udid` leave the standard capability constraints and must be defined by each driver.
- 4.0.2 cleans up sessions when a `createSession` plugin fails.
- **Implication:** Appium is named in 8 of 34 local postings; teams pinning 3.x should test their launch scripts and capabilities before moving.

**Patch release:** Playwright for Java 1.65.1 (19 Nov) rolls Chromium to 159.0.8154.6 ([release](https://github.com/microsoft/playwright-java/releases/tag/v1.65.1)). Playwright (Node) stays at 1.65.1 (13 Nov).

**Playwright vs Selenium: Playwright ahead again**
- AssertHired framework-named: Playwright 66% vs Selenium 61%; Playwright leads in the US, India, Poland and the UK; Selenium leads in Canada and South Africa.
- Skillenai SDET-title (refreshed, 61 postings): Playwright 42.6% vs Selenium 31.1%.
- Local posting texts: 23 vs 19 of 34. Codecaf mixed QA (unchanged): Selenium 47% vs Playwright 46%.
- **Implication:** pick one framework deeply; treat the other as transferable skill.

**AI in testing: platforms and AI products as test targets**
- Local posting texts: 13 of 34 name AI coding agents or AI-assisted test work (stricter term list; 15 of 33 last week). Wording includes "Validate AI-generated code and features" (Kake) and "Familiarity with AI coding assistants (e.g., Claude, Gemini, Codex/Copilot)" as a nice-to-have (Corsair).
- **AI-native test platforms named by product:** Hello Clever lists TesterArmy, mabl, Testim and BrowserStack AI features, to be combined with scripted Playwright / Selenium suites.
- **AI systems as the thing under test:** Galaxy FinX hires a QE for a shared AI-agent platform (Kubernetes, LangGraph, FastAPI, AWS Bedrock, LangFuse), separate from its AI tester role. GTEMAS's careers page asks QA engineers to build evaluation sets, check for hallucinations and regressions between model or prompt versions, and try prompt-injection cases ([source](https://gtemas.com/careers/qa-engineer)).
- Preferred-skill share for AI on Jobpedia stays **7%** (36 of 521); LLM is 3% of ROLIVA QA listings.

**Carried over from earlier reports:** manual QA contracting decline (Mentorpiece), Playwright ahead of Selenium in French QA ads, and the "boring five" (CI/CD, API testing, one language, Git, SQL) co-occurring in 60%+ of automation ads (TestDino).

**SDET career moves** ([Skillenai SDET](https://skillenai.com/data/role/software-development-engineer-in-test-sdet), unchanged): 43 same-role moves; **QA Automation Engineer → SDET 13 moves**, Software Engineer → SDET 9.

---

## 7. Recommended QA / automation skill priority list

*Order unchanged; changes are marked.*

1. **API testing in depth** (Playwright `request` + REST Assured, Postman for exploration): auth, schema, negative cases, idempotent methods, cookie scoping and query building, **signed webhook requests** *(new)*. *(24% of Jobpedia QA roles; 24 of 34 local posting texts.)*
2. **SQL + PostgreSQL transactions:** isolation levels, lost update and write skew, locking. Reproduce a race condition in a test, including a parallel-request burst with k6.
3. **Testcontainers** (Java and Go) with Postgres + Kafka + RabbitMQ in CI. *(CI/CD is required in 40% of Jobpedia QA roles.)*
4. **Testing async/event flows:** eventual consistency without sleep, duplicates, out-of-order, DLQ, contract tests (Pact), **payment webhooks with retries and replays** *(new)*.
5. **AI-in-testing literacy:** drive an agent to draft tests, then review every assertion against a requirement; know what AI-native platforms do and where scripted tests stay.
6. **Parallel-safe suites:** unique test data per test; named Playwright locks for shared resources; even Grid spread on Selenium 4.53+.
7. **One cloud, well.** AWS or Azure are both defensible; the lead flips between boards and weeks.

---

## 8. Key resources (official docs and primary sources)

1. **Stripe: receive events in your webhook endpoint** (retries, ordering, duplicates, signatures): https://docs.stripe.com/webhooks
2. **Cypress changelog 16.4.0**: https://docs.cypress.io/app/references/changelog#16-4-0
3. **Selenium 4.54.0 release notes**: https://github.com/SeleniumHQ/selenium/releases/tag/selenium-4.54.0
4. **Appium 4.0.0 release notes**: https://github.com/appium/appium/releases/tag/appium%404.0.0
5. **Playwright for Java 1.65.1 release notes**: https://github.com/microsoft/playwright-java/releases/tag/v1.65.1
6. **AssertHired QA job market (by country)**: https://www.asserthired.com/qa-jobs/market
7. **Jobpedia QA-engineer roles**: https://jobpedia.ai/roles/qa-engineer
8. **ROLIVA QA-engineer skill insights**: https://rolivajobs.com/insights/skills/qa-engineer
9. **Skillenai SDET role page**: https://skillenai.com/data/role/software-development-engineer-in-test-sdet

*(URLs checked for HTTP 200 on 27 Nov 2026. LinkedIn pages answer automated checks with 999 or 429.)*

---

## Caveats

- **Window overlap:** this report's alert window (20 – 27 Nov) overlaps the previous one on 20 Nov. Only alerts from 21 – 27 Nov are new; the 20 Nov alerts were counted last week.
- **Skillenai** refreshed on a smaller base (61 postings vs 81), so moves of a few points (e.g. Kubernetes +4.4, Cypress −6.3) may be sample noise.
- **ITviec** counts are a single-day snapshot of live tag pages; the comparison is with 13 Nov because the 20 Nov run could not reach the pages. **ITviec salaries** are self-reported 2025 survey medians.
- **ROLIVA** counts its own board and caps at 2,000 listings per role; its employer count rose from 356 to 364 this week.
- **AssertHired** shares are over the subset that name a tool in each table (28% of its tracked postings carry any tool tag), so they are not comparable one-to-one with Skillenai or Codecaf percentages of *all* postings. Its performance-tool subset is small (80 postings).
- **Local posting texts** are 34 LinkedIn pages for one city's alerts; 5 more postings could not be read (HTTP 429), and two cards came from Glassdoor and a freelance board. Counts are keyword mentions and include "nice to have" lines and employer blurbs. CI/CD counts the word "pipeline"; the AI count uses a strict list of agent and tool terms. Keyword lists are close to, but not guaranteed identical with, last week's, so small week-over-week moves in this table are indicative only.
- **One digest was cut off** after 10 job cards when read, so the card count may be slightly low.
- **Company types** come from each company's own description on its site or LinkedIn page. Outsourcing vs consultancy vs staffing is a judgement call for firms that do several (GTEMAS offers dedicated teams and recruitment; JDI offers recruitment, employer-of-record and venture services). "Client Company (Game Industry)" is marked unclear because its page has no description. Innovation in Technology Pty Ltd's type comes from its app listing and the EdTech product named in its own job ads.
- **Codecaf** is a two-day snapshot (30–31 Oct), English-language and ATS-heavy, refreshed annually.
- **JobRemotely, ADC, Mentorpiece, TestDino, InterviewStack and CoderPad** figures are carried over, not re-checked this week.
- **Jobpedia's** pay median covers only the 173 roles that state pay.
- **The VND→USD conversion** (≈26,000) is approximate.
- **Job-alert data** is alert titles, listed job cards and the linked public postings, from a sample of 18 alerts (15 new). Workflow / RPA automation, industrial "automation" (PLC), hardware module test and backend/developer alerts are excluded from the testing counts. No personal data, recruiter names or contacts are included.
