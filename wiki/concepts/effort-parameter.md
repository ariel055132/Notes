---
type: concept
aliases: ["effort level", "output_config effort"]
tags: [claude, model-configuration, reasoning]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Effort Parameter

## Definition

The effort parameter is a Claude runtime setting used to trade off intelligence, latency, token spend, and reasoning depth for a task. [[2026-05-24--prompting-best-practices|Prompting best practices]]

## Scope

This concept covers choosing lower effort for scoped latency-sensitive work and higher effort for intelligence-sensitive, coding, research, or agentic tasks. It does not replace clear prompt requirements or verification. [[2026-05-24--prompting-best-practices|Prompting best practices]]

## Contrasts

- **Prompt instructions**: Instructions describe what to do, while effort affects how much reasoning budget the model applies.
- **Adaptive Thinking**: Effort influences reasoning depth, while adaptive thinking decides when and how much reasoning to use during a task.

## Evidence

- [[2026-05-24--prompting-best-practices|Prompting best practices]] — The source recommends testing effort levels and raising effort for complex problems instead of trying to prompt around shallow reasoning.

## Related

- [[claude-opus-4-7|Claude Opus 4.7]]
- [[claude-sonnet-4-6|Claude Sonnet 4.6]]
- [[adaptive-thinking|Adaptive Thinking]]
- [[agentic-systems|Agentic Systems]]

## Open Questions

- What effort levels are cost-effective for the operator's real prompt-engineering and wiki-maintenance workloads?
