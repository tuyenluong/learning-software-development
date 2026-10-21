import sys; sys.path.insert(0,'tools')
from topics import TOPICS
NAMES={"mq":"Message_Queues","kafka":"Kafka","tx":"Transactions_and_Concurrency","dist":"Idempotency_and_Distributed_Transactions",
"redis":"Redis","db":"Databases","sd":"System_Design","go":"Go","java":"Java_Spring","node":"NodeJS","ops":"DevOps",
"sec":"Security","ai":"AI_Tools","career":"Career"}
DESC={"mq":"Message queues and RabbitMQ: queues, exchanges, acks, TTL, DLQ, message ordering.",
"kafka":"Kafka and event streaming: partitions, consumer groups, share groups, offsets, acks, lag, CDC.",
"tx":"Transactions, isolation levels, locks, race conditions, deadlocks, stock deduction under concurrency.",
"dist":"Idempotency, consistency, retries, distributed transactions: saga, outbox, CDC.",
"redis":"Redis and caching: data types, Lua vs transactions, distributed locks, cache penetration/breakdown/avalanche, sentinel.",
"db":"MySQL / PostgreSQL / MongoDB / Elasticsearch: indexes, query tuning, partitioning, sharding, replication.",
"sd":"System design, architecture, DDD, microservices, scaling, interviews.",
"go":"Go (Golang): Gin, GORM/sqlc, goroutines, channels, context.",
"java":"Java and Spring Boot: Spring Data JPA, Spring Security, threads, virtual threads.",
"node":"Node.js / NestJS / JavaScript.","ops":"DevOps, cloud, monitoring and logging.",
"sec":"Security and auth: JWT, RBAC, OTP, API keys.","ai":"AI and developer tools.","career":"Career and soft skills."}
if __name__=="__main__":
  for k,_,_ in TOPICS:
    n=NAMES[k]
    open(f"indexes/{n}.md","w").write(f'''---
Creation_date: 2026-10-21 15:55
Modification_date: Wednesday 21st October 2026 15:55:00
Indexes:
  - "[[home]]"
  - "[[anonystick]]"
---


----
{DESC[k]}

```dataview
table Creation_date, Modification_date
from [[{n}]]  sort Creation_date DESC
```



---
## Flash cards section
''')
  open("indexes/anonystick.md","w").write('''---
Creation_date: 2026-10-21 15:55
Modification_date: Wednesday 21st October 2026 15:55:00
Indexes:
  - "[[literature_notes]]"
---


----
Literature notes from the Vietnamese backend YouTube channel [anonystick](https://www.youtube.com/@anonystick) (Tips Javascript / Tips Java). Full catalogue: [[video-list]]. Processing status: [[PROGRESS]].

Topic indexes: '''+" · ".join(f"[[{NAMES[k]}]]" for k,_,_ in TOPICS)+'''

```dataview
table Creation_date, Modification_date
from [[anonystick]]  sort Creation_date DESC
```



---
## Flash cards section
''')
