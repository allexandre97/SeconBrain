---
type: concept
status: active
created: 2026-06-30
updated: 2026-06-30
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/scientific-modeling
tags:
  - symbolic-regression
  - interatomic-potentials
  - equation-learning
sources:
  - SRC-0017
  - SRC-0040
related:
  - "[[concepts/automated-force-field-training]]"
  - "[[concepts/gnn-to-symbolic-regression-potentials]]"
sensitivity: public
encryption: none
---

# Symbolic Regression Interatomic Potentials

## Summary

Symbolic regression interatomic potentials search over explicit mathematical forms for potential-energy terms, aiming to improve accuracy while retaining interpretable equations. [SRC-0017]

## Key Points

- SRC-0017 uses equation-learner networks plus Monte Carlo Tree Search to discover EAM-like copper potentials from DFT data. [SRC-0017]
- The approach can be constrained by a known physical scaffold, such as an embedded-atom decomposition, while still allowing pair, density, or embedding terms to evolve. [SRC-0017]
- Validation must include out-of-training physical properties, because good energy/force fitting alone does not prove transferability. [SRC-0017]
- For copper, SRC-0017 reports improved bulk, surface, defect, phonon, polymorph, and melting predictions relative to Sutton-Chen EAM. [SRC-0017]
- SRC-0040 uses a trained GNN as an intermediate representation, then applies symbolic regression to edge-model outputs to recover an interpretable Lennard-Jones-like pair potential from system-level MD energies. [SRC-0040]

## Core equation

EAM-style scaffold:

$$
E=\sum_i F(\rho_i)+\frac{1}{2}\sum_{i\ne j}\phi(r_{ij}).
$$

[SRC-0017]

## Caveats

Symbolic interpretability depends on the search grammar and physical scaffold. A learned closed-form expression is easier to inspect than a black-box neural potential, but it still requires validation outside the training distribution. [SRC-0017]

When symbolic regression is applied to GNN-derived latent contributions, interpretability also depends on whether the GNN architecture makes those contributions physically meaningful, such as pairwise additivity in the Lennard-Jones benchmark. [SRC-0040]

## Links

- [[sources/SRC-0017-symbolic-regression-reinforcement-learning-interatomic-potentials]]
- [[sources/SRC-0040-using-graph-neural-network-and-symbolic-regression-to]]
- [[concepts/automated-force-field-training]]
- [[concepts/gnn-to-symbolic-regression-potentials]]
- [[questions/force-field-training-validation-scope]]
