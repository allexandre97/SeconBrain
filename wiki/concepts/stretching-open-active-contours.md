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
  - SOAC
  - SOAX
  - active-contours
  - filament-tracing
related:
  - "[[wiki/concepts/cytoskeleton-segmentation-and-tracing]]"
  - "[[wiki/concepts/filament-instance-and-semantic-segmentation]]"
sources:
  - SRC-0035
  - SRC-0029
  - SRC-0030
sensitivity: public
encryption: none
---

# Stretching Open Active Contours

## Summary

Stretching Open Active Contours are deformable curves used by SOAX to trace biopolymer filament centerlines and infer junctions in 2D or 3D microscopy images. They are a classical model-based baseline for later neural filament segmentation papers. [SRC-0035] [SRC-0029] [SRC-0030]

## Key Points

- SOACs are initialized along intensity ridges, attracted to filament centerlines by image forces, elongated by stretching forces, and stopped or merged when they encounter filament tips or other contours. [SRC-0035]
- SOAX uses a final junction-configuration step to cluster nearby T-junctions and cut/splice contours so they better represent physical network topology. [SRC-0035]
- SOAX includes visualization and manual editing because fully automated extraction can be sensitive to noise, unrelated structures, and parameter choices. [SRC-0035]
- Parameter sensitivity makes SOAX useful but not fully automatic; ridge threshold and stretch factor are especially important. [SRC-0035]
- Later deep-learning filament papers use SOAX as a baseline and report that it can fragment dense or crossing filament networks under their test conditions. [SRC-0029] [SRC-0030]

## Links

- [[wiki/sources/SRC-0035-soax-software-for-quantification-of-3d-biopolymer-networks]]
- [[wiki/concepts/cytoskeleton-segmentation-and-tracing]]
- [[wiki/concepts/filament-instance-and-semantic-segmentation]]

## Open Questions

- When is SOAX parameter tuning preferable to training a neural pipeline, especially for small datasets or 3D images with limited labels?
