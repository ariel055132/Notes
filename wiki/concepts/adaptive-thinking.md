---
type: concept
aliases: ["thinking mode", "dynamic thinking"]
tags: [claude, reasoning, agentic-systems]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Adaptive Thinking

## Definition

Adaptive thinking is a Claude reasoning mode where the model dynamically decides whether and how much to reason based on task complexity and configured effort. [[2026-05-24--prompting-best-practices|Prompting best practices]]

## Scope

This concept covers multi-step tool use, coding tasks, long-horizon agent loops, and reflection after tool results. It does not require the model to reveal private reasoning, and it should be calibrated when latency or token cost matters. [[2026-05-24--prompting-best-practices|Prompting best practices]]

## Contrasts

- **Extended thinking with fixed budgets**: Adaptive thinking is dynamic, while older extended thinking configurations used explicit budget tokens.
- **Manual chain-of-thought prompting**: Adaptive thinking is a model capability, while manual reasoning instructions are prompt-level guidance.

## Evidence

- [[2026-05-24--prompting-best-practices|Prompting best practices]] — The guide recommends adaptive thinking for agentic behavior, multi-step tool use, complex coding tasks, and long-horizon loops.

## Related

- [[effort-parameter|Effort Parameter]]
- [[tool-use|Tool Use]]
- [[agentic-systems|Agentic Systems]]
- [[claude-sonnet-4-6|Claude Sonnet 4.6]]
- [[claude-opus-4-7|Claude Opus 4.7]]

## Open Questions

- When should prompts explicitly discourage thinking to reduce latency?
