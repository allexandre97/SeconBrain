---
type: question
status: active
created: 2026-07-01
updated: 2026-07-01
question_status: open
areas:
  - research
categories:
  - research/adaptive-sampling
  - research/molecular-simulation/free-energy
  - research/statistics/monte-carlo
tags:
  - question
  - windowing
  - free-energy-profiles
  - diagnostics
related:
  - "[[wiki/sources/SRC-0005-times-square-sampling-free-energy]]"
  - "[[wiki/sources/SRC-0006-times-square-sampling-supplement]]"
  - "[[wiki/sources/SRC-0008-awh-free-energy-landscapes]]"
  - "[[wiki/concepts/tss-implementation-patterns]]"
  - "[[wiki/concepts/times-square-sampling]]"
  - "[[wiki/concepts/accelerated-weight-histogram-method]]"
sources:
  - SRC-0005
  - SRC-0006
  - SRC-0008
sensitivity: public
encryption: none
---

# Windowed Local Free Energy and Global Profile Reliability

## Question

When do local or windowed free-energy estimates stitch into a reliable global free-energy profile, and what diagnostics should reject unstable window choices? [SRC-0005] [SRC-0006]

## Context

TSS uses overlapping local windows and solves global stitching problems for visit-control and reported free energies. SRC-0006 records practical window-size failure modes: too-large windows can permit unstable early jumps, while too-small windows can make dynamics diffusive and increase error bars. AWH PMF work also depends on a reaction-coordinate or umbrella-coordinate representation whose global profile quality depends on the chosen coordinate and explored region. [SRC-0006] [SRC-0008]

## Current Position

Local estimates should be treated as candidates for a global profile only when overlap, offset consistency, window mixing, and uncertainty estimates support the stitching. Windowing is a scalability mechanism, not a guarantee that the global profile is reliable. [SRC-0006]

## Validation Boundaries

- TSS visit-control free energies are used for sampling, while separate reported free energies are constructed to reduce tilt noise near convergence. [SRC-0006, section 6.2]
- Window size changes both stability and error bars. [SRC-0006, sections 9-10]
- AWH PMF applications remain sensitive to reaction-coordinate choice and high-free-energy boundary selection. [SRC-0008]

## Links

- [[wiki/sources/SRC-0005-times-square-sampling-free-energy]]
- [[wiki/sources/SRC-0006-times-square-sampling-supplement]]
- [[wiki/sources/SRC-0008-awh-free-energy-landscapes]]
- [[wiki/concepts/tss-implementation-patterns]]
- [[wiki/concepts/times-square-sampling]]
- [[wiki/concepts/accelerated-weight-histogram-method]]
