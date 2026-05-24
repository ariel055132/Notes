---
type: concept
aliases: ["tool calling", "tool usage"]
tags: [agentic-systems, tools, prompt-engineering]
created: 2026-05-24
updated: 2026-05-24
source_count: 2
---

# Tool Use

## Definition

Tool use is the model behavior of invoking external capabilities to inspect state, search, read files, retrieve context, modify artifacts, run commands, or otherwise act beyond text generation. [[2026-05-24--prompting-best-practices|Prompting best practices]] [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]]

## Scope

This concept covers when to trigger tools, how explicit prompts can default the model toward action or restraint, how to report progress, and how to avoid destructive or hard-to-reverse operations. It also covers prompts that connect to retrieval, APIs, or production workflows at a high level, but it does not include the implementation details of each external tool. [[2026-05-24--prompting-best-practices|Prompting best practices]] [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]]

## Contrasts

- **Answer-only behavior**: A model can respond with recommendations, while tool use lets it inspect or change actual state when permitted. [[2026-05-24--prompting-best-practices|Prompting best practices]]
- **Parallel Tool Calling**: Tool use is the broader capability; parallel tool calling is a scheduling pattern for independent tool calls. [[2026-05-24--prompting-best-practices|Prompting best practices]]
- **Retrieval-Augmented Generation**: Retrieval-augmented generation supplies source material for grounded answers, while tool use is the broader capability for calling retrieval systems, APIs, files, or other external capabilities. [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]]

## Evidence

- [[2026-05-24--prompting-best-practices|Prompting best practices]] — The source says models benefit from explicit direction to use tools and should distinguish ambiguous suggestions from requests to implement.
- [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]] — The source describes the trend toward prompts connected to tools, retrieval, APIs, searches, and production workflows.

## Related

- [[Agentic Systems]]
- [[Parallel Tool Calling]]
- [[Adaptive Thinking]]
- [[Subagent Orchestration]]
- [[Prompt Engineering]]
- [[Retrieval-Augmented Generation]]

## Open Questions

- Which wiki workflows should default to action, and which should stop for operator approval before edits?
