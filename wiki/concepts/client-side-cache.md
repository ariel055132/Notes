---
type: concept
aliases: ["client cache", "browser cache", "mobile cache", "client-side caching"]
tags: [system-design, caching, clients]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Client-Side Cache

## Definition

Client-side cache stores data in a browser, mobile app, or client library so repeated reads can avoid a network request or start with a local answer. [[2026-05-24--caching|Caching]]

## Scope

This concept covers static assets, recently viewed listings, small app-start configuration, and client or service-library metadata such as cluster routing information. [[2026-05-24--caching|Caching]] It is useful for latency and offline-friendly behavior but is hard to invalidate immediately across all clients, so it is not enough for security-sensitive or correctness-critical data. [[2026-05-24--caching|Caching]]

## Contrasts

- **In-Process Cache**: Client-side cache lives on the user's device or client library, while in-process cache lives inside an application server process. [[2026-05-24--caching|Caching]]
- **CDN and Edge Caching**: Client-side cache avoids even edge requests when valid, while CDN/edge cache still serves over the network from an edge node. [[2026-05-24--caching|Caching]]

## Evidence

- [[2026-05-24--caching|Caching]] — The source lists client-side cache as appropriate for low-risk local data and warns that freshness is difficult to control across all clients.

## Related

- [[cdn-and-edge-caching|CDN and Edge Caching]]
- [[in-process-cache|In-Process Cache]]
- [[freshness-budget|Freshness Budget]]
- [[cache-invalidation|Cache Invalidation]]

## Open Questions

- Which future source should cover browser cache headers, service workers, and mobile cache invalidation?
