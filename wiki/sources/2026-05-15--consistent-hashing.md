---
type: source
source_path: raw/archive/Consistent Hashing.pdf
title: "Consistent Hashing"
author: "BuildMoat"
date: 2026-05-15
tags: [system-design, load-distribution, sharding, caching]
created: 2026-05-24
---

# Consistent Hashing

## Summary

This source explains consistent hashing as a system-design routing strategy for keeping key ownership stable while nodes are added or removed. [[2026-05-15--consistent-hashing|Consistent Hashing]] It contrasts consistent hashing with direct `hash(key) % N`, where changing `N` can remap many keys and cause cache misses, data movement, connection redistribution, and cluster-wide churn. [[2026-05-15--consistent-hashing|Consistent Hashing]] The source describes the hash ring model, where both keys and nodes are placed in the same hash space and each key maps clockwise to the next node, limiting membership-change impact to adjacent ranges. [[2026-05-15--consistent-hashing|Consistent Hashing]] It also emphasizes virtual nodes for better balance, fixed hash slots as a related production pattern, and the limits of consistent hashing: it does not solve hot keys, replication, failover, consistency, or data migration by itself. [[2026-05-15--consistent-hashing|Consistent Hashing]]

## Key Claims

1. Consistent hashing solves stable key ownership under membership changes: the node set may change, but most keys should keep the same owner. [[2026-05-15--consistent-hashing|Consistent Hashing]]
2. Direct modulo routing such as `hash(key) % number_of_nodes` is fragile because changing the node count can remap a large fraction of keys. [[2026-05-15--consistent-hashing|Consistent Hashing]]
3. A hash ring places both keys and nodes into one hash space; the owner is the first node reached clockwise from the key's position. [[2026-05-15--consistent-hashing|Consistent Hashing]]
4. Adding a node should affect only the key range the new node takes from a neighboring node, while removing a node shifts only that failed node's range to the next node. [[2026-05-15--consistent-hashing|Consistent Hashing]]
5. Virtual nodes improve ring balance, make movement more granular, and let higher-capacity physical nodes own more key ranges. [[2026-05-15--consistent-hashing|Consistent Hashing]]
6. Consistent hashing is useful for distributed caches, rate limiter ownership, WebSocket room ownership, CDN or cache asset routing, and custom routing layers where the same key should usually go to the same owner. [[2026-05-15--consistent-hashing|Consistent Hashing]]
7. Consistent hashing reduces routing churn but does not automatically copy data, warm caches, provide replication, detect failures, coordinate consistency, or solve hot-key traffic concentration. [[2026-05-15--consistent-hashing|Consistent Hashing]]
8. Fixed hash slots, such as Redis Cluster's slot model, solve a similar key-ownership problem by hashing keys into stable slots and moving slot ownership rather than remapping all keys. [[2026-05-15--consistent-hashing|Consistent Hashing]]

## Notable Quotes

- "Consistent Hashing solves the problem that nodes change but key ownership should stay as stable as possible." [[2026-05-15--consistent-hashing|Consistent Hashing]]
- "Consistent hashing reduces the impact range of membership change on routing." [[2026-05-15--consistent-hashing|Consistent Hashing]]
- "It only solves routing stability, not a complete distributed database solution." [[2026-05-15--consistent-hashing|Consistent Hashing]]

## Entities Mentioned

- None. BuildMoat is treated as the source author/publisher in frontmatter rather than as a dedicated entity page. [[2026-05-15--consistent-hashing|Consistent Hashing]]

## Concepts Mentioned

- [[consistent-hashing|Consistent Hashing]] — Stable key-to-owner routing under node membership changes. [[2026-05-15--consistent-hashing|Consistent Hashing]]
- [[virtual-nodes|Virtual Nodes]] — Multiple hash-ring positions per physical node to improve balance and movement granularity. [[2026-05-15--consistent-hashing|Consistent Hashing]]
- [[fixed-hash-slots|Fixed Hash Slots]] — A stable slot-based key ownership model used by systems such as Redis Cluster. [[2026-05-15--consistent-hashing|Consistent Hashing]]
- [[hash-based-sharding|Hash-Based Sharding]] — Hashing a key for distribution, with modulo routing as the naive form and consistent hashing or slots as more stable forms. [[2026-05-15--consistent-hashing|Consistent Hashing]]
- [[virtual-buckets|Virtual Buckets]] — A related strategy where keys map to stable logical buckets before those buckets map to physical nodes. [[2026-05-15--consistent-hashing|Consistent Hashing]]
- [[resharding|Resharding]] — Changing ownership mappings as nodes are added, removed, or rebalanced. [[2026-05-15--consistent-hashing|Consistent Hashing]]
- [[hot-key|Hot Key]] — A single popular key can overload its owner even when key counts are evenly distributed. [[2026-05-15--consistent-hashing|Consistent Hashing]]
- [[application-level-caching|Application-Level Caching]] — A common use case where stable cache-key routing avoids broad cache churn during cluster changes. [[2026-05-15--consistent-hashing|Consistent Hashing]]
- [[database-sharding|Database Sharding]] — The broader distributed-data context in which key ownership and rebalancing matter. [[2026-05-15--consistent-hashing|Consistent Hashing]]

## Follow-ups

- Build a synthesis comparing consistent hashing, virtual buckets, fixed hash slots, and directory-based sharding as ownership-mapping strategies.
