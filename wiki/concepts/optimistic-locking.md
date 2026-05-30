---
type: concept
aliases: ["optimistic concurrency control", "version check", "compare-and-set update"]
tags: [system-design, databases, transactions, concurrency, locking]
created: 2026-05-24
updated: 2026-05-26
source_count: 2
---

# Optimistic Locking

## Definition

Optimistic locking is a concurrency-control technique that allows concurrent work to proceed and detects conflicts at update or commit time, commonly by checking a version column. [[2026-03-31--database-transactions|Database Transactions]] In distributed-lock designs, version checks can serve the same stale-write rejection role as fencing tokens when an old lease owner resumes after expiry. [[2026-05-15--distributed-lock|Distributed Lock]]

## Scope

This concept covers conflict detection for cases where conflicts are expected to be uncommon. [[2026-03-31--database-transactions|Database Transactions]] The transaction source presents an update with `WHERE id = 1 AND version = 1` as the key idea: if another transaction already changed the row version, the update affects zero rows and the application must retry or reject the operation. [[2026-03-31--database-transactions|Database Transactions]] The distributed-lock source extends the same idea to lease-protected writes: important writes need a fencing token or version check because TTL alone does not stop stale owners. [[2026-05-15--distributed-lock|Distributed Lock]]

## Contrasts

- **Pessimistic Locking**: Optimistic locking avoids holding a lock while work is in progress, while pessimistic locking blocks conflicting transactions before they can update the row. [[2026-03-31--database-transactions|Database Transactions]]
- **Lost Update**: Lost update is the anomaly; optimistic locking is one way to detect and prevent it. [[2026-03-31--database-transactions|Database Transactions]]
- **Fencing Token**: Optimistic locking usually checks a resource version in the database, while a fencing token is issued by a lock or coordination service and then checked by the downstream resource. [[2026-05-15--distributed-lock|Distributed Lock]]

## Evidence

- [[2026-03-31--database-transactions|Database Transactions]] — The source recommends version checks for lost-update scenarios where conflicts are not common.
- [[2026-05-15--distributed-lock|Distributed Lock]] — The source recommends version checks or fencing tokens so expired lock owners cannot overwrite newer state after resuming.

## Related

- [[lost-update|Lost Update]]
- [[pessimistic-locking|Pessimistic Locking]]
- [[transaction-isolation|Transaction Isolation]]
- [[deadlock|Deadlock]]
- [[version-vector|Version Vector]]
- [[fencing-token|Fencing Token]]
- [[conditional-update|Conditional Update]]
- [[distributed-lock|Distributed Lock]]

## Open Questions

- Which future source should cover retry budgets, backoff, and user-facing conflict resolution for optimistic updates?
