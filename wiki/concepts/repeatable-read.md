---
type: concept
aliases: ["repeatable read isolation"]
tags: [system-design, databases, transactions, concurrency]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Repeatable Read

## Definition

Repeatable Read is an isolation level where repeated reads of the same row within one transaction return the same value even if another transaction commits an update in the meantime. [[2026-03-31--database-transactions|Database Transactions]]

## Scope

This concept covers stronger read stability than Read Committed while usually preserving more concurrency than full Serializable isolation. [[2026-03-31--database-transactions|Database Transactions]] The source names MySQL InnoDB's default isolation level as Repeatable Read and explains it using snapshot-style behavior. [[2026-03-31--database-transactions|Database Transactions]]

## Contrasts

- **Read Committed**: Read Committed can show a different value on a later statement, while Repeatable Read keeps the same row stable inside a transaction. [[2026-03-31--database-transactions|Database Transactions]]
- **Serializable Isolation**: Serializable is stronger because it prevents phantom reads as well as dirty and non-repeatable reads. [[2026-03-31--database-transactions|Database Transactions]]

## Evidence

- [[2026-03-31--database-transactions|Database Transactions]] — The source describes Repeatable Read as preventing repeated reads of the same row from changing inside one transaction.

## Related

- [[transaction-isolation|Transaction Isolation]]
- [[non-repeatable-read|Non-Repeatable Read]]
- [[phantom-read|Phantom Read]]
- [[multi-version-concurrency-control|Multi-Version Concurrency Control]]
- [[serializable-isolation|Serializable Isolation]]

## Open Questions

- Which future source should distinguish snapshot isolation from SQL-standard Repeatable Read?
