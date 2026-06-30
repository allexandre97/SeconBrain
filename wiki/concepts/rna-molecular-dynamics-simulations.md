---
type: concept
status: active
created: 2026-06-30
updated: 2026-06-30
areas:
  - research
categories:
  - research/molecular-simulation/molecular-dynamics
  - research/biomolecules/rna
tags:
  - RNA
  - molecular-dynamics
  - enhanced-sampling
  - coarse-graining
related:
  - "[[wiki/concepts/rna-force-field-limitations]]"
  - "[[wiki/concepts/adaptive-enhanced-sampling]]"
  - "[[wiki/concepts/molecular-dynamics-constraint-solvers]]"
sources:
  - SRC-0055
  - SRC-0056
sensitivity: public
encryption: none
---

# RNA Molecular Dynamics Simulations

## Summary

RNA molecular dynamics simulations use atomistic or coarse-grained models to interpret RNA structure, dynamics, folding, ion binding, catalysis, and protein/RNA recognition. Their usefulness depends strongly on force-field quality, sampling, ion treatment, and experimental context. [SRC-0056]

## Key Points

- RNA MD can complement experiments by exposing atomistic and time-resolved structural dynamics that are difficult to observe directly. [SRC-0056]
- Atomistic RNA simulations are limited by both force-field accuracy and the difficulty of sampling long time-scale conformational changes. [SRC-0056]
- Enhanced sampling and coarse-grained models are often needed to study RNA thermodynamics and kinetics beyond the reach of straightforward MD. [SRC-0056]
- Small RNA motifs can be severe tests of simulation reliability; the UUCG tetraloop remains difficult for widely used RNA force fields. [SRC-0055]
- Simulation results should be interpreted together with experimental data and with explicit reporting of failures and uncertainty. [SRC-0056]

## Links

- [[wiki/sources/SRC-0055-uucg-rna-tetraloop-as-a-formidable-force-field]]
- [[wiki/sources/SRC-0056-rna-structural-dynamics-as-captured-by-molecular-simulations]]
- [[wiki/concepts/rna-force-field-limitations]]
- [[wiki/concepts/adaptive-enhanced-sampling]]
