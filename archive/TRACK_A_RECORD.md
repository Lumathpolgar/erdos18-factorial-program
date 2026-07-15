# Historical Track A Record

## Package

`Erdos18_Solution_Program_Phases1-12J.zip`

## Scope

This package contains the original constructive and computational program for the stronger lcm-core target

```text
L_m = lcm(1, 2, ..., m)
```

and the desired theorem

```text
H_{L_m}(floor(L_m^(1/3)) + 1) = O(log m).
```

## Included research areas

- divisor and prime-band utilities
- bitset and certificate infrastructure
- constructive correction layers
- colored divisor systems
- exact finite certificates
- greedy shell and orbit experiments
- counting obstructions
- local-to-global short-sum reductions
- central divisor and density research
- theorem reports and manifests through Phase 12J

## Status

The package contains valid finite certificates and several proved supporting lemmas, but it does not prove the lcm cube-root theorem.

Phase 12J reduced a proposed logarithmic greedy entry argument to a strong orbit-specific divisor-density condition. Later Phases 12K through 12P tested and largely retired the associated greedy and sequential architectures.

## Reuse policy

Direct factorial tracks may reuse:

- verified computational infrastructure
- exact certificate formats
- correction-layer lemmas whose hypotheses hold for `n!`
- local-to-global logic after a fresh domain audit
- failed-route obstructions as design constraints

No direct factorial track may assume the unproved lcm cube-root theorem.
