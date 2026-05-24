---
type: concept
aliases: ["prompt design", "prompting", "prompt writing"]
tags: [prompt-engineering, ai]
created: 2026-05-24
updated: 2026-05-24
source_count: 2
---

# Prompt Engineering

## Definition

Prompt engineering is the practice of designing instructions, context, examples, constraints, roles, and output expectations so a model can produce reliable, useful, and repeatable responses. [[2026-05-24--prompting-best-practices|Prompting best practices]] [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]]

## Scope

This concept covers clear instructions, task context, structured examples, role framing, output formatting, long-context layout, retrieval grounding, prompt chaining, refinement loops, and verification criteria. It does not cover model training, fine-tuning, or post-processing systems except where prompts direct those workflows. [[2026-05-24--prompting-best-practices|Prompting best practices]] [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]]

## Contrasts

- **Model configuration**: Prompt engineering steers behavior through text and structure, while settings such as [[Effort Parameter]] change runtime tradeoffs. [[2026-05-24--prompting-best-practices|Prompting best practices]]
- **Tool implementation**: Prompt engineering can instruct when to use tools, but the tools themselves belong to the surrounding application or agent harness. [[2026-05-24--prompting-best-practices|Prompting best practices]] [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]]
- **Prompt testing**: Prompt engineering designs the prompt, while [[Prompt Testing and Versioning]] checks whether the prompt remains reliable across real inputs and model changes. [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]]

## Evidence

- [[2026-05-24--prompting-best-practices|Prompting best practices]] — The guide emphasizes clear, explicit requests, context, examples, XML structure, role framing, and output controls.
- [[2025-06-13--prompt-engineering-in-2025-complete-guide|Prompt Engineering in 2025]] — The guide frames prompt engineering as a practical workflow built around goals, context, constraints, output formats, examples, refinement, retrieval, and testing.

## Related

- [[POWER Prompt Framework]]
- [[Zero-Shot Prompting]]
- [[Few-Shot Prompting]]
- [[Chain-of-Thought Prompting]]
- [[Retrieval-Augmented Generation]]
- [[Metacognitive Prompting]]
- [[Iterative Refinement]]
- [[Prompt Chaining]]
- [[Prompt Testing and Versioning]]
- [[XML Prompt Structure]]
- [[Long Context Prompting]]
- [[Tool Use]]
- [[Agentic Systems]]

## Open Questions

- Which prompt patterns should become reusable templates for this wiki's own operations?
