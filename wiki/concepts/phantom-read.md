---
type: concept
aliases: ["phantom reads", "phantom row"]
tags: [system-design, databases, transactions, concurrency]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Phantom Read

## Definition

A phantom read occurs when one transaction repeats the same range query and sees a different set of rows because another transaction committed an insert or delete in that range. [[2026-03-31--database-transactions|Database Transactions]]

## Scope

This concept covers result-set instability rather than a changed value on one already-read row. [[2026-03-31--database-transactions|Database Transactions]] It matters in system design when range predicates encode business rules, counts, uniqueness checks, capacity windows, reservations, or other constraints that can be invalidated by concurrent row creation. [[2026-03-31--database-transactions|Database Transactions]]

## Contrasts

- **Non-Repeatable Read**: Non-repeatable read changes a row's value, while phantom read changes which rows match a repeated query. [[2026-03-31--database-transactions|Database Transactions]]
- **Serializable Isolation**: Serializable isolation prevents phantom reads; weaker isolation levels may allow them. [[2026-03-31--database-transactions|Database Transactions]]

## Evidence

- [[2026-03-31--database-transactions|Database Transactions]] — The source uses a repeated query for accounts above a balance threshold where another transaction inserts a new matching account.

## Related

- [[transaction-isolation|Transaction Isolation]]
- [[repeatable-read|Repeatable Read]]
- [[serializable-isolation|Serializable Isolation]]
- [[non-repeatable-read|Non-Repeatable Read]]
- [[dirty-read|Dirty Read]]

## Open Questions

- Which future source should cover predicate locks, next-key locks, and range locks?
