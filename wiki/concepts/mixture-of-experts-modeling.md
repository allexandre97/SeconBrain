---
type: concept
status: active
created: 2026-06-30
updated: 2026-06-30
areas:
  - research
categories:
  - research/machine-learning/statistical-modeling
tags:
  - mixture-of-experts
  - gating-functions
  - statistical-learning
sources:
  - SRC-0038
related: []
sensitivity: public
encryption: none
---

# Mixture-of-Experts Modeling

## Summary

Mixture-of-experts models represent heterogeneous conditional relationships by combining input-dependent gating functions with expert conditional models. They can be used for classification, clustering, and regression, and they have both neural-network and statistical-mixture interpretations. [SRC-0038]

## Key Points

- Gates define input-dependent probabilities over latent components. [SRC-0038]
- Experts define conditional distributions of the response given the input and latent component. [SRC-0038]
- The resulting conditional density is a weighted sum over experts, with weights determined by the gates. [SRC-0038]
- Expert choices can be adapted to the response type, including Gaussian regression, logistic, Poisson, multinomial, robust, or other generalized-linear experts. [SRC-0038]
- Model selection often centers on the number of components, with BIC justified under regularity assumptions for some MoE families. [SRC-0038]

## Core equation

$$
\operatorname{MoE}(y\mid x;\theta)=
\sum_{z=1}^{g}\operatorname{Gate}_z(x;\gamma)
\operatorname{Expert}_z(y\mid x;\eta_z)
$$

[SRC-0038]

## Caveats

- Approximation, consistency, and asymptotic normality results are model-family-specific and depend on assumptions that may fail in flexible modern variants. [SRC-0038]
- As with mixture models generally, optimization and component selection can be sensitive to local optima and initialization. [SRC-0038]

## Links

- [[sources/SRC-0038-practical-and-theoretical-aspects-of-mixture-of-experts]]

## Open Questions

- Which classical MoE consistency and model-selection results carry over to large sparse expert models used in modern deep learning?
