---
type: concept
aliases: ["monotonic read consistency", "monotonic reads consistency"]
tags: [system-design, consistency, replication]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Monotonic Reads

## Definition

Monotonic reads are a consistency guarantee that once a user observes a version of data, later reads by that user should not return an older version. [[2026-05-02--replication|Replication]]

## Scope

This concept covers avoiding user-visible time travel when a load balancer routes repeated reads to replicas with different lag. [[2026-05-02--replication|Replication]] A common mitigation is routing a given user's reads consistently to the same replica, such as by hashing user ID, while allowing different users to read from different replicas. [[2026-05-02--replication|Replication]]

## Contrasts

- **Read-After-Write Consistency**: Read-after-write consistency ensures a user's own write becomes visible to that user, while monotonic reads ensure later reads do not regress from an already observed version. [[2026-05-02--replication|Replication]]
- **Strong Consistency**: Monotonic reads are weaker than full strong consistency because they constrain a user's observed sequence rather than requiring all users to see the latest global value immediately. [[2026-05-02--replication|Replication]]

## Evidence

- [[2026-05-02--replication|Replication]] — The source describes a user seeing a friend's comment, refreshing, and then losing the comment after being routed to a more lagged follower.

## Related

- [[replication-lag|Replication Lag]]
- [[read-after-write-consistency|Read-After-Write Consistency]]
- [[consistent-prefix-reads|Consistent Prefix Reads]]
- [[read-replica|Read Replica]]

## Open Questions

- How should monotonic-read routing interact with replica failure and cross-datacenter routing?
