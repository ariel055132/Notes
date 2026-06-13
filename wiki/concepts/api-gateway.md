---
type: concept
aliases: ["API gateway", "gateway", "public API gateway", "API entry point"]
tags: [system-design, api-gateway, microservices, routing]
created: 2026-06-13
updated: 2026-06-13
source_count: 1
---

# API Gateway

## Definition

API Gateway is the public entry point and policy layer that receives external API traffic, applies cross-cutting controls, and routes requests to internal backend services. [[2026-05-15--api-gateway|API Gateway]]

## Scope

This concept covers multi-service systems where clients should not know every internal service address, authentication scheme, route split, version handler, or error format. [[2026-05-15--api-gateway|API Gateway]] Typical gateway responsibilities include API routing, authentication, coarse authorization, rate limiting, TLS termination, CORS, request ID propagation, logging, tracing, versioning, and light request or response transformation. [[2026-05-15--api-gateway|API Gateway]]

## Contrasts

- **Load Balancer**: A load balancer mainly distributes traffic across instances, while an API Gateway understands API contracts and applies route-level policy. [[2026-05-15--api-gateway|API Gateway]]
- **Backend For Frontend**: Backend For Frontend shapes APIs for a specific client experience, while a general API Gateway should stay closer to entry control and shared policy. [[2026-05-15--api-gateway|API Gateway]]
- **Domain Service**: A domain service owns business decisions and data-level authorization; the gateway should not become a second application server. [[2026-05-15--api-gateway|API Gateway]]

## Evidence

- [[2026-05-15--api-gateway|API Gateway]] — The source defines API Gateway as the first control layer for external traffic and the first protection line for backend services.

## Related

- [[public-api-contract|Public API Contract]]
- [[api-routing|API Routing]]
- [[gateway-authentication|Gateway Authentication]]
- [[gateway-authorization|Gateway Authorization]]
- [[rate-limiting|Rate Limiting]]
- [[load-balancer|Load Balancer]]
- [[backend-for-frontend|Backend For Frontend]]
- [[api-gateway-boundary|API Gateway Boundary]]

## Open Questions

- Which future source should compare API Gateway, ingress controller, reverse proxy, service mesh gateway, and edge worker in one traffic-entry taxonomy?
