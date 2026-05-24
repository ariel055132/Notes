---
type: concept
aliases: ["anti-entropy", "replica anti-entropy", "background replica repair"]
tags: [system-design, databases, replication]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Anti-Entropy Process

## Definition

An anti-entropy process is a background reconciliation process that scans replicas for differences and copies missing or newer data so replicas can converge. [[2026-05-02--replication|Replication]]

## Scope

This concept covers background repair in leaderless systems where replicas may miss writes during failures or network partitions. [[2026-05-02--replication|Replication]] Unlike ordered leader-based replication logs, anti-entropy may not guarantee a specific replication order and may have noticeable delay before all differences are repaired. [[2026-05-02--replication|Replication]]

## Contrasts

- **Read Repair**: Anti-entropy repairs data proactively in the background, while read repair repairs stale values discovered by client reads. [[2026-05-02--replication|Replication]]
- **Replication Log**: Anti-entropy reconciles replica state differences, while a replication log streams ordered changes from a leader. [[2026-05-02--replication|Replication]]

## Evidence

- [[2026-05-02--replication|Replication]] — The source describes anti-entropy as a background process that compares replicas and copies missing data, with weaker ordering and delay characteristics than leader-based log replication.

## Related

- [[leaderless-replication|Leaderless Replication]]
- [[read-repair|Read Repair]]
- [[quorum-reads-and-writes|Quorum Reads and Writes]]
- [[replication-log|Replication Log]]

## Open Questions

- Which future source should add Merkle-tree-style anti-entropy implementation details?
