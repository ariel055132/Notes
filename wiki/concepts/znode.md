---
type: concept
aliases: ["ZNode", "znode", "ZooKeeper node"]
tags: [system-design, distributed-systems, coordination, zookeeper]
created: 2026-05-26
updated: 2026-05-26
source_count: 1
---

# ZNode

## Definition

A znode is a path-addressed node in ZooKeeper's tree-shaped data model that stores a small piece of coordination metadata. [[2026-05-15--zookeeper|Zookeeper]]

## Scope

This concept covers persistent znodes for configuration or metadata, ephemeral znodes for liveness and ownership, and sequential znodes for ordered candidates in leader election or fair locks. [[2026-05-15--zookeeper|Zookeeper]] Znode values should remain small, such as host, port, version, owner ID, capacity, or lease token, and should not contain large records, event streams, or arbitrary query data. [[2026-05-15--zookeeper|Zookeeper]]

## Contrasts

- **Database Row**: A database row can store business records and support rich queries, while a znode stores small path-addressed coordination metadata. [[2026-05-15--zookeeper|Zookeeper]]
- **Ephemeral ZNode**: A regular persistent znode remains until explicit deletion, while an ephemeral znode disappears when the client session expires. [[2026-05-15--zookeeper|Zookeeper]]
- **Sequential ZNode**: A znode is the base data model; a sequential znode adds a monotonic suffix for ordering candidates. [[2026-05-15--zookeeper|Zookeeper]]

## Evidence

- [[2026-05-15--zookeeper|Zookeeper]] — The source describes ZooKeeper as a small file-system-like tree where each path node stores coordination metadata.

## Related

- [[zookeeper|ZooKeeper]]
- [[coordination-metadata|Coordination Metadata]]
- [[ephemeral-znode|Ephemeral ZNode]]
- [[sequential-znode|Sequential ZNode]]
- [[zookeeper-watch|ZooKeeper Watch]]

## Open Questions

- Which future source should cover ZooKeeper znode version numbers, ACLs, and multi-operation transactions?
