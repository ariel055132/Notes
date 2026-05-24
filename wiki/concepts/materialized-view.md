---
type: concept
aliases: ["materialized views", "summary table", "precomputed read model"]
tags: [system-design, databases, precomputation]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Materialized View

## Definition

A materialized view is a precomputed read model that stores the result of an expensive query or aggregation so reads do not recompute it every time. [[2026-05-14--scaling-reads|Scaling Reads]]

## Scope

This concept covers database-native materialized views and application-maintained summary tables updated by background jobs, queue consumers, or CDC pipelines. [[2026-05-14--scaling-reads|Scaling Reads]] It is especially relevant for expensive aggregates such as average ratings, view counts, ranking summaries, or other read-heavy computed results. [[2026-05-14--scaling-reads|Scaling Reads]]

## Contrasts

- **Denormalization**: Denormalization often stores duplicated entity fields for faster joins, while materialized views emphasize precomputed results and aggregates. [[2026-05-14--scaling-reads|Scaling Reads]]
- **Application-Level Caching**: A materialized view is a persistent read model, while application-level cache is usually a transient layer in front of the database or read model. [[2026-05-14--scaling-reads|Scaling Reads]]

## Evidence

- [[2026-05-14--scaling-reads|Scaling Reads]] — The source describes precomputing home ratings into a materialized view or summary table instead of recalculating averages on each page load.

## Related

- [[read-scaling|Read Scaling]]
- [[denormalization|Denormalization]]
- [[freshness-budget|Freshness Budget]]
- [[application-level-caching|Application-Level Caching]]

## Open Questions

- When should the wiki prefer the term summary table over materialized view for application-maintained projections?
