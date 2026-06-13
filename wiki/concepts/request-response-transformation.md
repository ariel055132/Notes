---
type: concept
aliases: ["request transformation", "response transformation", "protocol translation", "field transformation", "schema transformation"]
tags: [system-design, api-gateway, api-design, compatibility]
created: 2026-06-13
updated: 2026-06-13
source_count: 1
---

# Request/Response Transformation

## Definition

Request/response transformation is the gateway responsibility of making lightweight changes to incoming requests or outgoing responses so public API contracts and internal service contracts can differ safely. [[2026-05-15--api-gateway|API Gateway]]

## Scope

This concept covers adding `X-Request-Id`, translating JWT claims into internal headers, mapping old `/v1` fields into newer service fields, translating REST requests to gRPC calls, standardizing error format, removing internal fields from responses, and maintaining compatibility for public API versions. [[2026-05-15--api-gateway|API Gateway]]

## Contrasts

- **Domain Logic**: Transformation adapts contract shape; it should not decide booking rules, payment capture, market matching, or other domain outcomes. [[2026-05-15--api-gateway|API Gateway]]
- **Request Aggregation**: Transformation changes one request or response shape, while aggregation coordinates multiple backend calls for one client-facing response. [[2026-05-15--api-gateway|API Gateway]]
- **API Versioning**: Versioning exposes multiple public contracts, while transformation can bridge contract differences behind those versions. [[2026-05-15--api-gateway|API Gateway]]

## Evidence

- [[2026-05-15--api-gateway|API Gateway]] — The source lists request and response transformation examples and warns that the gateway should not become the business-logic center.

## Related

- [[api-gateway|API Gateway]]
- [[public-api-contract|Public API Contract]]
- [[api-versioning|API Versioning]]
- [[request-aggregation|Request Aggregation]]
- [[api-gateway-boundary|API Gateway Boundary]]

## Open Questions

- Which future source should compare gateway transformation, adapter services, anti-corruption layers, and API schema evolution?
