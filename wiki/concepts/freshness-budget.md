---
type: concept
aliases: ["staleness budget", "acceptable staleness", "freshness window"]
tags: [system-design, caching, consistency]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Freshness Budget

## Definition

Freshness budget is the amount of staleness a read path can tolerate before the product behavior becomes incorrect or unacceptable. [[2026-05-14--scaling-reads|Scaling Reads]]

## Scope

This concept guides TTL selection, cache invalidation strategy, read replica tolerance, CDN eligibility, stale-while-revalidate behavior, and whether a read must go to the primary database. [[2026-05-14--scaling-reads|Scaling Reads]] It applies differently to product surfaces: view counts may tolerate minutes, listing descriptions may tolerate seconds or minutes, and payments or inventory usually require near-immediate correctness. [[2026-05-14--scaling-reads|Scaling Reads]]

## Contrasts

- **TTL**: TTL is a technical cache expiration setting, while freshness budget is the product and correctness constraint used to choose that setting. [[2026-05-14--scaling-reads|Scaling Reads]]
- **Strong consistency**: Strongly consistent reads minimize staleness, while freshness budgets allow explicit bounded staleness where the product can tolerate it. [[2026-05-14--scaling-reads|Scaling Reads]]

## Evidence

- [[2026-05-14--scaling-reads|Scaling Reads]] — The source says each read scenario should specify how old data may be, and uses that answer to choose TTL, CDN, invalidation, and replica-read behavior.

## Related

- [[read-scaling|Read Scaling]]
- [[application-level-caching|Application-Level Caching]]
- [[cache-invalidation|Cache Invalidation]]
- [[stale-while-revalidate|Stale-While-Revalidate]]
- [[read-replica|Read Replica]]
- [[cdn-and-edge-caching|CDN and Edge Caching]]

## Open Questions

- What default freshness-budget categories should the system-design wiki use when comparing architectures?
