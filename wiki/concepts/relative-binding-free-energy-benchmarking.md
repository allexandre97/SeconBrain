---
type: concept
status: active
created: 2026-06-29
updated: 2026-06-29
areas:
  - research
categories:
  - research/molecular-simulation/binding-free-energy
tags:
  - rbfe
  - drug-discovery
related:
  - "[[concepts/garnet-force-field]]"
sources:
  - SRC-0003
sensitivity: public
encryption: none
---

# Relative Binding Free Energy Benchmarking

## Summary

Relative binding free energy benchmarking evaluates how well simulations rank or predict ligand binding differences against experimental binding data. [SRC-0003]

## Key Points

- SRC-0003 evaluates Garnet on 8 systems from a public OpenFE benchmark set. [SRC-0003]
- The authors modified OpenFE to support the double exponential potential and related soft-core potential. [SRC-0003]
- Garnet is reported as broadly comparable to OpenFE on the tested systems, with a chk1 outlier noted. [SRC-0003]
- The benchmark is limited relative to the full 58-system public benchmark set. [SRC-0003]

## Links

- [[sources/SRC-0003-training-a-force-field-from-scratch]]
- [[concepts/garnet-force-field]]
- [[questions/garnet-validation-scope]]
