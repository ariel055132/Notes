---
type: concept
aliases: ["gateway authz", "API authorization", "coarse authorization", "route authorization"]
tags: [system-design, api-gateway, security, authorization]
created: 2026-06-13
updated: 2026-06-13
source_count: 1
---

# Gateway Authorization

## Definition

Gateway authorization is the use of API Gateway to enforce coarse route, role, API-key, or tenant-member checks before forwarding requests to backend services. [[2026-05-15--api-gateway|API Gateway]]

## Scope

This concept covers checks such as requiring an admin role for `/admin/*`, requiring login for billing routes, requiring a valid API key for public APIs, and allowing webhook management APIs only for tenant members. [[2026-05-15--api-gateway|API Gateway]] The source limits gateway authorization to coarse checks and keeps data-level authorization in domain services. [[2026-05-15--api-gateway|API Gateway]]

## Contrasts

- **Gateway Authentication**: Authentication verifies identity, while gateway authorization applies broad access policy to routes or route groups. [[2026-05-15--api-gateway|API Gateway]]
- **Data-Level Authorization**: Data-level authorization asks whether a specific user can view a booking, replay a webhook delivery, operate on a market order, or cancel a task run; the source says these decisions require domain data and belong in services. [[2026-05-15--api-gateway|API Gateway]]

## Evidence

- [[2026-05-15--api-gateway|API Gateway]] — The source explicitly separates "who are you" at the gateway from "can you operate this resource" in backend services.

## Related

- [[api-gateway|API Gateway]]
- [[gateway-authentication|Gateway Authentication]]
- [[public-api-contract|Public API Contract]]
- [[api-gateway-boundary|API Gateway Boundary]]
- [[idempotency-key|Idempotency Key]]

## Open Questions

- Which future source should define policy decision points, policy enforcement points, and service-local authorization checks?
