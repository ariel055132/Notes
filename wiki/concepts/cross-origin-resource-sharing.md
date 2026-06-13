---
type: concept
aliases: ["CORS", "cross-origin requests", "allowed origins", "allowed headers"]
tags: [system-design, api-gateway, browser, security]
created: 2026-06-13
updated: 2026-06-13
source_count: 1
---

# Cross-Origin Resource Sharing

## Definition

Cross-Origin Resource Sharing is a browser API access policy that controls which origins, methods, and headers a web app may use when calling an API from another origin. [[2026-05-15--api-gateway|API Gateway]]

## Scope

This concept covers gateway-level handling of allowed origins, allowed methods, and allowed headers so every backend service does not duplicate CORS configuration. [[2026-05-15--api-gateway|API Gateway]]

## Contrasts

- **Authentication**: CORS controls browser cross-origin access behavior, while authentication verifies who the caller is. [[2026-05-15--api-gateway|API Gateway]]
- **Public API Contract**: CORS is one policy attached to the public API contract, not the whole contract itself. [[2026-05-15--api-gateway|API Gateway]]

## Evidence

- [[2026-05-15--api-gateway|API Gateway]] — The source lists CORS as a cross-cutting concern and says the gateway can centralize allowed origins, methods, and headers.

## Related

- [[api-gateway|API Gateway]]
- [[public-api-contract|Public API Contract]]
- [[gateway-authentication|Gateway Authentication]]
- [[gateway-authorization|Gateway Authorization]]

## Open Questions

- Which future web-security source should cover preflight caching, credentialed requests, wildcard origins, and CORS misconfiguration risks?
