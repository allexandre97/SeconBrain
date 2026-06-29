---
type: source
status: active
created: 2026-06-29
updated: 2026-06-29
source_id: SRC-0003
source_path: raw/sources/SRC-0003-training-a-force-field-from-scratch.pdf
original_path: /home/xnadre/Descargas/2603.16770v1.pdf
sha256: d84bc9589f33dc1c4c7011240b8bdb5d394154e2fa254857dc6dec461ca74262
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/scientific-modeling
tags:
  - molecular-dynamics
  - force-fields
  - graph-neural-networks
related:
  - "[[concepts/garnet-force-field]]"
  - "[[concepts/automated-force-field-training]]"
sources:
  - SRC-0003
sensitivity: public
encryption: none
---

# SRC-0003: Training a Force Field for Proteins and Small Molecules from Scratch

## Summary

This arXiv paper introduces Garnet, a graph-neural-network system that predicts molecular mechanics force-field parameters for proteins and small molecules without reusing legacy force-field parameters. It trains from quantum mechanical data, condensed-phase properties, and protein NMR data, and reports performance competitive with established force fields across small molecules, folded proteins, protein complexes, disordered proteins, and relative binding free energy benchmarks. [SRC-0003]

## Key Points

- Garnet uses continuous atom typing from molecular topology to assign force-field parameters. [SRC-0003]
- The model trains all parameters from scratch, including water parameters, although reference trajectories were used early in training to provide conformations. [SRC-0003]
- The authors report that Lennard-Jones was difficult to train in their automated pipeline, while the double exponential potential trained effectively. [SRC-0003]
- Garnet performed comparably to existing methods on several benchmarks, but the paper notes caveats such as possible overfitting on GB3, over-compaction of intrinsically disordered proteins, and occasional aromatic-ring planarity issues. [SRC-0003]
- The Garnet force field, scripts, validation tools, and data are reported as available under a permissive license. [SRC-0003]

## Links

- [[concepts/garnet-force-field]]
- [[concepts/automated-force-field-training]]
- [[concepts/double-exponential-potential]]
- [[concepts/relative-binding-free-energy-benchmarking]]
- [[questions/garnet-validation-scope]]

## Open Questions

- [[questions/garnet-validation-scope]] - Which molecule classes and simulation tasks still need validation before treating Garnet as broadly transferable? [SRC-0003]
