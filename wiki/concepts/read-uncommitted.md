---
type: concept
aliases: ["read uncommitted isolation"]
tags: [system-design, databases, transactions, concurrency]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Read Uncommitted

## Definition

Read Uncommitted is the lowest isolation level, allowing a transaction to read data another transaction has written but not yet committed. [[2026-03-31--database-transactions|Database Transactions]]

## Scope

This concept covers an isolation choice that maximizes permissiveness but allows dirty reads, non-repeatable reads, and phantom reads. [[2026-03-31--database-transactions|Database Transactions]] The source describes it as dangerous because a transaction may observe data that is later rolled back and therefore never truly existed as committed database state. [[2026-03-31--database-transactions|Database Transactions]]

## Contrasts

- **Read Committed**: Read Committed prevents dirty reads, while Read Uncommitted permits them. [[2026-03-31--database-transactions|Database Transactions]]
- **Serializable Isolation**: Serializable prevents the listed read anomalies, while Read Uncommitted permits all of them. [[2026-03-31--database-transactions|Database Transactions]]

## Evidence

- [[2026-03-31--database-transactions|Database Transactions]] — The source says Read Uncommitted can read uncommitted writes and is rarely used in production.

## Related

- [[transaction-isolation|Transaction Isolation]]
- [[dirty-read|Dirty Read]]
- [[read-committed|Read Committed]]
- [[repeatable-read|Repeatable Read]]
- [[serializable-isolation|Serializable Isolation]]

## Open Questions

- None.
