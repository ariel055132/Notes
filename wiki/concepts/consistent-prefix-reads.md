---
type: concept
aliases: ["consistent prefix", "causal read ordering", "causal-order reads"]
tags: [system-design, consistency, replication]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Consistent Prefix Reads

## Definition

Consistent prefix reads are a consistency guarantee that causally related writes are observed in causal order, so a system does not show an effect before its cause. [[2026-05-02--replication|Replication]]

## Scope

This concept covers preserving causality across replicated reads, especially when related writes can be replicated through different partitions or replicas at different speeds. [[2026-05-02--replication|Replication]] Mitigations include storing causally related writes in the same partition or tracking causal dependencies with metadata such as version vectors. [[2026-05-02--replication|Replication]]

## Contrasts

- **Monotonic Reads**: Monotonic reads preserve a single user's non-regressing view, while consistent prefix reads preserve causal order among related writes. [[2026-05-02--replication|Replication]]
- **Eventual Consistency**: Eventual consistency says replicas converge if writes stop, while consistent prefix reads constrain which intermediate states can be shown before convergence. [[2026-05-02--replication|Replication]]

## Evidence

- [[2026-05-02--replication|Replication]] — The source uses a question-and-answer example where a third observer should not see an answer before seeing the question that caused it.

## Related

- [[replication-lag|Replication Lag]]
- [[version-vector|Version Vector]]
- [[monotonic-reads|Monotonic Reads]]
- [[read-after-write-consistency|Read-After-Write Consistency]]

## Open Questions

- Which future source should define causal consistency and causal metadata more formally?
