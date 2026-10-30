import re
# (key, label, regex) in LEARNING ORDER (foundations first)
TOPICS = [
 ("mq",      "1. Message queues & RabbitMQ (foundations)", r"rabbit|message queue|\bMQ\b|work queue|fanout|pub/?sub|publish.?subscribe|message order|message error|\bTTL\b|\bSQS\b|notification"),
 ("kafka",   "2. Kafka & event streaming", r"kafka|debezium|\bCDC\b|event[- ]driven"),
 ("tx",      "3. Transactions, isolation, locks & DB concurrency", r"transaction|giao dịch|ACID|isolation|MVCC|deadlock|race condition|optimistic|pessimistic|select for update|lock|concurren|đồng thời|inventory|tồn kho|stock|oversell"),
 ("dist",    "4. Idempotency, consistency & distributed transactions (saga/outbox)", r"idempot|saga|outbox|consisten|nhất quán|duplicate|distributed|phân tán|CAP\b|retry|replay|exactly"),
 ("redis",   "5. Redis & caching", r"redis|cache|valkey|lua|sentinel|redisearch"),
 ("db",      "6. MySQL / PostgreSQL / MongoDB / Elasticsearch", r"mysql|postgres|mongo|sql\b|index|pagination|partition|shard|replication|elastic|query|database|CSDL|\b[123]NF\b|join|table"),
 ("sd",      "7. System design, architecture & interviews", r"system design|architect|kiến trúc|microservice|DDD|scale|req/s|QPS|rate limit|circuit breaker|grpc|interview|phỏng vấn|high concurr|throughput|SOLID|design pattern"),
 ("go",      "8. Go (Golang)", r"\bGO\b|golang|goroutine|gin\b|\bGORM\b|sqlc|goose"),
 ("java",    "9. Java & Spring Boot", r"java|spring|jpa|mybatis|thread|virtual thread"),
 ("node",    "10. Node.js / NestJS / JavaScript", r"node|nest|javascript|\bJS\b|express|promise|event loop|typescript|ecmascript|shopdev|section \d+"),
 ("ops",     "11. DevOps, cloud, monitoring & logging", r"docker|kubernetes|k8s|aws|ec2|s3|cloudfront|nginx|ci/cd|prometheus|grafana|log|pm2|linux|cpu|etcd|monitor|giám sát"),
 ("sec",     "12. Security & auth", r"jwt|security|auth|rbac|token|otp|hack|idor|api key|x-api-key|password|permission|quyền|cookie"),
 ("ai",      "13. AI & tools", r"\bAI\b|claude|mcp|openai|notebooklm|vector|vs ?code|tool|git"),
 ("career",  "14. Career, soft skills & other (NoCODE)", r"."),
]
def topic(title):
    for k,l,r in TOPICS:
        if re.search(r, title, re.I): return k
