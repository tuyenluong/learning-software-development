# Job Market 2026: QE / SDET and Backend (Go · Spring Boot · Quarkus · Kafka · RabbitMQ)

**Prepared by:** Jake (Research) for Tuyen Luong and Jacob (Teacher)  **Date:** 21 Oct 2026
**Purpose:** Market facts to build a learning plan for QE → backend → solution architect. The core teaching focus is transaction and messaging problems.
**Builds on:** `software-tech-briefing-2026-10.md`, `jeremyluong-keyword-research.md`, `blog-post-briefs.md` (inbox aggregate).

> **How to read the numbers**
> - **Skillenai** = a job-posting index (90-day windows ending 14–20 Oct 2026). It shows how often a skill shows up in postings, not total hiring. Its SDET sample is small (140 postings), but its Backend Engineer sample is large (2,571).
> - **ITviec counts** = live listing counts I pulled from itviec.com tag pages on **21 Oct 2026**. They are a snapshot and move week to week.
> - **vitX** = a Vietnam hiring-pulse report built on ITviec/TopDev listings, 4 weeks to 15 Oct 2026. vitX is a staffing vendor.
> - **Second Talent** = a staffing vendor's rate cards. Its remote pay numbers are **vendor estimates**, not survey data.
> - Anything marked **(est.)** is my own estimate or conversion. VND→USD uses about **26,000 VND/USD**, which is approximate.
> - **Inbox (Jobs label)** = aggregate only. These are LinkedIn/Glassdoor alert digests, mostly job titles. No personal data is included, and nothing was sent or changed.

---

## 0. Bottom line (for Jacob)

1. **The QE market rewards an SDET who codes, not a tester.** CI/CD (57%), Python (51%), Playwright (47%), Java (36%) and API testing (21%) top SDET postings. AI shows up in job titles more and more.
2. **The backend market pays more.** In Vietnam, ITviec medians at 5–8 years are about **39.9M VND for backend vs 25.3M for Tester and 29.75M for QA-QC** (+35–58%). Remote vendor rate cards show a similar gap.
3. **Messaging and distributed systems are core backend skills, not extras.** "Distributed systems" is in **25%** of Backend Engineer postings and **Kafka in 18%**. Kafka has about **5× the postings of RabbitMQ**. Fintech employers (Wise, Barclays, Mastercard, Capital One, JPMorgan) lead Kafka hiring, which fits Tuyen's banking/fintech job alerts.
4. **Stack order: Spring Boot first, Go second, Quarkus last (concepts only).** Java/Spring is the largest stack in Vietnam and in enterprise and fintech. Go is the best remote and product-company bet. Quarkus demand is tiny, and in some datasets it's shrinking.
5. **Interviews are shifting** toward system design, real-world debugging and AI-allowed rounds. "Design X with retries, idempotency, outbox/saga, DLQ" is the standard place where messaging skill gets tested.

---

## 1. Most-demanded skills, with frequency signals

### A. QE / Automation / SDET

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
- **vitX (3 Sep census):** QA and testing had **72 of 469** engineering roles (about 15%), and QA ads stay up a median of **31 days**, tied with backend for the longest ([vitX Oct 2026](https://www.vitx.global/reports/vitx-vietnam-it-hiring-pulse-2026-10.pdf)).

**Inbox (Jobs label, aggregate):**
- About 50% of alerts are QA/automation roles. About 40% of QA titles are "Senior".
- Titles are converging on **SDET / Software Engineer in Test / Quality Engineer**.
- At least 8 QA titles name AI ("AI-Augmented Testing (Playwright, TypeScript)", "Software Engineer in Test (Agentic AI)", "QA Automation (MLOps)").
- About 10 roles are **banking/fintech**.

### B. Backend Engineer (Go / Java)

**Global: Skillenai, "Backend Engineer" title, 2,571 postings, 90 days to 14 Oct 2026** ([source](https://skillenai.com/data/role/backend-engineer))

| Skill | Share | Skill | Share |
|---|---|---|---|
| Python | 32.2% | Kafka | 17.9% |
| AWS | 31.8% | CI/CD | 17.8% |
| Kubernetes | 30.5% | TypeScript | 16.8% |
| Java | 26.6% | Observability | 16.6% |
| **Go** | **25.6%** | SQL | 15.9% |
| **Distributed systems** | **25.1%** | Redis | 15.1% |
| Docker | 21.2% | Microservices | 14.4% |
| PostgreSQL | 20.9% | | |

- **Top Backend Engineer posters:** Grafana Labs, GitLab, Wise, Stripe. Most of these are remote-friendly product companies.
- **CoderPad State of Tech Hiring 2026:** back-end is the #2 role hiring managers plan to fill (46%), after full-stack (49%). It is #3 hardest to fill (16%) ([CoderPad](https://coderpad.io/survey-reports/coderpad-state-of-tech-hiring-2026/)).

**Vietnam: ITviec live counts, 21 Oct 2026:** "java" 103, "backend developer" 92, "spring boot" 42, "golang" 37, "microservices" 28, "kafka" 14, "quarkus" no count shown (≈0) ([java](https://itviec.com/it-jobs/java), [golang](https://itviec.com/it-jobs/golang), [spring-boot](https://itviec.com/it-jobs/spring-boot), [kafka](https://itviec.com/it-jobs/kafka)).
- **vitX:**
  - Backend is the largest discipline: **144 of 469** engineering roles (30.7%).
  - Stacks named in job titles: **Java 52**, Python 43, React 35, .NET 26, AWS 23, **Go 22**.
  - **Banks, fintechs and securities firms posted 19%** of roles.
  - **45.4% of roles are senior, lead or manager**, and only 5.4% are junior.
  - **Remote is only 2.8%** of Vietnam-board roles.

  ([vitX](https://www.vitx.global/reports/vitx-vietnam-it-hiring-pulse-2026-10.pdf))
- **TopDev 2024–25:** Spring Boot is the #1 Java framework at 45.2% ([TopDev](https://topdev.vn/download-report)).

**Inbox:**
- About 40% of alerts are backend, mostly from the saved search **"remote Backend java"** (Java/Spring, AWS/Azure, API). About 19 of 41 backend alerts are remote.
- Keyword hits in alert bodies over 6 months: Spring Boot 3 threads, Go-related 6 (ambiguous match), and **Kafka, RabbitMQ and Quarkus 0**. Alerts are title digests, so this reflects stack names in titles only.

---

## 2. Must-have vs nice-to-have vs differentiator (mid → senior)

*This synthesis is my own, based on the frequencies above and the interview sources in §6.*

### A. QE / SDET

| Level | Must-have | Nice-to-have | Differentiator (gets the remote or senior offer) |
|---|---|---|---|
| **Mid** | One language done properly (TS or Java/Python); Playwright (or Selenium for Java shops); API testing (REST, auth, schema, negative cases); Git; CI (GitHub Actions/Jenkins); test design techniques; SQL basics | Docker; Cypress/Selenium migration; performance basics (k6/JMeter); mobile (Appium) | Contract testing (Pact); Testcontainers; testing async/event flows |
| **Senior** | Framework architecture (fixtures vs POM, data isolation, parallelism and sharding, reporting); flaky-test strategy; test strategy and risk-based planning; CI at scale; mentoring | Kubernetes test grids; observability (OTel traces in tests); security testing basics | **Backend-aware QE:** testing Kafka/RabbitMQ flows, idempotency, retries, DLQs, eventual consistency, DB isolation/race conditions; **AI-in-testing** (Playwright agents/MCP, evaluating LLM features); quality metrics with DORA language |

### B. Backend (Go / Spring Boot)

| Level | Must-have | Nice-to-have | Differentiator |
|---|---|---|---|
| **Mid** | Java 21/25 + Spring Boot 3/4 **or** Go; REST API design; SQL + PostgreSQL (indexes, transactions); Docker; unit and integration tests (JUnit/Testcontainers or Go testing); Git and CI; one cloud (AWS is most common) | Kafka *or* RabbitMQ producer/consumer basics; Redis; Kubernetes basics; gRPC | Strong testing of your own services (Tuyen's natural edge) |
| **Senior** | **Distributed systems:** microservices boundaries, messaging (Kafka), retries, timeouts, idempotency, outbox/saga, consistency trade-offs; observability (logs, metrics, traces); performance and concurrency; system design interviews; on-call/incident thinking | Event sourcing/CQRS; Kafka Streams/Connect/Debezium (CDC); K8s operations; security (OAuth2/OIDC) | **Proving correctness under failure:** fault injection, chaos tests, reproducing duplicate/out-of-order delivery; domain depth in payments/fintech; writing ADRs and design docs (the bridge to architect) |

---

## 3. Messaging, transactions and distributed systems: how often, and how tested

### Frequency signals
| Signal | Number | Source |
|---|---|---|
| Kafka postings (all roles, 90d) | **7,777** (flat, +0.1% vs prior 4 weeks) | [Skillenai Kafka](https://skillenai.com/data/skill/kafka) |
| RabbitMQ postings (90d) | **1,486** (−4.5%) → Kafka has about **5.2×** RabbitMQ (est.) | [Skillenai RabbitMQ](https://skillenai.com/data/skill/rabbitmq) |
| Event-driven architecture postings (90d) | **1,993** (+4.5%) | [Skillenai EDA](https://skillenai.com/data/skill/event-driven-architecture) |
| Microservices postings (90d) | **9,747** (+0.7%) | [Skillenai microservices](https://skillenai.com/data/skill/microservices) |
| Share of Backend Engineer postings | Distributed systems 25.1%, Kafka 17.9%, microservices 14.4%, Redis 15.1%, observability 16.6% | [Skillenai Backend](https://skillenai.com/data/role/backend-engineer) |
| Kafka in Java backend titles | 29.0% of "Java Backend Engineer", 27.8% of "Java Backend Developer" | [Skillenai Kafka](https://skillenai.com/data/skill/kafka) |
| RabbitMQ in backend titles | 14.3% "Back-End Engineer", 8.8% "Backend Software Engineer"; often paired *with* Kafka | [Skillenai RabbitMQ](https://skillenai.com/data/skill/rabbitmq) |
| Top Kafka employers | Wise, Cisco, CrowdStrike, **Barclays, Mastercard**, Databricks, **Capital One, JPMorgan** | [Skillenai Kafka](https://skillenai.com/data/skill/kafka) |
| Vietnam | ITviec "kafka" 14 and "microservices" 28 live jobs (vs Java 103) | ITviec, 21 Oct 2026 |

**Read (my interpretation):**
- **Kafka is the messaging skill to lead with.** RabbitMQ is a common second broker, especially in .NET/Python shops and integrations work.
- About **1 in 4 backend postings asks for distributed-systems skill outright**, and senior interviews test it whether or not the posting names it.
- **For QE roles, messaging is not a standard requirement**, which is exactly why it's a differentiator for a QE who wants to move toward backend.

### How it's tested in interviews
*Sources: interview-prep sites and hiring surveys. The topic lists are secondary-source consensus, not employer data.*

1. **System design round.** This is the main place messaging gets tested (system design appears in 38% of technical tests per [CoderPad 2026](https://coderpad.io/survey-reports/coderpad-state-of-tech-hiring-2026/)). Typical prompts:
   - "Design order checkout / payment / wallet transfer across services."
   - "Design a notification system."

   Interviewers expect:
   - local transactions with **no 2PC**
   - **transactional outbox** to publish reliably
   - **saga** (orchestration vs choreography) with compensations
   - **retries with backoff + timeouts**
   - **idempotent consumers** (dedupe keys)
   - **DLQ** for poison messages

   ([SystemRound saga pattern](https://thesystemround.com/learn/patterns/event-driven-saga), [InterviewKata workflows/sagas/outbox](https://interviewkata.com/system-design/modules/22-workflows-sagas.html))
2. **Kafka deep-dive questions.** Common topics:
   - partitions and ordering
   - consumer groups and **rebalancing**
   - offset commit timing (at-most-once vs at-least-once)
   - idempotent producer, transactions and `read_committed`
   - why "exactly-once" only covers Kafka-to-Kafka, so external DB/API side effects still need idempotency
   - **consumer lag**: causes and how to monitor it

   ([golinuxcloud Kafka Qs](https://www.golinuxcloud.com/kafka-interview-questions/), [Kafka docs: semantics](https://kafka.apache.org/documentation/#semantics))
3. **Database and concurrency questions.** Common topics:
   - isolation levels and their anomalies (lost update, write skew)
   - optimistic vs pessimistic locking
   - "two requests withdraw from the same account at once"
   - idempotency keys on POST

   ([PostgreSQL isolation docs](https://www.postgresql.org/docs/current/transaction-iso.html))
4. **Debugging/scenario rounds (rising):**
   - "Users get charged twice."
   - "Consumer lag keeps growing after a deploy."
   - "Messages end up in the DLQ after a schema change."

   Real-world scenario simulations are in 38% of tests, and debugging exercises in 19% ([CoderPad 2026](https://coderpad.io/survey-reports/coderpad-state-of-tech-hiring-2026/)).
5. **For SDET loops**, the same topics come up as **"how would you test it"**:
   - test strategy for an event-driven flow
   - contract tests between services
   - Testcontainers with a real broker
   - asserting eventual consistency without `sleep`
   - fault injection

**This maps directly onto Jacob's core focus.** Each lesson can follow "what breaks → how to reproduce/test (QE) → how to fix (backend) → how to design it out (architect)". That is the same three angles interviews probe.

---

## 4. Go vs Spring Boot vs Quarkus

| Signal | Go | Spring Boot | Quarkus |
|---|---|---|---|
| Global postings, 90d (Skillenai) | **13,887** (+4.0%) ¹ | **4,673** (+3.4%) | no Skillenai page; Alion lists **91–152** live roles ([Alion](https://alion.io/jobs/quarkus)) |
| Share of Backend Engineer postings | **25.6%** | (Java 26.6%) | n/a |
| Top employers | Capital One, Cisco, SpaceX, **Stripe**, CrowdStrike, Cloudflare, **Grab** | **Mastercard, Barclays, Wise, JPMorgan**, Capco | Citi, Sopra Steria, Red Hat consulting, defense/gov (OpenShift shops) |
| SO 2026 usage | Go language **16.5%** | Spring Boot **12.8%** of web-framework users (Java 27.6%) | **0.3%** ² |
| Java-org surveys | n/a | Azul 2025: **42%** of orgs use Spring Boot for Java microservices; Vaadin 2025: 86% | Azul 2025: **7%**; Jakarta EE 2025 survey: Quarkus runtime use **declining** |
| UK permanent jobs (ITJobsWatch, 6 mo) | n/a | n/a | **2** (vs 15 a year ago) ([ITJobsWatch](https://www.itjobswatch.co.uk/jobs/uk/quarkus.do)) |
| Vietnam ITviec (21 Oct) | **37** | **42** (Java 103) | ≈0 |
| Vietnam job titles (vitX) | **22** | Java **52** | n/a |
| Vietnam remote pay premium | Second Talent: Go seniors **+10–20%** over the backend range (vendor est.) | Baseline ("Java remains highest-demand backend language in Vietnam") | n/a |

¹ Skillenai resolves skills to a canonical entity, but "Go" is an ambiguous word, so treat its count as an upper bound.
² Quarkus may not have been a listed answer option in SO 2026, so 0.3% likely understates it. It's still far smaller than Spring.

Sources: [Skillenai Go](https://skillenai.com/data/skill/go), [Skillenai Spring Boot](https://skillenai.com/data/skill/spring-boot), [SO 2026 languages](https://survey.stackoverflow.co/2026/technology/data/languages), [SO 2026 web frameworks](https://survey.stackoverflow.co/2026/technology/data/web-framework), [Azul State of Java 2025](https://www.qbssoftware.com/wp-content/uploads/2025/04/Azul-report-State-of-Java-2025.pdf), [Jakarta EE 2025 survey](https://outreach.eclipse.foundation/hubfs/2025%20Jakarta%20EE%20Developer%20Survey%20Report.pdf), [Second Talent Vietnam](https://www.secondtalent.com/resources/true-cost-outsource-software-development-vietnam/).

**Verdict:**
- **Spring Boot is the primary stack.** It has the biggest Vietnam demand, it dominates bank and fintech hiring, it matches Tuyen's saved "remote Backend java" search, and Java skill carries over from Selenium/Java test work.
- **Go is the second language, aimed at remote and global product companies** (Stripe, Cloudflare, Grab, Grafana-type employers). It also wins on platform/infra work, and Kafka/K8s tooling is often written in Go.
- **Quarkus gets concepts only.** Teach it as a 1–2 lesson comparison (build-time DI, native image, MicroProfile Reactive Messaging, Dev Services). Only go deeper if a target employer uses Red Hat/OpenShift. Most Spring knowledge carries over.

---

## 5. Salary ranges

### Vietnam local: ITviec 2025–2026 report, median **gross VND / month**
([ITviec report](https://itviec.com/report/vietnam-it-salary-and-recruitment-market), 1,839 respondents, surveyed May–Nov 2025)

| Role | <1 yr | 1–2 yr | 3–4 yr | 5–8 yr | >8 yr | Overall |
|---|---|---|---|---|---|---|
| Tester | 14.15M | 14.2M | 20.7M | 25.3M (≈$970) | 36.5M (≈$1,400) | 28.8M |
| QA-QC | – | 18M | 24.4M | 29.75M (≈$1,140) | 38.5M (≈$1,480) | 31.2M |
| **Back-end Developer** | 12.4M | 25.35M | 30.1M | **39.9M (≈$1,530)** | **54.9M (≈$2,110)** | 37.8M |
| Tech Lead | – | 45.3M | 53.85M | – | 68.45M | 51.8M (≈$1,990) |
| Project Leader/PM | 17.2M | 29.85M | 48.4M | 58.45M | – | 50.1M |

- **Go (Second Talent, vendor):** junior 20–35M, mid 35–55M, **senior 55–80M**, lead/architect 80–140M VND/month ([source](https://www.secondtalent.com/developer-rate-card/golang-developer-vietnam/)). This runs higher than ITviec's general backend medians, so treat it as an upper-market estimate.
- **Inbox anecdotes (posted ranges in alert titles):** a QA Automation role "up to $2.1K/month", and a "Senior Java, good English, remote, up to 55M gross" role. Both are consistent with the medians above.
- An industry blog citing ITviec says automation and AI skills add about +20–40% over manual testing at the same seniority ([itlearn.vn](https://itlearn.vn/blog/luong-tester)). This is secondary and directional.

### Remote / international (Vietnam-based engineer, USD / month)
| Source | QA Automation | Backend (Java/Go/Node/Python) | Notes |
|---|---|---|---|
| [Second Talent, Vietnam rates 2026](https://www.secondtalent.com/resources/true-cost-outsource-software-development-vietnam/) (vendor) | Mid **$2,500–3,900** · Senior **$3,900–5,600** · Lead $5,600–7,700 | Mid **$3,400–4,900** · Senior **$4,900–7,000** · Lead/Architect **$7,000–9,800** | Go/.NET seniors +10–20%; "remote rates are 40–100% higher than local salaries"; English is the biggest differentiator |
| [Second Talent APAC benchmark, Oct 2026](https://www.secondtalent.com/apac-salary-benchmark/) (vendor) | n/a | Vietnam all-roles median: mid **$3,100**, senior **$4,500** (IQR $4,300–5,500), lead $5,300 | Remote contractor rates |
| Live listing ([Jobstore](https://www.jobstore.com/vn/job/l23019796/senior-java-developer-remote-job)) | n/a | Senior Java remote contract **$30–90/hr** (VND 60–110M/mo) | One listing, anecdotal |
| Global reference ([SO 2026 comp](https://survey.stackoverflow.co/2026/work/data/compensation)) | QA/test median not published (<100 resp.) | Back-end median **$85,296/yr** globally; Architect **$102,355/yr** | Mostly US/EU respondents, not a Vietnam remote rate |
| Freelance QA consulting (from keyword report) | Audits **$1,000–2,400**, migrations from **€4,500**, retainers **~$1,800/mo** | n/a | Solo consultants' public pricing |

**Read (est.):**
- A senior QA automation engineer working remotely from Vietnam lands around **$4–5.5K/mo**.
- A senior backend engineer lands around **$5–7K/mo**, so the backend premium is about **+25–35%** (est.).
- Architect/lead roles reach **$7–10K/mo**.
- Locally, the backend move is worth about **+35–55%** at 5–8+ years.

---

## 6. Typical interview formats and common topics

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

**Backend loop (mid/senior):** recruiter → coding (DSA, or a practical service task) → **system design** (senior: often 2 rounds) → **domain/deep-dive** (Spring internals or Go concurrency, DB/transactions, Kafka) → behavioral/leadership. Common topics:
- **Spring:** DI and bean lifecycle; `@Transactional` propagation and pitfalls (self-invocation, rollback rules); JPA N+1; connection pools; virtual threads (Java 21+).
- **Go:** goroutines, channels, `context` cancellation/timeouts, races (`-race`), worker pools, error handling.
- **Data:** indexes, isolation levels, locking, migrations.
- **Messaging:** see §3. Ordering, lag, rebalancing, delivery semantics, outbox/saga, DLQ, idempotency.
- **Ops:** observability, rate limiting, circuit breakers, retries with jitter.

**Vietnam specifics (est., from market structure):** outsourcing and service firms (about 36 international IT services firms per vitX) often run a shorter loop: tech interview + English check + sometimes a test. Foreign in-house centres (57% senior roles) and remote employers run fuller loops with system design. **English is a gate** for remote roles.

---

## 7. Trends

**AI in testing**
- **World Quality Report 2025-26:** 43% of organisations are experimenting with GenAI in QA, but only **15% have scaled it** enterprise-wide. **GenAI is the top-ranked skill for quality engineers (63%)**, ahead of core QE skills (60%). Synthetic test data use rose from 14% to 25% ([Capgemini WQR](https://www.capgemini.com/insights/research-library/world-quality-report-2025-26/)). OpenText's press release also reports an average 19% productivity gain, with a third seeing minimal gains; I couldn't re-verify this because the fetch was blocked ([OpenText](https://www.opentext.com/about/press-releases/world-quality-report-2025-ai-adoption-surges-in-quality-engineering-but-enterprise-level-scaling-remains-elusive)).
- **SO 2026:** 58.1% of AI users use it for writing or improving tests. 73% use coding agents daily, but only 48% trust output that isn't easy to check ([SO 2026 AI](https://survey.stackoverflow.co/2026/ai)).
- **Framework-native agents are now free:** Playwright Test Agents (planner, generator, healer) and MCP, Cypress `cy.prompt`, WebdriverIO v10 (see `software-tech-briefing-2026-10.md`).
- **Vietnam:** 13.7% of ITviec IT roles ask for AI, up from 11.3% in Aug ([vitX](https://www.vitx.global/reports/vitx-vietnam-it-hiring-pulse-2026-10.pdf)). The inbox shows at least 8 QA titles naming AI.
- **Implication:** the QE value shifts to **verifying AI-written code and tests**: oracles, contracts, determinism, and evaluating LLM features.

**AI-assisted backend dev**
- CoderPad: 82% of developers find GenAI useful, and 54% would lose ≥10% productivity without it.
- Developers expect **system design and debugging to grow in importance** and writing new code to shrink.
- Hiring budgets are expected to rise at 53% of companies (vs 37% in 2025).
- **Implication:** distributed-systems judgment (the messaging/transaction focus) is the part AI can't do for you. It is also what interviews increasingly test.

**QE → backend moves**
- Skillenai career flows show SDETs mostly move to **other SDET roles** (46 same-role moves). Only 2 observed SDET→Software Engineer moves vs 10 SE→SDET ([Skillenai SDET](https://skillenai.com/data/role/software-development-engineer-in-test-sdet)). Backend Engineer hires come mainly from Software Engineer (88 moves) ([Skillenai Backend](https://skillenai.com/data/role/backend-engineer)).
- **Read:** the switch is uncommon, so it needs deliberate proof: a deployed service, production-quality code, and system-design fluency.
- Practitioner guides suggest an **internal transfer** first, and **3–6 months** of focused work if you already write strong automation code (12–18 months if not) ([SeekerScore](https://www.seekerscore.com/routes/qa-engineer-to-software-engineer), [Codefarm](https://codefarm.in/blog/software-engineering/qa-to-developer-transition)). These are secondary sources, so treat the timelines as estimates.
- A good bridge role is **"backend-focused SDET / Quality Engineer – Core Services"**, which already appears in Tuyen's alerts.

**Path toward solution architect**
- SO 2026: "Architect, software or solutions" is 7% of respondents, with a **$102K** global median, the highest IC developer role after cloud infra.
- ITviec Vietnam: Tech Lead median **51.8M VND**, PM/PL 50.1M.
- CoderPad: software architect is in 15% of hiring plans.
- Architects are expected to make and document trade-offs (ADRs), handle reliability and scaling, cost, security, and cross-team integration. Messaging and consistency design is central to that.

---

## 8. Recommended skill priority list (QE → backend → architect)

*Time estimates assume about 6–8 hrs/week and are my estimates. Jacob should confirm Tuyen's actual weekly time.*

### Phase 1: Strengthen the QE base and become a "backend-aware SDET" (months 0–3)
1. **API testing in depth** (Playwright `request` + REST Assured in Java): auth, schema, negative cases, idempotent methods. *(21% of SDET postings; it's the bridge skill.)*
2. **SQL + PostgreSQL transactions:** isolation levels, lost update and write skew, locking. Reproduce a race condition in a test. *(Core focus.)*
3. **Testcontainers** (Java and Go) with Postgres + Kafka + RabbitMQ in CI (GitHub Actions). *(CI/CD is 57% of SDET postings.)*
4. **Testing async/event flows:** asserting eventual consistency (polling and awaitility, not sleep), duplicate and out-of-order injection, DLQ assertions, contract tests (Pact). *(Differentiator.)*
5. **AI-in-testing literacy:** Playwright agents/MCP, reviewing AI-generated tests. *(AI titles are rising.)*

### Phase 2: Backend engineer on Spring Boot (months 3–9)
6. **Java 21/25 + Spring Boot 3/4:** REST, validation, JPA, `@Transactional` semantics and pitfalls, error handling, security (OAuth2/JWT).
7. **Kafka with Spring for Apache Kafka:**
   - producers and consumers, keys and partitions, ordering
   - consumer groups and rebalancing
   - offset commits and delivery semantics, idempotent producer and transactions
   - retries/backoff, **DLT (dead-letter topic)**
   - **consumer lag** monitoring
8. **Reliability patterns:** idempotency keys and dedupe tables, **transactional outbox** (+ Debezium CDC as an option), **saga** (orchestration vs choreography, compensations), timeouts and circuit breakers (Resilience4j).
9. **RabbitMQ:** exchanges, routing, acks, publisher confirms, DLX, retry queues, quorum queues. Compare it with Kafka: when to use each.
10. **Observability:** structured logs, metrics, OTel traces across async hops; trace a message end-to-end.
11. **Portfolio proof:** one deployed "payments/orders" service set (Spring) with an outbox + saga + DLQ and a **failure-injection test suite**. This is the asset that gets the backend interview.

### Phase 3: Go as second language and remote-market reach (months 9–12)
12. **Go:** concurrency (goroutines, channels, `context`), `-race`, `net/http`/chi or gin, `database/sql`/pgx, Go testing. Port one service from Phase 2, with a Kafka client (franz-go or confluent-kafka-go) and an idempotent consumer.
13. **Quarkus (1–2 lessons):** Dev Services, SmallRye Reactive Messaging (Kafka), native image. Compare it with Spring and stop unless an employer needs it.

### Phase 4: Toward solution architect (12 months+)
14. **System design practice:** payments, wallet, notifications, inventory, rate limiter. Each one must cover consistency, messaging and failure modes.
15. **Distributed-systems theory:** DDIA concepts (replication, partitioning, consistency models, exactly-once myths), Jepsen consistency models.
16. **Architecture communication:** ADRs, C4 diagrams, trade-off write-ups, cost and SLOs. Kubernetes and cloud basics (AWS is 3.3× Azure in Vietnam titles per vitX).

**Why this order:**
- It keeps Tuyen employable as a senior SDET the whole way, since Phase 1 skills raise QE pay too.
- It hits the largest backend market first (Java/Spring in Vietnam and fintech).
- It adds Go for the remote premium.
- The messaging and transaction core runs through every phase, as Jacob's brief requires.

---

## 9. Key resources (official docs and courses)

1. **Confluent Developer courses** (free): Kafka 101, Kafka internals, transactions and EOS: https://developer.confluent.io/courses/
2. **Apache Kafka docs: message delivery semantics**: https://kafka.apache.org/documentation/#semantics
3. **Spring for Apache Kafka reference** (retries, DLT, transactions): https://docs.spring.io/spring-kafka/reference/
4. **RabbitMQ: reliability guide + dead-letter exchanges**: https://www.rabbitmq.com/docs/reliability · https://www.rabbitmq.com/docs/dlx
5. **microservices.io (Chris Richardson): transactional outbox and saga**: https://microservices.io/patterns/data/transactional-outbox.html · https://microservices.io/patterns/data/saga.html
6. **PostgreSQL: transaction isolation**: https://www.postgresql.org/docs/current/transaction-iso.html
7. **Testcontainers guides** (Java/Go, Kafka/Postgres/RabbitMQ): https://testcontainers.com/guides/
8. **Designing Data-Intensive Applications** (Kleppmann), the architect-track book: https://dataintensive.net/

Optional extras: [A Tour of Go](https://go.dev/tour/) · [Quarkus Kafka guide](https://quarkus.io/guides/kafka) · [Playwright API testing](https://playwright.dev/docs/api-testing) · [Jepsen consistency models](https://jepsen.io/consistency) · [System Design Primer](https://github.com/donnemartin/system-design-primer)

*(All URLs returned HTTP 200 on 21 Oct 2026.)*

---

## Caveats
- **Skillenai** measures posting mix, not hiring volume. The SDET sample is small (140), and its "Go" count may be inflated by the ambiguous word.
- **ITviec counts** are a one-day snapshot. Quarkus and RabbitMQ had no tag count.
- **Remote pay numbers** come from staffing vendors (Second Talent) and single listings. They are directional, not survey-grade.
- **ITviec salaries** are self-reported medians from 2025 survey waves.
- **The VND→USD conversion** (≈26,000) is approximate.
- **Interview topic lists** come from prep sites (secondary). CoderPad is a vendor survey of about 650 people.
- **Inbox data** is alert titles only. No personal data, recruiter names or contacts are included. No email was sent, drafted or changed.
