---
type: question
status: active
created: 2026-07-01
updated: 2026-07-01
question_status: open
areas:
  - research
categories:
  - research/computer-vision/biomedical-imaging
  - research/bioimage-analysis/filament-segmentation
tags:
  - question
  - topology
  - cldice
related:
  - "[[wiki/sources/SRC-0032-cldice-a-novel-topology-preserving-loss-function-for]]"
  - "[[wiki/concepts/topology-aware-tubular-structure-segmentation]]"
  - "[[wiki/concepts/deep-learning-cytoskeleton-image-analysis]]"
  - "[[wiki/claims/CLM-0003-cldice-connectivity-aware-tubular-segmentation]]"
sources:
  - SRC-0032
sensitivity: public
encryption: none
---

# clDice Biological Transfer Scope

## Question

How well do clDice and soft-clDice transfer to real biological fiber reconstruction tasks when labels are incomplete and the biologically relevant topology is uncertain? [SRC-0032]

## Context

SRC-0032 validates clDice across several tubular segmentation datasets and presents a topology-aware loss, but the wiki's topology-aware segmentation concept notes that cytoskeletal and other biological fiber applications still require domain-specific validation. [SRC-0032]

## Current Position

Treat clDice as a strong topology-aware candidate metric or loss for tubular structures, not as sufficient evidence that every biological filament reconstruction task is solved by the same loss. [SRC-0032]

## Links

- [[wiki/sources/SRC-0032-cldice-a-novel-topology-preserving-loss-function-for]]
- [[wiki/concepts/topology-aware-tubular-structure-segmentation]]
- [[wiki/concepts/deep-learning-cytoskeleton-image-analysis]]
- [[wiki/claims/CLM-0003-cldice-connectivity-aware-tubular-segmentation]]
- [[wiki/tensions/TEN-0003-cldice-topology-guarantee-vs-practical-transfer]]
