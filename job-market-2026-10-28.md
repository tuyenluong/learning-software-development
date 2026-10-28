# Job Market 2026-10-28: QE / SDET and Backend (Go · Spring Boot · Quarkus · Kafka · RabbitMQ)

**Prepared by:** Jake (Research) for Tuyen Luong and Jacob (Teacher)  **Date:** 28 Oct 2026
**Purpose:** Market facts to build a learning plan for QE → backend → solution architect. The core teaching focus is transaction and messaging problems.
**Coverage:** catch-up for the weekly run that failed on **Fri 23 Oct 2026**. Window covered: **17–28 Oct 2026**.
**Builds on:** `qe-backend-job-market-2026.md` (baseline, 21 Oct 2026).

> **How to read the numbers**
> - **Skillenai** = a job-posting index (90-day rolling windows, ending 18–27 Oct 2026). It shows how often a skill shows up in postings, not total hiring. Its SDET sample is small (132 postings), its Backend Engineer sample is large (2,627). Its headline "demand vs prior 4 weeks" is a *share* change, so a rising share on a small posting count is noise.
> - **ITviec counts** = live listing counts pulled from itviec.com tag pages on **28 Oct 2026**. Snapshot only; they move week to week.
> - **ROLIVA** = a QA/test-specific job board. Counts are its own live listings on 28 Oct 2026 (2,000 QA and test engineer listings), so percentages describe *that board*, not the whole market.
> - **JobRemotely** = a remote-job board, snapshot dated 1 Oct 2026 (687 listings). US-weighted.
> - **Jobpedia.AI** and **freehire** = posting aggregators that publish per-role skill shares over 90-day windows. freehire splits by seniority, which is why it is used heavily in §9.
> - **AutomationDataCamp (ADC)** = a French QA training company's public barometer of French job ads (405 "QA"-titled + 1,180 "test"-titled). European and French-language, so read it for direction, not for Vietnam.
> - **Mentorpiece Vacy Index** (reported via Habr) = share of tech companies with at least one open role of a given type. Company-level, not posting-level.
> - Anything marked **(est.)** is my own estimate or conversion. VND→USD uses about **26,000 VND/USD**, which is approximate.
> - **Inbox (Jobs label)** = aggregate only. These are LinkedIn/Glassdoor alert digests, mostly job titles. No personal data is included, and nothing was sent or changed.

---

## Top skills at a glance (28 Oct 2026)

**QE / automation — learn these first**
1. **CI/CD** — 56.1% of SDET postings ([Skillenai SDET](https://skillenai.com/data/role/software-development-engineer-in-test-sdet)); 35.1% of French QA ads ([ADC](https://www.automationdatacamp.com/blog-post-barometre-competences-qa)).
2. **Python**, then **Java** as the second language — Python 51.5%, Java 35.6% of SDET postings.
3. **Playwright** — 47.0% of SDET postings, and now **#1 in French QA ads at 24.2%, ahead of Selenium at 21.7%**. Playwright has crossed over.
4. **API testing** — 22.0% of SDET postings, 21% of QA-engineer roles ([Jobpedia](https://jobpedia.ai/roles/qa-engineer)); Postman named in 20% and REST Assured in 15.3% of French QA ads.
5. **SQL** — 21% of QA-engineer roles ([Jobpedia](https://jobpedia.ai/roles/qa-engineer)), 14.8% of French QA ads.

**Backend — learn these first**
1. **Java + Spring Boot** for Vietnam; **Python/AWS/Kubernetes** for the global remote market ([Skillenai Backend](https://skillenai.com/data/role/backend-engineer)).
2. **Distributed systems** — 25.6% of Backend Engineer postings.
3. **PostgreSQL** — 23.3%, up from 20.9% on 21 Oct. The fastest-rising skill in the table.
4. **Kafka** — 18.2% of Backend Engineer postings; 8,265 postings across all roles, about **5.2× RabbitMQ**.
5. **Observability** — 16.5% of Backend Engineer postings, 15% of Middle Backend postings ([freehire](https://freehire.me/insights/roles/backend/middle)).

---

## What changed this week (21 Oct → 28 Oct 2026)

**Job emails: yes, there were new ones.** 28 job-alert emails arrived in the Gmail **Jobs** label between 17 and 28 Oct. All 28 were automated digest emails from LinkedIn job alerts and Glassdoor. None came from a named recruiter, none stated a salary range, and I read them read-only: no email was replied to, labelled, archived or changed.

**The five changes worth acting on**

| # | Change | 21 Oct (baseline) | 28 Oct | Read |
|---|---|---|---|---|
| 1 | **Cloud platforms now have real numbers** | "AWS is most common", no QA-specific count | QA postings: **AWS 10%, Azure 10%, GCP 4%** (ROLIVA, 2,000 listings); remote listings: **AWS 53, GCP 31, Azure 23 of 687** (JobRemotely) | AWS first. Below AWS the two sources disagree, so the ordering is soft. See §1B. |
| 2 | **Playwright overtook Selenium** in French QA ads | Playwright 47.1% of SDET postings, Selenium 35.7% | Playwright **24.2% vs Selenium 21.7%** of QA ads; in SDET postings Playwright 47.0% vs Selenium 34.8% | Playwright is no longer the challenger. Teach it as the default, Selenium as legacy maintenance. |
| 3 | **Backend demand share is cooling even as Kafka rises** | Backend Engineer 2,571 postings | 2,627 postings, **demand share down 9.0%** vs prior 4 weeks; **Kafka +2.6%**, **event-driven architecture +15.6%** | Fewer backend seats, but the ones left are more distributed-systems-shaped. The messaging focus gets *more* valuable, not less. |
| 4 | **Manual QA is shrinking faster than automation** | — | Companies with open **manual QA** roles 14.1% → **9.5%** (−33%); automation QA 18.6% → 17.5% (−6%); **AI-QA 3.9% → 5.1%** (+31%) (Mentorpiece Vacy Index, Oct 2026) | The manual-to-automation move is now a survival move, not a pay-rise move. |
| 5 | **Vietnam board counts moved in Kafka and microservices** | ITviec: kafka 14, microservices 28, spring boot 42 | ITviec: **kafka 18, microservices 33, spring boot 44, java 104** | Small but consistent step up in messaging-adjacent listings in Vietnam. |

**Backend skill shares, 21 Oct → 28 Oct** (Skillenai, Backend Engineer; shares are of all postings in the window, including those with no skills listed, so treat small moves as rounding):

| Skill | 21 Oct | 28 Oct | Skill | 21 Oct | 28 Oct |
|---|---|---|---|---|---|
| Python | 32.2% | 33.9% | Kafka | 17.9% | 18.2% |
| AWS | 31.8% | 33.0% | SQL | 15.9% | 16.8% |
| Kubernetes | 30.5% | 30.8% | Observability | 16.6% | 16.5% |
| Java | 26.6% | 26.8% | Redis | 15.1% | 15.2% |
| Go | 25.6% | 25.8% | Microservices | 14.4% | **16.2%** |
| Distributed systems | 25.1% | **25.6%** | CI/CD | 17.8% | **20.3%** |
| Docker | 21.2% | 22.3% | TypeScript | 16.8% | 18.3% |
| PostgreSQL | 20.9% | **23.3%** | | | |

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

**Messaging, all roles (Skillenai 90-day totals).** These totals grow partly because the index grows, so read the *share change*, not the raw count:

| Signal | 21 Oct | 28 Oct | Share change |
|---|---|---|---|
| Kafka postings | 7,777 | **8,265** | **+2.6%** (as of 23 Oct) |
| RabbitMQ postings | 1,486 | **1,592** | **−4.6%** (as of 21 Oct) |
| Event-driven architecture | 1,993 | **2,451** | **+15.6%** (as of 21 Oct) |
| Microservices | 9,747 | **10,049** | +0.7% (as of 18 Oct) |

Kafka is now **5.2×** RabbitMQ by posting count (8,265 ÷ 1,592; est.). Event-driven architecture is the fastest-rising of the four.

**ITviec Vietnam, 21 Oct → 28 Oct 2026** (live listing counts, same tag pages):

| Tag | 21 Oct | 28 Oct | Tag | 21 Oct | 28 Oct |
|---|---|---|---|---|---|
| java | 103 | **104** | tester | 58 | **61** |
| backend developer | 92 | **88** | automation test | 36 | **40** |
| spring boot | 42 | **44** | playwright | 12 | **13** |
| golang | 37 | **35** | sdet | 11 | **9** |
| microservices | 28 | **33** | kafka | 14 | **18** |

([java](https://itviec.com/it-jobs/java), [backend developer](https://itviec.com/it-jobs/backend-developer), [spring-boot](https://itviec.com/it-jobs/spring-boot), [golang](https://itviec.com/it-jobs/golang), [microservices](https://itviec.com/it-jobs/microservices), [kafka](https://itviec.com/it-jobs/kafka), [tester](https://itviec.com/it-jobs/tester), [automation-test](https://itviec.com/it-jobs/automation-test), [playwright](https://itviec.com/it-jobs/playwright), [sdet](https://itviec.com/it-jobs/sdet))
- The Quarkus tag page returned **404** on 28 Oct, consistent with the baseline's "no count shown (≈0)".
- Java held flat, backend-dedicated titles slipped by 4, and the testing tags gained. Kafka and microservices both moved up, the one Vietnam-side signal that supports the messaging focus.

**Inbox (Jobs label, aggregate, 17–28 Oct):**
- **28 alerts in 11 days** — roughly the same daily rate as the baseline's 6-month sample.
- Split is still about **50% QA/automation and 40% backend**.
- Recurring QA titles: Senior QA Engineer, SDET, Automation Test Engineer (Middle/Senior), QC Auto, QA Analyst. Recurring backend titles: Principal Java/Kotlin Engineer, Intermediate/Senior Backend Engineer, Middle Java Developer, Senior Backend (Java, Fintech).
- **Remote backend widened:** one employer posted *both* an Intermediate and a Senior remote-Vietnam backend role in this window (19 and 25 Oct), the first time the alerts show the same company hiring two backend levels remotely in one window.
- **Banking and fintech stayed the biggest single cluster** of backend titles, as in the baseline.
- **Kafka, RabbitMQ and Quarkus still appear in zero alert titles.** Alerts are title digests; stack detail lives in the body, which is why §1 leans on posting indexes instead.
- **No salary ranges were stated in any of the 28 alerts.** Salary figures in §5 come from the ITviec survey and posted ranges on live listings, not from this window's inbox.

---

## 0. Bottom line (for Jacob)

1. **The QE market keeps moving toward "engineer who tests".** CI/CD 56.1%, Python 51.5%, Playwright 47.0%, Java 35.6% top SDET postings, and **Playwright has now overtaken Selenium** in an independent European ad survey (24.2% vs 21.7%). Meanwhile the share of companies with open *manual* QA roles fell **33%** in six months.
2. **Cloud is settled at the top and unsettled below it.** AWS leads on both sources: **10% of QA postings** (ROLIVA) and **53 of 64** cloud-naming remote listings (JobRemotely). Azure and GCP swap places between the two (Azure 10% vs GCP 4% on one; GCP 31 vs Azure 23 on the other), so **anything below AWS is a soft ordering**.
3. **Backend seats are getting scarcer but more distributed.** Backend Engineer demand share is **down 9.0%** vs the prior four weeks while **event-driven architecture is up 15.6%** and Kafka up 2.6%. The market is not asking for more backend engineers; it is asking the remaining ones for messaging and consistency skill.
4. **The pay gap that justifies the backend move is unchanged.** ITviec 5–8 year medians: **39.9M VND backend vs 25.3M Tester and 29.75M QA-QC** (+35–58%). No new salary data appeared this window, so this is still the 2025–2026 survey.
5. **The junior backend path being built for Tuyen is well aimed but has three real gaps:** JPA/Hibernate depth, build tooling and Kubernetes, and the fintech money-handling rules. §9 sets the three stages against real junior and mid postings and lists what is covered, what is missing and what is being taught that the market rarely asks for.

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
- **AWS first.** It is the only cloud both sources agree on, it leads the remote board by a wide margin (53 vs 31), and it is the cloud the backend postings in §9 name most often.
- **Treat the ordering below AWS as soft.** ROLIVA puts **Azure at 10% and GCP at 4%**; JobRemotely puts **GCP at 31 and Azure at 23**. The two disagree on which is second, and by a lot. What is safe to say: Azure and GCP are each roughly a third to a half of AWS, and neither is the one to learn first.
- JobRemotely adds a useful nuance: **Azure is rarely named alone** — only 4 listings named Azure and nothing else, and 70% of the listings naming Azure named all three clouds. So "Azure" in a posting often means "we are multi-cloud", not "we are an Azure shop".
- **Teaching consequence:** the one AWS deployment in Stage 2 is the right call, and it should be a real deploy (ECS or Elastic Beanstalk, plus RDS and S3), not a tutorial. Azure and GCP are a comparison lesson, not a track.

Other cloud-adjacent signals from ROLIVA's QA snapshot: **Docker 6% (114)**, **Kubernetes 6% (112)**, **Kafka 2% (47)**, **LLM 2% (39)**, **PostgreSQL 1% (22)**. Python leads the whole board at **27% (544)**, then Agile 16%, Java **15% (301)**, SQL 14%, Jira 13%. Vietnam appears as **24 of the 2,000 listings (1%)**.

### C. Backend Engineer (Go / Java)

**Global: Skillenai, "Backend Engineer" title, 2,627 postings, 90 days to 27 Oct 2026** ([source](https://skillenai.com/data/role/backend-engineer))

| Skill | Share | Skill | Share |
|---|---|---|---|
| Python | 33.9% | Kafka | 18.2% |
| AWS | 33.0% | SQL | 16.8% |
| Kubernetes | 30.8% | Observability | 16.5% |
| Java | 26.8% | Microservices | 16.2% |
| **Go** | **25.8%** | Redis | 15.2% |
| **Distributed systems** | **25.6%** | | |
| PostgreSQL | 23.3% | | |
| Docker | 22.3% | | |
| CI/CD | 20.3% | | |

- **Demand share down 9.0% vs the prior four weeks** — the first negative direction signal in either report.
- **Top Backend Engineer posters:** GitLab 129, Grafana Labs 117, CLERA 61, Wise 60, Stripe 56. Mostly remote-friendly product companies, unchanged from the baseline.
- **Top metros:** Berlin 4.4%, New York City 3.1%, London 2.8%, San Francisco 2.7%, Tel Aviv 2.5%.

**By seniority: freehire, open Backend postings, updated 27–28 Oct 2026**

| Level | Open postings | Skill leaders |
|---|---|---|
| **Junior** | **1,420** (1,239 list skills) | python 44%, **java 43%**, api 36%, ai 27%, sql 25%, git 22%, rest 20%, docker 16%, cloud 16%, ci-cd 15%, postgresql 14%, aws 14%, **redis 13%**, **spring 13%**, kubernetes 8%, go 7%, azure 6% |
| **Middle** | **1,178** (1,084 list skills) | api 65%, java 41%, **aws 41%**, rest 39%, cloud 38%, ci-cd 37%, ai 35%, docker 33%, python 31%, **kubernetes 28%**, microservices 27%, sql 27%, git 27%, postgresql 25%, azure 22%, spring 21%, **event-driven 21%**, **kafka 21%**, mysql 18%, devops 18%, agile 17%, **observability 15%**, distributed systems 15%, gcp 15%, redis 14%, nosql 14%, **test-automation 13%**, **rabbitmq 9%**, s3 9% |

([freehire junior](https://freehire.me/insights/roles/backend/junior), [freehire middle](https://freehire.me/insights/roles/backend/middle), [freehire backend seniority split](https://freehire.me/insights/roles/backend))

- **The junior-to-middle jump is the most useful line in this report.** From junior to middle, Kubernetes goes **8% → 28%**, CI/CD **15% → 37%**, AWS **14% → 41%**, observability **0% → 15%**, Kafka **0% → 21%**. Junior postings rarely ask for infrastructure. Middle postings expect it.
- freehire's seniority census (28 Oct): 23,169 open Backend roles — Senior 16,001, Lead 2,068, Staff 1,278, **Middle 1,178**, **Junior 1,085**, Intern 1,081, Principal 367. Junior and Middle grew faster than Senior month-over-month (+297 and +252, against +1,518 on a much larger base).

**Vietnam: ITviec live counts, 28 Oct 2026:** "java" 104, "backend developer" 88, "spring boot" 44, "golang" 35, "microservices" 33, "kafka" 18, "quarkus" no tag page (404, ≈0).
- Posted ranges visible on the same day's listings: a Mid/Sr Java role "up to $3,200", a Senior Backend role "up to 50M", a manual-plus-automation tester role "up to 28M net", a QC Manager role "up to 55M". Single listings, not survey data.
- Titles continue to cluster in **banking and fintech**: two bank backend roles, one bank senior quality engineer and one fintech platform Java role in this window's sample.

**Inbox:**
- About 40% of the 28 alerts are backend, about 50% QA/automation — unchanged from the baseline.
- **Kafka, RabbitMQ and Quarkus: still zero hits in alert titles.** The alerts remain title digests.

---

## 2. Must-have vs nice-to-have vs differentiator (mid → senior)

*This synthesis is my own, based on the frequencies above, the postings in §9 and the interview sources in §6.*

### A. QE / SDET

| Level | Must-have | Nice-to-have | Differentiator (gets the remote or senior offer) |
|---|---|---|---|
| **Mid** | One language done properly (TS or Java/Python); Playwright (or Selenium for Java shops); API testing (REST, auth, schema, negative cases); Git; CI (GitHub Actions/Jenkins); test design techniques; SQL basics | Docker; Cypress/Selenium migration; performance basics (k6/JMeter); mobile (Appium) | Contract testing (Pact); Testcontainers; testing async/event flows |
| **Senior** | Framework architecture (fixtures vs POM, data isolation, parallelism and sharding, reporting); flaky-test strategy; test strategy and risk-based planning; CI at scale; mentoring | Kubernetes test grids; observability (OTel traces in tests); security testing basics | **Backend-aware QE:** testing Kafka/RabbitMQ flows, idempotency, retries, DLQs, eventual consistency, DB isolation/race conditions; **AI-in-testing** (Playwright agents/MCP, evaluating LLM features); quality metrics with DORA language |

*Unchanged from the baseline. Nothing in this window's data moved the mid/senior boundary.*

### B. Backend (Go / Spring Boot)

| Level | Must-have | Nice-to-have | Differentiator |
|---|---|---|---|
| **Mid** | Java 21/25 + Spring Boot 3/4 **or** Go; REST API design; SQL + PostgreSQL (indexes, transactions); Docker; unit and integration tests (JUnit/Testcontainers or Go testing); Git and CI; one cloud (AWS is most common) | Kafka *or* RabbitMQ producer/consumer basics; Redis; Kubernetes basics; gRPC | Strong testing of your own services (Tuyen's natural edge) |
| **Senior** | **Distributed systems:** microservices boundaries, messaging (Kafka), retries, timeouts, idempotency, outbox/saga, consistency trade-offs; observability (logs, metrics, traces); performance and concurrency; system design interviews; on-call/incident thinking | Event sourcing/CQRS; Kafka Streams/Connect/Debezium (CDC); K8s operations; security (OAuth2/OIDC) | **Proving correctness under failure:** fault injection, chaos tests, reproducing duplicate/out-of-order delivery; domain depth in payments/fintech; writing ADRs and design docs (the bridge to architect) |

*One refinement this week: the mid-level row now sits closer to the senior row than the baseline suggested. **Kubernetes jumps from 8% of junior postings to 28% of middle postings**, and CI/CD from 15% to 37% ([freehire](https://freehire.me/insights/roles/backend/middle)), so a mid-level candidate without container orchestration or a pipeline is now the exception rather than the rule.*

---

## 3. Messaging, transactions and distributed systems: how often, and how tested

### Frequency signals

| Signal | Number | Source |
|---|---|---|
| Kafka postings (all roles, 90d) | **8,265** (+2.6% vs prior 4 weeks) | [Skillenai Kafka](https://skillenai.com/data/skill/kafka) |
| RabbitMQ postings (90d) | **1,592** (−4.6%) → Kafka is about **5.2×** RabbitMQ (est.) | [Skillenai RabbitMQ](https://skillenai.com/data/skill/rabbitmq) |
| Event-driven architecture postings (90d) | **2,451** (**+15.6%**) | [Skillenai EDA](https://skillenai.com/data/skill/event-driven-architecture) |
| Microservices postings (90d) | **10,049** (+0.7%) | [Skillenai microservices](https://skillenai.com/data/skill/microservices) |
| Share of Backend Engineer postings | Distributed systems 25.6%, Kafka 18.2%, microservices 16.2%, Redis 15.2%, observability 16.5% | [Skillenai Backend](https://skillenai.com/data/role/backend-engineer) |
| Share of **Middle** Backend postings | **Kafka 21%**, **event-driven architecture 21%**, distributed systems 15%, observability 15%, **RabbitMQ 9%** | [freehire middle](https://freehire.me/insights/roles/backend/middle) |
| Kafka in Java backend titles | 28.6% of "Java Backend Engineer"; 30.1% of "Distributed Systems Engineer" | [Skillenai Kafka](https://skillenai.com/data/skill/kafka) |
| RabbitMQ in backend titles | 12.1% "Back-End Engineer", 10.6% "Java Engineer"; often paired *with* Kafka | [Skillenai RabbitMQ](https://skillenai.com/data/skill/rabbitmq) |
| Kafka co-occurrence | Paired most with Python, Java, Kubernetes, AWS, SQL | [Skillenai Kafka](https://skillenai.com/data/skill/kafka) |
| Top Kafka employers | Wise 175, Cisco 149, CrowdStrike 115, **Mastercard 101, Barclays 91, Capital One 70, JPMorgan 60** | [Skillenai Kafka](https://skillenai.com/data/skill/kafka) |
| Top EDA employers | Wise 50, **Mastercard 45, Barclays 35**, Fiserv 16, Capco 16, Airwallex 12 | [Skillenai EDA](https://skillenai.com/data/skill/event-driven-architecture) |
| Vietnam | ITviec "kafka" **18** and "microservices" **33** live jobs (vs Java 104) | ITviec, 28 Oct 2026 |

**Read (my interpretation):**
- **Kafka is still the messaging skill to lead with.** 5.2× RabbitMQ across all roles, and it appears in middle-level backend postings (21%) as often as event-driven architecture does overall.
- **Event-driven architecture rising 15.6% while backend demand falls 9.0% is the clearest signal in this report.** Employers are not hiring more backend engineers; they are asking the ones they hire to understand events. That is exactly the gap a QA → backend move can attack, because Tuyen already knows how event flows fail.
- **RabbitMQ is holding steady in absolute count but losing share** (−4.6%). Still worth one lesson, because it is the broker in .NET/Python shops and in integration work.
- **For QE roles, messaging is still not a standard requirement** (Kafka is 2% of ROLIVA's QA listings). That is what makes it a differentiator.

### How it's tested in interviews
*Unchanged from the baseline — no new interview-format survey was published in this window. Sources are prep sites and vendor surveys, so treat the topic lists as secondary consensus, not employer data.*

1. **System design round.** The main place messaging gets tested (system design appears in 38% of technical tests per [CoderPad 2026](https://coderpad.io/survey-reports/coderpad-state-of-tech-hiring-2026/)). Prompts: checkout, payment, wallet transfer, notifications. Expected answers: local transactions with **no 2PC**, **transactional outbox**, **saga** with compensations, **retries with backoff and timeouts**, **idempotent consumers**, **DLQ** for poison messages.
2. **Kafka deep-dive questions.** Partitions and ordering; consumer groups and **rebalancing**; offset commit timing; idempotent producer and transactions; why "exactly-once" only covers Kafka-to-Kafka; **consumer lag**.
3. **Database and concurrency questions.** Isolation levels and their anomalies; optimistic vs pessimistic locking; "two requests withdraw from the same account"; idempotency keys on POST.
4. **Debugging/scenario rounds.** "Users get charged twice", "consumer lag grows after a deploy", "messages land in the DLQ after a schema change".
5. **For SDET loops**, the same topics arrive as "how would you test it": test strategy for an event-driven flow, contract tests, Testcontainers with a real broker, asserting eventual consistency without `sleep`, fault injection.

**This maps directly onto Jacob's core focus.** Each lesson can follow "what breaks → how to reproduce/test (QE) → how to fix (backend) → how to design it out (architect)".

---

## 4. Go vs Spring Boot vs Quarkus

| Signal | Go | Spring Boot | Quarkus |
|---|---|---|---|
| Global postings, 90d (Skillenai) | **13,887** (+4.0%) ¹ *(21 Oct figure, not re-pulled)* | **4,673** (+3.4%) *(21 Oct figure, not re-pulled)* | no Skillenai page; Alion lists **91–152** live roles ([Alion](https://alion.io/jobs/quarkus)) |
| Share of Backend Engineer postings | **25.8%** (28 Oct) | (Java 26.8%, 28 Oct) | n/a |
| Top employers | Capital One, Cisco, SpaceX, **Stripe**, CrowdStrike, Cloudflare, **Grab** | **Mastercard, Barclays, Wise, JPMorgan**, Capco | Citi, Sopra Steria, Red Hat consulting, defence/gov (OpenShift shops) |
| SO 2026 usage | Go language **16.5%** | Spring Boot **12.8%** of web-framework users (Java 27.6%) | **0.3%** ² |
| Java-org surveys | n/a | Azul 2025: **42%** of orgs use Spring Boot for Java microservices; Vaadin 2025: 86% | Azul 2025: **7%**; Jakarta EE 2025: Quarkus runtime use **declining** |
| UK permanent jobs (ITJobsWatch, 6 mo) | n/a | n/a | **2** (vs 15 a year ago) ([ITJobsWatch](https://www.itjobswatch.co.uk/jobs/uk/quarkus.do)) |
| Vietnam ITviec (28 Oct) | **35** (was 37) | **44** (Java 104; was 42) | **≈0** (tag page 404) |
| Vietnam job titles (vitX) | **22** | Java **52** | n/a |
| Vietnam remote pay premium | Second Talent: Go seniors **+10–20%** over the backend range (vendor est.) | Baseline ("Java remains highest-demand backend language in Vietnam") | n/a |

¹ Skillenai resolves skills to a canonical entity, but "Go" is an ambiguous word, so treat its count as an upper bound.
² Quarkus may not have been a listed answer option in SO 2026, so 0.3% likely understates it. It is still far smaller than Spring.

Sources: [Skillenai Go](https://skillenai.com/data/skill/go), [Skillenai Spring Boot](https://skillenai.com/data/skill/spring-boot), [SO 2026 languages](https://survey.stackoverflow.co/2026/technology/data/languages), [SO 2026 web frameworks](https://survey.stackoverflow.co/2026/technology/data/web-framework), [Azul State of Java 2025](https://www.qbssoftware.com/wp-content/uploads/2025/04/Azul-report-State-of-Java-2025.pdf), [Jakarta EE 2025 survey](https://outreach.eclipse.foundation/hubfs/2025%20Jakarta%20EE%20Developer%20Survey%20Report.pdf), [Second Talent Vietnam](https://www.secondtalent.com/resources/true-cost-outsource-software-development-vietnam/).

**Verdict (unchanged):**
- **Spring Boot is the primary stack.** Biggest Vietnam demand, dominates bank and fintech hiring, matches Tuyen's saved "remote Backend java" search, and Java skill carries over from Selenium/Java test work.
- **Go is the second language, aimed at remote and global product companies.** It wins on platform and infra work, and Kafka/K8s tooling is often written in Go.
- **Quarkus gets concepts only** — one or two lessons of comparison (build-time DI, native image, reactive messaging, Dev Services). Most Spring knowledge carries over.

*The one number that moved this window: Vietnam "golang" listings slipped 37 → 35 while "spring boot" rose 42 → 44. Two listings is noise, but the direction matches the baseline's recommendation.*

---

## 5. Salary ranges

**No new salary data this window.** The inbox contained no stated ranges, and ITviec has not published a new survey. The figures below are the 2025–2026 survey, re-read on 28 Oct 2026 and unchanged.

### Vietnam local: ITviec 2025–2026 report, median **gross VND / month**
([ITviec report](https://itviec.com/report/vietnam-it-salary-and-recruitment-market), 1,839 respondents, surveyed May–Nov 2025)

| Role | <1 yr | 1–2 yr | 3–4 yr | 5–8 yr | >8 yr | Overall |
|---|---|---|---|---|---|---|
| Tester | 14.15M | 14.2M | 20.7M | 25.3M (≈$970) | 36.5M (≈$1,400) | 28.8M |
| QA-QC | – | 18M | 24.4M | 29.75M (≈$1,140) | 38.5M (≈$1,480) | 31.2M |
| **Back-end Developer** | 12.4M | 25.35M | 30.1M | **39.9M (≈$1,530)** | **54.9M (≈$2,110)** | 37.8M |
| Tech Lead | – | 45.3M | 53.85M | – | 68.45M | 51.8M (≈$1,990) |
| Project Leader/PM | 17.2M | 29.85M | 48.4M | 58.45M | – | 50.1M |

- **The backend premium at 5–8 years is +35–58%** over the Tester and QA-QC medians. It widens above 8 years.
- **Posted ranges on live ITviec listings, 28 Oct:** Mid/Sr Java "up to $3,200"; Senior Backend "up to 50M"; manual-plus-automation tester "up to 28M net"; QC Manager "up to 55M". Consistent with the medians and with each other.
- **Go (Second Talent, vendor):** junior 20–35M, mid 35–55M, **senior 55–80M**, lead/architect 80–140M VND/month ([source](https://www.secondtalent.com/developer-rate-card/golang-developer-vietnam/)). An upper-market estimate, not a survey.

### Remote / international (Vietnam-based engineer, USD / month)

| Source | QA Automation | Backend (Java/Go/Node/Python) | Notes |
|---|---|---|---|
| [Second Talent, Vietnam rates 2026](https://www.secondtalent.com/resources/true-cost-outsource-software-development-vietnam/) (vendor) | Mid **$2,500–3,900** · Senior **$3,900–5,600** · Lead $5,600–7,700 | Mid **$3,400–4,900** · Senior **$4,900–7,000** · Lead/Architect **$7,000–9,800** | Go/.NET seniors +10–20%; remote rates 40–100% above local; English is the biggest differentiator |
| [Second Talent APAC benchmark, Oct 2026](https://www.secondtalent.com/apac-salary-benchmark/) (vendor) | n/a | Vietnam all-roles median: mid **$3,100**, senior **$4,500** (IQR $4,300–5,500), lead $5,300 | Remote contractor rates |
| [JobRemotely cloud analysis, 1 Oct 2026](https://jobremotely.io/blog/cloud-jobs-aws-azure-gcp) | n/a | Median across listings naming a cloud: **AWS $175,450**, Azure $168,500, GCP $165,250 per year. US-only: AWS $185,000 (n=35), Azure $193,050 (n=21), GCP $195,000 (n=21) | Global remote, mostly US-tagged (566 of 687). Not a Vietnam rate |
| [ADC France barometer, 2 Oct 2026](https://www.automationdatacamp.com/blog-post-barometre-competences-qa) | Median **€42,500** gross/yr; senior/lead **€50,000** (229 of 605 ads state pay) | n/a | French market, for comparison |
| Global reference ([SO 2026 comp](https://survey.stackoverflow.co/2026/work/data/compensation)) | QA/test median not published (<100 resp.) | Back-end median **$85,296/yr** globally; Architect **$102,355/yr** | Mostly US/EU respondents |

**Read (est.):**
- A senior QA automation engineer working remotely from Vietnam lands around **$4–5.5K/mo**.
- A senior backend engineer lands around **$5–7K/mo**, so the backend premium is about **+25–35%** (est.).
- Architect/lead roles reach **$7–10K/mo**.
- Locally, the backend move is worth about **+35–55%** at 5–8+ years.

---

## 6. Typical interview formats and common topics

**Market-wide (CoderPad 2026, about 650 respondents)** ([source](https://coderpad.io/survey-reports/coderpad-state-of-tech-hiring-2026/)) — *not re-surveyed this window; baseline figures*:
- **Exercises used:** algorithmic 43%, real-world scenarios 38%, system design 38%, pair programming 30%, code review 21%, debugging 19%.
- **What best predicts the job:** technical discussion (60% of recruiters) and live coding (60%). Take-homes score only 12%.
- **AI in interviews:** 34% ban it, **46% allow it** (broadly or with constraints), 20% decide case by case. When AI is allowed, the signals of real skill are **catching and fixing AI mistakes (66%)** and **explaining trade-offs (56%)**.
- **Top cheating concern:** agent-generated solutions (52%). This pushes companies toward live, multi-file, realistic tasks.

**SDET loop (typical, from prep guides):** recruiter screen → coding screen (Java/Python/TS: strings, maps, edge cases) → **framework design** (fixtures/POM, data isolation, parallel CI, reporting, retries and flake quarantine) → **API testing practical** (status codes, idempotency of methods, auth/JWT, schema and negative tests, contract tests) → test strategy (risk-based, test pyramid) → behavioural ([TechScreen 2026](https://techscreen.app/articles/sdet-qa-automation-interview-guide-2026), [SoftwareTestPilot](https://softwaretestpilot.com/blog/career-interview-prep/how-to-prepare-for-sdet-interview-at-faang)).
- Common questions: "Design a framework for X." · "How do you handle flaky tests?" · "Test a payment API." · "What's in your CI pipeline?" · "How would you test a Kafka consumer?" (senior/fintech).

**Backend loop (mid/senior):** recruiter → coding (DSA, or a practical service task) → **system design** (senior: often 2 rounds) → **domain/deep-dive** (Spring internals or Go concurrency, DB/transactions, Kafka) → behavioural/leadership. Common topics:
- **Spring:** DI and bean lifecycle; `@Transactional` propagation and pitfalls (self-invocation, rollback rules); **JPA N+1**; connection pools; virtual threads (Java 21+).
- **Go:** goroutines, channels, `context` cancellation/timeouts, races (`-race`), worker pools, error handling.
- **Data:** indexes, isolation levels, locking, migrations.
- **Messaging:** see §3. Ordering, lag, rebalancing, delivery semantics, outbox/saga, DLQ, idempotency.
- **Ops:** observability, rate limiting, circuit breakers, retries with jitter.

**Vietnam specifics (est., from market structure):** outsourcing and service firms often run a shorter loop — tech interview, English check, sometimes a test. Foreign in-house centres and remote employers run fuller loops with system design. **English is a gate** for remote roles; two of the postings read for §9 state a level outright (B2/C1 and B1+).

---

## 7. Trends

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

**AI-assisted backend dev**
- CoderPad: 82% of developers find GenAI useful, and 54% would lose ≥10% productivity without it. Developers expect **system design and debugging to grow in importance** and writing new code to shrink.
- **Implication:** distributed-systems judgement is the part AI cannot do for you. It is also what interviews increasingly test — and it is why the messaging focus survives a 9% drop in backend demand share.

**QE → backend moves**
- Skillenai career flows: SDETs mostly move to **other SDET roles** (46 same-role moves). Only 2 observed SDET→Software Engineer moves vs 10 SE→SDET ([Skillenai SDET](https://skillenai.com/data/role/software-development-engineer-in-test-sdet)). Backend Engineer hires come mainly from Software Engineer (104 moves in, 57 out) ([Skillenai Backend](https://skillenai.com/data/role/backend-engineer)).
- **Read:** the switch is still uncommon, so it needs deliberate proof: a deployed service, production-quality code, and system-design fluency. §9 turns that into a checklist.
- Practitioner guides suggest an **internal transfer** first, and **3–6 months** of focused work if you already write strong automation code (12–18 months if not) ([SeekerScore](https://www.seekerscore.com/routes/qa-engineer-to-software-engineer), [Codefarm](https://codefarm.in/blog/software-engineering/qa-to-developer-transition)). Secondary sources; treat the timelines as estimates.

**Path toward solution architect**
- SO 2026: "Architect, software or solutions" is 7% of respondents, with a **$102K** global median.
- ITviec Vietnam: Tech Lead median **51.8M VND**, PM/PL 50.1M.
- Architects are expected to make and document trade-offs (ADRs), handle reliability and scaling, cost, security, and cross-team integration. Messaging and consistency design is central to that.

---

## 8. Recommended skill priority list (QE → backend → architect)

*Time estimates assume about 6–8 hrs/week and are my estimates. Jacob should confirm Tuyen's actual weekly time. Order unchanged from the baseline; the §9 findings are folded in as additions, marked **new**.*

### Phase 1: Strengthen the QE base and become a "backend-aware SDET" (months 0–3)
1. **API testing in depth** (Playwright `request` + REST Assured in Java): auth, schema, negative cases, idempotent methods. *(22% of SDET postings; it is the bridge skill.)*
2. **SQL + PostgreSQL transactions:** isolation levels, lost update and write skew, locking. Reproduce a race condition in a test. *(Core focus.)*
3. **Testcontainers** (Java and Go) with Postgres + Kafka + RabbitMQ in CI (GitHub Actions). *(CI/CD is 56% of SDET postings.)*
4. **Testing async/event flows:** asserting eventual consistency (polling and awaitility, not sleep), duplicate and out-of-order injection, DLQ assertions, contract tests (Pact). *(Differentiator.)*
5. **AI-in-testing literacy:** Playwright agents/MCP, and the seven review checks before merging an AI-generated test. *(20.7% of French QA ads mention AI.)*
6. **new** — **One cloud, and make it AWS.** A single deployment to AWS beats a tour of three consoles, and AWS is the only cloud both sources put first.

### Phase 2: Backend engineer on Spring Boot (months 3–9)
7. **Java 21/25 + Spring Boot 3/4:** REST, validation, JPA, `@Transactional` semantics and pitfalls, error handling, security (OAuth2/JWT).
8. **Kafka with Spring for Apache Kafka:** producers and consumers, keys and partitions, ordering; consumer groups and rebalancing; offset commits and delivery semantics; idempotent producer and transactions; retries/backoff and **DLT**; **consumer lag** monitoring.
9. **Reliability patterns:** idempotency keys and dedupe tables, **transactional outbox**, **saga** with compensations, timeouts and circuit breakers (Resilience4j).
10. **RabbitMQ:** exchanges, routing, acks, publisher confirms, DLX, retry queues, quorum queues. Compare with Kafka: when to use each.
11. **Observability:** structured logs, metrics, OTel traces across async hops; trace a message end to end.
12. **Portfolio proof:** one deployed "payments/orders" service set (Spring) with an outbox + saga + DLQ and a **failure-injection test suite**.

### Phase 3: Go as second language and remote-market reach (months 9–12)
13. **Go:** concurrency (goroutines, channels, `context`), `-race`, `net/http`/chi or gin, `database/sql`/pgx, Go testing. Port one service from Phase 2, with a Kafka client and an idempotent consumer.
14. **Quarkus (1–2 lessons):** Dev Services, reactive messaging (Kafka), native image. Compare with Spring and stop unless an employer needs it.

### Phase 4: Toward solution architect (12 months+)
15. **System design practice:** payments, wallet, notifications, inventory, rate limiter. Each must cover consistency, messaging and failure modes.
16. **Distributed-systems theory:** DDIA concepts (replication, partitioning, consistency models, exactly-once myths), Jepsen consistency models.
17. **Architecture communication:** ADRs, C4 diagrams, trade-off write-ups, cost and SLOs. Kubernetes and cloud basics.

**Why this order (unchanged):** it keeps Tuyen employable as a senior SDET the whole way, it hits the largest backend market first (Java/Spring in Vietnam and fintech), it adds Go for the remote premium, and the messaging and transaction core runs through every phase.

---

## 9. Backend path vs the market

*A teammate is building Tuyen a junior-to-mid backend track in Java/Spring Boot. This section sets its three stages against what junior and mid Java backend postings actually ask for. Everything below comes from postings and public skill surveys read in this window. Where I had no count, I say "in the postings I read" rather than inventing a percentage.*

### The path as briefed

| Stage | Timing | Content | Project |
|---|---|---|---|
| **1. Junior** | 0–6 months | Core Java (collections, exceptions, streams, basic concurrency); HTTP and REST design; SQL with PostgreSQL (joins, indexes, transactions); Spring Boot CRUD API with validation, error handling and tests; Git, Docker, running the app locally with a database | A small orders API |
| **2. Strong junior** | 6–12 months | Auth (sessions, JWT, OAuth basics); transactions done right (isolation levels, race conditions, API idempotency); Flyway migrations and Testcontainers integration tests; a CI pipeline and a first deploy to AWS | Payments on the orders API with retries and idempotency keys |
| **3. Mid-level** | 12–24 months | Caching with Redis; background jobs; messaging basics; observability (logs, metrics, tracing); performance basics (slow queries, connection pools, timeouts); simple system design and writing down decisions; owning a feature end to end | — |

### What the postings ask for

Six real postings were read in full, plus four skill surveys that split by seniority. The postings span junior through mid:

- **Junior Java backend** ([junbrain, Oct 2026](https://junbrain.com/jobs/project/junior-java-developer-backend-role/ql1b6N9)): Java 11+, Spring/Spring Boot, PostgreSQL/MySQL and basic SQL, Git, OOP, Agile/Scrum, code reviews, debugging. Bonus: REST APIs, JUnit/Mockito, Maven/Gradle, Docker or cloud, GitHub portfolio.
- **Junior backend Java** ([Addeco](https://www.adecco.com/en-pl/job-offers/junior-backend-java-developer-warszawa-mazowieckie/jn-022026-963243)): Java 17+, Spring/Spring Boot/**Spring Security**, Maven, SQL databases, Git and GitHub including pipelines, unit testing, **Bash/Shell**, **Docker + Kubernetes + Helm**, PostgreSQL, English B2/C1, scrum. (Asks 2+ years despite the "Junior" title.)
- **Sber, Middle Java Backend, 2–4 years** ([hh.ru](https://hh.ru/vacancy/134545742)): Java 17+ core — collections, streams, concurrency basics; Spring Boot 3/Spring Cloud; REST/gRPC; **Kafka/NATS**; JUnit + **Testcontainers**; PostgreSQL indexes and **query plans**; **Redis** for caching, rate limiting and pub/sub; Docker; basic Kubernetes; CI/CD; **Prometheus/Grafana/ELK**; postmortems; basic performance tuning. AI tooling a plus.
- **Netomi, SDE II – Backend, 2–4 years** ([Built In](https://builtin.com/job/sde-ii-backend/10390296)): Java + Spring Boot, microservices, RDS MySQL/PostgreSQL, **Kafka or RabbitMQ**, **Redis/Memcached**, distributed systems, performance profiling, JUnit and integration tests, Docker/K8s/AWS ECS, CI/CD, third-party integrations, **end-to-end feature ownership**, collaboration with QA and DevOps.
- **Bees, Intermediate Java Developer** ([Greenhouse](https://job-boards.greenhouse.io/bees/jobs/8805778002)): Java, Spring Boot, REST, microservices, Azure DevOps, **observability (New Relic/Datadog), monitoring, logging, troubleshooting production issues**, agile, code reviews, CI/CD. Differentials: NoSQL, event-driven/messaging.
- **Neocode, Java FinTech, middle, 3–6 years** ([hirify](https://hirify.me/jobs/1218356-java-fintech-backend-developer)): Java 21+, Spring Boot 3/4, PostgreSQL, Redis, Kafka/RabbitMQ, **transactions, idempotency, distributed systems basics**, Docker, basic K8s, observability, Testcontainers, **BigDecimal for money, audit log, idempotency keys, secure webhooks, data masking, payment statuses, PCI DSS basics**, OAuth2/OIDC + Spring Security.
- **Métrica, Mid Backend – Java, Kafka, Spring Boot and AWS** ([remote, Spain](https://www.spainjobs.io/companies/metrica/desarrolladora-backend-mid-java-kafka-spring-boot-aws--22fcd61272)): Java 17+, Spring Boot 3.x Web/Data JPA, **Kafka in production (consumers, topics, partitions)** or RabbitMQ/SQS-SNS, **hexagonal architecture**, PostgreSQL/Oracle plus query optimisation, JUnit + Mockito, **GitHub Actions + SonarQube**, **OpenAPI/API-first**, SOLID/Clean Code. Nice-to-have: AWS in production (EKS, S3, CloudWatch), **outbox, idempotent consumer, retries + DLQ**, Redis, **Testcontainers and contract tests**, banking domain, English B1+.

Surveys used for the frequency numbers: [freehire junior backend](https://freehire.me/insights/roles/backend/junior) (1,420 postings, 27 Oct 2026), [freehire middle backend](https://freehire.me/insights/roles/backend/middle) (1,178 postings, 28 Oct 2026), [Jobpedia junior software engineer](https://jobpedia.ai/roles/software-engineer/junior) (323 roles), [Skillenai Backend Engineer](https://skillenai.com/data/role/backend-engineer) (2,627 postings), and [Zorky's Java backend skill survey](https://zorky.tech/en/research/backend/java).

### (a) What the path already covers

Each row is something real postings ask for **and** the path teaches.

| Path element | Where the market asks for it |
|---|---|
| Core Java: collections, exceptions, streams, basic concurrency | Sber lists exactly this for 2–4 years; Java is **43%** of junior backend postings ([freehire](https://freehire.me/insights/roles/backend/junior)) and 41% at middle |
| HTTP and REST design | api **36%** and rest **20%** of junior postings; api 65%, rest 39% at middle; Jobpedia REST 19% for junior SE, 21% for all SE |
| SQL + PostgreSQL: joins, indexes, transactions | sql **25%**, postgresql **14%** of junior postings; sql 27%, postgresql 25% at middle; Zorky puts SQL/PostgreSQL/indexes/transactions before Spring Boot in its roadmap |
| Spring Boot CRUD with validation, error handling, tests | spring **13%** of junior postings, **21%** at middle; all six postings read name Spring Boot, and four of them pin 3.x |
| Git | git **22%** junior, 27% middle; Addeco asks for Git and GitHub including pipelines |
| Docker and running locally with a database | docker **16%** junior, **33%** middle; Addeco and Sber both require Docker |
| Unit and integration tests | JUnit in Netomi, Sber and Métrica; Métrica pairs it with Mockito, Sber with Testcontainers |
| Flyway migrations | Postings ask for schema **migrations** generically; Zorky lists migrations in the database step. The tool name is rare — see (c) — but the capability is asked for |
| Testcontainers integration tests | Named outright by **Sber** (must-have), **Neocode** (must-have) and **Métrica** (nice-to-have). One of the path's strongest cards |
| CI pipeline | ci-cd **15%** junior, **37%** middle; Addeco (GitHub pipelines), Métrica (GitHub Actions + SonarQube) |
| First deploy to AWS | aws **14%** junior, **41%** middle; Jobpedia junior lists AWS as the top preferred cloud at 14%; ROLIVA and JobRemotely both put AWS first |
| Auth: sessions, JWT, OAuth basics | Addeco requires Spring Security; Neocode requires OAuth2/OIDC + Spring Security. The other four postings read here do not name auth at all, so it is a differentiator in the CV stack rather than a keyword most ads filter on |
| Transactions done right: isolation, races, API idempotency | Neocode: "transactions, idempotency"; Métrica: idempotent consumer as a nice-to-have. **The path's differentiator against every generic bootcamp** |
| Redis caching | redis **13%** junior, 14% middle; Sber (caching, rate limiting, pub/sub), Netomi (Redis/Memcached), Neocode |
| Messaging basics | kafka **21%** and event-driven architecture **21%** of middle postings, rabbitmq 9%; Skillenai backend Kafka 18.2%; Netomi "Kafka or RabbitMQ"; Métrica Kafka consumers/topics/partitions in production |
| Observability: logs, metrics, tracing | observability **15%** middle; Skillenai 16.5%; Bees (New Relic/Datadog, production troubleshooting), Sber (Prometheus/Grafana/ELK) |
| Performance basics: slow queries, pools, timeouts | Netomi performance profiling; Sber query plans and performance tuning |
| Simple system design and writing decisions | Netomi asks for end-to-end ownership at mid; ADRs are the architect bridge in §7 |
| Owning a feature end to end | Netomi states it explicitly for SDE II |

**Verdict on coverage:** strong. Of the roughly 20 skills that keep reappearing across the six postings, the path covers about 17. Its two best cards are the ones most bootcamps skip: **idempotency and transactions** (Stage 2) and **Testcontainers** (Stage 2). Both are must-haves at middle level, and both are where Tuyen's QA background gives an unfair advantage.

### (b) What the posts ask for that the path is missing

| Gap | Evidence | Where it should go |
|---|---|---|
| **JPA / Hibernate ORM, and the N+1 problem** | Zorky: Hibernate/JPA is standard, and "Spring Boot 3 + Spring Data JPA" appears in 95%+ of modern Java projects; Métrica names Spring Data JPA in the stack; §6 lists JPA N+1 as a standard backend interview topic | Stage 1, right after the first CRUD API — it is the first thing that goes wrong in a real repository |
| **Maven or Gradle** | Addeco "Maven"; junbrain "Maven/Gradle"; Zorky notes Maven is still ahead of Gradle in Java shops | Stage 1, day one — the build tool is how the project is created |
| **Mockito (unit-test isolation)** | Métrica "JUnit + Mockito"; Zorky "JUnit 5 + Mockito + Testcontainers"; junbrain lists JUnit/Mockito as the bonus | Stage 1, alongside the first tests |
| **Kubernetes basics** | freehire: **8% junior, 28% middle**; Jobpedia junior lists Kubernetes as a preferred skill at 10%; Zorky calls Docker + Kubernetes standard; Addeco requires Docker + Kubernetes + Helm | End of Stage 2 or start of Stage 3 — it is the biggest junior-to-middle jump in the dataset |
| **Microservices and service boundaries** | freehire: microservices 9% junior, **27% middle**; Skillenai: 16.2% of backend postings and **46.2% of Java Backend Developer postings**; Netomi, Bees and Métrica all list microservices | Stage 3 — messaging basics is the natural doorway |
| **OpenAPI / API-first design and contract tests** | Métrica: OpenAPI/API-first is a **required** skill; contract tests a nice-to-have | Stage 2, alongside the payments API |
| **Static analysis (SonarQube) and code-quality gates** | Métrica: GitHub Actions + SonarQube | Stage 2, as part of the CI pipeline |
| **Reading SQL query plans (EXPLAIN)** | Sber "query plans"; Métrica "query optimisation"; Jobpedia SE postings list SQL at 21% overall | Stage 3, inside "performance basics" — the path says "slow queries" but not "read the plan" |
| **gRPC** | Sber lists REST/gRPC together; the baseline called gRPC a mid-level nice-to-have | Optional Stage 3 lesson |
| **Bash / shell scripting** | Addeco; it is the practical glue for local Docker, migrations and CI | Stage 1, half a lesson |
| **English at a stated level** | Addeco B2/C1, Métrica B1+. English is the gate for the remote salaries in §5 | Not a lesson — a standing habit, noted so it is not discovered at interview time |
| **AI coding tools as a stated plus** | Sber lists AI tooling as a plus; freehire's broad "ai" keyword appears in **27%** of junior and **35%** of middle postings (broad keyword, treat as directional) | Fold into Stage 1 habits, not a separate lesson |
| **Fintech money rules: BigDecimal, audit log, webhook security, data masking, payment statuses, PCI DSS basics** | Neocode, a middle fintech posting, lists all of these; the baseline already flagged "proving correctness under failure" and payments domain depth as the senior differentiator | Stage 2, into the payments project — the path already builds payments, so this is a content upgrade, not a new stage |
| **NoSQL awareness** | freehire middle: nosql 14%, mysql 18%; a Vietnam bank backend listing in this window names Redis/MongoDB/MySQL/Oracle together | Stage 3, one comparison lesson |
| **Legacy context: Java EE / EJB, Oracle** | A Java EE (EJB) developer role appeared in this window's alerts; Zorky: Oracle still common in banks | Not for the path — but worth knowing why bank codebases look the way they do |

### (c) What the path teaches that the posts rarely ask for

These are not wasted, but they should be taught as **depth for interviews and for the job after next**, not as things that get a junior CV past a screen. Every claim below is about the six postings and the surveys read in this window.

| Path element | Reality in the postings |
|---|---|
| **Flyway by name** | None of the six postings named Flyway. They say "migrations" (Zorky) or describe the database work generically. Teaching Flyway is right — it is the standard tool — but do not expect the word to match a keyword search |
| **Isolation levels by name** | No posting named an isolation level (READ COMMITTED, REPEATABLE READ, SERIALIZABLE). They say "transactions" (Neocode) and "idempotency". The theory is what lets Tuyen answer the interview question, not what gets the CV read |
| **Outbox and saga patterns** | Métrica lists outbox and idempotent consumer as **nice-to-have**, not required. No junior or mid posting read here required them. They matter at senior and in interviews (§6), which is how the path should frame them |
| **Kafka internals depth: consumer lag, rebalancing, exactly-once semantics** | The postings ask for "Kafka in production (consumers, topics, partitions)". None named consumer lag, rebalancing or EOS. Skillenai shows Kafka in 18.2% of backend postings, so it is a minority skill — a strong differentiator, not a baseline requirement |
| **Explicit system-design practice and written ADRs** | Netomi asks for end-to-end ownership; no posting read here asked for ADRs. The baseline and §7 put ADRs at architect level. Keep it as the Phase 4 bridge, not a mid-level requirement |
| **Background jobs and schedulers as their own topic** | No posting in this window named them explicitly. They are usually implied by "messaging" or "async work" |
| **Caching strategy depth (eviction, stampede, write-through vs write-behind)** | Postings name **Redis** (13–14%) but none described a strategy. Teach the strategy in a lesson; do not build the path around it |
| **Deep concurrency beyond the basics** | Java concurrency appears at the level of "collections, streams, concurrency basics" (Sber). Advanced JVM and concurrency tuning is a senior ask per Zorky's roadmap |

### What I would change in the path

1. **Add JPA/Hibernate and the N+1 problem to Stage 1.** The single biggest omission: it is universal in Java shops and a standard interview question.
2. **Name the build tool (Maven) and Mockito explicitly** in Stage 1. An hour each to teach, and both appear verbatim in junior postings.
3. **Move Kubernetes basics to the end of Stage 2**, not Stage 3. It is the sharpest junior-to-middle jump in the data (8% → 28%).
4. **Put the fintech money rules into the Stage 2 payments project.** BigDecimal, audit log, webhook security and idempotency keys turn the project from "a CRUD app with retries" into "a payments service", which is what the fintech postings screen for.
5. **Keep outbox, saga and Kafka internals, but label them "interview depth".** They are nice-to-haves in postings and required in senior interviews. That is a different kind of value, and saying so out loud stops Tuyen feeling behind when a junior posting does not mention them.

---

## 10. Key resources (official docs and courses)

1. **Confluent Developer courses** (free): Kafka 101, Kafka internals, transactions and EOS: https://developer.confluent.io/courses/
2. **Apache Kafka docs: message delivery semantics**: https://kafka.apache.org/documentation/#semantics
3. **Spring for Apache Kafka reference** (retries, DLT, transactions): https://docs.spring.io/spring-kafka/reference/
4. **RabbitMQ: reliability guide + dead-letter exchanges**: https://www.rabbitmq.com/docs/reliability · https://www.rabbitmq.com/docs/dlx
5. **microservices.io (Chris Richardson): transactional outbox and saga**: https://microservices.io/patterns/data/transactional-outbox.html · https://microservices.io/patterns/data/saga.html
6. **PostgreSQL: transaction isolation**: https://www.postgresql.org/docs/current/transaction-iso.html
7. **Testcontainers guides** (Java/Go, Kafka/Postgres/RabbitMQ): https://testcontainers.com/guides/
8. **Designing Data-Intensive Applications** (Kleppmann), the architect-track book: https://dataintensive.net/
9. **new** — **Flyway docs** (migrations, versioning, repeatable migrations): https://documentation.red-gate.com/flyway
10. **new** — **Playwright Test Agents** (planner, generator, healer) and the MCP server: https://playwright.dev/docs/test-agents

Optional extras: [A Tour of Go](https://go.dev/tour/) · [Quarkus Kafka guide](https://quarkus.io/guides/kafka) · [Playwright API testing](https://playwright.dev/docs/api-testing) · [Jepsen consistency models](https://jepsen.io/consistency) · [System Design Primer](https://github.com/donnemartin/system-design-primer)

*(All URLs returned HTTP 200 on 28 Oct 2026, except the ITviec Quarkus tag page, which returned 404 and is reported as such above.)*

---

## Caveats

- **This is a catch-up report.** It covers 17–28 Oct after the 23 Oct run failed, so the "week" is 11 days and the deltas against the baseline are 7-day comparisons from 21 Oct to 28 Oct.
- **Skillenai** measures posting mix, not hiring volume. The SDET sample is small (132), and its "Go" count may be inflated by the ambiguous word. Its all-role skill totals grow partly with index coverage, so use the *share change* figures, not the raw count growth.
- **ROLIVA** counts its own board (2,000 QA/test listings). It is the best QA-specific cloud count available, but it is one board, not the market.
- **JobRemotely** is US-weighted (566 of 687 listings) and its cloud subsample is 64 listings. Treat its percentages as directional.
- **The two cloud sources disagree on Azure versus GCP.** ROLIVA puts Azure 10% and GCP 4%; JobRemotely puts GCP 31 and Azure 23. Only the AWS-first finding is supported by both.
- **freehire** counts a skill if it appears anywhere in the posting, including as a nice-to-have, so its percentages are a ceiling rather than a bar. Its "ai" keyword is broad.
- **Mentorpiece** measures companies with an open role, not postings, so a single large employer can move the number.
- **AutomationDataCamp** covers the French market only. It is used for direction (Playwright over Selenium, AI mentions), not for Vietnam numbers.
- **ITviec counts** are a one-day snapshot (28 Oct 2026). Quarkus has no tag page.
- **ITviec salaries** are self-reported medians from 2025 survey waves; no new salary data appeared in this window.
- **The VND→USD conversion** (≈26,000) is approximate.
- **Interview topic lists** come from prep sites (secondary). CoderPad is a vendor survey of about 650 people and was not re-run this window.
- **Section 9** is based on six full postings plus four surveys. It is a reading of what junior and mid Java postings ask for, not a census. Where I had no count I wrote "in the postings I read".
- **Inbox data** is alert titles only. No personal data, recruiter names or contacts are included. 28 alerts were read read-only; no email was sent, drafted, labelled, archived or changed.
