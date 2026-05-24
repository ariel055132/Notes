---
type: concept
aliases: ["Scaling Reads", "read path scaling", "read-heavy system scaling"]
tags: [system-design, databases, caching]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Read Scaling

## Definition

Read scaling is the practice of changing how a system serves repeated high-volume reads so the primary database does less repeated work while users still receive data with acceptable latency and freshness. [[2026-05-14--scaling-reads|Scaling Reads]]

## Scope

This concept covers read-heavy endpoints, repeated reads of shared data, database query tuning, replicas, sharding, application cache, CDN/edge cache, freshness, invalidation, hot keys, stampedes, and read-path observability. [[2026-05-14--scaling-reads|Scaling Reads]] It does not cover write-heavy scaling as the primary bottleneck, such as high-frequency location updates or collaborative editing conflict resolution. [[2026-05-14--scaling-reads|Scaling Reads]]

## Contrasts

- **Write scaling**: Read scaling handles repeated retrieval pressure, while write scaling handles sustained mutation throughput and durability. [[2026-05-14--scaling-reads|Scaling Reads]]
- **Generic performance optimization**: Read scaling is not just faster code; it changes where reads are served from and how much database work is repeated. [[2026-05-14--scaling-reads|Scaling Reads]]

## Evidence

- [[2026-05-14--scaling-reads|Scaling Reads]] — The source defines the core problem as repeated reads of the same data overwhelming database CPU, memory, I/O, or network capacity.

## Related

- [[freshness-budget|Freshness Budget]]
- [[database-indexing|Database Indexing]]
- [[read-replica|Read Replica]]
- [[application-level-caching|Application-Level Caching]]
- [[cdn-and-edge-caching|CDN and Edge Caching]]
- [[hot-key|Hot Key]]
- [[cache-stampede|Cache Stampede]]

## Open Questions

- Which future wiki pages should define the companion patterns for write scaling and consistency?
