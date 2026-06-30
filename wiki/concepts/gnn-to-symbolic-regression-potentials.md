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
  - research/machine-learning/molecular-modeling
tags:
  - graph-neural-networks
  - symbolic-regression
  - interatomic-potentials
sources:
  - SRC-0040
related:
  - "[[wiki/concepts/symbolic-regression-interatomic-potentials]]"
  - "[[wiki/concepts/automated-force-field-training]]"
sensitivity: public
encryption: none
---

# GNN to Symbolic Regression Potentials

## Summary

GNN-to-symbolic-regression potential learning uses a graph neural network to infer latent interaction contributions from system-level molecular-simulation data, then fits symbolic expressions to those learned contributions to recover interpretable analytical potentials. [SRC-0040]

## Key Points

- The approach is intended to bridge black-box ML potentials and classical analytical force fields. [SRC-0040]
- In the Lennard-Jones benchmark, the GNN is structured so edge outputs approximate pair contributions and the global output sums them into total potential energy. [SRC-0040]
- Symbolic regression uses pair distance and GNN edge outputs to search for compact equations. [SRC-0040]
- Dataset design matters: broad, decorrelated coverage of interatomic distances is necessary to avoid overfitting and recover steep repulsive regions. [SRC-0040]
- Generalization to many-body materials requires richer descriptors and symbolic forms beyond pairwise distance. [SRC-0040]

## Links

- [[wiki/sources/SRC-0040-using-graph-neural-network-and-symbolic-regression-to]]
- [[wiki/concepts/symbolic-regression-interatomic-potentials]]
- [[wiki/concepts/automated-force-field-training]]

## Open Questions

- How can symbolic regression remain tractable when the learned interaction depends on angular, local-environment, or many-body descriptors?
