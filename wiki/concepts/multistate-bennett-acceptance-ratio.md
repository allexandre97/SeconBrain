---
type: concept
status: active
created: 2026-06-30
updated: 2026-06-30
areas:
  - research
categories:
  - research/molecular-simulation/free-energy
  - research/statistics/monte-carlo
tags:
  - mbar
  - free-energy-estimation
  - reweighting
  - bridge-sampling
  - math-heavy
related:
  - "[[sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]"
  - "[[concepts/free-energy-estimation]]"
  - "[[concepts/mbar-with-configuration-mapping]]"
sources:
  - SRC-0023
sensitivity: public
encryption: none
---

# Multistate Bennett Acceptance Ratio

## Summary

The multistate Bennett acceptance ratio, MBAR, is a statistically efficient estimator for free energy differences and expectations from samples collected at multiple equilibrium states. It estimates ratios of normalizing constants using all cross-evaluated reduced potentials. [SRC-0023]

## Key Points

- MBAR reduces to BAR when only two sampled states are considered. [SRC-0023]
- MBAR is equivalent to WHAM in the limit of zero-width histogram bins, but avoids explicit histogram discretization. [SRC-0023]
- The estimator needs $u_k(x_n)$, the reduced potential of every retained sample evaluated at every state included in the estimate. [SRC-0023]
- The solved free energies are only defined up to a common additive constant. [SRC-0023]
- Additional unsampled states can be included with $N_i=0$ after solving the sampled-state equations. [SRC-0023]
- The asymptotic covariance matrix supports uncertainty propagation for free energy differences, expectations, and PMFs. [SRC-0023]

## Core equations

Self-consistent MBAR equation:

$$
\hat f_i=
-\log\sum_{j=1}^{K}\sum_{n=1}^{N_j}
\frac{\exp[-u_i(x_{jn})]}
{\sum_{k=1}^{K}N_k\exp[\hat f_k-u_k(x_{jn})]}.
$$

[SRC-0023]

Free-energy-difference uncertainty:

$$
\delta^2\Delta \hat f_{ij}
=
\hat\Theta_{ii}-2\hat\Theta_{ij}+\hat\Theta_{jj}.
$$

[SRC-0023]

Expectation estimator:

$$
\hat A=
\sum_{n=1}^{N}W_{na}A(x_n).
$$

[SRC-0023]

## Variable glossary

- $K$: number of thermodynamic states in the MBAR system. [SRC-0023]
- $N_i$: number of samples drawn from state $i$; unsampled targets may have $N_i=0$. [SRC-0023]
- $u_i(x)$: reduced potential for state $i$. [SRC-0023]
- $f_i$: dimensionless free energy, defined up to a constant. [SRC-0023]
- $W_{ni}$: normalized MBAR weight of sample $n$ for state $i$. [SRC-0023]
- $\hat\Theta$: asymptotic covariance matrix for log normalization constants. [SRC-0023]

## Implementation consequences

MBAR is natural for alchemical free energies, umbrella sampling, parallel tempering analysis, and any setting where samples from several biased equilibrium states can be evaluated under all relevant reduced potentials. [SRC-0023]

Correlated trajectories should be decorrelated or subsampled before using the asymptotic covariance estimator, otherwise uncertainty can be underestimated. [SRC-0023]

## Caveats

MBAR is statistically optimal within its assumptions, but the assumptions do not guarantee adequate phase-space overlap. Low-overlap states can still give unstable or high-variance estimates. [SRC-0023]

## Links

- [[sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]
- [[concepts/free-energy-estimation]]
- [[concepts/mbar-with-configuration-mapping]]
- [[concepts/on-the-fly-estimation-versus-mbar]]

## Open Questions

- Which overlap and influence diagnostics should accompany MBAR estimates by default? [SRC-0023]
