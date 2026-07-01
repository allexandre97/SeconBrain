---
type: concept
status: active
created: 2026-07-01
updated: 2026-07-01
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/molecular-simulation/free-energy
  - research/machine-learning/molecular-modeling
  - research/experimental-benchmarking
  - research/statistics/monte-carlo
tags:
  - validation
  - transferability
  - benchmarking
  - molecular-simulation
related:
  - "[[wiki/questions/force-field-training-validation-scope]]"
  - "[[wiki/concepts/automated-force-field-training]]"
  - "[[wiki/concepts/machine-learning-potential-datasets]]"
  - "[[wiki/concepts/machine-learned-interatomic-potential-foundation-models]]"
  - "[[wiki/concepts/stability-aware-mlff-training]]"
  - "[[wiki/concepts/free-energy-estimation]]"
  - "[[wiki/concepts/relative-binding-free-energy-benchmarking]]"
  - "[[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]"
sources:
  - SRC-0005
  - SRC-0006
  - SRC-0007
  - SRC-0008
  - SRC-0009
  - SRC-0014
  - SRC-0016
  - SRC-0018
  - SRC-0019
  - SRC-0020
  - SRC-0021
  - SRC-0023
  - SRC-0024
  - SRC-0025
  - SRC-0042
  - SRC-0044
  - SRC-0046
  - SRC-0059
  - SRC-0060
  - SRC-0061
  - SRC-0062
sensitivity: public
encryption: none
---

# Cross-Domain Validation Problems in Molecular Simulation

## Summary

Force-field fitting, machine-learning potentials, and free-energy estimators repeatedly fail validation for the same structural reasons: training-set success is mistaken for transfer, static metrics are mistaken for simulation reliability, sampling support is overestimated, uncertainty is underreported, benchmarks are too curated, and error sources are hard to identify. These problems differ in implementation detail, but they share a common validation logic: a method must be tested on the downstream system, observable, timescale, and statistical regime where it will be used. [SRC-0014] [SRC-0021] [SRC-0024] [SRC-0059] [SRC-0061]

## Recurring Problems

- **Transfer beyond fitted data:** Force-field fitting can improve one observable while degrading another, as in host-guest binding improvements with hydration-free-energy degradation or SAXS lipid fits with solvent-stress transfer limits. Machine-learning potential datasets also require downstream or domain-informed evaluation beyond random energy and force splits. [SRC-0014] [SRC-0021] [SRC-0042] [SRC-0044]
- **Simulation-level validity:** Low energy or force error does not guarantee stable or physically accurate dynamics. Stability-aware training and biology-focused foundation-model validation both add downstream molecular-dynamics tests because static structure metrics are insufficient. [SRC-0024] [SRC-0060]
- **Sampling support and overlap:** Reweighting, Multistate Bennett acceptance ratio estimators, and generated-sample free-energy methods depend on overlap between the reference samples and the target distribution. Effective sample size and related checks detect weight concentration, but they do not prove that all important conformations were sampled. [SRC-0016] [SRC-0018] [SRC-0020] [SRC-0023]
- **Estimator assumptions versus practical trajectories:** Adaptive and postprocessing free-energy estimators have formal assumptions about overlap, decorrelation, stability, gain sequences, and ergodicity. Practical molecular-dynamics trajectories are correlated and can mix poorly, so theoretical variance or convergence claims need matched empirical checks. [SRC-0005] [SRC-0006] [SRC-0023]
- **Benchmark representativeness:** Curated public benchmarks can overstate prospective performance. OpenFE public benchmark accuracy was better than blinded private active-project accuracy, and retrospective FEP benchmarks can be easier than prospective drug-discovery use because of selection and expert setup effects. [SRC-0046] [SRC-0061]
- **Uncertainty and repeatability:** Single adaptive runs or single benchmark summaries can hide uncertainty. The AWH validation page records that independent repeats remain important, while OpenFE supporting information records repeat, convergence, redundant-edge, and edge-difficulty diagnostics. [SRC-0009] [SRC-0062]
- **Error-source identifiability:** Experiment-simulation mismatch can be explained by force-field error, ensemble error, forward-model error, sampling error, or noisy experimental data. Regularization and cross-validation help but do not eliminate this ambiguity. [SRC-0019] [SRC-0020] [SRC-0046]
- **Benchmark metric design:** Edgewise, random-split, or aggregate metrics can reward the wrong behavior. All-to-all pairwise relative binding free-energy metrics better represent arbitrary ligand comparisons than edgewise transformations, and machine-learned interatomic potential foundation models need pragmatic downstream tasks rather than single-metric dominance. [SRC-0059] [SRC-0061]

## Evidence

- The force-field training validation page summarizes that strong claims require held-out systems, held-out observables, resimulation or independent recalculation, and explicit diagnostics for support or regularization. [SRC-0014] [SRC-0016] [SRC-0017] [SRC-0021]
- Machine-learning potential pages emphasize chemical and conformational coverage, label fidelity, downstream tests, long-range physics, and simulation-scale performance rather than only larger datasets or lower energy/force errors. [SRC-0042] [SRC-0044] [SRC-0059] [SRC-0060]
- Free-energy pages emphasize phase-space overlap, decorrelated samples, visit allocation, jackknife or asymptotic uncertainty assumptions, and benchmark interpretation against experimental reproducibility. [SRC-0005] [SRC-0006] [SRC-0023] [SRC-0046] [SRC-0061]

## Links

- [[wiki/questions/force-field-training-validation-scope]]
- [[wiki/concepts/automated-force-field-training]]
- [[wiki/concepts/force-field-training-from-experimental-observables]]
- [[wiki/concepts/free-energy-reweighting-for-force-field-fine-tuning]]
- [[wiki/concepts/stability-aware-mlff-training]]
- [[wiki/concepts/machine-learning-potential-datasets]]
- [[wiki/concepts/machine-learned-interatomic-potential-foundation-models]]
- [[wiki/concepts/free-energy-estimation]]
- [[wiki/concepts/relative-binding-free-energy-benchmarking]]

## Open Questions

- Which small set of validation diagnostics best predicts downstream reliability across force-field fitting, learned potentials, and free-energy workflows?
- How should benchmark reports combine experimental uncertainty, sampling uncertainty, setup uncertainty, and model-form uncertainty without collapsing them into one opaque score?
