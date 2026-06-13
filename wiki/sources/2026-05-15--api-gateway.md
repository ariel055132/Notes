---
type: source
source_path: raw/archive/API Gateway.pdf
title: "API Gateway"
author: "BuildMoat"
date: 2026-05-15
tags: [system-design, api-gateway, microservices, routing, reliability]
created: 2026-06-13
---

# API Gateway

## Summary

This source frames API Gateway as the external traffic control point and public API contract for a system with multiple backend services. [[2026-05-15--api-gateway|API Gateway]] It emphasizes that a gateway is useful for cross-cutting concerns such as routing, authentication, coarse authorization, rate limiting, TLS termination, CORS, request IDs, logging, tracing, versioning, and light request or response transformation. [[2026-05-15--api-gateway|API Gateway]] The source repeatedly warns that a gateway should protect backend services without swallowing domain logic: booking rules, payment decisions, market matching, transaction outcomes, and long-running work still belong in services, databases, queues, or workers. [[2026-05-15--api-gateway|API Gateway]] It also distinguishes API Gateway from a load balancer and gives practical examples for QR redirects, webhook platforms, task APIs, trading APIs, and booking systems. [[2026-05-15--api-gateway|API Gateway]]

## Key Claims

1. API Gateway gives clients one stable public entry point while hiding internal service topology and service splits. [[2026-05-15--api-gateway|API Gateway]]
2. Gateway responsibilities fit best when they are API-contract or policy concerns, such as route selection, authentication, coarse authorization, rate limits, TLS, CORS, request IDs, versioning, and transformation. [[2026-05-15--api-gateway|API Gateway]]
3. Gateway routing can use host, path, method, header, or version to forward requests to the right backend handler or service. [[2026-05-15--api-gateway|API Gateway]]
4. Backends may trust identity headers injected by the gateway only when they cannot be reached directly from outside and internal paths are protected by private networking, mTLS, service mesh, or internal auth. [[2026-05-15--api-gateway|API Gateway]]
5. Coarse role or route authorization can live in the gateway, but data-level authorization that depends on domain state belongs in backend services. [[2026-05-15--api-gateway|API Gateway]]
6. Distributed rate limiting needs shared counters such as Redis or a dedicated rate-limit service; local per-instance counters produce inaccurate global limits. [[2026-05-15--api-gateway|API Gateway]]
7. Rate-limit failure mode should be explicit: product APIs may fail open to avoid blocking normal traffic, while login, payment, or sensitive APIs may fail closed or use local fallback limits. [[2026-05-15--api-gateway|API Gateway]]
8. Large uploads should not pass through ordinary API servers when object storage signed URLs or batch upload flows fit better. [[2026-05-15--api-gateway|API Gateway]]
9. Long-running tasks should not keep a gateway HTTP request open; the request should return an accepted state such as `202 Accepted` and a job identifier while workers complete the work. [[2026-05-15--api-gateway|API Gateway]]
10. Backend For Frontend layers can improve client-specific API shapes and reduce client round trips, but they add another backend layer and should not make a general gateway into a large orchestration service. [[2026-05-15--api-gateway|API Gateway]]
11. A load balancer distributes traffic among service instances, while an API Gateway understands API contracts and applies request-level policies. [[2026-05-15--api-gateway|API Gateway]]
12. Gateway observability should include route request rate, p50/p95/p99 latency, upstream latency, 4xx/5xx rate, rate-limit hits, auth failures, rejected body count, timeout count, circuit-breaker count, rate-limit-store latency, gateway CPU, and active connections. [[2026-05-15--api-gateway|API Gateway]]

## Notable Quotes

- "API Gateway 最好的定位是：外部 API contract 的入口與政策執行點，不是第二個 application server." [[2026-05-15--api-gateway|API Gateway]]
- "Gateway 可以確認「你是誰」，服務要判斷「你能不能操作這筆資源」." [[2026-05-15--api-gateway|API Gateway]]
- "Redirect path 要非常薄，不能做重 aggregation." [[2026-05-15--api-gateway|API Gateway]]
- "Gateway 只做入口控制，真正交易邏輯交給 trading service 或 sequencer." [[2026-05-15--api-gateway|API Gateway]]

## Entities Mentioned

- None. Product and organization names such as AWS API Gateway, Kong, Envoy, Nginx, Traefik, Cloudflare Workers, Redis, PostgreSQL, Polymarket, and Airbnb are treated as implementation examples or scenario labels in this ingest rather than standalone entity pages. [[2026-05-15--api-gateway|API Gateway]]

## Concepts Mentioned

- [[api-gateway|API Gateway]] — A public API entry point and request-policy layer for multi-service systems. [[2026-05-15--api-gateway|API Gateway]]
- [[public-api-contract|Public API Contract]] — The stable client-facing API surface protected from internal service topology changes. [[2026-05-15--api-gateway|API Gateway]]
- [[api-routing|API Routing]] — Forwarding requests by host, path, method, header, or version. [[2026-05-15--api-gateway|API Gateway]]
- [[api-versioning|API Versioning]] — Preserving older public API versions while routing newer versions to different handlers. [[2026-05-15--api-gateway|API Gateway]]
- [[gateway-authentication|Gateway Authentication]] — Verifying request identity at the system entry point. [[2026-05-15--api-gateway|API Gateway]]
- [[gateway-authorization|Gateway Authorization]] — Applying coarse route or role checks at the gateway while leaving domain authorization to services. [[2026-05-15--api-gateway|API Gateway]]
- [[rate-limiting|Rate Limiting]] — Limiting traffic by IP, user, tenant, API key, endpoint, or route group before backends absorb abusive or excessive requests. [[2026-05-15--api-gateway|API Gateway]]
- [[tls-termination|TLS Termination]] — Centralizing public certificate handling at the gateway or edge. [[2026-05-15--api-gateway|API Gateway]]
- [[cross-origin-resource-sharing|Cross-Origin Resource Sharing]] — Gateway-level handling of browser API access policy. [[2026-05-15--api-gateway|API Gateway]]
- [[request-size-limit|Request Size Limit]] — Rejecting oversized request bodies and routing large blobs toward object storage flows. [[2026-05-15--api-gateway|API Gateway]]
- [[api-timeout|API Timeout]] — Bounding synchronous HTTP request duration so slow backends do not tie up gateway connections. [[2026-05-15--api-gateway|API Gateway]]
- [[request-id|Request ID]] — A request correlation identifier created or propagated by the gateway for logs, metrics, and traces. [[2026-05-15--api-gateway|API Gateway]]
- [[request-response-transformation|Request/Response Transformation]] — Lightweight contract adaptation at the gateway. [[2026-05-15--api-gateway|API Gateway]]
- [[request-aggregation|Request Aggregation]] — Combining backend calls for a client-facing endpoint while avoiding excessive orchestration in a general gateway. [[2026-05-15--api-gateway|API Gateway]]
- [[backend-for-frontend|Backend For Frontend]] — A client-specific backend layer for web, mobile, or partner API shapes. [[2026-05-15--api-gateway|API Gateway]]
- [[load-balancer|Load Balancer]] — A traffic distributor that is distinct from a gateway's API-contract and policy role. [[2026-05-15--api-gateway|API Gateway]]
- [[api-gateway-observability|API Gateway Observability]] — Metrics and traces used to locate gateway, network, auth, rate-limit, or backend problems. [[2026-05-15--api-gateway|API Gateway]]
- [[api-gateway-boundary|API Gateway Boundary]] — The rule that gateways should enforce entry policies without absorbing core business decisions. [[2026-05-15--api-gateway|API Gateway]]
- [[edge-gateway|Edge Gateway]] — Moving selected auth, redirect, cache, or bot-protection logic to edge infrastructure when latency and global traffic justify it. [[2026-05-15--api-gateway|API Gateway]]
- [[asynchronous-processing|Asynchronous Processing]] — Returning an accepted state for slow work while workers complete it later. [[2026-05-15--api-gateway|API Gateway]]
- [[message-queue|Message Queue]] — A supporting mechanism for background task execution after the gateway accepts a request. [[2026-05-15--api-gateway|API Gateway]]
- [[object-storage|Object Storage]] — The better destination for large file and media uploads than ordinary API server request bodies. [[2026-05-15--api-gateway|API Gateway]]
- [[signed-cdn-access|Signed CDN Access]] — A related signed URL pattern for private file transfer after application authorization. [[2026-05-15--api-gateway|API Gateway]]
- [[idempotency-key|Idempotency Key]] — A domain-service concern for retry-safe operations such as webhooks, bookings, payments, and task execution. [[2026-05-15--api-gateway|API Gateway]]
- [[service-discovery|Service Discovery]] — A related internal mechanism for routing gateway traffic to live backend instances. [[2026-05-15--api-gateway|API Gateway]]

## Follow-ups

- Create a synthesis comparing API Gateway, load balancer, reverse proxy, service mesh ingress, CDN edge worker, and Backend For Frontend as adjacent traffic-entry patterns. [[2026-05-15--api-gateway|API Gateway]]
