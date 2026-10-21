# Jacob's review of Module 1 additions 4a-7e (2026-10-21)

Verdict: all approved for teaching. The corrections in 4a, 6a, 7a, 7b and 7c are right (RC readers don't wait, SERIALIZABLE isn't a table lock, consumer shouldn't set published, Stripe keys are client-generated, same-transaction dedup, INSERT IGNORE swallowing other errors, hash partitioning).

## Fixes
- 7e Spring Kafka retries: "Only exceptions that extend RuntimeException are handled" is wrong. Checked exceptions thrown by a listener are wrapped in ListenerExecutionFailedException and go through the error handler too. The real line is Exception vs Error: a java.lang.Error isn't handled the same way.
- 7e DLT naming: please re-check the source for "DeadLetterPublishingRecoverer defaults to <topic>-dlt in 4.x". As far as I know the recoverer's default is still `<topic>.DLT` and `-dlt` is the @RetryableTopic suffix. Cite the exact doc line, or say both and tell the learner to check their version.
- 4b table: in the MySQL SERIALIZABLE column, add that plain SELECTs become FOR SHARE only when autocommit is off (a single autocommitted SELECT stays a snapshot read). 4a already says this.

## Teaching plan
4a+4b and 7a+7b are paired lessons. 7d and 7e are long, so each gets its own day, and the QA test lists in them become night-quiz scenario questions.
