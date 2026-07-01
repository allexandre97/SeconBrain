---
type: claim
status: active
created: 2026-07-01
updated: 2026-07-01
claim_status: limited
claim_scope: local
areas:
  - research
categories:
  - research/molecular-simulation/free-energy
  - research/computational-drug-discovery
  - research/adaptive-sampling
tags:
  - claim
  - ladybugs
  - lambda-dynamics
  - fastmbar
related:
  - "[[wiki/sources/SRC-0013-ladybugs-lambda-dynamics]]"
  - "[[wiki/concepts/lambda-dynamics-with-bias-updated-gibbs-sampling]]"
  - "[[wiki/questions/adaptive-estimators-vs-fixed-sample-estimators]]"
  - "[[wiki/questions/overlap-support-diagnostics-for-free-energy-estimators]]"
  - "[[wiki/tensions/TEN-0005-on-the-fly-bias-adaptation-vs-postprocessing-diagnostics]]"
sources:
  - SRC-0013
sensitivity: public
encryption: none
---

# LaDyBUGS Couples Gibbs Sampling With FastMBAR Bias Updates

## Claim

LaDyBUGS samples many discrete alchemical ligand states in one simulation by alternating coordinate dynamics with Gibbs updates over lambda states, then periodically uses FastMBAR estimates to update dynamic biases. [SRC-0013]

## Scope

This claim is local to SRC-0013 and should be read in the context of ligand series that can be represented as discrete alchemical states around a common core. It does not establish general transfer to every perturbation network. [SRC-0013]

## Evidence

- SRC-0013 defines the conditional Gibbs distribution over lambda states and a bias update using FastMBAR free-energy estimates and visit penalties. [SRC-0013, eqs. 1 and 4]
- SRC-0013 reports benchmark efficiency gains relative to its TI/MBAR comparisons across five protein-ligand systems. [SRC-0013]

## Caveats

- The reported gains depend on benchmark setup, implementation, ligand grouping, and sufficient coordinate sampling within conditional MD segments. [SRC-0013]
- FastMBAR use inside the loop makes overlap and support diagnostics relevant during the adaptive run, not only after production. [SRC-0013]

## Links

- [[wiki/sources/SRC-0013-ladybugs-lambda-dynamics]]
- [[wiki/concepts/lambda-dynamics-with-bias-updated-gibbs-sampling]]
- [[wiki/questions/adaptive-estimators-vs-fixed-sample-estimators]]
- [[wiki/questions/overlap-support-diagnostics-for-free-energy-estimators]]
- [[wiki/tensions/TEN-0005-on-the-fly-bias-adaptation-vs-postprocessing-diagnostics]]
