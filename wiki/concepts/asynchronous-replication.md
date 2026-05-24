---
type: concept
aliases: ["async replication", "eventual replication"]
tags: [system-design, databases, replication, availability]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Asynchronous Replication

## Definition

Asynchronous replication is a replication mode where the leader sends changes to followers but acknowledges the client write without waiting for followers to confirm receipt. [[2026-05-02--replication|Replication]]

## Scope

This concept covers faster writes, higher write availability, replication lag, stale follower reads, and the risk that acknowledged writes can be lost if the leader fails before followers receive them. [[2026-05-02--replication|Replication]] It is common in read-scaling designs because fully synchronous replication across every follower would make writes dependent on every follower's health. [[2026-05-02--replication|Replication]]

## Contrasts

- **Synchronous Replication**: Asynchronous replication favors write latency and availability, while synchronous replication favors stronger freshness and durability guarantees. [[2026-05-02--replication|Replication]]
- **Stale-While-Revalidate**: Both patterns may serve temporarily stale data, but asynchronous replication staleness comes from replica catch-up delay while stale-while-revalidate staleness comes from cache refresh policy. [[2026-05-14--scaling-reads|Scaling Reads]] [[2026-05-02--replication|Replication]]

## Evidence

- [[2026-05-02--replication|Replication]] — The source describes asynchronous replication as practical for read-heavy systems but highlights data-loss and stale-read risks.

## Related

- [[replication|Replication]]
- [[single-leader-replication|Single-Leader Replication]]
- [[synchronous-replication|Synchronous Replication]]
- [[replication-lag|Replication Lag]]
- [[read-after-write-consistency|Read-After-Write Consistency]]

## Open Questions

- Which product scenarios in future sources tolerate asynchronous lag, and which require stricter write acknowledgement?
