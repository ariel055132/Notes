---
type: concept
aliases: ["tool calling", "tool usage"]
tags: [agentic-systems, tools, prompt-engineering]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Tool Use

## Definition

Tool use is the model behavior of invoking external capabilities to inspect state, search, read files, modify artifacts, run commands, or otherwise act beyond text generation. [[2026-05-24--prompting-best-practices|Prompting best practices]]

## Scope

This concept covers when to trigger tools, how explicit prompts can default the model toward action or restraint, how to report progress, and how to avoid destructive or hard-to-reverse operations. It does not include the implementation details of each external tool. [[2026-05-24--prompting-best-practices|Prompting best practices]]

## Contrasts

- **Answer-only behavior**: A model can respond with recommendations, while tool use lets it inspect or change actual state when permitted.
- **Parallel Tool Calling**: Tool use is the broader capability; parallel tool calling is a scheduling pattern for independent tool calls.

## Evidence

- [[2026-05-24--prompting-best-practices|Prompting best practices]] — The source says models benefit from explicit direction to use tools and should distinguish ambiguous suggestions from requests to implement.

## Related

- [[Agentic Systems]]
- [[Parallel Tool Calling]]
- [[Adaptive Thinking]]
- [[Subagent Orchestration]]
- [[Prompt Engineering]]

## Open Questions

- Which wiki workflows should default to action, and which should stop for operator approval before edits?
