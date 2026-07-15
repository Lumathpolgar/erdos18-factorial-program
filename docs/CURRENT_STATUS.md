# Current Status

## Certified status

The factorial formulation of Erdős Problem 18 is not solved.

## Completed work

### Track B

Track B is a completed conditional endgame. It contains the reduction, packet, descent, boundary, and clean-room audit machinery needed to convert a suitable local half-range theorem into a global polylogarithmic factorial bound.

The final Track B merge gate remains intentionally closed because its required Track A theorem has not been proved.

### Historical Track A

Track A developed computational infrastructure, local correction theorems, exact certificates, colored divisor constructions, greedy orbit studies, and several late-stage asymptotic gates.

Phases 12K through 12P produced rigorous route decisions:

- Phase 12K: the proposed uniform entropy-scale entry mesh is obstructed by integer granularity.
- Phase 12L: fixed-power greedy growth fails, and the maximum-gap greedy route has a superlogarithmic lower bound.
- Phase 12M: raw marked-layer capacity is sufficient, but separable recursion and independently decoded CRT atlases are insufficient.
- Phase 12N: the high-prime atlas fails through first-entry and additive shell-gap obstructions.
- Phase 12O: a mixed-scale shared-core ladder works in exact finite tests and repairs the earlier shell gap.
- Phase 12P: the one-choice sequential shared-core ladder requires at least superlogarithmically many layers asymptotically.

These phases do not disprove the target theorem. They disprove specific proof architectures.

## Current pivot

The program is pivoting from the stronger `L_m` theorem to a direct factorial theorem. This is motivated by the much richer prime-power valuation structure of `n!`.

The direct working target is

```text
H_{n!}(floor(sqrt(n!)) + 1) = O((log n)^2).
```

## What is missing

No current theorem proves the required global occupancy or representation statement for the divisor set of `n!`.

The missing work must provide a genuinely nonseparable mechanism, or another direct construction, that achieves polylogarithmic representation length across the factorial half-range.

## Progress language

This repository does not assign a percentage solved. Research phases, code, and conditional reductions do not form a reliable linear measure of distance to an open theorem.
