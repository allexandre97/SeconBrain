---
type: concept
status: active
created: 2026-06-29
updated: 2026-06-29
areas:
  - admin
categories:
  - admin/wiki-governance
  - research/llm-wiki/workflows
tags:
  - workflow
  - codex
related:
  - "[[wiki/concepts/source-ingestion]]"
  - "[[wiki/concepts/wiki-linting]]"
sources:
  - SRC-0002
sensitivity: public
encryption: none
---

# Reusable Codex Task Contracts

## Summary

Recurring Codex constraints and report formats should be documented once in `AGENTS.md` and `schema/workflows.md` instead of repeated in every prompt. [SRC-0002]

## Key Points

- Codex tasks should remain focused and contained. [SRC-0002]
- Codex should run validation before reporting completion. [SRC-0002]
- Codex should preserve citations, provenance, sensitivity metadata, and encryption metadata when editing pages. [SRC-0002]

## Links

- [[wiki/sources/SRC-0002-project-design-note]]
- [[wiki/concepts/source-ingestion]]
- [[wiki/concepts/wiki-linting]]
