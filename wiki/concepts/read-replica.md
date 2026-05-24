---
type: concept
aliases: ["read replicas", "database replica", "leader-follower replication", "primary-replica"]
tags: [system-design, databases, replication]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Read Replica

## Definition

A read replica is a database copy that receives data from a primary database and serves read traffic so the primary does not handle every read. [[2026-05-14--scaling-reads|Scaling Reads]]

## Scope

This concept covers leader-follower replication, routing general reads to replicas, routing freshest reads to primary or caught-up replicas, separating analytics reads, and using replicas to increase read throughput and reduce primary load. [[2026-05-14--scaling-reads|Scaling Reads]]

## Contrasts

- **Database Sharding**: Read replicas copy the whole dataset to more nodes for read throughput, while sharding partitions the dataset across nodes to reduce per-node data and load. [[2026-05-14--scaling-reads|Scaling Reads]]
- **Application-Level Caching**: Replicas still execute database reads, while cache can avoid database execution for repeated answers. [[2026-05-14--scaling-reads|Scaling Reads]]

## Evidence

- [[2026-05-14--scaling-reads|Scaling Reads]] — The source explains that replicas increase read throughput but introduce replication lag and read-after-write inconsistency concerns.

## Related

- [[read-scaling|Read Scaling]]
- [[freshness-budget|Freshness Budget]]
- [[database-sharding|Database Sharding]]
- [[database-indexing|Database Indexing]]
- [[application-level-caching|Application-Level Caching]]

## Open Questions

- Which patterns should be added for lag-aware routing and read-your-writes guarantees?
