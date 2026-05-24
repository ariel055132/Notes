---
type: concept
aliases: ["hinted handoff", "handoff hints", "temporary replica handoff"]
tags: [system-design, databases, replication, availability]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Hinted Handoff

## Definition

Hinted handoff is the process of transferring writes that were temporarily accepted by non-home nodes back to their intended home replicas after those replicas become reachable again. [[2026-05-02--replication|Replication]]

## Scope

This concept covers repair after sloppy quorum writes, where reachable substitute nodes hold hints indicating which unavailable home replicas should eventually receive the data. [[2026-05-02--replication|Replication]] It helps restore the intended replica placement after a partition, but it does not make stale reads impossible during the interval when new values are still held outside the home replica set. [[2026-05-02--replication|Replication]]

## Contrasts

- **Sloppy Quorum**: Sloppy quorum accepts writes on substitute nodes, while hinted handoff moves those writes back home later. [[2026-05-02--replication|Replication]]
- **Anti-Entropy Process**: Hinted handoff targets known temporary writes, while anti-entropy scans for replica differences more generally. [[2026-05-02--replication|Replication]]

## Evidence

- [[2026-05-02--replication|Replication]] — The source describes hinted handoff as sending temporarily held writes back to home nodes after network recovery.

## Related

- [[sloppy-quorum|Sloppy Quorum]]
- [[leaderless-replication|Leaderless Replication]]
- [[quorum-reads-and-writes|Quorum Reads and Writes]]
- [[anti-entropy-process|Anti-Entropy Process]]

## Open Questions

- Which future source should cover hinted handoff failure cases and retention windows?
