---
type: concept
aliases: ["BASE", "Basically Available Soft state Eventual consistency", "BASE model"]
tags: [system-design, databases, consistency, nosql]
created: 2026-05-26
updated: 2026-05-26
source_count: 1
---

# BASE Consistency Model

## Definition

BASE is a consistency model shorthand for Basically Available, Soft state, and Eventual consistency, commonly used to describe systems that relax always-strong consistency to improve availability or horizontal scalability. [[2026-04-15--database|Database]]

## Scope

This concept covers NoSQL-style designs where some nodes may serve requests independently and data is allowed to converge later rather than requiring every read to observe a single immediately consistent state. [[2026-04-15--database|Database]] The source presents BASE as a common NoSQL tradeoff against ACID-style relational guarantees, especially when horizontal scaling is more important than immediate global consistency. [[2026-04-15--database|Database]]

## Contrasts

- **ACID Transactions**: ACID emphasizes atomicity, consistency, isolation, and durability for transaction correctness, while BASE relaxes immediate consistency in favor of availability and eventual convergence. [[2026-04-15--database|Database]] [[acid-transactions|ACID Transactions]]
- **Eventual Consistency**: Eventual consistency is one part of BASE; BASE also includes availability and soft-state assumptions. [[2026-04-15--database|Database]]
- **NoSQL Database**: NoSQL is a database-family label, while BASE is one consistency framing often associated with horizontally scalable NoSQL systems. [[2026-04-15--database|Database]]

## Evidence

- [[2026-04-15--database|Database]] — The source explains BASE as the reason some NoSQL systems can scale horizontally more easily after relaxing strict consistency requirements.

## Related

- [[nosql-database|NoSQL Database]]
- [[acid-transactions|ACID Transactions]]
- [[database-transactions|Database Transactions]]
- [[replication|Replication]]
- [[leaderless-replication|Leaderless Replication]]
- [[quorum-reads-and-writes|Quorum Reads and Writes]]
- [[read-after-write-consistency|Read-After-Write Consistency]]

## Open Questions

- Which future source should define eventual consistency as a dedicated concept and connect it to replication, queues, and caches?
