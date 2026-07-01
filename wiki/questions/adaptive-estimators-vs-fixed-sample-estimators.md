---
type: question
status: active
created: 2026-07-01
updated: 2026-07-01
question_status: open
areas:
  - research
categories:
  - research/adaptive-sampling
  - research/molecular-simulation/free-energy
  - research/statistics/monte-carlo
tags:
  - question
  - adaptive-sampling
  - mbar
  - free-energy-estimation
related:
  - "[[wiki/concepts/free-energy-estimation]]"
  - "[[wiki/concepts/adaptive-enhanced-sampling]]"
  - "[[wiki/concepts/on-the-fly-estimation-versus-mbar]]"
  - "[[wiki/claims/CLM-0001-tss-self-adjustment-can-lower-variance]]"
  - "[[wiki/claims/CLM-0004-mbar-is-optimal-but-overlap-limited]]"
  - "[[wiki/tensions/TEN-0001-tss-variance-advantage-vs-mbar-generalization]]"
  - "[[wiki/tensions/TEN-0005-on-the-fly-bias-adaptation-vs-postprocessing-diagnostics]]"
sources:
  - SRC-0005
  - SRC-0006
  - SRC-0007
  - SRC-0009
  - SRC-0010
  - SRC-0013
  - SRC-0023
sensitivity: public
encryption: none
---

# Adaptive Estimators Versus Fixed-Sample Estimators

## Question

When do adaptive free-energy estimators outperform fixed-sample estimators such as MBAR, and when is the comparison unfair because the methods receive different sampling information? [SRC-0005] [SRC-0006] [SRC-0023]

## Context

TSS makes a formal lower-variance comparison to MBAR in an on-the-fly setting where current estimates influence future samples. AWH, OPES, and LaDyBUGS also adapt sampling during a run, while MBAR is primarily a fixed-sample postprocessing estimator that efficiently uses already collected samples. [SRC-0005] [SRC-0007] [SRC-0010] [SRC-0013] [SRC-0023]

## Current Position

Treat adaptive-versus-fixed comparisons as statements about sampling protocols, not only estimator formulas. Adaptive methods may outperform when feedback changes future samples in useful ways; MBAR remains the appropriate fixed-sample baseline when the sample set and reduced-potential evaluations already cover the relevant states. [SRC-0005] [SRC-0009] [SRC-0023]

## Validation Boundaries

- TSS's strongest variance claim depends on independent-sample and overlap-matrix assumptions. [SRC-0006, section 4.5]
- AWH is not expected to dramatically outperform BAR/MBAR when intermediate-state sampling is already efficient. [SRC-0009, conclusion]
- OPES and LaDyBUGS change the sampled distribution during a run, so postprocessing diagnostics still need to be interpreted alongside adaptation history. [SRC-0010] [SRC-0013]
- MBAR remains overlap-limited even when statistically efficient for a fixed sample set. [SRC-0023]

## Links

- [[wiki/concepts/free-energy-estimation]]
- [[wiki/concepts/adaptive-enhanced-sampling]]
- [[wiki/concepts/on-the-fly-estimation-versus-mbar]]
- [[wiki/claims/CLM-0001-tss-self-adjustment-can-lower-variance]]
- [[wiki/claims/CLM-0004-mbar-is-optimal-but-overlap-limited]]
- [[wiki/tensions/TEN-0001-tss-variance-advantage-vs-mbar-generalization]]
- [[wiki/tensions/TEN-0005-on-the-fly-bias-adaptation-vs-postprocessing-diagnostics]]
