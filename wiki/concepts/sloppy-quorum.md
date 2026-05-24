---
type: concept
aliases: ["sloppy quorum writes", "temporary quorum"]
tags: [system-design, databases, replication, availability]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Sloppy Quorum

## Definition

Sloppy quorum is a leaderless-replication availability technique where writes are accepted by reachable nodes outside the intended replica set when the intended home replicas are unavailable. [[2026-05-02--replication|Replication]]

## Scope

This concept covers continuing to accept writes during network partitions or node failures by temporarily storing data on substitute nodes. [[2026-05-02--replication|Replication]] It improves write availability but weakens the usual quorum overlap guarantee because later reads from the intended replica set may not include the temporary nodes holding the newest value. [[2026-05-02--replication|Replication]]

## Contrasts

- **Strict Quorum**: Strict quorum refuses writes unless enough intended replicas are reachable, while sloppy quorum accepts writes on other reachable nodes. [[2026-05-02--replication|Replication]]
- **Hinted Handoff**: Sloppy quorum is the temporary acceptance of writes, while hinted handoff is the later transfer of those writes back to home replicas. [[2026-05-02--replication|Replication]]

## Evidence

- [[2026-05-02--replication|Replication]] — The source describes sloppy quorum as an AP-style choice that keeps writes available but can return stale reads even when `w + r > n` appears satisfied.

## Related

- [[leaderless-replication|Leaderless Replication]]
- [[quorum-reads-and-writes|Quorum Reads and Writes]]
- [[hinted-handoff|Hinted Handoff]]
- [[replication-lag|Replication Lag]]

## Open Questions

- Which workloads in future sources justify sloppy quorum instead of rejecting writes during partition?
