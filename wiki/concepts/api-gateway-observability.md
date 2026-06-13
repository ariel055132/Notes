---
type: concept
aliases: ["gateway observability", "API observability", "gateway metrics", "API gateway metrics"]
tags: [system-design, api-gateway, observability, operations]
created: 2026-06-13
updated: 2026-06-13
source_count: 1
---

# API Gateway Observability

## Definition

API Gateway observability is the set of metrics, logs, and traces used to determine whether failures or latency originate in the gateway, network, authentication, rate limiting, or backend services. [[2026-05-15--api-gateway|API Gateway]]

## Scope

This concept covers request rate by route, p50/p95/p99 latency, gateway upstream latency, 4xx and 5xx rate, rate-limit hit count, auth failure count, rejected body count, timeout count, backend circuit-breaker open count, Redis rate-limit latency, gateway CPU, TLS and JWT verification cost, and active connections. [[2026-05-15--api-gateway|API Gateway]]

## Contrasts

- **Request ID**: Request ID correlates one request across logs and traces, while gateway observability is the broader operational view over all requests. [[2026-05-15--api-gateway|API Gateway]]
- **Queue Health Metrics**: Queue metrics explain asynchronous backlog and worker health, while gateway metrics explain the synchronous entry path and upstream calls. [[2026-05-15--message-queue|Message Queue]] [[2026-05-15--api-gateway|API Gateway]]

## Evidence

- [[2026-05-15--api-gateway|API Gateway]] — The source lists the metrics a gateway should watch to diagnose gateway, network, auth, rate-limit, and backend issues.

## Related

- [[api-gateway|API Gateway]]
- [[request-id|Request ID]]
- [[rate-limiting|Rate Limiting]]
- [[api-timeout|API Timeout]]
- [[queue-health-metrics|Queue Health Metrics]]
- [[backpressure|Backpressure]]

## Open Questions

- Which future observability source should define trace boundaries and span naming conventions across CDN, gateway, service, database, queue, and worker layers?
