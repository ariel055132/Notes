---
type: concept
aliases: ["staleness budget", "acceptable staleness", "freshness window"]
tags: [system-design, caching, distributed-cache, consistency]
created: 2026-05-24
updated: 2026-05-25
source_count: 3
---

# Freshness Budget

## Definition

Freshness budget is the amount of staleness a read path can tolerate before the product behavior becomes incorrect or unacceptable. [[2026-05-14--scaling-reads|Scaling Reads]] In caching design, the freshness budget determines whether to use TTL, invalidation, stale-while-revalidate, write-through updates, cache-replica reads, or source-of-truth checks. [[2026-05-24--caching|Caching]] [[2026-05-15--distributed-cache|Distributed Cache]]

## Scope

This concept guides TTL selection, cache invalidation strategy, read replica tolerance, cache replica tolerance, CDN eligibility, stale-while-revalidate behavior, and whether a read must go to the primary database or another source of truth. [[2026-05-14--scaling-reads|Scaling Reads]] [[2026-05-24--caching|Caching]] [[2026-05-15--distributed-cache|Distributed Cache]] It applies differently to product surfaces: view counts may tolerate minutes, listing details may tolerate seconds or minutes, market snapshots may need very short staleness windows, and payments, ledgers, matching, or inventory usually require source-of-truth correctness. [[2026-05-14--scaling-reads|Scaling Reads]] [[2026-05-24--caching|Caching]] [[2026-05-15--distributed-cache|Distributed Cache]]

## Contrasts

- **TTL**: TTL is a technical cache expiration setting, while freshness budget is the product and correctness constraint used to choose that setting. [[2026-05-14--scaling-reads|Scaling Reads]]
- **Strong consistency**: Strongly consistent reads minimize staleness, while freshness budgets allow explicit bounded staleness where the product can tolerate it. [[2026-05-14--scaling-reads|Scaling Reads]]
- **Cache location**: Cache location decides where data is stored, while freshness budget decides whether that location is safe for the product behavior. [[2026-05-24--caching|Caching]]
- **Cache Replication**: Cache replication can improve availability, but its lag is acceptable only when the freshness budget allows stale cache reads. [[2026-05-15--distributed-cache|Distributed Cache]]

## Evidence

- [[2026-05-14--scaling-reads|Scaling Reads]] — The source says each read scenario should specify how old data may be, and uses that answer to choose TTL, CDN, invalidation, and replica-read behavior.
- [[2026-05-24--caching|Caching]] — The source repeatedly separates cacheable snapshots from correctness-critical paths, such as Airbnb search versus final booking availability.
- [[2026-05-15--distributed-cache|Distributed Cache]] — The source uses course metadata, QR redirect destinations, and payment results to connect stale windows to TTL, invalidation, and source-of-truth reads.

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

## Open Questions

- What default freshness-budget categories should the system-design wiki use when comparing architectures?
