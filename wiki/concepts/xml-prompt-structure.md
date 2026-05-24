---
type: concept
aliases: ["XML tags in prompts", "tagged prompt structure"]
tags: [prompt-engineering, structure]
created: 2026-05-24
updated: 2026-05-24
source_count: 1
---

# XML Prompt Structure

## Definition

XML prompt structure is the use of descriptive XML-style tags to separate instructions, context, examples, inputs, documents, metadata, and expected outputs inside a prompt. [[2026-05-24--prompting-best-practices|Prompting best practices]]

## Scope

This concept covers tag naming, consistency, and nesting when prompt content has a hierarchy. It does not require strict XML validation unless the application itself needs machine-parseable XML. [[2026-05-24--prompting-best-practices|Prompting best practices]]

## Contrasts

- **Plain prose prompts**: Plain prose may be enough for simple requests, while XML-style tags become more useful as prompts mix multiple content types.
- **Output schema enforcement**: XML tags clarify prompt structure but are separate from strict JSON schemas or parser-enforced output contracts.

## Evidence

- [[2026-05-24--prompting-best-practices|Prompting best practices]] — The source recommends tags such as `<instructions>`, `<context>`, `<input>`, and nested `<document>` structures for complex prompts.

## Related

- [[Prompt Engineering]]
- [[Few-Shot Prompting]]
- [[Long Context Prompting]]

## Open Questions

- Which tags should be standardized for reusable prompts in this wiki?
