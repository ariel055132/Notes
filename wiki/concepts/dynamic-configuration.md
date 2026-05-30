---
type: concept
aliases: ["dynamic config", "runtime configuration", "configuration management", "config version"]
tags: [system-design, distributed-systems, coordination, configuration]
created: 2026-05-26
updated: 2026-05-26
source_count: 1
---

# Dynamic Configuration

## Definition

Dynamic configuration is runtime configuration that services can read and update consistently while receiving notifications when important configuration values change. [[2026-05-15--zookeeper|Zookeeper]]

## Scope

This concept covers small, important runtime values such as scheduler bucket size, max enqueue rate, dispatcher capacity, feature toggles for infrastructure consumers, and gateway ownership mappings. [[2026-05-15--zookeeper|Zookeeper]] It does not replace static deployment-time config, environment variables, config files, Kubernetes ConfigMaps, cloud parameter stores, or general application settings when those simpler tools fit. [[2026-05-15--zookeeper|Zookeeper]]

## Contrasts

- **Static Configuration**: Static configuration changes with deploys or platform configuration, while dynamic configuration can be coordinated and watched at runtime. [[2026-05-15--zookeeper|Zookeeper]]
- **Business Data**: Business data records product state, while dynamic configuration controls operational behavior. [[2026-05-15--zookeeper|Zookeeper]]
- **ZooKeeper Watch**: Dynamic configuration is the data being coordinated; a ZooKeeper watch is one mechanism for notifying services about changes. [[2026-05-15--zookeeper|Zookeeper]]

## Evidence

- [[2026-05-15--zookeeper|Zookeeper]] — The source uses ChatGPT Tasks bucket size, retry limits, and Robotaxi dispatcher capacity as examples of small runtime configuration suited to ZooKeeper-style coordination.

## Related

- [[zookeeper|ZooKeeper]]
- [[coordination-metadata|Coordination Metadata]]
- [[znode|ZNode]]
- [[zookeeper-watch|ZooKeeper Watch]]
- [[service-discovery|Service Discovery]]

## Open Questions

- Which future source should compare dynamic configuration, feature flags, parameter stores, and control-plane config rollouts?
