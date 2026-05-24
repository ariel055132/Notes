---
type: concept
aliases: ["database deadlock", "deadlocks", "lock deadlock"]
tags: [system-design, databases, transactions, concurrency]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Deadlock

## Definition

A deadlock occurs when transactions hold locks and wait for one another in a cycle, so none of them can continue until one transaction is rolled back or aborted. [[2026-03-31--database-transactions|Database Transactions]]

## Scope

This concept covers a system-design risk introduced by pessimistic locking and multi-row updates. [[2026-03-31--database-transactions|Database Transactions]] The source recommends acquiring locks in a consistent order, relying on database deadlock detection to abort one participant, and making the application handle retries when a transaction is rolled back. [[2026-03-31--database-transactions|Database Transactions]]

## Contrasts

- **Lost Update**: Lost update happens when conflicting writes overwrite each other; deadlock happens when transactions block each other while trying to prevent conflicts. [[2026-03-31--database-transactions|Database Transactions]]
- **Optimistic Locking**: Optimistic locking can avoid long-held locks, while pessimistic locking can create deadlock risk. [[2026-03-31--database-transactions|Database Transactions]]

## Evidence

- [[2026-03-31--database-transactions|Database Transactions]] — The source explains that transactions locking resources in different orders can deadlock and that databases usually roll back one transaction.

## Related

- [[pessimistic-locking|Pessimistic Locking]]
- [[lost-update|Lost Update]]
- [[transaction-isolation|Transaction Isolation]]
- [[database-transactions|Database Transactions]]

## Open Questions

- Which future source should cover deadlock detection algorithms and lock wait timeout tuning?
