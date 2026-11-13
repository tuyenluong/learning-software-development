---
Creation_date: 2026-11-13
Modification_date: Friday 13th November 2026
Indexes:
  - "[[permanent_notes]]"
  - "[[QA_Automation]]"
  - "[[Pact contract testing]]"
Source: docs — https://docs.pact.io/consumer; @pact-foundation/pact 17.1.4, Matchers === MatchersV3 since v16; checked 2026-11-13
---

# Matchers

## What is the topic?

Matchers tell Pact which parts of a request or response must be compared loosely. Instead of saying "status must be the string `PAID`," you say "status is a string, and `PAID` is an example." The example is what the mock server returns to the consumer test; the matcher is what the provider must satisfy later.

Since v16, `Matchers` is the same export as `MatchersV3`. Common names: `like`, `eachLike`, `atLeastOneLike`, `integer`, `decimal`, `string`, `boolean`, `regex(pattern, example)`, `datetime` / `timestamp`, `uuid`, and `fromProviderState`.

Do not use the V2 names `term` or `somethingLike`. They are not part of the V3/V4 matcher API.

## What does it do?

- On the consumer side, the mock still returns a concrete example, so your client has a real body to parse.
- On the provider side, verification checks the *type / pattern*, not that every field equals the example.
- They keep the contract honest: you match only what the consumer relies on.

The rule from the [consumer docs](https://docs.pact.io/consumer): "Only include data and operations used by the consumer." A matcher on a field the client never reads still couples the provider to that field. Leave unused fields out entirely.

Pact checks message shape, not business logic. `integer(42)` does not mean "this order is always id 42." It means "this field is an integer, and 42 is a sample."

## How does it work?

A few matchers you will reach for first:

| Matcher | Meaning | Example value the mock returns |
| --- | --- | --- |
| `like(value)` | same type as `value` | `value` |
| `integer(n)` / `decimal(n)` | integer / decimal number | `n` |
| `string(s)` / `boolean(b)` | string / boolean | `s` / `b` |
| `eachLike(item)` | a non-empty array of items like `item` (min 1) | `[item]` |
| `atLeastOneLike(item)` | array with at least one matching item | `[item]` |
| `regex(pattern, example)` | string matching the pattern | `example` |
| `uuid(example)` | a UUID | `example` |
| `datetime` / `timestamp` | a date-time string | the example you pass |
| `fromProviderState(expression, example)` | value injected from provider state | `example` in the consumer test |

`fromProviderState` is how a consumer avoids hard-coding an id that only the provider can create. The provider's state handler returns values; verification substitutes them. You will wire the handler in lesson 4.

`like` is a type matcher, not a "close enough" matcher for any structure you have not looked at. If you wrap a whole object in `like`, you are still saying every key inside is part of the contract — so still drop keys the consumer ignores.

Compared with Pact JVM, names differ: JVM `integerType`, `stringType`, `decimalType`, `booleanType`, and `stringMatcher` are `integer`, `string`, `decimal`, `boolean`, and `regex` here.

## Step-by-step: how do I achieve the goal?

1. Open the client code (not the API docs) and list every field it reads from the response, and every field it sends on the request.
2. For each field, decide: exact value (a literal only when the client truly depends on that constant), or a shape matcher.
3. Prefer `integer`, `decimal`, `string`, `boolean`, `regex`, `uuid`, and `datetime` over a bare `like` when you know the type.
4. For arrays the client iterates, use `eachLike` or `atLeastOneLike`. Do not require three example items if the client only needs "one or more."
5. Delete any field you listed that the client does not actually use. If you cannot find a read in the client, it does not belong.
6. Put the matchers in `jsonBody` (and request body, if any). Run the consumer test and open the pact file — you should see matcher metadata, not only literal JSON.

## What is its usage?

- Loosen ids, timestamps, and generated strings so provider verification does not fail on a new UUID.
- Keep enums the client branches on tight enough (often `like('PAID')` or `regex`) that a type change still fails.
- Use `fromProviderState` when the provider must supply a real id, token, or path parameter at verify time.
- Never use matchers to encode "total must be 19.99" as a business rule. That is a functional assertion, in a functional test.

## Examples / code

The body below is deliberately unfinished. Replace every `/* ? */` and delete any field CheckoutWeb does not read. Do not invent a complete, copy-ready body.

```ts
import { Matchers } from '@pact-foundation/pact';

const {
  like,
  eachLike,
  atLeastOneLike,
  integer,
  decimal,
  string,
  boolean,
  regex,
  uuid,
  datetime,
  fromProviderState,
} = Matchers;

// Response the provider can return. The client uses id, status, and items.
// It does not use internalAuditRef. timestamps are displayed as text.
const body = {
  id: /* YOUR TURN: integer? uuid? fromProviderState? Why? */,
  status: /* YOUR TURN: like('PAID') or regex(...)? What does the client branch on? */,
  items: /* YOUR TURN: eachLike or atLeastOneLike? What is the item shape? */,
  // internalAuditRef: 'AUD-99',  // YOUR TURN: keep or delete? Why?
  updatedAt: /* YOUR TURN: datetime / timestamp / string? */,
};

// YOUR TURN: which of these would be a misuse?
// A. integer(42) to prove the order id is always 42
// B. eachLike({ sku: like('SKU-1'), qty: integer(1) }) for a line-item list
// C. like({ ...entire provider swagger payload }) because "the API has these fields"
// Write one sentence for each.
```

Fix the names. Two of these do not belong in a V3/V4 test.

```ts
const broken = {
  // YOUR TURN: rewrite or remove each line. Which two are V2 names?
  id: Matchers.somethingLike(42),
  code: Matchers.term({ matcher: '\\d{4}', generate: '2048' }),
  sku: Matchers.regex('\\w+-\\d+', 'SKU-1'),
};
```

## Check yourself

1. Quote the consumer-docs rule about what to include in a contract. What do you do with a field the client never reads?
2. What is the difference between the example value and the matcher, and which side of the test uses which?
3. Why are `term` and `somethingLike` the wrong names to reach for here?
4. When would you choose `fromProviderState` instead of `integer(42)`?
5. Why is wrapping the provider's entire payload in `like(...)` a problem even though it is a matcher?

## Flashcards

Q:: What is `Matchers` in current `@pact-foundation/pact`?
A:: The same export as `MatchersV3` (since v16).

Q:: What are `term` and `somethingLike`?
A:: V2 matcher names. They are not part of the V3/V4 matcher API. Use `regex` and `like` instead.

Q:: What does Pact check with matchers?
A:: Message shape (types, patterns, required fields the consumer uses), not business logic.
