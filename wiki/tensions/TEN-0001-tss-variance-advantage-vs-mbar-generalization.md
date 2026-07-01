---
type: tension
status: active
created: 2026-07-01
updated: 2026-07-01
tension_status: active
areas:
  - research
categories:
  - research/statistics/monte-carlo
  - research/molecular-simulation/free-energy
  - research/adaptive-sampling
tags:
  - tension
  - times-square-sampling
  - mbar
related:
  - "[[wiki/concepts/on-the-fly-estimation-versus-mbar]]"
  - "[[wiki/concepts/free-energy-estimation]]"
related_claims:
  - "[[wiki/claims/CLM-0001-tss-self-adjustment-can-lower-variance]]"
related_questions:
  - "[[wiki/questions/tss-generalization-scope]]"
sources:
  - SRC-0005
  - SRC-0006
sensitivity: public
encryption: none
---

# TSS Variance Advantage Versus MBAR Generalization

## Tension

TSS has a formal lower-variance comparison against MBAR in the analyzed adaptive on-the-fly setting, but that result should not be generalized to every MBAR use case or every practical molecular-dynamics regime. [SRC-0005, proposition 3] [SRC-0006, section 4.5]

## Positions

- The TSS source bundle supports a variance advantage when the sampler can self-adjust using current estimates and the theorem's assumptions apply. [SRC-0005, proposition 3] [SRC-0006, section 4.5]
- The same source bundle leaves practical transfer bounded by assumptions about sampling, overlap, correlation, and broader molecular validation. [SRC-0006, sections 4.5 and 10]

## Why it matters

Future answers comparing TSS and MBAR should preserve the distinction between adaptive sampling-time estimation and post hoc MBAR analysis.

## Resolution status

Active. Broader empirical benchmarking and careful matching of estimator assumptions are still needed. [SRC-0005] [SRC-0006]

## Links

- [[wiki/claims/CLM-0001-tss-self-adjustment-can-lower-variance]]
- [[wiki/questions/tss-generalization-scope]]
- [[wiki/concepts/on-the-fly-estimation-versus-mbar]]
