---
type: concept
aliases: ["nonrepeatable read", "non-repeatable reads"]
tags: [system-design, databases, transactions, concurrency]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Non-Repeatable Read

## Definition

A non-repeatable read occurs when one transaction reads the same row twice and sees different values because another transaction committed an update between the reads. [[2026-03-31--database-transactions|Database Transactions]]

## Scope

This concept covers row-level instability inside a transaction. [[2026-03-31--database-transactions|Database Transactions]] The source distinguishes it from phantom read by pointing out that non-repeatable read changes the value of a row already in the result set, while phantom read changes which rows are in a range-query result set. [[2026-03-31--database-transactions|Database Transactions]]

## Contrasts

- **Dirty Read**: Non-repeatable read sees committed data at both times, while dirty read sees uncommitted data. [[2026-03-31--database-transactions|Database Transactions]]
- **Phantom Read**: Non-repeatable read changes the value of the same row, while phantom read changes the membership of a range query's result set. [[2026-03-31--database-transactions|Database Transactions]]

## Evidence

- [[2026-03-31--database-transactions|Database Transactions]] — The source shows one transaction reading an account balance, another transaction committing an update, and the first transaction seeing a different value on the second read.

## Related

- [[transaction-isolation|Transaction Isolation]]
- [[read-committed|Read Committed]]
- [[repeatable-read|Repeatable Read]]
- [[dirty-read|Dirty Read]]
- [[phantom-read|Phantom Read]]

## Open Questions

- None.
