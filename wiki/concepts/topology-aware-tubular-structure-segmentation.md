---
type: concept
status: active
created: 2026-06-30
updated: 2026-06-30
areas:
  - research
categories:
  - research/computer-vision/biomedical-imaging
  - research/machine-learning/scientific-modeling
  - research/bioimage-analysis/filament-segmentation
tags:
  - topology
  - tubular-segmentation
  - connectivity
  - deep-learning
related:
  - "[[wiki/concepts/deep-learning-cytoskeleton-image-analysis]]"
  - "[[wiki/concepts/topology-aware-fiber-network-reconstruction]]"
sources:
  - SRC-0032
  - SRC-0033
sensitivity: public
encryption: none
---

# Topology-Aware Tubular Structure Segmentation

## Summary

Topology-aware tubular segmentation prioritizes connectedness, centerlines, branches, and junctions rather than only voxel overlap. This matters for vessels, neurons, roads, cytoskeletal filaments, and other network-like structures where a small missing segment can alter downstream graph or flow analysis. [SRC-0032] [SRC-0033]

## Key Points

- Overlap metrics such as Dice and Jaccard can assign similar scores to predictions with very different connectivity, especially when structures are thin and networks contain branches. [SRC-0032]
- clDice evaluates skeleton-mask agreement by combining topology precision and topology sensitivity, making it more sensitive to missing or spurious centerline branches. [SRC-0032]
- soft-clDice turns this idea into a neural-network training loss by approximating skeletonization with differentiable pooling operations. [SRC-0032]
- DeepVesselNet addresses related topology-relevant outputs by predicting vessels, centerlines, and bifurcations in 3D angiography while handling sparse targets, 3D memory cost, and limited annotation. [SRC-0033]
- These methods are adjacent to cytoskeletal image analysis but require domain-specific validation before being treated as directly transferable to actin, microtubules, collagen, or fibrin. [SRC-0032] [SRC-0033]

## Core equations

**clDice [SRC-0032]:**

$$
\operatorname{clDice}(V_P, V_L) =
2 \times \frac{T_{\mathrm{prec}}(S_P, V_L) T_{\mathrm{sens}}(S_L, V_P)}
{T_{\mathrm{prec}}(S_P, V_L) + T_{\mathrm{sens}}(S_L, V_P)}
$$

## Links

- [[wiki/sources/SRC-0032-cldice-a-novel-topology-preserving-loss-function-for]]
- [[wiki/sources/SRC-0033-deepvesselnet-vessel-segmentation-centerline-prediction-and-bifurcation-detection]]
- [[wiki/concepts/topology-aware-fiber-network-reconstruction]]
- [[wiki/concepts/deep-learning-cytoskeleton-image-analysis]]

## Open Questions

- Which topology-aware losses or architectures improve real biological fiber reconstruction when labels are incomplete and topology itself is uncertain?
