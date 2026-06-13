---
type: concept
aliases: ["load balancer", "LB", "L4 load balancer", "L7 load balancer", "traffic balancer"]
tags: [system-design, networking, reliability, api-gateway]
created: 2026-06-13
updated: 2026-06-13
source_count: 1
---

# Load Balancer

## Definition

A load balancer distributes traffic across multiple healthy instances of a service or gateway so one instance does not receive all traffic. [[2026-05-15--api-gateway|API Gateway]]

## Scope

This concept covers fronting API Gateway instances with a load balancer and using load balancers or service discovery behind the gateway for backend services. [[2026-05-15--api-gateway|API Gateway]] The source distinguishes L4 or L7 traffic distribution and health checks from API Gateway responsibilities such as routing, authentication, rate limiting, transformation, and versioning. [[2026-05-15--api-gateway|API Gateway]]

## Contrasts

- **API Gateway**: Load balancer scope is usually one service's instances, while API Gateway is a multi-service API entry point that understands API contracts and request policies. [[2026-05-15--api-gateway|API Gateway]]
- **Service Discovery**: Load balancing chooses among known endpoints, while service discovery maintains the live endpoint set. [[2026-05-15--zookeeper|Zookeeper]] [[2026-05-15--api-gateway|API Gateway]]

## Evidence

- [[2026-05-15--api-gateway|API Gateway]] — The source gives the common deployment chain `Internet -> Load Balancer -> API Gateway instances -> Backend services` and compares load balancer versus API Gateway responsibilities.

## Related

- [[api-gateway|API Gateway]]
- [[api-routing|API Routing]]
- [[service-discovery|Service Discovery]]
- [[tls-termination|TLS Termination]]
- [[failover|Failover]]

## Open Questions

- Which future source should compare L4 load balancing, L7 load balancing, DNS load balancing, client-side balancing, and service-mesh balancing?
