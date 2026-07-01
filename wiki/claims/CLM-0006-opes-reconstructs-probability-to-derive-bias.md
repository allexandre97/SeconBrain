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
  - research/adaptive-sampling
  - research/molecular-simulation/free-energy
tags:
  - claim
  - opes
  - metadynamics
  - probability-reconstruction
related:
  - "[[wiki/sources/SRC-0010-rethinking-metadynamics-opes]]"
  - "[[wiki/sources/SRC-0011-opes-supporting-information]]"
  - "[[wiki/concepts/on-the-fly-probability-enhanced-sampling]]"
  - "[[wiki/questions/adaptive-estimators-vs-fixed-sample-estimators]]"
  - "[[wiki/tensions/TEN-0005-on-the-fly-bias-adaptation-vs-postprocessing-diagnostics]]"
sources:
  - SRC-0010
  - SRC-0011
sensitivity: public
encryption: none
---

# OPES Derives Bias From Probability Reconstruction

## Claim

OPES reframes metadynamics-like enhanced sampling as on-the-fly reconstruction of a collective-variable probability distribution, then derives the bias from the estimated probability and an explicit target distribution. [SRC-0010]

## Scope

This claim covers the OPES main paper and supporting information. It is not evidence that OPES removes the need for meaningful collective variables or that every target distribution is equally useful. [SRC-0010] [SRC-0011]

## Evidence

- SRC-0010 defines a target-distribution bias, a weighted kernel probability estimate, explored-region normalization, and a regularized OPES bias. [SRC-0010, eqs. 4-8]
- SRC-0011 gives implementation details for compressed kernels, bandwidth rescaling, effective sample size, normalization, and barrier-based bias caps. [SRC-0011]

## Caveats

- OPES still depends on collective-variable choice, and the source bundle focuses mainly on well-tempered and flat targets. [SRC-0010]
- Kernel compression and bandwidth schedules add implementation tradeoffs rather than eliminating diagnostics. [SRC-0011]

## Links

- [[wiki/sources/SRC-0010-rethinking-metadynamics-opes]]
- [[wiki/sources/SRC-0011-opes-supporting-information]]
- [[wiki/concepts/on-the-fly-probability-enhanced-sampling]]
- [[wiki/questions/adaptive-estimators-vs-fixed-sample-estimators]]
- [[wiki/tensions/TEN-0005-on-the-fly-bias-adaptation-vs-postprocessing-diagnostics]]
