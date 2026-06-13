---
type: concept
aliases: ["API versions", "route versioning", "versioned API", "API compatibility"]
tags: [system-design, api-gateway, api-design, compatibility]
created: 2026-06-13
updated: 2026-06-13
source_count: 1
---

# API Versioning

## Definition

API versioning is the practice of exposing separate public API versions so clients can migrate over time while the system routes old and new contract shapes to appropriate handlers. [[2026-05-15--api-gateway|API Gateway]]

## Scope

This concept covers routes such as `/v1/webhooks/endpoints` and `/v2/webhooks/endpoints`, where the gateway can route different versions to different handlers. [[2026-05-15--api-gateway|API Gateway]] It is especially important for third-party APIs because partners cannot always upgrade immediately. [[2026-05-15--api-gateway|API Gateway]]

## Contrasts

- **Internal Refactor**: Internal services can be reorganized behind the gateway, while API versioning preserves the external contract for clients. [[2026-05-15--api-gateway|API Gateway]]
- **Request/Response Transformation**: Transformation can adapt old and new field shapes, while versioning exposes explicit contract versions. [[2026-05-15--api-gateway|API Gateway]]

## Evidence

- [[2026-05-15--api-gateway|API Gateway]] — The source uses `/v1` and `/v2` webhook endpoint routes as an example of gateway-level version routing.

## Related

- [[public-api-contract|Public API Contract]]
- [[api-routing|API Routing]]
- [[request-response-transformation|Request/Response Transformation]]
- [[backend-for-frontend|Backend For Frontend]]

## Open Questions

- Which future source should compare URL, header, media-type, and date-based API versioning strategies?
