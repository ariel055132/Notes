---
type: concept
aliases: ["distributed cache", "cache cluster", "distributed caching", "clustered cache"]
tags: [system-design, distributed-cache, distributed-queue, caching, reliability]
created: 2026-05-25
updated: 2026-05-25
source_count: 1
---

# Distributed Cache

## Definition

Distributed cache is a shared cache layer spread across multiple machines so cache capacity, read throughput, availability, and failure isolation can scale beyond a single cache node. [[2026-05-15--distributed-cache|Distributed Cache]]

## Scope

This concept covers cache clusters such as Redis Cluster, Memcached clusters, internal cache shards, and similar multi-node read-path protection layers. [[2026-05-15--distributed-cache|Distributed Cache]] It adds distributed-system concerns to ordinary caching: key routing, ownership, rebalancing, hot keys, cache replication, failover, stale reads, invalidation, cache warmup, and bounded database fallback. [[2026-05-15--distributed-cache|Distributed Cache]]

## Contrasts

- **In-Process Cache**: In-process cache is per application instance and avoids a network hop, while distributed cache is shared and scales across cache nodes. [[2026-05-24--caching|Caching]] [[2026-05-15--distributed-cache|Distributed Cache]]
- **Application-Level Caching**: Application-level caching describes the cache layer between app and database; distributed cache is the multi-node version with routing, ownership, and failover concerns. [[2026-05-24--caching|Caching]] [[2026-05-15--distributed-cache|Distributed Cache]]
- **Source of Truth**: Distributed cache protects the database from repeated reads, but correctness-critical decisions should still use the source of truth. [[2026-05-15--distributed-cache|Distributed Cache]]

## Evidence

- [[2026-05-15--distributed-cache|Distributed Cache]] — The source frames distributed cache as a database pressure buffer and warns against treating it as the authoritative data source.

## Related

- [[application-level-caching|Application-Level Caching]]
- [[cache-routing|Cache Routing]]
- [[cache-replication|Cache Replication]]
- [[cache-fallback-limit|Cache Fallback Limit]]
- [[hot-key|Hot Key]]
- [[cache-invalidation|Cache Invalidation]]
- [[freshness-budget|Freshness Budget]]

## Open Questions

- Which future source should compare Redis Cluster and Memcached cluster operational models in detail?
