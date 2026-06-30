---
type: concept
status: active
created: 2026-06-30
updated: 2026-06-30
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
tags:
  - water-models
  - opc
  - multipoles
sources:
  - SRC-0027
  - SRC-0028
related:
  - "[[concepts/automated-force-field-training]]"
sensitivity: public
encryption: none
---

# OPC Water Model

## Summary

OPC is a rigid fixed-charge water model built by optimizing a three-point charge distribution to reproduce low-order electrostatic multipole moments before fitting nonbonded parameters for liquid-water behavior. [SRC-0027]

## Key Points

- OPC abandons conventional water-geometry constraints except symmetry in the charge-placement problem. [SRC-0027]
- The model exactly reproduces the dipole and quadrupole constraints used in its construction and optimally approximates octupole moments. [SRC-0027] [SRC-0028]
- It reports strong agreement across bulk water properties and improved small-molecule hydration free energies relative to common rigid water models. [SRC-0027]

## Core equations

$$
\mu=2q(z_2-z_1),
\qquad
Q_T=\frac{3qy^2}{2}.
$$

[SRC-0027]

## Caveats

OPC remains a nonpolarizable fixed-charge model, so its accuracy is bounded by the representational limits of rigid point charges. [SRC-0027]

## Links

- [[sources/SRC-0027-building-water-models-different-approach-opc]]
- [[sources/SRC-0028-building-water-models-different-approach-supporting-information]]
- [[concepts/automated-force-field-training]]
