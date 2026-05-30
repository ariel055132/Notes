---
type: concept
aliases: ["fencing tokens", "monotonic fencing token", "write fencing token"]
tags: [system-design, distributed-systems, locking, consistency]
created: 2026-05-26
updated: 2026-05-26
source_count: 1
---

# Fencing Token

## Definition

A fencing token is a monotonically increasing token issued with lock or leadership ownership so downstream resources can reject writes from stale owners whose older token is no longer valid. [[2026-05-15--distributed-lock|Distributed Lock]]

## Scope

This concept covers stale-owner protection after lock expiry, GC pauses, network delay, CPU starvation, and failover. [[2026-05-15--distributed-lock|Distributed Lock]] A protected resource stores or compares the latest accepted token or version, so a later owner with token 11 can write and an older owner resuming with token 10 is rejected. [[2026-05-15--distributed-lock|Distributed Lock]]

## Contrasts

- **Lease TTL**: Lease TTL lets another owner eventually acquire the lock, while fencing tokens prevent the expired owner from writing stale state after it wakes up. [[2026-05-15--distributed-lock|Distributed Lock]]
- **Owner Token**: Owner tokens protect lock release from deleting another owner's lock, while fencing tokens protect downstream resources from stale writes. [[2026-05-15--distributed-lock|Distributed Lock]]
- **Optimistic Locking**: Optimistic locking uses resource versions to reject stale updates; fencing tokens provide a distributed-owner version that downstream resources can enforce. [[2026-03-31--database-transactions|Database Transactions]] [[2026-05-15--distributed-lock|Distributed Lock]]

## Evidence

- [[2026-05-15--distributed-lock|Distributed Lock]] — The source presents worker A with token 10 pausing, worker B with token 11 writing, and worker A's later token-10 write being rejected.

## Related

- [[distributed-lock|Distributed Lock]]
- [[lease-based-locking|Lease-Based Locking]]
- [[owner-token|Owner Token]]
- [[optimistic-locking|Optimistic Locking]]
- [[failover|Failover]]
- [[split-brain|Split Brain]]

## Open Questions

- Which future source should distinguish fencing tokens from epochs, terms, zxids, Raft terms, and database row versions?
