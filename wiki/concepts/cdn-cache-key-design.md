---
type: concept
aliases: ["CDN cache key", "edge cache key", "cache key design", "Vary header"]
tags: [system-design, cdn, caching, privacy]
created: 2026-05-26
updated: 2026-05-26
source_count: 1
---

# CDN Cache-Key Design

## Definition

CDN cache-key design is the choice of request dimensions that define whether two edge requests are allowed to share the same cached response, including path, query string, headers, cookies, authorization state, and `Vary`. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]

## Scope

This concept covers public asset URLs, image transformation keys, API response keys, query-string handling, header and cookie inclusion, authorization-sensitive responses, and private or personalized content that must not collapse into one shared cache entry. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]] It also covers versioned URLs such as hashed JS/CSS filenames or image version suffixes, because versioned naming can make normal content updates safer than relying on global purge. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]

## Contrasts

- **Cache Routing**: Cache routing chooses which cache node owns a key, while CDN cache-key design chooses whether requests represent the same shareable response. [[2026-05-15--distributed-cache|Distributed Cache]] [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]
- **Shard Key**: A shard key partitions durable data ownership, while a CDN cache key partitions cached edge responses and must account for privacy and response variation. [[2026-05-15--sharding|Sharding]] [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]
- **Cache Invalidation**: Cache-key design can make invalidation easier through versioned URLs; invalidation is the later act of replacing or removing stale cached entries. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]

## Evidence

- [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]] — The source warns that CDN can accidentally share user-specific responses unless cache keys and headers account for cookies, authorization, `Cache-Control`, and `Vary`.

## Related

- [[cdn-and-edge-caching|CDN and Edge Caching]]
- [[cache-invalidation|Cache Invalidation]]
- [[freshness-budget|Freshness Budget]]
- [[cache-routing|Cache Routing]]
- [[signed-cdn-access|Signed CDN Access]]

## Open Questions

- Which future source should add concrete cache-key examples for public APIs, localized pages, authenticated APIs, and image transformations?
