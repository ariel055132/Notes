---
type: concept
aliases: ["read your writes", "read-your-writes consistency", "read-after-write"]
tags: [system-design, consistency, replication]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Read-After-Write Consistency

## Definition

Read-after-write consistency is the guarantee that after a user completes a write, subsequent reads by that user can observe that write. [[2026-05-02--replication|Replication]]

## Scope

This concept covers routing reads for user-modified data to the leader, tracking a user's last write time or log position, requiring replicas to be caught up before serving the read, and temporarily reading from primary after recent writes. [[2026-05-02--replication|Replication]] It is especially important for user-facing workflows such as posting content or updating a profile because stale reads can make a successful write appear lost. [[2026-05-02--replication|Replication]]

## Contrasts

- **Monotonic Reads**: Read-after-write consistency is about seeing one's own writes, while monotonic reads are about not seeing older snapshots after newer ones. [[2026-05-02--replication|Replication]]
- **Consistent Prefix Reads**: Read-after-write consistency is user/session centered, while consistent prefix reads preserve causal order across related writes. [[2026-05-02--replication|Replication]]

## Evidence

- [[2026-05-02--replication|Replication]] — The source gives the example of a user publishing a post and then failing to see it because the read was routed to a lagging follower.

## Related

- [[replication-lag|Replication Lag]]
- [[read-replica|Read Replica]]
- [[replication-log|Replication Log]]
- [[monotonic-reads|Monotonic Reads]]
- [[consistent-prefix-reads|Consistent Prefix Reads]]

## Open Questions

- Which application patterns should standardize log-position tracking across devices and datacenters?
