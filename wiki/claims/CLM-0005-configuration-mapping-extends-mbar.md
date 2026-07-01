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
  - configuration-mapping
  - overlap
related:
  - "[[wiki/sources/SRC-0012-mbar-configuration-mapping]]"
  - "[[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]"
  - "[[wiki/concepts/mbar-with-configuration-mapping]]"
  - "[[wiki/claims/CLM-0004-mbar-is-optimal-but-overlap-limited]]"
  - "[[wiki/questions/overlap-support-diagnostics-for-free-energy-estimators]]"
  - "[[wiki/tensions/TEN-0004-configuration-mapping-overlap-gain-vs-support-risk]]"
sources:
  - SRC-0012
  - SRC-0023
sensitivity: public
encryption: none
---

# Configuration Mapping Extends MBAR Through Warped Overlap

## Claim

Invertible configuration mappings can extend MBAR to transformations with poor or zero raw configuration overlap by evaluating mapped reduced potentials that include Jacobian corrections. [SRC-0012]

## Scope

This claim is limited to cases where a useful bijective map can be constructed and the mapped samples have adequate support for the estimator. The method keeps the MBAR equations but changes the reduced-potential inputs. [SRC-0012] [SRC-0023]

## Evidence

- SRC-0012 defines warped reduced energies with a mapping and Jacobian term, then applies the standard MBAR self-consistent equations to those warped energies. [SRC-0012, eqs. 1-2]
- SRC-0012 reports exact recovery in a mapped truncated-oscillator example and large efficiency gains in selected water-model and solvated-dipole transformations. [SRC-0012]

## Caveats

- Mapping construction becomes the limiting requirement, and gains depend on mapping quality and observable type. [SRC-0012]
- A mapping can improve raw overlap without guaranteeing well-behaved mapped support for every target observable. [SRC-0012]

## Links

- [[wiki/sources/SRC-0012-mbar-configuration-mapping]]
- [[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]
- [[wiki/concepts/mbar-with-configuration-mapping]]
- [[wiki/claims/CLM-0004-mbar-is-optimal-but-overlap-limited]]
- [[wiki/questions/overlap-support-diagnostics-for-free-energy-estimators]]
- [[wiki/tensions/TEN-0004-configuration-mapping-overlap-gain-vs-support-risk]]
