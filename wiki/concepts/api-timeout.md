---
type: concept
aliases: ["API timeout", "gateway timeout", "request timeout", "HTTP timeout"]
tags: [system-design, api-gateway, reliability, latency]
created: 2026-06-13
updated: 2026-06-13
source_count: 1
---

# API Timeout

## Definition

API timeout is the bounded time a gateway or API server allows a synchronous HTTP request to remain open before returning an error or handing work off to an asynchronous path. [[2026-05-15--api-gateway|API Gateway]]

## Scope

This concept covers preventing long backend queries or long-running tasks from tying up gateway connections and causing cascading failure. [[2026-05-15--api-gateway|API Gateway]] The source recommends returning `202 Accepted` and a job identifier for long task creation while background workers complete the actual work. [[2026-05-15--api-gateway|API Gateway]]

## Contrasts

- **Asynchronous Processing**: Timeout protects synchronous request capacity; asynchronous processing moves slow work behind accepted or pending states. [[2026-05-15--message-queue|Message Queue]] [[2026-05-15--api-gateway|API Gateway]]
- **Visibility Timeout**: API timeout bounds a client-facing HTTP request, while visibility timeout controls how long a queued message is hidden from other consumers. [[2026-05-15--message-queue|Message Queue]] [[2026-05-15--api-gateway|API Gateway]]

## Evidence

- [[2026-05-15--api-gateway|API Gateway]] — The source says long tasks should not make the gateway wait and should return `202 Accepted` with a job ID.

## Related

- [[api-gateway|API Gateway]]
- [[asynchronous-processing|Asynchronous Processing]]
- [[message-queue|Message Queue]]
- [[visibility-timeout|Visibility Timeout]]
- [[api-gateway-observability|API Gateway Observability]]

## Open Questions

- Which future source should define timeout budgets across client, CDN, gateway, service, database, queue, and worker layers?
