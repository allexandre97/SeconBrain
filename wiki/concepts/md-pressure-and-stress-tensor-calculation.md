---
type: concept
status: active
created: 2026-06-30
updated: 2026-06-30
areas:
  - research
categories:
  - research/molecular-simulation/molecular-dynamics
tags:
  - pressure-tensor
  - stress-tensor
  - virial
  - periodic-boundary-conditions
related:
  - "[[concepts/particle-mesh-ewald-and-long-range-electrostatics]]"
sources:
  - SRC-0048
  - SRC-0051
sensitivity: public
encryption: none
---

# MD Pressure and Stress Tensor Calculation

## Summary

Pressure and stress tensor calculation in MD requires consistent virial contributions from interatomic forces, constraints, periodic images, and long-range electrostatics. The central implementation challenge is making the formula match the potential and boundary conditions actually used by the simulation. [SRC-0048] [SRC-0051]

## Key Points

- For arbitrary many-body potentials, force-based virial formulas are preferable to pair-decomposition formulas because the potential may not split naturally into pair terms. [SRC-0048]
- Atom-cell, atom, and group virial forms can be mathematically equivalent while serving different implementation needs. [SRC-0048]
- Constrained periodic molecular systems with Ewald electrostatics can require hybrid mechanical/thermodynamic pressure tensor contributions. [SRC-0051]
- Pressure tensor components can be sensitive diagnostics for force-field parameters, sometimes more sensitive than energy alone. [SRC-0051]

## Core equations

Scalar pressure relation:

$$
P = \frac{N k_B T}{V} + \frac{\langle W \rangle}{3V}.
$$

[SRC-0048, eq. 1]

Thermodynamic virial definition:

$$
W(r^N) = -3V \frac{dU}{dV}.
$$

[SRC-0048, eq. 2]

## Links

- [[sources/SRC-0048-general-formulation-of-pressure-and-stress-tensor-for]]
- [[sources/SRC-0051-a-general-pressure-tensor-calculation-for-molecular-dynamics]]
- [[concepts/particle-mesh-ewald-and-long-range-electrostatics]]
