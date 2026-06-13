---
type: concept
aliases: ["edge gateway", "edge worker gateway", "edge API gateway", "edge policy layer"]
tags: [system-design, api-gateway, edge, cdn]
created: 2026-06-13
updated: 2026-06-13
source_count: 1
---

# Edge Gateway

## Definition

Edge gateway is the pattern of moving selected API Gateway responsibilities such as auth, redirect, cache, bot protection, or lightweight routing closer to users at edge infrastructure. [[2026-05-15--api-gateway|API Gateway]]

## Scope

This concept covers edge workers or edge gateway logic for high-volume redirect paths, bot protection, simple authentication, and cacheable public reads. [[2026-05-15--api-gateway|API Gateway]] The source warns that authority checks may still need origin services or replicated stores, so edge execution does not remove source-of-truth boundaries. [[2026-05-15--api-gateway|API Gateway]]

## Contrasts

- **CDN and Edge Caching**: CDN caching serves repeated cacheable content from edge, while edge gateway logic can also run lightweight request policy or redirect code. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]] [[2026-05-15--api-gateway|API Gateway]]
- **API Gateway**: Edge gateway is one deployment placement for selected gateway concerns, while API Gateway is the broader architectural role. [[2026-05-15--api-gateway|API Gateway]]
- **Domain Service**: Edge gateway can reduce latency for simple checks, but domain decisions that require authoritative state still belong in origin services or replicated authoritative stores. [[2026-05-15--api-gateway|API Gateway]]

## Evidence

- [[2026-05-15--api-gateway|API Gateway]] — The source mentions Cloudflare Workers or edge gateway for auth, redirect, cache, and bot protection when edge placement fits.

## Related

- [[api-gateway|API Gateway]]
- [[cdn-and-edge-caching|CDN and Edge Caching]]
- [[cdn-cache-key-design|CDN Cache-Key Design]]
- [[hot-key|Hot Key]]
- [[api-gateway-boundary|API Gateway Boundary]]

## Open Questions

- Which future source should compare edge workers, CDN cache rules, API gateways, and service mesh gateways for global read and redirect paths?
