---
type: concept
aliases: ["BFF", "backend for frontend", "client-specific backend", "frontend-specific backend"]
tags: [system-design, api-gateway, api-design, frontend]
created: 2026-06-13
updated: 2026-06-13
source_count: 1
---

# Backend For Frontend

## Definition

Backend For Frontend is a backend layer tailored to one client type, such as web, mobile, or partner API, so each client receives an API shape that matches its user experience and constraints. [[2026-05-15--api-gateway|API Gateway]]

## Scope

This concept covers patterns such as Web App to Web Backend For Frontend, Mobile App to Mobile Backend For Frontend, and Partner API to a public API Gateway. [[2026-05-15--api-gateway|API Gateway]] The source gives examples where a web dashboard may fetch campaign, scan summary, and billing status together, while a mobile app may need recent QR codes and simplified state, and a partner API may need stable versioning, API keys, strict rate limits, and clear error codes. [[2026-05-15--api-gateway|API Gateway]]

## Contrasts

- **API Gateway**: API Gateway is the shared external entry and policy layer, while Backend For Frontend is client-specific and may own more aggregation or response shaping for one client. [[2026-05-15--api-gateway|API Gateway]]
- **Request Aggregation**: Request aggregation is one behavior a Backend For Frontend may perform, while Backend For Frontend is the broader client-specific service boundary. [[2026-05-15--api-gateway|API Gateway]]
- **Frontend Logic**: Backend For Frontend reduces client-side aggregation, but it adds backend maintenance and can become tightly coupled to frontend needs. [[2026-05-15--api-gateway|API Gateway]]

## Evidence

- [[2026-05-15--api-gateway|API Gateway]] — The source defines Backend For Frontend as serving different API shapes for different clients and says it improves frontend experience at the cost of another service layer.

## Related

- [[api-gateway|API Gateway]]
- [[request-aggregation|Request Aggregation]]
- [[public-api-contract|Public API Contract]]
- [[api-versioning|API Versioning]]
- [[api-gateway-boundary|API Gateway Boundary]]

## Open Questions

- When should this wiki recommend Backend For Frontend versus GraphQL, gateway aggregation, or client-side composition for dashboard-style data?
