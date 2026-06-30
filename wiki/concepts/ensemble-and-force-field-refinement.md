---
type: concept
status: active
created: 2026-06-30
updated: 2026-06-30
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
tags:
  - ensemble-refinement
  - maximum-entropy
  - forward-model-refinement
  - mdrefine
related:
  - "[[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]"
sources:
  - SRC-0019
  - SRC-0020
sensitivity: public
encryption: none
---

# Ensemble and Force Field Refinement

## Summary

Ensemble and force-field refinement adjusts a simulated ensemble, a force-field correction, and/or a forward model so that simulated observables agree with experiment while preserving a regularized connection to the original simulation model. [SRC-0019]

## Key Points

- MDRefine treats ensemble error, force-field error, and forward-model error as separable but potentially coupled causes of experiment/simulation mismatch. [SRC-0019]
- Maximum-entropy ensemble refinement gives an exponential reweighting form over the prior trajectory. [SRC-0019]
- Force-field corrections $\phi$ change the Boltzmann weights of frames, while forward-model parameters $\theta$ change the mapping from structures to observables. [SRC-0019]
- Hyperparameters $\alpha,\beta,\gamma$ control the relative confidence assigned to ensemble reweighting, force-field regularization, and forward-model regularization. [SRC-0019] [SRC-0020]
- The stationarity of the inner $\lambda^*$ problem simplifies outer differentiation. [SRC-0020]

## Core equations

Regularized ensemble loss:

$$
L[P]=\frac{1}{2}\chi^2[P]+\alpha D_{\mathrm{KL}}[P\Vert P_0].
$$

[SRC-0019]

Joint refinement loss:

$$
L_1(\phi,\theta)
=
-\alpha\Gamma(\lambda^*(\phi,\theta);\phi,\theta)
+\beta R_1(\phi)+\gamma R_2(\theta).
$$

[SRC-0019] [SRC-0020]

Stationarity derivative:

$$
\frac{\partial L_1}{\partial \mu_j}
=
\left.
\frac{\partial L}{\partial \mu_j}
\right|_{\lambda^*(\mu)},
\quad \mu=(\phi,\theta).
$$

[SRC-0020]

## Caveats

When both force-field and forward-model parameters are flexible, the same reduction in $\chi^2$ can sometimes be explained by multiple correction mechanisms. Cross-validation and regularization reduce but do not remove this identifiability issue. [SRC-0019] [SRC-0020]

## Links

- [[wiki/sources/SRC-0019-mdrefine-python-package-refining-md-trajectories]]
- [[wiki/sources/SRC-0020-mdrefine-supplementary-material]]
- [[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]
- [[wiki/questions/force-field-training-validation-scope]]
