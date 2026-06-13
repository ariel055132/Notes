---
type: concept
aliases: ["API route", "API routes", "route routing", "gateway routing", "request routing"]
tags: [system-design, api-gateway, routing, microservices]
created: 2026-06-13
updated: 2026-06-13
source_count: 1
---

# API Routing

## Definition

API routing is the gateway function that maps an incoming request to the correct backend service or handler based on request attributes such as host, path, method, header, or API version. [[2026-05-15--api-gateway|API Gateway]]

## Scope

This concept covers public route mappings such as QR redirect paths, QR management APIs, campaign APIs, billing APIs, webhook APIs, analytics ingestion, and task APIs. [[2026-05-15--api-gateway|API Gateway]] It also covers hiding internal service splits so a service can be split into new handlers without breaking the client-facing URL contract. [[2026-05-15--api-gateway|API Gateway]]

## Contrasts

- **Load Balancing**: API routing chooses the logical backend service or handler; load balancing chooses among healthy instances of a selected service. [[2026-05-15--api-gateway|API Gateway]]
- **Service Discovery**: Service discovery tracks live backend instances, while API routing decides which backend target a public route represents. [[2026-05-15--zookeeper|Zookeeper]] [[2026-05-15--api-gateway|API Gateway]]
- **Domain Decision**: Routing selects where work goes; it should not decide whether a booking, payment, or market order is valid. [[2026-05-15--api-gateway|API Gateway]]

## Evidence

- [[2026-05-15--api-gateway|API Gateway]] — The source gives route examples for QR redirects, QR management, campaigns, billing, and analytics ingestion.

## Related

- [[api-gateway|API Gateway]]
- [[public-api-contract|Public API Contract]]
- [[api-versioning|API Versioning]]
- [[load-balancer|Load Balancer]]
- [[service-discovery|Service Discovery]]
- [[api-gateway-boundary|API Gateway Boundary]]

## Open Questions

- Which future source should compare path-based, host-based, header-based, and service-discovery-backed routing in production gateways?
