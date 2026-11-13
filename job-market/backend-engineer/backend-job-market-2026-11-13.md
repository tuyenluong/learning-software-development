# Backend Engineer Job Market 2026-11-13: Go · Spring Boot · Quarkus · Kafka · RabbitMQ

**Date:** 13 Nov 2026
**Purpose:** Backend-only market facts for Go, Spring Boot, Quarkus, Kafka and RabbitMQ roles, with extra attention to transaction and messaging skills.
**Coverage:** weekly **Backend Engineer** report. Job-alert window **7 – 13 Nov 2026** (the 6 Nov alerts were counted in the previous report, so there is no overlap this week); fresh postings sampled from **~8 – 13 Nov 2026**; index data as of **5 – 13 Nov 2026**.
**Builds on:** [backend-job-market-2026-11-06.md](backend-job-market-2026-11-06.md) (previous weekly report) and [backend-job-market-2026-10-30.md](backend-job-market-2026-10-30.md) (series baseline). Backend figures from the older combined reports remain in the baseline's [Earlier data](backend-job-market-2026-10-30.md#earlier-data-21-oct-and-28-oct).

> **How to read the numbers**
> - **Skillenai** = a job-posting index (90-day rolling windows; Backend Engineer page says "as of 13 Nov 2026"). It shows how often a skill shows up in postings, not total hiring. Skill pages refresh on different days (Kafka, Spring Boot and event-driven architecture 12 Nov; Go and microservices 13 Nov). The **RabbitMQ page was not refreshed** (still 90 days ending 5 Nov), so its figures are unchanged. The Backend Engineer page still does **not** publish an adjusted demand-share change ("comparable posting coverage is insufficient"), so the −9.0% figure from 30 Oct stays un-updated.
> - **freehire** = a posting aggregator that splits Backend by seniority (updated 13 Nov 2026). It counts a skill if it appears *anywhere* in a posting, including as a nice-to-have, so its percentages are a ceiling. When the number of postings that list skills changes, every percentage moves a little with it.
> - **ITviec counts** = live listing counts from itviec.com tag-page meta ("N Hot … jobs") on **13 Nov 2026**. Snapshot only. Work-model and seniority reads cover the first page of job cards on each tag, not the full tag.
> - **LinkedIn search snapshot** = the first page (25 cards each) of two read-only LinkedIn job searches on 13 Nov 2026, filtered to the past week ("remote backend engineer Java Spring Boot Kafka" and "remote Golang backend engineer Kafka"). LinkedIn localised both to Vietnam. Used only for the work-model split in §1D. **Small sample (47 unique cards).**
> - **Fresh-postings sample** = 11 public junior-to-senior backend postings dated roughly 8 – 13 Nov 2026, found by web search for remote Go / Spring Boot / Quarkus / Kafka / RabbitMQ roles (one from the LinkedIn snapshot). **This is a small, search-biased sample (n=11), not a census.** Every one is remote because the searches asked for remote, so it says nothing about the remote share of the market. Roles already sampled last week (re-listed under a new date) and postings older than ~8 Nov were excluded; one candidate page returned 404 and one showed the role as removed, so both are excluded.
> - Anything marked **(est.)** is an estimate or conversion made for this report. VND→USD uses about **26,000 VND/USD**, which is approximate.
> - **Job-alert sample** = aggregate counts from a sample of job-alert emails, mostly job titles. No personal data, recruiter names or contacts are included.

---

## Top skills at a glance (13 Nov 2026)

**Backend — learn these first**
1. **Java + Spring Boot** for Vietnam and fintech — Java **27.8%** of Backend Engineer postings, up from 27.7% ([Skillenai Backend](https://skillenai.com/data/role/backend-engineer)); Spring Boot **6,372** postings across all roles, demand share **+10.0%** ([Skillenai Spring Boot](https://skillenai.com/data/skill/spring-boot)); Java named in **7 of 11** sampled fresh postings (including two that accept it as an alternative) and Spring Boot in **3 of 11**.
2. **REST API design** — api **51%** of junior and **71%** of middle Backend postings, rest **35% / 46%** ([freehire junior](https://freehire.me/insights/roles/backend/junior), [freehire middle](https://freehire.me/insights/roles/backend/middle)); REST or RPC APIs named in **8 of 11** sampled postings.
3. **PostgreSQL + SQL** — PostgreSQL **23.9%** of Backend Engineer postings (was 23.5%); **6 of 11** sampled postings name PostgreSQL. Transactions remain the entry point to the messaging and consistency topics below.
4. **Kafka (with RabbitMQ as the second broker)** — Kafka **18.9%** of Backend Engineer postings and **25%** of middle postings; RabbitMQ **13%** of middle postings. In the fresh sample **8 of 11** name a message broker or queue: Kafka 6, RabbitMQ 1 (counting nice-to-haves and "SQS, RabbitMQ or ActiveMQ").
5. **Distributed systems / microservices + Kubernetes** — distributed systems **25.1%**, Kubernetes **31.2%**, microservices **18.3%** of Backend Engineer postings; microservices **39%** and Kubernetes **29%** of middle postings; Kubernetes named in **5 of 11** and microservices in **4 of 11** sampled postings.

*Python (35.2%), AWS (32.7%) and Go (27.9%) remain higher in the global Backend Engineer list, and Go has moved just above Java this week. They matter for the global remote market; the order above weights Vietnam and the Java/Spring stack.*

---

## What changed this week (6 Nov → 13 Nov 2026)

**Job-alert sample: 20 alerts.** A sample of 20 job-alert emails dated 7 – 13 Nov was counted. **9 were backend-relevant** (digests from a remote Java backend search, "jobs similar to Java Developer" digests and recommendation digests with backend titles). The other 11 were QA/test, industrial automation, freelance testing gigs, or unrelated. One Glassdoor digest was QA-titled but carried two Java cards (Java Fullstack, Java Developer with Mandarin) among mostly QA/BA titles and is counted with the non-backend majority, as last week. All were automated digests; none came from a named recruiter and none of the backend-relevant alerts stated a salary range.

**The five changes worth acting on**

| # | Change | 6 Nov | 13 Nov | Read |
|---|---|---|---|---|
| 1 | **Event-driven architecture accelerated for a fifth report running** | 3,309 postings, share **+34.8%** | **3,692**, share **+42.6%** | Still the fastest-rising backend signal. Messaging and consistency stay the right core. |
| 2 | **Kafka, Go and microservices shares stepped up; Spring Boot eased slightly** | Kafka 8,743 (+5.3%), Go 15,899 (+7.0%), microservices 12,172 (+8.7%), Spring Boot 6,030 (+10.8%) | **Kafka 9,517 (+7.4%)**, **Go 16,992 (+8.4%)**, **microservices 13,087 (+9.9%)**, Spring Boot 6,372 (**+10.0%**) | Kafka's share change moved for the first time in two weeks. Spring Boot is still the largest stack share gain, but its first slowdown in the series. |
| 3 | **More middle postings, asking harder for microservices and Kafka** | Middle 1,154 open; kafka 24%, microservices 35%, spring 27%, kubernetes 27%, event-driven 19% | **Middle 1,230 open; kafka 25%, microservices 39%, spring 28%, kubernetes 29%, event-driven 20%** | Middle is the only level whose open count rose. Junior fell **977 → 933**; junior Kafka **6% → 7%**. |
| 4 | **Remote titles in the job-alert sample doubled; first Go title** | 2 remote-Vietnam titles, 1 employer; Go 0 titles | **4 remote titles from 3 employers** (2 remote-Vietnam, 1 remote APAC, 1 remote-tagged in HCMC); **1 Go title** ("Backend Engineer (Go/Java)") | Backend-relevant share of alerts rose **37% → 45%**. Kafka, RabbitMQ and Quarkus still never appear in alert titles. |
| 5 | **Vietnam: Go and backend tags fell, Spring Boot and microservices rose; still 0 remote** | java 92, backend 83, spring boot 42, golang 31, microservices 29, kafka 18 | **90, 75, 45, 25, 35, 16** | First pages of kafka, golang and spring-boot tags show **0 remote** again (third report running). Go listings are the most senior-heavy (**0 junior** of 20). |

**Backend skill shares, 6 Nov → 13 Nov** (Skillenai, Backend Engineer; 2,801 → **2,926** postings; shares are of all postings in the window, so treat moves under 0.5 points as rounding):

| Skill | 6 Nov | 13 Nov | Skill | 6 Nov | 13 Nov |
|---|---|---|---|---|---|
| Python | 34.2% | **35.2%** | TypeScript | 18.8% | **19.3%** |
| AWS | 33.2% | **32.7%** | Kafka | 18.5% | 18.9% |
| Kubernetes | 30.8% | 31.2% | SQL | 17.5% | 17.9% |
| Java | 27.7% | 27.8% | Microservices | 17.1% | **18.3%** |
| Go | 27.1% | **27.9%** | Observability | 16.1% | 15.9% |
| Distributed systems | 25.5% | 25.1% | Redis | 15.2% | **15.9%** |
| PostgreSQL | 23.5% | 23.9% | Docker | 22.7% | 22.5% |
| CI/CD | 21.5% | **22.1%** | | | |

Over the week the biggest moves are **Microservices +1.2 points, Python +1.0, Go +0.8, Redis +0.7, CI/CD +0.6**. AWS slipped 0.5 points and distributed systems 0.4. Go (27.9%) now sits just above Java (27.8%).

**Messaging and stacks, all roles (Skillenai 90-day totals).** Totals grow partly because the index grows, so read the *share change*, not the raw count:

| Signal | 6 Nov | 13 Nov | Share change (latest page) |
|---|---|---|---|
| Kafka postings | 8,743 | **9,517** | **+7.4%** (was +5.3%) |
| RabbitMQ postings | 1,879 | 1,879 (page not refreshed, still 5 Nov) | not published |
| Event-driven architecture | 3,309 | **3,692** | **+42.6%** (was +34.8%) |
| Microservices | 12,172 | **13,087** | **+9.9%** (was +8.7%) |
| Go | 15,899 | **16,992** | **+8.4%** (was +7.0%) |
| Spring Boot | 6,030 | **6,372** | **+10.0%** (was +10.8%) |

**freehire Middle Backend, 6 Nov → 13 Nov** (1,086 → 1,154 postings listing skills): kafka 24% → **25%**, rabbitmq 13% → 13%, event-driven 19% → **20%**, microservices 35% → **39%**, spring 27% → **28%**, postgresql 28% → **30%**, kubernetes 27% → **29%**, ci-cd 41% → **40%**, observability 18% → **19%**, test-automation 14% → **11%**, redis 15% → 15%, distributed systems 16% → **17%**, api 72% → **71%**.

**ITviec Vietnam, 6 Nov → 13 Nov 2026** (live listing counts, same tag pages):

| Tag | 6 Nov | 13 Nov |
|---|---|---|
| java | 92 | **90** |
| backend developer | 83 | **75** |
| spring boot | 42 | **45** |
| golang | 31 | **25** |
| microservices | 29 | **35** |
| kafka | 18 | **16** |
| quarkus | 404 (≈0) | **404 (≈0)** |
| rabbitmq | 404 (no tag page) | **404 (no tag page)** |

([java](https://itviec.com/it-jobs/java), [backend developer](https://itviec.com/it-jobs/backend-developer), [spring-boot](https://itviec.com/it-jobs/spring-boot), [golang](https://itviec.com/it-jobs/golang), [microservices](https://itviec.com/it-jobs/microservices), [kafka](https://itviec.com/it-jobs/kafka))

**Job-alert sample (aggregate, 7 – 13 Nov):**
- **9 of 20 alerts (45%) were backend-relevant**, up from 37%. They carried **29 backend or backend-adjacent title cards, about 26 unique** (three titles repeated across digests).
- Titles (aggregate): Java Developer (Middle), Java Developer (JavaEE, Spring Boot), Java Developer (×2 employers), Java Developer (Junior/Middle), Java Developer (3+ years), Java Software Engineer (×3 employers), Software Engineer (Java), Backend Java Developer, Backend Engineer, Backend Engineer (Go/Java), Backend Software Engineer, Senior Backend Engineer I, Senior Backend Software Engineer II, Senior Java Engineer, Senior Java Developer, Senior Java/.NET/C Software Engineer (Japanese), Senior Full-stack Engineer (Java, AI-native), Intermediate Backend Engineer (Remote, Vietnam), Senior Backend Engineer (Remote, Vietnam), Senior Backend Engineer (TypeScript/Python/C#, Remote), Fullstack Engineer (APAC Remote), Backend Technical Lead (merchant lending), API Integration Engineer (OAuth2 / WSO2 / AWS).
- **Seniority in the ~26 unique titles:** 4 junior-to-middle or middle (Junior/Middle, Middle, Intermediate, "3+ years"), 8 senior, 1 lead, 13 unstated.
- **Remote:** 4 titles explicitly remote from 3 employers — the two remote-Vietnam titles from the same foreign employer flagged on 28 Oct, 30 Oct and 6 Nov, plus one remote APAC full-stack title and one remote-tagged senior backend title listed in HCMC. All other titles were Ho Chi Minh City listings without a remote flag.
- **Payments / finance / banking:** surety, consumer-lending and merchant-lending titles appeared again; banking and fintech remain the biggest local cluster.
- **Go appeared in an alert title for the first time in the series** (one "Go/Java" backend title). **Kafka, RabbitMQ and Quarkus: zero hits in alert titles**, as in every earlier report. Spring Boot appeared in title text once (was twice). Alerts are title digests; stack detail lives in the body.
- **No salary ranges were stated in any backend-relevant alert.**

---

## 0. Bottom line

1. **Event-driven architecture is still the fastest-rising backend skill.** Share change **+42.6%** (3,692 postings), up from +34.8% a week earlier. Kafka's share change rose to **+7.4%** (from +5.3%), Go to **+8.4%** and microservices to **+9.9%**; Spring Boot eased to **+10.0%** but is still the largest stack gain.
2. **Spring Boot remains the stack to lead with.** Java **27.8%** of Backend Engineer postings, Spring Boot share **+10.0%**, Java in **7 of 11** fresh postings, and **90 Java / 45 Spring Boot** listings in Vietnam against **25 Go** and **≈0 Quarkus**.
3. **Messaging stays a middle-level bar, and one posting spelled out the depth.** Kafka **7%** of junior → **25%** of middle; RabbitMQ **13%** of middle. **8 of 11** fresh postings name a broker or queue, and for the first time in the series one posting (senior) names the **transactional outbox, idempotency keys, deduplication and the limits of exactly-once** as requirements (0 of 12 last week).
4. **Vietnam is still office-first.** First-page job cards on kafka, golang and spring-boot show **0 remote** (kafka 14 office / 2 hybrid; golang 16 / 4; spring boot 15 / 5). Remote work for Vietnam-based engineers still comes from foreign employers and contractor platforms: **10 of 47** LinkedIn snapshot cards were remote, and 6 of those 10 came from two hourly-contract platforms.
5. **Pay: no new local survey.** No backend alert stated a salary. **6 of 11** fresh postings stated pay, all regional (Canada, US, Europe). ITviec and Second Talent figures are unchanged from the baseline.

---

## 1. Most-demanded skills, with frequency signals

### A. Global: Skillenai, "Backend Engineer" title, 2,926 postings, 90 days to 13 Nov 2026
([source](https://skillenai.com/data/role/backend-engineer))

| Skill | Postings | Share | Skill | Postings | Share |
|---|---|---|---|---|---|
| Python | 1,029 | 35.2% | TypeScript | 565 | 19.3% |
| AWS | 958 | 32.7% | **Kafka** | **553** | **18.9%** |
| Kubernetes | 914 | 31.2% | **Microservices** | **536** | **18.3%** |
| **Go** | **817** | **27.9%** | SQL | 523 | 17.9% |
| **Java** | **813** | **27.8%** | Redis | 465 | 15.9% |
| **Distributed systems** | **733** | **25.1%** | Observability | 464 | 15.9% |
| PostgreSQL | 698 | 23.9% | | | |
| Docker | 658 | 22.5% | | | |
| CI/CD | 648 | 22.1% | | | |

- **Demand share change:** still not published on the 13 Nov page (insufficient comparable coverage). The −9.0% figure from 30 Oct is therefore **not updated** this week.
- **Top posters:** GitLab 143, Grafana Labs 113, Wise 60, Stripe 55, CLERA 55, Vinted 48, ABOUT YOU 42, Verkada 32, Spotify 28. Remote-friendly product companies; the top two are unchanged.
- **Top metros:** Berlin 3.8%, New York City 3.0%, San Francisco 3.0%, London 2.7%, Tel Aviv 2.0%, Bengaluru 1.6%.
- **Career flows:** Backend Engineer hires come mainly from Software Engineer (104 moves in, 57 out). Unchanged.

### B. By seniority: freehire, open Backend postings, updated 13 Nov 2026

| Level | Open postings | Skill leaders |
|---|---|---|
| **Junior** | **933** (770 list skills) | api 51%, python 42%, **java 41%**, rest 35%, git 33%, sql 32%, ai 25%, docker 22%, cloud 21%, ci-cd 21%, aws 20%, nodejs 20%, postgresql 19%, mysql 18%, **spring 16%**, microservices 15%, redis 13%, kubernetes 10%, **kafka 7%**, llm 7% |
| **Middle** | **1,230** (1,154 list skills) | api 71%, rest 46%, java 45%, aws 42%, ci-cd 40%, **microservices 39%**, cloud 38%, docker 35%, sql 33%, git 31%, python 31%, ai 31%, postgresql 30%, **kubernetes 29%**, **spring 28%**, **kafka 25%**, **event-driven 20%**, mysql 20%, **observability 19%**, azure 19%, **distributed systems 17%**, redis 15%, unit-testing 14%, **rabbitmq 13%**, **test-automation 11%**, llm 10%, api-design 9%, oracle 9% |

([freehire junior](https://freehire.me/insights/roles/backend/junior), [freehire middle](https://freehire.me/insights/roles/backend/middle), [freehire seniority split](https://freehire.me/insights/roles/backend))

- **The junior-to-middle jump** (most useful for planning study): Kubernetes **10% → 29%**, microservices **15% → 39%**, CI/CD **21% → 40%**, AWS **20% → 42%**, Kafka **7% → 25%**, observability **not in junior top 40 → 19%**, RabbitMQ **not in junior top 40 → 13%**, Spring **16% → 28%**.
- **Seniority census, 13 Nov:** 27,264 open Backend roles — Senior 12,757, Lead 1,965, **Middle 1,230**, Intern 1,018, Staff 967, **Junior 933**, Principal 303, C-level 106. 30-day growth: Senior **−4,053**, Lead −401, Middle **−353**, Staff −326, Junior **−223**. Junior + Middle together are about **7.9%** of open roles (est.; was 7.6%). The census total fell from 28,012; prefer the per-level skill shares over the total.
- **New on the page this week:** median time a Backend posting stays open **30 days** (up from 22 days the 30 days before), **17,704** new postings published in the last 30 days, and **5.6** page views per open posting a month (up from 4.5). Slower closes and more views per posting both point to more competition per opening.

### C. Fresh postings sample: 11 remote backend postings, ~8 – 13 Nov 2026

*Small, search-biased sample (n=11). Use it for what employers write in junior/mid postings right now, not for market shares.*

| # | Role (employer) | Posted | Level | Where | Stack named | Pay stated |
|---|---|---|---|---|---|---|
| 1 | [Junior Software Developer, Backend (Hootsuite, via Jobright)](https://jobright.ai/jobs/info/69900da80f6f7e7a2cec5fc7) | ~9 Nov | Junior (1–2 yr) | Remote, Canada | Scala or **Go**, **Kafka** (produce/consume, troubleshooting), Docker, Kubernetes, AWS (EC2, SQS), microservices, Prometheus/Grafana, tests | **CA$68–95K/yr** |
| 2 | [Software Engineer I, Data Platforms (AI) (employer hidden, via Hirify)](https://hirify.me/jobs/1409415-software-engineer-data-platforms) | 13 Nov | Junior (1+ yr) | Remote, US only | Python or **Go**, **Kafka**, AWS, Spark, Databricks, PostgreSQL, testing | **$122.4–176K/yr** |
| 3 | [Software Engineer – Go (Software Mind, via Poland Dev Jobs)](https://poland-devjobs.com/jobs/software-mind-mex-software-engineer-go-aurl7bs) | 9 Nov | Mid (3+ yr, 2+ Go) | Remote, Poland | **Go**, **Kafka** producers/consumers, REST/gRPC, PostgreSQL, Redis, Docker, Kubernetes, GCP, Terraform, CI/CD, metrics/logs/dashboards, unit + integration tests | No |
| 4 | [Middle/Senior Go Backend Developer (hygh, via CafeRemote)](https://www.caferemote.com/jobs/hygh-middlesenior-golang-backend-developer-mwd) | 8 Nov | Mid/Senior | Remote, Germany | **Go** (fiber, bun, swaggo, mockery), PostgreSQL (migrations, query tuning), Redis, Docker, swarm/K8s, AWS, integration tests, BDD | No |
| 5 | [Intermediate Java Developer (SkyBridge / Paladin, via WFH Beacon)](https://wfhbeacon.up.railway.app/job/intermediate-java-developer-remote-1) | 12 Nov | Mid (3–5 yr) | Remote, US (8-month contract) | Java 17, **Spring Boot**, microservices, **Kafka** (design, tuning, troubleshooting), AWS (SQS, DynamoDB, EKS…), GitLab CI/CD, Jenkins, Gradle; Spark/Avro preferred | **$85–120K/yr** |
| 6 | [Backend Developer, Java / Spring Boot (Afternow, via Devgigs)](https://devgigs.com/jobs/backend-developer-java-spring-boot) | ~11 Nov | Mid (4+ yr) | Remote, Europe or LATAM | Java 21, **Spring Boot**, Hibernate/JPA, PostgreSQL, REST, microservices, automated tests, Git; plus: AWS, DDD / event-driven architecture, AI coding tools | **€3,000/mo** B2B (≈€36K/yr) |
| 7 | [Mid Java Developer, Quarkus (via Jobgether / SecretRemote)](https://secretremote.com/java-backend-developer-mid-3365389f-307f-40f2-8658-89fcda8df474) | 11 Nov | Mid | Remote, Brazil | Java, **Quarkus**, REST, SQL, microservices, Git, unit + integration tests; nice: JMS / WebSphere Message Broker, Jenkins CI/CD, SonarQube | No |
| 8 | Intermediate Backend Engineer (Remote, Vietnam) (Employment Hero, LinkedIn job 4488760656) | ~8 Nov | "Intermediate" (typically 5+ yr) | **Remote, Vietnam** | Ruby in-house (not required); one of Ruby / Python / Java / PHP / JS-TS; REST, databases, automated testing; AI coding agents as a daily habit | No |
| 9 | [Senior Backend Engineer, Java/Spring (CoreSync, via WFH Beacon)](https://wfhbeacon.up.railway.app/job/senior-backend-engineer-javaspring-remote-us-1) | 10 Nov | Senior | Remote, US | Java 25, **Spring Boot** 3+/4, Hibernate/JPA or jOOQ, MySQL or PostgreSQL, REST, AWS, **SQS / RabbitMQ / ActiveMQ**, containers, GitHub Actions, Terraform, AI coding tools | **$45–65K/yr** (as listed) |
| 10 | [Senior Backend Engineer, Core Team (Playson, via Jobicy)](https://jobicy.com/jobs/152752-senior-backend-engineer-core-team) | 9 Nov | Senior | Remote, Europe / Ukraine | Node.js/TS (Java, Go and others accepted), **Kafka** (rebalances, offset commits under retries, limits of exactly-once), **transactional outbox, idempotency keys, deduplication**, gRPC, MySQL/PostgreSQL, Redis/NoSQL, Kubernetes, AWS/GCP | No (undisclosed) |
| 11 | [Junior Software Developer, Content Integration & Data Pipelines (Agility PR Solutions, via taskenzo)](https://taskenzo.space/remote-jobs/junior-software-developer-content-integration-data-pipelines) | 10 Nov | Junior (entry) | Remote, Canada | Java, REST, **Kafka** (event-driven services), TypeScript / Nest.js, SQL, Git, Maven, Linux, Solr, testing | **CA$65–75K/yr** |

**Counts across the 11 (mentioned anywhere, including nice-to-have and "accepted alternative" languages):**

| Skill | Count | Skill | Count |
|---|---|---|---|
| REST / API (incl. gRPC) | 8 | Java | 7 |
| **Any message broker or queue** | **8** | AWS | 7 |
| Tests named (unit/integration/automated) | 8 | **Kafka** | **6** |
| PostgreSQL | 6 | **Go** | **5** |
| AI tools mentioned | 6 | Kubernetes | 5 |
| Microservices | 4 | Docker / containers | 4 |
| CI/CD | 4 | **Spring Boot** | **3** |
| Redis | 3 | Observability tools | 2 |
| **RabbitMQ** | **1** | **Quarkus** | **1** |
| **Outbox / idempotency named** | **1** | | |

- **Seniority:** Junior 3, Mid 5 (including one "Intermediate" at 5+ years), Mid/Senior 1, Senior 2. The junior count is unchanged (3 of 11 vs 3 of 12).
- **Remote:** 11 of 11 by search design. All but one were tied to one country or region (Canada 2, US 3, Poland, Germany, Brazil, Europe/LATAM, Europe/Ukraine). **1 of 11** was explicitly open to Vietnam-based engineers (#8; last week 0 of 12).
- **Salary stated: 6 of 11** — CA$68–95K and CA$65–75K (Canada juniors), $122.4–176K (US junior, data platform), $85–120K (US mid contract), $45–65K (US senior, as listed), €3,000/mo B2B (Europe/LATAM mid). Too few and too region-specific to summarise into one band.
- **Go was easier to find this week, Quarkus harder.** Go named in 5 of 11 (was 2 of 12); Quarkus in 1 of 11 (was 5 of 12). Both follow what the searches surfaced inside the window, not a market shift.
- **Brokers are still "either/or" on many Java roles** (#9 accepts SQS, RabbitMQ or ActiveMQ; #7 lists JMS as a nice-to-have). The Go and data-platform roles (#1–#3) named Kafka specifically.

### D. Vietnam: ITviec live counts and first-page read, 13 Nov 2026

- Counts: "java" **90**, "backend developer" **75**, "spring boot" **45**, "golang" **25**, "microservices" **35**, "kafka" **16**, "quarkus" and "rabbitmq" no tag page (404, ≈0).
- **Work model on the first page of job cards:** kafka 16 → **14 at office, 2 hybrid, 0 remote**; golang first 20 → **16 office, 4 hybrid, 0 remote**; spring boot first 20 → **15 office, 5 hybrid, 0 remote**.
- **Seniority in slugs/titles, first page:** golang 20 → **9 senior or above**, 5 middle-to-senior ranges, 1 junior-to-senior range, 5 unstated, **0 junior-only**. Spring boot 20 → **12 senior or above**, 4 middle or middle-to-senior, 4 unstated, **0 junior**. Kafka 16 → **7 senior or above**, 2 middle-to-senior, 1 junior-to-senior range, 1 all-level, 5 unstated. (This week "middle–senior" ranges are counted separately from senior; last week's split was less strict, so compare directions, not exact numbers.)
- **Kafka-tagged titles remain Java-heavy** (Spring Boot / Java backend roles at securities firms and banks dominate the first page; several also name Go).
- **LinkedIn search snapshot (47 unique cards, past week, localised to Vietnam):** **10 remote**, 6 hybrid, 25 on-site, 6 unstated. Of the 10 remote cards, **6 came from two hourly-contract platforms** ($20–100/hr and $50–100/hr), 2 from the foreign employer already seen in the job-alert sample, 1 from Canonical (senior/staff/principal) and 1 from a Python data/AI role. No card from a Vietnam-based employer was marked remote.
- No posted USD band was extracted from first-page titles this snapshot.

---

## 2. Must-have vs nice-to-have vs differentiator (junior → mid → senior)

*Synthesis from the frequencies above, the 11 fresh postings and the interview sources in §6.*

| Level | Must-have | Nice-to-have | Differentiator |
|---|---|---|---|
| **Junior** | Java + Spring Boot (or Go); REST; SQL + PostgreSQL; Git; unit tests (JUnit/Mockito); Docker basics | A message queue "even from study" — **Kafka named in all three junior postings this week**; Redis; one cloud; AI coding tools as a stated habit | A small service that **dedupes events and retries with backoff**, tested |
| **Mid** | Java 17/21 + Spring Boot 3 **or** Go; REST (OpenAPI); PostgreSQL (indexes, transactions); Docker; unit + integration tests; CI/CD; **Kafka or RabbitMQ producer/consumer in production**; microservices | Kubernetes; Redis; observability (Grafana/Prometheus/ELK); gRPC; Terraform; hexagonal architecture; Oracle (banks); Quarkus as an accepted alternative to Spring | Testing services under failure; fintech domain basics |
| **Senior** | Distributed systems: messaging, retries, timeouts, **idempotent at-least-once handlers, transactional outbox, offset-commit strategy under rebalances, the limits of exactly-once**, saga, consistency trade-offs; observability; performance and concurrency; system design; on-call | Event sourcing/CQRS; Kafka Streams/Connect/Debezium; K8s operations; OAuth2/OIDC; multi-region failover | Proving correctness under failure; payments depth; ADRs and design docs |

*Change from 6 Nov: the senior must-have row now quotes the outbox / idempotency / exactly-once wording that a senior posting (#10) used verbatim, the first time the series has seen these as written requirements. Junior row notes that all three junior postings named Kafka (as required or as "exposure"). The mid row is unchanged.*

---

## 3. Messaging, transactions and distributed systems: how often, and how tested

### Frequency signals

| Signal | Number | Source |
|---|---|---|
| Kafka postings (all roles, 90d) | **9,517** (share **+7.4%** vs prior 4 weeks) | [Skillenai Kafka](https://skillenai.com/data/skill/kafka) |
| RabbitMQ postings (90d) | **1,879** (page not refreshed since 5 Nov) → Kafka is about **5.1×** RabbitMQ (est.; was 4.7× on 6 Nov, but the RabbitMQ side is a week older) | [Skillenai RabbitMQ](https://skillenai.com/data/skill/rabbitmq) |
| Event-driven architecture postings (90d) | **3,692** (share **+42.6%**) | [Skillenai EDA](https://skillenai.com/data/skill/event-driven-architecture) |
| Microservices postings (90d) | **13,087** (share +9.9%) | [Skillenai microservices](https://skillenai.com/data/skill/microservices) |
| Share of Backend Engineer postings | Distributed systems 25.1%, Kafka 18.9%, microservices 18.3%, observability 15.9%, Redis 15.9% | [Skillenai Backend](https://skillenai.com/data/role/backend-engineer) |
| Share of **Middle** Backend postings | **Kafka 25%**, event-driven 20%, observability 19%, distributed systems 17%, **RabbitMQ 13%** | [freehire middle](https://freehire.me/insights/roles/backend/middle) |
| Share of **Junior** Backend postings | **Kafka 7%**; RabbitMQ not in top 40; microservices 15%, redis 13% | [freehire junior](https://freehire.me/insights/roles/backend/junior) |
| Top role for each broker | Software Engineer: 40.5% of Kafka postings, 44.2% of RabbitMQ postings; Backend Engineer 5.7% of Kafka postings (542) | Skillenai Kafka / RabbitMQ |
| Roles most likely to require Kafka | CloudOps Engineer 42.9%, Distributed Systems Engineer 36.2%, Integrations Engineer 33.3%; Back-end Developer 25.6%, Java Backend Developer 25.0% | [Skillenai Kafka](https://skillenai.com/data/skill/kafka) |
| Top Kafka employers | **Wise 202**, Cisco 171, CrowdStrike 121, **Mastercard 119**, **Barclays 88**, Capital One 78, **JPMorgan 66**, Databricks 64 | [Skillenai Kafka](https://skillenai.com/data/skill/kafka) |
| Top EDA employers | **Mastercard 72, Wise 72, Barclays 37**, Bright Vision 30, CLERA 29, EPAM 27, State Street 23, Fiserv 19 | [Skillenai EDA](https://skillenai.com/data/skill/event-driven-architecture) |
| Top RabbitMQ employers (5 Nov page) | CLERA 26, Wrike 23, Bright Vision 18, Klaviyo 18, Wise 18, Cisco 18 | [Skillenai RabbitMQ](https://skillenai.com/data/skill/rabbitmq) |
| Fresh sample (n=11) | Broker or queue named in **8**: Kafka 6, RabbitMQ 1; outbox / idempotency keys / exactly-once limits named in **1** (senior) | §1C |
| Vietnam | ITviec "kafka" **16**, "microservices" **35** (vs "java" 90); no RabbitMQ tag | ITviec, 13 Nov 2026 |

**Read (interpretation):**
- **Kafka is still the broker to lead with**; banks and payments companies still dominate its top employers (Wise moved ahead of Cisco this week), which matches Vietnam's fintech-heavy backend titles.
- **Event-driven architecture keeps accelerating while Backend Engineer demand-share stays unpublished.** Fintech and banking employers lead EDA postings, so failure-handling in event flows is still the relevant depth.
- **RabbitMQ still deserves a full lesson.** All-roles Kafka ≈ **5×** RabbitMQ, but middle postings hold RabbitMQ at **13%**, and Java roles keep writing "SQS, RabbitMQ or ActiveMQ" or "Kafka or RabbitMQ".
- **The transaction-and-messaging vocabulary is now written into postings.** One senior posting (#10) asks for reasoning about rebalances and in-flight work, offset commits under retries and duplicates, "the limits of exactly-once", and idempotent handlers built with an outbox, idempotency keys and deduplication. The new [Kafka exactly-once note](../../learning-material/backend-engineering/messaging-and-transactions/Kafka%20exactly-once%20and%20its%20limits.md) covers that last point.

### How it's tested in interviews
*Unchanged from the baseline; no new interview-format survey this window. Sources are prep sites and vendor surveys (secondary). One posting (#10) this week published its loop: HR interview (30–45 min), hiring manager (45 min), **technical interview with live coding (90 min)**, final C-level interview (60 min).*

1. **System design round** (38% of technical tests per [CoderPad 2026](https://coderpad.io/survey-reports/coderpad-state-of-tech-hiring-2026/)): checkout, payment, wallet transfer, notifications. Expected: local transactions, **no 2PC**, **transactional outbox**, **saga** with compensations, **retries with backoff and timeouts**, **idempotent consumers**, **DLQ**.
2. **Kafka deep-dive:** partitions and ordering; consumer groups and rebalancing; offset commits; idempotent producer and transactions; why exactly-once covers Kafka-to-Kafka only; consumer lag.
3. **Database and concurrency:** isolation levels and anomalies; optimistic vs pessimistic locking; "two requests withdraw from the same account"; idempotency keys on POST.
4. **Debugging scenarios:** "users get charged twice", "consumer lag grows after a deploy", "messages land in the DLQ after a schema change".

---

## 4. Go vs Spring Boot vs Quarkus

| Signal | Go | Spring Boot | Quarkus |
|---|---|---|---|
| Global postings, 90d (Skillenai, latest) | **16,992** (share +8.4%) ¹ | **6,372** (share **+10.0%**) | no Skillenai page (404) |
| Share of Backend Engineer postings | **27.9%** | (Java 27.8%) | n/a |
| Top employers | Capital One 813, Cisco 559, **Stripe 205**, Anduril 196, SpaceX 182, CrowdStrike 175, Palo Alto Networks 175, NVIDIA 170, **Grab 168** | **Mastercard 331**, Wise 151, **Barclays 119**, JPMorgan 69, Cisco 68, Capco 63 | (sample: one mid role in Brazil) |
| Fresh sample (n=11) | **5** (all name Kafka except #4) | **3** | **1** — remote Brazil, mid |
| freehire junior / middle | go not in junior or middle top 40 | spring 16% junior / 28% middle | not in either top 40 |
| Vietnam ITviec (13 Nov) | **25** (was 31) | **45** (was 42; Java 90) | **≈0** (404) |
| Vietnam first-page seniority | 9 of 20 senior+, 6 ranges, **0 junior-only** | 12 of 20 senior+, 4 middle/range, 0 junior | n/a |

¹ "Go" is an ambiguous word; treat Skillenai's count as an upper bound.

Sources: [Skillenai Go](https://skillenai.com/data/skill/go), [Skillenai Spring Boot](https://skillenai.com/data/skill/spring-boot), [ITviec golang](https://itviec.com/it-jobs/golang), [ITviec spring-boot](https://itviec.com/it-jobs/spring-boot). SO 2026 and Java-org survey figures remain in the baseline [Earlier data](backend-job-market-2026-10-30.md#earlier-data-21-oct-and-28-oct) and were not re-pulled.

**Verdict (unchanged direction):**
- **Spring Boot is the primary stack.** Still the largest share gain among the three, leads in Vietnam (Spring Boot listings up 42 → 45) and in banks/fintech, and Java titles dominated the backend-relevant alerts.
- **Go is the second language for remote and global product companies.** Go moved just above Java in the global Backend Engineer list (27.9% vs 27.8%) and its share change rose to +8.4%, while Vietnam Go listings fell 31 → 25 and stayed senior-heavy. Two junior remote postings this week (#1, #2) accept Go with Kafka, both in North America.
- **Quarkus: concepts only.** ≈0 in Vietnam and 1 of 11 in this week's remote sample (5 of 12 last week was a search artefact of Europe-weighted results). One or two comparison lessons remain enough; most Spring knowledge carries over.

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
| Fresh sample (n=6 with pay) | Canada juniors **CA$65–75K** and **CA$68–95K/yr**; US junior data platform **$122.4–176K/yr**; US mid contract **$85–120K/yr**; US senior **$45–65K/yr** (as listed); Europe/LATAM mid **€3,000/mo** B2B | Single postings; regional; none open to Vietnam |
| LinkedIn snapshot, Vietnam remote cards | Two hourly-contract platforms: **$20–100/hr** and **$50–100/hr** | Platform ranges, not salaries; wide by design |
| Global reference ([SO 2026 comp](https://survey.stackoverflow.co/2026/work/data/compensation)) | Back-end median **$85,296/yr**; architect **$102,355/yr** | Mostly US/EU respondents; baseline figure |

**Read (est.):** a mid-level remote backend engineer in Vietnam still lands around **$2,500–4,300/mo** on contractor rates, and a senior around **$4,300–5,600/mo**. Both are roughly **2–3×** the local ITviec medians for 3–8 years. English is still the gate (fluent English / B2+ named in #3; professional English in #6).

---

## 6. Typical interview formats and common topics

*Unchanged from the baseline; not re-surveyed this window.*

- **Market-wide (CoderPad 2026, ~650 respondents):** algorithmic 43%, real-world scenarios 38%, system design 38%, pair programming 30%, code review 21%, debugging 19%. 46% of companies allow AI in interviews in some form; the skill signals are catching AI mistakes (66%) and explaining trade-offs (56%).
- **Backend loop (mid/senior):** recruiter → coding (DSA or a practical service task) → **system design** (seniors often get 2 rounds) → **deep-dive** (Spring internals or Go concurrency, DB and transactions, Kafka) → behavioural.
  - **Spring:** DI and bean lifecycle; `@Transactional` propagation and pitfalls; **JPA N+1**; connection pools; virtual threads.
  - **Go:** goroutines, channels, `context` cancellation, races (`-race`), worker pools.
  - **Messaging:** see §3.
- **Signals in this week's postings:** a senior posting publishes a four-step loop with a **90-minute live-coding** round (§3); a remote-Vietnam posting states that AI tools may screen applications and that candidate identity and location are verified; several postings (#3, #6, #10) name AI coding agents as part of daily work, and one (#6) names Spanish as a strong plus for a Europe/LATAM role.
- **Vietnam specifics (est.):** outsourcing firms run a shorter loop (tech interview, English check). Foreign in-house and remote employers add system design.

---

## 7. Trends

**Event-driven architecture is the fastest-rising backend skill**
- Share change **+42.6%** (3,692 postings), up from +34.8% a week earlier and +23.9% on 30 Oct. Mastercard and Wise tie at the top (72 each), then Barclays.
- **Implication:** a messaging-focused skill set is aligned with where demand is moving.

**Backend open roles: senior pool still shrinking fastest; middle is the only level that grew week on week**
- freehire Senior **−4,053** over 30 days; Junior −223, Middle −353. Week on week, Middle open postings rose 1,154 → 1,230 while Junior fell 977 → 933. Median time-to-close rose to 30 days (from 22).
- **Implication:** proof (a deployed service, tests, one broker) still matters more than a keyword list.

**Spring Boot is still gaining fastest of the three stacks, but Go is closing in**
- Spring Boot share **+10.0%** (was +10.8%) vs Go **+8.4%** (was +7.0%); Go overtook Java by 0.1 point in the Backend Engineer list. Quarkus remains ≈0 in Vietnam.

**AI in backend postings is broad but shallow**
- freehire "ai": **25%** junior, **31%** middle; "llm" 10% of middle. Fresh sample **6 of 11** mention AI tooling (was 3 of 12). Broad keyword, treat as directional.

**Vietnam stays office-first and senior-heavy**
- 0 remote and 0 junior-only titles on the first pages of the golang and spring-boot tags (§1D). Go listings fell 31 → 25. Remote options still come from foreign employers and hourly-contract platforms.

---

## 8. Recommended skill priority list (junior → mid backend)

*Time estimates assume about 6–8 hrs/week of study and are estimates. Order follows the baseline backend phases; changes from this week's data are marked **new**.*

### Stage 1: Junior foundations (months 0–6)
1. **Java 21 + Spring Boot 3:** REST with OpenAPI, validation, error handling, JPA/Hibernate (including **N+1**). *(Java 41% of junior postings; Java in 7 of 11 fresh postings.)*
2. **SQL + PostgreSQL transactions:** joins, indexes, isolation levels, lost update. *(PostgreSQL 23.9% of Backend Engineer postings; 6 of 11 fresh postings.)*
3. **Testing:** JUnit 5 + Mockito, then Testcontainers integration tests. *(Tests named in 8 of 11; unit-testing 14% of middle postings.)*
4. **Git, Maven, Docker, a CI pipeline (GitHub Actions).** *(CI/CD 21% junior → 40% middle.)*

### Stage 2: Strong junior (months 6–12)
5. **Idempotent consumer + retries with backoff, on RabbitMQ first.** Build a notifications consumer that dedupes by event id, retries with growing backoff, and records history in PostgreSQL. *(Still the clearest junior→middle bridge; RabbitMQ 13% of middle postings.)*
6. **Payments on the orders API with idempotency keys**, plus a first AWS deploy. *(AWS 20% junior → 42% middle.)*
7. **Auth (JWT/OAuth2 basics).**
8. **Treat AI coding tools as a habit, not a lesson.** *(Named in 6 of 11 fresh postings this week.)*

### Stage 3: Mid-level (months 12–24)
9. **Kafka with Spring for Apache Kafka:** keys and partitions, consumer groups, offset commits, retries/DLT, consumer lag. *(Kafka 25% of middle postings; 6 of 11 fresh postings, including all three junior ones.)*
10. **Reliability patterns:** transactional outbox, saga with compensations, timeouts and circuit breakers. **new — add "what exactly-once does and does not cover"** (Kafka transactions, `read_committed`, why a database write still needs an idempotent consumer or outbox). *(Named as a written requirement in a senior posting this week.)*
11. **Kubernetes basics + observability** (structured logs, Prometheus/Grafana, OTel traces across async hops). *(Kubernetes 10% → 29%, observability → 19% from junior to middle.)*
12. **Redis caching.** *(Redis 15.9% of Backend Engineer postings.)*
13. **Hexagonal architecture** as the structure for the payments/orders service.

### Later: Go and architect track
14. **Go** as the second language, porting one service with a Kafka consumer. *(Go 27.9% of Backend Engineer postings; Go + Kafka in 3 of this week's remote postings, two of them junior.)*
15. **Quarkus**, 1–2 comparison lessons. **System design** practice (payments, wallet, notifications), ADRs.

---

## 9. Backend path vs the market

*Checked against this week's 11 fresh postings and freehire junior/middle data. The full 28 Oct gap analysis remains in the baseline [Earlier data](backend-job-market-2026-10-30.md#28-oct-gap-analysis-backend-path-vs-the-market); this section only records what this week's data adds or confirms.*

| Path element | This week's evidence | Verdict |
|---|---|---|
| Spring Boot CRUD + PostgreSQL + tests (Stage 1) | Java 7/11, PostgreSQL 6/11, tests 8/11; Afternow mid asks for Java 21 + Spring Boot + JPA + PostgreSQL + REST | **Covered, keep** |
| API idempotency and retries (Stage 2) | One posting names idempotency keys and deduplication outright | **Covered; keep messaging version in Stage 2** |
| Messaging basics (Stage 3) | Brokers or queues in 8/11; Kafka 7% junior → 25% middle; RabbitMQ 13% middle; Kafka in all 3 junior postings | **Covered; teach RabbitMQ first, then Kafka** |
| Observability (Stage 3) | 2/11 name observability tools; 19% of middle postings | **Covered, keep** |
| Kubernetes | 5/11; 10% junior → 29% middle | **Gap from 28 Oct still stands: move basics to end of Stage 2** |
| Quarkus awareness | 1/11 this week (5/12 last week) | **Keep as 1–2 comparison lessons, not a primary stack** |
| Outbox / saga / exactly-once limits | Named in **1** of 11 postings (senior) as a written requirement; 0 of 12 last week | **Still interview depth for juniors and mids; now a written senior requirement. Exactly-once limits added to Stage 3.** |

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
12. **new — Spring for Apache Kafka, exactly-once semantics and transactions**: https://docs.spring.io/spring-kafka/reference/kafka/exactly-once.html · https://docs.spring.io/spring-kafka/reference/kafka/transactions.html

Optional extras: [A Tour of Go](https://go.dev/tour/) · [Quarkus Kafka guide](https://quarkus.io/guides/kafka) · [System Design Primer](https://github.com/donnemartin/system-design-primer)

*(Link check, 13 Nov 2026: Skillenai Backend / Spring Boot / Kafka / RabbitMQ / Go / EDA / microservices, freehire junior/middle/backend, ITviec java / backend-developer / spring-boot / golang / microservices / kafka, Spring Kafka exactly-once and transactions, and Second Talent pages returned HTTP 200. ITviec quarkus and rabbitmq tag pages and the Skillenai quarkus page returned 404. Of the 10 linked posting URLs, 9 returned 200; the taskenzo page (#11) returned 403 to a scripted check but loaded in a normal fetch the same day. #8 is cited by LinkedIn job id only. One candidate posting page returned 404 and one aggregator showed its role as removed; both were excluded from the sample.)*

---

## Caveats

- **Third weekly report in the backend-engineer series.** "What changed" compares against the 6 Nov report (a full week). Skillenai skill pages refresh on different days inside the window (the RabbitMQ page not at all this week), and comparison windows still overlap by ~62 days, so share changes are posting-mix signals, not a clean week of new hiring.
- **Skillenai** measures posting mix, not hiring volume. Its Backend Engineer demand-share change is unpublished again. "Go" may be inflated by the ambiguous word, which matters now that Go and Java differ by 0.1 point.
- **freehire** counts a skill anywhere in a posting (including nice-to-have), so its figures are a ceiling. Its total Backend census fell 28,012 → 27,264 while every level's 30-day growth is negative; prefer per-level shares.
- **Fresh-postings sample (n=11) is small and search-biased.** Remote share is 100% by design. Weighted to North America and Poland this week because that is where dated junior/mid Go and Kafka postings were easiest to find; last week's sample was Europe/Quarkus-weighted. Swings in Go (2 → 5) and Quarkus (5 → 1) counts reflect that, not the market. Several postings were read through aggregators (Jobright, Hirify, WFH Beacon, Devgigs, CafeRemote, Jobicy, taskenzo, SecretRemote), and "posted" dates come from those pages.
- **LinkedIn snapshot** is two first pages (47 unique cards), localised to Vietnam by LinkedIn, and ranked by LinkedIn's relevance, so it is not a random sample.
- **ITviec counts** are a one-day snapshot (13 Nov 2026) from tag-page meta text. Work-model and seniority reads cover first-page job cards only, and the seniority split is stricter than last week's.
- **Salaries:** ITviec figures are self-reported 2025 survey medians; Second Talent is a vendor rate card; Paymetric Labs does not publish its method. Only 6 of 11 sampled postings stated pay, none open to Vietnam. VND→USD at ≈26,000 is approximate.
- **Interview topic lists** come from prep sites and a vendor survey (secondary), carried over from the baseline.
- **Job-alert data** is alert titles only, from a sample of 20 alerts (9 backend-relevant). No personal data, recruiter names or contacts are included.
