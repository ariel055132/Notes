---
type: concept
aliases: ["directory sharding", "routing directory", "shard map", "mapping table sharding"]
tags: [system-design, databases, sharding]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Directory-Based Sharding

## Definition

Directory-based sharding uses a mapping table or routing service to record which shard owns a tenant, key, bucket, or special object. [[2026-05-15--sharding|Sharding]]

## Scope

This concept covers explicit routing entries such as a tenant being assigned to one shard or a hot market being moved to a dedicated shard. [[2026-05-15--sharding|Sharding]] It is flexible for enterprise SaaS, multi-tenant systems, and hot-key isolation, but the routing directory becomes a critical dependency and may add an extra lookup before queries. [[2026-05-15--sharding|Sharding]]

## Contrasts

- **Hash-Based Sharding**: Directory-based sharding stores explicit placement, while hash-based sharding computes placement from a shard key. [[2026-05-15--sharding|Sharding]]
- **Virtual Buckets**: Directory-based sharding can map individual tenants or hot objects, while virtual bucket schemes often map logical buckets to shards. [[2026-05-15--sharding|Sharding]]

## Evidence

- [[2026-05-15--sharding|Sharding]] — The source describes directory-based sharding as flexible but operationally heavier because the directory is a key dependency.

## Related

- [[database-sharding|Database Sharding]]
- [[shard-key|Shard Key]]
- [[virtual-buckets|Virtual Buckets]]
- [[hot-key|Hot Key]]
- [[resharding|Resharding]]

## Open Questions

- Which future source should describe high-availability design for shard-map services?
