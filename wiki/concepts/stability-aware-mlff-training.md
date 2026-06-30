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
  - research/molecular-simulation/molecular-dynamics
tags:
  - machine-learning-force-fields
  - stable-training
  - differentiable-simulation
sources:
  - SRC-0024
  - SRC-0060
related:
  - "[[wiki/concepts/automated-force-field-training]]"
  - "[[wiki/concepts/ubio-molfm-biological-molecular-foundation-model]]"
sensitivity: public
encryption: none
---

# Stability-Aware MLFF Training

## Summary

Stability-aware MLFF training augments energy/force fitting with simulation-derived observable losses so that a learned force field remains stable in downstream molecular dynamics. [SRC-0024]

## Key Points

- StABlE searches for unstable regions by running many MD replicas and then trains from near-unstable configurations. [SRC-0024]
- The Boltzmann Estimator computes gradients of equilibrium observable expectations without backpropagating through the entire MD trajectory. [SRC-0024]
- Energy/force regularization is retained because observable matching alone is underconstrained. [SRC-0024]
- Stability is evaluated as a downstream simulation property, not just as low force MAE on static structures. [SRC-0024]
- SRC-0060 follows the same validation logic for a foundation-model MLFF by moving from static out-of-distribution energy/force tests to short downstream MD tests for water, salt solution, Cyclosporine A, and RNA magnesium coordination. [SRC-0060, section 2.2]

## Core equations

$$
L_{\mathrm{StABlE}}(\theta)=
\left\|
E_{\Gamma\sim P_{\theta}}[g(\Gamma)]-g_{\mathrm{ref}}
\right\|_2^2+\lambda L_{\mathrm{QM}}.
$$

[SRC-0024]

## Caveats

The method depends on observables and instability criteria that are meaningful for the target system; a stable trajectory is not automatically a physically accurate trajectory. [SRC-0024]

UBio-MolFM reinforces this caveat: the report treats its 200 ps downstream tests as evidence of physical fidelity, while still listing longer timescales and larger biomolecular tasks as future validation targets. [SRC-0060, sections 2.2 and 3.2]

## Links

- [[wiki/sources/SRC-0024-stable-training-machine-learning-force-fields-boltzmann-estimators]]
- [[wiki/sources/SRC-0060-ubio-molfm-universal-molecular-foundation-model]]
- [[wiki/concepts/automated-force-field-training]]
- [[wiki/concepts/ubio-molfm-biological-molecular-foundation-model]]
- [[wiki/questions/force-field-training-validation-scope]]
