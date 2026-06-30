---
type: concept
status: active
created: 2026-06-30
updated: 2026-06-30
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/molecular-modeling
  - research/molecular-simulation/datasets
  - research/molecular-simulation/molecular-dynamics
  - research/biomolecules/proteins
  - research/biomolecules/rna
  - research/high-performance-computing
  - research/experimental-benchmarking
tags:
  - machine-learning-force-fields
  - foundation-models
  - equivariant-transformers
  - biological-simulation
sources:
  - SRC-0060
related:
  - "[[wiki/sources/SRC-0060-ubio-molfm-universal-molecular-foundation-model]]"
  - "[[wiki/concepts/machine-learned-interatomic-potential-foundation-models]]"
  - "[[wiki/concepts/machine-learning-potential-datasets]]"
  - "[[wiki/concepts/stability-aware-mlff-training]]"
sensitivity: public
encryption: none
---

# UBio-MolFM Biological Molecular Foundation Model

## Summary

UBio-MolFM is a biology-focused machine-learning force-field foundation model that combines a large biomolecular quantum-chemistry dataset, a scalable equivariant transformer, and conservative energy-force training for biomolecular molecular dynamics. [SRC-0060]

## Key Points

- The model is built to address the scale-accuracy gap: ab initio methods are too expensive for biological scale, while classical force fields can miss polarization, charge transfer, and complex potential-energy-surface effects. [SRC-0060, section 1]
- UBio-Mol26 extends molecular ML datasets toward biological macromolecules, including proteins, drug-like molecules, DNA/RNA fragments, lipid bilayers, explicit solvent, and trace ions. [SRC-0060, section 4.1]
- E2Former-V2 uses SO(3)-equivariant message passing with short-range local layers and longer-range fragment-style interactions, then optimizes the implementation with EAAS and an on-the-fly attention kernel. [SRC-0060, section 4.2]
- Conservative force computation is central: after Stage 1 initialization, forces are computed as gradients of predicted energy, reducing inconsistency between energy and force predictions. [SRC-0060, section 4.3.1]
- The strongest evidence in the report is for protein-rich biological systems at roughly 1,300-1,500 atoms and for short-timescale MD observables, not for arbitrary biomolecular production simulations. [SRC-0060, sections 2-3]

## Core equations

Conservative force relation: [SRC-0060, eqs. 7 and 10]

$$
\hat F_i=-\frac{\partial \hat E}{\partial \vec r_i}.
$$

Long-short range message split: [SRC-0060, eq. 6]

$$
m_i^S=\sum_{j\in N_{r_{\mathrm{short}}}(i)}\alpha_{ij}m_{ij},
\qquad
m_i^L=\sum_{j\in N_{r_{\mathrm{long}}}(i)}\alpha_{ij}m_{ij}.
$$

## Implementation consequences

- Downstream validation should check both static energy/force metrics and simulation observables, because the report treats static accuracy as necessary but insufficient for MD reliability. [SRC-0060, section 2.2]
- Nucleic-acid conclusions should be conservative: the report itself identifies DNA Stage 3 regression and limited top-down nucleic-acid data as gaps. [SRC-0060, sections 2.1.2 and 3.2]
- Scaling claims should include memory behavior, not just throughput, because UBio-MolFM still reports out-of-memory behavior at 100K atoms with long-range interactions enabled. [SRC-0060, section 2.3]

## Evidence

- The UBio-MolFM (S3) model reports strong improvements in protein force errors and protein relative-energy errors on a large out-of-distribution test set. [SRC-0060, section 2.1.2]
- Short MD tests report water and ionic solvation structure, solvent-dependent Cyclosporine A conformations, and RNA magnesium coordination behavior. [SRC-0060, section 2.2]
- Single-H100 benchmarks report higher throughput than compared equivariant baselines at 1K, 10K, and 50K atoms under conservative-force settings. [SRC-0060, table 4]

## Caveats

- The method is positioned as a proof of concept rather than a finished solution; the authors explicitly note that it remains much slower than classical force fields. [SRC-0060, section 3.1]
- Current evidence is strongest for short simulations and protein-focused data. Longer timescales, larger systems, protein-ligand binding free energies, and protein-protein interactions are listed as future validation targets. [SRC-0060, section 3.2]
- Public release status is partly future-facing: the report says dataset subset release exists, code for E2Former-V2 is available, and model weights will be released. [SRC-0060, section 5]

## Links

- [[wiki/sources/SRC-0060-ubio-molfm-universal-molecular-foundation-model]]
- [[wiki/concepts/machine-learned-interatomic-potential-foundation-models]]
- [[wiki/concepts/machine-learning-potential-datasets]]
- [[wiki/concepts/stability-aware-mlff-training]]
- [[wiki/questions/force-field-training-validation-scope]]

## Open Questions

- Which downstream biomolecular tasks will expose remaining failures once trajectories are longer than 200 ps? [SRC-0060, sections 2.2 and 3.2]
- Can balanced top-down sampling for DNA and RNA remove the observed nucleic-acid weakness without sacrificing protein accuracy? [SRC-0060, section 3.2]
