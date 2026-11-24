# Backend Engineer Job Market 2026-11-24: Go · Spring Boot · Quarkus · Kafka · RabbitMQ

**Date:** 24 Nov 2026
**Purpose:** Backend-only market facts for Go, Spring Boot, Quarkus, Kafka and RabbitMQ roles, with extra attention to transaction and messaging skills.
**Coverage:** weekly **Backend Engineer** report. Job-alert window **14 – 24 Nov 2026** (alerts up to 13 Nov were counted in the previous report, so there is no overlap; the window is 11 days because this report moved from Friday to Tuesday); fresh postings sampled from **~15 – 24 Nov 2026**; index data as of **18 – 24 Nov 2026**.
**Builds on:** [backend-job-market-2026-11-13.md](backend-job-market-2026-11-13.md) (previous weekly report) and [backend-job-market-2026-10-30.md](backend-job-market-2026-10-30.md) (series baseline). Backend figures from the older combined reports remain in the baseline's [Earlier data](backend-job-market-2026-10-30.md#earlier-data-21-oct-and-28-oct).

> **How to read the numbers**
> - **Skillenai** = a job-posting index (90-day rolling windows; Backend Engineer page says "as of 24 Nov 2026"). It shows how often a skill shows up in postings, not total hiring. Skill pages refresh on different days (Spring Boot 18 Nov; event-driven architecture and RabbitMQ 19 Nov; Kafka 22 Nov; Quarkus 23 Nov; Go and microservices 24 Nov). The Backend Engineer page still does **not** publish an adjusted demand-share change ("comparable posting coverage is insufficient"). **New this week:** Skillenai now has a **Quarkus** page (it returned 404 in every earlier report).
> - **freehire** = a posting aggregator that splits Backend by seniority (updated 24 Nov 2026). It counts a skill if it appears *anywhere* in a posting, including as a nice-to-have, so its percentages are a ceiling. **Its coverage jumped this week** (open Backend roles 27,264 → 41,044; Middle 1,230 → 4,057; Junior 933 → 3,735). Shares moved a lot with the new mix, so the week-on-week freehire comparison below is shown but should **not** be read as a market change.
> - **ITviec counts** = live listing counts from itviec.com tag-page meta ("N Hot … jobs") on **24 Nov 2026**. Snapshot only. Work-model and seniority reads cover the first page of job cards on each tag, not the full tag.
> - **LinkedIn search snapshot:** not repeated this week. The 13 Nov snapshot (47 cards) stays the latest LinkedIn work-model read.
> - **Fresh-postings sample** = 11 public junior-to-senior backend postings dated roughly 15 – 24 Nov 2026, found by web search for remote Go / Spring Boot / Quarkus / Kafka / RabbitMQ roles. **This is a small, search-biased sample (n=11), not a census.** Every one is remote because the searches asked for remote, so it says nothing about the remote share of the market. Excluded: postings first seen before ~14 Nov (re-listed under a new date), one hybrid-only role, and one aggregator listing labelled as a demo job (not a real opening).
> - **Job-alert sample** = aggregate counts from a sample of job-alert emails, mostly job titles. No personal data, recruiter names or contacts are included.
> - **Hiring companies** = each employer in the job-alert sample and the fresh sample, classified from its own website or LinkedIn company page (new section this week).
> - Anything marked **(est.)** is an estimate or conversion made for this report. VND→USD uses about **26,000 VND/USD**, which is approximate.

---

## Top skills at a glance (24 Nov 2026)

**Backend — learn these first**
1. **Java + Spring Boot** for Vietnam and fintech — Java **27.2%** of Backend Engineer postings, down from 27.8% ([Skillenai Backend](https://skillenai.com/data/role/backend-engineer)); Spring Boot **6,671** postings across all roles, demand share **+7.6%** ([Skillenai Spring Boot](https://skillenai.com/data/skill/spring-boot)); java **54%** of junior and **53%** of middle Backend postings on freehire's new base; Java named in **6 of 11** sampled fresh postings and Spring / Spring Boot in **4 of 11**.
2. **REST API design** — api **50%** of junior and **68%** of middle Backend postings, rest **34% / 39%** ([freehire junior](https://freehire.me/insights/roles/backend/junior), [freehire middle](https://freehire.me/insights/roles/backend/middle)); REST, gRPC or API design named in **9 of 11** sampled postings.
3. **PostgreSQL + SQL** — PostgreSQL **24.2%** of Backend Engineer postings (was 23.9%); **4 of 11** sampled postings name PostgreSQL and one (senior) asks for writing transactions and handling migrations.
4. **Kafka (with RabbitMQ as the second broker)** — Kafka **18.7%** of Backend Engineer postings; in the fresh sample **9 of 11** name a message broker or queue: Kafka 6, RabbitMQ 3 (counting nice-to-haves). One mid posting asks for Kafka "delivery guarantees, durability, and idempotency" in plain words.
5. **Distributed systems / microservices + Kubernetes** — distributed systems **25.6%**, Kubernetes **31.0%**, microservices **18.5%** of Backend Engineer postings; microservices in **5 of 11** and Kubernetes in **4 of 11** sampled postings.

*Python (36.1%), AWS (33.4%) and Go (27.7%) remain higher in the global Backend Engineer list. Go now leads Java by 0.5 points (was 0.1). They matter for the global remote market; the order above weights Vietnam and the Java/Spring stack.*

---

## What changed this week (13 Nov → 24 Nov 2026)

**Job-alert sample: 28 alerts.** A sample of 28 job-alert emails dated 14 – 24 Nov was counted. **7 were backend-relevant** (digests from a remote Java backend search set to Ho Chi Minh City). The other 21 were QA/test, industrial or process automation, freelance gig digests, or unrelated. One digest from an "automation engineer" search carried a manufacturing-test software title and is counted as non-backend. All were automated digests; none came from a named recruiter and none of the backend-relevant alerts stated a salary range.

**The five changes worth acting on**

| # | Change | 13 Nov | 24 Nov | Read |
|---|---|---|---|---|
| 1 | **Event-driven architecture slowed for the first time in the series** | 3,692 postings, share **+42.6%** | **4,071**, share **+37.3%** | Still the fastest-rising backend signal by far, but the acceleration seen in five reports running has stopped. Kafka also eased: **9,517 (+7.4%) → 10,176 (+6.1%)**. |
| 2 | **Go overtook Spring Boot as the fastest-gaining stack** | Go 16,992 (+8.4%), Spring Boot 6,372 (+10.0%), microservices 13,087 (+9.9%) | **Go 18,785 (+9.3%)**, **Spring Boot 6,671 (+7.6%)**, **microservices 13,505 (+4.5%)** | First report where Go's share change is above Spring Boot's. In the Backend Engineer list Go leads Java **27.7% vs 27.2%** (was 27.9% vs 27.8%). |
| 3 | **freehire coverage jumped; level shares reshuffled** | Middle 1,230 open; kafka 25%, rabbitmq 13%, microservices 39%, spring 28%, java 45% | **Middle 4,057 open; kafka 14%, rabbitmq not in top 40, microservices 33%, spring 33%, java 53%** | Total open Backend roles **27,264 → 41,044** and every level now shows positive 30-day growth (Senior **+13,288**). A one-week jump this size is a coverage change, so the share moves are not a market signal. Junior: kafka **7% → not in top 40**, java **41% → 54%**. |
| 4 | **Job-alert sample: smaller backend share, no remote titles, outsourcing-heavy** | 9 of 20 alerts backend-relevant (45%); 4 remote titles; 1 Go title | **7 of 28 (25%)**; **0 remote titles**; **0 Go titles** | **16 unique backend cards** from 12 employers; outsourcing or offshore firms posted **9 of 16** (DXC 3, Tinhvan 3). Kafka, RabbitMQ and Quarkus still never appear in alert titles. |
| 5 | **Fresh sample: more brokers named, less pay stated; Quarkus now indexed** | Broker in 8 of 11 (Kafka 6, RabbitMQ 1); pay stated in 6 of 11; Quarkus page 404 | **Broker in 9 of 11 (Kafka 6, RabbitMQ 3)**; **pay stated in 2 of 11**; **Skillenai Quarkus: 230 postings** | Kafka ≈ **4.8×** RabbitMQ in all-roles postings (10,176 vs 2,127, est.; was ≈5.1× with a stale RabbitMQ page). Open to Vietnam-based engineers: **1 of 11** (same as last week). |

**Backend skill shares, 13 Nov → 24 Nov** (Skillenai, Backend Engineer; 2,926 → **3,142** postings; shares are of all postings in the window, so treat moves under 0.5 points as rounding):

| Skill | 13 Nov | 24 Nov | Skill | 13 Nov | 24 Nov |
|---|---|---|---|---|---|
| Python | 35.2% | **36.1%** | TypeScript | 19.3% | 19.6% |
| AWS | 32.7% | **33.4%** | Kafka | 18.9% | 18.7% |
| Kubernetes | 31.2% | 31.0% | Microservices | 18.3% | 18.5% |
| Go | 27.9% | 27.7% | SQL | 17.9% | 17.7% |
| Java | 27.8% | **27.2%** | Observability | 15.9% | **16.4%** |
| Distributed systems | 25.1% | **25.6%** | Redis | 15.9% | not in top 15 |
| PostgreSQL | 23.9% | 24.2% | Node.js | not in top 15 | 15.1% |
| CI/CD | 22.1% | **22.7%** | Docker | 22.5% | 22.4% |

Over the 11 days the biggest moves are **Python +0.9 points, AWS +0.7, CI/CD +0.6, Java −0.6**. Distributed systems and observability each rose 0.5. Redis dropped out of the published top 15 and Node.js entered.

**Messaging and stacks, all roles (Skillenai 90-day totals).** Totals grow partly because the index grows, so read the *share change*, not the raw count:

| Signal | 13 Nov | 24 Nov | Share change (latest page) |
|---|---|---|---|
| Kafka postings | 9,517 | **10,176** | **+6.1%** (was +7.4%) |
| RabbitMQ postings | 1,879 (5 Nov page) | **2,127** (19 Nov page) | not published |
| Event-driven architecture | 3,692 | **4,071** | **+37.3%** (was +42.6%) |
| Microservices | 13,087 | **13,505** | **+4.5%** (was +9.9%) |
| Go | 16,992 | **18,785** | **+9.3%** (was +8.4%) |
| Spring Boot | 6,372 | **6,671** | **+7.6%** (was +10.0%) |
| Quarkus | page 404 | **230** (23 Nov page) | not published |

**freehire Middle Backend, 13 Nov → 24 Nov** (1,154 → **3,970** postings listing skills; coverage change, see the note above): kafka 25% → **14%**, rabbitmq 13% → **not in top 40**, event-driven 20% → **11%**, microservices 39% → **33%**, spring 28% → **33%**, java 45% → **53%**, postgresql 30% → **22%**, kubernetes 29% → **19%**, ci-cd 40% → **30%**, observability 19% → **20%**, distributed systems 17% → 17%, redis 15% → **not in top 40**, api 71% → **68%**.

**ITviec Vietnam, 13 Nov → 24 Nov 2026** (live listing counts, same tag pages):

| Tag | 13 Nov | 24 Nov |
|---|---|---|
| java | 90 | **85** |
| backend developer | 75 | **72** |
| spring boot | 45 | **42** |
| golang | 25 | **24** |
| microservices | 35 | **36** |
| kafka | 16 | **19** |
| quarkus | 404 (≈0) | **404 (≈0)** |
| rabbitmq | 404 (no tag page) | **404 (no tag page)** |

([java](https://itviec.com/it-jobs/java), [backend developer](https://itviec.com/it-jobs/backend-developer), [spring-boot](https://itviec.com/it-jobs/spring-boot), [golang](https://itviec.com/it-jobs/golang), [microservices](https://itviec.com/it-jobs/microservices), [kafka](https://itviec.com/it-jobs/kafka))

**Job-alert sample (aggregate, 14 – 24 Nov):**
- **7 of 28 alerts (25%) were backend-relevant**, down from 45%. They carried **17 backend or backend-adjacent title cards, 16 unique** (one full-stack Java title repeated across two digests).
- Titles (aggregate): Backend Engineer, Backend Java Developer, Backend (Java/.NET) Developer, Java Developer (×2 employers), Java Developer (3+ YOE), Java Developer (4–5 years, Vietnamese-language title), Java Developer (Mandarin), Java Software backend, Middle Java Developer, Senior Java Developers, Senior/Expert Java Developer, Senior Backend Developer, Senior Backend Software Engineer II, Senior Fullstack (Java/React) Developer, Junior Cloud Native Developer, Forward Deployed Engineer.
- **Seniority in the 16 unique titles:** 1 junior, 3 middle ("Middle", "3+ YOE", "4–5 years"), 5 senior, 7 unstated.
- **Remote: 0 titles** explicitly remote (was 4 from 3 employers). All cards were Ho Chi Minh City listings; one senior backend title from a US product company is listed by the employer as hybrid (onsite four days a week).
- **Go, Kafka, RabbitMQ and Quarkus: zero hits in alert titles** (Go had one last week). Spring Boot also did not appear in title text. Alerts are title digests; stack detail lives in the body.
- **No salary ranges were stated in any backend-relevant alert.**
- **Who posts:** outsourcing or offshore firms posted **9 of the 16** unique cards (see Hiring companies below).

---

## Hiring companies (job-alert sample 14 – 24 Nov, and fresh-postings sample)

Each company is classified from its own website or its LinkedIn company page (or, where noted, the company's own words in its posting). "–" means the source does not state it. Types: **product** company; **consultancy or agency**; **outsourcing or offshore service**; **staffing or recruiter** posting for an unnamed client; **other** (bank, insurer, retailer, in-house IT); **unclear** where sources are missing or conflict.

| Company | Sample | Type | Industry | Size | HQ | Roles posted (backend cards / postings) | Source |
|---|---|---|---|---|---|---|---|
| DXC Technology | Alerts | Outsourcing or offshore service | Enterprise IT services | – | – | Senior Java Developers; Middle Java Developer; Java Developer (Mandarin) | [site](https://dxc.com/) |
| Tinhvan Software | Alerts | Outsourcing or offshore service | Software outsourcing, offshore and on-site teams (Japan focus) | – | Vietnam | Backend (Java/.NET) Developer; Java Developer; Java Developer (4–5 years) | [site](https://tso.tinhvan.com/en/services/outsourcing-services) |
| Axon Active | Alerts | Outsourcing or offshore service | Dedicated offshore development teams, Swiss-owned | – | Switzerland (owner) / Vietnam | Senior Fullstack (Java/React) Developer (2 digests) | [site](https://axonactive.com/about/) |
| Endava | Alerts | Outsourcing or offshore service | Technology services | 11,479 staff (2025 sustainability report) | UK (London) | Junior Cloud Native Developer | [investors](https://investors.endava.com/about-us), [2025 report](https://www.endava.com/hubfs/Endava%202024/Who%20We%20Are/sustainability/2025-Endava-Sustainability-Report-04.09.2025.pdf), [LinkedIn](https://linkedin.com/company/endavavietnam) |
| fram^ | Alerts | Outsourcing or offshore service | Custom software, dedicated teams | – | Sweden / Vietnam | Forward Deployed Engineer | [site](https://wearefram.com/our-story/) |
| LINE Technology Vietnam | Alerts | Product company (LY Corporation development centre) | Messaging and internet services | – | Japan (group) | Backend Engineer | [site](https://vietnamdevcenter.linecorp.com/en/about) |
| One Mount | Alerts | Product company | Digital ecosystem: finance, retail, real estate | – | Vietnam | Senior/Expert Java Developer | [site](https://onemount.com/), [LinkedIn](https://linkedin.com/company/one-mount) |
| Axon | Alerts | Product company (Ho Chi Minh City R&D hub) | Public-safety technology | – | US | Senior Backend Software Engineer II (hybrid) | [careers](https://www.axon.com/careers/job/7336166003) |
| Colonial Surety Company | Alerts | Other (insurer) | Insurance | 11–50 | US | Backend Java Developer - VN | [LinkedIn](https://www.linkedin.com/company/colonial-surety-company/) |
| UNIT Technology Corporation | Alerts | Unclear (own site lists its own finance/banking software and IT outsourcing) | Finance, banking and insurance software | – | Vietnam | Java Developer (3+ YOE) | [site](https://unit.com.vn/introduction/), [LinkedIn](https://www.linkedin.com/company/unit-corp/) |
| IT Software Tech | Alerts | Unclear (own site has no readable description) | – | – | – | Java Software backend | [site](https://itsoftwaretech.com) |
| Reliccell | Alerts | Unclear (own site only says "Fresh Startup") | – | – | – | Senior Backend Developer | [site](https://reliccell.vn) |
| Paddle | Fresh #7 | Product company | Payments infrastructure (merchant of record) | – | UK (London) | Software Engineer (Go) | [about](https://www.paddle.com/about) |
| Boosta | Fresh #4 | Product company (tech holding; role is for its payments business FlintN) | Digital businesses, payments | 800+ experts, 15+ businesses | – | Middle Software Engineer – Backend (Platform) | [site](https://boosta.com/en/) |
| iPlayTech | Fresh #2 | Product company (payment orchestration platform, per its own ad) | Payments for iGaming | – | – | Junior Java Developer (Backend / Integrations) | [LinkedIn](https://www.linkedin.com/company/iplaytech), [ad](https://djinni.co/jobs/858224-junior-java-developer-backend-integrations-ig/) |
| BJAK | Fresh #11 | Product company | Insurance platform, consumer finance app | – | Malaysia | Backend Developer (remote, Vietnam) | [about](https://bjak.my/en/about-us) |
| Consultec-TI | Fresh #6 | Consultancy or agency | Custom software, integration, staff augmentation | – | – | Java / Quarkus Microservices Developer | [site](https://consultec-ti.com/) |
| Avion Labs | Fresh #8 | Consultancy or agency | Custom software and digital agency | – | – (remote-first) | Senior Backend Engineer (Go / PostgreSQL) | [site](https://avion-labs.com/) |
| Integral Solutions | Fresh #5 | Outsourcing or offshore service ("IT competency outsourcing"; role for an unnamed international client) | Data, AI and software specialists | – | Poland | Kafka Developer (Event Streaming Engineer) | [site](https://integralsolutions.pl/en/IT-competency-outsourcing/) |
| Amaze Systems | Fresh #3 | Staffing or recruiter (unnamed client) | IT staffing and talent consulting | – | US | Java Developer (Spring Boot, Kafka, LLM) | [site](https://amaze-systems.com/services/talent-consulting) |
| Slasify | Fresh #9 | Staffing or recruiter (contractor-of-record for an unnamed US-listed client) | HR technology, contractor payments | – | Singapore | Golang Software Engineer (6-month contract) | [site](https://slasify.com/about-us) |
| Employer not named (taskenzo listing) | Fresh #1 | Unclear (employer not named) | Fintech (transfers, AML teams, per the ad) | – | – | Software Engineer – Golang Junior / Junior+ | [posting](https://taskenzo.space/remote-jobs/software-engineer-golang-junior-junior) |
| Employer not named (taskenzo listing) | Fresh #10 | Unclear (employer not named) | – | – | – | Junior Backend Developer | [posting](https://taskenzo.space/remote-jobs/junior-backend-developer) |

**Split by type (23 employers):** product **7 (30%)** · outsourcing or offshore **6 (26%)** · unclear **5 (22%)** · consultancy or agency **2 (9%)** · staffing or recruiter **2 (9%)** · other **1 (4%)**.
- *Job-alert sample (12 employers, 16 cards):* outsourcing **5** employers / **9 cards (56%)** · product 3 / 3 · unclear 3 / 3 · other 1 / 1 · consultancy 0 · staffing 0.
- *Fresh sample (11 postings):* product **4** · consultancy 2 · staffing 2 · unclear 2 · outsourcing 1.

**Week over week:** the previous backend report ([13 Nov](backend-job-market-2026-11-13.md)) had no company-type split, so this is the **first split in the backend series**; next week's report compares against it.

**Read:** the two samples show different employer mixes. In the Ho Chi Minh City job-alert sample, outsourcing and offshore firms post more than half of the backend cards and no title is remote. In the remote fresh sample, product companies (three of them in payments) lead, and two of the 11 postings come through staffing or contractor-of-record firms for unnamed clients. Five employers could not be classified from their own sources and are marked unclear rather than guessed.

---

## 0. Bottom line

1. **Event-driven architecture is still the fastest-rising backend skill, but it slowed.** Share change **+37.3%** (4,071 postings), down from +42.6%, the first slowdown in the series. Kafka eased to **+6.1%** (from +7.4%) and microservices to **+4.5%** (from +9.9%).
2. **Spring Boot remains the stack to lead with in Vietnam; Go gains fastest globally.** Go's share change (**+9.3%**) passed Spring Boot's (**+7.6%**) for the first time, and Go leads Java 27.7% vs 27.2% in the Backend Engineer list. In Vietnam, Java (**85**) and Spring Boot (**42**) listings still far exceed Go (**24**) and Quarkus (≈0).
3. **Messaging is written into most fresh postings.** **9 of 11** name a broker or queue (Kafka 6, RabbitMQ 3). One mid posting spells out Kafka delivery guarantees, durability, idempotency, and backward-compatible changes during canary releases; one senior posting asks for PostgreSQL transactions and RabbitMQ queues.
4. **Vietnam is still office-first.** First-page job cards on kafka, golang and spring-boot show **0 remote** for the fourth report running (kafka 17 office / 2 hybrid; golang 14 / 6; spring boot 17 / 3), and no backend alert title was remote. Remote options for Vietnam-based engineers in the fresh sample: **1 of 11** (a product company hiring remote in Vietnam).
5. **Pay: no new local survey.** No backend alert stated a salary. Only **2 of 11** fresh postings stated pay (€35–45/hour B2B in Poland; $60–85K/yr contract listed for the US). Two ITviec first-page titles state caps (up to $3,200 for a mid/senior Java role; up to 28M VND for a Java developer).

---

## 1. Most-demanded skills, with frequency signals

### A. Global: Skillenai, "Backend Engineer" title, 3,142 postings, 90 days to 24 Nov 2026
([source](https://skillenai.com/data/role/backend-engineer))

| Skill | Postings | Share | Skill | Postings | Share |
|---|---|---|---|---|---|
| Python | 1,134 | 36.1% | TypeScript | 615 | 19.6% |
| AWS | 1,048 | 33.4% | **Kafka** | **589** | **18.7%** |
| Kubernetes | 974 | 31.0% | **Microservices** | **581** | **18.5%** |
| **Go** | **870** | **27.7%** | SQL | 557 | 17.7% |
| **Java** | **855** | **27.2%** | Observability | 515 | 16.4% |
| **Distributed systems** | **803** | **25.6%** | Node.js | 474 | 15.1% |
| PostgreSQL | 759 | 24.2% | | | |
| CI/CD | 712 | 22.7% | | | |
| Docker | 704 | 22.4% | | | |

- **Demand share change:** still not published on the 24 Nov page (insufficient comparable coverage). The −9.0% figure from 30 Oct is therefore **not updated**.
- **Top posters:** GitLab 162, Grafana Labs 117, CLERA 60, Stripe 50, Wise 50, Vinted 48, Spotify 31, Verkada 30, Binance 27, Xsolla 22. Remote-friendly product companies; the top two are unchanged.
- **Top metros:** Berlin 3.5%, London 3.2%, New York City 3.1%, San Francisco 3.1%, Tel Aviv 1.8%, Bengaluru 1.5%.
- **Career flows:** Backend Engineer hires come mainly from Software Engineer (104 moves in, 57 out). Unchanged.

### B. By seniority: freehire, open Backend postings, updated 24 Nov 2026

| Level | Open postings | Skill leaders |
|---|---|---|
| **Junior** | **3,735** (3,366 list skills) | **java 54%**, api 50%, python 41%, rest 34%, sql 32%, git 28%, mysql 24%, php 19%, agile 19%, nodejs 18%, **spring 18%**, **microservices 18%**, cloud 17%, docker 17%, csharp 15%, postgresql 15%, ci-cd 14%, mongodb 14%, ai 13%, aws 10%, kubernetes 8%, redis 7%, unit-testing 6% (kafka not in top 40) |
| **Middle** | **4,057** (3,970 list skills) | api 68%, **java 53%**, rest 39%, cloud 37%, aws 35%, **spring 33%**, **microservices 33%**, ci-cd 30%, docker 26%, sql 26%, git 26%, ai 23%, postgresql 22%, **observability 20%**, python 19%, **kubernetes 19%**, **distributed systems 17%**, azure 17%, mysql 16%, mongodb 15%, devops 14%, **kafka 14%**, kotlin 13%, unit-testing 12%, **event-driven 11%**, graphql 10%, api-design 8% (rabbitmq and redis not in top 40) |

([freehire junior](https://freehire.me/insights/roles/backend/junior), [freehire middle](https://freehire.me/insights/roles/backend/middle), [freehire seniority split](https://freehire.me/insights/roles/backend))

- **The junior-to-middle jump** on the new base: Kubernetes **8% → 19%**, microservices **18% → 33%**, CI/CD **14% → 30%**, AWS **10% → 35%**, Kafka **not in junior top 40 → 14%**, observability **not in junior top 40 → 20%**, Spring **18% → 33%**. The direction matches earlier reports (cloud, Kubernetes, messaging and observability separate middle from junior); the sizes differ because the posting base changed.
- **Seniority census, 24 Nov:** 41,044 open Backend roles — Senior 44,850, Lead 5,278, **Middle 4,057**, **Junior 3,735**, Staff 2,350, Intern 1,687, Principal 618, C-level 125 (levels sum above the total, as published). 30-day growth: Senior **+13,288**, Middle **+1,441**, Lead +1,181, **Junior +898**, Staff +472; only C-level fell (−28). Last week every level was negative. A swing this large in 11 days points to a change in what freehire crawls, so prefer per-level shares within one week over week-on-week totals.
- **Competition and speed:** median time a Backend posting stays open **28 days** (was 30 on 13 Nov; "up from 23 days" in the previous 30), **25,203** new postings in the last 30 days (was 17,704), and **6.1** page views per open posting a month (was 5.6).

### C. Fresh postings sample: 11 remote backend postings, ~15 – 24 Nov 2026

*Small, search-biased sample (n=11). Use it for what employers write in junior/mid postings right now, not for market shares.*

| # | Role (employer) | Posted | Level | Where | Stack named | Pay stated |
|---|---|---|---|---|---|---|
| 1 | [Software Engineer – Golang Junior / Junior+ (employer not named, via taskenzo)](https://taskenzo.space/remote-jobs/software-engineer-golang-junior-junior) | 22 Nov | Junior (1+ yr) | Remote, GMT+0 to GMT+5 (hubs in Serbia, Georgia, Kazakhstan) | **Go**, **Kafka**, AWS, EKS, PostgreSQL, MongoDB, Redis, tests; uses AI tools | No |
| 2 | [Junior Java Developer, Backend / Integrations (iPlayTech, via Findyet / Djinni)](https://findyet.devjoys.com/jobs/junior-java-developer-backend-integrations-igaming-iplaytech-3r2hljhg) | 16 Nov | Junior (1–2 yr) | Remote, Europe (Ukraine/EU overlap) | Java 23, Spring Boot (nice), Apache Camel, REST, SQS, Redis, PostgreSQL, AWS/EKS, Helm, Grafana, GitLab CI/CD; nice: **RabbitMQ** or SQS, Docker/Kubernetes | No |
| 3 | [Java Developer (Amaze Systems, via remoteitjobs)](https://www.remoteitjobs.app/job/netrolynx-ai-java-developer-remote) | 16 Nov | Listed "Junior"; text asks for substantial experience (unclear) | Remote, US (in-person client interview required) | Java, **Spring Boot**, Spring Cloud, microservices, REST/gRPC, Python, **Kafka** / event-driven, LLM orchestration, vector DBs, MCP | No |
| 4 | [Middle Software Engineer – Backend, Platform (Boosta / FlintN, via First Monday)](https://firstmonday.ai/jobs/middle-software-engineer-backend-platform-boosta-13f7bd54) | 16 Nov | Mid | Remote, 21 listed countries (not Vietnam) | Java, PostgreSQL, **Kafka** (delivery guarantees, durability, **idempotency**), retries, microservices, CI/CD, **canary releases with backward-compatible changes**, observability, unit + integration tests, TDD/BDD, AI tools | No |
| 5 | [Kafka Developer / Event Streaming Engineer (Integral Solutions, via Pracovite)](https://www.pracovite.pl/praca/kafka-developer-integral-solutions) | 15 Nov | Mid (2+ yr Kafka) | Remote, Poland (B2B) | Java, Spring, **Kafka** Streams / Connect / **Schema Registry**, Kafka CLI, ELK, Oracle SQL / PL/SQL, REST; nice: Confluent Cloud | **€35–45/hour net B2B** |
| 6 | [Java / Quarkus Microservices Developer (Consultec-TI, via Himalayas)](https://himalayas.app/companies/consultec-ti/jobs/java-quarkus-microservices-developer) | 15 Nov | Mid (2+ yr) | Remote (region not stated; Spanish-language ad) | Java 17+, **Quarkus** / Jakarta EE, microservices, REST, OpenAPI, SQL, Docker, Kubernetes, OpenShift, Maven, SonarQube; nice: IBM MQ, **Kafka**, SOAP | No |
| 7 | [Software Engineer (Go) (Paddle, via PickedJobs)](https://pickedjobs.com/jobs/paddle-software-engineer-go-7642fac5-d94b-4157-8b19-79a7dbc115ea) | 20 Nov | Mid | Remote, UK / Europe hubs | **Go**, AWS, API design, well-tested code, correctness with financial data | No |
| 8 | [Senior Backend Engineer, Go / PostgreSQL (Avion Labs)](https://avion-labs.com/careers/senior-backend) | 18 Nov | Senior (5+ yr, 3+ Go) | Remote | **Go**, PostgreSQL (**transactions**, migrations, query tuning), Redis or **RabbitMQ** queues, REST, microservices, Docker, clean architecture, tests | No ("competitive") |
| 9 | [Golang Software Engineer, 6-month contract (Slasify for an unnamed client, via WFH Beacon)](https://wfhbeacon.up.railway.app/job/golang-software-engineer-6-month-remote-contract-5) | 22 Nov | Mid (3+ yr) | Remote, listed US ("work from any location"; US Eastern meetings) | **Go** (goroutines, channels), REST/gRPC, microservices, testing; nice: containers, Kubernetes, AWS/GCP/Azure, **Kafka / RabbitMQ** | **$60–85K/yr** |
| 10 | [Junior Backend Developer (employer not named, via taskenzo)](https://taskenzo.space/remote-jobs/junior-backend-developer) | 24 Nov | Junior (1–2 yr) | Remote (region not stated) | Java, **Go**, **Spring Boot**, relational + non-relational DBs; plus: Terraform / AWS | No |
| 11 | [Backend Developer (BJAK, Ashby board)](https://jobs.ashbyhq.com/bjakcareer/7be3e8ec-79d6-495b-b813-7225cf9013de) | 23 Nov (board date) | Unstated ("strong production experience") | **Remote, Vietnam-based only** | APIs, databases, auth, **queues, jobs, events**, integrations, observability, data consistency; payments, transfers, KYC flows | No |

**Counts across the 11 (mentioned anywhere, including nice-to-have and "accepted alternative" languages):**

| Skill | Count | Skill | Count |
|---|---|---|---|
| **Any message broker or queue** | **9** | Java | 6 |
| REST / API (incl. gRPC) | 9 | **Kafka** | **6** |
| Tests named (unit/integration/automated) | 7 | **Go** | **5** |
| Microservices | 5 | AWS | 5 |
| PostgreSQL | 4 | **Spring / Spring Boot** | **4** |
| Observability tools or practice | 4 | Kubernetes | 4 |
| AI tools mentioned | 3 | Docker / containers | 4 |
| Redis | 3 | **RabbitMQ** | **3** |
| CI/CD | 2 | **Quarkus** | **1** |
| **Idempotency / delivery guarantees named** | **1** | **Schema Registry / schema compatibility** | **2** (#5 registry; #4 backward-compatible changes) |

- **Seniority:** Junior 3, Mid 5, Senior 1, unclear or unstated 2. Junior count unchanged (3 of 11 vs 3 of 11).
- **Remote:** 11 of 11 by search design. By region: Europe 2 (#2, #7), Poland 1, US-listed 2, GMT+0 to +5 1, 21 listed countries 1, Vietnam 1, region not stated 3 (#6, #8, #10). **1 of 11** was explicitly open to Vietnam-based engineers (#11; last week also 1 of 11).
- **Salary stated: 2 of 11** (was 6 of 11) — €35–45/hour net B2B (Poland mid, Kafka) and $60–85K/yr (6-month Go contract). Too few to summarise.
- **RabbitMQ was easier to find this week** (3 of 11 vs 1 of 11), each time as one option next to Redis, SQS or Kafka. Kafka stays at 6 of 11. Both follow what the searches surfaced, not a market shift.
- **Transaction and messaging wording in postings:** #4 asks for Kafka "message publishing and delivery guarantees, durability, and idempotency", retry logic, and "backward-compatible changes while different service versions coexist"; #8 asks for writing PostgreSQL transactions and migrations; #11 names data consistency. No posting this week names the transactional outbox (1 senior posting last week).
- **Excluded candidates:** a junior Go role whose employer board lists it as hybrid in Hamburg (an aggregator showed it as remote), an aggregator listing marked as a demo job, and roles first seen in October or early November but re-dated.

### D. Vietnam: ITviec live counts and first-page read, 24 Nov 2026

- Counts: "java" **85**, "backend developer" **72**, "spring boot" **42**, "golang" **24**, "microservices" **36**, "kafka" **19**, "quarkus" and "rabbitmq" no tag page (404, ≈0).
- **Work model, first-page cards:** kafka **17 office / 2 hybrid / 0 remote**; golang **14 / 6 / 0**; spring boot **17 / 3 / 0**. Fourth report running with 0 remote.
- **Seniority in slugs/titles, first page:** kafka 19 → **7 senior or above**, 3 middle-to-senior ranges, 1 junior-to-senior range, 1 all-level, 7 unstated. Golang 21 → **7 senior or above**, 3 middle-to-senior ranges, 1 junior-to-senior range, **1 intern**, 9 unstated, **0 junior-only**. Spring boot 21 → **12 senior or above**, 4 middle-to-senior ranges, 1 middle, 4 unstated, **0 junior**. (Same strict split as 13 Nov.)
- **Kafka-tagged titles remain Java- and finance-heavy:** banks and securities firms post Java / Spring Boot backend roles, several with Go as a second language; one bank posts junior-to-senior and all-level Java/Go roles.
- Two first-page titles state caps: a mid/senior Java role at a fintech **up to $3,200** and a Java developer role **up to 28M VND** (≈$1,080, est.).

---

## 2. Must-have vs nice-to-have vs differentiator (junior → mid → senior)

*Synthesis from the frequencies above, the 11 fresh postings and the interview sources in §6.*

| Level | Must-have | Nice-to-have | Differentiator |
|---|---|---|---|
| **Junior** | Java + Spring Boot (or Go); REST; SQL + PostgreSQL; Git; unit tests (JUnit/Mockito); Docker basics | A message queue — Kafka named in one junior Go posting, RabbitMQ/SQS as a nice-to-have in a junior Java posting; Redis; one cloud (AWS named in all three junior postings, once as a plus) | A small service that **dedupes events and retries with backoff**, tested |
| **Mid** | Spring Boot or Go in production; PostgreSQL (indexes, transactions); **one broker in depth** (Kafka or RabbitMQ): delivery guarantees, retries, **idempotent handlers**; integration tests (Testcontainers); CI/CD; Docker; one cloud | Kubernetes; observability; Redis; Quarkus or Jakarta EE; Schema Registry / Kafka Streams | **Shipping changes safely while old and new versions coexist** (backward-compatible APIs and events, canary releases); payments correctness |
| **Senior** | Distributed systems: messaging, retries, timeouts, idempotent at-least-once handlers, transactional outbox, offset-commit strategy under rebalances, the limits of exactly-once, saga, consistency trade-offs; observability; performance and concurrency; system design; on-call | Event sourcing/CQRS; Kafka Streams/Connect/Debezium; K8s operations; OAuth2/OIDC; multi-region failover | Proving correctness under failure; payments depth; ADRs and design docs |

*Change from 13 Nov: the mid row now names delivery guarantees, idempotent handlers and backward-compatible changes during canary releases, which a mid posting (#4) wrote as requirements. The junior row reflects that only one of three junior postings named Kafka this week (all three did last week). The senior row is unchanged.*

---

## 3. Messaging, transactions and distributed systems: how often, and how tested

### Frequency signals

| Signal | Number | Source |
|---|---|---|
| Kafka postings (all roles, 90d) | **10,176** (share **+6.1%** vs prior 4 weeks) | [Skillenai Kafka](https://skillenai.com/data/skill/kafka) |
| RabbitMQ postings (90d) | **2,127** → Kafka is about **4.8×** RabbitMQ (est.) | [Skillenai RabbitMQ](https://skillenai.com/data/skill/rabbitmq) |
| Event-driven architecture postings (90d) | **4,071** (share **+37.3%**) | [Skillenai EDA](https://skillenai.com/data/skill/event-driven-architecture) |
| Microservices postings (90d) | **13,505** (share +4.5%) | [Skillenai microservices](https://skillenai.com/data/skill/microservices) |
| Share of Backend Engineer postings | Distributed systems 25.6%, Kafka 18.7%, microservices 18.5%, observability 16.4% | [Skillenai Backend](https://skillenai.com/data/role/backend-engineer) |
| Share of **Middle** Backend postings (new base) | observability 20%, distributed systems 17%, **Kafka 14%**, event-driven 11%; RabbitMQ not in top 40 | [freehire middle](https://freehire.me/insights/roles/backend/middle) |
| Share of **Junior** Backend postings (new base) | Kafka and RabbitMQ not in top 40; microservices 18%, redis 7% | [freehire junior](https://freehire.me/insights/roles/backend/junior) |
| Top role for each broker | Software Engineer: 40.7% of Kafka postings, 44.1% of RabbitMQ postings; **Backend Engineer 6.0% of Kafka (606) and 10.8% of RabbitMQ (229) postings** | Skillenai Kafka / RabbitMQ |
| Roles most likely to require Kafka | CloudOps Engineer 39.1%, Distributed Systems Engineer 33.3%, Data Platform Architect 29.0%; Back-end Developer 26.8%, Java Backend Engineer 25.0%, Java Backend Developer 24.1% | [Skillenai Kafka](https://skillenai.com/data/skill/kafka) |
| Top Kafka employers | **Wise 186**, Cisco 158, **Mastercard 117**, CrowdStrike 113, SentinelOne 72, **JPMorgan 69**, Twilio 65 | [Skillenai Kafka](https://skillenai.com/data/skill/kafka) |
| Top EDA employers | **Mastercard 72, Wise 70**, CLERA 36, **Barclays 32**, EPAM 32, Bright Vision 30, State Street 27, CBA 26 | [Skillenai EDA](https://skillenai.com/data/skill/event-driven-architecture) |
| Top RabbitMQ employers (19 Nov page) | CLERA 27, Xsolla 26, Wrike 22, Cisco 22, Wise 20, Encora 20 | [Skillenai RabbitMQ](https://skillenai.com/data/skill/rabbitmq) |
| Fresh sample (n=11) | Broker or queue named in **9**: Kafka 6, RabbitMQ 3; idempotency / delivery guarantees named in **1** (mid); database transactions named in **1** (senior) | §1C |
| Vietnam | ITviec "kafka" **19**, "microservices" **36** (vs "java" 85); no RabbitMQ tag | ITviec, 24 Nov 2026 |

**Read (interpretation):**
- **Kafka is still the broker to lead with**; banks and payments companies still dominate its top employers (Wise ahead of Cisco again), matching Vietnam's finance-heavy kafka tag.
- **Event-driven architecture is still rising fast, just less fast.** The +37.3% share change is the first decline in the series; fintech and banking employers still lead EDA postings.
- **RabbitMQ is more of a backend-titled skill than Kafka.** Backend Engineer is **10.8%** of RabbitMQ postings vs **6.0%** of Kafka postings, and three fresh postings list RabbitMQ next to Redis, SQS or Kafka. It still deserves a full lesson.
- **Version coexistence is the new messaging theme this week.** One mid posting (#4) asks for backward-compatible changes while different service versions coexist during canary releases, and one (#5) names Schema Registry. The new note [Backward-compatible event changes during rolling and canary deploys](../../learning-material/backend-engineering/messaging-and-transactions/Backward-compatible%20event%20changes%20during%20rolling%20and%20canary%20deploys.md) covers the compatibility types and the upgrade order.

### How it's tested in interviews
*Unchanged from the baseline; no new interview-format survey this window. Sources are prep sites and vendor surveys (secondary). Loops published in this week's postings: intro call → technical interview with a short live-coding / pairing session → offer (#2); online assessment or practical task → technical interview → CEO round, aiming to finish within a week (#11); screening call → technical interview → interviews → reference check → offer (#4).*

1. **System design round** (38% of technical tests per [CoderPad 2026](https://coderpad.io/survey-reports/coderpad-state-of-tech-hiring-2026/)): checkout, payment, wallet transfer, notifications. Expected: local transactions, **no 2PC**, **transactional outbox**, **saga** with compensations, **retries with backoff and timeouts**, **idempotent consumers**, **DLQ**.
2. **Kafka deep-dive:** partitions and ordering; consumer groups and rebalancing; offset commits; idempotent producer and transactions; why exactly-once covers Kafka-to-Kafka only; consumer lag; **schema changes while producers and consumers run different versions**.
3. **Database and concurrency:** isolation levels and anomalies; optimistic vs pessimistic locking; "two requests withdraw from the same account"; idempotency keys on POST.
4. **Debugging scenarios:** "users get charged twice", "consumer lag grows after a deploy", "messages land in the DLQ after a schema change".

---

## 4. Go vs Spring Boot vs Quarkus

| Signal | Go | Spring Boot | Quarkus |
|---|---|---|---|
| Global postings, 90d (Skillenai, latest) | **18,785** (share **+9.3%**) ¹ | **6,671** (share +7.6%) | **230** (new page; share change not published) |
| Share of Backend Engineer postings | **27.7%** | (Java 27.2%) | n/a (Backend Engineer is 3.0% of Quarkus postings) |
| Top employers | Capital One 693, Cisco 569, **Stripe 265**, SpaceX 222, Anduril 193, NVIDIA 187, GitLab 177, CrowdStrike 164, Uber 160, Cloudflare 158 | **Mastercard 334**, Wise 138, **Barclays 117**, JPMorgan 72, Cisco 69, Capco 66 | Encora 11, Motorola Solutions 8, General Motors 7, Soficonv 6 |
| Paired skills | – | – | Java 217, Kubernetes 125, **Spring Boot 113**, Docker 97, Kafka 61 |
| Fresh sample (n=11) | **5** (#1 names Kafka; #9 lists Kafka or RabbitMQ as a plus; #8 names RabbitMQ) | **4** (Spring / Spring Boot) | **1** — remote, mid, Spanish-language ad |
| freehire junior / middle | go not in junior or middle top 40 | spring 18% junior / 33% middle | not in either top 40 |
| Vietnam ITviec (24 Nov) | **24** (was 25) | **42** (was 45; Java 85) | **≈0** (404) |
| Vietnam first-page seniority | 7 of 21 senior+, 3 ranges, 1 intern, **0 junior-only** | 12 of 21 senior+, 4 ranges, 1 middle, 0 junior | n/a |

¹ "Go" is an ambiguous word; treat Skillenai's count as an upper bound.

Sources: [Skillenai Go](https://skillenai.com/data/skill/go), [Skillenai Spring Boot](https://skillenai.com/data/skill/spring-boot), [Skillenai Quarkus](https://skillenai.com/data/skill/quarkus), [ITviec golang](https://itviec.com/it-jobs/golang), [ITviec spring-boot](https://itviec.com/it-jobs/spring-boot). SO 2026 and Java-org survey figures remain in the baseline [Earlier data](backend-job-market-2026-10-30.md#earlier-data-21-oct-and-28-oct) and were not re-pulled.

**Verdict (unchanged direction):**
- **Spring Boot is the primary stack.** Its share change eased to +7.6%, but it still leads in Vietnam (42 listings vs 24 Go) and in banks and fintech, and Java titles dominated the backend alerts again.
- **Go is the second language for remote and global product companies, and the fastest-gaining of the three.** Go's share change (+9.3%) passed Spring Boot's for the first time; three of this week's remote Go postings are junior or mid (#1, #7, #9) and one junior Java posting also accepts Go (#10). Vietnam Go listings stay senior-heavy.
- **Quarkus: concepts only.** Now measurable globally at **230** postings, about **3%** of Spring Boot's count (est.), and ≈0 in Vietnam. Almost half of Quarkus postings also name Spring Boot (113 of 230), so most Spring knowledge carries over. One or two comparison lessons remain enough.

---

## 5. Salary ranges

**No new local survey this window.** No backend-relevant alert stated a salary. The ITviec survey below is the 2025–2026 edition, unchanged. Second Talent APAC figures are carried from the 30 Oct report (still the current published pages).

### Vietnam local: ITviec 2025–2026 report, median **gross VND / month**
([ITviec report](https://itviec.com/report/vietnam-it-salary-and-recruitment-market), 1,839 respondents, surveyed May–Nov 2025)

| Role | <1 yr | 1–2 yr | 3–4 yr | 5–8 yr | >8 yr | Overall |
|---|---|---|---|---|---|---|
| **Back-end Developer** | 12.4M (≈$480) | 25.35M (≈$975) | 30.1M (≈$1,160) | **39.9M (≈$1,530)** | **54.9M (≈$2,110)** | 37.8M |
| Tech Lead | – | 45.3M | 53.85M | – | 68.45M | 51.8M (≈$1,990) |

- **Go (Second Talent rate card, vendor):** junior 20–35M, mid 35–55M, senior 55–80M VND/month ([source](https://www.secondtalent.com/developer-rate-card/golang-developer-vietnam/)). Unchanged; an upper-market estimate.
- **Paymetric Labs** lists a Vietnam back-end (Java/Go/Node.js) median of **₫41.6M/month**, range ₫37.8–42.6M, +6.5% year on year ([source](https://www.paymetriclabs.com/vn/salaries/back-end-developer-java-go-node-js)). Not re-checked this week; method and sample size not stated, so treat as a cross-check only.
- **ITviec first-page title caps (24 Nov):** mid/senior Java at a fintech **up to $3,200/month**; Java developer **up to 28M VND/month** (≈$1,080, est.). Single titles, not medians.

### Remote / international (Vietnam-based engineer, USD / month)

| Source | Back-end | Notes |
|---|---|---|
| [Second Talent APAC benchmark, Oct 2026](https://www.secondtalent.com/apac-salary-benchmark/) (vendor, carried over) | **Southeast Asia back-end family:** junior **$2,500** ($1,800–3,300), mid **$3,300** ($2,500–4,300), senior **$4,500** ($4,300–5,600), lead $5,400. **Vietnam back-end senior median: $4,600** | Remote contractor rates |
| [Second Talent, Vietnam rates 2026](https://www.secondtalent.com/resources/true-cost-outsource-software-development-vietnam/) (vendor) | Mid **$3,400–4,900** · Senior **$4,900–7,000** · Lead/Architect $7,000–9,800 | Unchanged; Go/.NET seniors +10–20% |
| Fresh sample (n=2 with pay) | Poland mid Kafka role **€35–45/hour net B2B**; US-listed 6-month Go contract **$60–85K/yr** (≈$5,000–7,100/month, est.) | Single postings; neither states it is open to Vietnam |
| Global reference ([SO 2026 comp](https://survey.stackoverflow.co/2026/work/data/compensation)) | Back-end median **$85,296/yr**; architect **$102,355/yr** | Mostly US/EU respondents; baseline figure |

**Read (est.):** unchanged from 13 Nov. A mid-level remote backend engineer in Vietnam lands around **$2,500–4,300/mo** on contractor rates and a senior around **$4,300–5,600/mo**, roughly **2–3×** the local ITviec medians for 3–8 years. English is still the gate (B1+ named in #1 and #2; strong English in #11; advanced English in the other remote listings).

---

## 6. Typical interview formats and common topics

*Unchanged from the baseline; not re-surveyed this window.*

- **Market-wide (CoderPad 2026, ~650 respondents):** algorithmic 43%, real-world scenarios 38%, system design 38%, pair programming 30%, code review 21%, debugging 19%. 46% of companies allow AI in interviews in some form; the skill signals are catching AI mistakes (66%) and explaining trade-offs (56%).
- **Backend loop (mid/senior):** recruiter → coding (DSA or a practical service task) → **system design** (seniors often get 2 rounds) → **deep-dive** (Spring internals or Go concurrency, DB and transactions, Kafka) → behavioural.
  - **Spring:** DI and bean lifecycle; `@Transactional` propagation and pitfalls; **JPA N+1**; connection pools; virtual threads.
  - **Go:** goroutines, channels, `context` cancellation, races (`-race`), worker pools (#9 names goroutines and channels outright).
  - **Messaging:** see §3.
- **Signals in this week's postings:** a junior posting runs a short live-coding / pairing session (#2); a remote-Vietnam posting starts with an online assessment or practical task and aims to make an offer within a week (#11); a US-listed role requires an in-person client interview despite being remote (#3); two postings (#1, #4) name AI tools as part of daily work, and #4 asks for judgment on what to delegate to AI and how to validate its output.
- **Vietnam specifics (est.):** outsourcing firms run a shorter loop (tech interview, English check). Foreign in-house and remote employers add system design.

---

## 7. Trends

**Event-driven architecture is still the fastest-rising backend skill, but slowing**
- Share change **+37.3%** (4,071 postings), down from +42.6% on 13 Nov, after rising from +23.9% on 30 Oct. Mastercard (72) and Wise (70) lead.
- **Implication:** a messaging-focused skill set is still aligned with where demand is moving; the slowdown is one data point, not a reversal.

**Go is now the fastest-gaining of the three stacks**
- Go share change **+9.3%** vs Spring Boot **+7.6%** and microservices **+4.5%**. Go leads Java 27.7% vs 27.2% in the Backend Engineer list. Quarkus is now indexed at 230 postings, ≈0 in Vietnam.

**Backend open-role census: coverage changed**
- freehire's Backend census rose 27,264 → 41,044 in 11 days and every level's 30-day growth turned positive. Median time-to-close 28 days; 6.1 views per posting. Treat the level shares on the new base as the reference from now on.

**AI in backend postings is broad but shallow**
- freehire "ai": **13%** junior, **23%** middle on the new base. Fresh sample **3 of 11** mention AI tooling (was 6 of 11). Broad keyword, treat as directional.

**Vietnam stays office-first and senior-heavy**
- 0 remote and 0 junior-only titles on the first pages of the golang and spring-boot tags (§1D) for the fourth report running. The kafka tag grew 16 → 19 while java fell 90 → 85. Outsourcing and offshore firms posted most backend alert cards.

---

## 8. Recommended skill priority list (junior → mid backend)

*Time estimates assume about 6–8 hrs/week of study and are estimates. Order follows the baseline backend phases; changes from this week's data are marked **new**.*

### Stage 1: Junior foundations (months 0–6)
1. **Java 21 + Spring Boot 3:** REST with OpenAPI, validation, error handling, JPA/Hibernate (including **N+1**). *(Java 54% of junior postings on freehire's new base; Java in 6 of 11 fresh postings.)*
2. **SQL + PostgreSQL transactions:** joins, indexes, isolation levels, lost update. *(PostgreSQL 24.2% of Backend Engineer postings; 4 of 11 fresh postings, one asking for transactions and migrations.)*
3. **Testing:** JUnit 5 + Mockito, then Testcontainers integration tests. *(Tests named in 7 of 11.)*
4. **Git, Maven, Docker, a CI pipeline (GitHub Actions).** *(CI/CD 14% junior → 30% middle.)*

### Stage 2: Strong junior (months 6–12)
5. **Idempotent consumer + retries with backoff, on RabbitMQ first.** Build a notifications consumer that dedupes by event id, retries with growing backoff, and records history in PostgreSQL. *(RabbitMQ in 3 of 11 fresh postings; Backend Engineer is 10.8% of RabbitMQ postings.)*
6. **Payments on the orders API with idempotency keys**, plus a first AWS deploy. *(AWS 10% junior → 35% middle.)*
7. **Auth (JWT/OAuth2 basics).**
8. **Treat AI coding tools as a habit, not a lesson.** *(Named in 3 of 11 fresh postings this week.)*

### Stage 3: Mid-level (months 12–24)
9. **Kafka with Spring for Apache Kafka:** keys and partitions, consumer groups, offset commits, retries/DLT, consumer lag. *(Kafka 14% of middle postings on the new base; 6 of 11 fresh postings.)*
10. **Reliability patterns:** transactional outbox, saga with compensations, timeouts and circuit breakers, what exactly-once does and does not cover. **new — add schema evolution and upgrade order** (BACKWARD / FORWARD / FULL compatibility; which side to deploy first; expand-then-contract for events). *(Written into a mid posting this week; see the new note.)*
11. **Kubernetes basics + observability** (structured logs, Prometheus/Grafana, OTel traces across async hops). *(Kubernetes 8% → 19%, observability → 20% from junior to middle.)*
12. **Redis caching.** *(Redis in 3 of 11 fresh postings; dropped out of Skillenai's published top 15 this week.)*
13. **Hexagonal architecture** as the structure for the payments/orders service.

### Later: Go and architect track
14. **Go** as the second language, porting one service with a Kafka consumer. *(Go 27.7% of Backend Engineer postings and the largest share gain of the three stacks; Go in 5 of 11 remote postings, four of them junior or mid.)*
15. **Quarkus**, 1–2 comparison lessons. **System design** practice (payments, wallet, notifications), ADRs.

---

## 9. Backend path vs the market

*Checked against this week's 11 fresh postings and freehire junior/middle data. The full 28 Oct gap analysis remains in the baseline [Earlier data](backend-job-market-2026-10-30.md#28-oct-gap-analysis-backend-path-vs-the-market); this section only records what this week's data adds or confirms.*

| Path element | This week's evidence | Verdict |
|---|---|---|
| Spring Boot CRUD + PostgreSQL + tests (Stage 1) | Java 6/11, PostgreSQL 4/11, tests 7/11; junior Java posting (#2) asks for Java, SQL/PostgreSQL and REST with Spring Boot as a plus | **Covered, keep** |
| API idempotency and retries (Stage 2) | One mid posting (#4) names idempotency, retry logic and delivery guarantees | **Covered; keep messaging version in Stage 2** |
| Messaging basics (Stage 3) | Brokers or queues in 9/11; Kafka 6/11, RabbitMQ 3/11; RabbitMQ is a larger share of backend-titled postings than Kafka | **Covered; teach RabbitMQ first, then Kafka** |
| Schema evolution / version coexistence | #4 asks for backward-compatible changes during canary releases; #5 names Schema Registry | **Gap: add to Stage 3 (new note this week)** |
| Observability (Stage 3) | 4/11 name observability tools or practice; 20% of middle postings | **Covered, keep** |
| Kubernetes | 4/11; 8% junior → 19% middle | **Gap from 28 Oct still stands: move basics to end of Stage 2** |
| Quarkus awareness | 1/11; 230 postings globally (new Skillenai page), ≈0 in Vietnam | **Keep as 1–2 comparison lessons, not a primary stack** |
| Outbox / saga / exactly-once limits | Not named in this week's postings (1 senior posting last week) | **Keep as interview depth; no change** |

---

## 10. Key resources (official docs and courses)

1. **Spring Boot reference**: https://docs.spring.io/spring-boot/
2. **Spring for Apache Kafka reference** (retries, DLT, transactions): https://docs.spring.io/spring-kafka/reference/
3. **Spring AMQP (RabbitMQ) reference**: https://docs.spring.io/spring-amqp/reference/
4. **RabbitMQ reliability guide + dead-letter exchanges**: https://www.rabbitmq.com/docs/reliability · https://www.rabbitmq.com/docs/dlx
5. **Confluent Developer courses** (free): https://developer.confluent.io/courses/
6. **Apache Kafka docs, message delivery semantics**: https://kafka.apache.org/documentation/#semantics
7. **microservices.io: transactional outbox, saga, idempotent consumer**: https://microservices.io/patterns/data/transactional-outbox.html · https://microservices.io/patterns/data/saga.html · https://microservices.io/patterns/communication-style/idempotent-consumer.html
8. **PostgreSQL transaction isolation**: https://www.postgresql.org/docs/current/transaction-iso.html
9. **Testcontainers guides**: https://testcontainers.com/guides/
10. **Designing Data-Intensive Applications** (Kleppmann): https://dataintensive.net/
11. **Flyway docs** (migrations, versioning, repeatable migrations): https://documentation.red-gate.com/flyway
12. **Spring for Apache Kafka, exactly-once semantics and transactions**: https://docs.spring.io/spring-kafka/reference/kafka/exactly-once.html · https://docs.spring.io/spring-kafka/reference/kafka/transactions.html
13. **new — Confluent Schema Registry, schema evolution and compatibility** (compatibility types, order of upgrading clients): https://docs.confluent.io/platform/current/schema-registry/fundamentals/schema-evolution.html

Optional extras: [A Tour of Go](https://go.dev/tour/) · [Quarkus Kafka guide](https://quarkus.io/guides/kafka) · [System Design Primer](https://github.com/donnemartin/system-design-primer)

*(Link check, 24 Nov 2026: Skillenai Backend / Spring Boot / Kafka / RabbitMQ / Go / EDA / microservices / Quarkus, freehire junior/middle/backend, ITviec java / backend-developer / spring-boot / golang / microservices / kafka returned HTTP 200 or loaded in a normal fetch. ITviec quarkus and rabbitmq tag pages returned 404. Of the 11 linked posting URLs, 7 returned 200 to a scripted check; the First Monday (#4) and Himalayas (#6) pages returned 403 and the two taskenzo pages (#1, #10) timed out to the script, but all four loaded in a normal fetch or search the same day. Company sources: the Axon careers page and FlintN site returned 403 to the script; the Axon Active, UNIT and Integral Solutions sites timed out to the script but were read through search the same day.)*

---

## Caveats

- **Fourth weekly report in the backend-engineer series.** "What changed" compares against the 13 Nov report (11 days, because this report moved from Friday to Tuesday). Skillenai skill pages refresh on different days inside the window, and comparison windows still overlap by ~62 days, so share changes are posting-mix signals, not a clean week of new hiring.
- **Skillenai** measures posting mix, not hiring volume. Its Backend Engineer demand-share change is unpublished again. "Go" may be inflated by the ambiguous word, which matters now that Go and Java differ by 0.5 points. The new Quarkus page has no earlier value to compare with.
- **freehire** counts a skill anywhere in a posting (including nice-to-have), so its figures are a ceiling. **Its census grew about 50% in 11 days** (27,264 → 41,044) and every level flipped from negative to positive 30-day growth, which points to a coverage change. Week-on-week freehire share changes in this report are not comparable; use them as a new baseline.
- **Fresh-postings sample (n=11) is small and search-biased.** Remote share is 100% by design. Weighted to Europe and Go this week; RabbitMQ (1 → 3) and stated pay (6 → 2) swings reflect what the searches surfaced. Several postings were read through aggregators (taskenzo, Findyet, remoteitjobs, First Monday, Pracovite, Himalayas, PickedJobs, WFH Beacon), and "posted" dates come from those pages. #11's date is the employer board's publish date, which may be a re-post. Two postings do not name their employer.
- **Hiring-company classification** uses the company's own site or LinkedIn company page; five of 23 employers are marked unclear rather than guessed. Size and HQ are shown only where a source states them. The job-alert and fresh samples have very different employer mixes (local alert digests vs remote web search), so the combined split is descriptive, not a market share.
- **ITviec counts** are a one-day snapshot (24 Nov 2026) from tag-page meta text. Work-model and seniority reads cover first-page job cards only.
- **Salaries:** ITviec figures are self-reported 2025 survey medians; Second Talent is a vendor rate card; Paymetric Labs does not publish its method. Only 2 of 11 sampled postings stated pay, none explicitly open to Vietnam. VND→USD at ≈26,000 is approximate.
- **Interview topic lists** come from prep sites and a vendor survey (secondary), carried over from the baseline.
- **Job-alert data** is alert titles only, from a sample of 28 alerts (7 backend-relevant). No personal data, recruiter names or contacts are included.
