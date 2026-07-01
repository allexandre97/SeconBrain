---
type: claim
status: active
created: 2026-07-01
updated: 2026-07-01
claim_status: limited
claim_scope: cross-source
areas:
  - research
categories:
  - research/adaptive-sampling
  - research/molecular-simulation/free-energy
  - research/statistics/monte-carlo
tags:
  - claim
  - accelerated-weight-histogram
  - adaptive-sampling
related:
  - "[[wiki/sources/SRC-0007-improving-efficiency-extended-ensemble-awh]]"
  - "[[wiki/sources/SRC-0008-awh-free-energy-landscapes]]"
  - "[[wiki/sources/SRC-0009-awh-alchemical-free-energy]]"
  - "[[wiki/concepts/accelerated-weight-histogram-method]]"
  - "[[wiki/questions/awh-validation-scope]]"
  - "[[wiki/tensions/TEN-0005-on-the-fly-bias-adaptation-vs-postprocessing-diagnostics]]"
sources:
  - SRC-0007
  - SRC-0008
  - SRC-0009
sensitivity: public
encryption: none
---

# AWH Updates Bias From Conditional Weight Histograms

## Claim

AWH adaptively updates free-energy bias parameters from accumulated conditional probabilities over the sampled parameter, using fractional weight histograms rather than only visited-state counts. [SRC-0007] [SRC-0008] [SRC-0009]

## Scope

This claim tracks the shared AWH mechanism across the original extended-ensemble paper, the molecular free-energy-landscape extension, and the alchemical free-energy application. It does not claim universal superiority over BAR, MBAR, umbrella sampling, or replica exchange. [SRC-0009]

## Evidence

- SRC-0007 defines the conditional weights and original weight-histogram update for an extended ensemble. [SRC-0007, eqs. 4-7]
- SRC-0008 applies the same mechanism to atomistic PMFs through umbrella centers and target distributions. [SRC-0008, section II]
- SRC-0009 specializes AWH to alchemical states and compares it with BAR/MBAR workflows. [SRC-0009]

## Caveats

- AWH still depends on useful parameterization, conditional overlap, and independent uncertainty checks. [SRC-0008] [SRC-0009]
- The reported advantages are strongest when adaptive movement along the chosen coordinate helps resolve slow exploration; equilibrium BAR/MBAR can be competitive when intermediate-state sampling is already efficient. [SRC-0009]

## Links

- [[wiki/sources/SRC-0007-improving-efficiency-extended-ensemble-awh]]
- [[wiki/sources/SRC-0008-awh-free-energy-landscapes]]
- [[wiki/sources/SRC-0009-awh-alchemical-free-energy]]
- [[wiki/concepts/accelerated-weight-histogram-method]]
- [[wiki/questions/awh-validation-scope]]
- [[wiki/tensions/TEN-0005-on-the-fly-bias-adaptation-vs-postprocessing-diagnostics]]
