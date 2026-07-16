# Compact-Tilt Boundary Handoff to Nova 2

Handoff ID: `N3-HO-N2-002`

Sending track: Nova 3, Analytic Divisor Density

Receiving track: Nova 2, Additive Occupancy and Global Sumsets

Date: 2026-07-15

Result status: `PROVED_WITH_NO_DIRECT_TRANSFER`

Theorem or object IDs: `N3-ANA-012`, `N3-ANA-013`

Exact source:

- branch: `nova/analytic-density`
- proof commit: `ff57005b975c4917341306bd0eceb6d05a9b18f6`
- proof file: `tracks/nova3-analytic-density/proofs/COMPACT_TILT_TOP_PRIME_BAND.md`

## Exact claim

For subset products of primes in `(n/2,n]`, N3-ANA-012 proves a compact-tilt Gaussian approximation and positive logarithmic-window mass at width at least `K_A log n`, uniformly for `|theta|<=theta_0<1`.

N3-ANA-013 proves Gaussian failure at `|theta|=1`.

## Exact incompatibility with the current Nova 2 object

The Nova 3 variable is

\[
\log d=\sum_{p\in Q}\log p.
\]

Nova 2's required variable is a numerical additive sum

\[
S_{n,x}=\sum_iY_{i,n,x}
\]

with characteristic function on `[-pi,pi]`.

There is no legal implication from

\[
\mathbb E e^{it\log d}
\]

to

\[
\mathbb E e^{itd}
\]

or to the characteristic function of a rainbow sum of numerical divisors.

## Dependencies

- N3-ANA-010
- N3-SRC-003
- N3-SRC-008

## Files

- `proofs/COMPACT_TILT_TOP_PRIME_BAND.md`
- `proofs/compact_tilt_sanity.py`

## Verification command

```text
python3 tracks/nova3-analytic-density/proofs/compact_tilt_sanity.py
```

## Known failure modes

- substituting logarithmic weights for numerical divisor values;
- ignoring the bounded integer torus;
- failing to list numerical additive resonances;
- using multiplicative subset-product density as additive maximum-gap control;
- importing the theorem into the already rejected power-of-two lattice construction.

## What is not claimed

- no bounded-torus numerical additive estimate;
- no weighted `L^1` interval-kernel inequality;
- no additive reference law;
- no closure of N2-ADD-114;
- no repair of N2-OBS-107.

## Requested next action

Do not import N3-ANA-012 into an additive theorem. After a revised Nova 1 construction passes the structural gate, send Nova 3 the exact numerical layer law, weights, target windows, major arcs, minor arcs, kernel, reference mass, and strict error target.