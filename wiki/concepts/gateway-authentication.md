---
type: concept
aliases: ["gateway authn", "API authentication", "JWT validation", "API key validation"]
tags: [system-design, api-gateway, security, authentication]
created: 2026-06-13
updated: 2026-06-13
source_count: 1
---

# Gateway Authentication

## Definition

Gateway authentication is the API Gateway responsibility of verifying who a request comes from before forwarding it to backend services. [[2026-05-15--api-gateway|API Gateway]]

## Scope

This concept covers validating JWT signature and expiry, checking API keys, extracting claims such as user ID, tenant ID, and roles, and injecting internal headers such as `X-User-Id`, `X-Tenant-Id`, and `X-Request-Id`. [[2026-05-15--api-gateway|API Gateway]] Backends may trust gateway-injected headers only if they are not directly reachable from outside and internal traffic is protected by private networking, mTLS, service mesh, or internal auth. [[2026-05-15--api-gateway|API Gateway]]

## Contrasts

- **Gateway Authorization**: Authentication answers who made the request, while authorization decides what that identity may do. [[2026-05-15--api-gateway|API Gateway]]
- **Domain Authorization**: Gateway authentication can pass identity context downstream, but backend services must still make data-level permission decisions when domain state is required. [[2026-05-15--api-gateway|API Gateway]]

## Evidence

- [[2026-05-15--api-gateway|API Gateway]] — The source gives a flow where the gateway validates JWTs, parses claims, injects identity headers, and forwards to backend services.

## Related

- [[api-gateway|API Gateway]]
- [[gateway-authorization|Gateway Authorization]]
- [[request-id|Request ID]]
- [[tls-termination|TLS Termination]]
- [[api-gateway-boundary|API Gateway Boundary]]

## Open Questions

- Which future security source should cover token introspection, session cookies, OAuth scopes, mTLS identity, and internal header spoofing defenses?
