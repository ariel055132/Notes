---
type: concept
aliases: ["API aggregation", "gateway aggregation", "response aggregation", "fan-out aggregation"]
tags: [system-design, api-gateway, api-design, latency]
created: 2026-06-13
updated: 2026-06-13
source_count: 1
---

# Request Aggregation

## Definition

Request aggregation is the pattern of making one client-facing API endpoint gather data from multiple backend services to reduce client round trips or create a client-specific response shape. [[2026-05-15--api-gateway|API Gateway]]

## Scope

This concept covers endpoints such as a booking page that needs listing data, pricing, availability, and review summary from separate services. [[2026-05-15--api-gateway|API Gateway]] The source says aggregation is a thicker gateway responsibility that can help clients, but it also makes the gateway understand more business context and can turn a general gateway into a large orchestration layer. [[2026-05-15--api-gateway|API Gateway]]

## Contrasts

- **Backend For Frontend**: Backend For Frontend is often the better home for client-specific aggregation, while a shared API Gateway should avoid becoming a large orchestration layer. [[2026-05-15--api-gateway|API Gateway]]
- **Request/Response Transformation**: Transformation adapts contract fields, while aggregation coordinates multiple backend calls. [[2026-05-15--api-gateway|API Gateway]]
- **Domain Service**: Aggregation can combine read models, but business decisions and state transitions still belong in domain services. [[2026-05-15--api-gateway|API Gateway]]

## Evidence

- [[2026-05-15--api-gateway|API Gateway]] — The source gives an Airbnb-style booking page example and warns to avoid making the gateway a large orchestration layer.

## Related

- [[api-gateway|API Gateway]]
- [[backend-for-frontend|Backend For Frontend]]
- [[request-response-transformation|Request/Response Transformation]]
- [[read-scaling|Read Scaling]]
- [[materialized-view|Materialized View]]

## Open Questions

- Which future source should compare gateway aggregation, Backend For Frontend, GraphQL federation, materialized read models, and client-side composition?
