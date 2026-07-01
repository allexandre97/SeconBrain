---
type: claim
status: active
created: 2026-07-01
updated: 2026-07-01
claim_status: limited
claim_scope: local
areas:
  - research
categories:
  - research/statistics/monte-carlo
  - research/molecular-simulation/free-energy
  - research/adaptive-sampling
tags:
  - claim
  - times-square-sampling
  - free-energy-estimation
related:
  - "[[wiki/concepts/times-square-sampling]]"
  - "[[wiki/concepts/on-the-fly-estimation-versus-mbar]]"
  - "[[wiki/questions/tss-generalization-scope]]"
  - "[[wiki/tensions/TEN-0001-tss-variance-advantage-vs-mbar-generalization]]"
sources:
  - SRC-0005
  - SRC-0006
sensitivity: public
encryption: none
---

# TSS Self-Adjustment Can Lower Variance

## Claim

Times Square Sampling can have lower asymptotic variance than MBAR in the paper's on-the-fly adaptive setting, because current estimates influence future sampling. [SRC-0005, proposition 3] [SRC-0006, section 4.5]

## Scope

This is a local, limited claim for the `times-square-sampling-2024` bundle. It should not be read as a blanket claim that MBAR is inferior in all post-processing or molecular-simulation settings. [SRC-0005, proposition 3] [SRC-0006, section 4.5]

## Evidence

- SRC-0005 states the variance comparison as a formal proposition for the analyzed on-the-fly estimator setting. [SRC-0005, proposition 3]
- SRC-0006 derives the covariance comparison under its overlap-matrix and independent-sample assumptions. [SRC-0006, section 4.5]

## Caveats

- Practical molecular dynamics samples are correlated, and the theorem's assumptions are not automatic in arbitrary simulations. [SRC-0006, section 4.5]
- The wiki records a separate validation-boundary question for how broadly this result should transfer. [SRC-0005] [SRC-0006]

## Links

- [[wiki/sources/SRC-0005-times-square-sampling-free-energy]]
- [[wiki/sources/SRC-0006-times-square-sampling-supplement]]
- [[wiki/concepts/on-the-fly-estimation-versus-mbar]]
- [[wiki/questions/tss-generalization-scope]]
- [[wiki/tensions/TEN-0001-tss-variance-advantage-vs-mbar-generalization]]
