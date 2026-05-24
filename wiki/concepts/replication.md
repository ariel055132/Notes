---
type: concept
aliases: ["data replication", "database replication", "replicated storage"]
tags: [system-design, databases, distributed-systems]
created: 2026-05-24
updated: 2026-05-24
source_count: 2
---

# Replication

## Definition

Replication is the practice of keeping copies of the same data on multiple networked machines so a system can reduce latency, improve availability, and increase read throughput. [[2026-05-02--replication|Replication]] It contrasts with sharding: replication copies records, while sharding partitions records across database machines or clusters. [[2026-05-15--sharding|Sharding]]

## Scope

This concept covers replica placement, leader and follower roles, multi-leader and leaderless designs, replication logs, lag, failover, quorum behavior, and consistency guarantees exposed to applications. [[2026-05-02--replication|Replication]] It does not by itself guarantee strong consistency, conflict-free writes, or correct failover behavior; those guarantees require explicit design choices such as synchronous replication, consensus, transactions, conflict resolution, or quorum configuration. [[2026-05-02--replication|Replication]] Replication and sharding can be combined, because each shard can itself have replicas, but they solve different distribution problems. [[2026-05-15--sharding|Sharding]]

## Contrasts

- **Read Scaling**: Replication can support read scaling by adding read replicas, while read scaling also includes indexes, query-shape fixes, caching, CDN use, and other read-path changes. [[2026-05-14--scaling-reads|Scaling Reads]] [[2026-05-02--replication|Replication]]
- **Database Sharding**: Replication copies the same data across nodes, while sharding gives different nodes ownership of different subsets of one logical dataset. [[2026-05-14--scaling-reads|Scaling Reads]] [[2026-05-02--replication|Replication]] [[2026-05-15--sharding|Sharding]]
- **Caching**: Replication keeps database-like copies that must track writes, while caching stores derived or repeated answers with explicit freshness tradeoffs. [[2026-05-14--scaling-reads|Scaling Reads]] [[2026-05-02--replication|Replication]]

## Evidence

- [[2026-05-02--replication|Replication]] — The source presents replication as a core distributed-system pattern for latency, availability, and read throughput, then compares single-leader, multi-leader, and leaderless architectures.
- [[2026-05-15--sharding|Sharding]] — The source clarifies the sharding side of the contrast: sharding splits a logical dataset across database machines rather than copying the same records.

## Related

- [[single-leader-replication|Single-Leader Replication]]
- [[multi-leader-replication|Multi-Leader Replication]]
- [[leaderless-replication|Leaderless Replication]]
- [[database-sharding|Database Sharding]]
- [[database-partitioning|Database Partitioning]]
- [[read-replica|Read Replica]]
- [[replication-lag|Replication Lag]]
- [[quorum-reads-and-writes|Quorum Reads and Writes]]

## Open Questions

- Which future sources should define consensus replication and distributed transactions as stricter alternatives to eventually consistent replication?
