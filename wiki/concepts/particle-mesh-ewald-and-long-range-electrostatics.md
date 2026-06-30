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
  - PME
  - Ewald-summation
  - electrostatics
  - PSWF
related:
  - "[[wiki/concepts/free-energy-estimation]]"
  - "[[wiki/concepts/md-pressure-and-stress-tensor-calculation]]"
sources:
  - SRC-0050
  - SRC-0054
sensitivity: public
encryption: none
---

# Particle Mesh Ewald and Long-range Electrostatics

## Summary

Particle Mesh Ewald methods split electrostatic interactions into short-range real-space and long-range reciprocal-space terms, then use gridding and FFTs to make periodic long-range electrostatics practical for large MD systems. [SRC-0050]

## Key Points

- Smooth PME uses B-spline interpolation of reciprocal-space structure factors, yielding smooth forces and analytic gradients at controllable accuracy. [SRC-0050]
- PME/PPPM reduce the cost of long-range Coulomb interactions but still require global FFT communication, which becomes a scaling bottleneck. [SRC-0054]
- ESP replaces Gaussian/B-spline choices with prolate-spheroidal-wave-function kernels to reduce Fourier grid size and communication for a target accuracy. [SRC-0054]
- Long-range electrostatics choices interact with virial/stress calculations because reciprocal-space terms contribute to pressure tensors. [SRC-0050] [SRC-0051]

## Core equations

Ewald energy split:

$$
E = E_{\mathrm{dir}} + E_{\mathrm{rec}} + E_{\mathrm{corr}}.
$$

[SRC-0050]

Electrostatic structure factor:

$$
S(m) =
\sum_{j=1}^{N}
q_j \exp\left(2\pi i\,m\cdot r_j\right).
$$

[SRC-0050, eq. 2.2]

## Links

- [[wiki/sources/SRC-0050-a-smooth-particle-mesh-ewald-method]]
- [[wiki/sources/SRC-0054-accelerating-molecular-dynamics-simulations-using-fast-ewald-summation]]
- [[wiki/concepts/md-pressure-and-stress-tensor-calculation]]
