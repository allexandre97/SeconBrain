---
type: concept
status: active
created: 2026-06-30
updated: 2026-06-30
areas:
  - research
categories:
  - research/molecular-simulation/free-energy
  - research/computational-drug-discovery
  - research/adaptive-sampling
tags:
  - ladybugs
  - lambda-dynamics
  - gibbs-sampling
  - relative-binding-free-energy
  - fastmbar
  - math-heavy
related:
  - "[[sources/SRC-0013-ladybugs-lambda-dynamics]]"
  - "[[concepts/relative-binding-free-energy-benchmarking]]"
  - "[[concepts/free-energy-estimation]]"
  - "[[concepts/adaptive-enhanced-sampling]]"
sources:
  - SRC-0013
sensitivity: public
encryption: none
---

# Lambda-Dynamics with Bias-Updated Gibbs Sampling

## Summary

Lambda-dynamics with bias-updated Gibbs sampling, or LaDyBUGS, is a relative-binding-free-energy method that samples many discrete alchemical ligand states in one simulation. It uses Gibbs sampling to switch $\lambda$ states, dynamic biases to maintain uniform state exploration, and FastMBAR to refine biases and estimate free energies. [SRC-0013]

## Key Points

- LaDyBUGS alternates short MD sampling of $P(X\mid\lambda)$ with direct Gibbs sampling of $P(\lambda\mid X)$. [SRC-0013]
- Biases are updated throughout production sampling, eliminating a separate static-bias burn-in phase. [SRC-0013]
- FastMBAR periodically estimates free-energy differences and contributes to the next bias update. [SRC-0013]
- The method is designed for ligand series where several analogues can be represented as discrete alchemical end states around a shared core. [SRC-0013]

## Core equations

Gibbs conditional: [SRC-0013, eq. 1]

$$
P(\lambda_i\mid X)=
\frac{\exp[-\beta(V^{SS}(X,\lambda_i)+V^{MS}(X,\lambda_i)+E_i)]}
{\sum_{l=1}^{M}\exp[-\beta(V^{SS}(X,\lambda_l)+V^{MS}(X,\lambda_l)+E_l)]}.
$$

Bias update: [SRC-0013, eq. 4]

$$
E_i=-\Delta G_i^{t=u}+\epsilon_b\,2^{L_i-\min[L(\lambda)]}.
$$

## Implementation consequences

- All $\lambda$ state energies are evaluated during Gibbs sampling, so the data required by MBAR are produced on the fly. [SRC-0013]
- Sampling multiple perturbations in one simulation can produce large efficiency gains relative to pairwise TI/MBAR. [SRC-0013]
- The number of discrete states grows with the number of ligands and lambda spacing, so grouping strategy matters. [SRC-0013, eq. 5]

## Caveats

- The reported gains are benchmark-specific and depend on implementation and system grouping. [SRC-0013]
- The method still needs enough coordinate sampling in each conditional MD segment for reliable MBAR estimates. [SRC-0013]

## Links

- [[sources/SRC-0013-ladybugs-lambda-dynamics]]
- [[concepts/relative-binding-free-energy-benchmarking]]
- [[concepts/free-energy-estimation]]
- [[concepts/adaptive-enhanced-sampling]]

## Open Questions

- How should ligand groups be selected to maximize LaDyBUGS efficiency while preserving reliable overlap and sampling? [SRC-0013]
