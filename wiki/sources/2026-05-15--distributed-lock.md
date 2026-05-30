---
type: source
source_path: raw/archive/Distributed Lock.pdf
title: "Distributed Lock"
author: "BuildMoat"
date: 2026-05-15
tags: [system-design, distributed-systems, locking, concurrency, reliability]
created: 2026-05-26
---

# Distributed Lock

## Summary

This source frames distributed lock as a short lease-based coordination tool for cases where multiple machines may try to modify the same shared resource. [[2026-05-15--distributed-lock|Distributed Lock]] It argues that a mature system-design answer should first try simpler correctness boundaries such as database transactions, unique constraints, conditional updates, queues, or single-writer ownership before reaching for a distributed lock. [[2026-05-15--distributed-lock|Distributed Lock]] When a distributed lock is necessary, the source emphasizes lease TTL, owner-token release safety, fencing tokens or version checks, idempotency, and keeping the critical section small. [[2026-05-15--distributed-lock|Distributed Lock]] It treats the lock as one piece of a broader correctness design, not as a complete guarantee against stale writes, long workflow failure, retries, or network partitions. [[2026-05-15--distributed-lock|Distributed Lock]]

## Key Claims

1. Distributed lock is for limiting ownership of a short critical section across machines, not for making distributed execution behave like a single process. [[2026-05-15--distributed-lock|Distributed Lock]]
2. Before using distributed lock, designers should ask whether the conflict can be handled inside one database transaction, unique constraint, conditional update, queue, or single-writer pattern. [[2026-05-15--distributed-lock|Distributed Lock]]
3. Distributed locks should be modeled as leases with TTL rather than permanent locks, because owners can crash or become unreachable. [[2026-05-15--distributed-lock|Distributed Lock]]
4. TTL prevents permanent lock ownership but does not prevent stale writes when an old owner resumes after GC pause, network delay, CPU starvation, or lock expiry. [[2026-05-15--distributed-lock|Distributed Lock]]
5. Fencing tokens or version checks are required when downstream resources must reject writes from stale owners. [[2026-05-15--distributed-lock|Distributed Lock]]
6. Redis `SET key owner_id NX PX ttl` can implement a short low-latency lease, but release must verify that the lock value still belongs to the releasing owner. [[2026-05-15--distributed-lock|Distributed Lock]]
7. ZooKeeper or etcd are more appropriate for stronger coordination, leader election, and membership, but have higher operational cost. [[2026-05-15--distributed-lock|Distributed Lock]]
8. Long workflows such as payment should not be wrapped in a distributed lock; use pending state, expiration, idempotency, and compensation instead. [[2026-05-15--distributed-lock|Distributed Lock]]
9. Distributed-lock observability should track acquisition latency, contention rate, timeout rate, and stale-write rejection. [[2026-05-15--distributed-lock|Distributed Lock]]

## Notable Quotes

- "是 lease，不是永遠持有的鎖." [[2026-05-15--distributed-lock|Distributed Lock]]
- "TTL 是為了避免 owner 掛掉後資源永遠鎖住；token 是為了避免過期 owner 回來後寫出舊狀態." [[2026-05-15--distributed-lock|Distributed Lock]]
- "Distributed lock 的重點不是把 race condition 藏起來，而是把競爭邊界縮到最小." [[2026-05-15--distributed-lock|Distributed Lock]]

## Entities Mentioned

- None. BuildMoat is treated as the source author/publisher in frontmatter. Redis, ZooKeeper, and etcd are treated as implementation examples rather than dedicated entity pages in this ingest. [[2026-05-15--distributed-lock|Distributed Lock]]

## Concepts Mentioned

- [[distributed-lock|Distributed Lock]] — A cross-machine mutual-exclusion mechanism for short critical sections. [[2026-05-15--distributed-lock|Distributed Lock]]
- [[lease-based-locking|Lease-Based Locking]] — Modeling lock ownership as an expiring lease rather than a permanent claim. [[2026-05-15--distributed-lock|Distributed Lock]]
- [[fencing-token|Fencing Token]] — A monotonic token that lets downstream resources reject stale owners. [[2026-05-15--distributed-lock|Distributed Lock]]
- [[owner-token|Owner Token]] — A unique owner value stored with a lock so clients release only locks they still own. [[2026-05-15--distributed-lock|Distributed Lock]]
- [[conditional-update|Conditional Update]] — Claiming work or resources with an atomic predicate update instead of an external lock. [[2026-05-15--distributed-lock|Distributed Lock]]
- [[unique-constraint|Unique Constraint]] — Letting the database reject duplicate resource creation such as double booking. [[2026-05-15--distributed-lock|Distributed Lock]]
- [[single-writer-pattern|Single-Writer Pattern]] — Serializing all writes for a resource through one owner or queue partition. [[2026-05-15--distributed-lock|Distributed Lock]]
- [[idempotency-key|Idempotency Key]] — A stable request or operation key that makes retries safe for external side effects. [[2026-05-15--distributed-lock|Distributed Lock]]
- [[optimistic-locking|Optimistic Locking]] — Version checks that can reject stale writes after a lease expires. [[2026-05-15--distributed-lock|Distributed Lock]]
- [[pessimistic-locking|Pessimistic Locking]] — Local database row locking as an alternative when state lives inside one database transaction. [[2026-05-15--distributed-lock|Distributed Lock]]
- [[deadlock|Deadlock]] — A risk when locks are too broad, held too long, or acquired inconsistently. [[2026-05-15--distributed-lock|Distributed Lock]]
- [[request-coalescing|Request Coalescing]] — A related one-worker pattern for cache rebuilds where distributed locks may be one implementation. [[2026-05-15--distributed-lock|Distributed Lock]]
- [[split-brain|Split Brain]] — A related stale-owner or dual-owner risk in leadership and failover. [[2026-05-15--distributed-lock|Distributed Lock]]
- [[failover|Failover]] — A setting where leases and fencing can prevent old leaders from writing after promotion. [[2026-05-15--distributed-lock|Distributed Lock]]

## Follow-ups

- Create a synthesis comparing database transactions, row locks, conditional updates, unique constraints, distributed locks, fencing tokens, queues, and single writers as competing concurrency-control tools.
