---
type: concept
aliases: ["regional cache", "per-region cache", "multi-region cache", "region-local cache"]
tags: [system-design, distributed-cache, distributed-queue, caching, multi-region]
created: 2026-05-25
updated: 2026-05-25
source_count: 1
---

# Regional Cache

## Definition

Regional cache is a multi-region cache strategy where each deployment region maintains its own cache cluster close to regional application traffic. [[2026-05-15--distributed-cache|Distributed Cache]]

## Scope

This concept covers using region-local application caches rather than trying to make cache globally strongly consistent. [[2026-05-15--distributed-cache|Distributed Cache]] The source recommends CDN for static public content, per-region cache clusters for application reads, queue or CDC invalidation events across regions, and accepting short cold-cache periods during region failover while protecting the database with limits. [[2026-05-15--distributed-cache|Distributed Cache]]

## Contrasts

- **Global Strong Consistency**: Regional cache accepts cache rebuild and bounded staleness, while strong cross-region consistency belongs in the database or coordination layer when required. [[2026-05-15--distributed-cache|Distributed Cache]]
- **CDN and Edge Caching**: CDN handles static or public content at the edge, while regional cache is a backend application cache per region. [[2026-05-24--caching|Caching]] [[2026-05-15--distributed-cache|Distributed Cache]]

## Evidence

- [[2026-05-15--distributed-cache|Distributed Cache]] — The source says cache usually can be rebuilt, making cross-region cache synchronization less worthwhile than regional caches plus invalidation events.

## Related

- [[distributed-cache|Distributed Cache]]
- [[cdn-and-edge-caching|CDN and Edge Caching]]
- [[cache-invalidation|Cache Invalidation]]
- [[cache-fallback-limit|Cache Fallback Limit]]
- [[freshness-budget|Freshness Budget]]

## Open Questions

- Which future source should cover cache invalidation fanout and regional failover runbooks?
