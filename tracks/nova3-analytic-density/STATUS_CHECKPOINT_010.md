# Nova 3 Status Addendum: Checkpoint 010

## State

`TENTH_SUBSTANTIVE_CHECKPOINT_COMPLETE`

The factorial half-range theorem and Erdős Problem 18 remain open.

## Imported heads

- Nova 1: `nova/factorial-structure@8c7ee8f64af56a8d082f1fa3adabb0b0309f6e27`
- Nova 2: `nova/additive-occupancy@591e4e51a00627ac48c0aa05fae4a955dccb9d14`
- Nova 4 inspected head: `nova/computational-verification@778709b18f9e3ac333aefb66b1d7bfe3e640e65a`

## Closed in this checkpoint

### Kernel-scale reduction

Only

\[
\rho_n-3
\]

dyadic ladder points lie beyond the first positive transformed interval-kernel zero.

All dyadic points with

\[
j\ge\rho_n-2
\]

lie inside the kernel central lobe and belong to the zero-frequency analysis.

At `n=120368`, this reduces separate dyadic treatment from `2189` ladder points to `44`.

### Full-menu phase reduction

At every remaining secondary dyadic point, one selected prefix coordinate has phase reversed by multiplying its positive odd core by `3`.

The selected legal cores decompose into consecutive 3-adic chains. Monotonicity of the tilted weights gives:

- lower-chain-endpoint control for nonpositive tilt;
- upper-chain-endpoint control for nonnegative tilt.

The complete transformed characteristic function is bounded by the same endpoint mass.

This uses the full selected menu, not the negligible low-state carrier from Checkpoint 009.

## Verification

```text
python3 tracks/nova3-analytic-density/proofs/dyadic_chain_endpoint_sanity.py
```

Equivalent calculations passed for `n in {12,15,18}` and transformed tilts `-1e-4`, `0`, and `1e-4`.

They checked:

- exact central-lobe inequalities;
- exact 3-adic chain contiguity;
- phase alternation under multiplication by `3`;
- chain reconstruction of the characteristic numerator;
- both sign-dependent endpoint bounds;
- selected large-scale ladder counts.

## Exact remaining blocker

The active missing estimate is now:

\[
P(B^-_{n,q,j})<1
\quad\text{uniformly when }\widetilde\lambda_{n,q}\le0,
\]

or

\[
P(B^+_{n,q,j})<1
\quad\text{uniformly when }\widetilde\lambda_{n,q}\ge0,
\]

with a quantitative gap strong enough for the transformed weighted Fourier inequality.

The estimate must hold for

\[
1\le j\le\rho_n-3
\]

and must be stable in neighborhoods of the dyadic points.

## Claim boundary

This checkpoint does not prove a strict endpoint-mass gap, neighborhood decay, transformed local-window positivity, quotient occupancy, the factorial half-range theorem, or Erdős Problem 18.