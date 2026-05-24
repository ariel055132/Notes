---
type: concept
aliases: ["subagents", "agent delegation"]
tags: [agentic-systems, delegation, tools]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Subagent Orchestration

## Definition

Subagent orchestration is the practice of delegating independent workstreams to separate agent contexts when parallelism, isolation, or specialized focus is useful. [[2026-05-24--prompting-best-practices|Prompting best practices]]

## Scope

This concept covers spawning subagents for fan-out research, independent file review, or isolated workstreams. It does not fit simple sequential tasks, single-file edits, or cases where shared context is essential. [[2026-05-24--prompting-best-practices|Prompting best practices]]

## Contrasts

- **Parallel Tool Calling**: Parallel tool calling invokes multiple tools directly, while subagent orchestration delegates reasoning and tool use to separate agent contexts.
- **Direct execution**: Direct execution is simpler when one agent can see the relevant context and complete the task without fan-out.

## Evidence

- [[2026-05-24--prompting-best-practices|Prompting best practices]] — The source recommends explicit guidance for when subagents are desirable and cautions against overuse on simple tasks.

## Related

- [[Agentic Systems]]
- [[Tool Use]]
- [[Parallel Tool Calling]]
- [[Claude Opus 4.7]]

## Open Questions

- Which wiki lint checks are independent enough to benefit from subagent fan-out?
