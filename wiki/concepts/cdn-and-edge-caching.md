---
type: concept
aliases: ["CDN", "edge caching", "content delivery network", "origin offload"]
tags: [system-design, caching, cdn]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# CDN and Edge Caching

## Definition

CDN and edge caching move public cacheable content closer to users so requests can be served from edge locations instead of origin servers and databases. [[2026-05-14--scaling-reads|Scaling Reads]]

## Scope

This concept covers static assets, thumbnails, manifest files, public listing pages, public API responses, short-lived search or category pages, cache keys, origin offload, latency reduction, and conservative handling of personalized or sensitive data. [[2026-05-14--scaling-reads|Scaling Reads]]

## Contrasts

- **Application-Level Caching**: Application-level cache reduces database load near backend services, while CDN/edge caching can keep repeated public reads from reaching origin at all. [[2026-05-14--scaling-reads|Scaling Reads]]
- **Private personalized cache**: CDN/edge caching is most aggressive for public shared responses, while personalized or sensitive responses need strict cache-key and privacy controls. [[2026-05-14--scaling-reads|Scaling Reads]]

## Evidence

- [[2026-05-14--scaling-reads|Scaling Reads]] — The source says CDN reduces user latency and origin load, but requires careful cache-key design around URLs, query strings, headers, cookies, and authorization.

## Related

- [[read-scaling|Read Scaling]]
- [[freshness-budget|Freshness Budget]]
- [[application-level-caching|Application-Level Caching]]
- [[cache-invalidation|Cache Invalidation]]
- [[hot-key|Hot Key]]

## Open Questions

- Which CDN cache-key examples should be documented for public APIs versus personalized APIs?
