---
type: source
source_path: raw/archive/CDN (Content Delivery Network).pdf
title: "CDN (Content Delivery Network)"
author: "BuildMoat"
date: 2026-05-15
tags: [system-design, cdn, caching, read-scaling, reliability]
created: 2026-05-26
---

# CDN (Content Delivery Network)

## Summary

This source frames CDN as an edge read-path layer for public, shareable, repeatedly read content whose latency and origin load improve when served near users. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]] It emphasizes that CDN design is not just drawing `client -> edge -> origin`; the important system-design work is deciding what is cacheable, how cache keys are formed, how content is updated, and how origin is protected when cache misses concentrate. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]] The source treats CDN as especially useful for static assets, images, video segments, public downloads, and carefully keyed public API responses. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]] It also warns that personalized data, real-time authorization, inventory, and other correctness-sensitive responses should not be casually pushed into a shared edge cache. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]

## Key Claims

1. CDN solves global distance from origin and repeated-origin overload, not every slow API problem. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]
2. CDN answers should begin with four questions: whether content is shareable, how often it changes, whether edge can answer without dynamic checks, and whether origin can survive cache misses. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]
3. Static assets, images, thumbnails, video chunks, manifests, public downloads, and public API responses are common CDN candidates when cache keys and freshness are controlled. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]
4. CDN cache-key design must account for path, query string, headers, cookies, authorization, and `Vary`, because a bad shared cache key can leak personalized data. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]
5. Versioned URLs are often safer than frequent global purge for normal releases, while purge is better reserved for emergency removal, policy violations, or security fixes. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]
6. Private downloads can still use CDN when application authorization issues short-lived signed URLs or signed cookies rather than making private assets permanently public. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]
7. Object storage should remain the durable source for files while CDN provides nearby transport and cache; edge cache may evict objects or vary by region. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]
8. Cache-miss storms can overload origin when popular content launches or cached content is purged, so CDN designs need origin shielding, request coalescing, warmup, and fallback controls. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]
9. CDN observability should include cache hit ratio, origin egress, edge latency, 4xx/5xx rate, and purge latency rather than only whether CDN exists in the architecture diagram. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]

## Notable Quotes

- "CDN 的本質是把「可共享、可重複讀、可接受短暫舊資料」的內容推到邊緣。" [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]
- "如果你可以控制 URL，通常「versioned URL」比頻繁 purge 更好。" [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]
- "不要把 CDN 當成唯一資料來源。" [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]

## Entities Mentioned

- None. BuildMoat is treated as the source author/publisher in frontmatter, while YouTube, Airbnb, and QR Code Generator are treated as illustrative product examples rather than dedicated entity pages in this ingest. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]

## Concepts Mentioned

- [[cdn-and-edge-caching|CDN and Edge Caching]] — Serving cacheable content from edge locations near users to reduce latency and origin load. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]
- [[cdn-cache-key-design|CDN Cache-Key Design]] — Choosing the path, query string, headers, cookies, and authorization dimensions that define a shared edge-cache entry. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]
- [[signed-cdn-access|Signed CDN Access]] — Using short-lived signed URLs or signed cookies so private downloadable files can be served by CDN after application authorization. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]
- [[object-storage|Object Storage]] — Durable file storage that remains the source for CDN origin fetches. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]
- [[cache-invalidation|Cache Invalidation]] — TTL, versioned URLs, and purge strategies for replacing stale edge content. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]
- [[freshness-budget|Freshness Budget]] — The tolerated stale window that determines whether CDN, TTL, or stale-while-revalidate is safe. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]
- [[stale-while-revalidate|Stale-While-Revalidate]] — Returning bounded stale edge content while refreshing in the background. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]
- [[read-through-cache|Read-Through Cache]] — CDN edge miss behavior where the edge fetches from origin and stores the response. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]
- [[cache-stampede|Cache Stampede]] — Cache-miss storms against origin after popular content launch or purge. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]
- [[cache-warming|Cache Warming]] — Preloading or warming popular CDN content before full traffic arrives. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]
- [[cache-fallback-limit|Cache Fallback Limit]] — Protecting origin when edge cache misses or fails. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]
- [[hot-key|Hot Key]] — A viral object, image, video segment, or landing page can become a hot content object even when served through CDN. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]

## Follow-ups

- Create a synthesis comparing CDN, distributed cache, object storage, and application cache as distinct read-path layers with different ownership, freshness, and privacy boundaries.
