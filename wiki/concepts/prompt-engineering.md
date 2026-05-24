---
type: concept
aliases: ["prompt design", "prompting"]
tags: [prompt-engineering, ai]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Prompt Engineering

## Definition

Prompt engineering is the practice of designing instructions, context, examples, constraints, roles, and output expectations so a model can produce reliable, useful responses. [[2026-05-24--prompting-best-practices|Prompting best practices]]

## Scope

This concept covers clear instructions, task context, structured examples, role framing, output formatting, long-context layout, and verification criteria. It does not cover model training, fine-tuning, or post-processing systems except where prompts direct those workflows. [[2026-05-24--prompting-best-practices|Prompting best practices]]

## Contrasts

- **Model configuration**: Prompt engineering steers behavior through text and structure, while settings such as [[Effort Parameter]] change runtime tradeoffs.
- **Tool implementation**: Prompt engineering can instruct when to use tools, but the tools themselves belong to the surrounding application or agent harness.

## Evidence

- [[2026-05-24--prompting-best-practices|Prompting best practices]] — The guide emphasizes clear, explicit requests, context, examples, XML structure, role framing, and output controls.

## Related

- [[Few-Shot Prompting]]
- [[XML Prompt Structure]]
- [[Long Context Prompting]]
- [[Tool Use]]
- [[Agentic Systems]]

## Open Questions

- Which prompt patterns should become reusable templates for this wiki's own operations?
