---
Creation_date: 2026-11-20 22:30
Modification_date: Friday 20th November 2026 22:30:00
Indexes:
  - "[[permanent_notes]]"
  - "[[QA_Automation]]"
  - "[[k6]]"
Source: docs (Grafana k6 v2.4.0 release notes; k6 docs for http.batch, options, thresholds, Counter, expectedStatuses, test lifecycle)
---

----
# Concurrent debit tests with k6: lost updates and double spends

> **Source type: official docs and release notes**, checked 2026-11-20 against **k6 v2.4.0** (12 Nov 2026). The script below was run against a small local wallet API in two modes (unsafe read-check-write and safe check-and-debit). Builds on [Test design for messaging and transaction edge cases](module-1/Test%20design%20for%20messaging%20and%20transaction%20edge%20cases.md) and [Playwright API testing (APIRequestContext)](module-1/Playwright%20API%20testing%20(APIRequestContext).md).

## Why this matters

Wallet and payment postings ask for tests of "debit, credit, rollback", "idempotency and duplicate request handling" and "concurrency and race-condition scenarios", often with k6 named for load. A race test is not a load test. Its goal is to send a few requests **at the same moment** and then check a business invariant, not to measure latency.

The invariant for a debit:

- the balance never goes below zero, **and**
- final balance = starting balance − (sum of accepted debits).

The second rule catches the **lost update**: two requests read the same balance, both pass the check, and both write. The balance can still look valid (for example 0), so a "never negative" check alone misses the bug.

## The k6 pieces you need

| Piece | What it does here | Doc |
|---|---|---|
| `http.batch([...])` | sends the requests of one VU **in parallel** over several TCP connections | [batch](https://grafana.com/docs/k6/latest/javascript-api/k6-http/batch/) |
| `batchPerHost` | max parallel connections per host for a batch; **default 6**, so 10 debits would go out 6 + 4 unless you raise it. `batch` (default 20) is the total cap | [options](https://grafana.com/docs/k6/latest/using-k6/k6-options/reference/#batch-per-host) |
| `shared-iterations`, 1 VU, 1 iteration | runs the race exactly once | [executor](https://grafana.com/docs/k6/latest/using-k6/scenarios/executors/shared-iterations/) |
| `setup()` | creates the wallet once and passes its id to the VU code | [test lifecycle](https://grafana.com/docs/k6/latest/using-k6/test-lifecycle/) |
| `http.setResponseCallback(http.expectedStatuses(...))` | marks `409 insufficient funds` as an *expected* answer so it is not counted in `http_req_failed` | [expectedStatuses](https://grafana.com/docs/k6/latest/javascript-api/k6-http/expected-statuses/) |
| `Counter` + threshold `count==1` | fails the run if more than one debit is accepted | [Counter](https://grafana.com/docs/k6/latest/javascript-api/k6-metrics/counter/), [thresholds](https://grafana.com/docs/k6/latest/using-k6/thresholds/) |
| threshold `checks: ['rate==1']` | turns failed `check()`s into a failed run; checks alone never change the exit code | [thresholds](https://grafana.com/docs/k6/latest/using-k6/thresholds/#fail-a-load-test-using-checks) |

## The test

```javascript
import http from 'k6/http';
import { check } from 'k6';
import { Counter } from 'k6/metrics';

const BASE = __ENV.BASE_URL || 'http://localhost:3000';
const PARALLEL = 10;
const acceptedDebits = new Counter('accepted_debits');

// 201 and 409 are both expected answers here; only other codes count as failed requests.
http.setResponseCallback(http.expectedStatuses(200, 201, 409));

export const options = {
  batchPerHost: PARALLEL, // default is 6, so raise it to send all debits at once
  scenarios: {
    race: { executor: 'shared-iterations', vus: 1, iterations: 1 },
  },
  thresholds: {
    accepted_debits: ['count==1'], // exactly one debit may win
    checks: ['rate==1'],
    http_req_failed: ['rate==0'],
  },
};

export function setup() {
  const res = http.post(`${BASE}/wallets`, JSON.stringify({ balance: 100 }), {
    headers: { 'Content-Type': 'application/json' },
  });
  return { walletId: res.json('id') };
}

export default function (data) {
  const url = `${BASE}/wallets/${data.walletId}/debits`;
  const params = { headers: { 'Content-Type': 'application/json' } };
  const body = JSON.stringify({ amount: 100 });

  // Ten different debits of the full balance, sent in parallel.
  const responses = http.batch(
    Array.from({ length: PARALLEL }, () => ['POST', url, body, params]),
  );
  const accepted = responses.filter((r) => r.status === 201).length;
  acceptedDebits.add(accepted);

  const wallet = http.get(`${BASE}/wallets/${data.walletId}`);
  check(wallet, {
    'balance never goes below zero': (r) => r.json('balance') >= 0,
    'balance matches accepted debits': (r) => r.json('balance') === 100 - 100 * accepted,
  });
}
```

Run it with `k6 run concurrent-debit.js` (add `-e BASE_URL=...` for another host).

## What the two runs showed (k6 v2.4.0, local toy API)

| Server logic | `accepted_debits` | "never below zero" | "matches accepted debits" | k6 exit code |
|---|---|---|---|---|
| read balance → wait 20 ms → check → write | **10** | ✓ (balance 0) | ✗ | **99** (thresholds crossed) |
| check and debit in one step | **1** | ✓ | ✓ | 0 |

The unsafe version accepted ten debits of 100 from a balance of 100 and still ended at 0. Only the "matches accepted debits" check and the `count==1` threshold caught it. Exit code 99 is what CI sees, so the pipeline fails without parsing output.

## Design notes

- **Different requests, not retries.** Each debit here has no idempotency key, so each is a new payment. That is the double-spend test. The duplicate test is different: send the **same** `Idempotency-Key` several times in parallel and expect **one** debit applied and the same response for every copy.
- **Make the window wide in a test environment, not in production code.** Real races are rare per request. A test build or a fault-injection flag that adds a short delay between read and write makes the race reproducible.
- **Assert on the source of truth.** Read the balance (or the ledger rows) after the batch. Counting 2xx responses alone hides a server that answers 201 but writes nothing.
- **Keep it out of the load profile.** Run the race scenario on its own (k6 v2.3+ can select it with `--scenario race`) so a latency threshold elsewhere does not mask a correctness failure.

## Exercise

1. Build a small wallet API with `POST /wallets`, `GET /wallets/:id` and `POST /wallets/:id/debits` (returns 201 or 409). Write it the unsafe way first: read, sleep 20 ms, check, write.
2. Run the script above and confirm k6 exits with 99 and `accepted_debits` is above 1.
3. Fix the server (single atomic check-and-update, for example `UPDATE wallets SET balance = balance - $1 WHERE id = $2 AND balance >= $1` in SQL) and confirm exit code 0.
4. Add a second scenario that sends the same `Idempotency-Key` five times in parallel. Assert one ledger entry, identical response bodies, and final balance = 100 − amount.
5. Raise `PARALLEL` to 30 without changing `batch` and explain why only 20 requests start at once.

## Sources
- [k6 v2.4.0 release notes](https://github.com/grafana/k6/releases/tag/v2.4.0) (12 Nov 2026)
- [k6 v2.3.0 release notes](https://github.com/grafana/k6/releases/tag/v2.3.0) (`--scenario` and `--once` flags)
- [k6: http.batch()](https://grafana.com/docs/k6/latest/javascript-api/k6-http/batch/)
- [k6 options reference: batch, batchPerHost](https://grafana.com/docs/k6/latest/using-k6/k6-options/reference/#batch-per-host)
- [k6: thresholds](https://grafana.com/docs/k6/latest/using-k6/thresholds/)
- [k6: Counter](https://grafana.com/docs/k6/latest/javascript-api/k6-metrics/counter/)
- [k6: expectedStatuses()](https://grafana.com/docs/k6/latest/javascript-api/k6-http/expected-statuses/)
- [k6: test lifecycle](https://grafana.com/docs/k6/latest/using-k6/test-lifecycle/)
- [k6: shared-iterations executor](https://grafana.com/docs/k6/latest/using-k6/scenarios/executors/shared-iterations/)
- Related note: [Race conditions and MySQL stock deduction](../backend-engineering/anonystick/GLqyIqWtRiA.md) (why read-check-write loses updates)
