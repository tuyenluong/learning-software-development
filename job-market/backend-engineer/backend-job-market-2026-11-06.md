# Backend Engineer Job Market 2026-11-06: Go · Spring Boot · Quarkus · Kafka · RabbitMQ

**Date:** 6 Nov 2026
**Purpose:** Backend-only market facts for Go, Spring Boot, Quarkus, Kafka and RabbitMQ roles, with extra attention to transaction and messaging skills.
**Coverage:** weekly **Backend Engineer** report. Job-alert window **30 Oct – 6 Nov 2026** (30 Oct overlaps the previous report; **31 Oct – 6 Nov** is new); fresh postings sampled from **~20 Oct – 6 Nov 2026**; index data as of **1–6 Nov 2026**.
**Builds on:** [backend-job-market-2026-10-30.md](backend-job-market-2026-10-30.md) (series baseline). Backend figures from the older combined reports remain in that file's [Earlier data](backend-job-market-2026-10-30.md#earlier-data-21-oct-and-28-oct).

> **How to read the numbers**
> - **Skillenai** = a job-posting index (90-day rolling windows; Backend Engineer page says "as of 5 Nov 2026"). It shows how often a skill shows up in postings, not total hiring. Skill pages refresh on different days (Kafka was last updated 1 Nov; Spring Boot / event-driven architecture 4 Nov; Go / RabbitMQ 5 Nov; microservices 6 Nov). This week's Backend Engineer page does **not** publish an adjusted demand-share change ("comparable posting coverage is insufficient"), so the −9.0% figure from 30 Oct is not updated here.
> - **freehire** = a posting aggregator that splits Backend by seniority (updated 6 Nov 2026). It counts a skill if it appears *anywhere* in a posting, including as a nice-to-have, so its percentages are a ceiling. When the number of postings that list skills changes, every percentage moves a little with it.
> - **ITviec counts** = live listing counts from itviec.com tag-page meta ("N Hot … jobs") on **6 Nov 2026**. Snapshot only. Work-model and seniority reads cover the first page of job cards on each tag, not the full tag.
> - **Fresh-postings sample** = 12 public junior-to-senior backend postings dated roughly 20 Oct – 6 Nov 2026, found by web search for remote Go / Spring Boot / Quarkus / Kafka / RabbitMQ roles. **This is a small, search-biased sample (n=12), not a census.** Every one is remote (or remote-first) because the searches asked for remote, so it says nothing about the remote share of the market. One link that appeared in search was already closed when re-checked (HTTP 404) and is excluded from counts; closed postings that were still readable in an archive are marked.
> - Anything marked **(est.)** is an estimate or conversion made for this report. VND→USD uses about **26,000 VND/USD**, which is approximate.
> - **Job-alert sample** = aggregate counts from a sample of LinkedIn/Glassdoor job-alert emails, mostly job titles. No personal data, recruiter names or contacts are included.

---

## Top skills at a glance (6 Nov 2026)

**Backend — learn these first**
1. **Java + Spring Boot** for Vietnam and fintech — Java **27.7%** of Backend Engineer postings, up from 27.3% ([Skillenai Backend](https://skillenai.com/data/role/backend-engineer)); Spring Boot **6,030** postings across all roles, demand share **+10.8%** ([Skillenai Spring Boot](https://skillenai.com/data/skill/spring-boot)); Java in **7 of 12** sampled fresh postings and Spring Boot in **6 of 12**.
2. **REST API design** — api **47%** of junior and **72%** of middle Backend postings, rest **32% / 45%** ([freehire junior](https://freehire.me/insights/roles/backend/junior), [freehire middle](https://freehire.me/insights/roles/backend/middle)); named in **9 of 12** sampled postings.
3. **PostgreSQL + SQL** — PostgreSQL **23.5%** of Backend Engineer postings; **6 of 12** sampled postings name PostgreSQL. Transactions remain the entry point to the messaging and consistency topics below.
4. **Kafka (with RabbitMQ as the second broker)** — Kafka **18.5%** of Backend Engineer postings and **24%** of middle postings; RabbitMQ **13%** of middle postings. In the fresh sample **9 of 12** name a message broker: Kafka 8, RabbitMQ 3 (counting nice-to-haves and "Kafka or RabbitMQ").
5. **Distributed systems / microservices + Kubernetes** — distributed systems **25.5%**, Kubernetes **30.8%**, microservices **17.1%** of Backend Engineer postings; microservices **35%** and Kubernetes **27%** of middle postings; microservices named in **8 of 12** sampled postings.

*Python (34.2%), AWS (33.2%) and Go (27.1%) remain higher in the global Backend Engineer list. They matter for the global remote market; the order above weights Vietnam and the Java/Spring stack.*

---

## What changed this week (30 Oct → 6 Nov 2026)

**Job-alert sample: 19 alerts.** A sample of 19 job-alert emails dated 30 Oct – 6 Nov was counted. **7 were backend-relevant** (LinkedIn digests from a remote Java backend search and "jobs you might like" digests with backend titles). The other 12 were QA/test, industrial automation / SCADA, or unrelated. One Glassdoor digest was QA-titled but carried a Java Developer card among mostly BA/QA titles and is counted with the non-backend majority. All were automated digests; none came from a named recruiter and none of the backend-relevant alerts stated a salary range.

**The five changes worth acting on**

| # | Change | 30 Oct | 6 Nov | Read |
|---|---|---|---|---|
| 1 | **Event-driven architecture accelerated again** | 2,902 postings, share **+23.9%** | **3,309**, share **+34.8%** | Fastest-rising backend signal for a fourth report running. Messaging and consistency stay the right core. |
| 2 | **Spring Boot, Go and microservices share all stepped up; Kafka held** | Spring Boot 5,634 (+9.5%), Go 15,020 (+5.4%), microservices 11,401 (+5.4%), Kafka 8,581 (+5.3%) | **Spring Boot 6,030 (+10.8%)**, **Go 15,899 (+7.0%)**, **microservices 12,172 (+8.7%)**, **Kafka 8,743 (+5.3%)** | Spring Boot remains the biggest stack share gain. Kafka's *share* change is flat week-on-week even as the raw count rose. |
| 3 | **Middle postings ask harder for Kafka, Spring and RabbitMQ** | middle: kafka 21%, spring 24%, rabbitmq 12%, microservices 32% | **kafka 24%, spring 27%, rabbitmq 13%, microservices 35%** | The junior→middle jump for messaging is sharper, not softer. Kafka is still **6%** of junior postings (now visible in the junior top 40). |
| 4 | **Vietnam backend listings stabilised; kafka tag rose** | java 95, backend 81, spring boot 41, golang 30, microservices 29, kafka 15 | **92, 83, 42, 31, 29, 18** | The end-of-October dip did not continue. Kafka-tagged listings are up 3. **Zero remote** on the first page of kafka, golang and spring-boot tags (same as 30 Oct). |
| 5 | **Junior and middle freehire pools both shrank; senior bled hardest** | Junior 981, Middle 1,200; Senior 13,980 (−665 / 30d) | **Junior 977 (−109 / 30d), Middle 1,154 (−147 / 30d)**; Senior **13,279 (−3,107 / 30d)** | Open junior/middle seats are slightly fewer. freehire's total Backend census jumped to **28,012** (was 20,804) — treat the per-level shares, not the absolute census, as the signal (likely a coverage/cleanup change). |

**Backend skill shares, 30 Oct → 6 Nov** (Skillenai, Backend Engineer; 2,685 → **2,801** postings; shares are of all postings in the window, so treat moves under 0.5 points as rounding):

| Skill | 30 Oct | 6 Nov | Skill | 30 Oct | 6 Nov |
|---|---|---|---|---|---|
| Python | 34.3% | 34.2% | TypeScript | 18.5% | 18.8% |
| AWS | 33.0% | **33.2%** | Kafka | 18.3% | **18.5%** |
| Kubernetes | 30.6% | **30.8%** | SQL | 17.1% | **17.5%** |
| Java | 27.3% | **27.7%** | Microservices | 16.4% | **17.1%** |
| Go | 26.1% | **27.1%** | Observability | 16.4% | 16.1% |
| Distributed systems | 25.4% | 25.5% | Redis | 15.5% | 15.2% |
| PostgreSQL | 23.4% | 23.5% | Docker | 22.6% | 22.7% |
| CI/CD | 20.7% | **21.5%** | | | |

Over the week the biggest moves are **Go +1.0 point, Microservices +0.7, CI/CD +0.8, Java +0.4**. Observability and Redis each slipped 0.3 points.

**Messaging and stacks, all roles (Skillenai 90-day totals).** Totals grow partly because the index grows, so read the *share change*, not the raw count:

| Signal | 30 Oct | 6 Nov | Share change (latest page) |
|---|---|---|---|
| Kafka postings | 8,581 | **8,743** | **+5.3%** (unchanged) |
| RabbitMQ postings | 1,735 | **1,879** | not published (still no share change on the page) |
| Event-driven architecture | 2,902 | **3,309** | **+34.8%** (was +23.9%) |
| Microservices | 11,401 | **12,172** | **+8.7%** (was +5.4%) |
| Go | 15,020 | **15,899** | **+7.0%** (was +5.4%) |
| Spring Boot | 5,634 | **6,030** | **+10.8%** (was +9.5%) |

**freehire Middle Backend, 30 Oct → 6 Nov** (1,130 → 1,086 postings listing skills): kafka 21% → **24%**, rabbitmq 12% → **13%**, event-driven 19% → 19%, microservices 32% → **35%**, spring 24% → **27%**, postgresql 28% → 28%, kubernetes 29% → **27%**, ci-cd 41% → 41%, observability 17% → **18%**, test-automation 15% → **14%**, redis 15% → 15%, distributed systems 15% → **16%**, api 68% → **72%**.

**ITviec Vietnam, 30 Oct → 6 Nov 2026** (live listing counts, same tag pages):

| Tag | 30 Oct | 6 Nov |
|---|---|---|
| java | 95 | **92** |
| backend developer | 81 | **83** |
| spring boot | 41 | **42** |
| golang | 30 | **31** |
| microservices | 29 | **29** |
| kafka | 15 | **18** |
| quarkus | 404 (≈0) | **404 (≈0)** |
| rabbitmq | 404 (no tag page) | **404 (no tag page)** |

([java](https://itviec.com/it-jobs/java), [backend developer](https://itviec.com/it-jobs/backend-developer), [spring-boot](https://itviec.com/it-jobs/spring-boot), [golang](https://itviec.com/it-jobs/golang), [microservices](https://itviec.com/it-jobs/microservices), [kafka](https://itviec.com/it-jobs/kafka))

**Job-alert sample (aggregate, 30 Oct – 6 Nov):**
- **7 of 19 alerts (37%) were backend-relevant**, the same share as the 30 Oct report. They carried about **20 backend or backend-adjacent titles** (several digests listed multiple cards).
- Titles (aggregate): Senior Java Engineer (AI-Driven Development), Senior Full-Stack Developer (Backend-focused), Junior Java Developer (Mandarin), Senior Java Engineer, Senior Backend Software Engineer II, Intermediate Backend Engineer (Remote, Vietnam), Senior Backend Engineer (Remote, Vietnam), Software Engineer (Java), Staff Backend Engineer, Senior/Lead Backend Engineer, Full Stack Engineer (APAC), Java Engineer, Java Developer, Java Software Engineer, Java Backend Developer (finance), Java Developer (JavaEE, Spring Boot), Full-Stack Java Developer, Backend Java Developer, Technical Architect (Kotlin, Java, Spring Boot, AI).
- **Remote:** 2 titles explicitly remote-Vietnam, both from one employer (Intermediate and Senior Backend Engineer) — the same pattern the 28 Oct and 30 Oct reports flagged. Staff Backend and Senior/Lead Backend titles appeared for HCMC without an explicit remote flag in the digest.
- **Payments / finance / banking:** several Java backend titles at finance and surety employers in the Capgemini-similar digest; banking and fintech remain the biggest local cluster.
- **Kafka, RabbitMQ, Quarkus and Go: zero hits in alert titles**, as in every earlier report. Spring Boot appeared in title text twice. Alerts are title digests; stack detail lives in the body.
- **No salary ranges were stated in any backend-relevant alert.**

---

## 0. Bottom line

1. **Event-driven architecture is still the fastest-rising backend skill.** Share change **+34.8%** (3,309 postings), up from +23.9% a week earlier. Kafka's share change held at **+5.3%** while Spring Boot (**+10.8%**), Go (**+7.0%**) and microservices (**+8.7%**) all accelerated.
2. **Spring Boot remains the stack to lead with.** Java **27.7%** of Backend Engineer postings, Spring Boot share **+10.8%**, Java in **7 of 12** fresh postings, and **92 Java / 42 Spring Boot** listings in Vietnam against **31 Go** and **≈0 Quarkus**.
3. **Messaging is more clearly a middle-level bar this week.** Kafka **6%** of junior → **24%** of middle; RabbitMQ **13%** of middle. In the fresh sample, **9 of 12** name a broker, and "Kafka or RabbitMQ" remains common on Java roles.
4. **Vietnam is still office-first.** First-page job cards on kafka, golang and spring-boot show **0 remote** (kafka 14 office / 4 hybrid; golang 16 / 4; spring boot 15 / 5). Remote work for Vietnam-based engineers still comes from foreign employers — the job-alert sample's two remote-Vietnam backend titles came from one foreign employer again.
5. **Pay: no new local survey.** No backend alert stated a salary. Fresh sample pay bands (where stated) sit in the same remote/international range as last week. ITviec and Second Talent figures are unchanged from the baseline.

---

## 1. Most-demanded skills, with frequency signals

### A. Global: Skillenai, "Backend Engineer" title, 2,801 postings, 90 days to 5 Nov 2026
([source](https://skillenai.com/data/role/backend-engineer))

| Skill | Postings | Share | Skill | Postings | Share |
|---|---|---|---|---|---|
| Python | 958 | 34.2% | TypeScript | 526 | 18.8% |
| AWS | 931 | 33.2% | **Kafka** | **518** | **18.5%** |
| Kubernetes | 864 | 30.8% | SQL | 491 | 17.5% |
| **Java** | **775** | **27.7%** | Microservices | 480 | 17.1% |
| **Go** | **759** | **27.1%** | Observability | 452 | 16.1% |
| **Distributed systems** | **715** | **25.5%** | Redis | 427 | 15.2% |
| PostgreSQL | 659 | 23.5% | | | |
| Docker | 637 | 22.7% | | | |
| CI/CD | 602 | 21.5% | | | |

- **Demand share change:** not published on the 5 Nov page (insufficient comparable coverage). The −9.0% figure from 30 Oct is therefore **not updated** this week.
- **Top posters:** GitLab 141, Grafana Labs 108, Wise 64, Stripe 61, CLERA 56, Vinted 50, ABOUT YOU 42. Remote-friendly product companies; CLERA dropped out of the top three.
- **Top metros:** Berlin 4.1%, New York City 2.9%, San Francisco 2.9%, London 2.8%, Tel Aviv 2.2%, Bengaluru 1.8%.
- **Career flows:** Backend Engineer hires come mainly from Software Engineer (104 moves in, 57 out). Unchanged.

### B. By seniority: freehire, open Backend postings, updated 6 Nov 2026

| Level | Open postings | Skill leaders |
|---|---|---|
| **Junior** | **977** (822 list skills) | api 47%, python 42%, **java 41%**, rest 32%, sql 31%, git 30%, ai 24%, docker 20%, ci-cd 20%, cloud 18%, postgresql 18%, aws 17%, **spring 17%**, nodejs 16%, mysql 15%, microservices 12%, redis 12%, kubernetes 10%, **kafka 6%** |
| **Middle** | **1,154** (1,086 list skills) | api 72%, rest 45%, java 44%, aws 42%, ci-cd 41%, cloud 38%, **microservices 35%**, docker 34%, sql 33%, git 33%, ai 31%, python 30%, postgresql 28%, **kubernetes 27%**, **spring 27%**, **kafka 24%**, azure 20%, mysql 20%, **event-driven 19%**, **observability 18%**, redis 15%, **test-automation 14%**, distributed systems 16%, **rabbitmq 13%**, llm 11% |

([freehire junior](https://freehire.me/insights/roles/backend/junior), [freehire middle](https://freehire.me/insights/roles/backend/middle), [freehire seniority split](https://freehire.me/insights/roles/backend))

- **The junior-to-middle jump** (most useful for planning study): Kubernetes **10% → 27%**, microservices **12% → 35%**, CI/CD **20% → 41%**, AWS **17% → 42%**, Kafka **6% → 24%**, observability **not in junior top 40 → 18%**, RabbitMQ **not in junior top 40 → 13%**, Spring **17% → 27%**.
- **Seniority census, 6 Nov:** 28,012 open Backend roles — Senior 13,279, Lead 1,961, **Middle 1,154**, Staff 1,056, Intern 1,049, **Junior 977**, Principal 312, C-level 103. 30-day growth: Senior **−3,107**, Lead −344, Middle **−147**, Junior **−109**. Junior + Middle together are about **7.6%** of open roles (est.). The absolute census rose sharply vs 30 Oct's 20,804; prefer the per-level skill shares over the census total.

### C. Fresh postings sample: 12 remote backend postings, ~20 Oct – 6 Nov 2026

*Small, search-biased sample (n=12). Use it for what employers write in junior/mid postings right now, not for market shares.*

| # | Role (employer) | Posted | Level | Where | Stack named | Pay stated |
|---|---|---|---|---|---|---|
| 1 | [Software Engineer, Golang Junior/Junior+ (Plata / DataStream via WFH Beacon)](https://wfhbeacon.up.railway.app/job/software-engineer-golang-junior-junior) | 4 Nov | Junior (1+ yr) | Remote, GMT-0 to GMT+5 | Go, Kafka, PostgreSQL, MongoDB, Redis, AWS, EKS | **$75–100K/yr** |
| 2 | [Java Backend Developer, Spring Boot / Kafka (knowmad mood)](https://knowmadmood.teamtailor.com/jobs/8643686-java-backend-developer-spring-boot-kafka-microservicios-remoto) | live (re-checked 6 Nov) | Mid | Remote, Spain | Java 17+, Spring Boot / Cloud / Security, Kafka, microservices, REST, JUnit 5, Mockito, SonarQube | No |
| 3 | [Mid Backend, Java / Kafka / Spring Boot / AWS (Métrica)](https://www.spainjobs.io/companies/metrica/desarrolladora-backend-mid-java-kafka-spring-boot-aws--22fcd61272) | ≤late Oct (still open 6 Nov) | Mid | Remote, Spain | Java 17+, Spring Boot 3, **Kafka (RabbitMQ/SQS-SNS accepted)**, PostgreSQL/Oracle, hexagonal architecture, JUnit + Mockito, GitHub Actions, OpenAPI | No |
| 4 | [Backend Developer, Jakarta EE / Quarkus (m2TALENTS)](https://www.glassever.com/jobs/backend-developer-jakarta-ee-quarkus-m2talents-job-2) | 20 Oct | Mid (3+ yr) | Remote, Germany (German C1) | Java, Jakarta EE, **Quarkus**; nice: REST, microservices, CI/CD | No (benefits only) |
| 5 | [Senior Java Backend Developer (Tieto Tech Consulting)](https://jobcore.r5b.is-great.net/remote-jobs/senior-java-backend-developer-tieto-tech-consulting-mfd) | 28 Oct | Senior (5+ yr) | Remote, Europe/EMEA | Java 21, **Quarkus** (Spring Boot accepted), REST, PostgreSQL, Oracle, Kubernetes, Jenkins, JUnit, SonarQube | No |
| 6 | [Remote Quarkus Backend Engineer (Dacomat)](https://lavori.co.it/backend-engineer_genova-c287754/2026-11-dacomat-srl_i4273109090) | 2 Nov | Mid (4+ yr) | Remote, Italy (occasional Milan) | Java, Maven, **Quarkus**, microservices, REST/OpenAPI, gRPC / Protobuf; corporate banking | **€50–90K/yr** |
| 7 | [Remote Backend Engineer, Java / Quarkus (Xelerate)](https://emprego24.pt/backend-engineer_porto-c402623/2026-11-xelerate_i4278958764) | 5 Nov | Mid | Remote, Portugal | Java, **Quarkus**, microservices, Azure, Docker, CI/CD, tests | **€60–90K/yr** |
| 8 | [Senior/Mid Data Platform Developer (Ideamotive / MindPal)](https://mindpal.co/jobs/106744) | ~3 Nov | Mid/Senior (~3 yr Kafka) | Remote, Poland (1×/mo Wrocław) | Kafka Connect / Streams / kSQL, Spring Boot, **Quarkus**, GraalVM, MongoDB, GraphQL, observability | **145–160 PLN/hr** B2B |
| 9 | [Junior Backend Developer (SolDevelo)](https://www.soldevelo.com/careers/junior-backend-developer/) | live (re-checked 6 Nov) | Junior | Remote | Java, Spring Boot, REST, relational DB / PostgreSQL, Docker; AI tooling expected | **PLN 6,000–8,900** gross · B2B **48–70 PLN/hr** |
| 10 | [Backend Developer, GraphQL / Kafka (Bitovi via Kickstart Remote)](https://kickstartremote.com/remote-jobs/backend-developer-graphql-kafka-united-states-remote-4726) | ~late Oct | Mid/Senior | Remote, US only | Go, GraphQL, Kafka (topics, consumer groups, lag, schema), AWS, Kubernetes; nice: SQS/SNS or RabbitMQ, Temporal | **$120–190K/yr** |
| 11 | AI Engineer Junior Backend Java (CI&T) — *closed when re-checked; archive readable* | 13 Oct (closed ~15 Oct) | Junior | Remote, Brazil | Java, Spring Boot, **Kafka or RabbitMQ**, microservices, JUnit/Mockito, Docker/K8s | No |
| 12 | Java Developer Fintech (via RocketHunt) — *page marks listing closed* | undated (archive) | Mid (2+ yr) | Remote, worldwide | Java 17+, Spring Boot, PostgreSQL, **Kafka / RabbitMQ**, microservices | No (estimator only) |

**Counts across the 12 (mentioned anywhere, including nice-to-have; closed #11–#12 still counted from readable text):**

| Skill | Count | Skill | Count |
|---|---|---|---|
| REST / API | 9 | Java | 7 |
| **Any message broker** | **9** | Microservices | 8 |
| **Kafka** | **8** | Spring Boot | 6 |
| PostgreSQL | 6 | Tests named (unit/integration/JUnit/Mockito) | 6 |
| CI/CD | 6 | **Quarkus** | **5** |
| Docker | 5 | Kubernetes | 4 |
| Go | 2 | **RabbitMQ** | **3** |
| Redis | 2 | AWS | 4 |
| Observability tools | 3 | AI mentioned | 3 |

- **Seniority:** Junior 3, Mid 5, Mid/Senior 2, Senior 1, closed-archive mid 1.
- **Remote:** 12 of 12 by search design. Only a minority were open worldwide or without a country restriction; most were tied to one country or region (Spain, Germany, Italy, Portugal, Poland, US, Brazil, GMT band). **0 of 12** were explicitly open to Vietnam-based engineers in the posting text (contrast the job-alert sample's Employment Hero remote-Vietnam titles).
- **Salary stated: 5 of 12** — $75–100K/yr (Go junior), €50–90K, €60–90K, 145–160 PLN/hr, PLN 6–8.9k / B2B 48–70. Too few and too region-specific to summarise into one band.
- **Brokers are still "either/or" on many Java roles.** Of the 9 postings naming a broker, several accept Kafka *or* RabbitMQ (or SQS). The Go roles (#1, #10) named Kafka specifically.

### D. Vietnam: ITviec live counts and first-page read, 6 Nov 2026

- Counts: "java" **92**, "backend developer" **83**, "spring boot" **42**, "golang" **31**, "microservices" **29**, "kafka" **18**, "quarkus" and "rabbitmq" no tag page (404, ≈0).
- **Work model on the first page of job cards:** kafka 18 → **14 at office, 4 hybrid, 0 remote**; golang first 20 → **16 office, 4 hybrid, 0 remote**; spring boot first 20 → **15 office, 5 hybrid, 0 remote**.
- **Seniority in slugs/titles, first page:** golang 20 → **13 senior or above**, 0 junior, 7 unstated. Spring boot 20 → **8 senior or above**, 3 mid/mid-sen, 1 all-level, 8 unstated, **0 junior**. Kafka 18 → **10 senior or above**, 1 mid, 1 all-level, 6 unstated.
- **Kafka-tagged titles remain Java-heavy** (Spring Boot / Java backend roles dominate the first page; several also name Go).
- No new posted USD band was extracted from first-page titles this snapshot (the "up to $3,200" Mid/Sr Java listing from 28–30 Oct was not re-confirmed on the first page).

---

## 2. Must-have vs nice-to-have vs differentiator (junior → mid → senior)

*Synthesis from the frequencies above, the 12 fresh postings and the interview sources in §6.*

| Level | Must-have | Nice-to-have | Differentiator |
|---|---|---|---|
| **Junior** | Java + Spring Boot (or Go); REST; SQL + PostgreSQL; Git; unit tests (JUnit/Mockito); Docker basics | A message queue "even from study"; Redis; one cloud; AI coding tools as a stated habit (named in junior postings this week) | A small service that **dedupes events and retries with backoff**, tested |
| **Mid** | Java 17/21 + Spring Boot 3 **or** Go; REST (OpenAPI); PostgreSQL (indexes, transactions); Docker; unit + integration tests; CI/CD; **Kafka or RabbitMQ producer/consumer in production**; microservices | Kubernetes; Redis; observability (Grafana/Prometheus/ELK); hexagonal architecture; gRPC; Oracle (banks); Quarkus as an accepted alternative to Spring | Testing services under failure; fintech domain basics |
| **Senior** | Distributed systems: messaging, retries, timeouts, idempotency, outbox/saga, consistency trade-offs; observability; performance and concurrency; system design; on-call thinking | Event sourcing/CQRS; Kafka Streams/Connect/Debezium; K8s operations; OAuth2/OIDC | Proving correctness under failure; payments depth; ADRs and design docs |

*Change from 30 Oct: junior row now notes AI tooling as a recurring nice-to-have in junior postings; Quarkus appears in 5 of 12 fresh postings this week (mostly Europe), so the mid nice-to-have row calls it out explicitly. The mid must-have "Kafka or RabbitMQ in production" is unchanged and better supported (9 of 12 name a broker; middle Kafka 24%).*

---

## 3. Messaging, transactions and distributed systems: how often, and how tested

### Frequency signals

| Signal | Number | Source |
|---|---|---|
| Kafka postings (all roles, 90d) | **8,743** (share **+5.3%** vs prior 4 weeks) | [Skillenai Kafka](https://skillenai.com/data/skill/kafka) |
| RabbitMQ postings (90d) | **1,879** → Kafka is about **4.7×** RabbitMQ (est.; was 4.9× on 30 Oct) | [Skillenai RabbitMQ](https://skillenai.com/data/skill/rabbitmq) |
| Event-driven architecture postings (90d) | **3,309** (share **+34.8%**) | [Skillenai EDA](https://skillenai.com/data/skill/event-driven-architecture) |
| Microservices postings (90d) | **12,172** (share +8.7%) | [Skillenai microservices](https://skillenai.com/data/skill/microservices) |
| Share of Backend Engineer postings | Distributed systems 25.5%, Kafka 18.5%, microservices 17.1%, observability 16.1%, Redis 15.2% | [Skillenai Backend](https://skillenai.com/data/role/backend-engineer) |
| Share of **Middle** Backend postings | **Kafka 24%**, event-driven 19%, observability 18%, distributed systems 16%, **RabbitMQ 13%** | [freehire middle](https://freehire.me/insights/roles/backend/middle) |
| Share of **Junior** Backend postings | **Kafka 6%**; RabbitMQ not in top 40; microservices 12%, redis 12% | [freehire junior](https://freehire.me/insights/roles/backend/junior) |
| Top role for each broker | Software Engineer: 40.2% of Kafka postings, 44.2% of RabbitMQ postings | Skillenai Kafka / RabbitMQ |
| Top Kafka employers | Wise 186, Cisco 163, **Mastercard 115**, CrowdStrike 114, **Barclays 91**, Capital One 78, Databricks 66, **JPMorgan 61** | [Skillenai Kafka](https://skillenai.com/data/skill/kafka) |
| Top EDA employers | **Mastercard 70, Wise 63, Barclays 37**, Bright Vision 29, EPAM 24 | [Skillenai EDA](https://skillenai.com/data/skill/event-driven-architecture) |
| Top RabbitMQ employers | CLERA 26, Wrike 23, Bright Vision 18, Klaviyo 18, Wise 18, Cisco 18 | [Skillenai RabbitMQ](https://skillenai.com/data/skill/rabbitmq) |
| Fresh sample (n=12) | Broker named in **9**: Kafka 8, RabbitMQ 3 | §1C |
| Vietnam | ITviec "kafka" **18**, "microservices" **29** (vs "java" 92); no RabbitMQ tag | ITviec, 6 Nov 2026 |

**Read (interpretation):**
- **Kafka is still the broker to lead with**; banks and payments companies still dominate its top employers, which matches Vietnam's fintech-heavy backend titles.
- **Event-driven architecture accelerated again while Backend Engineer demand-share is unpublished.** The gap still favours engineers who know how event flows fail.
- **RabbitMQ still deserves a full lesson.** All-roles Kafka ≈ **4.7×** RabbitMQ, but middle postings put RabbitMQ at **13%** and Java roles keep writing "Kafka or RabbitMQ".
- **Junior postings rarely require messaging; middle postings usually expect it.** Kafka's junior share is now measurable at 6%, but the middle share is 24%. Teach messaging as the Stage 2 → Stage 3 bridge, with idempotency early.

### How it's tested in interviews
*Unchanged from the baseline; no new interview-format survey this window. Sources are prep sites and vendor surveys (secondary).*

1. **System design round** (38% of technical tests per [CoderPad 2026](https://coderpad.io/survey-reports/coderpad-state-of-tech-hiring-2026/)): checkout, payment, wallet transfer, notifications. Expected: local transactions, **no 2PC**, **transactional outbox**, **saga** with compensations, **retries with backoff and timeouts**, **idempotent consumers**, **DLQ**.
2. **Kafka deep-dive:** partitions and ordering; consumer groups and rebalancing; offset commits; idempotent producer and transactions; why exactly-once covers Kafka-to-Kafka only; consumer lag.
3. **Database and concurrency:** isolation levels and anomalies; optimistic vs pessimistic locking; "two requests withdraw from the same account"; idempotency keys on POST.
4. **Debugging scenarios:** "users get charged twice", "consumer lag grows after a deploy", "messages land in the DLQ after a schema change".

---

## 4. Go vs Spring Boot vs Quarkus

| Signal | Go | Spring Boot | Quarkus |
|---|---|---|---|
| Global postings, 90d (Skillenai, latest) | **15,899** (share +7.0%) ¹ | **6,030** (share **+10.8%**) | no Skillenai page |
| Share of Backend Engineer postings | **27.1%** | (Java 27.7%) | n/a |
| Top employers | Capital One 771, Cisco 529, **Stripe 215**, Anduril 188, CrowdStrike 171, SpaceX 164, **Grab 162** | **Mastercard 330**, Wise 142, **Barclays 119**, Capco 64, JPMorgan 62, Cisco 60 | (sample: telecom, automotive/health-tech, corporate banking, B2B marketplace) |
| Fresh sample (n=12) | **2** (both name Kafka) | **6** | **5** — all remote Europe, mid to senior |
| freehire junior / middle | go not in junior top 40 this week; not in middle top 40 | spring 17% junior / 27% middle | not in either top 40 |
| Vietnam ITviec (6 Nov) | **31** (was 30) | **42** (Java 92) | **≈0** (404) |
| Vietnam first-page seniority | 13 of 20 senior+, 0 junior | 8 of 20 senior+, 0 junior | n/a |

¹ "Go" is an ambiguous word; treat Skillenai's count as an upper bound.

Sources: [Skillenai Go](https://skillenai.com/data/skill/go), [Skillenai Spring Boot](https://skillenai.com/data/skill/spring-boot), [ITviec golang](https://itviec.com/it-jobs/golang), [ITviec spring-boot](https://itviec.com/it-jobs/spring-boot). SO 2026 and Java-org survey figures remain in the baseline [Earlier data](backend-job-market-2026-10-30.md#earlier-data-21-oct-and-28-oct) and were not re-pulled.

**Verdict (unchanged direction, with a stronger Quarkus note in the remote-Europe sample):**
- **Spring Boot is the primary stack.** Biggest share gain again, leads in Vietnam and in banks/fintech, and Java/Spring titles dominated the backend-relevant alerts.
- **Go is the second language for remote and global product companies.** Vietnam Go listings ticked up one (30 → 31) and remain senior-heavy, so Go is still a remote-market play, not a local junior entry. One fresh junior Go/Kafka posting this week ($75–100K, GMT band) shows the remote junior door can open.
- **Quarkus: concepts only, plus one honest note.** Still ≈0 in Vietnam, but **5 of 12** remote European postings named it (often "Quarkus or Spring Boot / Jakarta EE"). One or two comparison lessons remain enough; most Spring knowledge carries over.

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
- **Paymetric Labs** lists a Vietnam back-end (Java/Go/Node.js) median of **₫41.6M/month**, range ₫37.8–42.6M, +6.5% year on year ([source](https://www.paymetriclabs.com/vn/salaries/back-end-developer-java-go-node-js)). Method and sample size not stated; treat as a cross-check only.

### Remote / international (Vietnam-based engineer, USD / month)

| Source | Back-end | Notes |
|---|---|---|
| [Second Talent APAC benchmark, Oct 2026](https://www.secondtalent.com/apac-salary-benchmark/) (vendor, carried over) | **Southeast Asia back-end family:** junior **$2,500** ($1,800–3,300), mid **$3,300** ($2,500–4,300), senior **$4,500** ($4,300–5,600), lead $5,400. **Vietnam back-end senior median: $4,600** | Remote contractor rates |
| [Second Talent, Vietnam rates 2026](https://www.secondtalent.com/resources/true-cost-outsource-software-development-vietnam/) (vendor) | Mid **$3,400–4,900** · Senior **$4,900–7,000** · Lead/Architect $7,000–9,800 | Unchanged; Go/.NET seniors +10–20% |
| Fresh sample (n=5 with pay) | Go junior **$75–100K/yr**; Europe Quarkus **€50–90K** and **€60–90K**; Poland mid Kafka **145–160 PLN/hr**; Poland junior Spring **PLN 6–8.9k** gross / B2B 48–70 | Single postings; regional |
| Global reference ([SO 2026 comp](https://survey.stackoverflow.co/2026/work/data/compensation)) | Back-end median **$85,296/yr**; architect **$102,355/yr** | Mostly US/EU respondents; baseline figure |

**Read (est.):** a mid-level remote backend engineer in Vietnam still lands around **$2,500–4,300/mo** on contractor rates, and a senior around **$4,300–5,600/mo**. Both are roughly **2–3×** the local ITviec medians for 3–8 years. English is still the gate.

---

## 6. Typical interview formats and common topics

*Unchanged from the baseline; not re-surveyed this window.*

- **Market-wide (CoderPad 2026, ~650 respondents):** algorithmic 43%, real-world scenarios 38%, system design 38%, pair programming 30%, code review 21%, debugging 19%. 46% of companies allow AI in interviews in some form; the skill signals are catching AI mistakes (66%) and explaining trade-offs (56%).
- **Backend loop (mid/senior):** recruiter → coding (DSA or a practical service task) → **system design** (seniors often get 2 rounds) → **deep-dive** (Spring internals or Go concurrency, DB and transactions, Kafka) → behavioural.
  - **Spring:** DI and bean lifecycle; `@Transactional` propagation and pitfalls; **JPA N+1**; connection pools; virtual threads.
  - **Go:** goroutines, channels, `context` cancellation, races (`-race`), worker pools.
  - **Messaging:** see §3.
- **Signals in this week's postings:** mid Spring postings still name hexagonal architecture and OpenAPI; Quarkus roles in Europe often require a local language (German C1) or a country presence; one junior Go posting sets English at **B1+** and expects AI tooling as a habit.
- **Vietnam specifics (est.):** outsourcing firms run a shorter loop (tech interview, English check). Foreign in-house and remote employers add system design.

---

## 7. Trends

**Event-driven architecture is the fastest-rising backend skill**
- Share change **+34.8%** (3,309 postings), up from +23.9% a week earlier. Banks and payments firms still lead (Mastercard, Wise, Barclays).
- **Implication:** a messaging-focused skill set is aligned with where demand is moving.

**Backend open roles: senior pool is bleeding; junior/middle are slightly down**
- freehire Senior **−3,107** over 30 days; Junior −109, Middle −147. Skillenai's Backend Engineer demand-share change is unpublished this week, so the −9.0% story from 30 Oct is paused, not reversed.
- **Implication:** proof (a deployed service, tests, one broker) still matters more than a keyword list.

**Spring Boot is gaining fastest of the three stacks**
- Spring Boot share **+10.8%** vs Go +7.0%; Quarkus remains ≈0 in Vietnam but is visible in remote-Europe samples.

**AI in backend postings is broad but shallow**
- freehire "ai": **24%** junior, **31%** middle; "llm" 11% of middle. Fresh sample **3 of 12** mention AI tooling or AI-driven development. Broad keyword, treat as directional.

**Vietnam stays office-first and senior-heavy**
- 0 remote and 0 junior titles on the first pages of the golang and spring-boot tags (§1D). Kafka-tagged listings rose 15 → 18 without adding remote seats. Remote options still come from foreign employers.

---

## 8. Recommended skill priority list (junior → mid backend)

*Time estimates assume about 6–8 hrs/week of study and are estimates. Order follows the baseline backend phases; changes from this week's data are marked **new**.*

### Stage 1: Junior foundations (months 0–6)
1. **Java 21 + Spring Boot 3:** REST with OpenAPI, validation, error handling, JPA/Hibernate (including **N+1**). *(Java 41% of junior postings; Spring Boot in 6 of 12 fresh postings.)*
2. **SQL + PostgreSQL transactions:** joins, indexes, isolation levels, lost update. *(PostgreSQL 23.5% of Backend Engineer postings; 6 of 12 fresh postings.)*
3. **Testing:** JUnit 5 + Mockito, then Testcontainers integration tests. *(Tests named in 6 of 12; test-automation 14% of middle postings.)*
4. **Git, Maven, Docker, a CI pipeline (GitHub Actions).** *(CI/CD 20% junior → 41% middle.)*

### Stage 2: Strong junior (months 6–12)
5. **Idempotent consumer + retries with backoff, on RabbitMQ first.** Build a notifications consumer that dedupes by event id, retries with growing backoff, and records history in PostgreSQL. *(Still the clearest junior→middle bridge; RabbitMQ 13% of middle postings.)*
6. **Payments on the orders API with idempotency keys**, plus a first AWS deploy. *(AWS 17% junior → 42% middle.)*
7. **Auth (JWT/OAuth2 basics).**
8. **new — Treat AI coding tools as a habit, not a lesson.** Junior postings this week name them as expected workflow; keep reviews and tests honest.

### Stage 3: Mid-level (months 12–24)
9. **Kafka with Spring for Apache Kafka:** keys and partitions, consumer groups, offset commits, retries/DLT, consumer lag. *(Kafka 24% of middle postings; 8 of 12 fresh postings.)*
10. **Reliability patterns:** transactional outbox, saga with compensations, timeouts and circuit breakers.
11. **Kubernetes basics + observability** (structured logs, Prometheus/Grafana, OTel traces across async hops). *(Kubernetes 10% → 27%, observability → 18% from junior to middle.)*
12. **Redis caching.** *(Redis 15.2% of Backend Engineer postings.)*
13. **Hexagonal architecture** as the structure for the payments/orders service. *(Still named in mid Spring postings.)*

### Later: Go and architect track
14. **Go** as the second language, porting one service with a Kafka consumer. *(Remote-market play; one junior Go/Kafka remote posting this week.)*
15. **Quarkus**, 1–2 comparison lessons (more relevant if targeting remote Europe). **System design** practice (payments, wallet, notifications), ADRs.

---

## 9. Backend path vs the market

*Checked against this week's 12 fresh postings and freehire junior/middle data. The full 28 Oct gap analysis remains in the baseline [Earlier data](backend-job-market-2026-10-30.md#28-oct-gap-analysis-backend-path-vs-the-market); this section only records what this week's data adds or confirms.*

| Path element | This week's evidence | Verdict |
|---|---|---|
| Spring Boot CRUD + PostgreSQL + tests (Stage 1) | Spring Boot 6/12, PostgreSQL 6/12, tests 6/12; SolDevelo junior asks for Java + REST + SQL | **Covered, keep** |
| API idempotency and retries (Stage 2) | Still the differentiator mid postings imply via Kafka/RabbitMQ production use | **Covered; keep messaging version in Stage 2** |
| Messaging basics (Stage 3) | Brokers in 9/12; Kafka 6% junior → 24% middle; RabbitMQ 13% middle | **Covered; teach RabbitMQ first, then Kafka** |
| Observability (Stage 3) | 3/12 name observability tools; 18% of middle postings | **Covered, keep** |
| Kubernetes | 4/12; 10% junior → 27% middle | **Gap from 28 Oct still stands: move basics to end of Stage 2** |
| Quarkus awareness | 5/12 remote-Europe postings | **Small addition: keep as 1–2 comparison lessons, not a primary stack** |
| Outbox / saga | Named in **0** of 12 postings as a required keyword | **Interview depth, not a CV keyword** (unchanged) |

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

Optional extras: [A Tour of Go](https://go.dev/tour/) · [Quarkus Kafka guide](https://quarkus.io/guides/kafka) · [System Design Primer](https://github.com/donnemartin/system-design-primer)

*(Link check, 6 Nov 2026: Skillenai Backend / Spring Boot / Kafka / RabbitMQ / Go / EDA / microservices, freehire junior/middle/backend, ITviec java / backend-developer / spring-boot / golang / microservices / kafka, and Second Talent pages returned HTTP 200. ITviec quarkus and rabbitmq tag pages returned 404. Of the sampled posting URLs, 10 returned 200; the BuiltIn Go listing used during search returned 404 and was excluded; CI&T and RocketHunt archive pages returned 200 but mark the roles closed.)*

---

## Caveats

- **Second weekly report in the backend-engineer series.** "What changed" compares against the 30 Oct baseline (a full week). Skillenai skill pages refresh on different days inside the window, and comparison windows still overlap by ~62 days, so share changes are posting-mix signals, not a clean week of new hiring.
- **Skillenai** measures posting mix, not hiring volume. Its Backend Engineer demand-share change is unpublished this week. Its RabbitMQ page still shows no share change. "Go" may be inflated by the ambiguous word.
- **freehire** counts a skill anywhere in a posting (including nice-to-have), so its figures are a ceiling. Its total Backend census rose 20,804 → 28,012 while every seniority level's 30-day growth is negative — treat that as a coverage/cleanup change and prefer per-level shares.
- **Fresh-postings sample (n=12) is small and search-biased.** Remote share is 100% by design. Weighted to Europe this week because that is where dated junior/mid Quarkus and Spring/Kafka postings were easiest to find. Two archive postings are closed. Postings with no clear date in or near the window were excluded where practical.
- **ITviec counts** are a one-day snapshot (6 Nov 2026) from tag-page meta text. Work-model and seniority reads cover first-page job cards only.
- **Salaries:** ITviec figures are self-reported 2025 survey medians; Second Talent is a vendor rate card; Paymetric Labs does not publish its method. Only 5 of 12 sampled postings stated pay. VND→USD at ≈26,000 is approximate.
- **Interview topic lists** come from prep sites and a vendor survey (secondary), carried over from the baseline.
- **Job-alert data** is alert titles only, from a sample of 19 alerts (7 backend-relevant). No personal data, recruiter names or contacts are included.
