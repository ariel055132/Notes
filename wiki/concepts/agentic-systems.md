---
type: concept
aliases: ["agentic workflows", "agent systems", "long-horizon agents"]
tags: [agentic-systems, tools, state-management]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Agentic Systems

## Definition

Agentic systems are workflows where a model pursues a task across multiple steps using tools, state tracking, verification, progress updates, and autonomy. [[2026-05-24--prompting-best-practices|Prompting best practices]]

## Scope

This concept covers long-horizon reasoning, tool use, context-window management, state files, tests or verification tools, subagents, safety checks, and incremental progress. It does not mean unrestricted autonomy; the source explicitly recommends considering reversibility and impact before risky actions. [[2026-05-24--prompting-best-practices|Prompting best practices]]

## Contrasts

- **Single-turn chat**: Single-turn chat optimizes for a direct answer, while agentic systems maintain orientation and take actions over time.
- **Prompt chaining**: Prompt chaining is a controlled multi-call pipeline; agentic systems may decide intermediate steps dynamically.

## Evidence

- [[2026-05-24--prompting-best-practices|Prompting best practices]] — The guide emphasizes incremental progress, state management, context-window awareness, verification tools, and safety boundaries for long-running work.

## Related

- [[tool-use|Tool Use]]
- [[parallel-tool-calling|Parallel Tool Calling]]
- [[subagent-orchestration|Subagent Orchestration]]
- [[adaptive-thinking|Adaptive Thinking]]
- [[long-context-prompting|Long Context Prompting]]

## Open Questions

- Which agentic safeguards should be encoded into this wiki's project instructions beyond the existing raw-source immutability rule?
