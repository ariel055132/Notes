---
type: concept
aliases: ["database deadlock", "deadlocks", "lock deadlock"]
tags: [system-design, databases, transactions, concurrency, locking]
created: 2026-05-24
updated: 2026-05-26
source_count: 2
---

# Deadlock

## Definition

A deadlock occurs when transactions hold locks and wait for one another in a cycle, so none of them can continue until one transaction is rolled back or aborted. [[2026-03-31--database-transactions|Database Transactions]] Distributed-lock designs reduce some local blocking by using leases and timeouts, but broad or long-held locks can still create throughput collapse, timeout loops, and recovery problems. [[2026-05-15--distributed-lock|Distributed Lock]]

## Scope

This concept covers a system-design risk introduced by pessimistic locking and multi-row updates. [[2026-03-31--database-transactions|Database Transactions]] It also covers the broader lock-design warning that large critical sections, long lock TTLs, and inconsistent ownership can make systems slow or unavailable even when a literal database deadlock is not present. [[2026-05-15--distributed-lock|Distributed Lock]] The transaction source recommends acquiring locks in a consistent order, relying on database deadlock detection to abort one participant, and making the application handle retries when a transaction is rolled back. [[2026-03-31--database-transactions|Database Transactions]]

## Contrasts

- **Lost Update**: Lost update happens when conflicting writes overwrite each other; deadlock happens when transactions block each other while trying to prevent conflicts. [[2026-03-31--database-transactions|Database Transactions]]
- **Optimistic Locking**: Optimistic locking can avoid long-held locks, while pessimistic locking can create deadlock risk. [[2026-03-31--database-transactions|Database Transactions]]
- **Distributed Lock**: Distributed lock uses TTL and timeout to avoid permanent ownership, but it still needs small critical sections so contention does not dominate the workflow. [[2026-05-15--distributed-lock|Distributed Lock]]

## Evidence

- [[2026-03-31--database-transactions|Database Transactions]] — The source explains that transactions locking resources in different orders can deadlock and that databases usually roll back one transaction.
- [[2026-05-15--distributed-lock|Distributed Lock]] — The source warns that locks held too broadly reduce throughput and increase latency, and recommends protecting only the short section that truly needs mutual exclusion.

## Related

- [[pessimistic-locking|Pessimistic Locking]]
- [[lost-update|Lost Update]]
- [[transaction-isolation|Transaction Isolation]]
- [[database-transactions|Database Transactions]]
- [[distributed-lock|Distributed Lock]]
- [[lease-based-locking|Lease-Based Locking]]

## Open Questions

- Which future source should cover deadlock detection algorithms and lock wait timeout tuning?
