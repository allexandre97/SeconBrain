---
type: concept
status: active
created: 2026-06-30
updated: 2026-06-30
areas:
  - research
categories:
  - research/bioimage-analysis/filament-segmentation
  - research/computer-vision/biomedical-imaging
tags:
  - filament-segmentation
  - instance-segmentation
  - microscopy
related:
  - "[[wiki/concepts/cytoskeleton-segmentation-and-tracing]]"
  - "[[wiki/concepts/deep-learning-cytoskeleton-image-analysis]]"
  - "[[wiki/concepts/stretching-open-active-contours]]"
sources:
  - SRC-0029
  - SRC-0030
  - SRC-0031
sensitivity: public
encryption: none
---

# Filament Instance and Semantic Segmentation

## Summary

Filament segmentation in microscopy can mean semantic foreground masking, instance-level reconstruction of individual filaments, or quantitative extraction of length and count. The Liu papers show a progression from stacked U-Net semantic segmentation, to orientation-aware instance reconstruction, to actin count/length estimation with keypoint detection and fast marching. [SRC-0029] [SRC-0030] [SRC-0031]

## Key Points

- Semantic segmentation is useful but not always sufficient: false gaps and fragments can corrupt downstream biological measurements such as filament count, length, curvature, and movement. [SRC-0029]
- Skeleton-aware metrics such as SKIoU can better reflect filament centerline agreement than pixel IoU alone, especially when thickness and small alignment differences are less important than continuity. [SRC-0029] [SRC-0030]
- Orientation-aware instance methods can simplify junction handling by decomposing filaments into orientation-associated outputs and reconnecting fragments away from intersections. [SRC-0030]
- Hybrid pipelines can combine CNN segmentation, keypoint detection, and graph/geodesic algorithms when the desired output is a biological measurement rather than a mask. [SRC-0031]
- Synthetic data are repeatedly used to reduce annotation burden for orientation decomposition and junction/endpoint detection. [SRC-0030] [SRC-0031]

## Evidence

- SRC-0029 reports improved IoU/SKIoU over SOAX on microtubule and actin semantic segmentation.
- SRC-0030 reports better instance-level microtubule extraction metrics than SOAX and SIFNE on the authors' dataset, while documenting bias and segmentation-dependence limits.
- SRC-0031 reports actin filament counts closer to manual counts on two images than SOAX or a skeleton-disconnect baseline.

## Links

- [[wiki/sources/SRC-0029-densely-connected-stacked-u-network-for-filament-segmentation]]
- [[wiki/sources/SRC-0030-intersection-to-overpass-instance-segmentation-on-filamentous-structures]]
- [[wiki/sources/SRC-0031-quantifying-actin-filaments-in-microscopic-images-using-keypoint]]
- [[wiki/concepts/cytoskeleton-segmentation-and-tracing]]
- [[wiki/concepts/deep-learning-cytoskeleton-image-analysis]]

## Open Questions

- How well do synthetic-training strategies transfer across microscopy modalities, filament types, and dense crossing regimes?
- What validation design is sufficient when full manual instance labels are prohibitively expensive?
