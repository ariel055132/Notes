---
type: concept
aliases: ["body size limit", "request body limit", "payload size limit", "upload size limit"]
tags: [system-design, api-gateway, reliability, upload]
created: 2026-06-13
updated: 2026-06-13
source_count: 1
---

# Request Size Limit

## Definition

Request size limit is the gateway policy that rejects request bodies above an allowed size so large blobs do not overload ordinary API request paths. [[2026-05-15--api-gateway|API Gateway]]

## Scope

This concept covers rejecting oversized bodies at the gateway and routing large files, images, videos, LLM outputs, or bulk uploads toward object storage and signed upload flows instead of posting them directly through API servers. [[2026-05-15--api-gateway|API Gateway]]

## Contrasts

- **Object Storage**: Request size limits protect API servers, while object storage is the durable target for large file or media bytes. [[2026-04-15--database|Database]] [[2026-05-15--api-gateway|API Gateway]]
- **Signed CDN Access**: Request size limits are about inbound upload protection, while signed CDN access is a related bounded-access pattern for serving private files after authorization. [[2026-05-15--cdn-content-delivery-network|CDN (Content Delivery Network)]] [[2026-05-15--api-gateway|API Gateway]]

## Evidence

- [[2026-05-15--api-gateway|API Gateway]] — The source says large files should not pass through API servers and gives object-storage pre-signed URLs as the better path for media or large LLM results.

## Related

- [[api-gateway|API Gateway]]
- [[object-storage|Object Storage]]
- [[signed-cdn-access|Signed CDN Access]]
- [[api-gateway-observability|API Gateway Observability]]

## Open Questions

- Which future source should cover direct-to-object-storage upload, multipart upload, virus scanning, and metadata commit workflows?
