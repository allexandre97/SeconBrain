---
type: tension
status: active
created: 2026-07-01
updated: 2026-07-01
tension_status: active
areas:
  - research
categories:
  - research/computer-vision/biomedical-imaging
  - research/bioimage-analysis/filament-segmentation
  - research/machine-learning/scientific-modeling
tags:
  - tension
  - cldice
  - topology
related:
  - "[[wiki/concepts/topology-aware-tubular-structure-segmentation]]"
related_claims:
  - "[[wiki/claims/CLM-0003-cldice-connectivity-aware-tubular-segmentation]]"
related_questions:
  - "[[wiki/questions/QST-0001-cldice-biological-transfer-scope]]"
sources:
  - SRC-0032
sensitivity: public
encryption: none
---

# clDice Topology Guarantee Versus Practical Transfer

## Tension

clDice is designed to preserve tubular topology, but its formal guarantee depends on foreground/background skeleton assumptions and does not automatically settle practical biological fiber reconstruction. [SRC-0032, section 3]

## Positions

- SRC-0032 defines clDice and soft-clDice to emphasize centerline connectivity and reports improved topology-aware segmentation behavior across several datasets. [SRC-0032, sections 2 and 5-6]
- SRC-0032's topological guarantee depends on structural assumptions, and the wiki records that biological fiber tasks still need domain-specific validation. [SRC-0032, section 3]

## Why it matters

Future image-analysis answers should not equate "topology-aware loss" with validated biological graph reconstruction in every microscopy setting.

## Resolution status

Active. Transfer to specific biological fiber applications remains an open validation question. [SRC-0032]

## Links

- [[wiki/claims/CLM-0003-cldice-connectivity-aware-tubular-segmentation]]
- [[wiki/questions/QST-0001-cldice-biological-transfer-scope]]
- [[wiki/concepts/topology-aware-tubular-structure-segmentation]]
