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
  - constraints
  - LINCS
  - SHAKE
  - molecular-dynamics
related:
  - "[[concepts/md-pressure-and-stress-tensor-calculation]]"
sources:
  - SRC-0052
sensitivity: public
encryption: none
---

# Molecular Dynamics Constraint Solvers

## Summary

Constraint solvers enforce fixed bond lengths or other holonomic constraints in MD, enabling larger time steps by removing high-frequency motions. LINCS is a linear constraint solver that resets constraints after an unconstrained step using a sparse constraint coupling matrix. [SRC-0052]

## Key Points

- Constraint equations are written as $g_h(r)=0$. [SRC-0052]
- The constraint gradient matrix $B$ collects the directions of the constraints and enters the constrained equations of motion. [SRC-0052]
- LINCS approximates the inverse of a sparse constraint coupling matrix with a power series and optionally applies rotation correction. [SRC-0052]
- LINCS was reported as three to four times faster than SHAKE at the same accuracy in the tested systems. [SRC-0052]
- Constraint contributions can matter for pressure tensor calculations in constrained periodic systems. [SRC-0051]

## Core equations

Constraint gradient:

$$
B_{hi} = \frac{\partial g_h}{\partial r_i}.
$$

Constrained equation form:

$$
-M\frac{d^2r}{dt^2} + B^T\lambda + f = 0.
$$

[SRC-0052]

## Links

- [[sources/SRC-0052-lincs-a-linear-constraint-solver-for-molecular-simulations]]
- [[concepts/md-pressure-and-stress-tensor-calculation]]
