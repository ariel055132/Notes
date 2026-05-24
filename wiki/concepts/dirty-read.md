---
type: concept
aliases: ["dirty reads"]
tags: [system-design, databases, transactions, concurrency]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Dirty Read

## Definition

A dirty read occurs when one transaction reads another transaction's uncommitted data, and that data may later be rolled back. [[2026-03-31--database-transactions|Database Transactions]]

## Scope

This concept covers the weakest and most dangerous read anomaly in the source because it lets a transaction reason from data that may never become committed database state. [[2026-03-31--database-transactions|Database Transactions]] It is directly allowed by Read Uncommitted and prevented by Read Committed or stronger isolation levels. [[2026-03-31--database-transactions|Database Transactions]]

## Contrasts

- **Non-Repeatable Read**: Dirty read observes uncommitted data, while non-repeatable read observes two different committed values inside one transaction. [[2026-03-31--database-transactions|Database Transactions]]
- **Phantom Read**: Dirty read concerns uncommitted values, while phantom read concerns changed result sets from committed inserts or deletes. [[2026-03-31--database-transactions|Database Transactions]]

## Evidence

- [[2026-03-31--database-transactions|Database Transactions]] — The source gives an account-balance example where a transaction reads a value that another transaction later rolls back.

## Related

- [[transaction-isolation|Transaction Isolation]]
- [[read-uncommitted|Read Uncommitted]]
- [[read-committed|Read Committed]]
- [[non-repeatable-read|Non-Repeatable Read]]
- [[phantom-read|Phantom Read]]

## Open Questions

- None.
