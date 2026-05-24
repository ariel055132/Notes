---
type: concept
aliases: ["CDN", "edge caching", "content delivery network", "origin offload"]
tags: [system-design, caching, cdn]
created: 2026-05-24
updated: 2026-05-24
source_count: 2
---

# CDN and Edge Caching

## Definition

CDN and edge caching move public cacheable content closer to users so requests can be served from edge locations instead of origin servers and databases. [[2026-05-14--scaling-reads|Scaling Reads]] CDN behavior is often read-through-like: an edge miss fetches from origin, stores the result, and serves later edge hits. [[2026-05-24--caching|Caching]]

## Scope

This concept covers static assets, thumbnails, video chunks, manifest files, public landing images, public listing pages, public API responses, short-lived search or category pages, cache keys, origin offload, latency reduction, and conservative handling of personalized or sensitive data. [[2026-05-14--scaling-reads|Scaling Reads]] [[2026-05-24--caching|Caching]]

## Contrasts

- **Application-Level Caching**: Application-level cache reduces database load near backend services, while CDN/edge caching can keep repeated public reads from reaching origin at all. [[2026-05-14--scaling-reads|Scaling Reads]]
- **Private personalized cache**: CDN/edge caching is most aggressive for public shared responses, while personalized or sensitive responses need strict cache-key and privacy controls. [[2026-05-14--scaling-reads|Scaling Reads]]
- **Read-Through Cache**: CDN/edge caching is a common read-through-like cache, while application-level Redis caches are more often cache-aside because the application handles source lookup. [[2026-05-24--caching|Caching]]

## Evidence

- [[2026-05-14--scaling-reads|Scaling Reads]] — The source says CDN reduces user latency and origin load, but requires careful cache-key design around URLs, query strings, headers, cookies, and authorization.
- [[2026-05-24--caching|Caching]] — The source uses YouTube video assets and thumbnails, QR landing assets, and product images as CDN-friendly examples.

## Related

- [[read-scaling|Read Scaling]]
- [[freshness-budget|Freshness Budget]]
- [[application-level-caching|Application-Level Caching]]
- [[read-through-cache|Read-Through Cache]]
- [[client-side-cache|Client-Side Cache]]
- [[cache-invalidation|Cache Invalidation]]
- [[hot-key|Hot Key]]

## Open Questions

- Which CDN cache-key examples should be documented for public APIs versus personalized APIs?
