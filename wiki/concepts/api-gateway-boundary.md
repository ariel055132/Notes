---
type: concept
aliases: ["gateway boundary", "thin gateway", "gateway domain boundary", "API gateway scope"]
tags: [system-design, api-gateway, architecture, boundaries]
created: 2026-06-13
updated: 2026-06-13
source_count: 1
---

# API Gateway Boundary

## Definition

API Gateway boundary is the architectural rule that a gateway should enforce public entry policy and API contract concerns without absorbing core domain decisions or long-running workflows. [[2026-05-15--api-gateway|API Gateway]]

## Scope

This concept covers keeping the gateway responsible for routing, authentication, coarse authorization, rate limiting, TLS, CORS, request IDs, versioning, logging, tracing, and light transformation. [[2026-05-15--api-gateway|API Gateway]] It excludes booking-rule decisions, payment capture, market-order matching, data-level authorization, transaction success, signature verification that needs domain data, idempotency decisions, and long-running task execution. [[2026-05-15--api-gateway|API Gateway]]

## Contrasts

- **Domain Service**: Domain services own business rules, resource permissions, transactions, and durable state transitions; the gateway owns entry control and shared request policy. [[2026-05-15--api-gateway|API Gateway]]
- **Backend For Frontend**: Backend For Frontend can intentionally be more client-specific and aggregating, while the shared gateway should remain thinner. [[2026-05-15--api-gateway|API Gateway]]
- **Message Queue**: A queue or worker handles deferred work after acceptance, while the gateway should not wait for long-running completion. [[2026-05-15--message-queue|Message Queue]] [[2026-05-15--api-gateway|API Gateway]]

## Evidence

- [[2026-05-15--api-gateway|API Gateway]] — The source repeatedly warns against making the gateway too thick and says core business logic should remain in domain services.

## Related

- [[api-gateway|API Gateway]]
- [[gateway-authorization|Gateway Authorization]]
- [[request-aggregation|Request Aggregation]]
- [[backend-for-frontend|Backend For Frontend]]
- [[asynchronous-processing|Asynchronous Processing]]
- [[database-transactions|Database Transactions]]
- [[idempotency-key|Idempotency Key]]

## Open Questions

- Which future synthesis should define "belongs in gateway" versus "belongs in service" decision criteria for system-design interviews?
