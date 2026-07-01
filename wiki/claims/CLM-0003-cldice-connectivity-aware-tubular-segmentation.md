---
type: claim
status: active
created: 2026-07-01
updated: 2026-07-01
claim_status: limited
claim_scope: local
areas:
  - research
categories:
  - research/computer-vision/biomedical-imaging
  - research/bioimage-analysis/filament-segmentation
  - research/machine-learning/scientific-modeling
tags:
  - claim
  - cldice
  - topology
related:
  - "[[wiki/concepts/topology-aware-tubular-structure-segmentation]]"
  - "[[wiki/questions/QST-0001-cldice-biological-transfer-scope]]"
  - "[[wiki/tensions/TEN-0003-cldice-topology-guarantee-vs-practical-transfer]]"
sources:
  - SRC-0032
sensitivity: public
encryption: none
---

# clDice Captures Tubular Connectivity Better Than Overlap Alone

## Claim

clDice evaluates skeleton-mask agreement for tubular structures, making it more sensitive than ordinary overlap metrics to missing or spurious centerline branches. [SRC-0032, section 2]

## Scope

This claim is local to SRC-0032 and limited by the paper's foreground/background skeleton assumptions, dataset choices, and task-specific validation requirements. [SRC-0032, sections 3-6]

## Evidence

- clDice combines topology precision and topology sensitivity to compare predicted and label skeleton-mask coverage. [SRC-0032, section 2]
- The paper benchmarks soft-clDice on public datasets covering retina vessels, roads, neurons, synthetic 3D vessels, and 3D brain vessels. [SRC-0032, sections 5-6]

## Caveats

- The homotopy-related guarantee depends on assumptions about foreground and background skeleta and does not automatically apply to arbitrary segmentations. [SRC-0032, section 3]
- Biological fiber applications still need domain-specific validation when labels are incomplete or topology is uncertain. [SRC-0032]

## Links

- [[wiki/sources/SRC-0032-cldice-a-novel-topology-preserving-loss-function-for]]
- [[wiki/concepts/topology-aware-tubular-structure-segmentation]]
- [[wiki/questions/QST-0001-cldice-biological-transfer-scope]]
- [[wiki/tensions/TEN-0003-cldice-topology-guarantee-vs-practical-transfer]]
