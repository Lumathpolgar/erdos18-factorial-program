# Proof Dependency Map

## Main objective

```text
h(n!) < (log n)^{O(1)}.
```

## Direct factorial route

The current preferred route is:

```text
Factorial half-range theorem
    |
    v
Audited local-to-global conversion
    |
    v
h(n!) = O((log n)^3)
```

The needed local theorem is:

```text
FHR(n): H_{n!}(floor(sqrt(n!)) + 1) = O((log n)^2).
```

The exact exponent `2` is the present sufficient target, not a claim that it is optimal.

## Conditional Track B route

Historical Track B established a separate conditional chain from a stronger lcm-core theorem:

```text
H_{L_m}(floor(L_m^(1/3)) + 1) = O(log m)
    |
    v
factorial packet and descent machinery
    |
    v
factorial half-range control
    |
    v
h(n!) = O((log n)^3)
```

The first box remains unproved. Track B therefore remains conditional and fail-closed.

## Current direct-factorial research questions

A successful direct proof may require one or more of the following.

1. A deterministic decomposition of the divisor lattice of `n!` into a polylogarithmic number of useful packets.
2. A global additive occupancy theorem for sums of distinct factorial divisors.
3. An analytic theorem controlling the density and distribution of factorial divisors across relevant scales.
4. A nonseparable correction mechanism that does not require interval coverage after every layer.
5. A direct representation algorithm with a provable polylogarithmic term budget.

## Retired proof routes

The following specific routes must not be reused without addressing their proved obstruction.

- uniform entropy-scale divisor mesh for the lcm core
- fixed-power maximum-gap greedy growth
- maximum-gap greedy proof of the `O(log m)` lcm theorem
- independent CRT-coordinate atlases with only `O(log m)` layers
- separable recursive packet trees with two or more independently paid subproblems
- magnitude-separated high-prime marker atlases
- one-choice sequential shared-core ladders

These obstructions apply to their stated architectures. They are not automatic obstructions to direct factorial constructions.
