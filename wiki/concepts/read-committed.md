---
type: concept
aliases: ["read committed isolation"]
tags: [system-design, databases, transactions, concurrency]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Read Committed

## Definition

Read Committed is an isolation level where a transaction can read only data that has already been committed by other transactions. [[2026-03-31--database-transactions|Database Transactions]]

## Scope

This concept covers the common default isolation level used by many databases, including PostgreSQL according to the source. [[2026-03-31--database-transactions|Database Transactions]] It prevents dirty reads but can still allow non-repeatable reads and phantom reads when other transactions commit changes between two reads in the same transaction. [[2026-03-31--database-transactions|Database Transactions]]

## Contrasts

- **Read Uncommitted**: Read Committed hides uncommitted writes, while Read Uncommitted may expose them. [[2026-03-31--database-transactions|Database Transactions]]
- **Repeatable Read**: Repeatable Read keeps repeated reads of the same row stable in a transaction, while Read Committed may return different committed values across statements. [[2026-03-31--database-transactions|Database Transactions]]

## Evidence

- [[2026-03-31--database-transactions|Database Transactions]] — The source identifies Read Committed as preventing dirty reads but not fully preventing other read anomalies.

## Related

- [[transaction-isolation|Transaction Isolation]]
- [[dirty-read|Dirty Read]]
- [[non-repeatable-read|Non-Repeatable Read]]
- [[phantom-read|Phantom Read]]
- [[repeatable-read|Repeatable Read]]

## Open Questions

- Which future source should document statement-level versus transaction-level snapshot behavior in PostgreSQL?
