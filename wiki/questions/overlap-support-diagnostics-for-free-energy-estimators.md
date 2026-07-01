---
type: question
status: active
created: 2026-07-01
updated: 2026-07-01
question_status: open
areas:
  - research
categories:
  - research/molecular-simulation/free-energy
  - research/statistics/monte-carlo
  - research/adaptive-sampling
tags:
  - question
  - overlap
  - support
  - diagnostics
related:
  - "[[wiki/concepts/free-energy-estimation]]"
  - "[[wiki/concepts/multistate-bennett-acceptance-ratio]]"
  - "[[wiki/concepts/mbar-with-configuration-mapping]]"
  - "[[wiki/claims/CLM-0004-mbar-is-optimal-but-overlap-limited]]"
  - "[[wiki/claims/CLM-0005-configuration-mapping-extends-mbar]]"
  - "[[wiki/tensions/TEN-0004-configuration-mapping-overlap-gain-vs-support-risk]]"
sources:
  - SRC-0005
  - SRC-0006
  - SRC-0012
  - SRC-0013
  - SRC-0023
sensitivity: public
encryption: none
---

# Overlap and Support Diagnostics for Free Energy Estimators

## Question

How should overlap and support be diagnosed across fixed-sample MBAR, mapped MBAR, and adaptive estimators whose sampling distributions change during the run? [SRC-0012] [SRC-0023]

## Context

MBAR needs adequate phase-space overlap in the collected sample set. Configuration mapping can transform samples to improve overlap before MBAR, but mapped support still needs validation. Adaptive methods such as TSS and LaDyBUGS generate samples under changing estimates or biases, so support diagnostics must account for how samples were produced. [SRC-0005] [SRC-0012] [SRC-0013] [SRC-0023]

## Current Position

Use overlap/support diagnostics as a cross-method validation requirement, not as an MBAR-only concern. The diagnostic details may differ, but the underlying question is whether the estimator is supported by samples that cover the relevant thermodynamic states after any biasing or mapping transformations. [SRC-0012] [SRC-0023]

## Validation Boundaries

- Standard MBAR can be unstable or high-variance when target states have poor support in sampled configurations. [SRC-0023]
- Configuration mapping helps only when the map produces useful warped overlap and includes the correct Jacobian correction. [SRC-0012]
- TSS variance comparisons use an overlap-matrix condition that is not automatic in correlated molecular dynamics. [SRC-0006, section 4.5]
- LaDyBUGS evaluates all lambda-state energies for MBAR-style updates, but coordinate sampling within conditional MD segments still matters. [SRC-0013]

## Links

- [[wiki/concepts/free-energy-estimation]]
- [[wiki/concepts/multistate-bennett-acceptance-ratio]]
- [[wiki/concepts/mbar-with-configuration-mapping]]
- [[wiki/claims/CLM-0004-mbar-is-optimal-but-overlap-limited]]
- [[wiki/claims/CLM-0005-configuration-mapping-extends-mbar]]
- [[wiki/tensions/TEN-0004-configuration-mapping-overlap-gain-vs-support-risk]]
