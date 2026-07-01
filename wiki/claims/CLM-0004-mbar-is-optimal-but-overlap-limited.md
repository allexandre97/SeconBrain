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
  - research/molecular-simulation/free-energy
  - research/statistics/monte-carlo
tags:
  - claim
  - mbar
  - overlap
  - reweighting
related:
  - "[[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]"
  - "[[wiki/sources/SRC-0012-mbar-configuration-mapping]]"
  - "[[wiki/concepts/multistate-bennett-acceptance-ratio]]"
  - "[[wiki/concepts/free-energy-estimation]]"
  - "[[wiki/questions/overlap-support-diagnostics-for-free-energy-estimators]]"
  - "[[wiki/tensions/TEN-0004-configuration-mapping-overlap-gain-vs-support-risk]]"
sources:
  - SRC-0023
  - SRC-0012
sensitivity: public
encryption: none
---

# MBAR Is Statistically Efficient But Overlap-Limited

## Claim

MBAR is a statistically efficient fixed-sample estimator for free energy differences, expectations, and uncertainties across multiple equilibrium states, but practical reliability still depends on phase-space overlap and adequate cross-state reduced-potential evaluations. [SRC-0023]

## Scope

This claim concerns MBAR-style postprocessing of collected samples. It does not say that a fixed sample set is always competitive with adaptive sampling, and it does not remove the need for mapped or additional sampling when raw support is poor. [SRC-0012] [SRC-0023]

## Evidence

- SRC-0023 derives MBAR as a multistate estimator for normalization-constant ratios, gives self-consistent equations, and provides asymptotic uncertainty estimates. [SRC-0023]
- SRC-0023 states practical requirements: reduced potentials for every retained sample at every estimator state, effectively uncorrelated samples for covariance interpretation, and sufficient phase-space overlap. [SRC-0023]
- SRC-0012 is motivated by the failure of ordinary reweighting when raw configuration overlap is poor or zero. [SRC-0012]

## Caveats

- MBAR removes histogram discretization and efficiently uses fixed samples, but it does not fix missing support or poor sampling. [SRC-0023]
- Mapping, additional intermediate states, or adaptive sampling may be needed when the fixed sample set does not cover the target states. [SRC-0012]

## Links

- [[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]
- [[wiki/sources/SRC-0012-mbar-configuration-mapping]]
- [[wiki/concepts/multistate-bennett-acceptance-ratio]]
- [[wiki/concepts/free-energy-estimation]]
- [[wiki/questions/overlap-support-diagnostics-for-free-energy-estimators]]
- [[wiki/tensions/TEN-0004-configuration-mapping-overlap-gain-vs-support-risk]]
