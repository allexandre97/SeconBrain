---
type: concept
status: active
created: 2026-06-30
updated: 2026-06-30
areas:
  - research
categories:
  - research/bioimage-analysis/cytoskeleton
  - research/computer-vision/biomedical-imaging
tags:
  - fiber-reconstruction
  - topology
  - collagen
  - microscopy
related:
  - "[[concepts/cytoskeleton-segmentation-and-tracing]]"
  - "[[concepts/topology-aware-tubular-structure-segmentation]]"
sources:
  - SRC-0034
  - SRC-0035
sensitivity: public
encryption: none
---

# Topology-Aware Fiber Network Reconstruction

## Summary

Topology-aware fiber network reconstruction extracts a graph-like representation of biological fiber networks while preserving biologically or mechanically meaningful connectivity. SOAX does this through active-contour tracing and junction configuration; ToFiE uses Discrete Morse theory and persistent homology to reconstruct dense heterogeneous 3D fiber networks. [SRC-0035] [SRC-0034]

## Key Points

- The desired output is usually more than a mask: downstream analysis may require edge lengths, orientation, connectivity, junction locations, edge density, curvature, or centrality. [SRC-0034] [SRC-0035]
- SOAX is a model-based tracing tool that can extract 2D/3D centerlines and junctions but depends on image signal-to-noise ratio and parameter tuning. [SRC-0035]
- ToFiE targets dense, heterogeneous 3D networks where absolute intensity thresholding can fragment fibers or distort bundles and junctions. [SRC-0034]
- ToFiE's synthetic validation links reconstruction accuracy to topology-aware node recall and structural distribution similarity rather than only pixel overlap. [SRC-0034]
- Topology-aware reconstruction is especially relevant when mechanical models predict that fiber-network behavior depends on average connectivity or junction structure. [SRC-0034]

## Evidence

- SRC-0035 demonstrates SOAX across actin, microtubule, fibrin-like, and synthetic networks while documenting parameter and image-quality constraints.
- SRC-0034 reports high 3- and 4-junction recall on synthetic collagen-like networks at adequate signal-to-noise ratio and applies the workflow to collagen I confocal stacks.

## Links

- [[sources/SRC-0034-tofie-topology-aware-fiber-extraction-workflow-for-3d]]
- [[sources/SRC-0035-soax-software-for-quantification-of-3d-biopolymer-networks]]
- [[concepts/cytoskeleton-segmentation-and-tracing]]
- [[concepts/topology-aware-tubular-structure-segmentation]]

## Open Questions

- How should reconstruction workflows quantify uncertainty in junction identity when dense biological fibers approach the optical resolution limit?
