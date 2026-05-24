---
type: concept
aliases: ["parallel tool execution", "parallel tool calls"]
tags: [tools, agentic-systems, efficiency]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Parallel Tool Calling

## Definition

Parallel tool calling is the practice of running independent tool calls concurrently when their inputs and outputs do not depend on one another. [[2026-05-24--prompting-best-practices|Prompting best practices]]

## Scope

This concept covers independent searches, file reads, and commands that can safely execute at the same time. It excludes dependent operations where later tool parameters require earlier results, and it should be bounded by system stability and resource constraints. [[2026-05-24--prompting-best-practices|Prompting best practices]]

## Contrasts

- **Sequential execution**: Sequential execution is required when later actions depend on earlier results, while parallel execution reduces latency for independent work.
- **Subagent Orchestration**: Parallel tool calling runs multiple tools, while subagent orchestration delegates work to separate agent contexts.

## Evidence

- [[2026-05-24--prompting-best-practices|Prompting best practices]] — The source recommends parallel calls for independent searches, file reads, and bash commands, while warning against guessing dependent parameters.

## Related

- [[Tool Use]]
- [[Agentic Systems]]
- [[Subagent Orchestration]]

## Open Questions

- What concurrency level is appropriate for local wiki operations without making output noisy or unstable?
