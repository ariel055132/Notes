---
type: concept
aliases: ["atomic conditional update", "compare-and-set update", "state transition update", "claim update"]
tags: [system-design, databases, concurrency, transactions]
created: 2026-05-26
updated: 2026-05-26
source_count: 1
---

# Conditional Update

## Definition

A conditional update is an atomic database update that changes state only if a predicate still holds, allowing one contender to claim work or a resource without a separate distributed lock. [[2026-05-15--distributed-lock|Distributed Lock]]

## Scope

This concept covers state transitions such as `scheduled -> running`, `available -> assigned`, or version-checked updates where the database update affects exactly one row only if the current state is still expected. [[2026-05-15--distributed-lock|Distributed Lock]] It is a preferred alternative when the contested state and correctness boundary live in one database. [[2026-05-15--distributed-lock|Distributed Lock]]

## Contrasts

- **Distributed Lock**: Conditional update lets the database perform the claim and state transition atomically, while distributed lock coordinates ownership outside the database. [[2026-05-15--distributed-lock|Distributed Lock]]
- **Optimistic Locking**: Optimistic locking is a version-based conditional update pattern, while conditional update also covers state-machine predicates such as `status = scheduled`. [[2026-03-31--database-transactions|Database Transactions]] [[2026-05-15--distributed-lock|Distributed Lock]]
- **Pessimistic Locking**: Pessimistic locking blocks other transactions before update, while conditional update allows contenders to race and only one predicate match succeeds. [[2026-03-31--database-transactions|Database Transactions]] [[2026-05-15--distributed-lock|Distributed Lock]]

## Evidence

- [[2026-05-15--distributed-lock|Distributed Lock]] — The source uses task claiming and robotaxi vehicle assignment as examples where conditional update may be simpler than distributed lock.

## Related

- [[distributed-lock|Distributed Lock]]
- [[optimistic-locking|Optimistic Locking]]
- [[pessimistic-locking|Pessimistic Locking]]
- [[unique-constraint|Unique Constraint]]
- [[single-shard-transaction|Single-Shard Transaction]]

## Open Questions

- Which future source should collect SQL patterns for state-machine transitions, atomic counters, and conditional reservation claims?
