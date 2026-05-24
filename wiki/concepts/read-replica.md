---
type: concept
aliases: ["read replicas", "database replica", "leader-follower replication", "primary-replica"]
tags: [system-design, databases, replication]
created: 2026-05-24
updated: 2026-05-24
source_count: 2
---

# Read Replica

## Definition

A read replica is a database copy that receives data from a primary database and serves read traffic so the primary does not handle every read. [[2026-05-14--scaling-reads|Scaling Reads]] In single-leader replication, a read replica is a follower that applies the leader's replication log while reads may be served by either the leader or caught-up followers. [[2026-05-02--replication|Replication]]

## Scope

This concept covers leader-follower replication, routing general reads to replicas, routing freshest reads to primary or caught-up replicas, separating analytics reads, follower catch-up, and using replicas to increase read throughput and reduce primary load. [[2026-05-14--scaling-reads|Scaling Reads]] [[2026-05-02--replication|Replication]]

## Contrasts

- **Database Sharding**: Read replicas copy the whole dataset to more nodes for read throughput, while sharding partitions the dataset across nodes to reduce per-node data and load. [[2026-05-14--scaling-reads|Scaling Reads]]
- **Application-Level Caching**: Replicas still execute database reads, while cache can avoid database execution for repeated answers. [[2026-05-14--scaling-reads|Scaling Reads]]
- **Leaderless Replication**: Read replicas in a single-leader design follow one primary, while leaderless replication lets clients read and write multiple replicas directly. [[2026-05-02--replication|Replication]]

## Evidence

- [[2026-05-14--scaling-reads|Scaling Reads]] — The source explains that replicas increase read throughput but introduce replication lag and read-after-write inconsistency concerns.
- [[2026-05-02--replication|Replication]] — The source places read replicas inside single-leader replication and explains how followers apply leader log changes, recover after failure, and may serve stale reads during lag.

## Related

- [[read-scaling|Read Scaling]]
- [[replication|Replication]]
- [[single-leader-replication|Single-Leader Replication]]
- [[replication-lag|Replication Lag]]
- [[read-after-write-consistency|Read-After-Write Consistency]]
- [[freshness-budget|Freshness Budget]]
- [[database-sharding|Database Sharding]]
- [[database-indexing|Database Indexing]]
- [[application-level-caching|Application-Level Caching]]

## Open Questions

- Which production metrics should define whether a follower is caught up enough for a specific read?
