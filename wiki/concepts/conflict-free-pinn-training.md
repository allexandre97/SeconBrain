---
type: concept
status: active
created: 2026-06-30
updated: 2026-06-30
areas:
  - research
categories:
  - research/machine-learning/scientific-modeling
tags:
  - PINNs
  - gradient-conflict
  - multi-objective-optimization
sources:
  - SRC-0036
related: []
sensitivity: public
encryption: none
---

# Conflict-Free PINN Training

## Summary

Conflict-free PINN training addresses cases where separate PINN loss terms, such as PDE residuals and boundary or initial conditions, produce gradients that interfere with each other. ConFIG constructs a final update direction with positive dot product against each loss-specific gradient and balanced projection lengths. [SRC-0036]

## Key Points

- A multi-loss update conflicts with loss $L_i$ when $g_i^\top g_c < 0$, because stepping along $g_c$ locally increases or fails to decrease that loss. [SRC-0036]
- ConFIG uses a pseudoinverse construction on normalized gradients to find an update direction that is conflict-free for all losses under its assumptions. [SRC-0036]
- Equal projection lengths are used to keep loss terms decreasing at comparable effective rates. [SRC-0036]
- M-ConFIG trades exact per-step gradient aggregation for momentum-based alternating updates, improving cost but adding memory and possible degradation with many losses. [SRC-0036]

## Links

- [[sources/SRC-0036-config-towards-conflict-free-training-of-physics-informed]]

## Open Questions

- How should conflict-free gradient aggregation be combined with better PINN architectures, causal training, or sampling strategies for chaotic or stiff PDEs?
