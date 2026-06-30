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
  - configuration-mapping
  - reweighting
  - phase-space-overlap
  - math-heavy
related:
  - "[[wiki/sources/SRC-0012-mbar-configuration-mapping]]"
  - "[[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]"
  - "[[wiki/concepts/free-energy-estimation]]"
  - "[[wiki/concepts/multistate-bennett-acceptance-ratio]]"
sources:
  - SRC-0012
  - SRC-0023
sensitivity: public
encryption: none
---

# MBAR with Configuration Mapping

## Summary

MBAR with configuration mapping extends multistate reweighting to thermodynamic states whose raw configuration spaces have poor or zero overlap. It maps configurations between states with an invertible transformation and includes the Jacobian in a warped reduced energy before applying MBAR. [SRC-0012]

## Key Points

- Reweighting fails when sampled configurations from one state have zero probability in another state. [SRC-0012]
- A bijective map $T_{ij}$ can transform samples from state $i$ into configurations in state $j$. [SRC-0012]
- The mapping changes volume, so the Jacobian determinant is part of the reduced potential. [SRC-0012, eq. 1]
- After constructing all warped reduced energies, the normal MBAR equations can be solved. [SRC-0012, eq. 2]

## Core equations

$$
u_{ij}^{w}(x_j)=u_i(T_{ji}(x_j))-\log|J_{ji}(x_j)|.
$$

$$
f_i=-\log\sum_{j,n}
\frac{\exp[-u_{ij}^{w}(x_{jn})]}
{\sum_k N_k\exp[f_k-u_{kj}^{w}(x_{jn})]}.
$$

## Implementation consequences

- The method is most useful when geometry changes cause poor overlap but a physically reasonable invertible mapping is available. [SRC-0012]
- Mapping can reduce required samples by orders of magnitude, but mapping construction becomes the hard part. [SRC-0012]
- It can estimate free energies and other expectations using the same formalism. [SRC-0012]

## Caveats

- Bad mappings may improve overlap only weakly or introduce difficult energy distributions. [SRC-0012]
- The method does not remove the need to validate thermodynamic cycles or statistical uncertainty. [SRC-0012]

## Links

- [[wiki/sources/SRC-0012-mbar-configuration-mapping]]
- [[wiki/sources/SRC-0023-statistically-optimal-analysis-multiple-equilibrium-states-mbar]]
- [[wiki/concepts/free-energy-estimation]]
- [[wiki/concepts/multistate-bennett-acceptance-ratio]]

## Open Questions

- Can robust automated mappings be built for flexible molecules with changing topology or symmetry? [SRC-0012]
