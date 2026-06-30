---
type: concept
status: active
created: 2026-06-30
updated: 2026-06-30
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/adaptive-sampling
  - research/molecular-simulation/free-energy
tags:
  - awh
  - replay-reweighting
  - natural-gradient
  - force-field-optimization
related:
  - "[[wiki/concepts/accelerated-weight-histogram-method]]"
  - "[[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]"
sources:
  - SRC-0018
sensitivity: public
encryption: none
---

# AWH Replay Force Field Optimization

## Summary

AWH replay force-field optimization uses adaptive AWH to obtain a broad reference ensemble, freezes the bias, and performs offline replay reweighting to optimize force-field parameters against free-energy and observable targets. [SRC-0018]

## Key Points

- The optimizer treats AWH as a data-generation mechanism, not as a differentiable online update rule. [SRC-0018]
- Frozen-bias replay estimates endpoint free energies and gradients for candidate parameter sets. [SRC-0018]
- The same replay machinery can estimate general state observables and their gradients. [SRC-0018]
- A latent-space empirical Fisher matrix provides the local metric for natural-gradient-like steps. [SRC-0018]
- KL-target scaling and ESS checks limit proposed updates to regions still supported by the frozen reference ensemble. [SRC-0018]

## Core equations

Endpoint replay gradient:

$$
\nabla_{\theta} \tilde F_m(\theta)
=
\beta^{-1}\sum_n
w_m^{\mathrm{rep}}(n;\theta)
\nabla_{\theta}u(x_n,m;\theta).
$$

[SRC-0018]

Fisher/KL step geometry:

$$
D_{\mathrm{KL}}(p_{\phi}\Vert p_{\phi+\Delta\phi})
\approx
\frac{1}{2}\Delta\phi^{\top}I(\phi)\Delta\phi.
$$

[SRC-0018]

## Implementation consequences

Training can mix free-energy-cycle targets and observable targets because the loss is assembled after replay and normalized by target tolerances. [SRC-0018]

## Caveats

The method is only as good as the support of the frozen ensemble; failed replay/AWH parity or low ESS indicates that new sampling is needed before trusting an update. [SRC-0018]

## Links

- [[wiki/sources/SRC-0018-force-field-optimization-via-awh-gradients]]
- [[wiki/concepts/accelerated-weight-histogram-method]]
- [[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]
