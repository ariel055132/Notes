---
type: "source"
source_path: "raw/imports/prompt-builder-guide/64c289db7934357690429d1d462fe8f52b169b99c4ffc0ab75030630542e4f5b.md"
title: "Prompt Engineering in 2025: Complete Guide for ChatGPT, Claude, and Gemini"
author: "Prompt Builder Team"
date: "2025-06-13"
tags: ["prompt-engineering", "prompting", "chatgpt", "claude", "gemini", "ai-learning", "knowledge-management"]
created: "2026-05-24"
source_id: "prompt-builder-guide"
source_type: "article"
source_url: "https://promptbuilder.cc/blog/prompt-engineering-in-2025-complete-guide"
published_date: "2025-06-13"
updated: "2026-09-24"
processing_status: "ready"
coverage: "partial"
confidence: "medium"
evidence_level: "original-document"
extraction_path: "derived/prompt-builder-guide/64c289db7934357690429d1d462fe8f52b169b99c4ffc0ab75030630542e4f5b-be50c169d2843a64.json"
upstream_sha256: "64c289db7934357690429d1d462fe8f52b169b99c4ffc0ab75030630542e4f5b"
captured_at: "2026-05-24"
review_scope: "Historical local clip: task clarity, evidence metadata and evaluation workflow only."
---

# Prompt Engineering in 2025: Complete Guide for ChatGPT, Claude, and Gemini

## Summary

This source presents prompt engineering as a practical discipline for getting consistent, reusable outputs from models such as ChatGPT, Claude, and Gemini. It prioritizes a simple prompt structure: state the goal, provide working context, define constraints, and specify the output format. It explains core techniques such as zero-shot prompting, few-shot prompting, chain-of-thought prompting, retrieval-augmented generation, prompt chaining, and iterative refinement. It also treats prompts as assets that should be tested, versioned, reused, and evaluated for accuracy, format adherence, cost, and latency.

## Key Claims

1. Effective prompts combine a clear objective, relevant context, explicit constraints, and a requested output format.
2. Prompt engineering has shifted from one-off phrasing toward reusable prompt libraries, connected tools, retrieval, and measurable quality workflows.
3. Zero-shot prompting is a good starting point for simple tasks, while few-shot prompting is better when tone, format, or structure matters.
4. Chain-of-thought prompting is useful for math, planning, trade-off analysis, and decisions that need explicit assumptions.
5. Retrieval-augmented generation grounds answers in supplied source material instead of relying only on model memory.
6. Advanced patterns such as metacognitive prompting, iterative refinement, multiple viewpoints, context-window optimization, and prompt chaining are most useful when a task is too large for a single straightforward prompt.
7. Important prompts should be tested with a small eval set and tracked for accuracy, format adherence, cost, latency, retries, and tool calls.
8. Industry-specific prompts should encode the domain's rules, limitations, evidence expectations, and risk boundaries.

## Notable Quotes

> "Prompts are shared assets"

> "Start with zero shot."

> "A solid prompt includes four things"

## Entities Mentioned

- [[Prompt Builder]] — Publisher of the article and related prompt-generator tools.
- [[ChatGPT]] — One of the target model products for the guide.
- [[Claude]] — One of the target model families for the guide.
- [[Gemini]] — One of the target model products for the guide.

## Concepts Mentioned

- [[Prompt Engineering]] — Practical design of goals, context, constraints, examples, and output formats.
- [[POWER Prompt Framework]] — Purpose, Output Format, Working Context, Examples, and Refinement Instructions.
- [[Zero-Shot Prompting]] — Prompting with instructions but no examples.
- [[Few-Shot Prompting]] — Prompting with examples that demonstrate the desired pattern.
- [[Chain-of-Thought Prompting]] — Asking the model to work through assumptions or reasoning steps before answering.
- [[Retrieval-Augmented Generation]] — Supplying source material for grounded answers.
- [[Metacognitive Prompting]] — Asking the model to inspect assumptions, missing information, and limits before answering.
- [[Iterative Refinement]] — Drafting, reviewing, and rewriting through feedback loops.
- [[Long Context Prompting]] — Structuring large inputs so relevant material remains usable.
- [[Prompt Chaining]] — Sequencing prompts so each output feeds the next step.
- [[Prompt Testing and Versioning]] — Treating prompts as reusable assets with evals and change control.
- [[Tool Use]] — Connecting prompts to tools, retrieval, and production workflows.

## Follow-ups

- Build a local prompt pattern library around practical prompt-engineering techniques rather than vendor-specific model behavior.
- Add example prompts for this wiki's ingest, query, and lint workflows using the POWER structure.
- Compare this Prompt Builder guide with the Anthropic source to identify model-agnostic principles that appear across vendors.

## 本輪閱讀範圍與限制

本輪核读 2026-05-24 本機剪藏，採用需求、上下文與驗收方法；沒有把模型專屬建議當作目前所有模型的通用行為，也未證明能提高個人學習成效。遠端圖片和現行網頁版本未逐一比對，因此 coverage 保留 partial。

相關主題：[[2026-09-24--ai-learning-knowledge-management|AI 輔助學習與知識管理]]。
