---
type: concept
aliases: ["read repair", "replica read repair"]
tags: [system-design, databases, replication]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Read Repair

## Definition

Read repair is a leaderless-replication technique where a client or coordinator reads from multiple replicas, detects a stale version, and writes the newer value back to stale replicas. [[2026-05-02--replication|Replication]]

## Scope

This concept covers repairing stale replicas as a side effect of read traffic and works best for data that is read frequently enough for stale copies to be discovered. [[2026-05-02--replication|Replication]] It does not guarantee quick repair for rarely read data, which may require background anti-entropy instead. [[2026-05-02--replication|Replication]]

## Contrasts

- **Anti-Entropy Process**: Read repair repairs data encountered during reads, while anti-entropy scans in the background to find and copy missing data. [[2026-05-02--replication|Replication]]
- **Replication Log Catch-Up**: Read repair compares replica values during reads, while leader-based log catch-up replays ordered changes from a leader. [[2026-05-02--replication|Replication]]

## Evidence

- [[2026-05-02--replication|Replication]] — The source presents read repair as a way for stale leaderless replicas to catch up when clients read from multiple replicas and detect older versions.

## Related

- [[leaderless-replication|Leaderless Replication]]
- [[anti-entropy-process|Anti-Entropy Process]]
- [[quorum-reads-and-writes|Quorum Reads and Writes]]
- [[version-vector|Version Vector]]

## Open Questions

- Which future source should define how read repair interacts with tombstones and deletes?
