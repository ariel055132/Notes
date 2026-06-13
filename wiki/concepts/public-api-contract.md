---
type: concept
aliases: ["public API contract", "external API contract", "client-facing API contract", "API contract"]
tags: [system-design, api-gateway, api-design]
created: 2026-06-13
updated: 2026-06-13
source_count: 1
---

# Public API Contract

## Definition

Public API contract is the stable client-facing request and response surface that a system exposes while hiding internal service topology and implementation changes. [[2026-05-15--api-gateway|API Gateway]]

## Scope

This concept covers paths, methods, versions, headers, error shape, request and response fields, and client expectations around stability. [[2026-05-15--api-gateway|API Gateway]] The source treats API Gateway as the natural owner of public API contract entry policy, especially when internal services are split, renamed, or reorganized without breaking clients. [[2026-05-15--api-gateway|API Gateway]]

## Contrasts

- **Internal Service Boundary**: The public contract is what clients depend on, while internal service boundaries can change behind gateway routing. [[2026-05-15--api-gateway|API Gateway]]
- **API Versioning**: API versioning is one mechanism for evolving a public API contract without forcing all clients to upgrade at once. [[2026-05-15--api-gateway|API Gateway]]
- **Request/Response Transformation**: Transformation adapts fields or formats so the public contract can remain stable while internal contracts evolve. [[2026-05-15--api-gateway|API Gateway]]

## Evidence

- [[2026-05-15--api-gateway|API Gateway]] — The source says clients should know the public API, not how backend services are split, and positions the gateway as the external API contract entry point.

## Related

- [[api-gateway|API Gateway]]
- [[api-routing|API Routing]]
- [[api-versioning|API Versioning]]
- [[request-response-transformation|Request/Response Transformation]]
- [[backend-for-frontend|Backend For Frontend]]

## Open Questions

- Which future source should define API compatibility rules for field addition, field removal, error formats, and version deprecation?
