---
type: concept
aliases: ["rate limit", "API rate limit", "quota", "abuse protection", "traffic limit"]
tags: [system-design, api-gateway, reliability, abuse-protection]
created: 2026-06-13
updated: 2026-06-13
source_count: 1
---

# Rate Limiting

## Definition

Rate limiting controls how many requests a caller, tenant, API key, endpoint, or route group may send within a time window so excessive or abusive traffic is rejected before backend services absorb it. [[2026-05-15--api-gateway|API Gateway]]

## Scope

This concept covers limits by IP, user, tenant, API key, endpoint, and route group. [[2026-05-15--api-gateway|API Gateway]] The source gives examples such as tenant-level webhook management limits, endpoint-level public webhook ingress limits, and user-level task creation or run-now limits. [[2026-05-15--api-gateway|API Gateway]] It also covers distributed rate-limit counters in Redis or a dedicated rate-limit service because gateway instances cannot each count locally and still enforce a correct global limit. [[2026-05-15--api-gateway|API Gateway]]

## Contrasts

- **Backpressure**: Rate limiting rejects or slows upstream traffic before it enters the system, while backpressure responds when downstream capacity is already under pressure. [[2026-05-15--message-queue|Message Queue]] [[2026-05-15--api-gateway|API Gateway]]
- **Cache Fallback Limit**: Cache fallback limits protect databases during cache failure, while gateway rate limits protect API entry points and backend services from client traffic volume. [[2026-05-15--distributed-cache|Distributed Cache]] [[2026-05-15--api-gateway|API Gateway]]
- **Business Quota**: Gateway rate limits fit broad traffic protection; precise business quota decisions may require domain data and should stay in services. [[2026-05-15--api-gateway|API Gateway]]

## Evidence

- [[2026-05-15--api-gateway|API Gateway]] — The source describes gateway-level rate limits, `HTTP 429 Too Many Requests`, shared Redis counters, and fail-open versus fail-closed choices.

## Related

- [[api-gateway|API Gateway]]
- [[api-gateway-observability|API Gateway Observability]]
- [[distributed-cache|Distributed Cache]]
- [[cache-fallback-limit|Cache Fallback Limit]]
- [[backpressure|Backpressure]]
- [[api-gateway-boundary|API Gateway Boundary]]

## Open Questions

- Which future source should define token bucket, leaky bucket, fixed window, sliding window, and distributed rate-limit algorithms?
