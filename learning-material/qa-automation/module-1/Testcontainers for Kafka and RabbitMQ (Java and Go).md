---
Creation_date: 2026-10-21 17:40
Modification_date: Wednesday 21st October 2026 17:40:00
Indexes:
  - "[[permanent_notes]]"
  - "[[QA_Automation]]"
  - "[[Message_Queues]]"
  - "[[Kafka]]"
  - "[[Java_Spring]]"
  - "[[Module 1 - QA Automation for Edge Cases]]"
Source: docs (Testcontainers for Java 2.0.5 docs + 2.0.0 release notes, Spring Boot 4.1 Testcontainers reference, Testcontainers for Go v0.44.0 module docs and source, GitHub Actions runner images)
---

----
# QA Lesson 4: Testcontainers for Kafka and RabbitMQ (Java and Go)

> **Source type: official docs and source code**, checked 2026-10-21. Versions: **Testcontainers for Java 2.0.5**, **Spring Boot 4.1.1** (`spring-boot-testcontainers`), **Testcontainers for Go v0.44.0**, images `apache/kafka:4.3.2`, `rabbitmq:4.3-management` (4.4.0 is 3 days old), `postgres:18-alpine`. This is where lesson 1's invariants become real tests: a **real** broker and DB in Docker, started by the test, thrown away after.

## The idea
Mocks can't show you a duplicate redelivery, a requeue loop or a DLX that doesn't exist. Testcontainers starts real Docker containers from your test code, waits until they're ready, gives you their random host ports, and removes them afterwards (a helper container called **Ryuk** cleans up even if the JVM/process dies; [configuration](https://java.testcontainers.org/features/configuration/)). Your Jenkins/GitHub Actions agent just needs Docker.

## Java: Testcontainers 2.x changes (if you've seen 1.x examples online)
From the [2.0.0 release notes](https://github.com/testcontainers/testcontainers-java/releases/tag/2.0.0):
- **Artifacts are prefixed:** `org.testcontainers:testcontainers-kafka`, `testcontainers-rabbitmq`, `testcontainers-postgresql`, `testcontainers-junit-jupiter` (all 2.0.5). Use the `testcontainers-bom` to keep them in sync.
- **Classes moved to `org.testcontainers.<module>`:** `org.testcontainers.kafka.KafkaContainer` (for `apache/kafka` and `apache/kafka-native`), `org.testcontainers.kafka.ConfluentKafkaContainer` (for `confluentinc/cp-kafka` ≥ 7.4.0), `org.testcontainers.rabbitmq.RabbitMQContainer`, `org.testcontainers.postgresql.PostgreSQLContainer`. The old `org.testcontainers.containers.*` classes still exist but are deprecated ([Kafka module](https://java.testcontainers.org/modules/kafka/)).
- **JUnit 4 support removed.** JUnit 5/6 via `@Testcontainers` + `@Container`; **TestNG** has no extension, so start containers yourself in `@BeforeClass`/`@BeforeSuite` (or a static singleton) and stop them in `@AfterSuite`.

## Java: Spring Boot `@ServiceConnection`
Spring Boot reads the container's host/port and wires the app to it, no `application-test.yml` URLs needed. Per the [Spring Boot Testcontainers reference](https://docs.spring.io/spring-boot/reference/testing/testcontainers.html), `@ServiceConnection` creates:
- `KafkaConnectionDetails` from `KafkaContainer`, `ConfluentKafkaContainer` or `RedpandaContainer`
- `RabbitConnectionDetails` from `RabbitMQContainer`
- `JdbcConnectionDetails` + `R2dbcConnectionDetails` from `PostgreSQLContainer`

**Prefer containers as Spring beans** (or `@ImportTestcontainers`). The docs warn that with the JUnit extension, static containers stop after the test class, but Spring **caches the ApplicationContext** and may reuse it in a later class, whose beans then point at a stopped container. Beans live as long as the cached context. This also works under TestNG (`AbstractTestNGSpringContextTests`), since Spring, not JUnit, owns the lifecycle.

```java
// src/test/java/.../TestInfra.java
@TestConfiguration(proxyBeanMethods = false)
class TestInfra {
    @Bean @ServiceConnection
    KafkaContainer kafka() { return new KafkaContainer("apache/kafka:4.3.2"); }

    @Bean @ServiceConnection
    RabbitMQContainer rabbit() { return new RabbitMQContainer("rabbitmq:4.3-management"); }

    @Bean @ServiceConnection
    PostgreSQLContainer postgres() { return new PostgreSQLContainer("postgres:18-alpine"); }
}

// A Kafka poison-message test (lesson 1, invariants 4 and 5). Assumes the app configures
// ErrorHandlingDeserializer + DefaultErrorHandler with a DeadLetterPublishingRecoverer (see Spring Kafka note)
@SpringBootTest
@Import(TestInfra.class)
class PaymentsConsumerIT {
    @Autowired KafkaTemplate<String, String> kafka;
    @Autowired JdbcTemplate db;
    @Autowired ConsumerFactory<String, String> cf;

    @Test
    void poisonGoesToDltOnceAndNextMessageIsProcessed() {
        String id = "pay-" + UUID.randomUUID();
        kafka.send("payments", "k1", "{not json");                         // poison
        kafka.send("payments", "k1", "{\"paymentId\":\"" + id + "\",\"amount\":100}");

        try (Consumer<String, String> dlt = cf.createConsumer("qa-dlt-" + id, null)) {
            dlt.subscribe(List.of("payments-dlt"));                          // Spring Kafka 3.3+ default suffix
            await().atMost(Duration.ofSeconds(20)).untilAsserted(() -> {     // lesson 5
                var records = KafkaTestUtils.getRecords(dlt, Duration.ofSeconds(1));
                assertThat(records.count()).isEqualTo(1);
            });
        }
        await().atMost(Duration.ofSeconds(20)).untilAsserted(() ->
            assertThat(db.queryForObject("select count(*) from payments where payment_id = ?", Integer.class, id)).isEqualTo(1));
    }
}
```
(`KafkaTestUtils` is in `spring-kafka-test`. Give each test's consumer its own group id, or tests read each other's records.)

**RabbitMQ: assert requeue vs dead-letter.** Declare the queue with a DLX in the test (or rely on the app's declarations) and check `x-death` on the DLQ copy:
```java
@Test
void permanentFailureIsDeadLetteredNotRequeuedForever(@Autowired RabbitTemplate rabbit) {
    rabbit.convertAndSend("orders.exchange", "orders.created", "{\"orderId\":\"bad\",\"amount\":-1}"); // validation fails
    await().atMost(Duration.ofSeconds(15)).untilAsserted(() -> {
        Message dead = rabbit.receive("orders.dlq", 500);
        assertThat(dead).isNotNull();
        List<Map<String, ?>> xDeath = dead.getMessageProperties().getHeader("x-death");
        assertThat(xDeath.get(0).get("reason")).isEqualTo("rejected");    // not "delivery_limit"
    });
}
```
If the reason comes back `delivery_limit`, the app is requeueing (Spring AMQP's `defaultRequeueRejected=true` default) until the quorum queue's limit (20 since RabbitMQ 4.0) kicks in: a bug worth reporting. With *no* DLX, that message just vanishes. See [[Test design for messaging and transaction edge cases]].

## Go: testcontainers-go
Each module has a `Run(ctx, image, opts...)` function (the older `RunContainer` is deprecated). Clean up with `testcontainers.CleanupContainer(t, ctr)` (registers `t.Cleanup`) or `testcontainers.TerminateContainer(ctr)`. Sources: [Kafka module](https://golang.testcontainers.org/modules/kafka/), [RabbitMQ module](https://golang.testcontainers.org/modules/rabbitmq/), [Postgres module](https://golang.testcontainers.org/modules/postgres/).
- `rabbitmq.Run(ctx, "rabbitmq:4.3-management", rabbitmq.WithAdminUsername("admin"), rabbitmq.WithAdminPassword("pw"))` → `ctr.AmqpURL(ctx)`.
- `postgres.Run(ctx, "postgres:18-alpine", postgres.WithDatabase("app"), postgres.WithUsername("u"), postgres.WithPassword("p"), postgres.BasicWaitStrategies())` → `ctr.ConnectionString(ctx, "sslmode=disable")`. It also has `Snapshot`/`Restore` to reset the DB between tests fast.
- **Gotcha: the Go Kafka module is built on Confluent's image**, not `apache/kafka`. Its start script runs `/etc/confluent/docker/...`, the docs example uses `confluentinc/confluent-local:7.5.0`, and it refuses `confluent-local` tags below 7.4.0 (KRaft). `kafka.Run(ctx, "confluentinc/confluent-local:7.5.0", kafka.WithClusterID("test"))` → `ctr.Brokers(ctx)`. (Read in the v0.44.0 source, `modules/kafka/kafka.go`.)

```go
// duplicate_test.go: a duplicate delivery must produce one row
func TestDuplicateOrderMessageIsAppliedOnce(t *testing.T) {
    ctx := context.Background()
    rmq, err := rabbitmq.Run(ctx, "rabbitmq:4.3-management")
    testcontainers.CleanupContainer(t, rmq)
    require.NoError(t, err)
    pg, err := postgres.Run(ctx, "postgres:18-alpine", postgres.BasicWaitStrategies())
    testcontainers.CleanupContainer(t, pg)
    require.NoError(t, err)

    amqpURL, _ := rmq.AmqpURL(ctx)
    dsn, _ := pg.ConnectionString(ctx, "sslmode=disable")
    app := startConsumer(t, amqpURL, dsn)                       // your service, in-process

    body := []byte(`{"orderId":"o-1","amount":100}`)
    msg := amqp091.Publishing{MessageId: "msg-1", ContentType: "application/json", Body: body}
    publish(t, amqpURL, "orders", msg)
    publish(t, amqpURL, "orders", msg)                          // same MessageId = duplicate

    require.EventuallyWithT(t, func(c *assert.CollectT) {       // lesson 5: no time.Sleep
        assert.Equal(c, 1, app.CountOrders("o-1"))
    }, 10*time.Second, 200*time.Millisecond)
}
```
(Client libs: `github.com/rabbitmq/amqp091-go` v1.16.0, `github.com/twmb/franz-go` v1.22.2 for Kafka.)

## Startup cost and reuse
- Each container takes seconds to start (Kafka and RabbitMQ are the slow ones). **Start once per suite, not per test**: Spring beans + context caching, a static singleton (Java), or `TestMain` (Go). Isolate tests with **unique topics/queues/ids** (lesson 3) instead of fresh containers.
- **Reusable containers** (Java) keep containers running *between* runs: opt in with `testcontainers.reuse.enable=true` in `~/.testcontainers.properties` (or `TESTCONTAINERS_REUSE_ENABLE=true`) plus `.withReuse(true)` and a manual `start()`. It's **experimental** and the docs say it's **not suited for CI** ([Reusable Containers](https://java.testcontainers.org/features/reuse/)). Use it on your laptop only.
- `apache/kafka-native` (GraalVM native build, also supported by `KafkaContainer`) is meant for local dev/testing and starts faster than the JVM image; compare both on your machine before switching.
- Pin image tags (`4.3.2`, not `latest`) so a new broker release doesn't change behaviour under you overnight.

## Docker in CI
- **GitHub Actions:** `ubuntu-latest` (= Ubuntu 24.04) hosted runners ship Docker server and client 28.x ([runner image readme](https://github.com/actions/runner-images/blob/main/images/ubuntu/Ubuntu2404-Readme.md)), so Testcontainers works with no extra setup. Don't use macOS runners for this.
- **Jenkins:** the agent needs a Docker daemon the build user can reach (`/var/run/docker.sock` or `DOCKER_HOST`). On Kubernetes agents that usually means a Docker-in-Docker sidecar or a remote Docker host; Testcontainers documents the patterns in [Patterns for running tests inside a Docker container](https://java.testcontainers.org/supported_docker_environment/continuous_integration/dind_patterns/). If Ryuk can't run privileged there, `TESTCONTAINERS_RYUK_DISABLED=true` turns it off, and then cleanup is on you.
- Pull images once per agent (or use a registry mirror) to avoid Docker Hub rate limits.

## What breaks / how to test it
- **Context-cached container stopped** → "connection refused" in the *second* test class only. Fix: containers as beans.
- **Tests share topics/queues** → a test consumes another test's message. Unique names per test, or filter by id.
- **Consumer not ready when the test publishes** → first message missed (Kafka `auto.offset.reset=latest`) → wait for partition assignment or use `earliest` in tests (lesson 5).
- **DLT has fewer partitions than the source topic** → DLT publish fails for high partitions (the recoverer uses the same partition number). Create test topics with the same partition count.
- **Fault injection:** `container.stop()` / `docker pause` mid-test to simulate a broker outage, then assert the outbox/retry catches up with no duplicates. Toxiproxy (a Testcontainers module) adds latency or cuts connections between app and broker.

## How it maps to the learning focus
- **Core focus:** duplicates, poison messages, DLQ/DLT routing, requeue loops, broker failures, all reproduced against real brokers.
- **Your QA work:** your AWS checks (S3, DynamoDB, Lambda) can use the same approach with the LocalStack module; the pattern (real dependency in a container, assert the effect) is identical.

## Related
[[Module 1 - QA Automation for Edge Cases]] · [[Test design for messaging and transaction edge cases]] · [[Spring Kafka retries and dead-letter topics]] · [[hrSP7UocdJ8]] · [[az2VNMgNFrk]] · [[Framework structure - fixtures and test data]]

---
## Flash cards section
What changed in Testcontainers for Java 2.0?::Artifacts got a testcontainers- prefix (testcontainers-kafka), classes moved to org.testcontainers.<module> (org.testcontainers.kafka.KafkaContainer), and JUnit 4 support was removed.
What does @ServiceConnection do in Spring Boot?::It turns a container into ConnectionDetails beans (Kafka, Rabbit, JDBC…) so the app connects to the container's random host/port without manual properties.
Why prefer containers as Spring beans over static @Container fields in Spring Boot tests?::Spring caches the ApplicationContext across test classes; a JUnit-managed container may already be stopped when a later class reuses the context. Beans live as long as the context.
Which image does the testcontainers-go Kafka module expect?::Confluent's confluentinc/confluent-local (7.4.0+ for KRaft; docs use 7.5.0), not apache/kafka. The Java KafkaContainer takes apache/kafka.
Should you use reusable containers in CI?::No. withReuse(true) is experimental and the docs say it isn't suited for CI. Use it locally; in CI start once per suite.
A RabbitMQ DLQ message has x-death reason delivery_limit instead of rejected. What does it tell you?::The app is requeueing failures until the quorum queue delivery limit (default 20 since 4.0) is hit, instead of rejecting without requeue.
