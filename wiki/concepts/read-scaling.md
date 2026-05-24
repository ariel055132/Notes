---
type: concept
aliases: ["Scaling Reads", "read path scaling", "read-heavy system scaling"]
tags: [system-design, databases, caching, replication]
created: 2026-05-24
updated: 2026-05-24
source_count: 4
---

# Read Scaling

## Definition

Read scaling is the practice of changing how a system serves repeated high-volume reads so the primary database does less repeated work while users still receive data with acceptable latency and freshness. [[2026-05-14--scaling-reads|Scaling Reads]] Indexing is often the first database-layer read-scaling move because it can make specific high-frequency queries avoid full table scans before adding new infrastructure. [[2026-05-15--database-indexing|Database Indexing]] Replication supports read scaling when followers serve read traffic, but that benefit depends on handling replication lag and freshness requirements explicitly. [[2026-05-02--replication|Replication]] Caching supports read scaling by serving frequently read or expensive data from a faster or closer layer while respecting staleness and failure-mode constraints. [[2026-05-24--caching|Caching]]

## Scope

This concept covers read-heavy endpoints, repeated reads of shared data, database query tuning, indexes, replicas, sharding, application cache, CDN/edge cache, client and in-process cache, freshness, invalidation, hot keys, stampedes, penetration, avalanche, replication lag, and read-path observability. [[2026-05-14--scaling-reads|Scaling Reads]] [[2026-05-02--replication|Replication]] [[2026-05-24--caching|Caching]] [[2026-05-15--database-indexing|Database Indexing]] It does not cover write-heavy scaling as the primary bottleneck, such as high-frequency location updates or collaborative editing conflict resolution. [[2026-05-14--scaling-reads|Scaling Reads]]

## Contrasts

- **Write scaling**: Read scaling handles repeated retrieval pressure, while write scaling handles sustained mutation throughput and durability. [[2026-05-14--scaling-reads|Scaling Reads]]
- **Generic performance optimization**: Read scaling is not just faster code; it changes where reads are served from and how much database work is repeated. [[2026-05-14--scaling-reads|Scaling Reads]]
- **Replication**: Replication is the mechanism of keeping multiple data copies, while read scaling is one reason to use those copies and one design lens for routing reads. [[2026-05-02--replication|Replication]] [[2026-05-14--scaling-reads|Scaling Reads]]

## Evidence

- [[2026-05-14--scaling-reads|Scaling Reads]] — The source defines the core problem as repeated reads of the same data overwhelming database CPU, memory, I/O, or network capacity.
- [[2026-05-15--database-indexing|Database Indexing]] — The source explains indexing as a targeted read-path improvement with storage and write-cost tradeoffs.
- [[2026-05-02--replication|Replication]] — The source explains that replication can scale reads through followers but makes lag-aware consistency guarantees part of the design.
- [[2026-05-24--caching|Caching]] — The source treats caching as a targeted read-path optimization for lowering latency, reducing database load, and absorbing hot reads.

## Related

- [[freshness-budget|Freshness Budget]]
- [[database-indexing|Database Indexing]]
- [[query-shape-optimization|Query Shape Optimization]]
- [[read-replica|Read Replica]]
- [[replication|Replication]]
- [[replication-lag|Replication Lag]]
- [[read-after-write-consistency|Read-After-Write Consistency]]
- [[application-level-caching|Application-Level Caching]]
- [[cdn-and-edge-caching|CDN and Edge Caching]]
- [[cache-aside|Cache-Aside]]
- [[in-process-cache|In-Process Cache]]
- [[hot-key|Hot Key]]
- [[cache-stampede|Cache Stampede]]

## Open Questions

- Which future wiki pages should define the companion patterns for write scaling and consistency?
