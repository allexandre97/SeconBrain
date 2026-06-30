---
type: concept
status: active
created: 2026-06-30
updated: 2026-06-30
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/scientific-modeling
  - research/data-management
  - research/molecular-simulation/datasets
  - research/machine-learning/molecular-modeling
  - research/biomolecules/proteins
tags:
  - datasets
  - machine-learning-potentials
  - quantum-chemistry
sources:
  - SRC-0042
  - SRC-0044
related:
  - "[[wiki/concepts/automated-force-field-training]]"
  - "[[wiki/concepts/stability-aware-mlff-training]]"
sensitivity: public
encryption: none
---

# Machine Learning Potential Datasets

## Summary

Machine-learning potential datasets provide quantum-chemistry energies, forces, structures, and sometimes auxiliary electronic properties for training ML models that approximate expensive electronic-structure calculations. SPICE targets drug-like molecules and protein-relevant chemistry; OMol25 expands scale, elements, charge/spin diversity, system size, and evaluation tasks. [SRC-0044] [SRC-0042]

## Key Points

- Dataset usefulness depends on both chemical-space coverage and conformational-space coverage. [SRC-0044]
- Forces are especially valuable because each conformation supplies many force components in addition to one energy. [SRC-0044]
- Consistent level of theory matters because heterogeneous quantum-chemistry labels can confound model training and evaluation. [SRC-0042] [SRC-0044]
- Charge and spin awareness are central for broader molecular chemistry datasets; OMol25 explicitly includes wide charge and spin variation. [SRC-0042]
- Practical evaluation should include downstream or domain-informed tasks, not only random-split energy and force errors. [SRC-0042]
- Overlay databanks address a complementary dataset problem: existing simulation trajectories can be made reusable for data-driven analyses by adding metadata, naming, quality-evaluation, and API layers without moving all raw data into one repository. [SRC-0057]

## Evidence

- SPICE reports more than 1.1 million conformations with DFT energies and forces for 15 elements. [SRC-0044]
- OMol25 reports more than 140 million DFT single-point calculations covering 83 elements, systems up to 350 atoms, and benchmark tasks such as conformer ranking, protonation, ionization, spin gaps, ligand-pocket interactions, and distance scaling. [SRC-0042]

## Links

- [[wiki/sources/SRC-0042-the-open-molecules-2025-omol25-dataset-evaluations-and]]
- [[wiki/sources/SRC-0044-spice-a-dataset-of-drug-like-molecules-and]]
- [[wiki/sources/SRC-0057-overlay-databank-unlocks-data-driven-analyses-of-biomolecules]]
- [[wiki/concepts/overlay-databanks-for-biomolecular-simulation-data]]
- [[wiki/concepts/automated-force-field-training]]
- [[wiki/concepts/stability-aware-mlff-training]]

## Open Questions

- Which dataset properties best predict downstream simulation stability and thermodynamic accuracy, beyond energy/force MAE?
