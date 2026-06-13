---
type: concept
aliases: ["request ID", "request identifier", "correlation ID", "trace ID"]
tags: [system-design, api-gateway, observability, tracing]
created: 2026-06-13
updated: 2026-06-13
source_count: 1
---

# Request ID

## Definition

Request ID is a correlation identifier that a gateway creates or propagates so logs, metrics, and traces across backend services can be connected to the same incoming request. [[2026-05-15--api-gateway|API Gateway]]

## Scope

This concept covers injecting or forwarding identifiers such as `X-Request-Id` from the gateway to backend services. [[2026-05-15--api-gateway|API Gateway]] The source treats request ID propagation as a gateway responsibility because the gateway is the external request entry point. [[2026-05-15--api-gateway|API Gateway]]

## Contrasts

- **API Gateway Observability**: Request ID is a correlation mechanism, while gateway observability is the broader metric, log, and trace view over gateway behavior. [[2026-05-15--api-gateway|API Gateway]]
- **Idempotency Key**: A request ID identifies and traces a request, while an idempotency key identifies an operation whose repeated execution must be deduplicated. [[2026-05-15--distributed-lock|Distributed Lock]] [[2026-05-15--api-gateway|API Gateway]]

## Evidence

- [[2026-05-15--api-gateway|API Gateway]] — The source says the gateway should generate or propagate request IDs so downstream logs, metrics, and traces can be stitched together.

## Related

- [[api-gateway|API Gateway]]
- [[api-gateway-observability|API Gateway Observability]]
- [[gateway-authentication|Gateway Authentication]]
- [[idempotency-key|Idempotency Key]]

## Open Questions

- Which future observability source should distinguish request ID, trace ID, span ID, operation ID, and idempotency key?
