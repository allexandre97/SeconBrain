---
type: concept
status: active
created: 2026-06-30
updated: 2026-06-30
areas:
  - research
categories:
  - research/molecular-simulation/molecular-dynamics
  - research/high-performance-computing
tags:
  - GPU
  - neighbor-lists
  - nonbonded-interactions
  - molecular-dynamics
related:
  - "[[wiki/concepts/particle-mesh-ewald-and-long-range-electrostatics]]"
sources:
  - SRC-0049
  - SRC-0053
sensitivity: public
encryption: none
---

# GPU MD Neighbor and Nonbonded Acceleration

## Summary

GPU MD acceleration depends heavily on making short-range nonbonded interaction evaluation and neighbor-list construction match GPU memory and execution patterns. Early GPU MD work used block/tile screening to avoid random atom-pair memory access, while later GPU-native neighbor lists use clustered and compressed layouts for memory efficiency. [SRC-0053] [SRC-0049]

## Key Points

- Standard atom-pair neighbor lists involve indirect memory access, which was especially expensive on early GPUs. [SRC-0053]
- Block/tile screening lists possible interacting atom blocks instead of individual atom pairs, improving locality while reducing unnecessary $N^2$ interactions. [SRC-0053]
- Clustered neighbor lists reduce list size by storing neighbor cluster indices rather than every particle pair. [SRC-0049]
- Space-filling-curve ordering improves locality and connects neighbor-list construction to octree domain decomposition. [SRC-0049]
- Hardware details matter: the best layout can differ between NVIDIA and AMD GPUs and between low and high neighbor counts. [SRC-0049]

## Core equations

At fixed density and cutoff, ideal short-range work scales as:

$$
O(N n_c) \approx O(N),
$$

where $n_c$ is the average number of neighbors within the cutoff. [SRC-0053]

## Links

- [[wiki/sources/SRC-0049-gpu-native-compressed-neighbor-lists-with-a-space]]
- [[wiki/sources/SRC-0053-efficient-nonbonded-interactions-for-molecular-dynamics-on-a]]
- [[wiki/concepts/particle-mesh-ewald-and-long-range-electrostatics]]
