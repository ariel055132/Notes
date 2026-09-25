---
type: concept
aliases: ["SSL termination", "TLS offload", "certificate termination", "HTTPS termination"]
tags: [system-design, api-gateway, security, networking]
created: 2026-06-13
updated: 2026-09-25
source_count: 2
---

# TLS Termination

## Definition

TLS termination is the point where encrypted client HTTPS traffic is decrypted and public certificate handling is centralized, commonly at an API Gateway, edge proxy, or load balancer. [[2026-05-15--api-gateway|API Gateway]]

## Scope

This concept covers centralizing public certificate management so backend services do not each manage public certificates. [[2026-05-15--api-gateway|API Gateway]] The source notes that whether internal gateway-to-service traffic remains encrypted depends on security requirements, and that financial, medical, or enterprise customer data may still require mTLS between gateway and service. [[2026-05-15--api-gateway|API Gateway]]

## Contrasts

- **Gateway Authentication**: TLS termination protects transport and certificate handling, while gateway authentication validates caller identity such as JWT or API key. [[2026-05-15--api-gateway|API Gateway]]
- **mTLS**: Public TLS termination handles external HTTPS, while mTLS can protect internal service-to-service traffic when sensitive data or zero-trust requirements demand it. [[2026-05-15--api-gateway|API Gateway]]

## Evidence

- [[2026-05-15--api-gateway|API Gateway]] — The source describes gateway-level TLS handling and the option of mTLS from gateway to backend services.

- [[2026-09-25--personal-information-feed-architecture|FreshRSS × NetNewsWire 架構筆記]] — 第 2、3 節以 Caddy 集中處理 HTTPS 與憑證，再轉交 Docker 內部的 FreshRSS；此為對話整理的架構範例，非服務實測證明。

## Related

- [[api-gateway|API Gateway]]
- [[gateway-authentication|Gateway Authentication]]
- [[load-balancer|Load Balancer]]
- [[edge-gateway|Edge Gateway]]

## Open Questions

- Which future networking source should compare TLS termination at CDN, load balancer, ingress controller, API Gateway, and service mesh sidecar?
