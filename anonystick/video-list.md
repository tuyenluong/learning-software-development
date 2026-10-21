# anonystick YouTube channel: full video list, grouped by topic

Source: https://www.youtube.com/@anonystick (Vietnamese backend/dev channel, credit: anonystick / Tips Javascript). Pulled 2026-10-21 with `yt-dlp --flat-playlist`.

**Total videos on the /videos tab: 786.** Grouped into 14 topic areas below, in the suggested learning order (foundations first). Each video is in exactly one group (first matching topic wins), so a few cross-topic videos sit in an earlier group.

Notes on the data:
- Titles are as YouTube returned them; YouTube auto-translates some titles into English, others stay Vietnamese.
- Upload month is approximate (YouTube only shows "x months/years ago").
- Views `?` = YouTube hid the count. Almost all of these are **members-only** videos (channel membership required): subtitles for those can't be fetched without signing in, which we don't do.
- Playlists: [WeekDaily - Con đường Lập Trình Viên](https://www.youtube.com/playlist?list=PLw0w5s5b9NK5xdGY8OyU9OrUl8Zkb7k3M), [Git vs GitHub](https://www.youtube.com/playlist?list=PLw0w5s5b9NK7dTWqY1li4u4_dZMNeSjQv). The channel also has YouTube "Courses", which yt-dlp can't list yet.
- Processing status per video: see [PROGRESS.md](PROGRESS.md).

## Topic areas

- [1. Message queues & RabbitMQ (foundations)](#mq) (35 videos)
- [2. Kafka & event streaming](#kafka) (22 videos)
- [3. Transactions, isolation, locks & DB concurrency](#tx) (51 videos)
- [4. Idempotency, consistency & distributed transactions (saga/outbox)](#dist) (19 videos)
- [5. Redis & caching](#redis) (47 videos)
- [6. MySQL / PostgreSQL / MongoDB / Elasticsearch](#db) (112 videos)
- [7. System design, architecture & interviews](#sd) (96 videos)
- [8. Go (Golang)](#go) (59 videos)
- [9. Java & Spring Boot](#java) (42 videos)
- [10. Node.js / NestJS / JavaScript](#node) (142 videos)
- [11. DevOps, cloud, monitoring & logging](#ops) (12 videos)
- [12. Security & auth](#sec) (12 videos)
- [13. AI & tools](#ai) (23 videos)
- [14. Career, soft skills & other (NoCODE)](#career) (114 videos)

<a id="mq"></a>
## 1. Message queues & RabbitMQ (foundations)

| # | Upload (approx.) | Title | Duration | Views | Link |
|---|---|---|---|---|---|
| 12 | 2026-08 | Simple Queue Service (SQS) FOR BACKEND: AWS Cloud Computing Tutorial | 15:25 | 1300 | https://www.youtube.com/watch?v=Ccbx5ItsSSQ |
| 13 | 2026-07 | Showcasing How Large Companies Send Millions of Emails \| AWS SQS, Lambda & SES | 16:14 | 3600 | https://www.youtube.com/watch?v=HnQ0Wt6YyO0 |
| 27 | 2026-05 | JAVA DDD Source Code: Place Order With MQ (RPS: ~6000) \| FE \| BE \| System Manager \| How to run() | 15:01 | ? | https://www.youtube.com/watch?v=Os0XnqOlUe0 |
| 69 | 2025-11 | Ecommerce Microservices NestJS (41): Scale PlaceOrder() sử dụng MQ với Fanout Exchange \| Junior... | 13:04 | ? | https://www.youtube.com/watch?v=x5lrfB_KAMc |
| 70 | 2025-11 | Advanced RabbitMQ (05): Fanout Exchange in Microservices System (⭐⭐⭐⭐) \| Up source | 10:02 | ? | https://www.youtube.com/watch?v=ps_P4haORpc |
| 74 | 2025-11 | Advanced RabbitMQ (04): Work Queue \| The Power MQ \| Place Order Event (⭐⭐⭐) | 10:36 | ? | https://www.youtube.com/watch?v=HOuJBE8cskc |
| 77 | 2025-10 | Advanced RabbitMQ (03): Hello Queue \| When Messages are Lost?? (⭐⭐) | 21:58 | ? | https://www.youtube.com/watch?v=pIm7KOdzPFI |
| 79 | 2025-10 | Advanced RabbitMQ (02): New Instance (Docker, Cloud) \| Add User \| Add Permission \| Virtual host (⭐⭐) | 17:17 | ? | https://www.youtube.com/watch?v=S5A2pwixCWk |
| 80 | 2025-10 | Advanced RabbitMQ (01): Why RabbitMQ? I'm not using it? (⭐⭐) | 12:59 | ? | https://www.youtube.com/watch?v=YgZb7q1Z0Dg |
| 209 | 2025-10 | How to deploy a budget-friendly Notification System that runs smoothly under high concurrency? | 21:13 | 5600 | https://www.youtube.com/watch?v=mYa4c-VyGS4 |
| 239 | 2025-10 | INTERN đánh bại SENIOR: GOOD CV - Với dự án tài chính thì bạn sử dụng Kafka hay là RabbitMQ? WHY? | 11:47 | 22000 | https://www.youtube.com/watch?v=wdV-XUcM2us |
| 465 | 2023-10 | Section 53: Practice on Message Ordering with Two Scenarios \| RabbitMQ \| Microservice Backend | 14:10 | ? | https://www.youtube.com/watch?v=XPaqZek9q-A |
| 467 | 2023-10 | Section 52: Message Ordering \| Microservice Backend \| #2 | 9:11 | ? | https://www.youtube.com/watch?v=nrFEJLiU-l0 |
| 469 | 2023-10 | Section 51: Message Ordering in Pub/Sub or Queues \| Microservices Backend | 13:54 | ? | https://www.youtube.com/watch?v=tVawGVrJPak |
| 471 | 2023-10 | How shopDEV Handles Message Errors in High-Concurrency Architectures with RabbitMQ \| Message Queue | 15:35 | 5100 | https://www.youtube.com/watch?v=hrSP7UocdJ8 |
| 472 | 2023-10 | Section 50: CRITICAL and Advanced Level Guide to Handling Error Messages in MQ Architecture | 9:06 | ? | https://www.youtube.com/watch?v=lZXkli4AhGA |
| 474 | 2023-10 | Section 49: Handling messages when encountering problems MQ server die (TTL) practice | 27:44 | ? | https://www.youtube.com/watch?v=muR4HURM0k4 |
| 476 | 2023-10 | Section 48: Xử lý Message Error or TTL (Time To Live) trong Message Queue thế nào? \| Kiến trúc MQ | 15:28 | ? | https://www.youtube.com/watch?v=nDxAiAB4UJg |
| 478 | 2023-10 | Section 47: [start server] First step in Microservice vs Message Queue \| Microservice System \| Lvxx | 16:44 | ? | https://www.youtube.com/watch?v=qw1z8hJRzuc |
| 482 | 2023-10 | Section 45: Tách dự án với kiến trúc Microservice System, test rabbitmq vs jest \| Level Nâng cao | 15:25 | ? | https://www.youtube.com/watch?v=eo6RJsQTOqI |
| 483 | 2023-10 | How to build application architecture with BE to send notifications to millions of users \| Part 2... | 16:05 | 12000 | https://www.youtube.com/watch?v=f1DY031XXPc |
| 484 | 2023-10 | Section 44: RabbitMQ Message Queue \| Microservice System | 15:16 | ? | https://www.youtube.com/watch?v=DWr5zV_TmF8 |
| 486 | 2023-10 | Section 43: Kafka Message Queue \| Microservice System | 18:49 | ? | https://www.youtube.com/watch?v=_YT0MsFszhY |
| 487 | 2023-10 | Khám phá kiến trúc Notifications điển hình của các ứng dụng và áp dụng vào ecommerce shopDEV | 10:55 | 9900 | https://www.youtube.com/watch?v=zeHD8cqK52I |
| 488 | 2023-10 | Section 42: Notifications Service  \| Tiếp đến là tách Message Queue System | 33:51 | ? | https://www.youtube.com/watch?v=dAefZUW3fOQ |
| 490 | 2023-10 | Section 41: Phân tích hành vi User áp dụng PUSH or PULL trong task Notification System (quan trọng). | 16:05 | ? | https://www.youtube.com/watch?v=7vFWLGBihhE |
| 492 | 2023-10 | Section 40: Triển khai hệ thống Notifications eCommerce ShopDEV \| Phần 1 | 13:16 | ? | https://www.youtube.com/watch?v=HCTET_WQR1I |
| 500 | 2023-10 | Section 37: Pub/Sub (Publish/Subscribe) \| Redis \| Application to shopDEV | 18:55 | ? | https://www.youtube.com/watch?v=U_Zy4ec_Kes |
| 624 | 2023-10 | Tại sao 80% lập trình viên tìm đến RabbitMQ cũng chỉ để sử dụng mô hình này NHANH GỌN LẸ. | 19:23 | 14000 | https://www.youtube.com/watch?v=lNs-wtsyBu8 |
| 630 | 2023-10 | RabbitMQ (5) Đỉnh cao mô hình Publish Subscribe với Node.js và so sánh với mô hình của Redis. | 22:57 | 14000 | https://www.youtube.com/watch?v=IMAzNKNUpZc |
| 632 | 2023-10 | RabbitMQ (4) Giải quyết vấn đề độ tin cậy trong queue (noAck, ttl, durable, persistent) phía Backend | 17:27 | 12000 | https://www.youtube.com/watch?v=az2VNMgNFrk |
| 633 | 2022-10 | RabbitMQ (3) Cách Send và Receive một Message vào QUEUE với NODEJS Và tôi đã thấy một số vấn đề sau. | 29:43 | 18000 | https://www.youtube.com/watch?v=--8OCUUqzTk |
| 634 | 2022-10 | RabbitMQ (2) bỏ qua cơ bản giờ đến lúc phải THÀNH THẠO tính năng Dashboard với CLOUD FREE và DOCKER | 17:36 | 21000 | https://www.youtube.com/watch?v=WVPNHLNu5m4 |
| 635 | 2022-10 | Chính xác là tôi nên sử dụng MQ khi nào? Giờ bạn đã hiểu về Message Queue \| Series RabbitMQ Node.js | 23:57 | 58000 | https://www.youtube.com/watch?v=DQRj7I3PcuM |
| 768 | 2021-10 | Nodejs microservice rabbitmq \|\| ecommerce microservice \|\| part 2 | 25:56 | 2500 | https://www.youtube.com/watch?v=7M_6_jKTSS0 |

<a id="kafka"></a>
## 2. Kafka & event streaming

| # | Upload (approx.) | Title | Duration | Views | Link |
|---|---|---|---|---|---|
| 1 | 2026-10 | Kafka (10): KAFKA 4.0 QUEUES \| SHARE GROUPS & CRITICAL NOTES (⭐⭐⭐⭐⭐) | 15:06 | 593 | https://www.youtube.com/watch?v=aJ5kLfn8AtI |
| 17 | 2026-07 | JAVA DDD Source Code: Saga, outbox, idempotency, kafka \| System Manager \| How to run() | 6:35 | ? | https://www.youtube.com/watch?v=45dfqu_jexA |
| 25 | 2026-06 | 100K QPS with Kafka + Outbox + Saga: How Senior Backend Engineers Prevent Data Loss? \| Part 2 | 11:56 | 3500 | https://www.youtube.com/watch?v=DQN0pRV8RnU |
| 26 | 2026-05 | ULTIMATE solution for system errors when switching from SAGA-OUTBOX Pattern to SAGA-CDC... | 16:51 | 5300 | https://www.youtube.com/watch?v=2TBqQBEI56A |
| 30 | 2026-05 | Kafka reduced performance by 60% due to a misunderstanding of the threading of a senior in an IoT... | 16:33 | 7700 | https://www.youtube.com/watch?v=ykIKPK6b3G4 |
| 88 | 2025-10 | Kafka (09): HASH KEY PARTITIONS IN KAFKA (⭐⭐⭐⭐⭐) | 20:05 | ? | https://www.youtube.com/watch?v=NrM4ldZHZ2E |
| 92 | 2025-10 | Kafka (08): SCALE PARTTION \| x3 PERFORMANCE (⭐⭐⭐⭐⭐) | 19:29 | ? | https://www.youtube.com/watch?v=7TO7ogwgWss |
| 93 | 2025-10 | Kafka (07): TEST BENCHMARK BENCHMARK TEST MILIONS DATA vs ORDERED (⭐⭐⭐⭐) | 12:17 | 4700 | https://www.youtube.com/watch?v=-JUCzDDHOmo |
| 163 | 2025-10 | Kafka (06): ONE PARTITION vs MULTI THREAD (⭐⭐⭐) | 24:04 | ? | https://www.youtube.com/watch?v=fZafqe9yZNI |
| 169 | 2025-10 | GO Intern (02): Sync.Once() and Singleton, how to ensure secure MySQL and Kafka connections? | 7:34 | ? | https://www.youtube.com/watch?v=HJr4KDqoxxY |
| 172 | 2025-10 | KafKa (05): MISTAKE MSG ORDER IS WRONG (⭐⭐⭐) | 6:03 | 5600 | https://www.youtube.com/watch?v=yiXL052rNNI |
| 219 | 2025-10 | KafKa(4): HI BOSS, LAG IN KAFA CONSUMER (⭐⭐⭐) | 15:59 | ? | https://www.youtube.com/watch?v=z3TPi-UDmeY |
| 220 | 2025-10 | Kafka (3): OPTIMIZING PRODUCER THROUGHPUT FOR MULTIPLE CONCURRENT MESSAGES (⭐⭐⭐⭐) | 15:32 | ? | https://www.youtube.com/watch?v=OAPiWUYy9BQ |
| 221 | 2025-10 | Kafka (2): SEND MULTIPLE ORDERS ON SALE DAYS (⭐⭐⭐) | 12:15 | ? | https://www.youtube.com/watch?v=71Bx0Qfs4JQ |
| 224 | 2025-10 | Kafka (1): GUIDE and INSTANCE BROKER vs PARTITION (⭐⭐⭐) | 16:45 | ? | https://www.youtube.com/watch?v=q5leZEPVSkU |
| 295 | 2024-10 | JAVA Fresher 11: Làm việc với Kafka Service kết hợp TEAM GO | 10:54 | ? | https://www.youtube.com/watch?v=9AGeQCwJCAs |
| 297 | 2024-10 | GO Backend (06): Deploying Kafka Microservices | 12:05 | ? | https://www.youtube.com/watch?v=uq3OvTC-LJA |
| 316 | 2024-10 | SENIOR ENGINEER: How to Sync Mysql Data to Kafka Using Debezium with N Tables at REALTIME Speed | 16:21 | ? | https://www.youtube.com/watch?v=KqLzls2xCnQ |
| 324 | 2024-10 | Kafka: Practical application of BUYING AND SELLING system Backend API | 24:01 | 14000 | https://www.youtube.com/watch?v=UIFWVisug1M |
| 326 | 2024-10 | GO Fresher (15): Kafka thực hành về mua bán cổ phiếu với các tình huống | 24:01 | ? | https://www.youtube.com/watch?v=GFGp9jZQcmI |
| 330 | 2024-10 | Kafka: Here are 7 things that are enough to start the war between TOPIC, PARTITIONS and Consumer ... | 16:32 | 33000 | https://www.youtube.com/watch?v=a7lmP5hdgB0 |
| 332 | 2024-10 | Kafka đã thay đổi hệ thống eCommerce trở nên mạnh mẽ như thế nào so với cách cũ | 11:39 | 36000 | https://www.youtube.com/watch?v=yK4T7Myi9N4 |

<a id="tx"></a>
## 3. Transactions, isolation, locks & DB concurrency

| # | Upload (approx.) | Title | Duration | Views | Link |
|---|---|---|---|---|---|
| 7 | 2026-08 | JAVA DDD (33): Automatic Order Cancellation for Overdue Payments with High Concurrency \| Redis \| ... | 9:16 | ? | https://www.youtube.com/watch?v=yDixCurikHg |
| 19 | 2026-06 | JAVA DDD (32): Handling Duplicate Order Payments with High Concurrent Data | 8:23 | ? | https://www.youtube.com/watch?v=mvLjvh1RfqQ |
| 20 | 2026-06 | Why Do Banking Jobs Always Ask Senior Backend Developers How to Detect and Fix Deadlocks in Multi... | 16:27 | 4700 | https://www.youtube.com/watch?v=9kpISaXHBvM |
| 35 | 2026-04 | INTERVIEWER ASK (2): How is Idempotency designed in your API in a high-concurrency project? | 21:02 | ? | https://www.youtube.com/watch?v=XXqDOTHTQFw |
| 42 | 2026-04 | DEV SENIOR: Atomic Update vs Optimistic Lock trừ hàng tồn kho sự khác biệt tình huống Concurrency | 15:36 | 5900 | https://www.youtube.com/watch?v=Zes0Glt8cT0 |
| 43 | 2026-03 | Dev Senior họ giải thích và xử lý tình huống đồng thời cao như thế nào? Race Condition \| Mysql ACID | 18:51 | 10000 | https://www.youtube.com/watch?v=GLqyIqWtRiA |
| 52 | 2026-01 | A deadlock, a layoff, a language change... WHAT kind of change this year? In my opinion, it would... | 13:28 | 7700 | https://www.youtube.com/watch?v=bttCAxwH1GI |
| 56 | 2026-01 | Decoding JD Java 33M-80M Gross: Why is Multithreading/Concurrency Necessary? Strong Tech Team \| (01) | 18:03 | 13000 | https://www.youtube.com/watch?v=kQeL3ORphFs |
| 57 | 2025-12 | A programmer entrusted $500,000 to 5 LLMs to invest in the stock market – what happened to Grok, ... | 7:05 | 5000 | https://www.youtube.com/watch?v=SyhJdieqXm0 |
| 59 | 2025-12 | Ecommerce Microservices NestJS (45): Share Source ERP  Microservices \| order, payment, inventory... | 2:23 | ? | https://www.youtube.com/watch?v=Ub1DbRUi43w |
| 63 | 2025-12 | Ecommerce Microservices NestJS (43): Choose PostgreSQL for Inventory instead of MySQL Let me show... | 16:27 | ? | https://www.youtube.com/watch?v=V1Dg1nSouUc |
| 67 | 2025-11 | Ecommerce Microservices NestJS (41): 10.000 req/s khi order call inventory chọn TCP, Rest, Webhook? | 16:57 | ? | https://www.youtube.com/watch?v=X6ED_5s5onQ |
| 72 | 2025-11 | NestJS (40): Thực hành Order Process (payment, reward, inventory) trong Microservices \| 2 NodeA, B | 16:55 | 7900 | https://www.youtube.com/watch?v=RI3i8s16384 |
| 94 | 2025-10 | NestJS (33): How Feed() System is Built During High-Concurrency Hours | 16:27 | ? | https://www.youtube.com/watch?v=gCic1x2doL4 |
| 132 | 2025-10 | JAVA DDD (24): SAGA PATTERN - Distributed Transactions - Senior BE | 8:06 | ? | https://www.youtube.com/watch?v=CpolDThiuWA |
| 159 | 2025-10 | My 9th Mistake (MYSQL): SELECT FOR UPDATE and the Midnight Crash \| Locking the Whole Table | 11:04 | 4500 | https://www.youtube.com/watch?v=jA8w2MoH4SA |
| 166 | 2025-10 | GO SENIOR (07): Giảm 99.99% Query MySQL với Redis Distributed Lock (40K req/s) | 11:50 | ? | https://www.youtube.com/watch?v=p8ZZY8Zvcgs |
| 175 | 2025-10 | JAVA Intern (3): ThreadPool ưu điểm NHANH, nhược điểm hệ thống TREO DeadLock | 9:03 | ? | https://www.youtube.com/watch?v=5zCsCR2TquM |
| 178 | 2025-10 | JAVA Intern (02): Vì sao bắt đầu lại là Thread cho Lập trình đồng thời? | 9:02 | ? | https://www.youtube.com/watch?v=cGMBfKBYYgI |
| 196 | 2025-10 | JAVA DDD 21: Sau OpenTicket, api nhất quán dữ liệu về Khấu trừ hàng tồn kho \| PlaceOrder() | 12:54 | ? | https://www.youtube.com/watch?v=8d2nKa82eTM |
| 201 | 2025-10 | GO SENIOR (02): Hiệu suất của Go gấp 3 lần so với JAVA khi mở bán vé hệ thống High Concurrency | 8:39 | ? | https://www.youtube.com/watch?v=JGiwW24SFz8 |
| 202 | 2025-10 | JAVA DDD 20: High concurrency control and inventory deduction in Senior vetautet | 13:38 | ? | https://www.youtube.com/watch?v=ROBf8UMAshM |
| 206 | 2025-10 | JAVA DDD 19: BA CÁCH TRỪ HÀNG TỒN KHO trong MYSQL: Tôi đã dành cho bạn một CÁCH là CÁCH THỨ 3 | 17:59 | ? | https://www.youtube.com/watch?v=9Zrxe62vdcs |
| 207 | 2025-10 | JAVA DDD 18: Bán hàng tồn kho (StockDeduction), tôi đã TỪNG đổ máu NHƯNG bạn tuyệt đối KHÔNG! | 13:49 | ? | https://www.youtube.com/watch?v=p8T082hUaXI |
| 208 | 2025-10 | GO SENIOR (01): How the High Concurrency project was started with a backend architecture using GO. | 23:22 | ? | https://www.youtube.com/watch?v=4nqpL9fDKyw |
| 210 | 2025-10 | Section 112: MASTERING MYSQL - 4 levels of isolation in Transaction, performance is FAST or SLOW ... | 26:10 | 6800 | https://www.youtube.com/watch?v=VWXZUWzT46U |
| 215 | 2025-10 | Redis Senior (2): LUA vs TRANSACTION at enterprise level, senior programmers need to understand A... | 13:30 | ? | https://www.youtube.com/watch?v=I-dDoxy1sv8 |
| 216 | 2025-10 | Redis Senior (1): OrderTicket() Must Understand LUA vs TRANSACTION in REDIS | 5:24 | ? | https://www.youtube.com/watch?v=ShLzvtglVjM |
| 229 | 2025-10 | GO Fresher (24): Xung đột đồng thời khi một goroutine xử lý nhiều channel thì select có mặt | 20:28 | ? | https://www.youtube.com/watch?v=nDik5DZ_lxU |
| 232 | 2025-10 | JAVA DDD 15: Proxy Nginx vs 2 server kịch bản mua vé đồng thời CAO StockAvailable không nhất quán | 22:24 | ? | https://www.youtube.com/watch?v=S0jeMyqSrVE |
| 241 | 2025-10 | GO Fresher (22): Đến lúc đến phần lập trình đồng thời trong GO - Goroutine Concurrency in golang | 24:03 | ? | https://www.youtube.com/watch?v=PLdLSF0_QQY |
| 252 | 2025-10 | GO Backend (19): Ngăn chặn lượng đồng thời cao 3 lớp của Router GO | 23:29 | ? | https://www.youtube.com/watch?v=1jxHWBbhV5g |
| 325 | 2024-10 | Section 116: MASTERING MYSQL - When do DEADLOCKS happen??? | 12:47 | ? | https://www.youtube.com/watch?v=JDbKCDj3pMs |
| 327 | 2024-10 | MVCC xử lý các vấn đề đồng thời của MySQL như thế nào? Câu hỏi đã được giải đáp? | 26:10 | 13000 | https://www.youtube.com/watch?v=WKGIz5ViT7Y |
| 333 | 2024-10 | Section 110: LÀM CHỦ MYSQL - Nguyên tắc ACID, sự cô lập vs cơ chế trong transaction HIỂU SÂU | 15:29 | ? | https://www.youtube.com/watch?v=ylidVS4HvtE |
| 348 | 2024-10 | NoCODE: Backend chú ý về CAP có thể gây rắc rối trong các kịch bản có tính ĐỒNG THỜI cao | 15:45 | 3100 | https://www.youtube.com/watch?v=GqH8Ez1O8pc |
| 423 | 2024-10 | How FrontEnd Helped Backend Manage High Concurrency with 1000 Requests Like a Pro... | 10:29 | 16000 | https://www.youtube.com/watch?v=vfxKrC6w34g |
| 427 | 2024-10 | NO CODE - What good options can Programmers have? Say no to Stocks with too many losses. | 11:41 | 7500 | https://www.youtube.com/watch?v=nuHM_dP8wJ4 |
| 502 | 2023-10 | Section 36: Transaction Redis \| How to use in BIG projects | 19:40 | ? | https://www.youtube.com/watch?v=63x7fIW5CkQ |
| 503 | 2023-10 | Test về MEMORY cho 1.000.000 task đồng thời giữa các ngôn ngữ Rust, Go, Node.js, Java, C#, Python | 11:28 | 9000 | https://www.youtube.com/watch?v=zZHFxVGgmrU |
| 530 | 2023-10 | Distributed locking (Optimistic and Pessimistic) Where to deploy LARGE SYSTEMS? Use CODE like this! | 12:04 | 8100 | https://www.youtube.com/watch?v=UjiGO37qugY |
| 540 | 2023-10 | Xem 3 cách CODE này bạn mới thấy được sự lợi hại về lập trình parallel và concurrent \| Nodejs | 17:59 | 5700 | https://www.youtube.com/watch?v=CBhPFo3Lz4M |
| 544 | 2023-10 | Thật tốt để CODE về nguyên tắc lập trình tuần tự, song song và đồng thời theo cách đường CAO TỐC | 14:00 | 4900 | https://www.youtube.com/watch?v=9VBRHwYDY7A |
| 585 | 2023-10 | How to implement an algorithm to BLOCK HACKERS from stealing JWT even if they steal KEYSECRET fro... | 16:32 | 15000 | https://www.youtube.com/watch?v=pK3oBX0vB38 |
| 658 | 2022-10 | Block API replay attacks for non-Backend task HACKERS \| Nonce vs timestamp | 25:21 | 19000 | https://www.youtube.com/watch?v=HXMJD4mN4bY |
| 664 | 2022-10 | Giải pháp này giúp aliconcon.com giải quyết bán không vượt hàng tồn kho trong eCommerce Rest api p-6 | 36:37 | 5600 | https://www.youtube.com/watch?v=OQcAhKwF2oI |
| 667 | 2022-10 | Bạn muốn biết 2 cách quản lý tồn kho mà Tiki Shopee đang sử dụng \| Kiến trúc backend eCommerce | 18:51 | 6600 | https://www.youtube.com/watch?v=qHqMB47liwQ |
| 711 | 2022-10 | Nodejs có thể chịu tải được 100k/s test với 100 users đồng thời ? \| Autocannon Load Test Nodejs | 21:49 | 12000 | https://www.youtube.com/watch?v=_tBWQ8JaFOs |
| 713 | 2022-10 | Setup Mongodb Replication hoàn tiền lại tài khoản nếu giao dịch lỗi (2) \| Transaction Mongodb Nodejs | 21:02 | 5900 | https://www.youtube.com/watch?v=fQPB5TPqcGM |
| 714 | 2022-10 | Using Transactions to send and receive money in Banking with MongoDB (1) \| Transaction MongoDB No... | 25:31 | 8700 | https://www.youtube.com/watch?v=spdyW-ANgJw |
| 723 | 2022-10 | The problem is that there is 1 item left in inventory but many USERS are buying at the same time ... | 18:52 | 36000 | https://www.youtube.com/watch?v=qxRtMizGvWE |

<a id="dist"></a>
## 4. Idempotency, consistency & distributed transactions (saga/outbox)

| # | Upload (approx.) | Title | Duration | Views | Link |
|---|---|---|---|---|---|
| 21 | 2026-06 | INSERT INTO vs. INSERT IGNORE: Lessons from Stripe (Payments) on Preventing Duplicate Data | 14:49 | 2400 | https://www.youtube.com/watch?v=G4-_ckYTtvo |
| 22 | 2026-06 | How to implement Stripe's simple and effective API Idempotency. I'll show you how to apply it. | 13:09 | 3400 | https://www.youtube.com/watch?v=A9gqa8q-l1w |
| 24 | 2026-06 | JAVA DDD (31): DONE Implementing the Outbox Pattern to Prevent Message Loss | 8:49 | ? | https://www.youtube.com/watch?v=KGjgbx9vTos |
| 36 | 2026-04 | System Design: How is Idempotency implemented when duplicate payments occur simultaneously at hig... | 18:31 | 7200 | https://www.youtube.com/watch?v=inUimYVAGv0 |
| 40 | 2026-04 | Phỏng vấn lần 2 với 4TECH: Cách đảm bảo tính nhất quán khi ghi dữ liệu vào cả Redis và MySQL? | 14:28 | 6300 | https://www.youtube.com/watch?v=piN--APNE98 |
| 97 | 2025-10 | NestJS (32): System to implement WRITE CACHE and MYSQL data consistency with the following 4 comp... | 14:15 | ? | https://www.youtube.com/watch?v=MMczVW-4jb4 |
| 157 | 2025-10 | SOURCE[04/27/25]: Tet Train Ticket System - Scaling APIs to 40,000 req/s with a Distributed System | 6:28 | ? | https://www.youtube.com/watch?v=Y7TnDNYuROI |
| 176 | 2025-10 | JAVA DDD (25): SAGA PATTERN - Order, Payment is DONE ✅ ✅ ✅ | 11:56 | ? | https://www.youtube.com/watch?v=CMapX0yC7zM |
| 226 | 2025-10 | JAVA DDD 17: Implementing the optimal level of consistency for application requirements (2) | 19:09 | ? | https://www.youtube.com/watch?v=0w-DO4guvRU |
| 228 | 2025-10 | JAVA DDD 16: DEV SA (Solution Architecture), dữ liệu phân tán giờ đã nhất quán với cách đơn giản | 9:37 | ? | https://www.youtube.com/watch?v=XKCKnwJ0F9Y |
| 235 | 2025-10 | Data consistency: Have you ever encountered this issue when booking a flight? | 9:35 | 4000 | https://www.youtube.com/watch?v=XBwGeRSo20A |
| 236 | 2025-10 | JAVA DDD 14: Stop coding for 5 minutes; what kind of consistency do you see in practice? | 9:35 | ? | https://www.youtube.com/watch?v=agIL52ZnQ0o |
| 240 | 2025-10 | JAVA DDD 13: Triển khai hệ thống phân tán LOGs ELK cho hệ thống LỚN vetautet.com DDD - Project | 27:41 | ? | https://www.youtube.com/watch?v=6DGnzYkK0uQ |
| 250 | 2025-10 | JAVA DDD 10: Hệ thống giám sát Connects vs Performance Distributed Redis như thế nào? Chưa ngủ ngon | 16:41 | ? | https://www.youtube.com/watch?v=5IuSc2NAM60 |
| 261 | 2025-10 | JAVA DDD 06: Tâm sự DEV và vì sao tôi lại không sử dụng LUA Redis trong kịch bản Distributed Cache! | 11:54 | ? | https://www.youtube.com/watch?v=zQWWGnhyZ0s |
| 262 | 2025-10 | SHOCK: Distributed Cache Redis has betrayed us, $1 billion lost on the second day of ticket sales. | 9:53 | 12000 | https://www.youtube.com/watch?v=1pGuG5S68zM |
| 264 | 2025-10 | JAVA DDD 05: Distributed Cache - Second Line of Defense API (Online Ticketing) - LUA vs Redisson | 18:26 | ? | https://www.youtube.com/watch?v=GqCohsho54s |
| 453 | 2023-10 | Backend vs FrontEnd: Retry API Carefully \| HOT FIX | 10:00 | 4800 | https://www.youtube.com/watch?v=gyaoxeCKkRY |
| 458 | 2023-10 | Backend vs FrontEnd: Error 5xx at midnight, when using retryAble, retryDelay I slept very WELL! | 11:27 | 4700 | https://www.youtube.com/watch?v=uuaST5OhCx4 |

<a id="redis"></a>
## 5. Redis & caching

| # | Upload (approx.) | Title | Duration | Views | Link |
|---|---|---|---|---|---|
| 90 | 2025-10 | NestJS (35): Why Redis Pipeline is the Secret Weapon for Like/Unlike? | 19:46 | ? | https://www.youtube.com/watch?v=Qs1d13ZlL6w |
| 98 | 2025-10 | NestJS (31): Time to integrate Cache to increase QPS, TPS in high traffic systems RIGHT | 12:54 | ? | https://www.youtube.com/watch?v=87eviq_Oz4k |
| 101 | 2025-10 | NestJS (30): FE + BE project trybuy.com is on the shelf (aws, smtp, elastic, nginx, redis, mysql,... | 10:07 | ? | https://www.youtube.com/watch?v=2gXttp6tWEM |
| 185 | 2025-10 | SOURCE[21/03/25]: vetautet - Tích hợp cluster, sentinel vs local cache tăng tốc API up 30.000 req/s | 2:48 | ? | https://www.youtube.com/watch?v=gCNccxGuIv0 |
| 186 | 2025-10 | GO SENIOR (5): The secret behind Local Cache in a million-request ticketing system. | 12:58 | ? | https://www.youtube.com/watch?v=g2Cii1Sy4kU |
| 190 | 2025-10 | OpenSource: Valkey Redis competitor, stop using redis? | 7:08 | 3100 | https://www.youtube.com/watch?v=IR03bajM_ig |
| 199 | 2025-10 | GO SENIOR (03): Boost READ and WRITE performance in APIs with REDIS Standalone vs Sentinel vs Clu... | 11:35 | ? | https://www.youtube.com/watch?v=7vT59QnZigI |
| 211 | 2025-10 | Redis Senior (5): Master đã sập, hệ thống tự động chuyển đổi nhờ Sentinel | 13:53 | ? | https://www.youtube.com/watch?v=OrbVP56w9UA |
| 212 | 2025-10 | Redis Senior (4): Hệ thống bây giờ căng quá, Master/Slave đến đây... | 9:46 | ? | https://www.youtube.com/watch?v=fe6yeDRtD0E |
| 214 | 2025-10 | Redis Senior (3): Lập trình về LUA vì sao các hệ thống đều sử dụng LUA? | 13:38 | ? | https://www.youtube.com/watch?v=wNOGLTkEb7I |
| 322 | 2024-10 | Redis Cache Breakdown: Thử thách 2 khi xử lý Dữ liệu NÓNG hàng TRIỆU dữ liệu của Backend \| Cạm bẫy 2 | 9:50 | 4700 | https://www.youtube.com/watch?v=mco-hXkHqjY |
| 331 | 2024-10 | GO Fresher (13): Redis Pool In Sevice | 14:03 | ? | https://www.youtube.com/watch?v=hwXW_2DAdHo |
| 355 | 2024-10 | Section 98: Practicing the CACHE PENETRATION pitfall with Redis vs Nodejs | 24:45 | ? | https://www.youtube.com/watch?v=ZeyO1_DwkfM |
| 356 | 2024-10 | Redis Cache Penetration: How Did Outstanding Backends Handle 100 Million Requests? (Pitfall 1) | 13:48 | 22000 | https://www.youtube.com/watch?v=_15A-fkBP7o |
| 357 | 2024-10 | Redis: Cạm bẫy đầu tiên khi sử dụng cache mà một backend xuất sắc phải xử lý 100 triệu requests | 13:13 | ? | https://www.youtube.com/watch?v=BLfrJxvA2aY |
| 390 | 2024-10 | How to Connect Redis and Node.js with Reliability and Timeout Monitoring | 23:02 | 7600 | https://www.youtube.com/watch?v=q8d6An4a60E |
| 391 | 2024-10 | Section: 84: Phương pháp tốt nhất connect redis vs node.js tin cậy cao trong backend | 23:02 | ? | https://www.youtube.com/watch?v=4s3gHFS3aO8 |
| 406 | 2024-10 | RediSearch \| SEARCH trong eCommerce backend sử dụng công nghệ tìm kiếm mạnh mẽ như thế này? | 18:28 | 6100 | https://www.youtube.com/watch?v=mw-DdAPKV_A |
| 505 | 2023-10 | Section 35: Redis Zset \| Common Commands for Tracking Best-Sellers, Views, and Follows | 12:26 | ? | https://www.youtube.com/watch?v=8fw-VnP3Zq0 |
| 507 | 2023-10 | 34\| Redis Sets \| Used to develop like functions, find common friends like facebook and common com... | 18:48 | ? | https://www.youtube.com/watch?v=SLGE0L-Ndo8 |
| 514 | 2023-10 | Section 31: List Redis \| Cấu trúc dữ liệu, lệnh phổ biến và kịch bản nào sử dụng? \| Redis backend | 22:15 | ? | https://www.youtube.com/watch?v=zwDT1KDlNF8 |
| 516 | 2023-10 | Section 30: Hash Redis \| Cấu trúc dữ liệu, lệnh phổ biến và kịch bản nào sử dụng? \| Redis backend | 15:26 | ? | https://www.youtube.com/watch?v=uz73HbycDLM |
| 519 | 2023-10 | Section 29: String Redis \| Data structures, common commands and what scenarios to use? \| Redis ba... | 26:38 | ? | https://www.youtube.com/watch?v=X7NiSVo_NHE |
| 524 | 2023-10 | Section 28: Hôm nay tôi đi phỏng vấn về Redis có 5 câu hỏi dành cho tôi và bạn \| Node.js backend | 17:24 | 16000 | https://www.youtube.com/watch?v=u5-flcmINc4 |
| 525 | 2023-10 | Section 27: Học Redis vui lòng xem qua mẩu chuyện này của Antirez cha đẻ nguồn cảm hứng. | 17:32 | ? | https://www.youtube.com/watch?v=QEUQsBXRFJk |
| 529 | 2023-10 | Section 26: Order service Part 2 \| Tiếp đến là Redis chuyên sâu. | 48:52 | ? | https://www.youtube.com/watch?v=mswayRA-870 |
| 617 | 2023-10 | Thử nghiệm VOICER ROBO AI giới thiệu 3 cuốn sách nổi tiếng về REDIS mà các Developers nên ĐỌC FREE | 2:27 | 1800 | https://www.youtube.com/watch?v=jDJ46aQrRWs |
| 637 | 2022-10 | Connect Nodejs Redis async await với 3 level khác nhau và cách nào hiệu quả hơn \| redis tutorial | 17:45 | 7800 | https://www.youtube.com/watch?v=EXv_NCNXH7c |
| 639 | 2022-10 | Redis vs MySQL Để check QPS (query per second) tôi phải đến năm thứ 4 lập trình mới biết về sysbench | 13:19 | 9700 | https://www.youtube.com/watch?v=dpDGXbe_LeE |
| 640 | 2022-10 | Redis and Nodejs Practice \| Using Redis Cloud FREE with Redisinsight \| Redis Tutorial \| Part 1 | 10:49 | 18000 | https://www.youtube.com/watch?v=bkSdxT1Vk4s |
| 641 | 2022-10 | REDIS and 3 common problems when using nodejs \| Cache avalanche \| Cache breakdown \| Cache penetra... | 9:21 | 20000 | https://www.youtube.com/watch?v=VE1oTBR0gig |
| 642 | 2022-10 | Redis là gì? Bài học này đủ để bắt đầu \| Là một Backend bạn đã từng gặp những trường hợp này chưa? | 19:15 | 93000 | https://www.youtube.com/watch?v=HSknuSIoK6A |
| 662 | 2022-10 | Sử dụng redis làm Shopping CART tăng hiệu suất GIỜ CAO ĐIỂM cho hệ thống eCommerce \| Series Redis | 16:25 | 15000 | https://www.youtube.com/watch?v=lMf0tBKfgPw |
| 699 | 2022-10 | Vì sao lại sử dụng RedisStore với Express Session, nếu không sử dụng thì sao? \| EXPRESS SESSION NODE | 22:42 | 8600 | https://www.youtube.com/watch?v=d7hbNHy5ToM |
| 718 | 2022-10 | LRUCache là gì? Cách triển khai và khi nào nên áp dụng \| Performance Backend Services \| Microservice | 18:55 | 4700 | https://www.youtube.com/watch?v=d04M8IYiOGE |
| 720 | 2022-10 | Services tự động hủy đơn hàng nếu chưa thanh toán N phút như Traveloka \| Microservices redis nodejs | 26:10 | 8500 | https://www.youtube.com/watch?v=tIuUXU2Zf04 |
| 722 | 2022-10 | Cách khắc phục kho còn 1 nhưng có nhiều USERS mua hàng cùng một lúc (2) \| Microservices redis nodejs | 27:00 | 21000 | https://www.youtube.com/watch?v=OUGfEleDGaE |
| 724 | 2021-10 | Thiết kế microservices với nodejs và redis pub sub ai cũng hiểu \| REDIS VS NODEJS MICROSERVICES | 29:58 | 19000 | https://www.youtube.com/watch?v=wzZXRoeYFPw |
| 734 | 2021-10 | Cách hạn chế User Requests N lần trên X phút trong Rest API \| Nodejs Redis | 25:14 | 8500 | https://www.youtube.com/watch?v=_9J3HyhVv5k |
| 736 | 2021-10 | Redis sets \| Redis CLI Tutorial \| Complete Course | 12:11 | 2400 | https://www.youtube.com/watch?v=qgoYBqmSjko |
| 737 | 2021-10 | Redis lists \| Redis CLI Tutorial \| Complete Course | 13:17 | 3200 | https://www.youtube.com/watch?v=_inbcP9batQ |
| 738 | 2021-10 | Redis string \| Redis CLI Tutorial \| Complete Course | 10:59 | 12000 | https://www.youtube.com/watch?v=OF97evA4JVI |
| 743 | 2021-10 | Blacklist and Refresh Tokens (JWT) with Redis (12) \| NODE.JS API Authentication \| ANONYSTICK | 10:41 | 8700 | https://www.youtube.com/watch?v=PP_7AvltBBM |
| 745 | 2021-10 | Using redis, redis-commander and create a redis client Nodejs (10) \| NODE.JS API Authentication | 12:04 | 5700 | https://www.youtube.com/watch?v=ORkgL1SURhg |
| 765 | 2021-10 | Full-text search with RediSearch Nodejs | 4:49 | 1100 | https://www.youtube.com/watch?v=83tSHafdsHU |
| 766 | 2021-10 | install redisearch ubuntu 20.04 | 10:18 | 1000 | https://www.youtube.com/watch?v=Pqv8_q-620Q |
| 770 | 2021-10 | Caching in nodejs with redis | 4:45 | 1800 | https://www.youtube.com/watch?v=0oJCzoMSEw4 |

<a id="db"></a>
## 6. MySQL / PostgreSQL / MongoDB / Elasticsearch

| # | Upload (approx.) | Title | Duration | Views | Link |
|---|---|---|---|---|---|
| 2 | 2026-10 | Vector Databases: Understanding the Evolution from Software Engineer to AI Engineer | 12:45 | 17000 | https://www.youtube.com/watch?v=kRXoK02KJow |
| 6 | 2026-09 | Claude Code \| How to Deploy MCP for Optimal Database Connection BUT Stay Secure with These 5 Gold... | 15:58 | 8600 | https://www.youtube.com/watch?v=lKpSn7q-oEA |
| 38 | 2026-04 | Senior Backend: Dữ liệu đã được mã hoá trong MYSQL, làm thế nào tìm kiếm NUMPHONE đây SẾP? | 14:46 | 8600 | https://www.youtube.com/watch?v=1u5YbRBb9ls |
| 51 | 2026-01 | Solving problem (1): DELETING MESSAGES IN GROUP CHAT vs DESIGNING A CHAT DATABASE \| System Design | 16:52 | ? | https://www.youtube.com/watch?v=fSkWLqXUtJI |
| 62 | 2025-12 | MYSQL BACKEND: Tối ưu hoá UNION từ 3.3s còn 0.45s với 2 tables 6.000.000 dữ liệu? Share kinh nghiệm | 11:22 | 4300 | https://www.youtube.com/watch?v=rF08XXh9klw |
| 64 | 2025-12 | Vấn đề query CHẬM khi tách Monolith qua Microservices đã được FIX thế nào? #microservices #backend | 11:10 | 6100 | https://www.youtube.com/watch?v=LHv4oFFPCdE |
| 71 | 2025-11 | Is PostgreSQL a Better Choice than MySQL for High PERFORMANCE Application Deployment? A Multi-Thr... | 15:30 | 6200 | https://www.youtube.com/watch?v=Brc-yvUL57Q |
| 75 | 2025-10 | In Microservices architecture: How is the problem of integrating multiple databases handled? | 14:09 | 14000 | https://www.youtube.com/watch?v=ReQZtMHTdbA |
| 83 | 2025-10 | MYSQL sync ELASTCISEARCH: Chọn 1 trong 4 cách đồng bộ hiệu suất cao REALTIME \| Best Practice Binlog | 10:25 | 3200 | https://www.youtube.com/watch?v=WaexBdjw_ic |
| 84 | 2025-10 | Migration DATABASE Trick from OLD to NEW \| When API is still ONLINE to ensure no data is missed? | 17:10 | ? | https://www.youtube.com/watch?v=p745Za1JbTA |
| 86 | 2025-10 | MySQL Backend: I APOLOGIZE for the confusion about the 3 concepts PARTITION, SHARDING, REPLICATION | 12:43 | 4800 | https://www.youtube.com/watch?v=rETG8-x_XFo |
| 89 | 2025-10 | Solving N + 1 Problem, besides JOIN, this is how BIG systems like FB or Netflix use it! | 12:06 | 15000 | https://www.youtube.com/watch?v=h0Y9oaBQv9w |
| 103 | 2025-10 | JAVA Fresher (21): Spring Security Designs Shopee Decentralization with RBAC, MySQL and MyBatis-Plus | 28:05 | ? | https://www.youtube.com/watch?v=zHYpL-Hizx0 |
| 108 | 2025-10 | NestJS (27): Security vs Permission JWT MySQL TypeORM | 31:44 | ? | https://www.youtube.com/watch?v=eIYVH2irhF4 |
| 109 | 2025-10 | NestJS (26): Source Code: API Search MySQL vs ElasticSearch | 1:56 | ? | https://www.youtube.com/watch?v=CgEz7QeKe9c |
| 110 | 2025-10 | NestJS (25): BUID API to search BILLION products on eCommerce with standard design in ELASTICSEARCH | 18:25 | ? | https://www.youtube.com/watch?v=sQb9aHBOVvs |
| 111 | 2025-10 | How is the eCommerce Products search API designed to STANDARDIZE data when using ElasticSearch? | 13:31 | 7300 | https://www.youtube.com/watch?v=DvT_6USVg1k |
| 119 | 2025-10 | Section 54: MySQL Setup master slave \| SQL | 27:50 | 7600 | https://www.youtube.com/watch?v=ikH6_39OF7k |
| 130 | 2025-10 | 9 INDISPENSABLE PRINCIPLES with MYSQL Table before initializing with Backend Programming \| SHOULD... | 24:57 | 11000 | https://www.youtube.com/watch?v=hicWEOfMPn8 |
| 149 | 2025-10 | GO Fresher (25): Export MySQL to Excel với 1.000.000 rows từ 10s còn 3s. Tuyệt vời lắm GO + STREAM | 11:23 | ? | https://www.youtube.com/watch?v=ES-hUowEVMo |
| 152 | 2025-10 | Export Data SQL to Excel: VERY HIGH performance with millions of data I have tried the following ... | 12:29 | 4000 | https://www.youtube.com/watch?v=dxNr51KxwUQ |
| 167 | 2025-10 | JAVA DDD (26): Triển khai TINH TẾ một TABLE có dữ liệu tăng lên CHỤC TRIỆU order mỗi tháng | 15:13 | ? | https://www.youtube.com/watch?v=AGZIx1syYrE |
| 174 | 2025-10 | GO SENIOR (06): From MySQL DOWN to stable at 17,000 req/s — A System Design Lesson | 14:00 | ? | https://www.youtube.com/watch?v=Q8yU105xCx0 |
| 180 | 2025-10 | JAVA Fresher (18): MySQL vs MyBatis-Plus | 11:39 | ? | https://www.youtube.com/watch?v=YDtWZnm-QT0 |
| 181 | 2025-10 | Intern beats Senior: Stop using LIKE in SEARCH MYSQL we improved from 6s to 0.1s | 14:34 | 19000 | https://www.youtube.com/watch?v=1GTak-ifAnQ |
| 204 | 2025-10 | KHI NÀO SHARDING TABLE LỚN trong MYSQL? Đây là 2 cách, VẤN ĐỀ phiền toái bắt đầu từ đây | 14:07 | 4300 | https://www.youtube.com/watch?v=xya2ClZWbNM |
| 217 | 2025-10 | MySQL BE: Điều gì xảy ra nếu khai báo int(10) thay vì int(1)? Performance có thay đổi hay không? | 8:00 | 2900 | https://www.youtube.com/watch?v=d8vMgg32juU |
| 251 | 2025-10 | JAVA DDD 09: Giám sát MYSQL ONLINE qua hệ thống API | 11:22 | ? | https://www.youtube.com/watch?v=jqspVKUye9M |
| 253 | 2025-10 | Which time data type in MySQL is the best: DateTime, Timestamp, or bigInt? | 10:23 | 4400 | https://www.youtube.com/watch?v=JwbQKBhmrC4 |
| 286 | 2024-10 | Database Backend: If you feel SLOW QUERIES, see how smart MYSQL optimization is? | 32:00 | 7600 | https://www.youtube.com/watch?v=ls6vJLO4otA |
| 290 | 2024-10 | MYSQL BACKEND: When using JOINS, REMEMBER the principle that they must be CLOSE and INCLUSIVE to ... | 27:55 | 6900 | https://www.youtube.com/watch?v=Oe_AcOyUnVs |
| 294 | 2024-10 | MYSQL BACKEND: Why choose MONGODB, can't MYSQL do it too? 2/8 criteria worth pondering | 8:33 | 16000 | https://www.youtube.com/watch?v=tnUBjJJnwn0 |
| 298 | 2024-10 | MYSQL BACKEND: Cùng một câu QUERY nhưng đồng nghiệp tôi hiệu suất CAO HƠN rất nhiều | 18:32 | 8000 | https://www.youtube.com/watch?v=1dYbhikXnkw |
| 302 | 2024-10 | MYSQL BACKEND: Tại sao sử dụng SELECT * sẽ làm chậm hiệu suất và không hiệu quả, Tôi tiếp tục thử... | 10:51 | 10000 | https://www.youtube.com/watch?v=O3tTBcEmpWA |
| 303 | 2024-10 | JAVA Fresher 07: Getting familiar with pageable pagination with Spring Data JPA | 12:59 | ? | https://www.youtube.com/watch?v=pDKVqwN4fLg |
| 308 | 2024-10 | MYSQL BACKEND: Optimizing Pagination from 7s to 1s with a 10,000,000-Row Table, Get a Raise... | 18:30 | 61000 | https://www.youtube.com/watch?v=tjT4O5HGIEU |
| 314 | 2024-10 | GO Backend (02): Goose (A database migration tool) hiệu suất cao của dân BACKEND | 17:31 | ? | https://www.youtube.com/watch?v=GTeu_vX2NWU |
| 315 | 2024-10 | GO Backend (01) - JOIN TEAM vs CÔNG TY ĐỀ NGHỊ chuyển GORM sang SQLC như thế nào? | 14:44 | ? | https://www.youtube.com/watch?v=j8pfNFX7rs8 |
| 319 | 2024-10 | GO Fresher (19): Migrating Schema with GORM to MYSQL and DUMP Database | 15:45 | ? | https://www.youtube.com/watch?v=EWqsyxVKj18 |
| 328 | 2024-10 | Section 114: MASTER MYSQL - JSON in MYSQL It's very good, ladies and gentlemen. | 24:45 | ? | https://www.youtube.com/watch?v=tPDdm3N2Yq0 |
| 334 | 2024-10 | GO Fresher (12): Connect Mysql Pool hiệu quả và Test BenchMark cho 2 trường hợp! | 29:01 | ? | https://www.youtube.com/watch?v=aIHwJCfvNfY |
| 336 | 2024-10 | MySQL - Are INDEXES actually being used incorrectly? An interviewer shares the best OPTIMIZATION ... | 17:38 | 22000 | https://www.youtube.com/watch?v=UYmCFPVx-XY |
| 337 | 2024-10 | Section 108: LÀM CHỦ MYSQL - Nguyên tắc sử dụng 6 loại index và công thức tối ưu. | 17:38 | ? | https://www.youtube.com/watch?v=BosoW1zMzuw |
| 341 | 2024-10 | Section 106: LÀM CHỦ MYSQL (5) - HIỂU NHẦM VỀ INDEX PRIMARY, UNIQUE, FULLTEXT? | 29:00 | ? | https://www.youtube.com/watch?v=7pfVaIBSZ_U |
| 343 | 2024-10 | Section 104: Essential steps to troubleshoot MySQL errors online \| MySQL Series | 25:22 | ? | https://www.youtube.com/watch?v=Jn26PlOEkVE |
| 352 | 2024-10 | Section 100: Best Practices for Connecting Elasticsearch with Node.js and Implementing CRUD Opera... | 19:20 | ? | https://www.youtube.com/watch?v=7vnSdxvIwQY |
| 360 | 2024-10 | ElasticSearch (3) Kỹ năng cần thiết sử dụng API REST trong môi trường làm việc | 19:38 | 5800 | https://www.youtube.com/watch?v=L5q2xNIQQrc |
| 367 | 2024-10 | Giải thích chi tiết về ElasticSearch cho các câu lệnh truy vấn cho DÂN BACKEND nhà mình. | 19:43 | 15000 | https://www.youtube.com/watch?v=QaHvavpqxMU |
| 368 | 2024-10 | Section 91: Giờ hãy thêm elasticSearch vào CV để chuẩn bị cuộc phỏng vấn chất lượng CAO | 19:38 | ? | https://www.youtube.com/watch?v=nG8DOtbNO0k |
| 373 | 2024-10 | Section 90: Tư duy kiến trúc elasticsearch cho kỹ sư BE (1) | 19:43 | ? | https://www.youtube.com/watch?v=61LBcDdpCr4 |
| 374 | 2024-10 | I don't know when to use Elaticsearch instead of MySQL, Mongodb? | 10:48 | 16000 | https://www.youtube.com/watch?v=ccxuHMGKX3U |
| 380 | 2024-10 | Understanding SKUs and SPUs: Designing Product Data with MySQL and MongoDB for Seniors \| Members ... | 15:28 | 8600 | https://www.youtube.com/watch?v=902xL7t3cX8 |
| 393 | 2024-10 | Hiểu biết đầy đủ về kiến trúc MySQL: Thiết kế bảng cơ sở dữ liệu theo dạng 3NF (3) | 17:25 | 7100 | https://www.youtube.com/watch?v=-N3x7ESpHrQ |
| 396 | 2024-10 | Hiểu biết đầy đủ về kiến trúc MySQL: Thiết kế bảng cơ sở dữ liệu theo dạng 2NF (2) | 10:35 | 14000 | https://www.youtube.com/watch?v=L9tOHpxlnMA |
| 398 | 2024-10 | A thorough understanding of MySQL architecture: Designing database tables in 1NF form (1) | 17:55 | 15000 | https://www.youtube.com/watch?v=7Y0ii_QjlKM |
| 409 | 2024-10 | RBAC database design with 4 Mysql tables and 3 Mongodb collections | 11:08 | 6700 | https://www.youtube.com/watch?v=ZbJmxu33-Gc |
| 410 | 2024-10 | Section 76: Thiết kế CSDL MySQL về phân quyền và cách query như thế nào trong shopDEV ecommerce. | 14:42 | ? | https://www.youtube.com/watch?v=lmCaDqakf6o |
| 413 | 2024-10 | How to Implement Role-Based Access Control (RBAC) in eCommerce Systems and Design Efficient MySQL... | 12:23 | 9500 | https://www.youtube.com/watch?v=uo_OjJQ0q5s |
| 421 | 2024-10 | Section 72: Import Mysql local to EC2 và cho phép truy cập mysql từ xa \| Làm chủ AWS | 13:58 | ? | https://www.youtube.com/watch?v=XvbqDLfbczo |
| 422 | 2024-10 | Sự thật về cú pháp SQL trong Next.js 14, tôi đã tìm thấy một điều tuyệt vời. | 12:30 | 10000 | https://www.youtube.com/watch?v=DQ77JGebNQE |
| 424 | 2024-10 | Section 71: Setup EC2 + Mysql với Linux. Tạo quyền, quản lý database bảo mật... | 15:49 | ? | https://www.youtube.com/watch?v=QxB3ifUaLDA |
| 436 | 2024-10 | MySQL task to optimize Orders table with tens of millions of data per MONTH in eCommerce ShopDEV | 29:26 | 17000 | https://www.youtube.com/watch?v=aY8SiBuFLPw |
| 444 | 2023-10 | 2 of 4 ways to FAST data sync between MySQL (Mongob) vs ElasticSearch \| DBS | 10:20 | 11000 | https://www.youtube.com/watch?v=I8xq5Phu2h0 |
| 448 | 2023-10 | Section 60: Index MySQL những sai lầm nên tránh | 47:04 | ? | https://www.youtube.com/watch?v=GSonUVsFFJ8 |
| 450 | 2023-10 | Section 59: Partition Database dành cho Level cao, DBA \| Phần 2 | 20:16 | ? | https://www.youtube.com/watch?v=eEt3yuz3S_I |
| 452 | 2023-10 | Section 58: Database Partitioning, Highly Important (1) | 28:07 | ? | https://www.youtube.com/watch?v=KZ199lfI7N0 |
| 459 | 2023-10 | Section 56: Practice creating test data of 10,000,000 records in MySQL for level 2,3 \| Part 2 | 22:18 | ? | https://www.youtube.com/watch?v=UFfn1dHbfCs |
| 462 | 2023-10 | Section 55: Hands-on Tutorial: Generating 10,000,000 Test Records in MySQL for Beginners | 7:47 | ? | https://www.youtube.com/watch?v=UjVTDWdPL0U |
| 479 | 2023-10 | Docker MySQL setup: Front-end (FE) engineers should understand this too, not just back-end (BE) | 16:57 | 6400 | https://www.youtube.com/watch?v=-UX_bz376UA |
| 480 | 2023-10 | Section 46: Integration Testing with Jest vs Mongodb \| Microservice System | 10:50 | ? | https://www.youtube.com/watch?v=0pgx_XUjddo |
| 494 | 2023-10 | Phỏng vấn RẤT OK! NHƯNG làm thế nào để phân biệt trình độ của một lập trình viên khi JOIN TEAM mới? | 13:00 | 15000 | https://www.youtube.com/watch?v=uvkZjU2LBIs |
| 499 | 2023-10 | Reduce Query Time from 3s to 0.2s for Nested Comments: See How My Boss Stores Data to Understand | 15:47 | 14000 | https://www.youtube.com/watch?v=PE6f66u7KBQ |
| 515 | 2023-10 | How to properly handle high MongoDB CPU usage beyond optimizing indexes? \| The Programmer's Path | 14:00 | 2100 | https://www.youtube.com/watch?v=6Oln-40kOq0 |
| 517 | 2023-10 | Testing MySQL PoolConnect Config: Are 96 connections 50x faster than 1000? (With GIT) | 9:58 | 2300 | https://www.youtube.com/watch?v=AjzeZ8nzJ8E |
| 553 | 2023-10 | Subset Pattern MongoDB: What will the big app do? They take the solution and put it into practice... | 12:17 | 3300 | https://www.youtube.com/watch?v=CQzxsR8hnHQ |
| 558 | 2023-10 | Attribute Pattern Mongodb: Khi Sếp chỉ cách đánh INDEX, tiết kiệm sizeStoreINDEX và truy vấn NHANH | 8:41 | 4900 | https://www.youtube.com/watch?v=48RTknpjmkk |
| 561 | 2023-10 | Polymorphic Pattern in MongoDB: Designing Products to Overcome Application Limitations | 11:46 | 6000 | https://www.youtube.com/watch?v=9fBNtR6yU98 |
| 563 | 2023-10 | Index Database: Nếu trả lời được câu hỏi này, vui lòng gửi CV cho Tips \| Mongodb Design Patterns (2) | 24:57 | 13000 | https://www.youtube.com/watch?v=n3yRC2HBrPw |
| 566 | 2023-10 | We already have MySQL, why do we need MongoDB? How to solve massive data problems with MongoDB \| ... | 18:58 | 19000 | https://www.youtube.com/watch?v=TlxWi81Z4Y0 |
| 586 | 2023-10 | Section 3: Connect MongoDB to Node.js Using Mongoose and 7 things to implement in the system. | 37:29 | ? | https://www.youtube.com/watch?v=TiMiJazU4Pc |
| 595 | 2023-10 | (5) SQL Injection Mongodb Chỉ đơn giản thế này là XONG PHIM và cách phòng chống  \| Node.js Backend | 17:48 | 5600 | https://www.youtube.com/watch?v=nzighSNJM6M |
| 597 | 2023-10 | (4) Cách kết nối multiple database trong Nodejs một cách Thanh lịch \| Node.js Backend Architecture | 15:50 | 5100 | https://www.youtube.com/watch?v=mfuQjkqdbNA |
| 601 | 2023-10 | Time to Use the MongoDB Bucket Pattern to Design a Comment System and It's Truly OPTIMIZED (3) | 29:51 | 5100 | https://www.youtube.com/watch?v=7ki7uw46Flw |
| 605 | 2023-10 | Câu trả lời quá BẤT NGỜ: Tôi hỏi con CHAT GPT: "Thiết kế cho tao một model comments with MongoDB?" | 1:24 | 7100 | https://www.youtube.com/watch?v=_kYOxnAK9J8 |
| 607 | 2023-10 | Index Database thì lời khuyên nên xem CẤU TRÚC này? Và không phải index nào cũng nhanh? | 15:33 | 24000 | https://www.youtube.com/watch?v=XPtlC1YeRwU |
| 613 | 2023-10 | Elasticsearch Bạn có CHẮC là bạn sử dụng ĐÚNG những lệnh SEARCH dữ liệu của các tình huống SAU ĐÂY ? | 22:42 | 13000 | https://www.youtube.com/watch?v=hUOgRS6dEVQ |
| 621 | 2023-10 | Thực hành Kinaba cách tạo Index, Mapping thao tác CRUD trong Elasticsearch (2) \| Search Engine | 26:07 | 8600 | https://www.youtube.com/watch?v=HrGVCCjRDZQ |
| 626 | 2023-10 | ELK Stack là gì? Tôi đã bắt đầu tìm hiểu Elasticsearch và Kibana với thao tác nhanh gọn lẹ như sau | 28:44 | 29000 | https://www.youtube.com/watch?v=Bs41dR_Kf-0 |
| 628 | 2023-10 | BackEnd Programming: 4 Ways to Improve Query Performance When Order Databases Get Too Large! | 21:25 | 9300 | https://www.youtube.com/watch?v=3vOiXwI4AVQ |
| 636 | 2022-10 | If you use MySQL to design the Products model, my colleague has found this method to be as effect... | 17:45 | 12000 | https://www.youtube.com/watch?v=qblPthhsqR4 |
| 665 | 2022-10 | Design 4 models mongodb quan trọng orders, carts, products, inventories trong System eCommerce P - 5 | 20:35 | 8200 | https://www.youtube.com/watch?v=tMAe893baIs |
| 675 | 2022-10 | Statics methods virtual in mongoose - node.js \|  eCommerce ALICONCON \| Hooks in Mongoose | 15:35 | 4300 | https://www.youtube.com/watch?v=xEh1ggoU8zI |
| 677 | 2022-10 | Bucket Pattern Mongodb -  Cách phân trang và tìm hiểu ưu và nhược của mô hình này \| Phù hợp với IoT | 42:00 | 7000 | https://www.youtube.com/watch?v=4DwqZPTtUpE |
| 678 | 2022-10 | Understand atomic in mongodb and see in practice how to use findOneAndUpdate which is a prerequis... | 24:20 | 6600 | https://www.youtube.com/watch?v=EVACo8bfU48 |
| 680 | 2022-10 | Học Mongodb quan trọng nhất là bài học này \| MongoDB Schema Design Best Practices \| Nodejs Tutorial | 29:18 | 42000 | https://www.youtube.com/watch?v=yXbz-DRvFRk |
| 681 | 2022-10 | E2E là gì? Vì sao ZALO lại nâng cấp \| Cách triển khai thuật toán trong NODE.JS vs MONGODB | 24:31 | 6800 | https://www.youtube.com/watch?v=Q4jR42L9UlA |
| 694 | 2022-10 | PassportJS là gì? Cách xác thực API thông qua nodejs mongoose và expressjs \| node js tutorial | 50:23 | 9600 | https://www.youtube.com/watch?v=KMtPfRYWmjU |
| 695 | 2022-10 | Stackoverflow CLONE \|\| Website built using MySQL, Express, React, Node, Sequelize | 1:22 | 1000 | https://www.youtube.com/watch?v=pizW1-xacBE |
| 697 | 2022-10 | How effective is Populate in Mongoose? Explained with an example | 25:43 | 8500 | https://www.youtube.com/watch?v=IZlfBvp75zI |
| 700 | 2022-10 | CreatePool: How to connect MySQL and Node.js 3x faster than the standard createConnection method | 26:38 | 11000 | https://www.youtube.com/watch?v=vjHWkHm4cqo |
| 701 | 2022-10 | Install mysql docker this article is just a premise for BACKEND PRO \| nodejs performance best pra... | 13:08 | 8100 | https://www.youtube.com/watch?v=BwEIMkQMui4 |
| 729 | 2021-10 | Connecting mongoose và create users model chuẩn và hiện đại \| Series Social Media REST API (4) | 17:42 | 3200 | https://www.youtube.com/watch?v=eQxboSVmM6U |
| 731 | 2021-10 | Khởi tạo và install những middleware cần thiết \| Series Social Media REST API \| Node.js Mongodb (2) | 25:09 | 5400 | https://www.youtube.com/watch?v=iYf9YVJERxU |
| 752 | 2021-10 | User Registration Mongodb with Node.js Express (3) \| Node and express course \| ANONYSTICK | 16:11 | 4400 | https://www.youtube.com/watch?v=JJirK21iaf8 |
| 753 | 2021-10 | Connect and create model using mongoose in Node.js (2) \| Node and express course \| ANONYSTICK | 9:33 | 4300 | https://www.youtube.com/watch?v=YVY0qLLz5Qk |
| 771 | 2021-10 | Install mongodb docker WITH 5 mins | 4:15 | 1600 | https://www.youtube.com/watch?v=APrTeibWidw |
| 773 | 2021-10 | Install elasticsearch and kibana using docker compose | 3:17 | 1100 | https://www.youtube.com/watch?v=ktGj1Swi0w8 |
| 774 | 2021-10 | Setup replica set mongodb in 3 mins | 5:58 | 3800 | https://www.youtube.com/watch?v=p8CZ2H5rt8U |
| 775 | 2021-10 | Uninstall mongodb mac brew | 3:00 | 4500 | https://www.youtube.com/watch?v=tlfixElrlcM |
| 778 | 2021-10 | How to backup MongoDb on Linux | 4:05 | 5200 | https://www.youtube.com/watch?v=76Q7rEnfzRU |
| 783 | 2020-10 | Part 4: Tạo chức năng login và register sử dụng nodejs, expressjs, mongodb | 1:04 | 9300 | https://www.youtube.com/watch?v=x66LimqLa-g |
| 784 | 2020-10 | part 3 - Setup project using nodejs, expressjs, mongodb | 0:28 | 16000 | https://www.youtube.com/watch?v=Dpl8p2nyffw |

<a id="sd"></a>
## 7. System design, architecture & interviews

| # | Upload (approx.) | Title | Duration | Views | Link |
|---|---|---|---|---|---|
| 4 | 2026-09 | System Design Interview: Essential Study Guide \| Tips Before You Start (Get the Guide in the Desc... | 11:21 | ? | https://www.youtube.com/watch?v=iDiAj-7Sqw0 |
| 5 | 2026-09 | System Design Interview: Eliminating 80% of surrounding backend developers isn't as hard as you t... | 11:21 | 17000 | https://www.youtube.com/watch?v=95vD_r9hsY0 |
| 11 | 2026-08 | System Design: How Big Tech Automatically Cancels Orders After 15 Minutes? 3 Methods, I Chose Met... | 10:57 | 3500 | https://www.youtube.com/watch?v=3OK0bYhayXI |
| 15 | 2026-07 | GO DDD Source Code: SaaS \| System Management \| How to run() | 2:32 | ? | https://www.youtube.com/watch?v=zvElcHduPw8 |
| 16 | 2026-07 | I have no experience, is there a way to pass interviews? Yes, this video is for you... | 20:13 | 3400 | https://www.youtube.com/watch?v=IWeb4Gkvx1I |
| 18 | 2026-07 | Tôi phát hiện vì sao tôi gửi một đống CV mà không nhận được lời phỏng vấn nào? Mặc dù rất tự tin... | 12:06 | 4600 | https://www.youtube.com/watch?v=BAC6xTit6NY |
| 29 | 2026-05 | JAVA DDD (30): Cancel Order là quá trình ngược lại với việc PlaceOrder nhưng nó phức tạp hơn... | 20:58 | ? | https://www.youtube.com/watch?v=ZXSCqkFpa_g |
| 32 | 2026-05 | INTERVIEWER ASK (3): Vẽ được sơ đồ này, bạn đã chứng minh được năng lực làm việc thực tế của một BE | 7:08 | ? | https://www.youtube.com/watch?v=BYw5wb8sKyA |
| 33 | 2026-05 | Build hệ thống bán vé với FULLSTACK: JAVA DDD Backend vs React Vite Frontend chịu tải 30.000 Req/S | 1:07 | 3700 | https://www.youtube.com/watch?v=NJmRdgftBTA |
| 34 | 2026-04 | JAVA DDD (29): Scale Order, when "Big Data" but queries are FAST? How should vetautet implement it? | 15:56 | ? | https://www.youtube.com/watch?v=xOUFOXwGdfo |
| 37 | 2026-04 | INTERVIEWER ASK (1): Dữ liệu đã được mã hoá và lưu trữ, làm thế nào client có thể tìm kiếm nhanh. | 27:29 | ? | https://www.youtube.com/watch?v=T55PVOAKNbI |
| 39 | 2026-04 | JAVA DDD (28): Thực sự dự án Senior được code, build, run bởi những vũ khí hạng nặng thế nào? | 19:37 | ? | https://www.youtube.com/watch?v=0r0F_u3Lrlo |
| 53 | 2026-01 | Ecommerce Microservices (48): Gateway Service \| Security OneToken \| Time to delete RefreshToken \| 03 | 22:05 | ? | https://www.youtube.com/watch?v=zKv3c4Aiu5I |
| 55 | 2026-01 | Ecommerce Microservices NestJS (47): Gateway Service \| Security JTW \| 02 | 8:27 | ? | https://www.youtube.com/watch?v=3Mc3HNiFywc |
| 58 | 2025-12 | Ecommerce Microservices NestJS (46): Gateway Service \| Security 01 | 19:53 | ? | https://www.youtube.com/watch?v=1YJdusUzLF0 |
| 60 | 2025-12 | YouTube's data structure, GitHub helped me 'flex' in my Senior interview \| Bloom Filters | 10:46 | 11000 | https://www.youtube.com/watch?v=z2WsQIlS9gc |
| 61 | 2025-12 | Ecommerce Microservices NestJS (44): Sourcecode trybuy \| order, payment, user, product, chat | 17:25 | ? | https://www.youtube.com/watch?v=tAFMP5-TbcA |
| 65 | 2025-11 | Senior Backend: How did my colleague prepare for the second round of interviews after failing the... | 14:21 | 5700 | https://www.youtube.com/watch?v=u5smNti5cwE |
| 68 | 2025-11 | Why do people with good programming skills often fail interviews? Looking for a Remote Senior... | 12:07 | 131000 | https://www.youtube.com/watch?v=OhBPuI1ylhY |
| 76 | 2025-10 | NestJS (39)  \| Microservices: Authenticate Multiple Service | 23:16 | ? | https://www.youtube.com/watch?v=_bwRXZx0Fk4 |
| 82 | 2025-10 | NestJS (38): Microservice System \| To manage secure Config Files, use Etcd, K8s | 10:45 | ? | https://www.youtube.com/watch?v=7Dide2Cw3PQ |
| 85 | 2025-10 | NestJS (37): Microservice System \| Git Code Management and What to Do When Multiple Services Are ... | 15:58 | ? | https://www.youtube.com/watch?v=AE9CTCbrG2w |
| 87 | 2025-10 | NestJS (36): Microservice System \| How to split Monolith into Microservice? TCP or GRPC communica... | 21:52 | ? | https://www.youtube.com/watch?v=2JsWOsEGgBs |
| 106 | 2025-10 | Rate Limiter System Design: Token Bucket, Leaky Bucket \| It's simple but very effective, right? | 9:18 | 4000 | https://www.youtube.com/watch?v=4LcRTajOUs0 |
| 121 | 2025-10 | Solution Architecture: How to OPTIMIZE CHAT GROUP Messages data with 10,000 members in the Group? | 25:17 | 4800 | https://www.youtube.com/watch?v=tJMd2rNkt0M |
| 125 | 2025-10 | System Design Interview: Part 2 - HOT SEAT REPORT with 15 questions about BACKEND vs SYSTEM... | 11:03 | ? | https://www.youtube.com/watch?v=091fhIvj23g |
| 126 | 2025-10 | System Design Interview: TƯỜNG THUẬT NGỒI GHẾ NÓNG với 15 câu hỏi về BACKEND vs SYSTEM.. | 13:47 | ? | https://www.youtube.com/watch?v=snyL0mdkqKo |
| 133 | 2025-10 | GO FRESHER (28): Refactoring CODE from MVC to DDD Project (Source MVC - FEAT) | 14:22 | ? | https://www.youtube.com/watch?v=e-5S8t5mKoc |
| 135 | 2025-10 | NestJS (16): Scale App Microservice using PM2 | 23:56 | ? | https://www.youtube.com/watch?v=ZV7Bxfo7l0Y |
| 137 | 2025-10 | JAVA DDD (27): CORRECT Formula When Configuring Thread Based on CPU Cores - Video Worthy of $1000 | 19:41 | ? | https://www.youtube.com/watch?v=Z0sHzUhjFjI |
| 139 | 2025-10 | HOT - CHÍNH THỨC: Cơ hội làm REMOTE nhiều hơn khi PHỎNG VẤN TIẾNG ANH sẽ không còn như trước! TUYỆT | 9:25 | 8800 | https://www.youtube.com/watch?v=uuX3zCCr1-8 |
| 158 | 2025-10 | JAVA DDD Source Code ~ 30,000 QPS: Ticket Sales System Video Section 17 - 26 How to run() | 7:34 | ? | https://www.youtube.com/watch?v=WSVFQ24mGac |
| 179 | 2025-10 | GO Interview: Phỏng vấn 1 ??? là gì và cách fix ??? thế nào trong Uber? | 8:35 | ? | https://www.youtube.com/watch?v=edtCrXCcO8c |
| 187 | 2025-10 | JAVA DDD 23: How Seniors can store data for vetautet efficiently and with good performance. | 14:26 | ? | https://www.youtube.com/watch?v=UKL0x9jijak |
| 192 | 2025-10 | GO SENIOR (4): The precise method to ACCELERATE API performance to 30,000 req/second with a small... | 14:50 | ? | https://www.youtube.com/watch?v=vB5Ch-dNHbQ |
| 193 | 2025-10 | JAVA DDD 22: Luận bàn về 100 trung tâm bán 5000 ticket mỗi ngày và việc chia dữ liệu Order | 10:05 | ? | https://www.youtube.com/watch?v=jrs2zlyC3Pc |
| 213 | 2025-10 | I got an SA (Solution Architect) interview: Estimate a server for 30 billion requests. Why do SAs... | 27:13 | 9600 | https://www.youtube.com/watch?v=G9_9Wj_01RM |
| 222 | 2025-10 | JAVA DDD Source Code ~ 15,000 QPS: Selling Tickets From Video Section 5-17 How to run() | 3:28 | ? | https://www.youtube.com/watch?v=_4KTlUvdXoM |
| 223 | 2025-10 | TIPS nhảy việc: Đã kinh qua DDD và Microservice, nhưng vẫn thất bại với câu hỏi phỏng vấn thế này? | 6:37 | 9400 | https://www.youtube.com/watch?v=op2eUV20Ggg |
| 225 | 2025-10 | NVIDIA Phỏng vấn Intern KHÓ thế này? Tiết lộ ask interview và giải pháp vượt qua như thế này... | 6:12 | 11000 | https://www.youtube.com/watch?v=CR4yiNTSEKg |
| 231 | 2025-10 | NVIDIA Interview: Tips use Docker và Kubernetes để triển khai quá trình triển khai dự án từ 0 đến 1? | 43:19 | 6300 | https://www.youtube.com/watch?v=wuyak_clfmU |
| 238 | 2025-10 | Like a Senior: Service Authentication in Microservices \| Eureka and Java Spring Boot | 18:55 | 11000 | https://www.youtube.com/watch?v=rR9AUwEk4OA |
| 243 | 2025-10 | JAVA DDD 12: Không những 20.000 mà là 25.000 req/s chúng tôi nhận thưởng | 23:36 | ? | https://www.youtube.com/watch?v=akl14joFf2A |
| 245 | 2025-10 | JAVA DDD 11: Họp TEAM vũ khí cho việc tăng tốc 20.000 req/s phải đạt 5 tiêu chí sau. DDD - Project | 10:44 | ? | https://www.youtube.com/watch?v=gv_XHpOigbk |
| 247 | 2025-10 | How Intern Beats Senior Interviewer? Real Interview Scenarios and Answers | 21:42 | 33000 | https://www.youtube.com/watch?v=Xp92z9DeGf4 |
| 249 | 2025-10 | JAVA DDD Source Code ~ 5.000 QPS: Bán Vé Từ Video Section 4 - 10 vs How to run() | 2:00 | ? | https://www.youtube.com/watch?v=zoZu10avosY |
| 257 | 2025-10 | JAVA DDD 08: Big Brother Graphana - System Monitoring - Helps DEV Sleep Well | 9:45 | ? | https://www.youtube.com/watch?v=NSpHw9tUFjs |
| 258 | 2025-10 | JAVA DDD 07: Setup hệ thống giám sát API Prometheus Service giúp DEV ngủ ngon | 19:07 | ? | https://www.youtube.com/watch?v=MGQrPOrtKhE |
| 259 | 2025-10 | How to Scale API Handling from 6,000 to 20,000 req/s Thanks to the BOSS's Email (Without Using Re... | 7:35 | 6100 | https://www.youtube.com/watch?v=agO2UhMX6pk |
| 265 | 2025-10 | JAVA DDD Source Code ~ 1.000 QPS: DDD Project - Bán Vé Từ Video 0 - 4 - How to run() | 3:21 | ? | https://www.youtube.com/watch?v=nXmppGlu4hw |
| 266 | 2025-10 | JAVA DDD 04:  Circuit Breaker vs RateLimiter - Tuyến phòng thủ đầu tiên cho DDD (bán vé trực tuyến) | 27:27 | ? | https://www.youtube.com/watch?v=tK7NDEr_vtE |
| 269 | 2025-10 | JAVA DDD 3: Complete SETUP Project according to Microservice architecture | 24:27 | ? | https://www.youtube.com/watch?v=IcDiMkb7_TA |
| 271 | 2025-10 | JAVA DDD 02: BÁN VÉ TÀU TẾT với DDD Structure Project - Phần 02 | 15:19 | ? | https://www.youtube.com/watch?v=hux9dtGQL7w |
| 272 | 2025-10 | JAVA DDD 01: HOW TO BUILD A DDD DEPLOYMENT PROJECT FOR SELLING TRAIN TICKETS AND MUSIC WITH HIGH-... | 14:12 | 32000 | https://www.youtube.com/watch?v=WFlIoNHD_Yo |
| 274 | 2025-10 | PHỎNG VẤN BE 03: Hệ thống bán vé đã xây dựng gửi 1.000.000 emails thế nào? Tỷ lệ lỗi được kiểm soát? | 14:43 | 8100 | https://www.youtube.com/watch?v=Lx-Okh4Z0us |
| 276 | 2025-10 | JAVA Fresher 17: Xác minh quyền RBAC - Chèn Phỏng vấn Backend | 19:54 | ? | https://www.youtube.com/watch?v=bFp_D9r0NVc |
| 278 | 2025-10 | BACKEND INTERVIEW 02: How to optimize a system for sending millions of emails? Junior level... | 6:11 | 8100 | https://www.youtube.com/watch?v=oOPuYa9PgEM |
| 301 | 2024-10 | GO Backend (05): Working with Microservices, Go OTP Handler, Java Sending OTP to AWS | 11:35 | ? | https://www.youtube.com/watch?v=z6FN492XwDw |
| 335 | 2024-10 | Cách sử dụng gRPC: Triển khai Order Service Go, Java! Độ trễ gần như KHÔNG CÓ \| Từng bước... | 16:06 | 6200 | https://www.youtube.com/watch?v=x5ZVWiJIuSM |
| 340 | 2024-10 | Từ MÔNG LUNG tới Back-End vs Front-End Developer tiết kiệm THỜI GIAN (Kiến trúc và Source) | 10:29 | 16000 | https://www.youtube.com/watch?v=SThv5ApvD8M |
| 369 | 2024-10 | SOLID: Open Closes Principle OCP - Mức độ khó (★★★☆☆) \| Mức độ phổ biến (★★★★★) \| Nguyên tắc (2) | 12:12 | 10000 | https://www.youtube.com/watch?v=Pbpq4Re1REQ |
| 370 | 2024-10 | gRPC vs Rest API When? Where? See colleague explain | 9:56 | 19000 | https://www.youtube.com/watch?v=n2GI_4Rbzwg |
| 371 | 2024-10 | DESIGN PATTERN vs SOLID: What's the difference? Which should I learn first? I'm anti-S in SOLID. | 20:12 | 23000 | https://www.youtube.com/watch?v=OYACAk1QqLE |
| 377 | 2024-10 | Phỏng vấn về Hash thành công - Giúp Lập Trình Viên được trả lương cao | 19:03 | 12000 | https://www.youtube.com/watch?v=D6-xKguNpWg |
| 382 | 2024-10 | Phỏng vấn BackEnd: Trong LINUX chúng ta nên lo lắng về MỨC TẢI TRUNG BÌNH của hệ thống (2) | 13:06 | 10000 | https://www.youtube.com/watch?v=3JdFrh1ZvRA |
| 383 | 2024-10 | BackEnd Interview: Now I Understand Synchronous and Asynchronous Through a Reality-Based Question #1 | 13:33 | 45000 | https://www.youtube.com/watch?v=XM5qmMZRrjE |
| 394 | 2024-10 | Quy trình backend đăng ký Shop và các thao tác send Token Email, verify Token \| Kiến Trúc ShopDEV | 6:34 | 6400 | https://www.youtube.com/watch?v=-uz1lKVdKZ8 |
| 425 | 2024-10 | Backend architecture: How did the app grow from 0 to 14 million users in just one year? | 12:16 | 29000 | https://www.youtube.com/watch?v=4yiE_1Bts9U |
| 449 | 2023-10 | 13 Node.js Programming Interview Questions for Fresher and Intern \| Beginner Level \| Level 0, 1 | 9:47 | 16000 | https://www.youtube.com/watch?v=VvAZeHNRGJI |
| 477 | 2023-10 | Docker, Dockerfile, Docker Compose: An FE Engineer Explained EXCELLENTLY in a Senior Interview | 7:57 | 11000 | https://www.youtube.com/watch?v=NbJ45r9sbiE |
| 546 | 2023-10 | Adapter Pattern: module exports MoMo to Visa Card để đăng ký HỘI VIÊN trên YOUTUBE \| Design Patterns | 14:26 | 4800 | https://www.youtube.com/watch?v=cUNoGD7sR-g |
| 555 | 2023-10 | Bucket pattern: Bí mật trong e-Commerce hay IoT được giải quyết NHANH GỌN \| Mongdb Design Patterns | 16:02 | 4100 | https://www.youtube.com/watch?v=EXzaoPWo7sk |
| 573 | 2023-10 | How to design WEB API security for your system? \| Systems Architecture \| 23 | 12:58 | 9400 | https://www.youtube.com/watch?v=dSgXDKiLLvw |
| 574 | 2023-10 | Section 8:  Make Your API Response use class \|  Course Node.js Backend Architecture | 9:26 | ? | https://www.youtube.com/watch?v=mvMEn5ofnlQ |
| 576 | 2023-10 | Section 7: Xử lý ErrorHandler trong API \| Course Node.js Backend Architecture | 17:24 | ? | https://www.youtube.com/watch?v=hyF1S0nFS7A |
| 577 | 2023-10 | Api-gateway vs load balancing cách tối ưu hệ thống eCommerce \| Systems Architecture \| #22 | 9:06 | 15000 | https://www.youtube.com/watch?v=jUQQ7WPjqnI |
| 581 | 2023-10 | Singleton Pattern triển khai thuật toán Round-Robin trong kiến trúc load balancing \| Design Patterns | 14:51 | 10000 | https://www.youtube.com/watch?v=UybOa4xiW_c |
| 583 | 2023-10 | Load Balancers giải thích 5 thuật toán bằng hình ảnh và cùng nhau vào dự án lớn \| architecture notes | 14:20 | 4600 | https://www.youtube.com/watch?v=EINOE9z3sLE |
| 587 | 2023-10 | Kubernetes vs Docker: Hiểu trước sau đó là cách triển khai hoạt động giữa thực tế và microservices | 17:43 | 51000 | https://www.youtube.com/watch?v=gQVWGj3h1pM |
| 588 | 2023-10 | Section 2: Node.js Backend Architecture - Những folders và packages cần thiết khi khởi tạo Project! | 29:22 | ? | https://www.youtube.com/watch?v=qpIfPitAIX0 |
| 590 | 2023-10 | Course: Node.js Backend Architecture - Project introduction, experience, skills and confidences C... | 25:11 | ? | https://www.youtube.com/watch?v=5keK7PRH9pE |
| 592 | 2023-10 | Factory Method Pattern - Why is it so popular but easy to learn \| Design Patterns \| (6) | 11:21 | 12000 | https://www.youtube.com/watch?v=54-rJHUM2L8 |
| 594 | 2023-10 | (6) The Essential Backend API Key for Routers \| Build Node.js Backend Architecture PRO | 12:56 | ? | https://www.youtube.com/watch?v=rdAYZKiwnQk |
| 598 | 2023-10 | (3) Build Node.js Backend Architecture PRO: Vì sao Router phải được triển khai bởi LEADER thực hành | 13:44 | 5100 | https://www.youtube.com/watch?v=FxpXlZz-dh8 |
| 608 | 2023-10 | Kiến trúc quy trình ủy quyền đăng nhập (auth) \| Schema and comments (replies) \| Video 30 seconds | 0:44 | 1900 | https://www.youtube.com/watch?v=rejhP-hKnKc |
| 616 | 2023-10 | Hệ thống BackEnd tắc nghẽn ở giờ CAO ĐIỂM Tôi dựa vào công thức tính QPS và bài toán định luật 80/20 | 18:59 | 6600 | https://www.youtube.com/watch?v=uZhe6O_JXM8 |
| 618 | 2023-10 | Applying SOLID principles to eCommerce projects \| What is the S here? \| Part 1 \| SOLID Javascript... | 22:34 | 12000 | https://www.youtube.com/watch?v=a0wDsf9YjSw |
| 620 | 2023-10 | Khi Lập Trình Viên phỏng vấn Designer tương lai \| Funny Dev - Videos | 2:20 | 1600 | https://www.youtube.com/watch?v=VLquzZ3hPqQ |
| 627 | 2023-10 | Developer Interview Series (3) Token (jwt) sinh ra thay cho Session với tình huống nào??Gợi ý 3 cách | 15:47 | 16000 | https://www.youtube.com/watch?v=yv9vCIhfZEk |
| 629 | 2023-10 | Developer Interview (2): Cookie vs Session, time to clarify the relationship with SessionID | 15:03 | 24000 | https://www.youtube.com/watch?v=noxqc_CpVLQ |
| 631 | 2023-10 | Developer Interview Series: Backend (1) Forward Proxy vs Reverse Proxy Trăm nghe không bằng một thấy | 1:21 | 3200 | https://www.youtube.com/watch?v=zdOVvu3RGOo |
| 646 | 2022-10 | The BACKEND Developer roadmap I committed to after seeing this system architecture - 01 | 19:54 | 49000 | https://www.youtube.com/watch?v=M4AFU8CNtk4 |
| 653 | 2022-10 | Strategy Pattern: Level 1 vs. Level 4 Usage \| From Rome's Strategy to Shopee \| Design Patterns | 12:37 | 31000 | https://www.youtube.com/watch?v=sheV2IBlQkU |
| 654 | 2022-10 | DESIGN PATTERNS \| Bạn có dám chắc trả lời được 5 Câu hỏi này không? \| Hướng dẫn cách học 23 patterns | 14:50 | 48000 | https://www.youtube.com/watch?v=l84-JRQ95V4 |
| 670 | 2022-10 | Popular interview question: What is the difference between Process and Thread? 10 seconds a day | 0:25 | 4200 | https://www.youtube.com/watch?v=0bvwcq_W4gg |
| 674 | 2022-10 | Điều gì xảy ra khi User nhập một Url \| Phỏng vấn Backend | 0:23 | 3400 | https://www.youtube.com/watch?v=mD7tf2a8mug |

<a id="go"></a>
## 8. Go (Golang)

| # | Upload (approx.) | Title | Duration | Views | Link |
|---|---|---|---|---|---|
| 10 | 2026-08 | The Path to Becoming a Backend Developer (256) \| Deep Understanding and Examples of CONTEXT in Go... | 4:10 | ? | https://www.youtube.com/watch?v=jdvIhlEZ38w |
| 28 | 2026-05 | GO SENIOR (09): Những bài học đắt giá khi Refactor và nâng cấp một hệ thống đang chạy production | 18:15 | ? | https://www.youtube.com/watch?v=l6amtaNBKWU |
| 41 | 2026-04 | GO Fresher (16): Interface Why I Always Recommend Implementing Large Projects \| NOCODE | 9:53 | ? | https://www.youtube.com/watch?v=LjFa5hXooeM |
| 48 | 2026-02 | LẬP TRÌNH GO CHO NGƯỜI MỚI (or JAVA to GO) \| Intern - Fresher - Junior - Senior \| Lộ trình này là đủ | 16:54 | 4100 | https://www.youtube.com/watch?v=frT-R9hc42Q |
| 127 | 2025-10 | Thực hành vì sao WhatsApp user LOGIN với việc đồng bộ List Friends, Groups cấp triệu rất NHANH | 14:52 | 3200 | https://www.youtube.com/watch?v=d7j_ErLsNqg |
| 129 | 2025-10 | Panic Recover Defer - The magic that GO has for Programmers if they know how to handle ERROR | 12:31 | ? | https://www.youtube.com/watch?v=IW-3UGz3h7c |
| 134 | 2025-10 | GO Fresher(27): I Built 3 Project Structures to Go From Fresher to Senior. Sharing Them With You All | 14:22 | ? | https://www.youtube.com/watch?v=dYeS4LmT1Q0 |
| 145 | 2025-10 | GO Fresher (26): Implementing Crontab system (System Scheduler) to fix and increase HIGH performance | 19:41 | ? | https://www.youtube.com/watch?v=NL2_YsnqPGQ |
| 160 | 2025-10 | GO SENIOR (08): Request Validation với Struct — Best Practice cho Backend Developer | 5:35 | ? | https://www.youtube.com/watch?v=30Slk-sq8Ys |
| 161 | 2025-10 | GO intern (04): Security - Validator API REQUEST việc không riêng của FE | 6:06 | ? | https://www.youtube.com/watch?v=Pa_fKmcaCXg |
| 165 | 2025-10 | GO Intern (03): Vì sao Context đáng giá NHẤT trong GO? Khi nào dùng Background() vs TODO() | 13:01 | ? | https://www.youtube.com/watch?v=2KyRvQP728U |
| 170 | 2025-10 | NestJS (07): Api Backend vé tàu tết: User Registration và User Login | 32:12 | ? | https://www.youtube.com/watch?v=VJYRI_gEylg |
| 182 | 2025-10 | GO Intern (01): When talking about GO, start with STRUCT | 7:18 | ? | https://www.youtube.com/watch?v=CgbMzPudXX4 |
| 203 | 2025-10 | SOURCE GO API [25/02/2025]: How to run project? | 3:39 | ? | https://www.youtube.com/watch?v=g__VyA7RelA |
| 233 | 2025-10 | Virtual Threads JAVA: Can the Big Brother Surpass Goroutine Go? x16 times? This example is enough... | 17:44 | 7600 | https://www.youtube.com/watch?v=aUybpn3T4hg |
| 234 | 2025-10 | 2025: Vị trí HOT (BE, FS) GO trả lương cao nhất và 4 ngôn ngữ lập trình năm 2025 tại Việt Nam | 12:03 | 16000 | https://www.youtube.com/watch?v=w33dg6EoWl0 |
| 237 | 2025-10 | GO Fresher (23): Master the channel and quickly deploy publishers vs subscribers | 19:29 | ? | https://www.youtube.com/watch?v=QdIB0pjXhLw |
| 244 | 2025-10 | GO Backend (21): Traffic Request thời gian thực với Prometheus và Grafana Phần 2 | 8:50 | ? | https://www.youtube.com/watch?v=q1ojLhNxWes |
| 248 | 2025-10 | GO Backend (20): Triển khai giám sát thời gian thực với Prometheus và Grafana Request Traffic | 16:00 | ? | https://www.youtube.com/watch?v=E9-48WT6ix8 |
| 260 | 2025-10 | GO Backend (18): User setup two-factor VerifyOTPAuthentication vs Login two-factor | 17:31 | ? | https://www.youtube.com/watch?v=FmWrAPrBZkA |
| 263 | 2025-10 | GO Backend (17): User setup two-factor authentication | 28:17 | ? | https://www.youtube.com/watch?v=KD4aN-XiXos |
| 268 | 2025-10 | GO Backend (16): Two Factor Authentication - Implement vs Service | 19:12 | ? | https://www.youtube.com/watch?v=vzGmZYAOYg4 |
| 273 | 2025-10 | GO Backend (15): Two Factor Authentication - Interface vs SQLC | 18:58 | ? | https://www.youtube.com/watch?v=-Uuu4AX4SP0 |
| 275 | 2025-10 | GO Backend (14): GENERATE TOKEN LOGIN - JWT AUTHENTICATION | 13:43 | ? | https://www.youtube.com/watch?v=YbK2cCtjjBY |
| 277 | 2025-10 | GO Backend (13): LOGIN USER - JWT AUTHENTICATION | 16:30 | ? | https://www.youtube.com/watch?v=CbLYtz4cwLk |
| 282 | 2024-10 | GO Backend (12): Update Password Register | 29:26 | ? | https://www.youtube.com/watch?v=elrgdNIAQEg |
| 285 | 2024-10 | GO Backend (11): VerifyOTP() method when User REGISTERS successfully | 14:00 | ? | https://www.youtube.com/watch?v=GUViVHAxodc |
| 287 | 2024-10 | GO Backend (10): Tích hợp API SWAGGER DOCUMENTATION | 46:23 | ? | https://www.youtube.com/watch?v=luVb_lvHrKo |
| 289 | 2024-10 | GO Backend (09): Implement IUserLogin - Register, CheckOTP, Login (token), UpdatePassRegister | 31:30 | ? | https://www.youtube.com/watch?v=iYwOZIy2Dno |
| 291 | 2024-10 | GO Backend (08) - Đến lúc trở thành Senior làm việc với  Diagrams Authentication và sử dụng Makefile | 20:44 | ? | https://www.youtube.com/watch?v=wSdaJ0Oyt8k |
| 292 | 2024-10 | GO Backend (07): REFACTOR BROTHERS restructure the project interface after seeing a colleague's CODE | 29:16 | ? | https://www.youtube.com/watch?v=5UVx7TITbXM |
| 296 | 2024-10 | JAVA Fresher 10: Send OTP Email Spring With SMTP AWS, GO PUSH OTP | 23:17 | ? | https://www.youtube.com/watch?v=iSRRM5exThE |
| 305 | 2024-10 | GO Backend (04): The GORM boss replaces the GOOSE vs SQLC rookie system, making it powerful. | 15:32 | ? | https://www.youtube.com/watch?v=RLaZs_upIns |
| 307 | 2024-10 | GO Backend (03): User Register Send OTP To Email Template | 53:06 | ? | https://www.youtube.com/watch?v=qe5-Q0psiYM |
| 317 | 2024-10 | GO Fresher (21) :Chiến đấu với Docker Link, Docker Compose build Project | 20:59 | ? | https://www.youtube.com/watch?v=gBdQgm5tzQ4 |
| 318 | 2024-10 | Go Fresher (20): Chiến đấu DOCKER, sai lầm cách build này Level 0, 1 | 12:56 | ? | https://www.youtube.com/watch?v=Ng_g2KdXwqU |
| 320 | 2024-10 | Trying out 100 million with goroutine go, Java threads, and Node.js eventloop on my NEW M3 phone :v | 16:44 | 9000 | https://www.youtube.com/watch?v=rZ2shLV6BqI |
| 321 | 2024-10 | GO Fresher (18): Wire Dependency Injection | 14:49 | ? | https://www.youtube.com/watch?v=Yc9XnmUvsc4 |
| 323 | 2024-10 | GO Fresher (17): Interface Cách triển khai và bố trí CODE \| THỰC HÀNH | 19:24 | ? | https://www.youtube.com/watch?v=3HArGaE0Sbs |
| 329 | 2024-10 | GO Fresher (14): Triển khai Router cho TEAM LỚN \| Cuộc chiến bắt đầu | 21:45 | ? | https://www.youtube.com/watch?v=WLwSdpVB6ts |
| 338 | 2024-10 | GO Fresher (11): Using Lumberjack to manage LARGE LOG FILES | 19:18 | ? | https://www.youtube.com/watch?v=xTjwb6VhEx0 |
| 339 | 2024-10 | Java, Go, NodeJS: NẾU chọn lại TÔI sẽ không LÃNG PHÍ thời gian chọn SAI ngôn ngữ | 15:23 | 39000 | https://www.youtube.com/watch?v=KeiFxYXRTh0 |
| 342 | 2024-10 | GO Fresher (10):  FIX func Main để tạo nhóm kết nối chung (Initialize) | 17:23 | ? | https://www.youtube.com/watch?v=mQMCRFrIO9M |
| 344 | 2024-10 | GO Fresher (09):  Unit test Service | 16:22 | ? | https://www.youtube.com/watch?v=6mlM-les3YI |
| 346 | 2024-10 | GO Fresher (8): GIN vs 5 types of Middleware | 14:59 | ? | https://www.youtube.com/watch?v=fMTeKC617KM |
| 347 | 2024-10 | GO Fresher (7): GIN vs Viper Config YAML | 18:12 | ? | https://www.youtube.com/watch?v=G0YRksaHOFU |
| 349 | 2024-10 | GO FRESHER TIPS: TOOLS TỐT NHẤT khởi tạo dự án trong vòng 3 giây (NÊN DÙNG) | 7:59 | 8100 | https://www.youtube.com/watch?v=m4f_b9PNwT8 |
| 350 | 2024-10 | GO Fresher (6): GIN vs Logs Handler ZAP | 22:33 | ? | https://www.youtube.com/watch?v=vqf-2StTn0Q |
| 353 | 2024-10 | GO Fresher (5): GIN vs Error Handler | 13:21 | ? | https://www.youtube.com/watch?v=dhj4MqYqpqU |
| 358 | 2024-10 | GO Fresher (4): GIN and the MVC Pattern | 13:34 | ? | https://www.youtube.com/watch?v=uOwcqwC4Ni8 |
| 359 | 2024-10 | GO FRESHER INTRO: Nói về Golang để xem nhân viên GOOGLE nói gì? | 10:03 | 28000 | https://www.youtube.com/watch?v=oUvTfcMSbqw |
| 361 | 2024-10 | GO Fresher (03): GIN vs ROUTER | 17:28 | ? | https://www.youtube.com/watch?v=EF8Sp03O_sk |
| 362 | 2024-10 | GO Fresher (02): Setup Backend Project | 14:23 | ? | https://www.youtube.com/watch?v=x5-YICJ9YyY |
| 364 | 2024-10 | GO Fresher (01): Giới thiệu những cấu trúc dự án Backend Project Structure | 9:23 | ? | https://www.youtube.com/watch?v=L_kqWi7U2E0 |
| 441 | 2024-10 | Go và CON ĐƯỜNG lập trình toàn diện cho nhiều level khác nhau (1) \| Series Golang \| Source vs Book | 16:52 | 17000 | https://www.youtube.com/watch?v=80vgCpHXs98 |
| 506 | 2023-10 | Speaking of SALARY, how about Node.js and Go? Is this a quick way to switch from NODE.JS to GOLANG? | 10:19 | 14000 | https://www.youtube.com/watch?v=c4Sn3vGyfhw |
| 572 | 2023-10 | Section 9: Login Shop Api \| Course Node.js Backend eCommerce | 23:07 | ? | https://www.youtube.com/watch?v=0O1PlClhmIc |
| 709 | 2022-10 | Nhận AccessToken mới khi Token hết hạn mà người dùng không cần login lại như Facebook \| Axios API | 42:55 | 24000 | https://www.youtube.com/watch?v=7fKjiBcBj3E |
| 749 | 2021-10 | Loggin Users with bcrypt Node.js (6) \| Node and express course \| ANONYSTICK | 10:16 | 2900 | https://www.youtube.com/watch?v=lY8inZOeQhw |

<a id="java"></a>
## 9. Java & Spring Boot

| # | Upload (approx.) | Title | Duration | Views | Link |
|---|---|---|---|---|---|
| 3 | 2026-09 | Java Excel \| Why our team switched from EasyExcel to Apache POI (Real Data) \| Spring | 10:41 | 5300 | https://www.youtube.com/watch?v=g8tolSSWe3c |
| 50 | 2026-01 | HOW TO LEARN JAVA FOR BEGINNERS (or CAREER CHANGERS) - Don't digress — Please focus on these aspe... | 14:49 | 7900 | https://www.youtube.com/watch?v=bpHYSYBuqyU |
| 81 | 2025-10 | Spring Boot vs NestJS: Không nên kết hợp DTO vs Entity \| Tôi chọn NestJS nói về DTO hơn MapStruct | 12:12 | 7200 | https://www.youtube.com/watch?v=sgMGwdP5pdM |
| 96 | 2025-10 | JAVA Fresher (23): Improve CPU performance, THREAD not for Fresher | 21:23 | ? | https://www.youtube.com/watch?v=31pkSHg0pUc |
| 100 | 2025-10 | JAVA Fresher (22): Remember-Me Authentication - Bảo mật Token Remember #springsecurity #rbac | 14:53 | ? | https://www.youtube.com/watch?v=f__leeKpY7M |
| 102 | 2025-10 | SPRING SECURTY 6 \| FULL \| JWT, RBAC, CSRF, Persistent Token, Rememer-Me \| HackToken | 14:54 | 2400 | https://www.youtube.com/watch?v=cUV6uckeG6k |
| 105 | 2025-10 | JAVA Fresher (20): Spring Security is the easiest to understand I have ever learned, NOW I want t... | 25:49 | ? | https://www.youtube.com/watch?v=2uea3OCz_yk |
| 147 | 2025-10 | Method 2: Export Excel file with 1,000,000 rows, time reduced from 15s to 5s. Using ThreadPool | 21:53 | ? | https://www.youtube.com/watch?v=zUHKsQ3T3Hw |
| 151 | 2025-10 | JAVA Fresher (19): How to Export Excel files with 1,000,000 records and improve from 10s to 6s... | 12:22 | ? | https://www.youtube.com/watch?v=n97s7yxGLoE |
| 162 | 2025-10 | JAVA Intern (5): Virtual Thread, Platform Thread sự vĩ đại cuối cũng của JAVA JUC | 25:56 | ? | https://www.youtube.com/watch?v=cttaY3UzVws |
| 171 | 2025-10 | JAVA Intern (4): How ThreadLocal Works - Memory Leaks | 7:13 | ? | https://www.youtube.com/watch?v=qqYE9nfXqJo |
| 184 | 2025-10 | JAVA Intern (01): Vì sao dev BE lại thích sử dụng Stream() | 12:39 | ? | https://www.youtube.com/watch?v=zqf1LuYTeYo |
| 280 | 2024-10 | JAVA Fresher (16): SPRING BOOT SECURITY - SecurityFilterChain | 14:49 | ? | https://www.youtube.com/watch?v=Hpv6Q56o0-k |
| 281 | 2024-10 | JAVA Fresher 15: SPRING BOOT SECURITY - Roles vs Authorities | 12:17 | ? | https://www.youtube.com/watch?v=_mAvzmgV3ik |
| 284 | 2024-10 | JAVA Fresher 14:  SPRING BOOT SECURITY - WHO ARE YOU? | 24:55 | ? | https://www.youtube.com/watch?v=hXV2rT3dqI0 |
| 288 | 2024-10 | JAVA Fresher 13: SPRING BOOT SECURITY - 4 methods of identity authentication? | 7:06 | ? | https://www.youtube.com/watch?v=jIRyd2tjYSc |
| 293 | 2024-10 | JAVA Fresher 12: SPRING BOOT SECURITY - Toàn diện về Security dân Backend | 15:52 | ? | https://www.youtube.com/watch?v=1h7yp9ubWzQ |
| 299 | 2024-10 | JAVA Fresher 09: Spring Data JPA, working with ManyToMany | 13:35 | ? | https://www.youtube.com/watch?v=SgMbCgvs2Z8 |
| 300 | 2024-10 | JAVA Fresher 08: Spring Data JPA, working with OneToOne, OneToMany and ManyToOne | 23:05 | ? | https://www.youtube.com/watch?v=qkCRcKnvJ70 |
| 304 | 2024-10 | JAVA Fresher 06:  Controller vs Spring Data JPA | 11:07 | ? | https://www.youtube.com/watch?v=0unBab23Kok |
| 306 | 2024-10 | JAVA Fresher 05:  Spring Data JPA | 34:53 | ? | https://www.youtube.com/watch?v=EwSrtrk7Kq0 |
| 309 | 2024-10 | Java Fresher 04: Getting Started with Spring Boot Folder Structure | 21:27 | ? | https://www.youtube.com/watch?v=jnURsbcOycM |
| 310 | 2024-10 | Java Fresher 03: Kỹ năng chuyển đổi PROJECT từ DEV qua TEST, PRE, PRODUCT | 10:43 | ? | https://www.youtube.com/watch?v=z49Kb4a_cV0 |
| 311 | 2024-10 | Java Fresher 02: Configuring a project with properties, yaml, and .env priority levels | 17:50 | ? | https://www.youtube.com/watch?v=PvcIwEkUcEc |
| 312 | 2024-10 | Java Fresher 01: Install vs Start APP with VSCODE vs Intellij IDEA | 14:43 | ? | https://www.youtube.com/watch?v=BpQsIGVrmXs |
| 313 | 2024-10 | FULL JAVA: Welcome SpringBoot, the path from Basic, Fresher, Junior. Added NestJS | 15:08 | ? | https://www.youtube.com/watch?v=pNZyzE_9EPM |
| 420 | 2024-10 | canParse() - Đề xuất xác thực URL trong JavaScript mới nhất \| Tools vs Methods backend | 1:22 | 3600 | https://www.youtube.com/watch?v=5tZZe_rXM2s |
| 496 | 2023-10 | Delete a node from nested model set với thuật toán sau đây, áp dụng cho PHP, JAVA, JAVASCRIPT | 6:42 | 2900 | https://www.youtube.com/watch?v=6594tqArXkA |
| 610 | 2023-10 | Tips Javascript - Một dòng CODE CSS để thay đổi site GITHUB thành đen trắng \| Video 45 seconds | 0:47 | 1900 | https://www.youtube.com/watch?v=9uuebwAOqsY |
| 611 | 2023-10 | Tips Javascript - Tổng hợp những tính năng 80% lập trình Javascript thường được sử dụng trong DỰ ÁN | 16:11 | 8100 | https://www.youtube.com/watch?v=x2xkzvG1NDg |
| 612 | 2023-10 | ECMAScript 2022 (ES13) Những tính năng được tuyệt vời FrontEnd hay Backend cần học trong Javascript. | 19:55 | 4100 | https://www.youtube.com/watch?v=BmcGtkABKu0 |
| 650 | 2022-10 | Browser In The Browser (BITB) Attack \| Tips Javascript | 1:04 | 3900 | https://www.youtube.com/watch?v=lHSwa7pBPD4 |
| 651 | 2022-10 | Detect When Users Switch Tabs using JavaScript \| Tutorials Javascript \| SHORT VIDEOS | 0:12 | 3200 | https://www.youtube.com/watch?v=qDHyuV209Fo |
| 669 | 2022-10 | Stop sử dụng typeof trong javascript và đây là giải pháp \| JavaScript check data type | 11:28 | 7200 | https://www.youtube.com/watch?v=kPRyWBzzUJE |
| 687 | 2022-10 | Sơ lược vòng đời của Event loop callback promise async await trong Javascript qua chuyện tăng lương | 34:30 | 19000 | https://www.youtube.com/watch?v=HhWDDG52M1E |
| 706 | 2022-10 | 4 Useful VS Code Extensions for JavaScript Tips to Save Coding Time \| VS Code Extensions | 15:49 | 10000 | https://www.youtube.com/watch?v=Ujyal1dzCms |
| 708 | 2022-10 | Xem cách Senior họ hander error async await như thế nào? \| Async await javascript | 10:18 | 16000 | https://www.youtube.com/watch?v=OMpCldR3XsU |
| 717 | 2022-10 | Cách tăng tốc ỨNG DỤNG NODE.JS lên x3 với ThreadPool \| PERFORMANCE NODEJS | 10:43 | 9200 | https://www.youtube.com/watch?v=PLCrpMgaaeg |
| 721 | 2022-10 | Debounce là gì? Ngăn chặn User click liên tục vào một chức năng \| Javascript debounce example | 17:54 | 11000 | https://www.youtube.com/watch?v=Z3LUDahthQo |
| 776 | 2021-10 | fireworks javascript code | 0:43 | 984 | https://www.youtube.com/watch?v=7R73T8YKTLo |
| 777 | 2021-10 | Example autocomplete search javascript | 2:06 | 1000 | https://www.youtube.com/watch?v=sK9b5h22Fx8 |
| 779 | 2020-10 | Speech recognition api javascript Example - Anonystick.com | 3:33 | 1500 | https://www.youtube.com/watch?v=sS6iQBMaj84 |

<a id="node"></a>
## 10. Node.js / NestJS / JavaScript

| # | Upload (approx.) | Title | Duration | Views | Link |
|---|---|---|---|---|---|
| 66 | 2025-11 | Nodejs Backend(76): Resize Images with Node.js and AWS Lambda | 16:54 | ? | https://www.youtube.com/watch?v=SM8wWKieViU |
| 91 | 2025-10 | NestJS (34): How do Social platforms implement LIKE/UNLIKE? Are there many pitfalls in this appro... | 13:45 | ? | https://www.youtube.com/watch?v=git5LEvshG4 |
| 104 | 2025-10 | NestJS (29): Security RBAC the foundation of every large system: How to implement RBAC in API [AD... | 32:27 | ? | https://www.youtube.com/watch?v=jtFXbo16RmE |
| 107 | 2025-10 | NestJS (28): How to Decentralize Small and Medium-sized Systems? Implementing Tokens and ACLs | 25:21 | ? | https://www.youtube.com/watch?v=r---B8OW1fI |
| 112 | 2025-10 | NestJS (24): Prisma proficient in Schema, ApiDocs, OnetoOne, OntoMany, ManytoMany | 27:33 | ? | https://www.youtube.com/watch?v=i0R0NjmQuqI |
| 113 | 2025-10 | NestJS (23): Cơ bản đến thành thạo PRISMA. Vì sao có thế thay thế TypeORM ??? | 26:59 | ? | https://www.youtube.com/watch?v=DHsXjMlLcr8 |
| 120 | 2025-10 | NestJS (22): 5 MINUTES OF EXPERIENCE and How to integrate STANDARD TypeORM into NestJS - Should u... | 21:39 | ? | https://www.youtube.com/watch?v=XGoVsC1YLL8 |
| 122 | 2025-10 | NestJS (21): TypeORM vs Migration - Why not in development? Migration only in PROD | 18:53 | ? | https://www.youtube.com/watch?v=-muckznhxEc |
| 123 | 2025-10 | NestJS (20): TypeORM - ManyToMany. Why does this relationship always have to have an Intermediate... | 18:05 | ? | https://www.youtube.com/watch?v=y_gSwrnTTWo |
| 124 | 2025-10 | NestJS (19): TypeORM - OneToMany, ManyToOne - Người mới thường mắc 3 điều sau | 17:12 | ? | https://www.youtube.com/watch?v=UPljKC830qg |
| 128 | 2025-10 | NestJS (18): TypeORM - OneToOne - Vì sao Foreign Key ít được sử dụng với các dự án | 21:12 | ? | https://www.youtube.com/watch?v=Sdw3SLu6dZ8 |
| 131 | 2025-10 | NestJS (17): TypeORM - LÀM CHỦ KỸ NĂNG | 34:45 | ? | https://www.youtube.com/watch?v=I7lVdTBCGFk |
| 140 | 2025-10 | NestJS (15): Mẹo tối ưu Dockerfile của dự án, hãy xem kỹ về kỹ thuật này... | 16:06 | ? | https://www.youtube.com/watch?v=tVWIAfM4Tbw |
| 141 | 2025-10 | NestJS (14): Làm việc với Dockerfile đầu tiên như thế nào đối với FE qua FS và những chú ý của DEV | 13:20 | ? | https://www.youtube.com/watch?v=8uA1l5kb9e4 |
| 142 | 2025-10 | NestJS (13): FrontEnd bắt đầu hình thành FullStack với Docker Desktop, đừng đốt cháy giai đoạn... | 16:36 | ? | https://www.youtube.com/watch?v=mw1FLun0_7Q |
| 143 | 2025-10 | Node.js 24 mới RELEASE: 6 Tính Năng bạn chưa từng trải nghiệm đúng không? Dự án mới có thể sử dụng | 10:38 | 2600 | https://www.youtube.com/watch?v=p8hCqqGWBmU |
| 146 | 2025-10 | NestJS (12): Integrate Winston into API - Logger System More Powerful Than Ever \| File Search Format | 16:43 | ? | https://www.youtube.com/watch?v=akymw_jIYFk |
| 150 | 2025-10 | NestJS (11): 6 cấp độ ghi LOGs và vì sao Nodejs lại sử dụng Winston một cách mạnh mẽ về Logger | 19:14 | ? | https://www.youtube.com/watch?v=TTbaZG6e-mg |
| 153 | 2025-10 | NestJS (10): How complete is the Logger system in Nestjs? | 12:58 | ? | https://www.youtube.com/watch?v=YredrrdHJA8 |
| 155 | 2025-10 | NestJS (09): Upload Large File, FrontEnd chia nhỏ nhiều File và Backend merge file, hiệu suất cao | 46:08 | ? | https://www.youtube.com/watch?v=ScYKoRfS34c |
| 156 | 2025-10 | NestJS (08): Upload File Use Multer - DiskStorage | 17:42 | ? | https://www.youtube.com/watch?v=g4S4rmnAC5w |
| 173 | 2025-10 | NestJS (06): AOP is the core of BackEnd language proficiency mastering 5 concepts | 27:21 | ? | https://www.youtube.com/watch?v=QmGc7mt7scw |
| 183 | 2025-10 | Nest.JS (05): Use Providers | 10:12 | ? | https://www.youtube.com/watch?v=oYYzfdtZgP0 |
| 188 | 2025-10 | Nest.JS (04): How to Debug | 11:06 | ? | https://www.youtube.com/watch?v=0Tf1BPM9MwY |
| 191 | 2025-10 | Nest.JS (03): Use CLI | 15:02 | ? | https://www.youtube.com/watch?v=u5j5oQwSFs0 |
| 197 | 2025-10 | Nest.JS (02): The Power of IoC in Backend Language | 12:11 | ? | https://www.youtube.com/watch?v=8EhoEu_kYPU |
| 198 | 2025-10 | Nest.JS (01): Level Up from Front-End to Full-Stack — Why Nest.JS is the Shortest and Best Path | 12:35 | ? | https://www.youtube.com/watch?v=isgh-Pb2_bc |
| 200 | 2025-10 | ECMAScript2025: Promise được nâng cấp với try() vs tính năng từ Python được áp dụng Nodejs 2025 | 11:12 | 3100 | https://www.youtube.com/watch?v=OcvW7Vglfyg |
| 376 | 2024-10 | Section 89: Deploying Service spu and sku for optimal efficiency \| Noisy House hihi | 46:54 | ? | https://www.youtube.com/watch?v=f5pK9_A-XTk |
| 378 | 2024-10 | Section 88: Triển khai và giải thích schema spu và sku model [Tối ưu SKU] | 15:22 | ? | https://www.youtube.com/watch?v=gLo4guKxgfg |
| 381 | 2024-10 | Section 87: Senior - Data Design for SKU and SPU in Product (1) | 15:28 | ? | https://www.youtube.com/watch?v=RnhqkmHG4vE |
| 384 | 2024-10 | Section 86: User Registration \| Verify OTP vs Create New User (2) | 21:08 | ? | https://www.youtube.com/watch?v=d4Xy6MyaaCI |
| 387 | 2024-10 | Section 85: Sharing shopDEV Interface Source Code (React+Vite) and Mobile App (iOS + Android) Dow... | 9:09 | ? | https://www.youtube.com/watch?v=A-tXuWpyBss |
| 392 | 2024-10 | Section 83: Triển khai module đăng ký thành viên ShopDEV thông qua verify Email OTP | 1:07:08 | ? | https://www.youtube.com/watch?v=A78uC7AfZPU |
| 395 | 2024-10 | Section 82: Shop Registration \| Email OTP Sending and Verification Workflow via SMTP (AWS) (1) | 6:34 | ? | https://www.youtube.com/watch?v=Y-pqDc3Xl9Q |
| 397 | 2024-10 | Section 81: Hoàn thành hệ thống tracking Logs với traceId hoàn chỉnh cho level 4, 5 | 24:13 | ? | https://www.youtube.com/watch?v=bzCKJ3HorXc |
| 399 | 2024-10 | Node.js Logging: How to Write Logs Like a Pro! | 15:28 | 4300 | https://www.youtube.com/watch?v=6_DJEZ7285Q |
| 400 | 2024-10 | Section 80: Designing TRACKING LOGs in e-commerce systems \| Part 2 | 26:33 | ? | https://www.youtube.com/watch?v=8LicTFZvPzE |
| 402 | 2024-10 | Section 79: Thiết kế quyền trong hệ thống thương mại điện tử (Hoàn thành source thực tế) | 42:24 | ? | https://www.youtube.com/watch?v=3jIDM99037U |
| 404 | 2024-10 | Section 78: Designing Rights in E-commerce Systems (Part 2) | 16:56 | ? | https://www.youtube.com/watch?v=2zrU3NAY0jo |
| 407 | 2024-10 | Section 77: Designing Rights in E-Commerce Systems (Part 1) | 10:11 | ? | https://www.youtube.com/watch?v=2w4TQ7EV-84 |
| 412 | 2024-10 | Section 75: Add domain shopdev.com to NGINX with SSL port (443) | 11:29 | ? | https://www.youtube.com/watch?v=67cAjD-twoU |
| 415 | 2024-10 | Section 74: Reverse Proxy Nginx vs EC2 \| Next setup Domain Shopdev.com | 7:00 | ? | https://www.youtube.com/watch?v=UfV1FUtVypc |
| 416 | 2024-10 | Stream trong NodeJS: Kinh nghiệm của 2 Lập Trình Viên xử lý tối ưu FILE LỚN như thế nào? | 12:07 | 9100 | https://www.youtube.com/watch?v=6u7B54FGpGA |
| 418 | 2024-10 | Section 73: Triển khai CI/CD từ GitHub và EC2 (AWS) | 31:59 | ? | https://www.youtube.com/watch?v=2ZYH1FuZ0uY |
| 426 | 2024-10 | Section 70: Comprehensive Deployment of EC2 - The Backend's Sharpest Weapon | 22:45 | ? | https://www.youtube.com/watch?v=-k5jfYrtQJo |
| 429 | 2024-10 | Section 69: AWS CloudFront File Security Prevents BackEnd Copying | 20:42 | ? | https://www.youtube.com/watch?v=pSwROxV2l8I |
| 431 | 2024-10 | Section 68: Setup Cloudfront với S3 \| AWS Pro | 9:51 | ? | https://www.youtube.com/watch?v=dFe7jE5Otr4 |
| 432 | 2024-10 | Promise sử dụng khi nào với từng trường hợp all, race, any và allSettled trong  ứng dụng Nodejs | 16:13 | 7100 | https://www.youtube.com/watch?v=fnOg4DF-t7U |
| 433 | 2024-10 | Section 67: AWS - S3 Deploying secure S3 link backend service and testing URL performance speed | 12:35 | ? | https://www.youtube.com/watch?v=HnF6tfUE0gk |
| 435 | 2024-10 | Section 66: Upload Images to S3 from Node Back End \| AWS | 17:20 | ? | https://www.youtube.com/watch?v=APZCs7lALQk |
| 437 | 2024-10 | Section 65: Amazon Web Services (AWS) S3 Bucket Setup and Security (2) | 16:48 | ? | https://www.youtube.com/watch?v=MDQEu7-GZMY |
| 439 | 2024-10 | Section 64: Amazon Web Service (AWS) Intro and Registration | 10:50 | ? | https://www.youtube.com/watch?v=zPMdzBH61PE |
| 440 | 2024-10 | Anh em Coder hóng chức năng này đã quá LÂU rồi \| New chrome \| Learn Nodejs | 12:00 | 9000 | https://www.youtube.com/watch?v=BBdXwmPbSdA |
| 442 | 2024-10 | Section 63: Y chang Shopee \| Use multer vs cloudinary upload Multiple Files (3) \| Next AWS | 10:30 | ? | https://www.youtube.com/watch?v=x3h4UUUCMnY |
| 445 | 2023-10 | Section 62: Use multer vs cloudinary upload File (2) | 18:09 | ? | https://www.youtube.com/watch?v=fUO6VF394eA |
| 446 | 2023-10 | Section 61: Intro Cloud vs Upload Service For Api (1) | 33:27 | ? | https://www.youtube.com/watch?v=dFIhLYlNXtw |
| 447 | 2023-10 | Tạm biệt TypeScript, các dự án LỚN đành hẹn gặp lại ! | 19:52 | 33000 | https://www.youtube.com/watch?v=m6mcXjnqFFo |
| 454 | 2023-10 | Section 57: x-api-key You ask, I answer ??? | 7:50 | ? | https://www.youtube.com/watch?v=--yEOnZBB8o |
| 455 | 2023-10 | Bảo mật API Keys như thế nào trong shopDEV ?? Hỏi đáp.. | 7:50 | 7900 | https://www.youtube.com/watch?v=cqY_z0fkMfs |
| 461 | 2023-10 | Bun vs Node.js tôi test performance, sự thật không phải như cộng đồng lập trình nói ??? | 22:37 | 10000 | https://www.youtube.com/watch?v=YmTGDn4ttAA |
| 464 | 2023-10 | I tried Bun and then looked back at Node.js and... | 17:26 | 17000 | https://www.youtube.com/watch?v=JcMr866DJ-o |
| 468 | 2023-10 | Node.js (20.6.0) mới phát hành với tính năng NÀY tôi và Anh Em đã mong chờ từ lâu. | 7:54 | 5700 | https://www.youtube.com/watch?v=0haeS2SpdTo |
| 491 | 2023-10 | Why Learn Algorithms? Why Does My shopDEV Feed Show Products My Wife Buys? | 11:57 | 9000 | https://www.youtube.com/watch?v=b4-58Ass58A |
| 495 | 2023-10 | Section 39: Formula calculation and deleting comments in shopDEV eCommerce \| Nested Set Model | 16:19 | ? | https://www.youtube.com/watch?v=2rYyw1FSIPc |
| 497 | 2023-10 | Lần đầu TEAM với dự án ShopDEV (eCommerce) show CODE về việc triển khai comments parent và child | 7:06 | 5800 | https://www.youtube.com/watch?v=gI6FkHZam5Y |
| 498 | 2023-10 | Section 38: Implementing Nested Comments system in shopDEV eCommerce \| create vs list comments | 32:45 | ? | https://www.youtube.com/watch?v=CVF8QXumS00 |
| 510 | 2023-10 | Section 33: Export Service Push Log Router backend lên Discord với Postman eCommerce Backend Node.js | 18:34 | 3400 | https://www.youtube.com/watch?v=aBiVefqfuR0 |
| 512 | 2023-10 | Section 32: Xây dựng hệ thống loggers sử dụng Discord vào dự án eCommerce Backend Node.js \| Auto Bot | 16:58 | 4800 | https://www.youtube.com/watch?v=c6-ZDgz7SCo |
| 528 | 2023-10 | ES14 (ECMAScript 2023) đã xuất phát những TÍNH NĂNG này bạn đã thử? Học nhanh thôi. | 11:17 | 3000 | https://www.youtube.com/watch?v=Keoyg8GRIE0 |
| 531 | 2023-10 | Section 25: Order Service Api (part 1) | 34:12 | ? | https://www.youtube.com/watch?v=rpoQjTm9In4 |
| 534 | 2023-10 | Nodejs Event Loop - Last explanation for those who are still DOUBTING through two classic EXAMPLES | 25:09 | 15000 | https://www.youtube.com/watch?v=GVx47SJYZhI |
| 535 | 2023-10 | Section 24: Cart Service Api \| Update, reduce, increase product [User] Part 2 | 32:48 | ? | https://www.youtube.com/watch?v=Ezf_10SsfWs |
| 536 | 2023-10 | Section 23: Cart Service in eCommerce Part 1 \| Cart Model vs add product to cart [User] | 29:32 | ? | https://www.youtube.com/watch?v=HQkAB2z4OcI |
| 537 | 2023-10 | Stream Nodejs - See the following two examples to see the core of the programmer using the Stream... | 12:24 | 8000 | https://www.youtube.com/watch?v=AiPuHlyP8qM |
| 538 | 2023-10 | Tập trung 3 tính năng này của NODE.JS vậy tôi hỏi các bạn tôi có sai không? \| Podcast Lập Trình Viên | 14:56 | 8000 | https://www.youtube.com/watch?v=vqPqf7GQE3s |
| 539 | 2023-10 | Section 22: Discount Service in eCommerce Part 2 - FULL | 49:23 | ? | https://www.youtube.com/watch?v=nVH56wVEDCg |
| 541 | 2023-10 | Section 21: Discount Service in eCommerce with 6 features | 36:32 | ? | https://www.youtube.com/watch?v=77kTtMdnqek |
| 542 | 2023-10 | Node.js 20  phát hành NÊN học tính nằng này không cần phải nhiều?\| What's new in Node v20? | 10:50 | 2700 | https://www.youtube.com/watch?v=SnFxlqFPjtQ |
| 545 | 2023-10 | Section 20: Discount Model in eCommerce | 22:06 | ? | https://www.youtube.com/watch?v=-jhjxo7TW1g |
| 547 | 2023-10 | Section 19: Inventories Model vs Services | 19:24 | ? | https://www.youtube.com/watch?v=VYOlDxdcehY |
| 550 | 2023-10 | Section 18: Update với POST, PUT, PATCH trong Product Service API | 37:28 | ? | https://www.youtube.com/watch?v=w3dpcns7zj4 |
| 552 | 2023-10 | Section 17: Remaining features, findAll, findOne, selectData, unSelectData in Product Service API | 18:48 | ? | https://www.youtube.com/watch?v=pKbdGrQGVJk |
| 554 | 2023-10 | Section 16: Add isDraft, isPublish, unPublish features and add Product Service API schema | 59:30 | ? | https://www.youtube.com/watch?v=ZD5cWfsZO3A |
| 557 | 2023-10 | Section 15: Thiết kế Api Service Product kết hợp giữa Factory và Strategy quá hiệu quả (Video Bonus) | 14:26 | ? | https://www.youtube.com/watch?v=T5rkuB8ca_g |
| 565 | 2023-10 | Section 12: Schema Product Ecommerce How to design millions of products and optimize queries FAST | 20:43 | ? | https://www.youtube.com/watch?v=j1Qb_qMNXzE |
| 567 | 2023-10 | Section 11( version 2 ): FIXED Bug bị sai và tối ưu hơn so với phiên bản cũ | 14:53 | ? | https://www.youtube.com/watch?v=sR3YViTbFJ8 |
| 568 | 2023-10 | Section 11: Handling Unauthorized Token Use and How to Handle It \| RefreshToken | 23:27 | ? | https://www.youtube.com/watch?v=S8yvvRag6Kk |
| 569 | 2023-10 | Section 10: Logout vs Authentication \| Course Node.js Backend eCommerce | 22:54 | ? | https://www.youtube.com/watch?v=vXhNEryxP0E |
| 570 | 2023-10 | Triển Khai CODE: Bảo mật giữa Postman(FE) và Node.js(BE) sử dụng thuật toán HMAC \| Phần 23 | 14:47 | 3200 | https://www.youtube.com/watch?v=wAyQ0Q2NpGQ |
| 578 | 2023-10 | Section 6:  Custom Dynamic Middleware for ApiKey and Permissions | 18:36 | ? | https://www.youtube.com/watch?v=nQxEwBAcYrI |
| 579 | 2023-10 | Section 5: Reup Sign-up Shop (FULL) RSA and JWT algorithms for two additional levels keyToken, au... | 49:53 | ? | https://www.youtube.com/watch?v=Ha_LFuZ5x1U |
| 580 | 2023-10 | Section 5: Api Sign-up Shop (FULL) implements RSA and JWT algorithms for two levels. (missing ver... | 27:04 | ? | https://www.youtube.com/watch?v=EkFGhtrXX0w |
| 582 | 2023-10 | Section 5: Api Sign-up Shop (1) | 31:07 | ? | https://www.youtube.com/watch?v=mkol2daN7FU |
| 584 | 2023-10 | Section 4: Lịch sử của .env và cách kết hợp env và configs cho dự án nhiều môi trường và Members | 19:04 | ? | https://www.youtube.com/watch?v=jnxsMU5hjqs |
| 599 | 2023-10 | Phần 2 - 13 tips cần BIẾT của một BackEnd khi Building a Project REST API with Node.js and Express | 11:59 | 6100 | https://www.youtube.com/watch?v=aXBZjId5XEE |
| 600 | 2023-10 | 13 tips cần BIẾT của một BackEnd khi Building a Project REST API with Node.js and Express - Phần 1 | 13:09 | 18000 | https://www.youtube.com/watch?v=sQj2c7dEj2o |
| 604 | 2023-10 | CHATGPT vs Node.js - Build a Service app CHAT in my COMPANY use OpenAI - (1) | 1:00 | 6100 | https://www.youtube.com/watch?v=hk8TVn3Y9Is |
| 615 | 2023-10 | Node.js 19  phát hành NÊN học tính nằng này không cần phải nhiều?\| What's new in Node v19? | 13:39 | 4500 | https://www.youtube.com/watch?v=MBs9BmArgCc |
| 656 | 2022-10 | Hóa ra đây là phần hoàn chỉnh về bảo mật REST API nếu bạn là một Backend sử dụng NodeJS build API | 40:30 | 9600 | https://www.youtube.com/watch?v=z8qrSG2j1fo |
| 657 | 2022-10 | Backend Nodejs vs thuật toán trao đổi KEY API Diffie Hellman và 2 ví dụ mã hóa của bác PHẠM XUÂN ẨN | 41:03 | 9300 | https://www.youtube.com/watch?v=so0myCu8EGY |
| 671 | 2022-10 | Send OTP hiệu quả và ALICONCON đã dùng cách này \| E-COMMERCE ALICONCON \| Part - 3 \| Node.js Tutorial | 45:12 | 12000 | https://www.youtube.com/watch?v=rdvjxRRvVF0 |
| 673 | 2022-10 | Node.js developer roadmap \| Backend Service | 0:48 | 49000 | https://www.youtube.com/watch?v=8YE_waVWa7A |
| 682 | 2022-10 | Ai nói forEach là xấu khi làm việc với Loops with Async / Await \| Nodejs tutorial \| Cách tôi FIX | 27:40 | 5000 | https://www.youtube.com/watch?v=luzg3zpN0SY |
| 683 | 2022-10 | Difference between returning await and not using await in Promises \| Async Await \| Node.js tutorial | 10:14 | 11000 | https://www.youtube.com/watch?v=NzzcRHpmhJk |
| 684 | 2022-10 | Lợi ích của Promise so với async-await đa số người chưa biết về 3 cách  \| Promises or async-await | 13:17 | 17000 | https://www.youtube.com/watch?v=0WJK4rWlw_0 |
| 685 | 2022-10 | Socket.io authentication express \| Socket io jwt \| Nodejs tutorial | 19:04 | 8000 | https://www.youtube.com/watch?v=OcskWwBV0j0 |
| 686 | 2022-10 | Socket.io triển khai theo MVC Express \| Best practice question involving Socket.io and MVC \| Nodejs | 32:01 | 12000 | https://www.youtube.com/watch?v=jY3aDAYNq_Q |
| 688 | 2022-10 | What is CORS? Fix it with a few lines of code \| Using CORS in Express \| Nodejs Tutorial | 9:48 | 7800 | https://www.youtube.com/watch?v=VuXakfARDC4 |
| 690 | 2022-10 | Config routes trong express thế nào khi có 1000 routes và nhiều thành viện tham gia dự án | 16:07 | 6500 | https://www.youtube.com/watch?v=0OTmTe5EnpQ |
| 691 | 2022-10 | Parsing request RESTful api \| Express.js vs Node.js | 16:46 | 2400 | https://www.youtube.com/watch?v=7U71q1GLEro |
| 692 | 2022-10 | Cấu trúc dự án API REST từ lv1 đến lv4 \| APIStructure Your Nodejs REST API for beginner to Advanced | 23:42 | 18000 | https://www.youtube.com/watch?v=i4Pr81apfnU |
| 693 | 2022-10 | Node.js 18 Release SHOULD I learn this feature without much effort?\| What's new in Node v18? | 14:46 | 2100 | https://www.youtube.com/watch?v=a66kWREgnr4 |
| 702 | 2022-10 | Cookie là gì? Tìm hiểu Cookie hoạt động HTTPOnly, Secure với EXPRESS NODEJS | 20:53 | 18000 | https://www.youtube.com/watch?v=LvlUsIwYLW4 |
| 703 | 2022-10 | Comprehensive Guide to Amazon Cloud (AWS): Setting up a Server with domain, https, nginx, node, a... | 22:24 | 14000 | https://www.youtube.com/watch?v=OWS7h5Mm-v8 |
| 712 | 2022-10 | Node.js 17 phát hành NÊN học tính nằng này không cần phải nhiều?\| What's new in Node v17? | 8:58 | 2500 | https://www.youtube.com/watch?v=01YdaPRVNYQ |
| 715 | 2022-10 | What are Event Emitters? Useful features of Nodejs in 5 command lines \| Nodejs Tutorial | 6:14 | 3200 | https://www.youtube.com/watch?v=SNU0QTWTXvM |
| 716 | 2022-10 | Boost Your Node.js App Speed with Compression \| Node.js Performance | 11:11 | 5500 | https://www.youtube.com/watch?v=bIFq0fxNLoE |
| 725 | 2021-10 | Docker là gì? Cách tạo một docker đơn giản cho node.js video quá đầy đủ \| NODEJS WITH DOCKER | 22:47 | 15000 | https://www.youtube.com/watch?v=jbd71z2Gdo4 |
| 726 | 2021-10 | Nodejs write log to file \| Series Social Media REST API NODE.JS (6) \| ANONYSTICK | 14:35 | 5000 | https://www.youtube.com/watch?v=Fb2W_GBx3QY |
| 727 | 2021-10 | Bắt đến chết API ERROR và EXPRESS ERROR \| Series Social Media REST API NODE.JS (5) | 9:35 | 3800 | https://www.youtube.com/watch?v=mJWg96W2YE4 |
| 728 | 2021-10 | Convert text to speech (audio Mp3) Node.js with gTTS \| Useful NPM Packages Node.js \| ANONYSTICK | 5:31 | 2200 | https://www.youtube.com/watch?v=XiUnYr6Iijg |
| 730 | 2021-10 | Route Express có thể bạn chưa biết điều này \| Series Social Media REST API Nodejs\| Phần 3 | 20:06 | 3500 | https://www.youtube.com/watch?v=W2h0dUdILj4 |
| 733 | 2021-10 | 9 Principles and Best Practices for Designing REST APIs When Developing a Backend for shopDEV | 10:17 | 22000 | https://www.youtube.com/watch?v=CX_BGViLEoM |
| 735 | 2021-10 | Phân quyền User với Rest API trong Nodejs \|  NodeJS Authorization | 21:41 | 10000 | https://www.youtube.com/watch?v=f-Gb91Sc_rY |
| 739 | 2021-10 | How to send emails with Node.js with Nodemailer \| GMAIL \| OAUTH2 | 19:35 | 5000 | https://www.youtube.com/watch?v=aqMPRCNzkbg |
| 740 | 2021-10 | Add Controller pattern vs Complete Course (14) \| NODEJS API AUTHENTICATION \| ANONYSTICK | 5:26 | 2000 | https://www.youtube.com/watch?v=m4Ev3M_4jK0 |
| 741 | 2021-10 | Logout User (13) \| Node JS API Authentication | 6:24 | 4800 | https://www.youtube.com/watch?v=Mk60ETaiTeg |
| 742 | 2021-10 | Google drive api upload file with Node.js \| Google API \| Anonystick | 37:34 | 10000 | https://www.youtube.com/watch?v=bJYoUOt6QWk |
| 744 | 2021-10 | Using refresh token create new token (11) \| NODE.JS API Authentication \| ANONYSTICK | 14:25 | 7000 | https://www.youtube.com/watch?v=-_fxOtzK44U |
| 746 | 2021-10 | Generating Refresh Tokens (9) \| Node.js API Authentication \| ANONYSTICK | 7:15 | 3800 | https://www.youtube.com/watch?v=A7YeZOEPquw |
| 747 | 2021-10 | Verify access token Node.js ( 8 ) \| Nodejs and Express.js API Authentication \| ANONYSTICK | 12:54 | 4100 | https://www.youtube.com/watch?v=baiyWCJUhWM |
| 748 | 2021-10 | Generator JWT Access Token (7) \| Node and express course \| ANONYSTICK | 10:03 | 4400 | https://www.youtube.com/watch?v=5eQmHXx-ayw |
| 750 | 2021-10 | Bcrypt hash password in Node.js (5) \| Node and express course \| ANONYSTICK | 11:22 | 3500 | https://www.youtube.com/watch?v=KTmLRBhVGNo |
| 751 | 2021-10 | Joi awesome code validation for Node.js and Express (4) \|  \| Node and express course \| ANONYSTICK | 10:24 | 4200 | https://www.youtube.com/watch?v=jYFcmcessNE |
| 754 | 2021-10 | Setting express with error handler (1) \| Node and express course for beginner tutorial \| ANONYSTICK | 21:22 | 17000 | https://www.youtube.com/watch?v=gDo-I9YgZTQ |
| 755 | 2021-10 | Dotenv là gì? Cách sử dụng trong Nodejs \| Tự học Nodejs | 4:54 | 3100 | https://www.youtube.com/watch?v=cCYneHh6DLw |
| 763 | 2021-10 | Helmet NodeJS \| Middleware NodeJS | 6:02 | 2200 | https://www.youtube.com/watch?v=oaTYX01pk-M |
| 767 | 2021-10 | How To Write and Run Your First Program in Node.js | 11:23 | 535 | https://www.youtube.com/watch?v=xBUxZw0w0Fg |
| 769 | 2021-10 | Authentication services Nodejs with JsonWebToken | 30:20 | 2900 | https://www.youtube.com/watch?v=yaLm4l_EzJU |
| 781 | 2020-10 | Build a simple chat app with node.js, firebase and Heroku | 2:25 | 2100 | https://www.youtube.com/watch?v=ssJb1PQ-D_E |
| 782 | 2020-10 | Get Metadata from url with nodejs | 0:27 | 2900 | https://www.youtube.com/watch?v=O4Pobbwt0Ds |

<a id="ops"></a>
## 11. DevOps, cloud, monitoring & logging

| # | Upload (approx.) | Title | Duration | Views | Link |
|---|---|---|---|---|---|
| 73 | 2025-11 | AWS: 6 sai lầm cần tránh trước khi trở thành kỹ sư Cloud. | 10:21 | 2200 | https://www.youtube.com/watch?v=Rhu0KBw1068 |
| 194 | 2025-10 | Đánh bại Senior: JWT Logout đơn giản - mà không làm ảnh hưởng đến các thiết bị khác cùng tài khoản. | 9:44 | 21000 | https://www.youtube.com/watch?v=IEEdKxXk3SQ |
| 242 | 2025-10 | Intern beats Senior: How to optimize Docker? And the result is a Docker image from 500MB to 100MB | 15:30 | 15000 | https://www.youtube.com/watch?v=T5MHC7WeU5Y |
| 255 | 2025-10 | Docker vs Kubernetes API Backend: Accomplishing DevOPS Missions | 17:18 | 3700 | https://www.youtube.com/watch?v=HZAXNSkAQqA |
| 256 | 2025-10 | Docker vs Kubernetes API: Testing DevOPS Locations - This video is sufficient for deploying Apple... | 26:02 | 5100 | https://www.youtube.com/watch?v=4oi3VqKfHkc |
| 408 | 2024-10 | Why do COMPANIES log Backend API data this way? What's the professional approach? | 16:50 | 18000 | https://www.youtube.com/watch?v=ZwDpGJmGGb8 |
| 417 | 2024-10 | Từng bước xây dựng CI/CD và phát hành tự động Backend Api dựa trên GitHub và EC2 (AWS), PM2 | 31:59 | 10000 | https://www.youtube.com/watch?v=ghIltBUCyns |
| 419 | 2024-10 | Oh No, 100% CPU! How Do I Fix This? | 14:28 | 8600 | https://www.youtube.com/watch?v=qb49coRptls |
| 511 | 2023-10 | Docker trong con mắt của một Backend là phải thao tác nhanh gọn và dứt khoát phải giống như DevOps | 9:04 | 6600 | https://www.youtube.com/watch?v=8HSiwP92aPw |
| 593 | 2023-10 | Simple factory pattern sử dụng trong ứng dụng Logistics như thế nào giữa Level 0 và Level xxx? | 18:43 | 8400 | https://www.youtube.com/watch?v=O6TsDdKtyz0 |
| 649 | 2022-10 | Which technology stack, Push or Pull, did Facebook and Instagram choose to develop their news feed? | 13:41 | 17000 | https://www.youtube.com/watch?v=qu3Lc2evkTw |
| 705 | 2022-10 | Toàn diện về Amazon Cloud (AWS): EC2 (VPS) Đăng Ký Free cho Lập Trình Viên mới bắt đầu \| (1) | 26:30 | 16000 | https://www.youtube.com/watch?v=aLOcO8qT7k0 |

<a id="sec"></a>
## 12. Security & auth

| # | Upload (approx.) | Title | Duration | Views | Link |
|---|---|---|---|---|---|
| 189 | 2025-10 | Họ nói JWT không thể thu hồi  - Cách TỐT nhất vô hiệu hoá nhiều devices khi changePassword | 9:52 | 6500 | https://www.youtube.com/watch?v=z84fkObC5Pw |
| 279 | 2024-10 | INTERN đánh bại SENIOR: Làm thế nào để bảo vệ Server khi action SPAM vào FORGOT PASSWORD API ? | 12:23 | 24000 | https://www.youtube.com/watch?v=_9O0eyRM-eE |
| 379 | 2024-10 | I LOST (was hacked) my account like this? What is IDOR? | 16:17 | 8300 | https://www.youtube.com/watch?v=2KqZJDf7uQI |
| 405 | 2024-10 | What Programmers Should Do Now That Third-Party Cookies Are Being Phased Out: Important Reminder ... | 10:21 | 7700 | https://www.youtube.com/watch?v=UtRisKVCYIE |
| 428 | 2024-10 | Đề xuất Tools cho DEV: Liệu có cần FrontEnd nữa hay không? Khi tạo youtube, hack news chỉ với 1 phút | 5:28 | 16000 | https://www.youtube.com/watch?v=VYCaAyVA0cQ |
| 602 | 2023-10 | (2) Shopee vs Hack news đã triển khai hệ thống Comments như thế này với Rest Api? Dành cho Level 1 | 33:29 | 4300 | https://www.youtube.com/watch?v=i8WLvdbF_W8 |
| 603 | 2023-10 | CHATGPT Share tài khoản OpenAI miễn phí hàng tuần (Email + password ) đính kèm trong video \|Tuần 3 | 1:03 | 9100 | https://www.youtube.com/watch?v=j_ObF0lCeDU |
| 622 | 2023-10 | Token (JWT) Triển khai hệ thống tự động phát hiện Token đã được sử dụng bởi Hacker và cách xử lý! | 23:01 | 16000 | https://www.youtube.com/watch?v=1HHvCfAu008 |
| 625 | 2023-10 | Token (JWT) How to revoke a hacked token and some questions about the safety of using tokens | 23:45 | 23000 | https://www.youtube.com/watch?v=93fTk16-st0 |
| 666 | 2022-10 | SECURITY MESSAGE: Nói về việc bảo mật nội dung CHAT, MEMBERs.... | 30:16 | 5500 | https://www.youtube.com/watch?v=TWSWymrSmiE |
| 679 | 2022-10 | Triển khai 3 cách phân trang APIs với hệ thống Stackoverflow, reddit, facebook và hack news | 57:43 | 13000 | https://www.youtube.com/watch?v=EOqKXH8Ztrg |
| 707 | 2022-10 | REST Security với JWT có lẽ đây là phương pháp tốt nhất AccessToken hết hạn hiện nay \| JWT Secure | 39:07 | 12000 | https://www.youtube.com/watch?v=nONm8yu_9gE |

<a id="ai"></a>
## 13. AI & tools

| # | Upload (approx.) | Title | Duration | Views | Link |
|---|---|---|---|---|---|
| 8 | 2026-08 | Claude Code – This One Video Is Enough for Plugins, Goals, MCP, Skills, and Setup \| So Good! | 10:37 | 12000 | https://www.youtube.com/watch?v=aSEhzM23-Ek |
| 46 | 2026-02 | CLAUDE CODE: A guide to obtaining the CLAUDE CODE certification and completing 8 levels of AI pro... | 14:01 | 35000 | https://www.youtube.com/watch?v=sqZAjzI9P7o |
| 144 | 2025-10 | Backend AI AGENT: BUILD training OpenAI Assistant API - BOSS Increase Revenue (With Source + Docu... | 8:47 | 3500 | https://www.youtube.com/watch?v=rMuH9ZR7rvo |
| 154 | 2025-10 | NotebookLM: Google is beyond imagination now, you REALLY should give it a try, Oh my God... | 10:02 | 18000 | https://www.youtube.com/watch?v=otk_1EdYdRk |
| 205 | 2025-10 | SỰ UY TÍN CỦA Leaderboard AI  vs LẬP TRÌNH VIÊN "MÙ CODE" | 7:20 | 7000 | https://www.youtube.com/watch?v=8O68zxJICBA |
| 254 | 2025-10 | Tool System Administration mà các bạn hỏi là đây... | 4:14 | 3200 | https://www.youtube.com/watch?v=DJHNLI6nuCs |
| 351 | 2024-10 | Guide for Programmers to participate in PR in the high-quality OpenSource GitHub community | 12:34 | 3900 | https://www.youtube.com/watch?v=82oFC6cO5lg |
| 366 | 2024-10 | VS Code với 5 phím tắt cho kỹ năng từ sự lười biếng haha | 7:04 | 4000 | https://www.youtube.com/watch?v=rfXHa6DA4Do |
| 463 | 2023-10 | Lập trình viên LƯƠNG CAO? Ai hỏi như vậy vui lòng đưa họ video này? | 14:35 | 11000 | https://www.youtube.com/watch?v=eFaKfXY5pTs |
| 508 | 2023-10 | Autocomplete terminal - This is a TOOL that I and the BIG BROTHERS cannot do without, now I share... | 10:13 | 8300 | https://www.youtube.com/watch?v=qnn8bqRsijk |
| 638 | 2022-10 | CDN là gì? Với 1 PHÚT ai cũng hiểu vì sao lại sử dụng CDN và nếu không có CDN thì sao? | 1:08 | 4700 | https://www.youtube.com/watch?v=77m4cQN35G8 |
| 660 | 2022-10 | Biết GIT chỉ là học việc quan trọng Fix Git mới là bậc thầy l Git cherry pick l Git stash Git reset | 32:07 | 16000 | https://www.youtube.com/watch?v=41KMhNTq5tA |
| 661 | 2022-10 | Tôi chưa bao giờ hiểu Git Rebase và Git Merge cho đến khi Sếp giải thích cho tôi như thế này \| Git | 38:37 | 42000 | https://www.youtube.com/watch?v=l0VtRcPz1ME |
| 663 | 2022-10 | Comprehensive summary of Git usage and GitFlow workflow and my boss asked me to learn | 35:59 | 96000 | https://www.youtube.com/watch?v=vQgcl8VouLU |
| 698 | 2022-10 | How to Copy Variable from Chrome Dev Tools Console | 1:13 | 2500 | https://www.youtube.com/watch?v=oDTaOtvlnzY |
| 756 | 2021-10 | Git vs GitHub - .gitignore file (08/07) \| Self-learn GIT | 5:23 | 8900 | https://www.youtube.com/watch?v=Xv152mjrPxo |
| 757 | 2021-10 | Git vs. GitHub - Branching (8/6) \| Learning GIT | 6:56 | 1800 | https://www.youtube.com/watch?v=5b9_Y9hZJOU |
| 758 | 2021-10 | Git vs Github pull changes (5/08) \| Tự học GIT | 1:20 | 1600 | https://www.youtube.com/watch?v=cs27QEkg08k |
| 759 | 2021-10 | Git vs Github - Commit and Push (4/08) \| Tự học GIT | 2:07 | 1700 | https://www.youtube.com/watch?v=wHEntKYM1yM |
| 760 | 2021-10 | Hướng dẫn sử dụng Github và Git \| Setting Global (3/08) \| Tự học GIT | 1:10 | 1900 | https://www.youtube.com/watch?v=DGfixYOBdVU |
| 761 | 2021-10 | Hướng dẫn sử dụng Github và Git \| Clone Git (2/08) \| Tự học GIT | 1:06 | 2400 | https://www.youtube.com/watch?v=prFUvdqasK4 |
| 762 | 2021-10 | Hướng dẫn sử dụng Github và Git \| Installing Git (1/08) \| Tự học GIT | 1:03 | 3400 | https://www.youtube.com/watch?v=Q4EQTrpLB1k |
| 772 | 2021-10 | Hướng dẫn sử dụng ESLINT với VSCODE | 5:56 | 2200 | https://www.youtube.com/watch?v=M9sVMHtnJTo |

<a id="career"></a>
## 14. Career, soft skills & other (NoCODE)

| # | Upload (approx.) | Title | Duration | Views | Link |
|---|---|---|---|---|---|
| 9 | 2026-08 | NoCode \| Nhóm (Referral job...) gần 100 người. Giới thiệu remote cho FE, QA, Tester và U40 Backend. | 17:16 | 3600 | https://www.youtube.com/watch?v=h5Nc6ehIzNM |
| 14 | 2026-07 | Programmer: A New Milestone in the Journey \| SILVER PLAY BUTTON \| Thank You All | 2:05 | 1500 | https://www.youtube.com/watch?v=Tf1YdIb_fnw |
| 23 | 2026-06 | NoCODE: I watched an awards ceremony and saw an OVER-THE-HILL programmer who’s still writing CODE... | 14:49 | 22000 | https://www.youtube.com/watch?v=v0F8-5fL4HQ |
| 31 | 2026-05 | Khi nào dev nên nhảy việc? Tôi nhận ra 3 điều đó là khi không còn học được gì ở môi trường cũ! | 9:59 | 4000 | https://www.youtube.com/watch?v=1y9e1IsiZP4 |
| 44 | 2026-03 | IT Industry 2026 - These programmers need to shift their goals to be more realistic. (A British q... | 17:37 | 90000 | https://www.youtube.com/watch?v=mYfOAMzazOA |
| 45 | 2026-02 | Solve the problem (4): SOURCE CODE 👇👇👇👇👇 | 6:01 | ? | https://www.youtube.com/watch?v=JlyubT4_KXw |
| 47 | 2026-02 | Solving problem (3): How to list conversions vs synchronize messages for multiple devices? | 18:44 | ? | https://www.youtube.com/watch?v=Xz06iXHHcLU |
| 49 | 2026-02 | Solving problem (2): REALTIME GROUP MESSAGE vs. WebSocket, Socket.io or Firebase choice?? | 16:10 | ? | https://www.youtube.com/watch?v=QR4VDr1mT7I |
| 54 | 2026-01 | IT Industry 2026: Freelancing Reigns Supreme, Top 3 Languages, 3 Skills Retained \| New Directions... | 22:10 | 42000 | https://www.youtube.com/watch?v=PKMlPmO0UQA |
| 78 | 2025-10 | Stop Using ModelMapper. Use ??? Instead! Why? | 10:57 | 3900 | https://www.youtube.com/watch?v=uHPh5uxE5mo |
| 95 | 2025-10 | NoCODE: SENIOR passed? And I think you might need the answer! Detailed question... | 13:25 | 3800 | https://www.youtube.com/watch?v=QY7gkhb65Zk |
| 99 | 2025-10 | Backend vs Frontend: There's a discussion about which position is HARDER here, would you like to ... | 13:55 | 8900 | https://www.youtube.com/watch?v=QBdoOPGToRY |
| 114 | 2025-10 | Not using TypeORM when you have Prisma ??? Not good at all... | 12:02 | 3500 | https://www.youtube.com/watch?v=0VLtpaFWAYo |
| 115 | 2025-10 | SA - CHAT APP (3): VERSION 3 THE OPTIMAL DATA DESIGN IS HERE, ONE vs ONE AND GROUP | 13:50 | ? | https://www.youtube.com/watch?v=MTAUHRg5t3Y |
| 116 | 2025-10 | SA - APP CHAT (2): Optimize scenario 2, message SIZE has been reduced, BUT WRITE performance is s... | 13:49 | ? | https://www.youtube.com/watch?v=_nhV5TyL8gM |
| 117 | 2025-10 | SA - APP CHAT (1): Optimize scenario 1, billions of redundant MESSAGES and high WRITE rate... | 11:25 | ? | https://www.youtube.com/watch?v=oK_hvlZ40Zc |
| 118 | 2025-10 | NoCode: Long time no see HAPPINESS - CHAT APP: Data design with BILLIONS OF MESSAGES... Next... | 11:25 | 1900 | https://www.youtube.com/watch?v=s0f8dNtJnt8 |
| 136 | 2025-10 | Thiết kế triển khai APP CHAT MESSAGE với cấp triệu USERs thay thế Telegram với hiệu suất khả thi. | 17:35 | 6600 | https://www.youtube.com/watch?v=pSjnGaB1OmM |
| 138 | 2025-10 | Why should projects use npx? What is the difference between npm and npx? Do you remember pnpm? | 5:28 | 3900 | https://www.youtube.com/watch?v=n4YeMrw3nKY |
| 148 | 2025-10 | OK x10 hiệu suất UPLOAD LARGE FILE hệ thống. Cái bắt tay FE + BE. Tối ưu Web workers thế nào đây. | 46:10 | 5600 | https://www.youtube.com/watch?v=8ANuWk9KWcA |
| 164 | 2025-10 | I get an OUTSIDE project and how do I get PAY and complete it? Can I share? | 11:17 | 6600 | https://www.youtube.com/watch?v=OEc8RKElPaE |
| 168 | 2025-10 | NOCODE: LAYOFF - Approaching 50 and I still don't dare to take a PM role... | 7:55 | 8500 | https://www.youtube.com/watch?v=YZzuHqyjmT0 |
| 177 | 2025-10 | Improve SELECT COUNT(*) from 4.2s to 0.002s with 13 MILLION records, what is the DATA TRADE-OFF? ... | 16:53 | 19000 | https://www.youtube.com/watch?v=2sfOGqLKXq8 |
| 195 | 2025-10 | ShareScreen Độ Trễ Thấp, Chất Lượng Cao với Open Source - Tốt nhất hiện tại - OpenSource (07) | 4:00 | 3600 | https://www.youtube.com/watch?v=k7zAUmZgdjA |
| 218 | 2025-10 | NEW - U50 có offer về Rust Backend, cách học ngôn ngữ mới NHANH và HIỆU QUẢ... yeah... | 8:20 | 7300 | https://www.youtube.com/watch?v=wOz9YrsAtbM |
| 227 | 2025-10 | 👉👉👉: LINK DISCORD FOR MEMBER - UPDATE 01/2025 | 0:40 | ? | https://www.youtube.com/watch?v=hcz1-Srwh6k |
| 230 | 2025-10 | Upstream - Only after watching did I realize why a notorious R&D LEAD had to choose that delivery... | 11:21 | 18000 | https://www.youtube.com/watch?v=mqgsV5Oo4cE |
| 246 | 2025-10 | Senior asks Intern: What do you think is the best way to check if a user exists among 100 million... | 24:43 | 88000 | https://www.youtube.com/watch?v=5iq4h1KwaGc |
| 267 | 2025-10 | API bán vé TÀU TẾT: Ngày thứ hai bán vé API USER đã truy cập TỐT nhờ kinh nghiệm của TEAM BACKEND. | 17:45 | 6700 | https://www.youtube.com/watch?v=1p7dxud9FkQ |
| 270 | 2025-10 | Project bán vé TÀU TẾT: API sập ngày đầu bán vé (CODE TEST) Review CODE với thấy có vấn đề SAI SÓT. | 25:16 | 17000 | https://www.youtube.com/watch?v=EQ4WTurq5I0 |
| 283 | 2024-10 | 5 available WEAPONS ensure optimal performance to handle tens of millions of access requests that... | 9:05 | 8500 | https://www.youtube.com/watch?v=oZ6m3aUPoC4 |
| 345 | 2024-10 | The BEST way to learn how to simplify complex programming code | 9:49 | 9300 | https://www.youtube.com/watch?v=UvAX36Mh7Dk |
| 354 | 2024-10 | NoCODE: 3 vấn đề CẦN giải quyết trong mỗi cá nhân nhất định phải trong 30 năm ? | 10:12 | 4500 | https://www.youtube.com/watch?v=c4Y_Q59FgTQ |
| 363 | 2024-10 | Nói về Cluster: Càng nhiều process thì càng tốt, theo bạn phải không? | 9:26 | 6100 | https://www.youtube.com/watch?v=_74_z2-uOys |
| 365 | 2024-10 | NoCODE - Tại sao TÔI nên học nhiều ngôn ngữ lập trình cùng một lúc? | 9:44 | 8000 | https://www.youtube.com/watch?v=VK_--v4FMvQ |
| 372 | 2024-10 | Cách sử dụng và các kịch bản dùng với các trường hợp ?., ??, ??= | 12:33 | 5700 | https://www.youtube.com/watch?v=ozSPsZh_b5Y |
| 375 | 2024-10 | Một BackEnd TẠI SAO bạn không biết 5 LỖ HỔNG máy chủ phổ biến NÀY CHỨ? | 11:06 | 16000 | https://www.youtube.com/watch?v=wGsYVgNeEAs |
| 385 | 2024-10 | NoCODE - Programmers show 2 competitive abilities? Which way should companies CHOOSE when intervi... | 19:07 | 17000 | https://www.youtube.com/watch?v=O_YxCOw5kwA |
| 386 | 2024-10 | Share hệ thống nền tảng thương mại điện tử eCommerce bao gồm WEB REACT vs APP MOBILE \| Link download | 9:09 | 9800 | https://www.youtube.com/watch?v=pc8Hs2iukko |
| 388 | 2024-10 | Solving Memory Leaks: Using WeakMap vs. Map in Engineering \| Senior vs. Middle | 14:33 | 4900 | https://www.youtube.com/watch?v=j1clD8XDYyw |
| 389 | 2024-10 | Performance APIs - A profound way to accelerate backend performance that should be implemented in... | 10:51 | 15000 | https://www.youtube.com/watch?v=_MtfJwJW7lc |
| 401 | 2024-10 | How Should Developers Choose a Company? Two Options Every Graduate Faces... | 11:58 | 5400 | https://www.youtube.com/watch?v=QfmEYbd3Dp0 |
| 403 | 2024-10 | This is How I Learned BackEnd Faster and Gained a Deeper Understanding of Systems \| Attached Reso... | 16:02 | 65000 | https://www.youtube.com/watch?v=Ttg9hezH-V0 |
| 411 | 2024-10 | End of 2023 summary of my years as a programmer vs Welcome 2024... | 12:11 | 5000 | https://www.youtube.com/watch?v=yuMMqpbSzsg |
| 414 | 2024-10 | Top 3 vị trí tuyển dụng (BE, SA)  trả lương cao nhất và 4 ngôn ngữ lập trình năm 2024 tại Việt Nam | 15:24 | 11000 | https://www.youtube.com/watch?v=kCzRVyc9CxI |
| 430 | 2024-10 | NO CODE - Làn sóng sa thải ngành phần mềm và đây là cách Lập Trình Viên nên làm? | 17:10 | 98000 | https://www.youtube.com/watch?v=xJj_klgABTE |
| 434 | 2024-10 | No Code: Lập Trình Viên TAY TRÁI vs TAY PHẢI thu nhập tài chính cùng đơn vị THỜI GiAN | 14:45 | 6100 | https://www.youtube.com/watch?v=ABs-U21GQXQ |
| 438 | 2024-10 | Lập trình viên có sự khác biệt khi nhìn công thức TÀI CHÍNH cho bản thân như thế nào? | 16:14 | 5400 | https://www.youtube.com/watch?v=HE3ROI9f7gQ |
| 443 | 2024-10 | Builders (I am 100%) switched to Programmers for these reasons... | 9:24 | 4400 | https://www.youtube.com/watch?v=thLNxhmLPW8 |
| 451 | 2023-10 | Why do programmers submit their CVs to more than 10 companies but still haven't received an offer... | 14:10 | 5400 | https://www.youtube.com/watch?v=UYP3BPRvMAA |
| 456 | 2023-10 | Hãy nắm bắt 6 đặc điểm của Lập Trình Viên xuất sắc, tôi chưa làm được điều 4! | 2:48 | 3000 | https://www.youtube.com/watch?v=xCPX2QnZtno |
| 457 | 2023-10 | Urgent: HOT FIX. Anh em trong MEMBER chú ý. Tại hạ nhận lỗi. | 2:00 | ? | https://www.youtube.com/watch?v=2K3Pk-_pFSc |
| 460 | 2023-10 | Lập Trình Viên Già nói chuyện với Tân Lập Trình Viên... Tôi cũng từng là sinh viên. | 12:28 | 4600 | https://www.youtube.com/watch?v=oObzpOkfBUw |
| 466 | 2023-10 | The Fullstack Developer Role: One Path, Two Destinies? | 21:41 | 12000 | https://www.youtube.com/watch?v=tGwx3d8yuTI |
| 470 | 2023-10 | FrontEnd to Backend: Pressure, Skills, Salary, and Starting Point? \| The Programmer's Path | 10:24 | 13000 | https://www.youtube.com/watch?v=KCylCGATTO0 |
| 473 | 2023-10 | Backend vs FrontEnd: Một số lỗi của BE làm FE gánh đạn và tổng hợp cách fixed của anh em FE. | 11:14 | 8100 | https://www.youtube.com/watch?v=YR_hHPGAE-o |
| 475 | 2023-10 | API vs SDK: If a car is an SDK, what is an API? By the way, here's a picture from Tips \| The Prog... | 8:19 | 6300 | https://www.youtube.com/watch?v=A0D6BPcEb0w |
| 481 | 2023-10 | Where are you in the Programmer Levels? The last level is really I don't know! | 18:18 | 14000 | https://www.youtube.com/watch?v=EG0cr7eYR-Q |
| 485 | 2023-10 | Should you proactively ask your boss for a raise if you're unsure? Let's examine whether this is ... | 16:27 | 4000 | https://www.youtube.com/watch?v=lXsCVwf4SW8 |
| 489 | 2023-10 | New Data Structures Guide and Best Tips for Mastering Algorithms – Free Download! | 15:58 | 20000 | https://www.youtube.com/watch?v=LKz_Fs3mcsg |
| 493 | 2023-10 | Data Structures and Algorithms My TEACHER once taught me about designing and building an economic... | 12:25 | 8400 | https://www.youtube.com/watch?v=dCr9Rctt74I |
| 501 | 2023-10 | Top 8 Solutions to Secure Data API INTERFACE with a BACKEND Programming and How Are You? | 9:46 | 9100 | https://www.youtube.com/watch?v=IA1MYI66vi4 |
| 504 | 2023-10 | Các Lập trình viên hiện tại nói về khả năng cạnh tranh cốt lõi chính xác là gì? Vị trí đạt được... | 16:10 | 10000 | https://www.youtube.com/watch?v=o4DI0a0TWws |
| 509 | 2023-10 | My wife says many developers will be rich in the future, right? How do I answer that! | 10:16 | 7300 | https://www.youtube.com/watch?v=B5OwJ-C05pk |
| 513 | 2023-10 | Tại sao TÔI rời CÔNG TY CŨ? \| Podcast Lập Trình Viên Già | 8:56 | 5600 | https://www.youtube.com/watch?v=fULWtp6iyes |
| 518 | 2023-10 | Call Bind Apply \| If anyone asks you, please show them this video \| Programmer's Path | 17:17 | 3600 | https://www.youtube.com/watch?v=O12TkHGWYB0 |
| 520 | 2023-10 | NO CODE \| When talking about SALARY INCREASE with LEADERSHIP, I said this? Do you think it's right? | 15:41 | 5500 | https://www.youtube.com/watch?v=JQGXPwATWKw |
| 521 | 2023-10 | Tôi đã thay đổi cấu trúc dữ liệu GIA PHẢ như thế nào để nâng cấp hiệu suất CAO cho một dòng họ lớn? | 11:48 | 3300 | https://www.youtube.com/watch?v=V3_BDlQB-ng |
| 522 | 2023-10 | Talking about MASTER application PERFORMANCE I have question 3.1x + 4 = 13 how to find (x)? | 12:04 | 3000 | https://www.youtube.com/watch?v=f8_t_Ck2vHI |
| 523 | 2023-10 | NO CODE \| Level của lập trình viên đáng giá bao nhiêu? Nhiều hay ít thùy thuộc vào hằng số này? | 13:37 | 5700 | https://www.youtube.com/watch?v=TuOaN_lAphg |
| 526 | 2023-10 | In the code in the project I often use the following features? Let me explain in detail (1) | 17:35 | 3300 | https://www.youtube.com/watch?v=XX0_6PLkoXI |
| 527 | 2023-10 | NO CODE \| Lương thế nào với khối lượng công việc của kinh nghiệm nghề Lập Trình Viên không nên nói | 18:03 | 7700 | https://www.youtube.com/watch?v=_7SDtcl4_cg |
| 532 | 2023-10 | What is Process nextTick? I will prove my class IF not using it will crash the Server? | 18:25 | 3800 | https://www.youtube.com/watch?v=WTmhaKrIK44 |
| 533 | 2023-10 | AUDIO - NO CODE \| Hidden Skills of a Senior Programmer \| The Path to Programmer (28) | 14:13 | 7500 | https://www.youtube.com/watch?v=sr8Y65_epz0 |
| 543 | 2023-10 | Bridge Pattern: Có thể triển khai hệ thống thanh toán giống YOUTUBE \| Khó (★★★☆☆) - Phổ biến (★★★☆☆) | 13:22 | 4100 | https://www.youtube.com/watch?v=0CuTOeCKbjM |
| 548 | 2023-10 | Builder Pattern: Code thanh lịch là khi phức tạp trở thành đơn giản đó là khi Dev lên LEVEL. | 13:40 | 5700 | https://www.youtube.com/watch?v=j-oCmwWggjY |
| 549 | 2023-10 | Tại sao một công ty lại quy định tất cả các giao diện UPDATE đều sử dụng  PATCH mà không PUT, POST? | 12:14 | 8700 | https://www.youtube.com/watch?v=-khw4pjvdYE |
| 551 | 2023-10 | Prototype Pattern: Tìm hiểu và học cách CODE triển khai các cầu thủ trong GAME FiFaOnline 4 | 14:44 | 6000 | https://www.youtube.com/watch?v=Wn2Bwi4qHl0 |
| 556 | 2023-10 | Share Source: Sử dụng CHAT GPT 3.5 tự động làm SHORT VIDEO  (tiktok, youtube) \|  Kèm account FREE | 5:06 | 3500 | https://www.youtube.com/watch?v=ki3s9-zjbbc |
| 559 | 2023-10 | Lập trình viên có thể làm gì khác sau 40? 3 lối thoát mà bạn tôi (U50) đạt được thật kỳ lạ. | 21:23 | 11000 | https://www.youtube.com/watch?v=CP4Xc1lbKCk |
| 560 | 2023-10 | Section14: Api Service Products (Optimal For LV.xxx) \| Nâng cao cấu trúc Product | 11:21 | ? | https://www.youtube.com/watch?v=SCSCiPRba50 |
| 562 | 2023-10 | Section13: API Product use Factory Pattern \| Create new Product for level 1,2 | 18:52 | ? | https://www.youtube.com/watch?v=57fGKY_zbT4 |
| 564 | 2023-10 | GPT-4 - How to use GPT-4 for FREE without limits and NO REGISTRATION REQUIRED \| CHAT GPT-4 | 7:42 | 73000 | https://www.youtube.com/watch?v=8y-DSOnMnO0 |
| 571 | 2023-10 | Sau khi lướt qua 100 CV thì tôi nghĩ Lập Trình Viên nên theo PHƯƠNG PHÁP này (Mẫu CV đính kèm) | 12:32 | 15000 | https://www.youtube.com/watch?v=boOhNAhgOk8 |
| 575 | 2023-10 | Implementing the best code with load balancing and API gateways \| The Programmer's Path \| 22 | 7:45 | 22000 | https://www.youtube.com/watch?v=dQAXlR77cEk |
| 589 | 2023-10 | 5 chiến lược triển khai NÂNG CAO khi di chuyển hệ thống BackEnd CŨ sang MỚI: Hướng dẫn toàn diện. | 18:17 | 2600 | https://www.youtube.com/watch?v=j0dchuY2DSk |
| 591 | 2023-10 | CHATGPT (Microsoft) vs BARD (Google) Cùng HỎI một CÂU nhưng CÓ sự khác biệt? Lần này BARD ghi điểm ? | 12:46 | 2300 | https://www.youtube.com/watch?v=OvUliuwLJMg |
| 596 | 2023-10 | 5 dấu hiệu cho thấy LẬP TRÌNH VIÊN nên thay đổi môi trường MỚI và thời điểm thích hợp | 17:16 | 7000 | https://www.youtube.com/watch?v=th3WJqnryoc |
| 606 | 2023-10 | ChatGPT nó quá thông minh có thể lập trình viên  và một số ngành khác sẽ thất nghiệp ??? | 14:30 | 20000 | https://www.youtube.com/watch?v=ICB80lXwcwQ |
| 609 | 2023-10 | Hai phương pháp hay nhất quản lý Your Version API Backend một cách hiệu quả nếu bạn là một Dev BE. | 21:41 | 5000 | https://www.youtube.com/watch?v=jSWkGTvZeco |
| 614 | 2023-10 | Elon Musk Just leaving Twitter HQ code review and redraw by ANONYSTICK.COM | 0:48 | 2800 | https://www.youtube.com/watch?v=hR6nUoP_sj0 |
| 619 | 2023-10 | What is your SALARY expectation? And my 3 answers that will make the Recruiter think? | 12:37 | 14000 | https://www.youtube.com/watch?v=mtQGdn1Y3WQ |
| 623 | 2023-10 | Show doanh thu KHỦNG trên youtube khi đạt 10.000 Subscribers và LỜI CẢM ƠN ANH CHỊ DEVELOPERS. | 9:14 | 4000 | https://www.youtube.com/watch?v=uCu5F7FBA1A |
| 643 | 2022-10 | Api Gateway kết hợp Backend for FrontEnd (BFF) như HỔ mọc thêm CÁNH \| Lộ trình trở thành Backend. | 0:58 | 8200 | https://www.youtube.com/watch?v=_KE9VYR8rXE |
| 644 | 2022-10 | High Availability là gì? Tiết lộ CÔNG THỨC tính cho phép hệ thống DIE mỗi NĂM  vs 3 cách triển khai | 18:42 | 6100 | https://www.youtube.com/watch?v=EKLVEQs3USA |
| 645 | 2022-10 | Cách thiết kế hệ thống BackEnd mở rộng hàng triệu người sử dụng (2) | 19:11 | 18000 | https://www.youtube.com/watch?v=QAW9YFidqn8 |
| 647 | 2022-10 | Proxy Pattern: If you want a raise, give this Pattern to your Boss's Proxy \| Who is this Proxy? | 20:05 | 11000 | https://www.youtube.com/watch?v=Z3mPTWuFw00 |
| 648 | 2022-10 | Facade pattern Vì sao các KỸ SƯ LV4 luôn sử dụng? Còn LV1, 2 hầu như chưa nghe dù chỉ là một lần ??? | 21:17 | 17000 | https://www.youtube.com/watch?v=zK_sNkfzugs |
| 652 | 2022-10 | Observer pattern được sử dụng triển khai news feed trong facebook và cách triển khai DOTA 2 vs IP 14 | 24:39 | 26000 | https://www.youtube.com/watch?v=7J5pRc2vzWk |
| 655 | 2022-10 | Dùng IF ELSE hay SWITCH thế này cho tôi hỏi các bạn LẬP TRÌNH VIÊN, cách CODE của tôi có sai không? | 29:48 | 13000 | https://www.youtube.com/watch?v=-YgvJwcrCrI |
| 659 | 2022-10 | How accurately do systems calculate views if multiple IPs watch videos at the same time \| Backend | 40:26 | 11000 | https://www.youtube.com/watch?v=BKuNdc92ltI |
| 668 | 2022-10 | Design product model \| 90% trang TMĐT đều triển khai theo cách này \| Performance 99% \| app aliconcon | 19:25 | 9600 | https://www.youtube.com/watch?v=1sTAklCy4zk |
| 672 | 2022-10 | How Facebook encodes Videos \| Become a better developer in 10 seconds a day | 0:14 | 6300 | https://www.youtube.com/watch?v=Ig6vJWcm_JI |
| 676 | 2022-10 | Build An eCommerce ALICONCON Using An API, Setup #1 | 11:14 | 8400 | https://www.youtube.com/watch?v=IOorKo7qLYc |
| 689 | 2022-10 | 9 nguồn tin công nghệ mà các Lập Trình Viên và Tôi dành 30 phút mỗi ngày để bước tiếp... | 14:38 | 11000 | https://www.youtube.com/watch?v=tHgAXlWLvmI |
| 696 | 2022-10 | A DEV.to clone using MERN stack by Eknoorpreet | 2:44 | 1000 | https://www.youtube.com/watch?v=HqqV2aSLwqg |
| 704 | 2022-10 | WebGL Water Demo | 0:44 | 2900 | https://www.youtube.com/watch?v=uLBwJpPGBw4 |
| 710 | 2022-10 | Senior sử dụng async await fetch api thực sự pro nhu thế nào? \| FETCH API | 12:42 | 16000 | https://www.youtube.com/watch?v=tf1ko6sBoLY |
| 719 | 2022-10 | What is Throttle Technique? Implement and Understand Through 2 Classic Examples in Programming \| ... | 13:25 | 6200 | https://www.youtube.com/watch?v=vsl4my0Ot-s |
| 732 | 2021-10 | What is HATEOAS? It's a pity to do Rest APIs without it \| Social Media REST API Series (2) | 9:20 | 6600 | https://www.youtube.com/watch?v=ngqwsfMMEEA |
| 764 | 2021-10 | Install ohmyzsh in 1 minute | 5:52 | 620 | https://www.youtube.com/watch?v=YQGOyeic_c8 |
| 780 | 2020-10 | Configure Apache Virtual Hosts in Ubuntu 18.04 LTS | 3:40 | 747 | https://www.youtube.com/watch?v=mKG9AVCklik |
| 785 | 2019-10 | How to rename Alias short name in Terminal On MacBook OS X | 1:14 | 372 | https://www.youtube.com/watch?v=m2KjazaHmSs |
| 786 | 2019-10 | How to fix create-react-app: command not found | 2:57 | 3300 | https://www.youtube.com/watch?v=NFkfrVG_IVI |
