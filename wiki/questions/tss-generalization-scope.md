---
type: question
status: active
created: 2026-06-29
updated: 2026-07-01
question_status: partially-answered
areas:
  - research
categories:
  - research/statistics/monte-carlo
  - research/molecular-simulation/free-energy
tags:
  - validation
  - adaptive-sampling
  - free-energy-estimation
related:
  - "[[wiki/sources/SRC-0005-times-square-sampling-free-energy]]"
  - "[[wiki/sources/SRC-0006-times-square-sampling-supplement]]"
  - "[[wiki/concepts/times-square-sampling]]"
  - "[[wiki/concepts/on-the-fly-estimation-versus-mbar]]"
  - "[[wiki/concepts/tss-implementation-patterns]]"
  - "[[wiki/claims/CLM-0001-tss-self-adjustment-can-lower-variance]]"
  - "[[wiki/tensions/TEN-0001-tss-variance-advantage-vs-mbar-generalization]]"
sources:
  - SRC-0005
  - SRC-0006
sensitivity: public
encryption: none
---

# Times Square Sampling Generalization Scope

## Question

How broadly should Times Square Sampling's lower-variance, convergence, and resource-allocation claims be expected to transfer beyond the analyzed settings in the `times-square-sampling-2024` bundle? [SRC-0005] [SRC-0006]

## Context

SRC-0005 provides convergence theory under stated assumptions, an analytical self-adjustment comparison, and numerical evidence from a shifted-Gaussian example. SRC-0006 adds detailed proofs, programming recursions, and an aqueous-solution molecular dynamics example involving eight amino acid structures connected through alchemical paths. [SRC-0005] [SRC-0006]

The supplement strengthens the implementation and evidence base, but it does not turn the paper into broad validation across molecular systems, force fields, alchemical schedules, or hardware architectures. [SRC-0006, section 10]

## Current Position

Treat Times Square Sampling as a theoretically motivated adaptive free energy estimation framework with promising implementation mechanisms, not as a universally validated replacement for every existing free energy estimator. Claims about outperforming MBAR should remain tied to on-the-fly adaptive sampling settings where estimate information changes future samples and the theorem's assumptions are relevant. [SRC-0005, proposition 3] [SRC-0006, section 4.5]

## Validation Boundaries

- The convergence theorem depends on stated assumptions such as stability, gain-sequence conditions, and drift/ergodicity conditions. [SRC-0006, section 5]
- The MBAR variance comparison assumes the theorem's independent-sample and overlap-matrix conditions; practical MD samples are correlated. [SRC-0006, section 4.5]
- The aqueous-solution example is useful evidence for windowing, visit control, and self-adjustment, but it is one application family rather than a benchmark suite. [SRC-0006, section 10]
- Tuning choices such as `eta`, window size, history forgetting, regularization, and update frequency have documented tradeoffs and failure modes. [SRC-0006, sections 8-10]

## Links

- [[wiki/sources/SRC-0005-times-square-sampling-free-energy]]
- [[wiki/sources/SRC-0006-times-square-sampling-supplement]]
- [[wiki/concepts/times-square-sampling]]
- [[wiki/concepts/on-the-fly-estimation-versus-mbar]]
- [[wiki/concepts/tss-implementation-patterns]]
- [[wiki/claims/CLM-0001-tss-self-adjustment-can-lower-variance]]
- [[wiki/tensions/TEN-0001-tss-variance-advantage-vs-mbar-generalization]]
