---
type: concept
aliases: ["optimistic concurrency control", "version check", "compare-and-set update"]
tags: [system-design, databases, transactions, concurrency]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Optimistic Locking

## Definition

Optimistic locking is a concurrency-control technique that allows concurrent work to proceed and detects conflicts at update or commit time, commonly by checking a version column. [[2026-03-31--database-transactions|Database Transactions]]

## Scope

This concept covers conflict detection for cases where conflicts are expected to be uncommon. [[2026-03-31--database-transactions|Database Transactions]] The source presents an update with `WHERE id = 1 AND version = 1` as the key idea: if another transaction already changed the row version, the update affects zero rows and the application must retry or reject the operation. [[2026-03-31--database-transactions|Database Transactions]]

## Contrasts

- **Pessimistic Locking**: Optimistic locking avoids holding a lock while work is in progress, while pessimistic locking blocks conflicting transactions before they can update the row. [[2026-03-31--database-transactions|Database Transactions]]
- **Lost Update**: Lost update is the anomaly; optimistic locking is one way to detect and prevent it. [[2026-03-31--database-transactions|Database Transactions]]

## Evidence

- [[2026-03-31--database-transactions|Database Transactions]] — The source recommends version checks for lost-update scenarios where conflicts are not common.

## Related

- [[lost-update|Lost Update]]
- [[pessimistic-locking|Pessimistic Locking]]
- [[transaction-isolation|Transaction Isolation]]
- [[deadlock|Deadlock]]
- [[version-vector|Version Vector]]

## Open Questions

- Which future source should cover retry budgets, backoff, and user-facing conflict resolution for optimistic updates?
