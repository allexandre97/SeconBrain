---
type: concept
status: active
created: 2026-06-30
updated: 2026-06-30
areas:
  - research
categories:
  - research/molecular-simulation/datasets
  - research/data-management
  - research/biomolecules/lipids
tags:
  - overlay-databank
  - FAIR-data
  - biomolecular-simulation
  - machine-learning
related:
  - "[[wiki/concepts/machine-learning-potential-datasets]]"
  - "[[wiki/concepts/protein-force-field-benchmark-datasets]]"
  - "[[wiki/concepts/rna-molecular-dynamics-simulations]]"
sources:
  - SRC-0057
  - SRC-0058
sensitivity: public
encryption: none
---

# Overlay Databanks for Biomolecular Simulation Data

## Summary

An overlay databank makes scattered simulation data reusable by keeping raw data in stable public repositories while adding a standardized metadata, naming, quality-evaluation, and analysis layer. The NMRlipids Databank demonstrates this pattern for lipid bilayer MD simulations. [SRC-0057]

## Key Points

- The pattern separates storage of raw data from the curated index and analysis layer, reducing infrastructure cost while improving findability and reuse. [SRC-0057]
- Programmatic access depends on stable metadata, permanent raw-data links, and mappings from simulation-specific molecule/atom names to universal names. [SRC-0057] [SRC-0058]
- Quality-evaluated overlay databanks can support model selection, force-field evaluation, rare-event mining, and ML model training. [SRC-0057]
- A GUI broadens access for users without programming expertise, while an API enables automated analysis and downstream applications. [SRC-0057]
- The same architecture could apply to proteins, RNA, carbohydrates, or other biomolecular simulations if communities define analogous metadata and validation standards. [SRC-0057]

## Implementation Consequences

- Store enough provenance to locate raw trajectories, topology files, software, force fields, composition, temperature, trajectory length, warnings, and experimental references. [SRC-0058]
- Use universal naming/mapping layers so analyses can run across heterogeneous simulation packages and force fields. [SRC-0057] [SRC-0058]
- Keep application analyses separate from the core databank layer so new analyses can be developed without destabilizing the curated index. [SRC-0057]
- Treat ML predictions from the databank as conditional on current coverage and quality metrics, not as guaranteed physical truth. [SRC-0057]

## Links

- [[wiki/sources/SRC-0057-overlay-databank-unlocks-data-driven-analyses-of-biomolecules]]
- [[wiki/sources/SRC-0058-supplementary-information-for-overlay-databank-unlocks-data-driven]]
- [[wiki/concepts/machine-learning-potential-datasets]]
- [[wiki/concepts/protein-force-field-benchmark-datasets]]
