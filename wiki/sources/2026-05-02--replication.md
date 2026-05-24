---
type: source
source_path: raw/archive/Replication.pdf
title: "Replication"
author: "BuildMoat"
date: 2026-05-02
tags: [system-design, databases, replication, distributed-systems]
created: 2026-05-24
---

# Replication

## Summary

This source explains replication as keeping copies of the same data on multiple networked machines to reduce latency, improve availability, and scale read throughput. [[2026-05-02--replication|Replication]] It compares three major architectures: single-leader replication, multi-leader replication, and leaderless replication. [[2026-05-02--replication|Replication]] The practical emphasis is on system-design tradeoffs: synchronous versus asynchronous replication, failover, replication lag, read-after-write consistency, monotonic reads, consistent prefix reads, write conflicts, quorum reads and writes, sloppy quorum, hinted handoff, and version vectors. [[2026-05-02--replication|Replication]] The source frames replication as an interview topic where the strongest answers connect architecture choices to product requirements rather than naming a pattern in isolation. [[2026-05-02--replication|Replication]]

## Key Claims

1. Replication is useful because copies can be placed near users, survive node failures, and spread read traffic across machines. [[2026-05-02--replication|Replication]]
2. Single-leader replication is simple and avoids write conflicts because all writes pass through one leader, but that leader becomes a write bottleneck and a failover risk. [[2026-05-02--replication|Replication]]
3. Synchronous replication improves durability and freshness guarantees, while asynchronous replication improves write latency and availability at the cost of possible data loss and stale reads. [[2026-05-02--replication|Replication]]
4. Replication lag creates user-visible consistency problems such as read-after-write inconsistency, non-monotonic reads, and causally inverted reads. [[2026-05-02--replication|Replication]]
5. Multi-leader replication is most compelling across datacenters, offline clients, and collaborative editing, but it shifts the hard problem to conflict resolution. [[2026-05-02--replication|Replication]]
6. Leaderless replication improves write availability by letting any replica accept writes, but applications must reason about quorums, stale replicas, concurrent writes, and weaker consistency guarantees. [[2026-05-02--replication|Replication]]
7. Quorum rules such as `w + r > n` can make stale reads less likely, but they do not by themselves provide read-your-writes, monotonic reads, or causal ordering under all failure modes. [[2026-05-02--replication|Replication]]
8. In system-design interviews, replication choices should be justified with requirements such as read volume, write availability, geographic latency, financial correctness, and tolerance for stale data. [[2026-05-02--replication|Replication]]

## Notable Quotes

- "Replication Lag is the core problem you must understand deeply." [[2026-05-02--replication|Replication]]
- "There is no best architecture." [[2026-05-02--replication|Replication]]
- "Always discuss tradeoffs." [[2026-05-02--replication|Replication]]

## Entities Mentioned

- None. BuildMoat is treated as the source author/publisher in frontmatter rather than as a dedicated entity page. [[2026-05-02--replication|Replication]]

## Concepts Mentioned

- [[replication|Replication]] — Maintaining copies of the same data across machines for latency, availability, and throughput. [[2026-05-02--replication|Replication]]
- [[single-leader-replication|Single-Leader Replication]] — A replication architecture where one primary accepts writes and followers copy its log. [[2026-05-02--replication|Replication]]
- [[read-replica|Read Replica]] — A follower that can serve read traffic while writes continue through the leader. [[2026-05-02--replication|Replication]]
- [[synchronous-replication|Synchronous Replication]] — A write is acknowledged only after at least one follower confirms the replicated change. [[2026-05-02--replication|Replication]]
- [[asynchronous-replication|Asynchronous Replication]] — A leader acknowledges writes without waiting for follower confirmation. [[2026-05-02--replication|Replication]]
- [[replication-log|Replication Log]] — The ordered record of changes used to bring replicas into the same state. [[2026-05-02--replication|Replication]]
- [[failover|Failover]] — Promoting a replica when the leader fails and redirecting clients to the new leader. [[2026-05-02--replication|Replication]]
- [[split-brain|Split Brain]] — A failure mode where more than one node believes it is the leader and accepts writes. [[2026-05-02--replication|Replication]]
- [[replication-lag|Replication Lag]] — The delay between a leader accepting a write and followers applying it. [[2026-05-02--replication|Replication]]
- [[read-after-write-consistency|Read-After-Write Consistency]] — A user can read their own completed writes. [[2026-05-02--replication|Replication]]
- [[monotonic-reads|Monotonic Reads]] — A user should not see data move backward in time across repeated reads. [[2026-05-02--replication|Replication]]
- [[consistent-prefix-reads|Consistent Prefix Reads]] — Causally related writes should be observed in causal order. [[2026-05-02--replication|Replication]]
- [[multi-leader-replication|Multi-Leader Replication]] — Multiple leaders accept writes and replicate changes to one another. [[2026-05-02--replication|Replication]]
- [[write-conflict-resolution|Write Conflict Resolution]] — Techniques for handling concurrent writes that update the same data. [[2026-05-02--replication|Replication]]
- [[last-write-wins|Last Write Wins]] — A conflict rule that keeps the write with the greatest timestamp and discards other concurrent writes. [[2026-05-02--replication|Replication]]
- [[conflict-free-replicated-data-types|Conflict-Free Replicated Data Types]] — Mergeable data structures for concurrent replicated updates. [[2026-05-02--replication|Replication]]
- [[operational-transformation|Operational Transformation]] — A collaborative-editing algorithm family for transforming concurrent text operations. [[2026-05-02--replication|Replication]]
- [[leaderless-replication|Leaderless Replication]] — A replication architecture where clients can read from and write to multiple replicas directly. [[2026-05-02--replication|Replication]]
- [[read-repair|Read Repair]] — Repairing stale replicas when reads reveal older versions. [[2026-05-02--replication|Replication]]
- [[anti-entropy-process|Anti-Entropy Process]] — A background process that reconciles data differences between replicas. [[2026-05-02--replication|Replication]]
- [[quorum-reads-and-writes|Quorum Reads and Writes]] — Read/write thresholds chosen so read and write replica sets overlap. [[2026-05-02--replication|Replication]]
- [[sloppy-quorum|Sloppy Quorum]] — Temporarily accepting writes on reachable nodes outside the preferred replica set. [[2026-05-02--replication|Replication]]
- [[hinted-handoff|Hinted Handoff]] — Moving temporarily accepted writes back to their intended home replicas after recovery. [[2026-05-02--replication|Replication]]
- [[version-vector|Version Vector]] — Per-replica version metadata used to detect causal ordering and concurrent writes. [[2026-05-02--replication|Replication]]

## Follow-ups

- Build a system-design synthesis comparing replication, read scaling, caching, and sharding as separate but interacting scale patterns.
- Add a future source on consensus and distributed transactions to contrast replication-for-availability with replication-for-strong-consistency.
