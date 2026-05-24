---
type: source
source_path: raw/archive/Distributed Cache.pdf
title: "Distributed Cache"
author: "BuildMoat"
date: 2026-05-15
tags: [system-design, distributed-cache, distributed-queue, caching, reliability]
created: 2026-05-25
---

# Distributed Cache

## Summary

This source explains distributed cache as a read-path protection layer that spreads cache capacity, read throughput, availability, and failure isolation across multiple machines. [[2026-05-15--distributed-cache|Distributed Cache]] It warns that a cache cluster is a small distributed system: designers must reason about key ownership, routing, node changes, hot keys, replication, failover, invalidation, stale windows, and database protection during cache failures. [[2026-05-15--distributed-cache|Distributed Cache]] The source recommends starting from cacheability, traffic skew, freshness budget, and failure behavior rather than from tool names such as Redis Cluster or Memcached cluster. [[2026-05-15--distributed-cache|Distributed Cache]] Its practical system-design framing is to treat distributed cache as a rebuildable pressure buffer in front of the database, not as the source of truth for correctness-critical state. [[2026-05-15--distributed-cache|Distributed Cache]]

## Key Claims

1. Distributed cache becomes useful when a single cache node cannot satisfy capacity, throughput, availability, or failure-isolation needs. [[2026-05-15--distributed-cache|Distributed Cache]]
2. A distributed cache should be evaluated through four questions: which data is cacheable, whether key traffic is skewed, how stale the data may be, and what protects the database when cache fails. [[2026-05-15--distributed-cache|Distributed Cache]]
3. Once cache becomes clustered, routing and ownership become central concerns: each key needs a shard map, hash slot, or consistent-hashing rule that identifies its owner. [[2026-05-15--distributed-cache|Distributed Cache]]
4. Naive modulo routing can cause large cache churn during expansion or shrinkage; hash slots or consistent hashing reduce full key remapping, but still require warmup, migration, and database fallback protection. [[2026-05-15--distributed-cache|Distributed Cache]]
5. Even key distribution does not imply even traffic distribution; hot keys can overload a single shard unless mitigated with local cache, key replication, key splitting, CDN, or per-key/per-shard observability. [[2026-05-15--distributed-cache|Distributed Cache]]
6. Cache replication and failover reduce single-node cache failure risk but introduce replica lag, failover turbulence, retries, timeouts, and possible stale reads. [[2026-05-15--distributed-cache|Distributed Cache]]
7. Cache freshness should be driven by a freshness budget, using strategies such as TTL-only, write invalidate, write-through, or event-based invalidation. [[2026-05-15--distributed-cache|Distributed Cache]]
8. Distributed-cache failures are often partial or slow rather than total; defensive design needs TTL jitter, request coalescing, cache warming, short timeouts, retry budgets, circuit breakers, bounded database fallback, stale serving, or degraded responses. [[2026-05-15--distributed-cache|Distributed Cache]]
9. Multi-region cache is usually best kept regional and rebuildable; static public content can go to CDN, while writes can notify regions through queue or CDC invalidation events. [[2026-05-15--distributed-cache|Distributed Cache]]

## Notable Quotes

- "Distributed Cache is not a new source of truth." [[2026-05-15--distributed-cache|Distributed Cache]]
- "Queue is not a garbage can" applies analogously here: cache fallback must be bounded rather than dumping all traffic into the database. [[2026-05-15--distributed-cache|Distributed Cache]]
- "The point of Distributed Cache is not memorizing Redis Cluster, but explaining whether data can be stale, whether traffic is skewed, how nodes fail, and whether the database stays protected." [[2026-05-15--distributed-cache|Distributed Cache]]

## Entities Mentioned

- None. BuildMoat is treated as the source author/publisher in frontmatter rather than as a dedicated entity page. Redis Cluster, Memcached cluster, and CDN edge cache are treated as implementation examples rather than dedicated entity pages in this ingest. [[2026-05-15--distributed-cache|Distributed Cache]]

## Concepts Mentioned

- [[distributed-cache|Distributed Cache]] — A clustered cache layer that spreads cache capacity, throughput, and failure isolation across nodes. [[2026-05-15--distributed-cache|Distributed Cache]]
- [[cache-routing|Cache Routing]] — Routing cache keys to owner shards using shard maps, hash slots, or consistent hashing. [[2026-05-15--distributed-cache|Distributed Cache]]
- [[cache-replication|Cache Replication]] — Replicating cache shards for failover and read availability while accepting possible lag. [[2026-05-15--distributed-cache|Distributed Cache]]
- [[cache-fallback-limit|Cache Fallback Limit]] — Bounding database fallback when cache misses, slows, or fails so the cache outage does not take the database down. [[2026-05-15--distributed-cache|Distributed Cache]]
- [[regional-cache|Regional Cache]] — Keeping per-region cache clusters instead of trying to make cache globally strongly consistent. [[2026-05-15--distributed-cache|Distributed Cache]]
- [[application-level-caching|Application-Level Caching]] — The broader shared backend cache layer that distributed cache extends across nodes. [[2026-05-15--distributed-cache|Distributed Cache]]
- [[consistent-hashing|Consistent Hashing]] — A key routing strategy that limits remapping when cache nodes change. [[2026-05-15--distributed-cache|Distributed Cache]]
- [[fixed-hash-slots|Fixed Hash Slots]] — A slot-based ownership model used by systems such as Redis Cluster. [[2026-05-15--distributed-cache|Distributed Cache]]
- [[hot-key|Hot Key]] — A single highly requested cache key can overload one owner shard. [[2026-05-15--distributed-cache|Distributed Cache]]
- [[cache-invalidation|Cache Invalidation]] — Strategies to remove or refresh stale cached data after writes. [[2026-05-15--distributed-cache|Distributed Cache]]
- [[freshness-budget|Freshness Budget]] — The tolerated stale window that drives TTL, invalidation, and source-of-truth checks. [[2026-05-15--distributed-cache|Distributed Cache]]
- [[cache-stampede|Cache Stampede]] — Many simultaneous misses can overwhelm the origin or database. [[2026-05-15--distributed-cache|Distributed Cache]]
- [[request-coalescing|Request Coalescing]] — A defense that allows only one rebuild or origin fetch for a missing hot key. [[2026-05-15--distributed-cache|Distributed Cache]]
- [[ttl-jitter|TTL Jitter]] — Randomizing TTLs to avoid synchronized expiration. [[2026-05-15--distributed-cache|Distributed Cache]]
- [[cache-warming|Cache Warming]] — Preloading or gradually warming cache after node changes or restarts. [[2026-05-15--distributed-cache|Distributed Cache]]

## Follow-ups

- Create a synthesis comparing distributed cache, application-level cache, CDN/edge cache, local cache, and read replicas as read-path protection layers with different failure and freshness tradeoffs.
