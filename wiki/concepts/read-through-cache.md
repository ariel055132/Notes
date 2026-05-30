---
type: concept
aliases: ["read-through caching", "read through cache"]
tags: [system-design, caching, cdn, read-scaling]
created: 2026-05-24
updated: 2026-05-26
source_count: 2
---

# Read-Through Cache

## Definition

Read-through cache is a caching pattern where the cache layer knows how to fetch data from the origin or source of truth on a miss, then returns and stores the result. [[2026-05-24--caching|Caching]] CDN edge caching is a common read-through-like form: an edge miss fetches from origin or object storage, caches the response, and serves later edge hits. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]

## Scope

This concept covers systems where application code asks the cache and the cache layer itself performs origin fetch on miss. [[2026-05-24--caching|Caching]] CDN edge caching is a common read-through-like example because an edge miss goes to origin or object storage, stores the response, and serves future edge hits. [[2026-05-24--caching|Caching]] [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]

## Contrasts

- **Cache-Aside**: Read-through hides miss-fetch logic in the cache layer, while cache-aside keeps miss-fetch logic in application code. [[2026-05-24--caching|Caching]]
- **CDN and Edge Caching**: CDN behavior is often read-through-like at the edge, while application-level Redis caches are more commonly cache-aside because application code knows database schema and fallback logic. [[2026-05-24--caching|Caching]]
- **Object Storage**: Object storage can be the durable origin that a CDN reads through to, while the CDN stores temporary edge copies. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]

## Evidence

- [[2026-05-24--caching|Caching]] — The source explains read-through through the cache-layer miss flow and compares it to CDN origin fetch.
- [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]] — The source describes the CDN flow where edge cache misses fetch from origin or object storage, store a copy, and return content.

## Related

- [[cache-aside|Cache-Aside]]
- [[cdn-and-edge-caching|CDN and Edge Caching]]
- [[application-level-caching|Application-Level Caching]]
- [[cache-stampede|Cache Stampede]]
- [[object-storage|Object Storage]]

## Open Questions

- Which future source should compare read-through caches in CDN, database proxy, and service-mesh contexts?
