---
type: concept
aliases: ["distributed locks", "cross-machine lock", "distributed mutex"]
tags: [system-design, distributed-systems, locking, concurrency, coordination]
created: 2026-05-26
updated: 2026-05-26
source_count: 2
---

# Distributed Lock

## Definition

Distributed lock is a coordination mechanism that lets multiple machines contend for ownership of a shared resource while allowing only one owner to run a short critical section at a time. [[2026-05-15--distributed-lock|Distributed Lock]] ZooKeeper can implement low-frequency, correctness-critical distributed locks with sequential ephemeral znodes, where the smallest sequence owns the lock and others watch their predecessor. [[2026-05-15--zookeeper|Zookeeper]]

## Scope

This concept covers cross-service or cross-worker coordination when the shared resource cannot be protected cleanly by one local database transaction, unique constraint, conditional update, queue partition, or single writer. [[2026-05-15--distributed-lock|Distributed Lock]] It should be used as a short lease, not as a wrapper around long external workflows such as payment, and it needs owner tokens, fencing tokens or version checks, timeouts, idempotency, and observability to be safe. [[2026-05-15--distributed-lock|Distributed Lock]] ZooKeeper-style locks are better suited to low-frequency metadata coordination such as schema migration, partition reassignment, or infrastructure control-plane work than per-request product paths. [[2026-05-15--zookeeper|Zookeeper]]

## Contrasts

- **Pessimistic Locking**: Pessimistic locking protects rows inside one database consistency boundary, while distributed lock coordinates across processes or services outside one database transaction. [[2026-03-31--database-transactions|Database Transactions]] [[2026-05-15--distributed-lock|Distributed Lock]]
- **Optimistic Locking**: Optimistic locking detects stale writes with version checks, while distributed lock tries to reduce concurrent ownership before the write happens. [[2026-03-31--database-transactions|Database Transactions]] [[2026-05-15--distributed-lock|Distributed Lock]]
- **Single-Writer Pattern**: A distributed lock grants temporary ownership to one contender, while a single-writer pattern routes all work for a resource to one serialized owner. [[2026-05-15--distributed-lock|Distributed Lock]]
- **ZooKeeper Leader Election**: ZooKeeper sequential ephemeral nodes can implement locks and leader election, but the higher-level design still needs to keep the protected work small and off hot paths. [[2026-05-15--zookeeper|Zookeeper]]

## Evidence

- [[2026-05-15--distributed-lock|Distributed Lock]] — The source says distributed lock should be considered only after data-model, transaction, queue, or single-writer solutions are ruled out.
- [[2026-05-15--zookeeper|Zookeeper]] — The source describes fair distributed locks built with sequential ephemeral znodes and predecessor watches, while warning against high-frequency ZooKeeper locks.

## Related

- [[lease-based-locking|Lease-Based Locking]]
- [[fencing-token|Fencing Token]]
- [[owner-token|Owner Token]]
- [[conditional-update|Conditional Update]]
- [[unique-constraint|Unique Constraint]]
- [[single-writer-pattern|Single-Writer Pattern]]
- [[optimistic-locking|Optimistic Locking]]
- [[pessimistic-locking|Pessimistic Locking]]
- [[split-brain|Split Brain]]
- [[zookeeper|ZooKeeper]]
- [[sequential-znode|Sequential ZNode]]
- [[ephemeral-znode|Ephemeral ZNode]]
- [[zookeeper-watch|ZooKeeper Watch]]

## Open Questions

- Which future source should compare Redis locks, Redlock, ZooKeeper, etcd, and database advisory locks under partitions and clock drift?
