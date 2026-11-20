# Job Market 2026-11-20: QE / SDET / QA Automation

**Date:** 20 Nov 2026
**Purpose:** QA / QE automation market facts. This report covers QA, SDET and test automation roles only.
**Coverage:** weekly report. Window covered: **13 – 20 Nov 2026**. The previous report's window ended on 13 Nov, so **13 Nov overlaps**; only **14 – 20 Nov** is new in the job-alert sample.
**Builds on:** [job-market-2026-11-13.md](job-market-2026-11-13.md) (previous weekly report) and [qe-job-market-2026.md](qe-job-market-2026.md) (baseline, 21 Oct 2026).

> **How to read the numbers**
> - **Skillenai** = a job-posting index (90-day rolling window). Its SDET page **was refreshed this week** (90 days ending 19 Nov 2026, **81 postings**, down from 105), so shares can move on a smaller base.
> - **ITviec counts** = live listing counts from itviec.com tag pages. **Not refreshed this week**: the pages returned a bot check (HTTP 403) on 20 Nov 2026, so the 13 Nov counts are repeated and marked *carried over*.
> - **ROLIVA** = a job board that reads employers' careers pages. Counts are its 2,000 most recently confirmed QA and test engineer listings on 20 Nov 2026, so percentages describe *that board*, not the whole market. A mention is not necessarily a requirement.
> - **Jobpedia.AI** = a posting aggregator that publishes per-role skill shares over 90-day windows (here, 90 days to 20 Nov 2026).
> - **Codecaf** = a one-time count of 552 QA / SDET / automation postings collected 30–31 Oct 2026 (annual edition; unchanged).
> - **AssertHired** = a multi-country board of QA postings (here, last seen 15 Sep – 20 Nov 2026). Framework, language and tool shares are over the subset that name a tool in that table, not every posting.
> - **Local posting texts** = **33** full LinkedIn job pages for the testing roles in the job-alert sample, read on 20 Nov 2026. Counts are keyword mentions ("named in N of 33"), not weighted requirements.
> - **JobRemotely**, **AutomationDataCamp (ADC)**, **Mentorpiece** and **CoderPad** were not re-published this week; their figures are carried over from earlier reports and marked *carried over*.
> - Anything marked **(est.)** is an estimate or conversion made for this report. VND→USD uses about **26,000 VND/USD**, which is approximate.
> - **Job-alert sample** = aggregate counts from a sample of job-alert emails (LinkedIn digests and recommendations, one Glassdoor digest, one ITviec digest, one freelance-board digest), mostly job titles. No personal data, recruiter names or contacts are included.

---

## Top skills at a glance (20 Nov 2026)

**QE / automation — learn these first**
1. **CI/CD** — required in **40%** of QA-engineer roles ([Jobpedia](https://jobpedia.ai/roles/qa-engineer), 196 of 487); 59.3% of SDET postings ([Skillenai SDET](https://skillenai.com/data/role/software-development-engineer-in-test-sdet)); named in **19 of 33** local posting texts.
2. **Python and Java, now level** — AssertHired language subset: Python **47%**, Java **47%** (was 48% vs 45%) ([AssertHired](https://www.asserthired.com/qa-jobs/market)); Python 38% of Jobpedia QA roles (183 of 487) and 25% of ROLIVA's 2,000 QA listings; in local posting texts Python 13 and Java 12 of 33.
3. **Playwright and Selenium** — AssertHired framework-named subset: Playwright **65%** vs Selenium **60%** (was 66% vs 59%); Skillenai SDET 46.9% vs 33.3%; local posting texts **18 vs 18** of 33.
4. **API testing** — required in 25% of QA-engineer roles (Jobpedia, 121 of 487); named in **23 of 33** local posting texts. Postman (60%) and REST Assured (55%) lead the AssertHired API-tool subset.
5. **SQL** — required in 19% of QA-engineer roles (Jobpedia, 93 of 487); 12% of ROLIVA's QA listings.

**Rising this week:** working with AI coding agents (Claude Code, Copilot, Cursor, Codex) and checking what they generate is named in **15 of 33** local posting texts.

---

## What changed this week (13 Nov → 20 Nov 2026)

**Job-alert sample: 22 alerts dated 13 – 20 Nov**, of which **20 are new since the previous report** (14 – 20 Nov; 13 Nov overlaps). Digests came from LinkedIn job alerts and recommendations (17), one Glassdoor digest, one ITviec digest and one freelance-board digest. None came from a named recruiter.

**The changes worth acting on**

| # | Change | 13 Nov | 20 Nov | Read |
|---|---|---|---|---|
| 1 | **Selenium 4.53 shipped agent-facing features in a stable release** | Selenium 4.52 latest; MCP server only in nightly builds | **Selenium 4.53** (17 Nov): accessibility snapshots in Python (`driver.accessibility_snapshot()`) and JavaScript (`getAccessibilitySnapshot()`), in Classic and BiDi sessions; the MCP server for coding agents now lives in its own repo, SeleniumHQ/mcp; Grid spreads new sessions across Nodes again (since 4.36 it filled one Node first) ([blog](https://www.selenium.dev/blog/2026/selenium-4-53-released/), [release](https://github.com/SeleniumHQ/selenium/releases/tag/selenium-4.53.0)) | All three big browser tools now expose page structure to agents in stable builds. Selenium Grid users who saw uneven Node load on 4.36–4.52 get even spread back. |
| 2 | **AI-agent use moved from job titles into job requirements** | Two AI titles in the sample (spec-driven / AI-augmented testing) | **15 of 33** local posting texts name AI coding agents or AI-assisted test work; several ask candidates to *review* AI-generated tests for meaningful assertions (e.g. CODE LEAP for JTL-Software, Vinova, Billease, SCC Vietnam, NVIDIA) | Using agents is becoming a normal line in a senior QA posting. The skill being tested is judgement: does the generated test check a real requirement? |
| 3 | **Transaction-flow testing appeared in a local QA posting, with k6** | Messaging / transactions a differentiator; no local posting named them | VORTECH, Senior QA Automation Engineer: wallet debit, credit and rollback; idempotency and duplicate requests; concurrency and race conditions; mock partner services with timeouts, retries and partial failures; load and stress tests with **k6** | The repo's teaching focus now shows up word for word in a local ad. New note: [Concurrent debit tests with k6: lost updates and double spends](../../learning-material/qa-automation/Concurrent%20debit%20tests%20with%20k6%20-%20lost%20updates%20and%20double%20spends.md). |
| 4 | **Testing-titled share of alerts rose; first stated USD band from a LinkedIn card** | ~33% testing-titled; no stated pay | **10 of 20 (50%)** testing-titled subjects; Goelett Principal QA Engineer **$2,500–3,200/month** (hybrid, HCMC) | More of the sample is QA this week. One data point on pay, not a trend. |
| 5 | **Cloud mentions rose on ROLIVA** | Azure 9% (183), AWS 7% (140) | **Azure 11% (219), AWS 9% (170)**; Agile 16% → **19%** | Azure keeps the lead on this board. One cloud well is still enough. |

**Jobpedia QA-engineer roles, 13 Nov → 20 Nov** ([source](https://jobpedia.ai/roles/qa-engineer); 90-day windows):

| Signal | 13 Nov | 20 Nov |
|---|---|---|
| Roles counted | 437 | **487** |
| Employers | 355 | **396** |
| CI/CD required | 41% | **40%** |
| Test automation required | 38% | **38%** |
| Python required | 36% | **38%** |
| API testing required | 25% | **25%** |
| SQL required | 20% | **19%** |
| Remote | 81% | **81%** |
| Median stated pay | $120.1k | **$121.7k** (163 of 487 state pay) |

*Python now ties test automation (183 roles each) behind CI/CD; the sample grew by 50 roles.*

**ITviec Vietnam** — *carried over* from 13 Nov (pages not reachable this week): tester 57, automation test 40, playwright 12, sdet 10 ([tester](https://itviec.com/it-jobs/tester), [automation-test](https://itviec.com/it-jobs/automation-test), [playwright](https://itviec.com/it-jobs/playwright), [sdet](https://itviec.com/it-jobs/sdet)).

**Job-alert sample (aggregate, 13 – 20 Nov):**
- **22 alerts in 8 days**, almost all with Ho Chi Minh City locations (one freelance listing in Hà Nội).
- **10 of 20 new subjects (50%)** were testing-titled (QA / QC / Automation QA / Automation Test), up from ~33% in the previous report. Seven were backend or Java developer alerts and are out of scope here; one "MTE Software Engineer" alert (manufacturing test) is excluded.
- **47 testing job cards** across the digests, from **36 companies** (a few cards repeat one posting under two titles or IDs). Industrial PLC "automation" and hardware verification cards are excluded.
- **Seniority from titles:** 21 of 47 cards are senior, lead, principal or staff; 2 are middle; 3 are junior, early-career or intern; the rest give no level.
- **Work mode:** 3 cards are remote (Billease, Kake, Colonial Surety); the rest are on-site or hybrid in HCMC.
- **Stated pay this window:** Goelett Principal QA Engineer $2,500–3,200/month; ST Talent Automation Test Engineer (embedded / automotive client) "up to 35M" VND/month (≈$1,350, est.); STYL Solutions QA Engineer Intern 200–250 USD; bbv Vietnam AI Quality Engineer "up to 1,250 USD net" (same card as the previous window); freelance board: Senior Tester (Japanese-speaking, manual UI/API), Hà Nội, 20–45M VND (≈$770–1,730, est.).

---

## Hiring companies (job-alert sample, 14 – 20 Nov)

Each company is classified from its own website or its LinkedIn company page (the company block on its LinkedIn posting). "–" means the source does not state it. Types: **product** company; **consultancy or agency**; **outsourcing or offshore service**; **staffing or recruiter** posting for an unnamed client; **other** (bank, insurer, retailer, in-house IT); **unclear** where sources conflict.

| Company | Type | Industry | Size | HQ | Roles posted (testing cards) | Source |
|---|---|---|---|---|---|---|
| CODE LEAP | Outsourcing or offshore service (role for named client JTL-Software) | IT services, Germany–Vietnam dev teams | 51–200 | Germany / Vietnam | Senior QA Automation Engineer - DC34 (2 cards, incl. Shipping) | [LinkedIn](https://www.linkedin.com/company/codeleapag/), [site](https://codeleap.de/) |
| FPT Software | Outsourcing or offshore service | IT services | 10,001+ (33,000+ staff) | Vietnam | Automation Test (early career) | [LinkedIn](https://www.linkedin.com/company/fsoft-academy/), [site](https://fptsoftware.com/) |
| KMS Technology | Outsourcing or offshore service | Technology services | 1,001–5,000 | US (founded there) | Senior Full-stack Test Engineer (3 cards) | [LinkedIn](https://www.linkedin.com/company/kms-technology/) |
| NTT DATA | Outsourcing or offshore service | IT services and consulting | – | – | Senior Associate Software QA / Testing Engineer | [site](https://www.nttdata.com/global/en/) |
| DXC Technology | Outsourcing or offshore service | Enterprise IT services | – | – | Quality Engineering; QC automation; Software Test Engineer; Senior Automation Test; QA Engineer (ServiceNow) | [posting](https://www.linkedin.com/jobs/view/4453706316/), [site](https://dxc.com/) |
| Ban Vien Corporation | Outsourcing or offshore service | Software and embedded development, dedicated centres | 501–1,000 | – | Senior QC Engineer (Salesforce); Embedded Test Engineer | [LinkedIn](https://www.linkedin.com/company/ban-vien-corp/) |
| Kake | Outsourcing or offshore service (Teams as a Service) | IT services | 201–500 | – (remote-first) | Senior QA Engineer – Remote (contract) | [LinkedIn](https://www.linkedin.com/company/kake/) |
| Orient Software | Outsourcing or offshore service | Software development outsourcing | – | Vietnam | Senior Automation Test Engineer | [site](https://www.orientsoftware.com/) |
| L4 Studio | Outsourcing or offshore service | IT outsourcing, offshore development | 11–50 | Vietnam | Automation Test Engineer (Mobile & Web) | [LinkedIn](https://www.linkedin.com/company/l4studiovn/) |
| VORTECH | Outsourcing or offshore service | B2B software outsourcing (founded 2025) | 201–500 | – | Senior QA Automation Engineer | [LinkedIn](https://www.linkedin.com/company/vortech-entertainment/) |
| ELCA Vietnam | Outsourcing or offshore service | IT services and consulting | 201–500 (group 2,200+) | Switzerland (group) | QA Engineer | [LinkedIn](https://www.linkedin.com/company/elca-vietnam/), [site](https://www.elca.ch/) |
| Yoong Solutions | Outsourcing or offshore service | Staff augmentation and outsourcing | – | Vietnam | Manual QA Engineer (Windows) | [site](https://www.yoong.vn/) |
| Vinova | Consultancy or agency | Software development for clients | 201–500 | Singapore | Senior Automation QA | [LinkedIn](https://www.linkedin.com/company/vinova-sg/) |
| Silicon Stack | Consultancy or agency | Digital development, consulting and creative agency | 200+ staff | Australia | Middle Automation QA (API) | [LinkedIn](https://www.linkedin.com/company/silicon-stack/), [site](https://siliconstack.com.au/) |
| Astek Vietnam | Consultancy or agency | Engineering and technology consulting | 5,001–10,000 (group 7,500+) | France (group) | QA Automation Engineer; Senior QA Engineer | [LinkedIn](https://www.linkedin.com/company/astek-vietnam/) |
| Amaris Consulting | Consultancy or agency | Technology consulting | 7,600 people | – | Data Quality Control Analyst (Manual/Automation) | [site](https://amaris.com/) |
| bbv Vietnam | Consultancy or agency | Digital consulting, AI, software development | – | Switzerland (group) | AI Quality Engineer | [site](https://www.bbv.ch/en/) |
| Xspera | Consultancy or agency (with own platform) | Management consultancy | 11–50 | – | Senior QA-QC Engineer (posting about a year old) | [LinkedIn](https://www.linkedin.com/company/xspera-ltd/) |
| Billease | Product company | Consumer finance / buy now pay later | 201–500 | – | Senior QA Automation Engineer (mobile, remote) | [LinkedIn](https://www.linkedin.com/company/billease/) |
| Qualgo Technologies | Product company | Cybersecurity products (R&D centre) | 201–500 | – | Senior QA Engineer | [LinkedIn](https://www.linkedin.com/company/qualgotech/) |
| CyberLogitec | Product company | Shipping and logistics platforms | 501–1,000 | – | Automation QC Engineer (Playwright) | [LinkedIn](https://www.linkedin.com/company/cyberlogitec/) |
| NVIDIA | Product company | Computer hardware, AI computing | 10,001+ | – | SWQA Test Developer Engineer, SDET | [LinkedIn](https://www.linkedin.com/company/nvidia/) |
| Motorola Solutions | Product company | Public-safety and video security | – | – | QA Automation Engineer | [site](https://www.motorolasolutions.com/) |
| Corsair | Product company | Gaming hardware | 1,001–5,000 | – | Software QA Engineer | [LinkedIn](https://www.linkedin.com/company/corsair/) |
| Safetrust | Product company | Physical access software | 51–200 | – | Lead QA Automation Engineer | [LinkedIn](https://www.linkedin.com/company/safetrust-inc-/) |
| The Access Group | Product company | Business management software | – | – | Senior QA Engineer | [site](https://www.theaccessgroup.com/) |
| Goelett | Product company | Business travel booking (part of S4BT) | 201–500 | – | Principal QA Engineer (Manual + Automation) | [LinkedIn](https://www.linkedin.com/company/goelett/) |
| STYL Solutions | Product company | Payment terminals and IoT | – | Singapore | QA Engineer Intern | [site](https://styl.com.sg/about-us/) |
| ST Talent | Staffing or recruiter (unnamed client) | Recruitment services | 2–10 | – | Automation Test Engineer (embedded, automotive) | [LinkedIn](https://www.linkedin.com/company/sttalent/) |
| Manpower Vietnam | Staffing or recruiter (unnamed client) | Staffing and recruiting | 201–500 | – (ManpowerGroup subsidiary) | QA Automation Engineer (mobile) | [LinkedIn](https://www.linkedin.com/company/manpowervn/) |
| Talentia Consulting | Staffing or recruiter (unnamed client) | Business consulting and services | 2–10 | – | Senior QA Automation Engineer (Fintech / Digital Banking) | [LinkedIn](https://www.linkedin.com/company/talentia-consulting8686/) |
| SCC Vietnam | Other (service centre for a UK / French IT group) | IT services, group-internal | 201–500 | UK / France (group) | Middle QA Automation (Playwright); QA Tester Engineer (Automation); Software Test Engineer (Automation) | [LinkedIn](https://www.linkedin.com/company/scc-vn/) |
| Eurofins | Other (in-house IT delivery centre) | Life-sciences testing laboratories | – | – | Junior Test Automation Engineer | [posting](https://www.linkedin.com/jobs/view/4491145046/), [site](https://www.eurofins.com/) |
| Colonial Surety Company | Other (insurer) | Insurance | 11–50 | US | QA Engineer – Manual/Visual and automation (remote) | [LinkedIn](https://www.linkedin.com/company/colonial-surety-company/) |
| Zeya Labs AI | Other (in-house lab of an operating group) | AI and data for a diversified group | 11–50 | Vietnam | Senior QA Engineer (Automation) | [LinkedIn](https://www.linkedin.com/company/zeya-labs-ai/) |
| Zyneric | Unclear (own site describes custom AI and security work; ITviec lists "IT Product" and "outsourcing") | AI, cybersecurity, software | 1–50 (ITviec) | Vietnam | QC Automation (AI, QA QC, API) | [site](https://zyneric.com/about), [ITviec](https://itviec.com/it-jobs/qc-automation-ai-qa-qc-api-zyneric-0013) |

**Split by type (36 companies):** outsourcing or offshore **12 (33%)** · product **10 (28%)** · consultancy or agency **6 (17%)** · other **4 (11%)** · staffing or recruiter **3 (8%)** · unclear **1 (3%)**. By testing cards (47): outsourcing 20 (43%), product 10 (21%), consultancy 7 (15%), other 6 (13%), staffing 3 (6%), unclear 1 (2%).
**Week over week:** the previous report ([13 Nov](job-market-2026-11-13.md)) had no company-type split, so this is the **first split in the series**; next week's report compares against it.

**Read:** in this HCMC-heavy sample, a third of hiring companies sell delivery capacity (outsourcing and offshore centres) and they post the most cards (DXC 5, KMS 3). Product companies are close behind on company count, with one card each. Recruiter posts for unnamed clients are a small share.

---

## 0. Bottom line

1. **Same skill core.** CI/CD (40% of Jobpedia QA roles), Python and Java (level in AssertHired's subset), Playwright and Selenium, API testing and SQL.
2. **Playwright and Selenium are level in local postings** (18 of 33 each), while Playwright keeps a small lead in AssertHired's multi-country subset (65% vs 60%). Learn one deeply and expect to meet the other.
3. **Working with AI coding agents is now a common requirement** in local senior postings (15 of 33), with review of generated tests as the stated duty.
4. **Transaction-flow testing (wallets, idempotency, races, partner failures) appeared in a local QA ad**, together with k6.
5. **Pay:** Jobpedia median **$121.7k/yr**; one local principal band of **$2,500–3,200/month**; ITviec survey medians unchanged.

---

## 1. Most-demanded skills, with frequency signals

### A. QE / Automation / SDET

**Global: Skillenai, SDET title, 81 postings, 90 days to 19 Nov 2026** ([source](https://skillenai.com/data/role/software-development-engineer-in-test-sdet)) — *refreshed this week (was 105 postings to 5 Nov).*

| Skill | Share of postings | 5 Nov |
|---|---|---|
| CI/CD | 59.3% | 59.0% |
| Python | 54.3% | 53.3% |
| Playwright | 46.9% | 46.7% |
| Test automation | 39.5% | 38.1% |
| Java | 39.5% | 41.0% |
| Jenkins | 33.3% | 31.4% |
| Selenium | 33.3% | 34.3% |
| JavaScript | 33.3% | 36.2% |
| Cypress | 30.9% | 30.5% |
| API testing | **29.6%** | 23.8% |
| TypeScript | 28.4% | 28.6% |
| Git | 24.7% | – (not in top 15) |
| GitHub Actions | 24.7% | 22.9% |
| Kubernetes | 23.5% | 23.8% |
| Performance testing | 21.0% | 22.9% |

- Docker (21.9% on 5 Nov) dropped out of the top 15; Git entered. API testing gained most, on a smaller sample.
- **Messaging, Kafka and distributed systems are still absent from the SDET top 15.** For a QE they remain a **differentiator**, not a requirement.

**QA-engineer roles across all levels: Jobpedia.AI, 487 roles, 396 employers, 90 days to 20 Nov 2026** ([source](https://jobpedia.ai/roles/qa-engineer)) — required skills:

| Skill | Share | Skill | Share |
|---|---|---|---|
| CI/CD | 40% (196) | Agile | 21% (102) |
| Python | 38% (183) | JavaScript | 21% (102) |
| Test automation | 38% (183) | Git | 21% (101) |
| API testing | 25% (121) | Java | 19% (93) |
| TypeScript | 21% (104) | SQL | 19% (93) |

- Preferred skills: CI/CD 16%, test automation 10%, Docker 9%, Jira 9%, AWS 8%, Agile 8%, Git 7%, Python 7%, **AI 7%** (34 of 487), Kubernetes 6%.
- **81% remote.** 45% of roles stating years ask 5–7 years; 60% ask at least 5.
- 18% require a degree; another 23% accept experience instead; 55% don't mention one.

**AssertHired, 7,087 QA postings across 18 countries, last seen 15 Sep – 20 Nov 2026** ([source](https://www.asserthired.com/qa-jobs/market)):

| Table (subset that names a tool) | Result | 13 Nov |
|---|---|---|
| Browser frameworks (1,159 postings) | Playwright **65%**, Selenium **60%**, Cypress 14%, WebdriverIO 1.7% | 66% / 59% / 14% / 1.7% |
| Languages (1,437 postings) | Python **47%**, Java **47%**, JavaScript 18%, TypeScript 16%, C# 14% | 48% / 45% / 17% / 17% / 14% |
| API tools (264 postings) | Postman 60%, REST Assured 55% | 59% / 55% |
| Performance tools (76 postings) | JMeter 93%, Gatling 24%, k6 11% | 89% / 23% / 11% |
| Seniority (all 7,087) | Entry 3.1%, Mid 64%, Senior 24%, Lead/manager 8.7%; remote 4.1% | 3.1 / 64 / 24 / 8.8; 4.0% |

Country split for frameworks: UK Playwright 75% / Selenium 35%; US 70% / 64%; India 69% / 53%; Canada Selenium leads 76% / Playwright 49%. In the US, REST Assured (72%) leads Postman (48%) in the API-tool subset.

**Local posting texts: 33 testing roles from the job-alert sample, read in full on 20 Nov 2026** (LinkedIn job pages; keyword mentions):

| Named in … of 33 | Skills / tools |
|---|---|
| 23 | API testing |
| 19 | CI/CD |
| 18 | Playwright; Selenium |
| 15 | AI coding agents / AI-assisted testing; TypeScript |
| 13 | Cypress; JavaScript; Python |
| 12 | Java; Postman |
| 10 | Mobile app testing (iOS / Android) |
| 9 | Performance, load or stress testing (k6, JMeter, Gatling or the words) |
| 8 | REST Assured; Jira |
| 6 | Appium; C#; contract testing (Pact named by DXC) |
| 5 | Jenkins; SQL; Azure |
| 4 | Flaky-test control; ISTQB |
| 3 | k6; JMeter; Docker; Kubernetes; GitHub Actions; GitLab CI |
| 2 | Kafka; Robot Framework; ServiceNow ATF; AWS |
| 1 | Maestro; GitHub Spec Kit (spec-driven tests); idempotency |

**Codecaf, 552 QA / automation / SDET postings, collected 30–31 Oct 2026** ([source](https://codecaf.com/research/qa-hiring-statistics/)) — *annual edition, unchanged:* Selenium 47%, Playwright 46%, Cypress 33%; Python 43%, JavaScript 37%, Java 36%; API testing 68%; CI/CD or delivery tooling 60%; Postman 29%, RestAssured 19%; JMeter 16%, Appium 15%; ISTQB 9%; median stated experience minimum 4 years.

### B. Cloud platforms for QA roles

| Cloud | ROLIVA 13 Nov | ROLIVA 20 Nov | JobRemotely (remote listings, 1 Oct, *carried over*) | Codecaf (30–31 Oct) |
|---|---|---|---|---|
| **AWS** | 7% (140) | **9% (170)** | **53** of 687 (53 of the 64 that name a cloud) | 21% (117/552) |
| **Azure** | 9% (183) | **11% (219)** | 23 | 12% (67/552) |
| **GCP** | 3% (50) | **3% (55)** | 31 | 8% (44/552) |

Sources: [ROLIVA QA-engineer skill insights](https://rolivajobs.com/insights/skills/qa-engineer) (2,000 of 3,590 open QA and test engineer listings, 356 employers, 60 countries, as of 20 Nov 2026); [JobRemotely cloud-jobs analysis](https://jobremotely.io/blog/cloud-jobs-aws-azure-gcp); [Codecaf](https://codecaf.com/research/qa-hiring-statistics/).

**Read:**
- **Azure stays ahead of AWS on ROLIVA**, and both rose. Codecaf's broader sample still puts AWS first among postings that name a cloud. In local posting texts Azure (5) also leads AWS (2), on a tiny base.
- What every source still agrees on: **GCP is third**, and cloud is mentioned in a minority of QA listings.

Other ROLIVA signals (20 Nov): Python **25% (493)**, Agile **19%**, Java 13%, Jira 13%, SQL 12%, Excel 9%, JavaScript 9%, Scrum 8%, TypeScript 7%, Docker 6%, Kubernetes 5%, machine learning 3%, **LLM 2% (47)**, **Kafka 2% (38)**. Vietnam is **16 of the 2,000 listings (0.8%)**.

---

## 2. Must-have vs nice-to-have vs differentiator (mid → senior)

*Largely unchanged. Additions this week are marked.*

| Level | Must-have | Nice-to-have | Differentiator |
|---|---|---|---|
| Mid | One browser framework deeply (Playwright *or* Selenium), API testing, CI/CD basics, one language (Python or Java), Git, SQL | Cypress familiarity, Docker, JMeter/k6, cloud basics, Postman *and* REST Assured, mobile basics (Appium) | Contract tests, Testcontainers, flaky-test control in CI, cookie scoping by domain and path |
| Senior | Framework design, pipeline ownership, mentoring, risk-based strategy, **working with AI coding agents and reviewing their output** *(now common in local postings)* | Kubernetes, performance ownership, multi-cloud, mobile framework from scratch | Messaging/async testing, **race and double-spend tests on transaction APIs** *(new in a local ad)*, spec-driven review of AI-generated tests, parallel-safe suite design |

AssertHired's seniority mix (64% mid, 24% senior) and Jobpedia's experience bar (60% of roles stating years ask 5+) both say most advertised roles are mid-level and up. In the local sample, 21 of 47 testing cards are senior or above.

---

## 3. Testing messaging and distributed systems: why it matters for a QE

- **Messaging is still not a standard QE requirement.** Kafka is 2% (38) of ROLIVA's QA listings, absent from the SDET top 15, and named in 2 of 33 local posting texts (Talentia's fintech client, Orient Software).
- **New this week, on the transaction side:** one local senior QA automation posting lists wallet debit, credit and rollback, idempotency and duplicate requests, concurrency and race conditions, and mock partner services that time out, retry and fail part-way. That is the full set of edge cases in [Test design for messaging and transaction edge cases](../../learning-material/qa-automation/module-1/Test%20design%20for%20messaging%20and%20transaction%20edge%20cases.md).
- **How to test the race in one request burst:** k6 `http.batch()` sends parallel requests from one VU; raise `batchPerHost` (default 6) so all debits leave at once, then assert *final balance = start − accepted debits*, not only "balance ≥ 0". A lost update can end at a valid-looking 0. Worked example and run results: [Concurrent debit tests with k6: lost updates and double spends](../../learning-material/qa-automation/Concurrent%20debit%20tests%20with%20k6%20-%20lost%20updates%20and%20double%20spends.md).
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

**Local stated bands, 14 – 20 Nov (job-alert sample):**

| Role | Company type | Stated pay | USD (est.) |
|---|---|---|---|
| Principal QA Engineer (Manual + Automation, English), hybrid HCMC | Product | $2,500–3,200 / month | — |
| Automation Test Engineer (embedded, automotive client), HCMC | Recruiter | up to 35M VND / month | ≈$1,350 |
| Senior Tester (Japanese-speaking, manual UI/API), Hà Nội, freelance board | – | 20–45M VND | ≈$770–1,730 |
| AI Quality Engineer, HCMC (same card as previous window) | Consultancy | up to 1,250 USD net | — |
| QA Engineer Intern, HCMC | Product | 200–250 USD | — |

- **Read:** the principal band sits well above the ITviec >8-year QA-QC median (≈$1,480), for an English-speaking principal role at a company in a European business-travel group. One band is a data point, not a market rate.

### Remote / international
- **Jobpedia** (global QA-engineer roles that state pay): median **$121.7k/yr** (163 of 487 roles; was $120.1k).
- Vendor and France figures (*carried over*): Second Talent senior QA automation remote from Vietnam **$3,900–5,600/mo**; ADC France median **€42,500/yr**.
- InterviewStack SDET board (*carried over* from Jul 2026 sample of 1,027 listings): median US base **$130,000** across 181 postings with US salary disclosed.
- **Read (est., unchanged):** a senior QA automation engineer working remotely from Vietnam lands around **$4–5.5K/mo**.

---

## 5. Typical interview formats and common topics

*Carried over; no new interview-format survey was published this window.* CoderPad 2026 (about 650 respondents): technical discussion and live coding best predict the job (60% each); 46% of companies allow AI in interviews in some form, and when they do, catching and fixing AI mistakes (66%) is the top signal ([source](https://coderpad.io/survey-reports/coderpad-state-of-tech-hiring-2026/)). The SDET loop (coding screen → framework design → API testing practical → test strategy → behavioural) is unchanged.

Likely new practical questions after this week's postings:
- "Ten debits hit one wallet at the same time. What do you assert, and how do you make the race happen in a test?"
- "An AI agent wrote this test. Which assertions would you delete or change, and why?"

---

## 6. Trends

**Selenium 4.53 (17 Nov 2026)** ([blog](https://www.selenium.dev/blog/2026/selenium-4-53-released/), [release](https://github.com/SeleniumHQ/selenium/releases/tag/selenium-4.53.0))
- **Accessibility snapshots** of a page or element in Python (`driver.accessibility_snapshot()`, `element.accessibility_snapshot()`) and JavaScript (`getAccessibilitySnapshot()`), in Classic and BiDi sessions. Java, Ruby and .NET follow later.
- **MCP server** for coding agents started in this release and now lives in its own repository, SeleniumHQ/mcp.
- **Grid** spreads new sessions across Nodes again; since 4.36.0 the Distributor filled one Node before the next.
- Python: relative locators work from a `WebElement` and a `ShadowRoot`; `driver.webextension` deprecated. Java: faster JSON handling; `Response.status` removed.
- **Implication:** Selenium, Playwright (`"ai"` aria snapshots) and Cypress 16.3 (agent-friendly `cypress open`) all now ship agent-facing features in stable releases.

**Patch releases**
- Playwright 1.65.1 (13 Nov): fixes a 1.65 regression loading decorated classes with static fields when `useDefineForClassFields: false`, and one-column-off test locations under Bun 1.4.4+ ([release](https://github.com/microsoft/playwright/releases/tag/v1.65.1)). Playwright for Python 1.65.1 (11 Nov) bundles Node.js 26.13.1, a security release; 1.65.2 (14 Nov) rolls Chromium to 159.0.8154.6 ([1.65.1](https://github.com/microsoft/playwright-python/releases/tag/v1.65.1), [1.65.2](https://github.com/microsoft/playwright-python/releases/tag/v1.65.2)).
- k6 v2.4.0 (12 Nov): experimental tracing of runs, scenarios, VUs and iterations; credential-header redaction in HTTP and gRPC debug logs; built-in InfluxDB and Prometheus remote-write outputs deprecated ahead of v3 ([release](https://github.com/grafana/k6/releases/tag/v2.4.0)).

**Playwright vs Selenium: level in the local sample**
- AssertHired framework-named: Playwright 65% vs Selenium 60% (was 66% vs 59%); Playwright leads in the US, India, Poland and the UK; Selenium leads in Canada and South Africa.
- Skillenai SDET-title (refreshed): Playwright 46.9% vs Selenium 33.3%.
- Local posting texts: 18 vs 18 of 33. Codecaf mixed QA (unchanged): Selenium 47% vs Playwright 46%.
- **Implication:** pick one framework deeply; treat the other as transferable skill.

**AI in testing: from titles to duties**
- Local posting texts: 15 of 33 name AI coding agents or AI-assisted test work. Typical wording: use agents to draft scenarios and scripts, then "review generated tests for meaningful assertions" or "validate AI-generated outputs".
- Preferred-skill share for AI on Jobpedia stays **7%** (34 of 487), and LLM is 2% of ROLIVA QA listings. In global data it is still a plus; in this local sample it is turning into a normal senior duty.

**Carried over from earlier reports:** manual QA contracting decline (Mentorpiece), Playwright ahead of Selenium in French QA ads, and the "boring five" (CI/CD, API testing, one language, Git, SQL) co-occurring in 60%+ of automation ads (TestDino).

**SDET career moves** ([Skillenai SDET](https://skillenai.com/data/role/software-development-engineer-in-test-sdet), unchanged): 43 same-role moves; **QA Automation Engineer → SDET 13 moves**, Software Engineer → SDET 9.

---

## 7. Recommended QA / automation skill priority list

*Order unchanged; changes are marked.*

1. **API testing in depth** (Playwright `request` + REST Assured, Postman for exploration): auth, schema, negative cases, idempotent methods, cookie scoping and query building. *(25% of Jobpedia QA roles; 23 of 33 local posting texts.)*
2. **SQL + PostgreSQL transactions:** isolation levels, lost update and write skew, locking. Reproduce a race condition in a test, **including a parallel-request burst with k6** *(new)*.
3. **Testcontainers** (Java and Go) with Postgres + Kafka + RabbitMQ in CI. *(CI/CD is required in 40% of Jobpedia QA roles.)*
4. **Testing async/event flows:** eventual consistency without sleep, duplicates, out-of-order, DLQ, contract tests (Pact).
5. **AI-in-testing literacy** *(moved from titles into duties)*: drive an agent to draft tests, then review every assertion against a requirement.
6. **Parallel-safe suites:** unique test data per test; named Playwright locks for shared resources; even Grid spread on Selenium 4.53+.
7. **One cloud, well.** AWS or Azure are both defensible; the lead flips between boards and weeks.

---

## 8. Key resources (official docs and primary sources)

1. **Selenium 4.53 release blog**: https://www.selenium.dev/blog/2026/selenium-4-53-released/
2. **Selenium 4.53.0 release notes**: https://github.com/SeleniumHQ/selenium/releases/tag/selenium-4.53.0
3. **Playwright 1.65.1 release notes**: https://github.com/microsoft/playwright/releases/tag/v1.65.1
4. **k6 v2.4.0 release notes**: https://github.com/grafana/k6/releases/tag/v2.4.0
5. **k6 http.batch()**: https://grafana.com/docs/k6/latest/javascript-api/k6-http/batch/
6. **AssertHired QA job market (by country)**: https://www.asserthired.com/qa-jobs/market
7. **Jobpedia QA-engineer roles**: https://jobpedia.ai/roles/qa-engineer
8. **ROLIVA QA-engineer skill insights**: https://rolivajobs.com/insights/skills/qa-engineer
9. **Skillenai SDET role page**: https://skillenai.com/data/role/software-development-engineer-in-test-sdet

*(URLs checked for HTTP 200 on 20 Nov 2026. LinkedIn and ITviec pages answer automated checks with 999, 429 or 403.)*

---

## Caveats

- **Window overlap:** this report's alert window (13 – 20 Nov) overlaps the previous one on 13 Nov. Only alerts from 14 – 20 Nov are new.
- **Skillenai** refreshed on a smaller base (81 postings vs 105), so moves of a few points (e.g. API testing +5.8) may be sample noise.
- **ITviec counts** could not be refreshed (bot check, HTTP 403); the 13 Nov figures are repeated. **ITviec salaries** are self-reported 2025 survey medians.
- **ROLIVA** counts its own board and caps at 2,000 listings per role; its employer count rose from 347 to 356 this week.
- **AssertHired** shares are over the subset that name a tool in each table (28% of its tracked postings carry any tool tag), so they are not comparable one-to-one with Skillenai or Codecaf percentages of *all* postings. Its performance-tool subset is small (76 postings).
- **Local posting texts** are 33 LinkedIn pages for one city's alerts; counts are keyword mentions and include "nice to have" lines. Several pages carry the employer's own blurb, which can add words such as "AI" or "performance" that are not requirements; the AI count uses a stricter list of agent and tool terms.
- **Company types** come from each company's own description on its site or LinkedIn page. Outsourcing vs consultancy vs agency is a judgement call for firms that do both; Zyneric is marked unclear because its sources conflict. Sizes are LinkedIn bands unless stated otherwise.
- **Codecaf** is a two-day snapshot (30–31 Oct), English-language and ATS-heavy, refreshed annually.
- **JobRemotely, ADC, Mentorpiece, TestDino, InterviewStack and CoderPad** figures are carried over, not re-checked this week.
- **Jobpedia's** pay median covers only the 163 roles that state pay.
- **The VND→USD conversion** (≈26,000) is approximate.
- **Job-alert data** is alert titles, listed job cards and the linked public postings, from a sample of 22 alerts. Industrial "automation" (PLC), hardware verification and backend/developer alerts are excluded from the testing counts. No personal data, recruiter names or contacts are included.
