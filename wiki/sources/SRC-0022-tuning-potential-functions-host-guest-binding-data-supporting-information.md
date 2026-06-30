---
type: source
status: active
created: 2026-06-30
updated: 2026-06-30
source_id: SRC-0022
source_path: raw/sources/SRC-0022-tuning-potential-functions-host-guest-binding-data-supporting.pdf
imported_path: raw/sources/SRC-0022-tuning-potential-functions-host-guest-binding-data-supporting.pdf
original_path: /lmb/home/alexandrebg/Documents/Papers/FF_train/ct3c01050_si_001.pdf
sha256: 67d0ff5c51327dd598abdf838c6d8a12e65edeb3529f2dd970dcebc177a9c822
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/computational-drug-discovery
tags:
  - supporting-information
  - host-guest
  - binding-free-energy
  - implicit-solvent
related:
  - "[[sources/SRC-0021-tuning-potential-functions-host-guest-binding-data]]"
  - "[[concepts/force-field-training-from-experimental-observables]]"
sources:
  - SRC-0022
sensitivity: public
encryption: none
ingestion_status: complete
coverage_profile: standard
---

# SRC-0022: Supporting Information for Tuning Potential Functions to Host-Guest Binding Data

## Source bundle

Supporting information for SRC-0021. [SRC-0021] [SRC-0022]

## Summary

This supporting information contains host-guest ABFE setup details, train/test complexes, binding free-energy tables, protein-ligand transfer benchmarks, hydration free-energy benchmarks, and prior-width sensitivity analysis for the OBC2 cavity-radius optimization in SRC-0021. [SRC-0022]

## Key Points

- The SI specifies host conformational restraints for cyclodextrins, cucurbiturils, and octa-acids. [SRC-0022]
- It provides the 36-system training set and 90-system test set binding free energies. [SRC-0022]
- It reports error statistics for host-guest training and test sets. [SRC-0022]
- It includes protein-ligand benchmark tables for different protein/ligand force-field combinations. [SRC-0022]
- It includes hydration free-energy benchmark error statistics showing the binding/HFE tradeoff discussed in the main text. [SRC-0022]
- The prior-width section explains how the Bayesian/prior penalty controls maximum parameter displacement in ForceBalance. [SRC-0022]

## Evidence

Figure S5 documents ForceBalance objective reduction over optimization and the evolution of selected GB cavity radii. [SRC-0022]

The prior-width analysis reports that reducing the parameter prior width restrains the fit and changes host-guest RMSE, illustrating the role of regularization. [SRC-0022]

## Links

- [[sources/SRC-0021-tuning-potential-functions-host-guest-binding-data]]
- [[concepts/force-field-training-from-experimental-observables]]
- [[questions/force-field-training-validation-scope]]

## Open Questions

- Which host classes dominate the optimized-radius direction and the hydration-free-energy failure mode? [SRC-0022]

## Ingestion QA

### Retrieval questions checked

- What ABFE setup details are provided?
- Where are train/test binding free energies tabulated?
- What protein-ligand and hydration benchmarks are included?
- How is prior-width sensitivity discussed?

### Coverage decision

Complete at `coverage_profile: standard` as a supporting-information source. [SRC-0022]

### Known gaps

- Large numeric tables are summarized rather than transcribed.
