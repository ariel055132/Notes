---
type: concept
aliases: ["version vectors", "vector clock", "vector clocks", "causal version vector"]
tags: [system-design, distributed-systems, replication, consistency]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Version Vector

## Definition

A version vector is per-replica version metadata used to track causal relationships among writes and detect when versions are concurrent rather than one superseding the other. [[2026-05-02--replication|Replication]]

## Scope

This concept covers leaderless and multi-leader systems where multiple replicas can accept writes to the same key. [[2026-05-02--replication|Replication]] A server returns version metadata with reads, clients include that metadata with later writes, and replicas can use it to overwrite causally older values while preserving concurrent values that require merge. [[2026-05-02--replication|Replication]]

## Contrasts

- **Last Write Wins**: Version vectors preserve information about concurrency, while last-write-wins collapses concurrent versions to one timestamp winner. [[2026-05-02--replication|Replication]]
- **Single Version Number**: A single version number can track one ordered stream, while multiple writers require per-replica components to distinguish causality from concurrency. [[2026-05-02--replication|Replication]]

## Evidence

- [[2026-05-02--replication|Replication]] — The source presents version vectors as the mechanism needed when multiple replicas each maintain their own version number for a key and clients must carry version metadata through reads and writes.

## Related

- [[leaderless-replication|Leaderless Replication]]
- [[multi-leader-replication|Multi-Leader Replication]]
- [[write-conflict-resolution|Write Conflict Resolution]]
- [[consistent-prefix-reads|Consistent Prefix Reads]]
- [[last-write-wins|Last Write Wins]]

## Open Questions

- Which future source should distinguish vector clocks, version vectors, dotted version vectors, and causal contexts?
