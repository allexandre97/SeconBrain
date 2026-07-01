---
type: concept
status: active
created: 2026-07-01
updated: 2026-07-01
areas:
  - research
categories:
  - research/molecular-simulation/force-fields
  - research/machine-learning/molecular-modeling
  - research/machine-learning/scientific-modeling
  - research/scientific-computing
tags:
  - garnet
  - functional-form-search
  - symbolic-regression
  - differentiable-simulation
related:
  - "[[wiki/concepts/garnet-force-field]]"
  - "[[wiki/concepts/double-exponential-potential]]"
  - "[[wiki/concepts/symbolic-regression-interatomic-potentials]]"
  - "[[wiki/concepts/gnn-to-symbolic-regression-potentials]]"
  - "[[wiki/concepts/stability-aware-mlff-training]]"
  - "[[wiki/concepts/force-field-training-from-experimental-observables]]"
sources:
  - SRC-0003
  - SRC-0014
  - SRC-0017
  - SRC-0021
  - SRC-0024
  - SRC-0040
sensitivity: public
encryption: none
---

# Garnet Functional-Form Search

## Summary

Functional-form search for Garnet should be treated as a bilevel model-selection problem: a discrete or relaxed search proposes candidate interaction forms, then Garnet's differentiable parameter-training and simulation-observable losses evaluate the selected candidates. Symbolic regression is useful for proposing interpretable analytical terms, but ordinary symbolic-regression structure search is not itself end-to-end differentiable through the full Garnet pipeline. [SRC-0003] [SRC-0017] [SRC-0040]

## Key Points

- Garnet already demonstrates that functional form matters: Lennard-Jones became difficult to train once simulations entered the automated pipeline, while the double exponential non-bonded potential trained effectively in that setting. [SRC-0003]
- The Garnet paper explicitly frames automated training as a way to explore new functional forms, including bonded and non-bonded terms, soft-core potentials, polarization, and charge flux. [SRC-0003]
- Garnet's authors tested multiple non-bonded and valence functional forms by training model variants, reporting that buffered 14-7 and Lennard-Jones 6-9 could train while several other forms were unstable or not better than conventional choices. This is evidence for Garnet as an evaluator of functional forms, not evidence that arbitrary functional-form discovery is cheap. [SRC-0003, section "Different functional forms"]
- Symbolic regression can search over explicit potential-energy equations, especially when constrained by a physical scaffold such as an EAM decomposition or by a GNN architecture that exposes pairwise edge contributions. [SRC-0017] [SRC-0040]
- The discrete expression-search part of symbolic regression is usually not compatible with direct gradient descent through every pipeline component; however, once an expression is chosen, its continuous coefficients and Garnet-predicted parameters can be optimized by gradient-based methods if the expression is differentiable and implemented in the simulation backend. [SRC-0017] [SRC-0040]
- A baseline Garnet model can seed symbolic regression only by producing a usable supervised target, such as residual energies or forces, local pair/angle/torsion contribution estimates, learned edge or embedding outputs, or observable residuals. It does not seed SR by handing over a fixed parameter vector, because candidate expressions may have different numbers and meanings of parameters. [SRC-0040]
- Parameter-count mismatch should be handled by expression-local coefficient fitting, padded/masked readout heads, or a library/gating formulation. A candidate with more coefficients than the baseline Garnet term is not blocked by the baseline; it just requires a new coefficient fit and later a new Garnet readout if the coefficients are to be context-dependent. [SRC-0017] [SRC-0003]
- Simulation-level objectives remain essential because low static energy or force error does not guarantee stable or physically accurate downstream MD. StABlE makes downstream stability and observable recovery part of training, while observable-fitting work shows that property pipelines can provide analytic, automatic-differentiation, finite-difference, or fluctuation-response gradients. [SRC-0024] [SRC-0014] [SRC-0021]
- Functional-form candidates should be evaluated against out-of-training observables and systems, because force-field fitting can improve one target while degrading transferability. [SRC-0014] [SRC-0021]

## Implementation Consequences

Use symbolic regression as a proposal and compression layer rather than as the inner differentiable loop. Candidate expressions can be generated offline from learned Garnet residuals, GNN edge or local-environment contributions, force-matching data, or observable residuals. Promising expressions then become differentiable modules inside Garnet and are retrained with the full multi-objective loss. [SRC-0003] [SRC-0040]

The most practical search space is probably scaffolded, not unconstrained. For Garnet, plausible scaffolds include replacements or corrections for non-bonded radial terms, soft-core alchemical forms, torsion corrections, polarization or charge-flux terms, and residual terms added to the current double-exponential potential. [SRC-0003]

A full Garnet-training objective can be used as the outer score for SR proposals, but it should be reserved for a small shortlist. ForceBalance and Garnet-style workflows show that simulation-backed property objectives are computationally expensive, while reweighting workflows show that cached trajectories and effective-sample-size diagnostics can cheaply screen small perturbations before resimulation. [SRC-0025] [SRC-0003] [SRC-0016]

An epoch-by-epoch loop in which Garnet emits features, SR proposes new formulas, and the model retrains is conceptually possible but operationally unstable unless the SR step is slow-moving and cached. A safer version is a macro-epoch loop: train or freeze Garnet, export SR datasets, run SR offline, insert a small number of differentiable candidates, fine-tune, then repeat only after validation shows a persistent residual. [SRC-0040] [SRC-0024]

## Candidate Workflows

### Residual distillation

Train a baseline Garnet, then compute residual targets against DFT or high-quality reference data:

$$
\Delta U(x)=U_{\mathrm{ref}}(x)-U_{\mathrm{Garnet}}(x),
$$

and, where force labels are available,

$$
\Delta F_i(x)=F_{i,\mathrm{ref}}(x)-F_{i,\mathrm{Garnet}}(x).
$$

Symbolic regression then searches for a compact correction term, for example $\Delta U_{\mathrm{SR}}(r, z)$, using distances, angles, atom embeddings, or local descriptors $z$ as inputs. This is most defensible when the residual can be localized to an interaction family. [SRC-0003] [SRC-0040]

### Contribution distillation

Architect the baseline model so that some internal output has the semantics SR needs. SRC-0040 does this by using a deliberately pair-additive GNN whose edge outputs approximate pair energies; SR then fits distance-to-edge-output data. For Garnet, an analogous design would expose candidate non-bonded pair contributions, torsion residuals, or local many-body correction channels. [SRC-0040]

### Functional library and gating

Use SR to build a small library of candidate terms, then let Garnet learn context-dependent weights or gates over that library. This keeps training differentiable after the library is fixed and avoids rerunning symbolic search every minibatch or epoch. [SRC-0003]

### Expensive outer-loop selection

Use the full Garnet training pipeline as the final score for a shortlist of expressions. This is the most faithful evaluation, but it is too expensive for raw SR search because each candidate would require coefficient fitting, implementation, simulation, and validation. Cheaper static, reweighted, or short-simulation filters should precede it. [SRC-0003] [SRC-0016] [SRC-0025]

## Caveats

Symbolic interpretability is conditional on the grammar and scaffold. A compact equation is easier to inspect than a black-box neural potential, but it is not automatically physically correct or transferable. [SRC-0017]

GNN-to-symbolic-regression workflows are most straightforward when the architecture exposes meaningful local contributions. The Lennard-Jones demonstration in SRC-0040 uses a pair-additive benchmark; many-body biomolecular interactions will need richer descriptors and stricter validation. [SRC-0040]

Per-epoch SR is a poor fit for ordinary neural training unless the discrete search is amortized or replaced by a differentiable relaxation. Otherwise, the model's loss landscape changes whenever SR changes the expression, and the cost resembles repeated architecture search rather than ordinary end-to-end training. [SRC-0017] [SRC-0024]

## Links

- [[wiki/concepts/garnet-force-field]]
- [[wiki/concepts/double-exponential-potential]]
- [[wiki/concepts/symbolic-regression-interatomic-potentials]]
- [[wiki/concepts/gnn-to-symbolic-regression-potentials]]
- [[wiki/concepts/stability-aware-mlff-training]]
- [[wiki/concepts/force-field-training-from-experimental-observables]]
- [[wiki/answers/garnet-symbolic-regression-functional-search]]

## Open Questions

- Which Garnet interaction family should be searched first: non-bonded radial form, soft-core alchemical form, torsion correction, polarization, or charge flux?
- Can Garnet expose stable per-interaction residual targets that are meaningful enough for symbolic regression, or does the search need to operate only at the full-energy and observable level?
- How should expression complexity be penalized relative to simulation stability, transfer benchmarks, and implementation cost?
- What is the minimum architectural change needed for Garnet to expose local contribution targets without making those targets arbitrary latent quantities?
