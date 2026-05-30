---
type: concept
aliases: ["unique constraints", "uniqueness constraint", "database uniqueness", "dedupe constraint"]
tags: [system-design, databases, concurrency, constraints]
created: 2026-05-26
updated: 2026-05-26
source_count: 1
---

# Unique Constraint

## Definition

A unique constraint is a database-enforced rule that rejects duplicate values for a key or key combination, making it a strong tool for preventing duplicate resource creation under concurrency. [[2026-05-15--distributed-lock|Distributed Lock]]

## Scope

This concept covers correctness cases such as preventing two reservations for the same room and date, deduplicating idempotency records, and rejecting duplicate creation without relying on an external lock. [[2026-05-15--distributed-lock|Distributed Lock]] It is most effective when the invariant can be represented inside one database or shard boundary. [[2026-05-15--distributed-lock|Distributed Lock]]

## Contrasts

- **Distributed Lock**: A unique constraint lets the database reject invalid duplicates at write time, while a distributed lock tries to serialize the decision before the write. [[2026-05-15--distributed-lock|Distributed Lock]]
- **Conditional Update**: Conditional update changes existing state only if a predicate holds, while unique constraint prevents duplicate rows or keys from being created. [[2026-05-15--distributed-lock|Distributed Lock]]
- **Optimistic Locking**: Optimistic locking detects stale updates to an existing row, while unique constraints enforce uniqueness across inserted or updated rows. [[2026-03-31--database-transactions|Database Transactions]] [[2026-05-15--distributed-lock|Distributed Lock]]

## Evidence

- [[2026-05-15--distributed-lock|Distributed Lock]] — The source recommends a unique constraint on `room_id + date` as the clean database-level answer for preventing double booking.

## Related

- [[distributed-lock|Distributed Lock]]
- [[conditional-update|Conditional Update]]
- [[database-transactions|Database Transactions]]
- [[single-shard-transaction|Single-Shard Transaction]]
- [[idempotency-key|Idempotency Key]]

## Open Questions

- Which future source should compare unique constraints, exclusion constraints, and serializable transactions for booking-style invariants?
