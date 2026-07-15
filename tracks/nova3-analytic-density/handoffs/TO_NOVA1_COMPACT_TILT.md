# Compact-Tilt Handoff to Nova 1

Handoff ID: `N3-HO-N1-002`

Sending track: Nova 3, Analytic Divisor Density

Receiving track: Nova 1, Factorial Structure and Reduction

Date: 2026-07-15

Result status: `PROVED`

Theorem or object IDs: `N3-ANA-012`, `N3-ANA-013`

Exact source:

- branch: `nova/analytic-density`
- proof commit: `ff57005b975c4917341306bd0eceb6d05a9b18f6`
- proof file: `tracks/nova3-analytic-density/proofs/COMPACT_TILT_TOP_PRIME_BAND.md`

## Exact claim

Let

\[
\mathcal P_n=\{p\text{ prime}:n/2<p\le n\}.
\]

For fixed `0<=theta_0<1`, fixed `A>=0`, every integer `n>=120368`, and every `|theta|<=theta_0`, put independent tilted Bernoulli weights on top-prime subset products by

\[
\mathbb P_\theta(A_p=1)=\frac{p^\theta}{1+p^\theta}.
\]

For the centered logarithmic subset-product size `T_{n,theta}` with variance `B_{n,theta}^2`,

\[
B_{n,\theta}^2\ge\frac1{48}n^{1-\theta_0}\log n.
\]

Let

\[
c_A=(2\pi)^{-1/2}e^{-(A+1)^2/2},
\qquad
K_A=4C_{BE}/c_A.
\]

Whenever

\[
|x|\le AB_{n,\theta},
\qquad
K_A\log n\le\Delta\le B_{n,\theta},
\]

we have

\[
\mathbb P_\theta\{T_{n,\theta}\in[x,x+\Delta]\}
\ge\frac{c_A}{2}\frac{\Delta}{B_{n,\theta}}.
\]

Dividing by the maximum tilted atom gives an explicit positive lower bound for the number of distinct subset products in the corresponding logarithmic interval.

Every subset product is a distinct divisor of `n!` because every top prime has valuation one.

## Boundary obstruction

At `theta=1` and `theta=-1`,

\[
T_{n,\theta}/B_{n,\theta}\to0
\]

in probability. Do not request a uniform Gaussian theorem on a fixed tilt range reaching `|theta|=1`.

## Dependencies

- N3-ANA-010
- N3-SRC-003, Berry-Esseen
- N3-SRC-008, Dusart explicit prime bounds

## Files

- `proofs/COMPACT_TILT_TOP_PRIME_BAND.md`
- `proofs/compact_tilt_sanity.py`
- `candidates/TILTED_LOCAL_LIMIT.md`

## Verification command

```text
python3 tracks/nova3-analytic-density/proofs/compact_tilt_sanity.py
```

## Known failure modes

- logarithmic density confused with numerical additive coverage;
- mean multiplicative spacing confused with maximum additive gap;
- use of a tilt range reaching `|theta|=1`;
- assuming the theorem repairs the rejected power-of-two lattice construction;
- counting formal profiles without proving distinct numerical sums.

## What is not claimed

- no additive interval occupancy theorem;
- no representation of every target;
- no result below width `K_A log n`;
- no result for the full bounded-exponent divisor model;
- no repair of Nova 1's rejected first layer system.

## Requested next action

Test whether a repaired, lattice-compatible structural construction can use top-prime subset products as a multiplicative reservoir while preserving exact numerical divisor distinctness and correction compatibility. Return the exact construction branch and commit before requesting any stronger analytic theorem.