---
type: tension
status: active
created: 2026-07-01
updated: 2026-07-01
tension_status: active
areas:
  - research
categories:
  - research/adaptive-sampling
  - research/molecular-simulation/free-energy
  - research/statistics/monte-carlo
tags:
  - tension
  - adaptive-sampling
  - diagnostics
  - mbar
related:
  - "[[wiki/concepts/adaptive-enhanced-sampling]]"
  - "[[wiki/concepts/free-energy-estimation]]"
related_claims:
  - "[[wiki/claims/CLM-0006-opes-reconstructs-probability-to-derive-bias]]"
  - "[[wiki/claims/CLM-0007-awh-updates-bias-from-conditional-histograms]]"
  - "[[wiki/claims/CLM-0008-ladybugs-couples-gibbs-sampling-with-fastmbar-bias-updates]]"
related_questions:
  - "[[wiki/questions/adaptive-estimators-vs-fixed-sample-estimators]]"
  - "[[wiki/questions/overlap-support-diagnostics-for-free-energy-estimators]]"
sources:
  - SRC-0007
  - SRC-0008
  - SRC-0009
  - SRC-0010
  - SRC-0011
  - SRC-0013
  - SRC-0023
sensitivity: public
encryption: none
---

# On-the-Fly Bias Adaptation Versus Postprocessing Diagnostics

## Tension

On-the-fly bias adaptation can improve exploration by changing future samples, but it complicates comparison with reproducible fixed-sample postprocessing diagnostics such as MBAR overlap and uncertainty checks. [SRC-0007] [SRC-0010] [SRC-0013] [SRC-0023]

## Positions

- AWH, OPES, and LaDyBUGS all use information gathered during a run to update future biasing or state-sampling behavior. [SRC-0007] [SRC-0010] [SRC-0013]
- MBAR-style postprocessing provides a clear fixed-sample estimator and uncertainty framework, but it does not by itself solve poor sampling or missing support. [SRC-0023]

## Why it matters

Future method comparisons should separate two questions: whether adaptation generated better samples, and whether the final estimator diagnostics support the reported free energies.

## Resolution status

Active. Adaptive methods still need reproducible diagnostics that account for adaptation history, overlap/support, and uncertainty estimation. [SRC-0009] [SRC-0011] [SRC-0013] [SRC-0023]

## Links

- [[wiki/claims/CLM-0006-opes-reconstructs-probability-to-derive-bias]]
- [[wiki/claims/CLM-0007-awh-updates-bias-from-conditional-histograms]]
- [[wiki/claims/CLM-0008-ladybugs-couples-gibbs-sampling-with-fastmbar-bias-updates]]
- [[wiki/questions/adaptive-estimators-vs-fixed-sample-estimators]]
- [[wiki/questions/overlap-support-diagnostics-for-free-energy-estimators]]
- [[wiki/concepts/adaptive-enhanced-sampling]]
- [[wiki/concepts/free-energy-estimation]]
