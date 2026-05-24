---
type: concept
aliases: ["replica lag", "follower lag", "replication delay"]
tags: [system-design, databases, replication, consistency]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Replication Lag

## Definition

Replication lag is the delay between a leader accepting a write and a follower applying that write, during which follower reads may return stale data. [[2026-05-02--replication|Replication]]

## Scope

This concept covers eventual consistency in asynchronously replicated systems, lag-aware routing, reading from primary after recent writes, rejecting overly stale replicas, and using log positions rather than wall-clock time to decide whether a replica is caught up. [[2026-05-02--replication|Replication]] It is a central risk in read-replica designs because read capacity improves only if applications can tolerate or manage stale reads. [[2026-05-14--scaling-reads|Scaling Reads]] [[2026-05-02--replication|Replication]]

## Contrasts

- **Freshness Budget**: A freshness budget defines how stale a read may be for a product behavior, while replication lag is one mechanism that can make reads stale. [[2026-05-14--scaling-reads|Scaling Reads]] [[2026-05-02--replication|Replication]]
- **Cache Staleness**: Cache staleness depends on invalidation and TTL policy, while replication lag depends on write propagation and follower catch-up. [[2026-05-14--scaling-reads|Scaling Reads]] [[2026-05-02--replication|Replication]]

## Evidence

- [[2026-05-02--replication|Replication]] — The source names read-after-write inconsistency, monotonic-read inconsistency, and consistent-prefix inconsistency as common lag consequences.
- [[2026-05-14--scaling-reads|Scaling Reads]] — The source notes that read replicas improve read throughput but require explicit handling for lag and read-after-write behavior.

## Related

- [[read-replica|Read Replica]]
- [[read-after-write-consistency|Read-After-Write Consistency]]
- [[monotonic-reads|Monotonic Reads]]
- [[consistent-prefix-reads|Consistent Prefix Reads]]
- [[asynchronous-replication|Asynchronous Replication]]
- [[freshness-budget|Freshness Budget]]

## Open Questions

- Which future source should add operational metrics and alerts for replica lag thresholds?
