---
type: concept
status: active
created: 2026-06-30
updated: 2026-06-30
areas:
  - research
categories:
  - research/molecular-simulation/free-energy
tags:
  - solvation-free-energy
  - LAMMPS
  - thermodynamic-integration
  - decoupling
related:
  - "[[concepts/free-energy-estimation]]"
sources:
  - SRC-0047
sensitivity: public
encryption: none
---

# Solvation Free Energy Decoupling in LAMMPS

## Summary

Solvation free energy decoupling in LAMMPS can be implemented by staging solute-solvent Lennard-Jones and Coulomb interactions while preserving intramolecular solute interactions through an overlay correction. [SRC-0047]

## Key Points

- Decoupling differs from annihilation by keeping the solute's intramolecular interactions active while changing only solute-environment interactions. [SRC-0047]
- In LAMMPS, solute charge scaling is useful for long-range electrostatics but undesirably scales intramolecular solute Coulomb interactions. [SRC-0047]
- The overlay correction adds back the missing intramolecular Coulomb energy so that charge-scaled staging preserves the isolated-solute internal energy. [SRC-0047, eq. 7]
- The demonstrated workflow uses thermodynamic integration and Gauss-Legendre quadrature, but the correction is estimator-independent in principle. [SRC-0047]

## Core equations

The correction adds:

$$
U_{\mathrm{coul}}^{\mathrm{overlay}}(r_{ij};\lambda_q)
=
U_{\mathrm{coul}}^{\mathrm{intra}}(r_{ij})
-
U_{\mathrm{coul}}^{\mathrm{intra,scaled}}(r_{ij};\lambda_q).
$$

With charges scaled by $\lambda_q$, this becomes:

$$
U_{\mathrm{coul}}^{\mathrm{overlay}}(r_{ij};\lambda_q)
=
\frac{1-\lambda_q^2}{\lambda_q^2}
U_{\mathrm{coul}}^{\mathrm{intra,scaled}}(r_{ij};\lambda_q).
$$

[SRC-0047, eq. 7]

## Implementation Consequences

- Use a separate overlay term for intramolecular solute electrostatics when using scaled charges to stage solute-solvent Coulomb interactions. [SRC-0047]
- Validate implementation by comparing both total free energies and $\langle dU/d\lambda\rangle_\lambda$ integrands against a code with built-in decoupling support when possible. [SRC-0047]
- Treat small test systems as implementation checks, not as evidence of broad accuracy for all solvents, solutes, or force fields. [SRC-0047]

## Links

- [[sources/SRC-0047-performing-solvation-free-energy-calculations-in-lammps-using]]
- [[concepts/free-energy-estimation]]
