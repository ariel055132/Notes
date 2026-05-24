---
type: concept
aliases: ["SWR", "stale while revalidate", "background cache refresh"]
tags: [system-design, caching, latency]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Stale-While-Revalidate

## Definition

Stale-while-revalidate is a caching pattern where a read path returns stale cached data within a permitted window while refreshing the cache asynchronously in the background. [[2026-05-14--scaling-reads|Scaling Reads]]

## Scope

This concept covers soft TTL, hard TTL, asynchronous refresh, lower tail latency, reduced backend spikes, and use cases such as home pages, listing pages, and recommendation modules. [[2026-05-14--scaling-reads|Scaling Reads]]

## Contrasts

- **Hard expiration**: Hard expiration blocks or misses once TTL expires, while stale-while-revalidate can return old data while refresh proceeds. [[2026-05-14--scaling-reads|Scaling Reads]]
- **Distributed lock**: A distributed lock limits who rebuilds a cache entry, while stale-while-revalidate avoids making users wait for rebuild when stale data is acceptable. [[2026-05-14--scaling-reads|Scaling Reads]]

## Evidence

- [[2026-05-14--scaling-reads|Scaling Reads]] — The source recommends returning stale data after soft TTL but before hard TTL, then refreshing cache asynchronously.

## Related

- [[read-scaling|Read Scaling]]
- [[freshness-budget|Freshness Budget]]
- [[application-level-caching|Application-Level Caching]]
- [[cache-invalidation|Cache Invalidation]]
- [[cache-stampede|Cache Stampede]]

## Open Questions

- Which endpoint classes in the system-design wiki should default to stale-while-revalidate?
