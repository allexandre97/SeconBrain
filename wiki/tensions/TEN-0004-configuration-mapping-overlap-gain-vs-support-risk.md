---
type: tension
status: active
created: 2026-07-01
updated: 2026-07-01
tension_status: active
areas:
  - research
categories:
  - research/molecular-simulation/free-energy
  - research/statistics/monte-carlo
tags:
  - tension
  - configuration-mapping
  - mbar
  - overlap
related:
  - "[[wiki/concepts/mbar-with-configuration-mapping]]"
  - "[[wiki/concepts/multistate-bennett-acceptance-ratio]]"
related_claims:
  - "[[wiki/claims/CLM-0004-mbar-is-optimal-but-overlap-limited]]"
  - "[[wiki/claims/CLM-0005-configuration-mapping-extends-mbar]]"
related_questions:
  - "[[wiki/questions/overlap-support-diagnostics-for-free-energy-estimators]]"
sources:
  - SRC-0012
  - SRC-0023
sensitivity: public
encryption: none
---

# Configuration Mapping Overlap Gain Versus Support Risk

## Tension

Configuration mapping can make MBAR usable when raw configuration overlap is poor or zero, but a poor or poorly validated map can leave the estimator with inadequate mapped support or uneven observable accuracy. [SRC-0012] [SRC-0023]

## Positions

- SRC-0012 supports mapping as a way to transform samples before MBAR, with Jacobian-corrected warped reduced potentials and large efficiency gains in favorable examples. [SRC-0012]
- SRC-0012 also identifies mapping construction as the limiting requirement and shows that gains can depend on the observable. SRC-0023 preserves the broader MBAR requirement that estimates need adequate support and reduced-potential information. [SRC-0012] [SRC-0023]

## Why it matters

Future mapped-reweighting answers should not equate an invertible map with validated estimator support. The map must improve the relevant overlap enough for the reported quantity.

## Resolution status

Active. Better mapping diagnostics and automated map construction remain open validation problems. [SRC-0012]

## Links

- [[wiki/claims/CLM-0004-mbar-is-optimal-but-overlap-limited]]
- [[wiki/claims/CLM-0005-configuration-mapping-extends-mbar]]
- [[wiki/questions/overlap-support-diagnostics-for-free-energy-estimators]]
- [[wiki/concepts/mbar-with-configuration-mapping]]
- [[wiki/concepts/multistate-bennett-acceptance-ratio]]
