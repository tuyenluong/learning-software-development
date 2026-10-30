# Backend Engineer Job Market 2026-10-30: Go · Spring Boot · Quarkus · Kafka · RabbitMQ

**Prepared by:** Jake (Research) for Tuyen Luong and Jacob (Teacher)  **Date:** 30 Oct 2026
**Purpose:** Backend-only market facts for the QE → backend → solution architect learning plan. The core teaching focus is transaction and messaging problems.
**Coverage:** first run of the weekly **Backend Engineer** report (a separate series from the QE/combined reports). Inbox window **22–30 Oct 2026**; fresh postings sampled from **14–30 Oct 2026**; index data as of **29–30 Oct 2026**.
**Builds on:** the backend parts of the 21 Oct 2026 baseline and the 28 Oct 2026 report. Those two reports were combined QE + backend reports and are now QA-only ([qe-job-market-2026.md](../qa-engineer/qe-job-market-2026.md), [job-market-2026-10-28.md](../qa-engineer/job-market-2026-10-28.md)); their backend figures are kept in [Earlier data](#earlier-data-21-oct-and-28-oct) below. This report is the **baseline for the backend-engineer series**; next Friday's report compares against it.

> **How to read the numbers**
> - **Skillenai** = a job-posting index (90-day rolling windows; this run's pages say "as of 29 Oct 2026"). It shows how often a skill shows up in postings, not total hiring. Its "demand vs prior 4 weeks" is a *share* change between two heavily overlapping windows (both ending by 26 Oct), so a 2-day move from the 28 Oct report is mostly index refresh, not a new week of hiring.
> - **freehire** = a posting aggregator that splits Backend by seniority (updated 30 Oct 2026). It counts a skill if it appears *anywhere* in a posting, including as a nice-to-have, so its percentages are a ceiling. When the number of postings that list skills changes, every percentage moves a little with it.
> - **ITviec counts** = live listing counts from itviec.com tag pages on **30 Oct 2026**. Snapshot only; two days after the last snapshot, so small moves are listing churn.
> - **Fresh-postings sample** = 13 public junior-to-lead backend postings dated 14–30 Oct 2026, found by web search for remote Go / Spring Boot / Quarkus / Kafka / RabbitMQ roles. **This is a small, search-biased sample (n=13), not a census.** Every one is remote because the searches asked for remote, so it says nothing about the remote share of the market. Four of the 13 links had already closed (HTTP 404/410) when re-checked on 30 Oct; they were read from the search index while live and are marked.
> - Anything marked **(est.)** is my own estimate or conversion. VND→USD uses about **26,000 VND/USD**, which is approximate.
> - **Inbox (Jobs label)** = aggregate only. These are LinkedIn/Glassdoor alert digests, mostly job titles. No personal data is included, and nothing was sent or changed.

---

## Top skills at a glance (30 Oct 2026)

**Backend — learn these first**
1. **Java + Spring Boot** for Vietnam and fintech — Java **27.3%** of Backend Engineer postings, up from 26.8% ([Skillenai Backend](https://skillenai.com/data/role/backend-engineer)); Spring Boot **5,634** postings across all roles, demand share **+9.5%** ([Skillenai Spring Boot](https://skillenai.com/data/skill/spring-boot)); Java in **7 of 13** sampled fresh postings and Spring Boot in **6 of 13**.
2. **REST API design** — api **47%** of junior and **68%** of middle Backend postings, rest **31% / 43%** ([freehire junior](https://freehire.me/insights/roles/backend/junior), [freehire middle](https://freehire.me/insights/roles/backend/middle)); named in **9 of 13** sampled postings.
3. **PostgreSQL + SQL** — PostgreSQL **23.4%** of Backend Engineer postings; **7 of 13** sampled postings name PostgreSQL. Transactions are where the teaching focus starts.
4. **Kafka (with RabbitMQ as the second broker)** — Kafka **18.3%** of Backend Engineer postings and **21%** of middle postings; RabbitMQ rose to **12%** of middle postings (from 9%). In the fresh sample **9 of 13** name a message broker: Kafka 8, RabbitMQ 6 (counting nice-to-haves).
5. **Distributed systems / microservices + Kubernetes** — distributed systems **25.4%**, Kubernetes **30.6%**, microservices **16.4%** of Backend Engineer postings; microservices **32%** and Kubernetes **29%** of middle postings; microservices named in **7 of 13** sampled postings.

*Python (34.3%), AWS (33.0%) and Go (26.1%) are higher in the global Backend Engineer list. They matter for the global remote market; the order above weights Vietnam and the Java path Tuyen is on.*

---

## What changed this week (21 Oct / 28 Oct → 30 Oct 2026)

**Job emails: yes, there were new ones.** 19 job-alert emails arrived in the Gmail **Jobs** label between 22 and 30 Oct. **7 were backend-relevant** (6 backend-titled LinkedIn alerts, 6 of them from the saved search "remote Backend java", plus 1 mixed Glassdoor digest with backend titles). The other 12 were QA/test or unrelated roles. All were automated digests; none came from a named recruiter, none stated a salary range, and I read them read-only: no email was replied to, labelled, archived or changed.

**The five changes worth acting on**

| # | Change | 21 Oct (baseline) | 28 Oct | 30 Oct | Read |
|---|---|---|---|---|---|
| 1 | **Event-driven architecture keeps accelerating** | 1,993 postings | 2,451, share **+15.6%** | **2,902**, share **+23.9%** | The fastest-rising backend signal in all three reports. Backend Engineer demand share is still **−9.0%**, so employers want *fewer* backend engineers who know *more* about events. Messaging stays the right core. |
| 2 | **Spring Boot and Kafka share both stepped up** | Spring Boot 4,673 (+3.4%), Kafka 7,777 | Kafka 8,265 (+2.6%) | **Spring Boot 5,634 (+9.5%)**, **Kafka 8,581 (+5.3%)**, microservices 11,401 (+5.4%), Go 15,020 (+5.4%) | Every stack Tuyen is learning gained share. Spring Boot gained most, which supports Spring as the primary stack. |
| 3 | **RabbitMQ is closer to Kafka at junior/mid level than the totals suggest** | RabbitMQ −4.6%, Kafka ≈5.2× RabbitMQ (all roles) | middle: Kafka 21%, RabbitMQ 9% | **middle: Kafka 21%, RabbitMQ 12%**; fresh sample: **Kafka 8 / RabbitMQ 6 of 13** | All-roles Kafka is still ≈**4.9×** RabbitMQ (8,581 ÷ 1,735, est.), but in junior and mid postings RabbitMQ shows up as an accepted alternative. One full RabbitMQ lesson is justified, not just a comparison slide. |
| 4 | **Vietnam backend listings dipped on every tag** | java 103, backend dev 92, spring boot 42, golang 37, microservices 28, kafka 14 | 104, 88, 44, 35, 33, 18 | **95, 81, 41, 30, 29, 15** | A 2-day drop of 7–14% across all six tags looks like end-of-month listing churn, not a trend. Watch next week. **Zero** remote listings on the first page of the kafka, golang and spring-boot tags. |
| 5 | **The junior pool shrank, middle grew** | — | Junior 1,085, Middle 1,178 | **Junior 981, Middle 1,200** (freehire 30-day growth: Junior +169, Middle +124, Senior −665) | Fewer junior seats open right now. Kafka has dropped out of the junior top 40 (below 7%), while it holds at 21% of middle postings. Messaging is a middle-level ask. |

**Backend skill shares, 21 Oct → 28 Oct → 30 Oct** (Skillenai, Backend Engineer; 2,571 → 2,627 → **2,685** postings; shares are of all postings in the window, so treat moves under 0.5 points as rounding):

| Skill | 21 Oct | 28 Oct | 30 Oct | Skill | 21 Oct | 28 Oct | 30 Oct |
|---|---|---|---|---|---|---|---|
| Python | 32.2% | 33.9% | **34.3%** | TypeScript | 16.8% | 18.3% | 18.5% |
| AWS | 31.8% | 33.0% | 33.0% | Kafka | 17.9% | 18.2% | 18.3% |
| Kubernetes | 30.5% | 30.8% | 30.6% | SQL | 15.9% | 16.8% | 17.1% |
| Java | 26.6% | 26.8% | **27.3%** | Microservices | 14.4% | 16.2% | 16.4% |
| Go | 25.6% | 25.8% | 26.1% | Observability | 16.6% | 16.5% | 16.4% |
| Distributed systems | 25.1% | 25.6% | 25.4% | Redis | 15.1% | 15.2% | 15.5% |
| PostgreSQL | 20.9% | 23.3% | 23.4% | Docker | 21.2% | 22.3% | 22.6% |
| CI/CD | 17.8% | 20.3% | 20.7% | | | | |

Over the full 21 → 30 Oct span the biggest moves are **PostgreSQL +2.5 points, CI/CD +2.9, Microservices +2.0, Python +2.1**. Nothing fell by more than 0.2 points.

**Messaging and stacks, all roles (Skillenai 90-day totals).** Totals grow partly because the index grows, so read the *share change*, not the raw count:

| Signal | 21 Oct | 28 Oct | 30 Oct | Share change (30 Oct page) |
|---|---|---|---|---|
| Kafka postings | 7,777 | 8,265 | **8,581** | **+5.3%** (was +2.6%) |
| RabbitMQ postings | 1,486 | 1,592 | **1,735** | not published on the 30 Oct page (was −4.6%) |
| Event-driven architecture | 1,993 | 2,451 | **2,902** | **+23.9%** (was +15.6%) |
| Microservices | 9,747 | 10,049 | **11,401** | **+5.4%** (was +0.7%) |
| Go | 13,887 | n/a | **15,020** | +5.4% (was +4.0%) |
| Spring Boot | 4,673 | n/a | **5,634** | **+9.5%** (was +3.4%) |

**freehire Middle Backend, 28 Oct → 30 Oct** (1,084 → 1,130 postings listing skills): kafka 21% → 21%, **rabbitmq 9% → 12%**, event-driven 21% → 19%, microservices 27% → **32%**, spring 21% → **24%**, postgresql 25% → 28%, kubernetes 28% → 29%, ci-cd 37% → 41%, observability 15% → 17%, test-automation 13% → 15%, redis 14% → 15%, distributed systems 15% → 15%.

**ITviec Vietnam, 21 Oct → 28 Oct → 30 Oct 2026** (live listing counts, same tag pages):

| Tag | 21 Oct | 28 Oct | 30 Oct |
|---|---|---|---|
| java | 103 | 104 | **95** |
| backend developer | 92 | 88 | **81** |
| spring boot | 42 | 44 | **41** |
| golang | 37 | 35 | **30** |
| microservices | 28 | 33 | **29** |
| kafka | 14 | 18 | **15** |
| quarkus | no page | 404 | **404 (≈0)** |
| rabbitmq | — | — | **404 (no tag page)** |

([java](https://itviec.com/it-jobs/java), [backend developer](https://itviec.com/it-jobs/backend-developer), [spring-boot](https://itviec.com/it-jobs/spring-boot), [golang](https://itviec.com/it-jobs/golang), [microservices](https://itviec.com/it-jobs/microservices), [kafka](https://itviec.com/it-jobs/kafka))

**Inbox (Jobs label, aggregate, 22–30 Oct):**
- **7 of 19 alerts (37%) were backend-relevant**, close to the 28 Oct report's ~40%. They carried about **10 backend or backend-adjacent titles**.
- Titles: Principal Java/Kotlin Engineer (Spring Boot), Intermediate Backend Engineer, Senior Backend Engineer, Backend Developer (Payment Integration), Middle Java Developer, JavaEE Developer (EJB), Full Stack Engineer (Java/React), Java Developer, Senior Backend Developer (Java, Fintech), Fullstack Developer.
- **Remote:** 2 titles explicitly remote-Vietnam, both from one employer (Intermediate and Senior Backend Engineer, posted 25 Oct). This is the same employer the 28 Oct report flagged for hiring two remote backend levels at once.
- **Payments and fintech:** 2 titles (a payment-integration backend role and a fintech senior backend role). Banking and fintech remain the biggest cluster.
- **Kafka, RabbitMQ, Quarkus and Go: zero hits in alert titles**, as in both earlier reports. Kotlin appeared once. Alerts are title digests; stack detail lives in the body.
- **No salary ranges were stated in any alert.**

---

## 0. Bottom line (for Jacob)

1. **Fewer backend seats, more event-driven ones.** Backend Engineer demand share is **−9.0%** for the third report running, while event-driven architecture's share change accelerated from **+15.6% to +23.9%** and Kafka's from **+2.6% to +5.3%**. Messaging and consistency is still the right core for the course.
2. **Spring Boot is the stack to lead with, and the data got stronger this week.** Spring Boot share **+9.5%** (the biggest stack move), Java up to **27.3%** of Backend Engineer postings, Java in **7 of 13** fresh postings, and **95 Java / 41 Spring Boot** listings in Vietnam against **30 Go** and **≈0 Quarkus**.
3. **Messaging is a middle-level requirement, not a junior one.** Kafka is **21%** of middle postings but below **7%** of junior postings. In the fresh sample, every **Java** junior/mid posting that names a broker accepts Kafka *or* RabbitMQ (the Go roles want Kafka), and one junior Java role is *built around* a RabbitMQ consumer with dedupe and retries — exactly the course's idempotency lessons.
4. **Vietnam is office-first.** The first page of the ITviec kafka, golang and spring-boot tags shows **0 remote** listings (kafka 11 office / 4 hybrid; golang 15 / 5; spring boot 14 / 6), and **0 junior** titles on the golang and spring-boot pages. Remote work for Tuyen comes from foreign employers and English, not from local boards.
5. **Pay: no new survey; one new vendor benchmark.** Second Talent's Oct 2026 APAC benchmark puts Southeast Asian **back-end** remote contractors at **mid $3,300/mo, senior $4,500/mo**, and Vietnam back-end seniors at **$4,600/mo**. Local medians (ITviec) are unchanged: **39.9M VND (≈$1,530)** at 5–8 years.

---

## 1. Most-demanded skills, with frequency signals

### A. Global: Skillenai, "Backend Engineer" title, 2,685 postings, 90 days to 29 Oct 2026
([source](https://skillenai.com/data/role/backend-engineer))

| Skill | Postings | Share | Skill | Postings | Share |
|---|---|---|---|---|---|
| Python | 922 | 34.3% | TypeScript | 497 | 18.5% |
| AWS | 885 | 33.0% | **Kafka** | **492** | **18.3%** |
| Kubernetes | 821 | 30.6% | SQL | 458 | 17.1% |
| **Java** | **733** | **27.3%** | Microservices | 440 | 16.4% |
| **Go** | **702** | **26.1%** | Observability | 439 | 16.4% |
| **Distributed systems** | **683** | **25.4%** | Redis | 415 | 15.5% |
| PostgreSQL | 629 | 23.4% | | | |
| Docker | 606 | 22.6% | | | |
| CI/CD | 557 | 20.7% | | | |

- **Demand share down 9.0% vs the prior four weeks** (adjusted posting share 1.1% → 1.0%). Same figure as 28 Oct; the comparison windows barely moved.
- **Top posters:** GitLab 132, Grafana Labs 112, CLERA 64, Wise 62, Stripe 58, Vinted 42, ABOUT YOU 42. Remote-friendly product companies, unchanged.
- **Top metros:** Berlin 4.4%, New York City 3.0%, London 2.9%, San Francisco 2.7%, Tel Aviv 2.5%, Bengaluru 2.0%.
- **Career flows:** Backend Engineer hires come mainly from Software Engineer (104 moves in, 57 out). Unchanged.

### B. By seniority: freehire, open Backend postings, updated 30 Oct 2026

| Level | Open postings | Skill leaders |
|---|---|---|
| **Junior** | **981** (846 list skills) | api 47%, python 42%, **java 39%**, sql 33%, rest 31%, git 30%, ai 24%, docker 21%, ci-cd 21%, cloud 20%, postgresql 19%, aws 19%, mysql 18%, nodejs 17%, **spring 16%**, microservices 13%, redis 12%, kubernetes 10%, go 7% — **kafka not in the top 40 (<7%)** |
| **Middle** | **1,200** (1,130 list skills) | api 68%, rest 43%, java 42%, ci-cd 41%, aws 40%, cloud 38%, docker 35%, **microservices 32%**, git 32%, sql 31%, ai 30%, python 30%, **kubernetes 29%**, postgresql 28%, **spring 24%**, **kafka 21%**, azure 21%, **event-driven 19%**, mysql 19%, **observability 17%**, redis 15%, **test-automation 15%**, distributed systems 15%, **rabbitmq 12%**, llm 11% |

([freehire junior](https://freehire.me/insights/roles/backend/junior), [freehire middle](https://freehire.me/insights/roles/backend/middle), [freehire seniority split](https://freehire.me/insights/roles/backend))

- **The junior-to-middle jump** (the most useful line for the course): Kubernetes **10% → 29%**, microservices **13% → 32%**, CI/CD **21% → 41%**, AWS **19% → 40%**, Kafka **<7% → 21%**, observability **not in junior top 40 → 17%**, RabbitMQ **not in junior top 40 → 12%**.
- **Seniority census, 30 Oct:** 20,804 open Backend roles (was 23,169 on 28 Oct) — Senior 13,980, Lead 1,970, **Middle 1,200**, Staff 1,186, Intern 1,065, **Junior 981**, Principal 316, C-level 106. 30-day growth: Middle **+124**, Junior **+169**, Intern +665, Senior **−665**. Junior + Middle together are about **10.5%** of open roles (est.).

### C. Fresh postings sample: 13 remote backend postings, 14–30 Oct 2026

*Small, search-biased sample (n=13). Use it for what employers write in junior/mid postings right now, not for market shares.*

| # | Role (employer) | Posted | Level | Where | Stack named | Pay stated |
|---|---|---|---|---|---|---|
| 1 | [Software Engineer, Distributed Databases (DoorDash)](https://getdataengineeringjobs.com/jobs/4176-software-engineer-distributed-databases-doordash/) | 20 Oct | Junior (1+ yr) | Remote, no restriction stated | Go, Kafka, PostgreSQL, Redis, Cassandra, CockroachDB, AWS | No |
| 2 | Middle/Senior Go Developer (Intetics) — *link closed 30 Oct (404)* | ~25 Oct | Mid/Senior | Remote, Ukraine | Go, REST + gRPC, **Kafka and/or RabbitMQ**, PostgreSQL, Docker, microservices, Grafana/Prometheus, backend tests | No |
| 3 | Software Backend Engineer, mid (Angkas) — *link closed (410)* | 20 Oct | Mid (3+ yr) | Remote/hybrid, Philippines | Go, Kafka, Kubernetes, Redis, PostgreSQL | No |
| 4 | [Remote Backend Engineer, Go/Kafka/AWS (Oliver Bernard)](https://jobboard.ph/backend-engineer_quezon-city-c14862825/2026-10-oliver-bernard_i4254842158) | 21 Oct | Not stated | Remote, Europe | Go or Python, Kafka, AWS, event-driven microservices, SQL/NoSQL | **Up to €95K/yr** + share options |
| 5 | [Backend Mid, Java/Kafka/Spring Boot/AWS (Métrica)](https://www.spainjobs.io/es/empresas/metrica/desarrolladora-backend-mid-java-kafka-spring-boot-aws--22fcd61272) | ≤22 Oct | Mid | Remote, Spain | Java 17+, Spring Boot 3, **Kafka (RabbitMQ/SQS-SNS accepted)**, PostgreSQL/Oracle, hexagonal architecture, JUnit + Mockito, GitHub Actions, OpenAPI | No |
| 6 | Back-End Engineer Java, Mid-Level (TQI) — *link closed (410)* | ~23 Oct | Mid | Remote, Brazil | Java/Kotlin, Spring (Boot/Data/Cloud), **RabbitMQ/JMS/Kafka**, microservices, Oracle, AWS, CI/CD, New Relic/Grafana/ELK, test automation | No |
| 7 | [Java Backend Developer (LITIT)](https://keywordise.com/jobs/java-backend-developer-5zj2oawwdl) | 14 Oct | Mid | Remote, worldwide | Java, **Quarkus**/Jakarta EE or Spring Boot, REST, Docker, CI/CD, unit + integration tests | No |
| 8 | [Senior Java Backend Developer (Tieto Tech Consulting)](https://jobcore.r5b.is-great.net/remote-jobs/senior-java-backend-developer-tieto-tech-consulting-mfd) | 28 Oct | Senior (5+ yr) | Remote, Europe/EMEA | Java 21, **Quarkus** (Spring Boot accepted), REST, PostgreSQL, Oracle, Kubernetes, Jenkins, JUnit, SonarQube | No |
| 9 | [Backend Developer, Jakarta EE/Quarkus (m2TALENTS)](https://www.glassever.com/jobs/backend-developer-jakarta-ee-quarkus-m2talents-job-2) | 20 Oct | Mid (3+ yr) | Remote, Germany (German C1) | Java, Jakarta EE, **Quarkus**; nice: REST, microservices, CI/CD | No (benefits only) |
| 10 | [Junior/Mid Back-end Developer (Hyperativa)](https://www.remotery.co/job/remote-juniormid-level-back-end-developer-at-hyperativa-in-brazil-full-time-66d8cb) | ~29 Oct | Junior/Mid | Remote, Brazil | C#/.NET 8, REST, SQL Server, DDD; preferred: **RabbitMQ**, Redis, Docker, Kubernetes; PCI | No |
| 11 | [Java Developer Junior, Notifications (via Sylision)](https://www.sylision.com/vagas/desenvolvedor-java-junior-notificacoes-487) | 26 Oct | Junior | Remote, Brazil | Java, Spring Boot, **RabbitMQ consumer**, **dedupe by event id**, **retries with growing backoff**, PostgreSQL, JUnit 5; nice: Kafka, Docker Compose | **R$3,000–4,500/mo** |
| 12 | [Backend Engineer, Remote Vietnam (Alongside)](https://jobs.evolc.com/job/alongside-backend-engineer-remote-vietnam-y5584) | 20 Oct | Mid (2–5 yr) | **Remote, Vietnam**, contract | C#/.NET, third-party APIs and webhooks, event correlation from telemetry | **$12–16/hr** |
| 13 | Lead Java Backend Developer (Komplete Teleservices, via Dice) — *link closed (410)* | ~15 Oct | Lead (7+ yr) | Remote, US (EST/CST) | Java 17+, Spring Boot, **Kafka, RabbitMQ**, microservices, event-driven, PostgreSQL, MongoDB/DynamoDB, Redis, Docker, Kubernetes, OAuth2/JWT, Prometheus/Grafana/ELK | DOE (not stated) |

**Counts across the 13 (mentioned anywhere, including nice-to-have):**

| Skill | Count | Skill | Count |
|---|---|---|---|
| REST / API | 9 | Java | 7 |
| **Any message broker** | **9** | Microservices | 7 |
| PostgreSQL | 7 | **Kafka** | **8** |
| Spring Boot | 6 | **RabbitMQ** | **6** |
| Tests named (unit/integration/JUnit/TDD/automation) | 6 | CI/CD | 6 |
| Redis | 5 | Event-driven named | 5 |
| Go | 4 | Docker (incl. Docker Compose) | 5 |
| Kubernetes | 4 | AWS | 4 |
| Quarkus | 3 | Oracle | 3 |
| Observability tools (Grafana/Prometheus/ELK/New Relic) | 3 | C#/.NET | 2 |
| AI mentioned | 3 | gRPC | 1 |

- **Seniority:** Junior 2, Junior/Mid 1, Mid 6, Mid/Senior 1, Senior 1, Lead 1, not stated 1.
- **Remote:** 13 of 13 by search design. Only **2 of 13** were open worldwide or without a stated country restriction; the rest were tied to one country or region. **1 of 13** (a .NET contract) was open to Vietnam-based engineers.
- **Salary stated: 3 of 13** — up to €95K/yr (Europe), R$3,000–4,500/mo (Brazil, junior), $12–16/hr (Vietnam, contract). Too few to summarise.
- **Brokers are "either/or" at junior and mid.** Of the 9 postings naming a broker, 4 accept Kafka *or* RabbitMQ (or JMS/SQS). Only the Go roles (#1, #3, #4) named Kafka alone.

### D. Vietnam: ITviec live counts and first-page read, 30 Oct 2026

- Counts: "java" **95**, "backend developer" **81**, "spring boot" **41**, "golang" **30**, "microservices" **29**, "kafka" **15**, "quarkus" and "rabbitmq" no tag page (404, ≈0).
- **Work model on the first page of each tag:** kafka 15 listings → 11 at office, 4 hybrid, **0 remote**; golang first 20 → 15 office, 5 hybrid, **0 remote**; spring boot first 20 → 14 office, 6 hybrid, **0 remote**.
- **Seniority in titles, first page:** golang 20 → **12 senior or above** (senior, staff, expert, lead, architect), 4 middle or middle/senior, 4 unstated, **0 junior**. Spring boot 20 → **10 senior or above**, 4 mid/senior, 1 "All Level", 5 unstated, **0 junior**.
- **Kafka-tagged titles are Java-heavy:** 7 of the 15 name Java or Spring Boot; 4 name Go (two name both).
- One posted range visible in a title: Mid/Sr Java Developer (English required) **"up to $3,200"** (same listing as on 28 Oct).

---

## 2. Must-have vs nice-to-have vs differentiator (junior → mid → senior)

*My synthesis, from the frequencies above, the 13 fresh postings and the interview sources in §6.*

| Level | Must-have | Nice-to-have | Differentiator |
|---|---|---|---|
| **Junior** | Java + Spring Boot (or Go); REST; SQL + PostgreSQL; Git; unit tests (JUnit/Mockito); Docker basics | A message queue "even from study" (the Brazilian junior posting says exactly this); Redis; one cloud | A small service that **dedupes events and retries with backoff**, tested — the same task a junior notifications role describes |
| **Mid** | Java 17/21 + Spring Boot 3 **or** Go; REST (OpenAPI); PostgreSQL (indexes, transactions); Docker; unit + integration tests; CI/CD; **Kafka or RabbitMQ producer/consumer in production**; microservices | Kubernetes; Redis; observability (Grafana/Prometheus/ELK); hexagonal architecture; gRPC; Oracle (banks) | Testing your own services under failure (Tuyen's natural edge); fintech domain basics |
| **Senior** | Distributed systems: messaging, retries, timeouts, idempotency, outbox/saga, consistency trade-offs; observability; performance and concurrency; system design; on-call thinking | Event sourcing/CQRS; Kafka Streams/Connect/Debezium; K8s operations; OAuth2/OIDC | Proving correctness under failure (fault injection, duplicate/out-of-order delivery tests); payments depth; ADRs and design docs |

*Change from the 28 Oct report: a **junior** row is added because this series is backend-only. The mid row now says "Kafka **or** RabbitMQ in production" as a must-have: 9 of 13 fresh postings name a broker, and the middle share of RabbitMQ rose to 12%.*

---

## 3. Messaging, transactions and distributed systems: how often, and how tested

### Frequency signals

| Signal | Number | Source |
|---|---|---|
| Kafka postings (all roles, 90d) | **8,581** (share **+5.3%** vs prior 4 weeks) | [Skillenai Kafka](https://skillenai.com/data/skill/kafka) |
| RabbitMQ postings (90d) | **1,735** → Kafka is about **4.9×** RabbitMQ (est.; was 5.2× on 28 Oct) | [Skillenai RabbitMQ](https://skillenai.com/data/skill/rabbitmq) |
| Event-driven architecture postings (90d) | **2,902** (share **+23.9%**) | [Skillenai EDA](https://skillenai.com/data/skill/event-driven-architecture) |
| Microservices postings (90d) | **11,401** (share +5.4%) | [Skillenai microservices](https://skillenai.com/data/skill/microservices) |
| Share of Backend Engineer postings | Distributed systems 25.4%, Kafka 18.3%, microservices 16.4%, observability 16.4%, Redis 15.5% | [Skillenai Backend](https://skillenai.com/data/role/backend-engineer) |
| Share of **Middle** Backend postings | **Kafka 21%**, event-driven 19%, observability 17%, distributed systems 15%, **RabbitMQ 12%** | [freehire middle](https://freehire.me/insights/roles/backend/middle) |
| Share of **Junior** Backend postings | Kafka and RabbitMQ both **below 7%** (not in top 40); microservices 13%, redis 12% | [freehire junior](https://freehire.me/insights/roles/backend/junior) |
| Top role for each broker | Software Engineer: 40.0% of Kafka postings, 44.1% of RabbitMQ postings | Skillenai Kafka / RabbitMQ |
| Top Kafka employers | Wise 186, Cisco 156, CrowdStrike 114, **Mastercard 111, Barclays 92, Capital One 78**, Databricks 69, **JPMorgan 61** | [Skillenai Kafka](https://skillenai.com/data/skill/kafka) |
| Top EDA employers | **Mastercard 62, Wise 62, Barclays 37**, Fiserv 18, Capco 15 | [Skillenai EDA](https://skillenai.com/data/skill/event-driven-architecture) |
| Top RabbitMQ employers | Wrike 28, CLERA 24, Klaviyo 18, Wise 18, Encora 16 | [Skillenai RabbitMQ](https://skillenai.com/data/skill/rabbitmq) |
| Fresh sample (n=13) | Broker named in **9**: Kafka 8, RabbitMQ 6; explicit dedupe/idempotency + backoff retries in **1** (junior) | §1C |
| Vietnam | ITviec "kafka" **15**, "microservices" **29** (vs "java" 95); no RabbitMQ tag | ITviec, 30 Oct 2026 |

**Read (my interpretation):**
- **Kafka is still the broker to lead with**; banks and payments companies (Mastercard, Barclays, Capital One, JPMorgan, Wise) dominate its top employers, which matches Vietnam's fintech-heavy backend titles.
- **Event-driven architecture is accelerating while backend demand falls.** That gap is the course's opportunity: Tuyen already knows how event flows fail.
- **RabbitMQ deserves a full lesson.** It is a smaller market overall, but at junior and mid level employers write "Kafka or RabbitMQ", and the one junior posting that describes real work is a RabbitMQ consumer with dedupe and backoff.
- **Junior postings rarely require messaging; middle postings usually expect it.** Teach messaging as the Stage 2 → Stage 3 bridge, with the idempotency piece early.

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
| Global postings, 90d (Skillenai, 30 Oct) | **15,020** (share +5.4%) ¹ | **5,634** (share **+9.5%**) | no Skillenai page |
| Share of Backend Engineer postings | **26.1%** | (Java 27.3%) | n/a |
| Top employers | Capital One 745, Cisco 491, **Stripe 209**, Anduril 175, SpaceX 169, **Grab 162**, CrowdStrike 158 | **Mastercard 310**, Wise 137, **Barclays 121**, Capco 58, Cisco 58, JPMorgan 57 | (sample: telecom consultancy, automotive client, German health-tech) |
| Fresh sample (n=13) | **4** (all three Go-led roles name Kafka) | **6** | **3** — all remote Europe/worldwide, mid to senior |
| freehire junior / middle | go 7% junior; not in middle top 40 | spring 16% junior / 24% middle | not in either top 40 |
| Vietnam ITviec (30 Oct) | **30** (was 35, 37) | **41** (Java 95) | **≈0** (404) |
| Vietnam first-page seniority | 12 of 20 senior+, 0 junior | 10 of 20 senior+, 0 junior | n/a |

¹ "Go" is an ambiguous word; treat Skillenai's count as an upper bound.

Sources: [Skillenai Go](https://skillenai.com/data/skill/go), [Skillenai Spring Boot](https://skillenai.com/data/skill/spring-boot), [ITviec golang](https://itviec.com/it-jobs/golang), [ITviec spring-boot](https://itviec.com/it-jobs/spring-boot). SO 2026 and Java-org survey figures (21 Oct) are in [Earlier data](#earlier-data-21-oct-and-28-oct) and were not re-pulled.

**Verdict (unchanged, with stronger support):**
- **Spring Boot is the primary stack.** It had the biggest share gain this week, it leads in Vietnam and in banks and fintech, and it fits Tuyen's saved "remote Backend java" search (6 of the 7 backend alerts this week).
- **Go is the second language for remote and global product companies.** Vietnam Go listings slipped again (37 → 35 → 30) and are senior-heavy, so Go is a remote-market play, not a local junior entry.
- **Quarkus: concepts only, plus one honest note.** It is ≈0 in Vietnam but showed up in 3 of 13 remote European postings, always as "Quarkus *or* Spring Boot / Jakarta EE". One or two comparison lessons are enough; most Spring knowledge carries over.

---

## 5. Salary ranges

**No new local survey this window.** No alert stated a salary. The ITviec survey below is the 2025–2026 edition, unchanged. One new vendor benchmark (Second Talent APAC, Oct 2026) gives a back-end-specific remote line.

### Vietnam local: ITviec 2025–2026 report, median **gross VND / month**
([ITviec report](https://itviec.com/report/vietnam-it-salary-and-recruitment-market), 1,839 respondents, surveyed May–Nov 2025)

| Role | <1 yr | 1–2 yr | 3–4 yr | 5–8 yr | >8 yr | Overall |
|---|---|---|---|---|---|---|
| **Back-end Developer** | 12.4M (≈$480) | 25.35M (≈$975) | 30.1M (≈$1,160) | **39.9M (≈$1,530)** | **54.9M (≈$2,110)** | 37.8M |
| Tech Lead | – | 45.3M | 53.85M | – | 68.45M | 51.8M (≈$1,990) |

- **Go (Second Talent rate card, vendor):** junior 20–35M, mid 35–55M, senior 55–80M VND/month ([source](https://www.secondtalent.com/developer-rate-card/golang-developer-vietnam/)). Unchanged; an upper-market estimate.
- **Paymetric Labs** lists a Vietnam back-end (Java/Go/Node.js) median of **₫41.6M/month**, range ₫37.8–42.6M, +6.5% year on year ([source](https://www.paymetriclabs.com/vn/salaries/back-end-developer-java-go-node-js)). Its method and sample size are not stated; treat as a cross-check only. It sits close to ITviec's 5–8 year median.
- **Posted range visible on ITviec, 30 Oct:** Mid/Sr Java (English required) "up to $3,200". One listing.

### Remote / international (Vietnam-based engineer, USD / month)

| Source | Back-end | Notes |
|---|---|---|
| [Second Talent APAC benchmark, Oct 2026](https://www.secondtalent.com/apac-salary-benchmark/) (vendor, **new this report**) | **Southeast Asia back-end family (35 rate cards):** junior **$2,500** ($1,800–3,300), mid **$3,300** ($2,500–4,300), senior **$4,500** ($4,300–5,600), lead $5,400 ($4,500–7,200). **Vietnam back-end senior median: $4,600** | Remote contractor rates. The 28 Oct report used only its Vietnam all-roles line (mid $3,100, senior $4,500) |
| [Second Talent, Vietnam rates 2026](https://www.secondtalent.com/resources/true-cost-outsource-software-development-vietnam/) (vendor) | Mid **$3,400–4,900** · Senior **$4,900–7,000** · Lead/Architect $7,000–9,800 | Unchanged from 28 Oct; Go/.NET seniors +10–20% |
| Fresh sample (n=3 with pay) | Vietnam remote .NET contract **$12–16/hr** (≈$2,100–2,800/mo full-time, est.); Europe remote Go/Kafka **up to €95K/yr**; Brazil junior Java R$3,000–4,500/mo | Single postings |
| Global reference ([SO 2026 comp](https://survey.stackoverflow.co/2026/work/data/compensation)) | Back-end median **$85,296/yr**; architect **$102,355/yr** | Mostly US/EU respondents; baseline figure |

**Read (est.):** a mid-level remote backend engineer in Vietnam lands around **$2,500–4,300/mo** on contractor rates, and a senior around **$4,300–5,600/mo**. Both are roughly **2–3×** the local ITviec medians for 3–8 years. English is still the gate.

---

## 6. Typical interview formats and common topics

*Unchanged from the baseline; not re-surveyed this window.*

- **Market-wide (CoderPad 2026, ~650 respondents):** algorithmic 43%, real-world scenarios 38%, system design 38%, pair programming 30%, code review 21%, debugging 19%. 46% of companies allow AI in interviews in some form; the skill signals are catching AI mistakes (66%) and explaining trade-offs (56%).
- **Backend loop (mid/senior):** recruiter → coding (DSA or a practical service task) → **system design** (seniors often get 2 rounds) → **deep-dive** (Spring internals or Go concurrency, DB and transactions, Kafka) → behavioural.
  - **Spring:** DI and bean lifecycle; `@Transactional` propagation and pitfalls; **JPA N+1**; connection pools; virtual threads.
  - **Go:** goroutines, channels, `context` cancellation, races (`-race`), worker pools.
  - **Messaging:** see §3.
- **Signals in this week's postings:** one mid Spring posting asks candidates to give an example of how a SOLID principle helped a real design, and names hexagonal architecture; one senior Go posting sets English at **B2+**; the German Quarkus role requires German C1.
- **Vietnam specifics (est.):** outsourcing firms run a shorter loop (tech interview, English check). Foreign in-house and remote employers add system design.

---

## 7. Trends

**Event-driven architecture is the fastest-rising backend skill**
- Share change **+23.9%** (2,902 postings), up from +15.6% two days earlier and from 1,993 postings on 21 Oct. Banks and payments firms lead (Mastercard, Wise, Barclays, Fiserv).
- **Implication:** the course's messaging core is aligned with where demand is moving, and "how event flows fail" is exactly what a QA background prepares Tuyen to talk about.

**Backend demand share is still falling**
- Backend Engineer demand share **−9.0%** vs the prior four weeks, and freehire's Senior pool lost 665 roles in 30 days. Junior (+169) and Middle (+124) grew, but from a small base (about 10.5% of open roles together, est.).
- **Implication:** a junior backend CV needs proof (a deployed service, tests, one broker) more than ever.

**Spring Boot is gaining fastest of the three stacks**
- Spring Boot share **+9.5%** vs Go +5.4%; Quarkus remains ≈0 in Vietnam.

**AI in backend postings is broad but shallow**
- freehire "ai": **24%** junior, **30%** middle; "llm" 11% of middle postings. In the fresh sample **3 of 13** mention AI (AI-driven features, AI concepts, an AI automation platform). Broad keyword, treat as directional.

**Vietnam stays office-first and senior-heavy**
- 0 remote and 0 junior titles on the first pages of the golang and spring-boot tags (§1D). Remote options come from foreign employers; the inbox's two remote-Vietnam roles came from one foreign employer.

---

## 8. Recommended skill priority list (junior → mid backend)

*Time estimates assume about 6–8 hrs/week and are my estimates. Jacob should confirm Tuyen's actual weekly time. Order follows the baseline backend phases; changes from this week's data are marked **new**.*

### Stage 1: Junior foundations (months 0–6)
1. **Java 21 + Spring Boot 3:** REST with OpenAPI, validation, error handling, JPA/Hibernate (including **N+1**). *(Java 39% of junior postings; Spring Boot in 6 of 13 fresh postings.)*
2. **SQL + PostgreSQL transactions:** joins, indexes, isolation levels, lost update. *(PostgreSQL 23.4% of Backend Engineer postings; 7 of 13 fresh postings.)*
3. **Testing:** JUnit 5 + Mockito, then Testcontainers integration tests. *(Tests named in 6 of 13; test-automation 15% of middle postings.)*
4. **Git, Maven, Docker, a CI pipeline (GitHub Actions).** *(CI/CD 21% junior → 41% middle.)*

### Stage 2: Strong junior (months 6–12)
5. **new — Idempotent consumer + retries with backoff, on RabbitMQ first.** Build a notifications consumer that dedupes by event id, retries with growing backoff, and records history in PostgreSQL. *(This is almost word for word the junior posting #11.)*
6. **Payments on the orders API with idempotency keys**, plus a first AWS deploy. *(AWS 19% junior → 40% middle.)*
7. **Auth (JWT/OAuth2 basics).**

### Stage 3: Mid-level (months 12–24)
8. **Kafka with Spring for Apache Kafka:** keys and partitions, consumer groups, offset commits, retries/DLT, consumer lag. *(Kafka 21% of middle postings; 8 of 13 fresh postings.)*
9. **Reliability patterns:** transactional outbox, saga with compensations, timeouts and circuit breakers.
10. **Kubernetes basics + observability** (structured logs, Prometheus/Grafana, OTel traces across async hops). *(Kubernetes 10% → 29%, observability → 17% from junior to middle.)*
11. **Redis caching.** *(Redis 15.5% of Backend Engineer postings.)*
12. **new — Hexagonal architecture** as the structure for the payments/orders service. *(Named in a mid Spring posting; makes messaging and persistence adapters testable.)*

### Later: Go and architect track
13. **Go** as the second language, porting one service with a Kafka consumer. *(Remote-market play; Vietnam Go listings are senior-heavy.)*
14. **Quarkus**, 1–2 comparison lessons. **System design** practice (payments, wallet, notifications), ADRs.

---

## 9. Backend path vs the market

*Checked against this week's 13 fresh postings and freehire junior/middle data. The full 28 Oct gap analysis is in [Earlier data → 28 Oct gap analysis](#28-oct-gap-analysis-backend-path-vs-the-market); this section only records what this week's data adds.*

| Path element | This week's evidence | Verdict |
|---|---|---|
| Spring Boot CRUD + PostgreSQL + tests (Stage 1) | Spring Boot 6/13, PostgreSQL 7/13, tests 6/13; junior posting #11 asks for JUnit 5 by name | **Covered, keep** |
| API idempotency and retries (Stage 2) | Junior posting #11 is built on "avoid duplicate sends using the event id" and "retries with growing intervals" | **Covered; move the messaging version earlier (Stage 2)** |
| Messaging basics (Stage 3) | Brokers in 9/13; Kafka <7% junior → 21% middle; RabbitMQ 12% middle | **Covered; teach RabbitMQ first, then Kafka** |
| Observability (Stage 3) | 3/13 name Grafana/Prometheus/ELK/New Relic; 17% of middle postings | **Covered, keep** |
| Kubernetes | 4/13; 10% junior → 29% middle | **Gap noted on 28 Oct still stands: move basics to end of Stage 2** |
| JPA/Hibernate, Maven, Mockito | Mockito named in posting #5; Spring Data JPA in #6 | **Gap noted on 28 Oct still stands: add to Stage 1** |
| Hexagonal / ports-and-adapters | Named in mid posting #5 | **new gap, small: one lesson in Stage 3** |
| Outbox / saga | Named in **0** of 13 postings | **Interview depth, not a CV keyword** (unchanged) |

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

*(Link check, 30 Oct 2026: the Skillenai, freehire, ITviec (java, backend-developer, spring-boot, golang, microservices, kafka) and Second Talent pages returned HTTP 200. ITviec quarkus and rabbitmq tag pages returned 404. Of the 13 sampled postings, 9 returned 200; #2 returned 404 and #3, #6 and #13 returned 410 (closed). All resource URLs above, plus the ITviec report, CoderPad, SO 2026 comp and both Second Talent pages, returned 200.)*

---

## Earlier data (21 Oct and 28 Oct)

*These backend figures first appeared in the two combined QE + backend reports (21 Oct baseline and 28 Oct catch-up). Those reports are now QA-only, so the backend figures that are not already in the sections above are kept here with their original sources. They were not re-pulled on 30 Oct.*

### From the 21 Oct 2026 baseline

**Skillenai and hiring surveys**
- **Kafka in Java backend titles:** 29.0% of "Java Backend Engineer", 27.8% of "Java Backend Developer" postings. **RabbitMQ in backend titles:** 14.3% of "Back-End Engineer", 8.8% of "Backend Software Engineer", often paired *with* Kafka ([Skillenai Kafka](https://skillenai.com/data/skill/kafka), [Skillenai RabbitMQ](https://skillenai.com/data/skill/rabbitmq)).
- **CoderPad State of Tech Hiring 2026:** back-end is the #2 role hiring managers plan to fill (46%, after full-stack 49%) and #3 hardest to fill (16%). Software architect is in 15% of hiring plans. 82% of developers find GenAI useful and 54% would lose ≥10% productivity without it; developers expect system design and debugging to grow in importance. Hiring budgets are expected to rise at 53% of companies (vs 37% in 2025) ([CoderPad](https://coderpad.io/survey-reports/coderpad-state-of-tech-hiring-2026/)).
- **Career flows:** Backend Engineer hires came mainly from Software Engineer (88 moves on 21 Oct; 104 in / 57 out on 28 Oct) ([Skillenai Backend](https://skillenai.com/data/role/backend-engineer)).

**Go vs Spring Boot vs Quarkus: usage surveys**

| Signal | Go | Spring Boot | Quarkus |
|---|---|---|---|
| SO 2026 usage | Go language **16.5%** | Spring Boot **12.8%** of web-framework users (Java 27.6%) | **0.3%** (may not have been a listed option, so likely understated) |
| Java-org surveys | n/a | Azul 2025: **42%** of orgs use Spring Boot for Java microservices; Vaadin 2025: 86% | Azul 2025: **7%**; Jakarta EE 2025 survey: Quarkus runtime use **declining** |
| UK permanent jobs (ITJobsWatch, 6 mo) | n/a | n/a | **2** (vs 15 a year ago) |
| Live roles | n/a | n/a | Alion lists **91–152** live Quarkus roles |
| Top employers (Skillenai) | Capital One, Cisco, SpaceX, Stripe, CrowdStrike, Cloudflare, Grab | Mastercard, Barclays, Wise, JPMorgan, Capco | Citi, Sopra Steria, Red Hat consulting, defence/gov (OpenShift shops) |

Sources: [SO 2026 languages](https://survey.stackoverflow.co/2026/technology/data/languages), [SO 2026 web frameworks](https://survey.stackoverflow.co/2026/technology/data/web-framework), [Azul State of Java 2025](https://www.qbssoftware.com/wp-content/uploads/2025/04/Azul-report-State-of-Java-2025.pdf), [Jakarta EE 2025 survey](https://outreach.eclipse.foundation/hubfs/2025%20Jakarta%20EE%20Developer%20Survey%20Report.pdf), [ITJobsWatch Quarkus](https://www.itjobswatch.co.uk/jobs/uk/quarkus.do), [Alion Quarkus jobs](https://alion.io/jobs/quarkus), [Skillenai Go](https://skillenai.com/data/skill/go), [Skillenai Spring Boot](https://skillenai.com/data/skill/spring-boot).

**Vietnam**
- **vitX** (4 weeks to 15 Oct 2026): backend is the largest discipline, **144 of 469** engineering roles (30.7%). Stacks named in job titles: **Java 52**, Python 43, React 35, .NET 26, AWS 23, **Go 22**. Banks, fintechs and securities firms posted **19%** of roles. **45.4%** of roles are senior, lead or manager and only **5.4%** junior. Remote is only **2.8%** of Vietnam-board roles. AWS is named about **3.3×** as often as Azure ([vitX](https://www.vitx.global/reports/vitx-vietnam-it-hiring-pulse-2026-10.pdf)).
- **TopDev 2024–25:** Spring Boot is the #1 Java framework at **45.2%** ([TopDev](https://topdev.vn/download-report)).
- **ITviec 2025–2026 survey, Project Leader/PM** (median gross VND/month): <1 yr 17.2M, 1–2 yr 29.85M, 3–4 yr 48.4M, 5–8 yr 58.45M, overall 50.1M ([ITviec report](https://itviec.com/report/vietnam-it-salary-and-recruitment-market)).
- **Inbox (21 Oct, aggregate):** about **40%** of alerts were backend, mostly from the saved search "remote Backend java" (Java/Spring, AWS/Azure, API); about **19 of 41** backend alerts were remote. Keyword hits in alert bodies over 6 months: Spring Boot 3 threads, Go-related 6 (ambiguous match), Kafka, RabbitMQ and Quarkus 0. One posted range in an alert title: "Senior Java, good English, remote, **up to 55M gross**".

**Remote pay (Vietnam-based engineer)**
- [Second Talent APAC benchmark](https://www.secondtalent.com/apac-salary-benchmark/) (vendor), Vietnam **all-roles** median: mid **$3,100**, senior **$4,500** (IQR $4,300–5,500), lead **$5,300**.
- Live listing ([Jobstore](https://www.jobstore.com/vn/job/l23019796/senior-java-developer-remote-job)): Senior Java remote contract **$30–90/hr** (VND 60–110M/mo). One listing, anecdotal.
- **Estimates (21 Oct, est.):** senior backend remote about **$5–7K/mo**, a premium of about **+25–35%** over senior QA automation remote; architect/lead roles **$7–10K/mo**; locally the backend move is worth about **+35–55%** over Tester/QA-QC medians at 5–8+ years.

**Interviews: backend loop topics not listed in §6**
- **Data:** indexes, isolation levels, locking, migrations.
- **Ops:** observability, rate limiting, circuit breakers, retries with jitter.

**QE → backend transition and architect path**
- Practitioner guides suggest an **internal transfer** first, and **3–6 months** of focused work if you already write strong automation code (12–18 months if not) ([SeekerScore](https://www.seekerscore.com/routes/qa-engineer-to-software-engineer), [Codefarm](https://codefarm.in/blog/software-engineering/qa-to-developer-transition)). Secondary sources; treat the timelines as estimates.
- The switch is uncommon (2 observed SDET→Software Engineer moves vs 10 SE→SDET), so it needs deliberate proof: a deployed service, production-quality code, and system-design fluency.
- **Architect path:** SO 2026 "Architect, software or solutions" is 7% of respondents with a **$102K** global median; ITviec Tech Lead median 51.8M VND, PM/PL 50.1M. Architects are expected to make and document trade-offs (ADRs), handle reliability, scaling, cost, security and cross-team integration.

### From the 28 Oct 2026 report

**Skillenai, Backend Engineer (2,627 postings, 90 days to 27 Oct)**
- **Top posters:** GitLab 129, Grafana Labs 117, CLERA 61, Wise 60, Stripe 56. **Top metros:** Berlin 4.4%, New York City 3.1%, London 2.8%, San Francisco 2.7%, Tel Aviv 2.5% ([Skillenai Backend](https://skillenai.com/data/role/backend-engineer)).
- **Kafka in titles:** 28.6% of "Java Backend Engineer", 30.1% of "Distributed Systems Engineer". **RabbitMQ in titles:** 12.1% of "Back-End Engineer", 10.6% of "Java Engineer". Kafka is paired most with Python, Java, Kubernetes, AWS and SQL ([Skillenai Kafka](https://skillenai.com/data/skill/kafka), [Skillenai RabbitMQ](https://skillenai.com/data/skill/rabbitmq)).
- **Top Kafka employers:** Wise 175, Cisco 149, CrowdStrike 115, Mastercard 101, Barclays 91, Capital One 70, JPMorgan 60. **Top event-driven architecture employers:** Wise 50, Mastercard 45, Barclays 35, Fiserv 16, Capco 16, Airwallex 12 ([Skillenai EDA](https://skillenai.com/data/skill/event-driven-architecture)).

**freehire, open Backend postings by seniority (updated 27–28 Oct)**

| Level | Open postings | Skill leaders |
|---|---|---|
| **Junior** | **1,085** (937 list skills) | api 47%, python 40%, java 39%, sql 33%, git 29%, rest 27%, ai 23%, docker 22%, cloud 20%, ci-cd 20%, postgresql 18%, aws 18%, spring 17%, microservices 13%, redis 11%, kubernetes 11%, azure 9%, kafka 7%, gcp 7% |
| **Middle** | **1,178** (1,084 list skills) | api 65%, java 41%, aws 41%, rest 39%, cloud 38%, ci-cd 37%, ai 35%, docker 33%, python 31%, kubernetes 28%, microservices 27%, sql 27%, git 27%, postgresql 25%, azure 22%, spring 21%, event-driven 21%, kafka 21%, mysql 18%, devops 18%, agile 17%, observability 15%, distributed systems 15%, gcp 15%, redis 14%, nosql 14%, test-automation 13%, rabbitmq 9%, s3 9% |

([freehire junior](https://freehire.me/insights/roles/backend/junior), [freehire middle](https://freehire.me/insights/roles/backend/middle), [freehire backend seniority split](https://freehire.me/insights/roles/backend))

- **Junior → middle jumps (28 Oct):** Kubernetes 11% → 28%, CI/CD 20% → 37%, AWS 18% → 41%, microservices 13% → 27%, Kafka 7% → 21%. Observability is not in the junior top 40 and is 15% at middle.
- **Seniority census (28 Oct):** 23,169 open Backend roles: Senior 16,001, Lead 2,068, Staff 1,278, Middle 1,178, Junior 1,085, Intern 1,081, Principal 367. Month-over-month growth: Junior +297, Middle +252, Senior +1,518 (on a much larger base).
- **Correction recorded on 28 Oct:** the junior column was rebuilt against freehire's live page before reporting. The junior posting count is 1,085 (not 1,420), and java 39% (not 43%), api 47% (not 36%), kubernetes 11% (not 8%).

**Vietnam and inbox (28 Oct)**
- Posted ranges on live ITviec listings: Mid/Sr Java "up to $3,200", **Senior Backend "up to 50M"**. Titles kept clustering in **banking and fintech**: two bank backend roles and one fintech platform Java role in that window's sample.
- Inbox (17–28 Oct): about **40%** of 28 alerts were backend. Recurring backend titles: Principal Java/Kotlin Engineer, Intermediate/Senior Backend Engineer, Middle Java Developer, Senior Backend (Java, Fintech). One employer posted *both* an Intermediate and a Senior remote-Vietnam backend role (19 and 25 Oct), the first time the alerts showed one company hiring two backend levels remotely in one window.

**Cloud-listing pay (global remote, not a Vietnam rate)**
- [JobRemotely cloud analysis, 1 Oct 2026](https://jobremotely.io/blog/cloud-jobs-aws-azure-gcp): median yearly pay across listings naming a cloud: **AWS $175,450**, Azure $168,500, GCP $165,250. US-only: AWS $185,000 (n=35), Azure $193,050 (n=21), GCP $195,000 (n=21). Mostly US-tagged (566 of 687 listings).

### 28 Oct gap analysis: backend path vs the market

*Moved here in full from §9 of the 28 Oct report, which is now QA-only. Section references (§5, §6) point to this report's salary and interview sections.*

*A teammate is building Tuyen a junior-to-mid backend track in Java/Spring Boot. This section sets its three stages against what junior and mid Java backend postings actually ask for. Everything below comes from postings and public skill surveys read in this window. Where I had no count, I say "in the postings I read" rather than inventing a percentage.*

#### The path as briefed

| Stage | Timing | Content | Project |
|---|---|---|---|
| **1. Junior** | 0–6 months | Core Java (collections, exceptions, streams, basic concurrency); HTTP and REST design; SQL with PostgreSQL (joins, indexes, transactions); Spring Boot CRUD API with validation, error handling and tests; Git, Docker, running the app locally with a database | A small orders API |
| **2. Strong junior** | 6–12 months | Auth (sessions, JWT, OAuth basics); transactions done right (isolation levels, race conditions, API idempotency); Flyway migrations and Testcontainers integration tests; a CI pipeline and a first deploy to AWS | Payments on the orders API with retries and idempotency keys |
| **3. Mid-level** | 12–24 months | Caching with Redis; background jobs; messaging basics; observability (logs, metrics, tracing); performance basics (slow queries, connection pools, timeouts); simple system design and writing down decisions; owning a feature end to end | — |

#### What the postings ask for

Six real postings were read in full, plus four skill surveys that split by seniority. The postings span junior through mid:

- **Junior Java backend** ([junbrain, Oct 2026](https://junbrain.com/jobs/project/junior-java-developer-backend-role/ql1b6N9)): Java 11+, Spring/Spring Boot, PostgreSQL/MySQL and basic SQL, Git, OOP, Agile/Scrum, code reviews, debugging. Bonus: REST APIs, JUnit/Mockito, Maven/Gradle, Docker or cloud, GitHub portfolio.
- **Junior backend Java** ([Addeco](https://www.adecco.com/en-pl/job-offers/junior-backend-java-developer-warszawa-mazowieckie/jn-022026-963243)): Java 17+, Spring/Spring Boot/**Spring Security**, Maven, SQL databases, Git and GitHub including pipelines, unit testing, **Bash/Shell**, **Docker + Kubernetes + Helm**, PostgreSQL, English B2/C1, scrum. (Asks 2+ years despite the "Junior" title.)
- **Sber, Middle Java Backend, 2–4 years** ([hh.ru](https://hh.ru/vacancy/134545742)): Java 17+ core — collections, streams, concurrency basics; Spring Boot 3/Spring Cloud; REST/gRPC; **Kafka/NATS**; JUnit + **Testcontainers**; PostgreSQL indexes and **query plans**; **Redis** for caching, rate limiting and pub/sub; Docker; basic Kubernetes; CI/CD; **Prometheus/Grafana/ELK**; postmortems; basic performance tuning. AI tooling a plus.
- **Netomi, SDE II – Backend, 2–4 years** ([Built In](https://builtin.com/job/sde-ii-backend/10390296)): Java + Spring Boot, microservices, RDS MySQL/PostgreSQL, **Kafka or RabbitMQ**, **Redis/Memcached**, distributed systems, performance profiling, JUnit and integration tests, Docker/K8s/AWS ECS, CI/CD, third-party integrations, **end-to-end feature ownership**, collaboration with QA and DevOps.
- **Bees, Intermediate Java Developer** ([Greenhouse](https://job-boards.greenhouse.io/bees/jobs/8805778002)): Java, Spring Boot, REST, microservices, Azure DevOps, **observability (New Relic/Datadog), monitoring, logging, troubleshooting production issues**, agile, code reviews, CI/CD. Differentials: NoSQL, event-driven/messaging.
- **Neocode, Java FinTech, middle, 3–6 years** ([hirify](https://hirify.me/jobs/1218356-java-fintech-backend-developer)): Java 21+, Spring Boot 3/4, PostgreSQL, Redis, Kafka/RabbitMQ, **transactions, idempotency, distributed systems basics**, Docker, basic K8s, observability, Testcontainers, **BigDecimal for money, audit log, idempotency keys, secure webhooks, data masking, payment statuses, PCI DSS basics**, OAuth2/OIDC + Spring Security.
- **Métrica, Mid Backend – Java, Kafka, Spring Boot and AWS** ([remote, Spain](https://www.spainjobs.io/companies/metrica/desarrolladora-backend-mid-java-kafka-spring-boot-aws--22fcd61272)): Java 17+, Spring Boot 3.x Web/Data JPA, **Kafka in production (consumers, topics, partitions)** or RabbitMQ/SQS-SNS, **hexagonal architecture**, PostgreSQL/Oracle plus query optimisation, JUnit + Mockito, **GitHub Actions + SonarQube**, **OpenAPI/API-first**, SOLID/Clean Code. Nice-to-have: AWS in production (EKS, S3, CloudWatch), **outbox, idempotent consumer, retries + DLQ**, Redis, **Testcontainers and contract tests**, banking domain, English B1+.

Surveys used for the frequency numbers: [freehire junior backend](https://freehire.me/insights/roles/backend/junior) (1,085 postings, 937 with skills, 28 Oct 2026), [freehire middle backend](https://freehire.me/insights/roles/backend/middle) (1,178 postings, 28 Oct 2026), [Jobpedia junior software engineer](https://jobpedia.ai/roles/software-engineer/junior) (323 roles), [Skillenai Backend Engineer](https://skillenai.com/data/role/backend-engineer) (2,627 postings), and [Zorky's Java backend skill survey](https://zorky.tech/en/research/backend/java).

#### (a) What the path already covers

Each row is something real postings ask for **and** the path teaches.

| Path element | Where the market asks for it |
|---|---|
| Core Java: collections, exceptions, streams, basic concurrency | Sber lists exactly this for 2–4 years; Java is **39%** of junior backend postings ([freehire](https://freehire.me/insights/roles/backend/junior)) and 41% at middle |
| HTTP and REST design | api **47%** and rest **27%** of junior postings; api 65%, rest 39% at middle; Jobpedia REST 19% for junior SE, 21% for all SE |
| SQL + PostgreSQL: joins, indexes, transactions | sql **33%**, postgresql **18%** of junior postings; sql 27%, postgresql 25% at middle; Zorky puts SQL/PostgreSQL/indexes/transactions before Spring Boot in its roadmap |
| Spring Boot CRUD with validation, error handling, tests | spring **17%** of junior postings, **21%** at middle; all six postings read name Spring Boot, and four of them pin 3.x |
| Git | git **29%** junior, 27% middle; Addeco asks for Git and GitHub including pipelines |
| Docker and running locally with a database | docker **22%** junior, **33%** middle; Addeco and Sber both require Docker |
| Unit and integration tests | JUnit in Netomi, Sber and Métrica; Métrica pairs it with Mockito, Sber with Testcontainers |
| Flyway migrations | Postings ask for schema **migrations** generically; Zorky lists migrations in the database step. The tool name is rare — see (c) — but the capability is asked for |
| Testcontainers integration tests | Named outright by **Sber** (must-have), **Neocode** (must-have) and **Métrica** (nice-to-have). One of the path's strongest cards |
| CI pipeline | ci-cd **20%** junior, **37%** middle; Addeco (GitHub pipelines), Métrica (GitHub Actions + SonarQube) |
| First deploy to AWS | aws **18%** junior, **41%** middle; Jobpedia junior lists AWS as the top preferred cloud at 14%; ROLIVA and JobRemotely both put AWS first |
| Auth: sessions, JWT, OAuth basics | Addeco requires Spring Security; Neocode requires OAuth2/OIDC + Spring Security. The other four postings read here do not name auth at all, so it is a differentiator in the CV stack rather than a keyword most ads filter on |
| Transactions done right: isolation, races, API idempotency | Neocode: "transactions, idempotency"; Métrica: idempotent consumer as a nice-to-have. **The path's differentiator against every generic bootcamp** |
| Redis caching | redis **11%** junior, 14% middle; Sber (caching, rate limiting, pub/sub), Netomi (Redis/Memcached), Neocode |
| Messaging basics | kafka **21%** and event-driven architecture **21%** of middle postings, rabbitmq 9%; Skillenai backend Kafka 18.2%; Netomi "Kafka or RabbitMQ"; Métrica Kafka consumers/topics/partitions in production |
| Observability: logs, metrics, tracing | observability **15%** middle; Skillenai 16.5%; Bees (New Relic/Datadog, production troubleshooting), Sber (Prometheus/Grafana/ELK) |
| Performance basics: slow queries, pools, timeouts | Netomi performance profiling; Sber query plans and performance tuning |
| Simple system design and writing decisions | Netomi asks for end-to-end ownership at mid; ADRs are the architect bridge (see the 21 Oct architect-path notes above) |
| Owning a feature end to end | Netomi states it explicitly for SDE II |

**Verdict on coverage:** strong. Of the roughly 20 skills that keep reappearing across the six postings, the path covers about 17. Its two best cards are the ones most bootcamps skip: **idempotency and transactions** (Stage 2) and **Testcontainers** (Stage 2). Both are must-haves at middle level, and both are where Tuyen's QA background gives an unfair advantage.

#### (b) What the posts ask for that the path is missing

| Gap | Evidence | Where it should go |
|---|---|---|
| **JPA / Hibernate ORM, and the N+1 problem** | Zorky: Hibernate/JPA is standard, and "Spring Boot 3 + Spring Data JPA" appears in 95%+ of modern Java projects; Métrica names Spring Data JPA in the stack; the backend interview loop (§6) lists JPA N+1 as a standard topic | Stage 1, right after the first CRUD API — it is the first thing that goes wrong in a real repository |
| **Maven or Gradle** | Addeco "Maven"; junbrain "Maven/Gradle"; Zorky notes Maven is still ahead of Gradle in Java shops | Stage 1, day one — the build tool is how the project is created |
| **Mockito (unit-test isolation)** | Métrica "JUnit + Mockito"; Zorky "JUnit 5 + Mockito + Testcontainers"; junbrain lists JUnit/Mockito as the bonus | Stage 1, alongside the first tests |
| **Kubernetes basics** | freehire: **11% junior, 28% middle**; Jobpedia junior lists Kubernetes as a preferred skill at 10%; Zorky calls Docker + Kubernetes standard; Addeco requires Docker + Kubernetes + Helm | End of Stage 2 or start of Stage 3 — it is the biggest junior-to-middle jump in the dataset |
| **Microservices and service boundaries** | freehire: microservices 13% junior, **27% middle**; Skillenai: 16.2% of backend postings and **46.2% of Java Backend Developer postings**; Netomi, Bees and Métrica all list microservices | Stage 3 — messaging basics is the natural doorway |
| **OpenAPI / API-first design and contract tests** | Métrica: OpenAPI/API-first is a **required** skill; contract tests a nice-to-have | Stage 2, alongside the payments API |
| **Static analysis (SonarQube) and code-quality gates** | Métrica: GitHub Actions + SonarQube | Stage 2, as part of the CI pipeline |
| **Reading SQL query plans (EXPLAIN)** | Sber "query plans"; Métrica "query optimisation"; Jobpedia SE postings list SQL at 21% overall | Stage 3, inside "performance basics" — the path says "slow queries" but not "read the plan" |
| **gRPC** | Sber lists REST/gRPC together; the baseline called gRPC a mid-level nice-to-have | Optional Stage 3 lesson |
| **Bash / shell scripting** | Addeco; it is the practical glue for local Docker, migrations and CI | Stage 1, half a lesson |
| **English at a stated level** | Addeco B2/C1, Métrica B1+. English is the gate for the remote salaries in §5 | Not a lesson — a standing habit, noted so it is not discovered at interview time |
| **AI coding tools as a stated plus** | Sber lists AI tooling as a plus; freehire's broad "ai" keyword appears in **23%** of junior and **35%** of middle postings (broad keyword, treat as directional) | Fold into Stage 1 habits, not a separate lesson |
| **Fintech money rules: BigDecimal, audit log, webhook security, data masking, payment statuses, PCI DSS basics** | Neocode, a middle fintech posting, lists all of these; the baseline already flagged "proving correctness under failure" and payments domain depth as the senior differentiator | Stage 2, into the payments project — the path already builds payments, so this is a content upgrade, not a new stage |
| **NoSQL awareness** | freehire middle: nosql 14%, mysql 18%; a Vietnam bank backend listing in this window names Redis/MongoDB/MySQL/Oracle together | Stage 3, one comparison lesson |
| **Legacy context: Java EE / EJB, Oracle** | A Java EE (EJB) developer role appeared in this window's alerts; Zorky: Oracle still common in banks | Not for the path — but worth knowing why bank codebases look the way they do |

#### (c) What the path teaches that the posts rarely ask for

These are not wasted, but they should be taught as **depth for interviews and for the job after next**, not as things that get a junior CV past a screen. Every claim below is about the six postings and the surveys read in this window.

| Path element | Reality in the postings |
|---|---|
| **Flyway by name** | None of the six postings named Flyway. They say "migrations" (Zorky) or describe the database work generically. Teaching Flyway is right — it is the standard tool — but do not expect the word to match a keyword search |
| **Isolation levels by name** | No posting named an isolation level (READ COMMITTED, REPEATABLE READ, SERIALIZABLE). They say "transactions" (Neocode) and "idempotency". The theory is what lets Tuyen answer the interview question, not what gets the CV read |
| **Outbox and saga patterns** | Métrica lists outbox and idempotent consumer as **nice-to-have**, not required. No junior or mid posting read here required them. They matter at senior and in interviews (§6), which is how the path should frame them |
| **Kafka internals depth: consumer lag, rebalancing, exactly-once semantics** | The postings ask for "Kafka in production (consumers, topics, partitions)". None named consumer lag, rebalancing or EOS. Skillenai shows Kafka in 18.2% of backend postings, so it is a minority skill — a strong differentiator, not a baseline requirement |
| **Explicit system-design practice and written ADRs** | Netomi asks for end-to-end ownership; no posting read here asked for ADRs. The baseline put ADRs at architect level. Keep it as the later architect-track bridge, not a mid-level requirement |
| **Background jobs and schedulers as their own topic** | No posting in this window named them explicitly. They are usually implied by "messaging" or "async work" |
| **Caching strategy depth (eviction, stampede, write-through vs write-behind)** | Postings name **Redis** (13–14%) but none described a strategy. Teach the strategy in a lesson; do not build the path around it |
| **Deep concurrency beyond the basics** | Java concurrency appears at the level of "collections, streams, concurrency basics" (Sber). Advanced JVM and concurrency tuning is a senior ask per Zorky's roadmap |

#### What I would change in the path

1. **Add JPA/Hibernate and the N+1 problem to Stage 1.** The single biggest omission: it is universal in Java shops and a standard interview question.
2. **Name the build tool (Maven) and Mockito explicitly** in Stage 1. An hour each to teach, and both appear verbatim in junior postings.
3. **Move Kubernetes basics to the end of Stage 2**, not Stage 3. It is the sharpest junior-to-middle jump in the data (11% → 28%).
4. **Put the fintech money rules into the Stage 2 payments project.** BigDecimal, audit log, webhook security and idempotency keys turn the project from "a CRUD app with retries" into "a payments service", which is what the fintech postings screen for.
5. **Keep outbox, saga and Kafka internals, but label them "interview depth".** They are nice-to-haves in postings and required in senior interviews. That is a different kind of value, and saying so out loud stops Tuyen feeling behind when a junior posting does not mention them.


---

## Caveats

- **First report in the backend-engineer series.** Its "What changed" deltas compare against the backend sections of the 21 Oct baseline and the 28 Oct combined report. The 28 Oct → 30 Oct gap is **two days**, and Skillenai's comparison windows overlap by 62 days, so most 2-day moves are index refresh. Next week's report is the first true week-on-week backend comparison. Backend figures from the 21 Oct and 28 Oct reports that are not re-pulled here are kept in [Earlier data](#earlier-data-21-oct-and-28-oct), with their original sources.
- **Skillenai** measures posting mix, not hiring volume. Its all-role totals grow with index coverage; use the share changes. Its RabbitMQ page no longer shows a share change, so none is reported. "Go" may be inflated by the ambiguous word.
- **freehire** counts a skill anywhere in a posting (including nice-to-have), so its figures are a ceiling. Its total census fell 23,169 → 20,804 in two days, which suggests a cleanup of stale listings; use the per-level shares rather than the totals.
- **Fresh-postings sample (n=13) is small and search-biased.** Remote share is 100% by design. It is weighted to Europe and Latin America because that is where the search found dated junior/mid postings. Four links closed between reading and re-checking. Postings with no clear date in the window were excluded (for example, roles posted 5–11 Oct, and an undated generic junior listing). One listing with machine-generated text was excluded as unreliable.
- **ITviec counts** are a one-day snapshot (30 Oct 2026). The work-model and seniority reads cover only the first page of three tags (55 listings with overlaps), not the full tag.
- **Salaries:** ITviec figures are self-reported 2025 survey medians; Second Talent is a vendor rate card; Paymetric Labs does not publish its method. Only 3 of 13 sampled postings stated pay. VND→USD at ≈26,000 is approximate.
- **Interview topic lists** come from prep sites and a vendor survey (secondary), carried over from the baseline.
- **Inbox data** is alert titles only. No personal data, recruiter names or contacts are included. 19 alerts were read read-only (7 backend-relevant); no email was sent, drafted, labelled, archived or changed.
