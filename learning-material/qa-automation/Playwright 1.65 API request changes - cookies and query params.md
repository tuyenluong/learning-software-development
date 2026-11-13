---
Creation_date: 2026-11-13 22:30
Modification_date: Friday 13th November 2026 22:30:00
Indexes:
  - "[[permanent_notes]]"
  - "[[QA_Automation]]"
  - "[[Playwright]]"
Source: docs (Playwright 1.65.0 release notes, Node and Python; RFC 6265)
---

----
# Playwright 1.65 API request changes: cookies and query params

> **Source type: official release notes**, checked 2026-11-13: Playwright **1.65.0** for Node (5 Nov 2026) and Python (9 Nov 2026). Builds on [Playwright API testing (APIRequestContext)](module-1/Playwright%20API%20testing%20(APIRequestContext).md).

## Why this matters for API tests

Two changes in 1.65 alter what an `APIRequestContext` request actually sends. A suite that passed on 1.64 can go red on 1.65 without any change in the app under test. Often the new result is the correct one.

## 1. Cookie matching follows RFC 6265

When you pass a URL, `browserContext.cookies()` and `apiRequestContext.cookies()` now use the same domain and path rules a browser uses:

| Cookie | Request URL | 1.64 | 1.65 |
|---|---|---|---|
| Host-only cookie for `api.example.com` (no `Domain` attribute) | `https://eu.api.example.com/...` | returned | **not returned** |
| `Path=/api` | `/apiv2/orders` | returned | **not returned** (path must match on a `/` boundary) |
| `Path=/foo/` | `/foo` | returned | **not returned** |

Also:
- A cookie without a name is sent as `Cookie: x`, not `Cookie: =x`.
- `Set-Cookie: token` (no `=`) is stored as a cookie **without a name** and value `token`.

**Test-design takeaway:** a session or CSRF cookie that "worked" across `/api` and `/apiv2`, or across subdomains, was leaking. Real browsers would not send it. If a test fails after the upgrade, check the `Set-Cookie` header the server returns (`Domain`, `Path`) before changing the test.

```ts
// Assert cookie scope explicitly instead of relying on leakage
const res = await request.post('/api/login', { data: { user: 'u1', pass: 'p1' } });
expect(res.ok()).toBeTruthy();

const forApi = await request.storageState();
const session = forApi.cookies.find(c => c.name === 'session');
expect(session?.path).toBe('/api');   // scoped as the server intends
```

## 2. `params` are appended to an existing query

String values of the `params` option (and `URLSearchParams` in Node) are now **appended** to a query the URL already has, instead of replacing it.

```ts
// 1.64: sent /orders?status=paid   (page=2 dropped)
// 1.65: sent /orders?page=2&status=paid
await request.get('/orders?page=2', { params: 'status=paid' });
```

**Test-design takeaway:** pick one place to build the query. Either put everything in `params`, or everything in the URL. A test that mixed both and asserted on "status only" results can now pass extra filters to the server.

## 3. Python-only notes (1.65.0)

- Proxy credentials in the `proxy` option now answer **only** proxy challenges. For site auth use `http_credentials`.
- The Python client is now a line-by-line port of the Node client, so the two behave the same way.

## Upgrade checklist for an API suite

1. Search tests for `cookies(` calls with a URL and for hard-coded `Cookie:` headers.
2. Search for requests that pass both a `?` in the URL and a `params` option.
3. Run the suite once on 1.64 and once on 1.65; diff the failures.
4. For each new failure, read the server's `Set-Cookie` or the final request URL in the trace before touching the assertion.

## Exercise

1. Stand up a small server that sets `session` with `Path=/api` on `POST /api/login`, and exposes `GET /api/me` and `GET /apiv2/me`, both requiring the cookie.
2. Write two Playwright API tests: `/api/me` returns 200; `/apiv2/me` returns 401. Run on 1.65 and confirm both pass.
3. Change the server to `Path=/` and watch the second test fail; that is the point: the test now pins cookie scope as a requirement.
4. Add `GET /orders?page=2` with `params: 'status=paid'` and assert the server received both `page` and `status`.

## Sources
- [Playwright 1.65.0 release notes (Node)](https://github.com/microsoft/playwright/releases/tag/v1.65.0)
- [Playwright for Python 1.65.0 release notes](https://github.com/microsoft/playwright-python/releases/tag/v1.65.0)
- [Playwright: APIRequestContext](https://playwright.dev/docs/api/class-apirequestcontext)
- [Playwright: API testing](https://playwright.dev/docs/api-testing)
- [RFC 6265: HTTP State Management Mechanism](https://www.rfc-editor.org/rfc/rfc6265) (sections 5.1.3 domain matching and 5.1.4 path matching)
- Related note: [Playwright 1.65 exclusive lock and failure reporters](Playwright%201.65%20exclusive%20lock%20and%20failure%20reporters.md)
