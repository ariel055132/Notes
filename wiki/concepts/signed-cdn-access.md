---
type: concept
aliases: ["signed URL", "signed URLs", "signed cookie", "signed cookies", "signed CDN URL"]
tags: [system-design, cdn, caching, access-control]
created: 2026-05-26
updated: 2026-05-26
source_count: 1
---

# Signed CDN Access

## Definition

Signed CDN access is a pattern where an application authorizes a user first, then issues a short-lived signed URL or signed cookie that allows the CDN to serve a private file without making the asset permanently public. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]

## Scope

This concept covers private downloads such as course PDFs, SDK packages, media files, or other assets stored behind CDN where the application remains responsible for enrollment, payment, or permission checks. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]] The source recommends short expiration, and when needed IP or user scoping, so leaked URLs do not provide long-lived access. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]

## Contrasts

- **Public CDN Caching**: Public CDN caching serves shared content directly by cache key, while signed CDN access preserves an application authorization step before edge delivery. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]
- **Application Authorization**: Application authorization decides whether a user may access an asset; signed CDN access delegates the subsequent file transfer to the CDN for a bounded time. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]
- **No-Store Responses**: Highly personalized or correctness-sensitive responses may need `no-store`, while private static files can sometimes be served through signed CDN URLs after authorization. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]]

## Evidence

- [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]] — The source describes a course platform flow where the app checks enrollment, returns a short-lived signed CDN URL, and the student downloads the PDF from edge.

## Related

- [[cdn-and-edge-caching|CDN and Edge Caching]]
- [[cdn-cache-key-design|CDN Cache-Key Design]]
- [[object-storage|Object Storage]]
- [[cache-invalidation|Cache Invalidation]]

## Open Questions

- Which future security source should compare signed URLs, signed cookies, origin authorization, and token-bound downloads?
