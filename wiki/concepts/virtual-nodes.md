---
type: concept
aliases: ["virtual node", "vNode", "vNodes", "virtual nodes in consistent hashing"]
tags: [system-design, load-distribution, sharding, caching]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Virtual Nodes

## Definition

Virtual nodes are multiple logical positions assigned to one physical node on a consistent-hash ring, so each physical node can own many smaller key ranges. [[2026-05-15--consistent-hashing|Consistent Hashing]]

## Scope

This concept covers a practical improvement to basic consistent hashing: rather than placing each physical machine once on the ring, the system places names such as `cache-a-0`, `cache-a-1`, and `cache-a-2`, then maps those virtual positions back to the physical machine. [[2026-05-15--consistent-hashing|Consistent Hashing]] Virtual nodes improve distribution, make node addition and removal affect smaller ranges, and let higher-capacity machines own more ranges by assigning them more virtual nodes. [[2026-05-15--consistent-hashing|Consistent Hashing]]

## Contrasts

- **Single Ring Position**: One position per physical node can create large uneven ranges, while virtual nodes spread each physical node across the ring. [[2026-05-15--consistent-hashing|Consistent Hashing]]
- **Virtual Buckets**: Virtual nodes are ring positions that map back to physical nodes, while virtual buckets are stable logical buckets that are assigned to physical shards through a mapping layer. [[2026-05-15--consistent-hashing|Consistent Hashing]] [[2026-05-15--sharding|Sharding]]

## Evidence

- [[2026-05-15--consistent-hashing|Consistent Hashing]] — The source identifies more even distribution, finer movement during membership changes, and capacity weighting as the main benefits of virtual nodes.

## Related

- [[consistent-hashing|Consistent Hashing]]
- [[virtual-buckets|Virtual Buckets]]
- [[hash-based-sharding|Hash-Based Sharding]]
- [[resharding|Resharding]]
- [[hot-key|Hot Key]]

## Open Questions

- Which future source should describe how many virtual nodes to use and how to rebalance them safely?
