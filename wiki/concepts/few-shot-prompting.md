---
type: concept
aliases: ["multishot prompting", "examples in prompts"]
tags: [prompt-engineering, examples]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# Few-Shot Prompting

## Definition

Few-shot prompting is the use of representative examples in a prompt to steer a model's output format, tone, structure, and edge-case behavior. [[2026-05-24--prompting-best-practices|Prompting best practices]]

## Scope

This concept covers examples that are relevant, diverse, and clearly separated from instructions or input. It does not mean copying a single sample mechanically or relying on examples that conflict with the written task. [[2026-05-24--prompting-best-practices|Prompting best practices]]

## Contrasts

- **Zero-shot prompting**: Zero-shot prompts rely on instructions alone, while few-shot prompts demonstrate the desired pattern.
- **Negative instructions**: Examples often steer more reliably than telling a model only what to avoid.

## Evidence

- [[2026-05-24--prompting-best-practices|Prompting best practices]] — The source recommends 3-5 relevant, diverse, structured examples and suggests wrapping them in `<example>` or `<examples>` tags.

## Related

- [[Prompt Engineering]]
- [[XML Prompt Structure]]
- [[Code Review Harnesses]]

## Open Questions

- What examples best represent the operator's preferred wiki style and citation density?
