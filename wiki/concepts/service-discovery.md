---
type: concept
aliases: ["service discovery", "service registry", "membership registry", "instance registry"]
tags: [system-design, distributed-systems, coordination, discovery]
created: 2026-05-26
updated: 2026-05-26
source_count: 1
---

# Service Discovery

## Definition

Service discovery is the mechanism by which service instances register their network location and liveness so other components can find active instances and update routing when membership changes. [[2026-05-15--zookeeper|Zookeeper]]

## Scope

This concept covers ZooKeeper-style service registration through ephemeral znodes, dispatcher membership, worker membership, broker membership, sequencer ownership, and connection-server ownership. [[2026-05-15--zookeeper|Zookeeper]] It also covers the practical caveat that modern platforms often provide service discovery through Kubernetes Services, Consul, Cloud Map, service mesh, managed Kafka, or other platform-native control planes. [[2026-05-15--zookeeper|Zookeeper]]

## Contrasts

- **Load Balancing**: Load balancing chooses among known healthy endpoints, while service discovery maintains the set of endpoints and their membership state. [[2026-05-15--zookeeper|Zookeeper]]
- **Ephemeral ZNode**: Ephemeral znodes are one ZooKeeper implementation primitive for service discovery membership. [[2026-05-15--zookeeper|Zookeeper]]
- **Consistent Hashing**: Consistent hashing maps keys to owners, while service discovery tells clients which owners or service instances currently exist. [[2026-05-15--consistent-hashing|Consistent Hashing]] [[2026-05-15--zookeeper|Zookeeper]]

## Evidence

- [[2026-05-15--zookeeper|Zookeeper]] — The source gives dispatcher, sequencer, worker, and broker registration examples and notes that modern platforms often replace ZooKeeper for service discovery.

## Related

- [[zookeeper|ZooKeeper]]
- [[ephemeral-znode|Ephemeral ZNode]]
- [[zookeeper-session|ZooKeeper Session]]
- [[zookeeper-watch|ZooKeeper Watch]]
- [[leader-election|Leader Election]]
- [[consistent-hashing|Consistent Hashing]]

## Open Questions

- Which future source should compare DNS, client-side discovery, service mesh, Consul, Kubernetes Services, and ZooKeeper discovery?
