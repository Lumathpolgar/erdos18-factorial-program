# Nova 3: Analytic Divisor Density

## Branch

`nova/analytic-density`

## Mission

Prove exact asymptotic counting and distribution estimates for divisors of `n!` that are legally matched to structural or additive theorem contracts.

## Current proved frontier

The branch now contains:

- the exact independent exponent and exponential-tilt model;
- a uniform logarithmic local-count ceiling;
- a non-Gaussian limit theorem for the full uniform-divisor model;
- an obstruction to unrestricted pointwise minor-arc decay;
- a high-prime zero-tilt central limit theorem and coarse-window result;
- the explicit upper-half prime interval bound
  \[
  \pi(n)-\pi(n/2)\ge n/(3\log n)
  \qquad(n\ge120368);
  \]
- the explicit Nova 1 menu-capacity threshold `n_3=n_4=n_5=120368`;
- a compact-tilt Gaussian and coarse logarithmic-window theorem for exact subset products of primes in `(n/2,n]`, uniform for every fixed `|theta|<=theta_0<1`;
- a unit-tilt freezing obstruction showing that the compact range cannot reach `|theta|=1`.

## Current distinction

Logarithmic divisor density and numerical additive occupancy are different analytic objects.

A theorem for

\[
\mathbb E e^{it\log d}
\]

does not control

\[
\mathbb E e^{itd}
\]

or a numerical rainbow sum. Nova 2's additive theorem requires a repaired layer system and a matched bounded-torus analysis on `[-pi,pi]`.

## Active theorem target

Determine the sharpest true uniform logarithmic-window scale below `K_A log n` for compactly tilted top-prime subset products. Prove a bounded-frequency local theorem, weaken to the strongest true intermediate width, or prove a resonance or maximum-gap obstruction.

## Required files

- `STATUS.md`
- `THEOREMS.md`
- `SOURCE_LEDGER.md`
- `OPEN_REQUIREMENTS.md`
- `PREFERRED_ROUTE.md`
- candidate theorem files under `candidates/`
- proof files under `proofs/`
- handoffs under `handoffs/`

## Verification

```text
python3 tracks/nova3-analytic-density/proofs/scale_sanity.py
python3 tracks/nova3-analytic-density/proofs/prime_interval_capacity_sanity.py
python3 tracks/nova3-analytic-density/proofs/compact_tilt_sanity.py
```

Finite checks and computational tables remain explicitly separated from asymptotic proof.

## Claim boundary

The factorial half-range theorem and Erdős Problem 18 remain open. Counting, formal profile capacity, logarithmic density, and Gaussian approximation do not by themselves imply additive coverage or maximum-gap control.