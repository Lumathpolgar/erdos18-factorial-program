# Compact-Tilt Audit Handoff to Nova 4

Handoff ID: `N3-HO-N4-002`

Sending track: Nova 3, Analytic Divisor Density

Receiving track: Nova 4, Computation, Falsification, and Verification

Date: 2026-07-15

Result status: `PROVED` theorem audit with `FINITE_CERTIFICATE` and `COMPUTATIONAL_EVIDENCE` requests

Theorem or object IDs: `N3-ANA-012`, `N3-ANA-013`, `N3-FIN-003`, `N3-COMP-002`

Exact source:

- branch: `nova/analytic-density`
- proof commit: `ff57005b975c4917341306bd0eceb6d05a9b18f6`
- verifier commit: `d6f3385f186ec7b21a36ee5dddf6b5d8df70766c`

## Exact theorem to reconstruct

For

\[
\mathcal P_n=\{p:n/2<p\le n\},
\]

fixed `0<=theta_0<1`, and `|theta|<=theta_0`, verify:

\[
B_{n,\theta}^2\ge\frac1{48}n^{1-\theta_0}\log n,
\]

\[
\rho_{n,\theta}
\le(\log n)B_{n,\theta}^2,
\]

and

\[
\sup_z
\left|
\mathbb P_\theta\{T_{n,\theta}/B_{n,\theta}\le z\}
-\Phi(z)
\right|
\le
C_{BE}\frac{\log n}{B_{n,\theta}}.
\]

For

\[
c_A=(2\pi)^{-1/2}e^{-(A+1)^2/2},
\qquad
K_A=4C_{BE}/c_A,
\]

verify that

\[
|x|\le AB_{n,\theta},
\qquad
K_A\log n\le\Delta\le B_{n,\theta}
\]

implies

\[
\mathbb P_\theta\{T_{n,\theta}\in[x,x+\Delta]\}
\ge\frac{c_A}{2}\frac{\Delta}{B_{n,\theta}}.
\]

Verify the maximum-tilted-atom conversion to a lower count of distinct subset products.

## Boundary obstruction to reconstruct

At `theta=1`, prove that the probability of any minority bit is at most

\[
\frac2{\log n-1.1},
\]

that the centered favored atom is `o(B_{n,1})`, and therefore

\[
T_{n,1}/B_{n,1}\to0
\]

in probability. Repeat by symmetry for `theta=-1`.

## Files

- `proofs/COMPACT_TILT_TOP_PRIME_BAND.md`
- `proofs/compact_tilt_sanity.py`
- `THEOREMS.md`
- `SOURCE_LEDGER.md`

## Verification command

```text
python3 tracks/nova3-analytic-density/proofs/compact_tilt_sanity.py
```

## Requested exact tests

1. Recompute the Bernoulli tilt formula for positive and negative `theta`.
2. Verify the variance constant `1/48` without using asymptotic notation.
3. Verify `E|X|^3 <= log(n) E X^2` coordinatewise.
4. Check that the Berry-Esseen error is subtracted at both interval endpoints.
5. Verify the normal-density minimum on `[-A,A+1]`.
6. Check the sign-dependent maximum tilted atom in the count conversion.
7. Exhaustively enumerate the listed small `n` and `theta` grid independently.
8. Add adversarial tests at `theta=0.99`, `theta=1`, and `theta=-1`.
9. Verify that no output claims numerical additive occupancy.
10. Return separate verdicts for N3-ANA-012 and N3-ANA-013.

## Known failure modes

- treating `theta_0=1` as covered;
- assuming the finite table proves uniform asymptotics;
- losing a factor of two in the two-endpoint Berry-Esseen subtraction;
- using the wrong interval endpoint for negative tilt in the maximal-atom bound;
- confusing distinct subset products with distinct additive sums;
- transferring `log d` results to numerical divisor values.

## What is not claimed

- no fine local limit below `K_A log n`;
- no theorem for all high-prime bounded exponents;
- no numerical additive convolution theorem;
- no closure of the factorial half-range theorem.

## Requested next action

Return `ACCEPTED`, `NEEDS_REPAIR`, or `REJECTED` separately for N3-ANA-012 and N3-ANA-013, with an independent proof reconstruction and adversarial verifier results.