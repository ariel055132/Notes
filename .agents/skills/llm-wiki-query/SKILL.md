---
name: llm-wiki-query
description: Find and answer questions from Notes evidence in Chinese or English, including legacy notes, with source-level citations and explicit coverage limits.
---

# Notes query

Read `AGENTS.md`. Start with `python3 scripts/wiki_qa_bot.py --question "QUESTION" --json` and `wiki/index.md`. The CLI returns evidence excerpts; it does not generate an LLM answer. Search includes Wiki plus AWS, Stock, Container and SystemDesign unless `--no-legacy` is requested.

Read relevant excerpts, source cards and their underlying evidence before composing an answer. Use the operator's language. Cite the supporting file and heading/page for each important conclusion; distinguish source claims, assistant inference and confirmed personal views.

Preserve uncertainty from needs-review, partial or secondary-summary evidence. Do not answer from Open Questions/Follow-ups or unreviewed placeholders. If available evidence does not support the question, say what is missing; do not fill the gap with assumptions. Search is lexical with curated bilingual aliases, so try equivalent terms or file inspection before concluding a topic is absent.

File reusable syntheses when already requested or clearly within an agreed pilot; clarify only when intent is ambiguous. Then rebuild/check the generated index and append to the log. Never replace user-authored judgments with generated opinions or silently promote limited evidence.
