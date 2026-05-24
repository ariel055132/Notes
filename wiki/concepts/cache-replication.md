---
type: concept
aliases: ["cache replica", "cache replicas", "cache failover", "replicated cache"]
tags: [system-design, distributed-cache, distributed-queue, caching, reliability]
created: 2026-05-25
updated: 2026-05-25
source_count: 1
---

# Cache Replication

## Definition

Cache replication keeps one or more copies of a cache shard so reads or failover can continue when the primary cache node is unavailable. [[2026-05-15--distributed-cache|Distributed Cache]]

## Scope

This concept covers primary-replica cache layouts, failover to cache replicas, and the tradeoff between cache availability and stale reads. [[2026-05-15--distributed-cache|Distributed Cache]] The source notes that replica lag is often acceptable for cache because cached data is usually rebuildable and eventually consistent, but it is unsafe when stale data would drive correctness-critical decisions such as balances, inventory, or payment state. [[2026-05-15--distributed-cache|Distributed Cache]]

## Contrasts

- **Database Replication**: Database replication protects source-of-truth state, while cache replication protects a rebuildable acceleration layer. [[2026-05-02--replication|Replication]] [[2026-05-15--distributed-cache|Distributed Cache]]
- **Replication Lag**: Cache replication can lag just like database replication, but the product impact depends on the cache freshness budget and whether stale data is only advisory. [[2026-05-02--replication|Replication]] [[2026-05-15--distributed-cache|Distributed Cache]]

## Evidence

- [[2026-05-15--distributed-cache|Distributed Cache]] — The source describes cache shard primaries and replicas, then warns about replica lag and failover turbulence.

## Related

- [[distributed-cache|Distributed Cache]]
- [[replication|Replication]]
- [[replication-lag|Replication Lag]]
- [[freshness-budget|Freshness Budget]]
- [[cache-fallback-limit|Cache Fallback Limit]]

## Open Questions

- Which future source should compare cache replica reads with database read replicas under failure?
