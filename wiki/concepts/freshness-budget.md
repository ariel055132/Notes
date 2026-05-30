---
type: concept
aliases: ["staleness budget", "acceptable staleness", "freshness window"]
tags: [system-design, caching, distributed-cache, cdn, consistency]
created: 2026-05-24
updated: 2026-05-26
source_count: 4
---

# Freshness Budget

## Definition

Freshness budget is the amount of staleness a read path can tolerate before the product behavior becomes incorrect or unacceptable. [[2026-05-14--scaling-reads|Scaling Reads]] In caching design, the freshness budget determines whether to use TTL, invalidation, stale-while-revalidate, write-through updates, cache-replica reads, CDN edge caching, or source-of-truth checks. [[2026-05-24--caching|Caching]] [[2026-05-15--distributed-cache|Distributed Cache]] [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]

## Scope

This concept guides TTL selection, cache invalidation strategy, read replica tolerance, cache replica tolerance, CDN eligibility, stale-while-revalidate behavior, and whether a read must go to the primary database or another source of truth. [[2026-05-14--scaling-reads|Scaling Reads]] [[2026-05-24--caching|Caching]] [[2026-05-15--distributed-cache|Distributed Cache]] [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]] It applies differently to product surfaces: static assets may tolerate long TTLs with versioned URLs, public rankings may tolerate short stale windows, listing details may tolerate seconds or minutes, market snapshots may need very short staleness windows, and payments, ledgers, matching, or inventory usually require source-of-truth correctness. [[2026-05-14--scaling-reads|Scaling Reads]] [[2026-05-24--caching|Caching]] [[2026-05-15--distributed-cache|Distributed Cache]] [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]

## Contrasts

- **TTL**: TTL is a technical cache expiration setting, while freshness budget is the product and correctness constraint used to choose that setting. [[2026-05-14--scaling-reads|Scaling Reads]]
- **Strong consistency**: Strongly consistent reads minimize staleness, while freshness budgets allow explicit bounded staleness where the product can tolerate it. [[2026-05-14--scaling-reads|Scaling Reads]]
- **Cache location**: Cache location decides where data is stored, while freshness budget decides whether that location is safe for the product behavior. [[2026-05-24--caching|Caching]]
- **Cache Replication**: Cache replication can improve availability, but its lag is acceptable only when the freshness budget allows stale cache reads. [[2026-05-15--distributed-cache|Distributed Cache]]
- **CDN Cache-Key Design**: CDN cache-key design decides whether two edge requests can share a cached response, while freshness budget decides how long that response may remain valid. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]

## Evidence

- [[2026-05-14--scaling-reads|Scaling Reads]] — The source says each read scenario should specify how old data may be, and uses that answer to choose TTL, CDN, invalidation, and replica-read behavior.
- [[2026-05-24--caching|Caching]] — The source repeatedly separates cacheable snapshots from correctness-critical paths, such as Airbnb search versus final booking availability.
- [[2026-05-15--distributed-cache|Distributed Cache]] — The source uses course metadata, QR redirect destinations, and payment results to connect stale windows to TTL, invalidation, and source-of-truth reads.
- [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]] — The source says CDN is strongest for shareable, repeated content that can accept short-lived staleness, while personalized or real-time checks should be handled conservatively.

## Related

- [[read-scaling|Read Scaling]]
- [[application-level-caching|Application-Level Caching]]
- [[cache-invalidation|Cache Invalidation]]
- [[stale-while-revalidate|Stale-While-Revalidate]]
- [[write-through-cache|Write-Through Cache]]
- [[read-replica|Read Replica]]
- [[cdn-and-edge-caching|CDN and Edge Caching]]
- [[cache-replication|Cache Replication]]
- [[distributed-cache|Distributed Cache]]
- [[cdn-cache-key-design|CDN Cache-Key Design]]
- [[signed-cdn-access|Signed CDN Access]]

## Open Questions

- What default freshness-budget categories should the system-design wiki use when comparing architectures?
