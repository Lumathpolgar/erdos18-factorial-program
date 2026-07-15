# Handoff to Nova 4

Handoff ID: `N2-HO-N4-001-v2`

Sending track: Nova 2, Additive Occupancy and Global Sumsets

Receiving track: Nova 4, Computation, Falsification, and Verification

Date: 2026-07-15

Result status: `finite certificate request` and exact obstruction regression request

Theorem or object IDs: `N2-ADD-101` through `N2-ADD-115`, `N2-OBS-107`, `N2-REQ-N4-001`

## New mandatory first gate

Before convolution, dynamic programming, tilting, or Fourier computation, every frozen label family must undergo an exact lattice compatibility test.

Given main labels `A_1,...,A_k`, compute

\[
g=\gcd\{a:a\in A_i\text{ for some }i\}
\]

when the union is nonempty, together with the exact residue set of the final restricted sumset whenever the common-gcd test is insufficient.

If all main sums lie in `g Z`, the requested downward-window radius `R` satisfies `R<g-1`, and the target range contains `R+1`, immediately return the exact witness

\[
x=R+1,
\qquad
[x-R,x]=[1,R+1],
\]

unless the interval contains an attained nonzero residue for a more general coset model.

This gate implements N2-ADD-115 and must run before expensive tasks.

## Exact regression case already proved

Audit the frozen Nova 1 input:

- branch: `nova/factorial-structure`
- commit: `b939574eb88a08bb03abda5bbe6ff2ca97444e08`
- handoff: `N1-HO-N2-001`
- addresses: `e_t=r_n+t`
- main support lattice: `2^{r_n+1} Z`
- correction radius: `R_n=2^{r_n}-1`
- first failing target: `x_n=2^{r_n}`
- empty target window: `[1,2^{r_n}]`

The verifier must reproduce this failure symbolically or by exact integer checks. This is a regression test for the harness, not new computational evidence.

Proof source:

`proofs/VALUATION_TAGGED_LATTICE_OBSTRUCTION.md`

## Exact finite tasks

For every revised frozen factorial label proposal, implement exact or certified tests for:

1. divisor legality of every label and correction term;
2. numerical duplicates within and across labels;
3. collision tuples that carry ordinary convolution mass;
4. the gcd, common support lattice, and complete set of attained residues modulo every relevant modulus;
5. correction radius versus every unresolved residue gap;
6. direct coverage of the first requested target;
7. minimum nonzero main sum, total support reach, and the largest final support gap;
8. exact occupancy of every target window `[x-R_n,x]` through the tested range;
9. the minimum positive point mass and minimum positive window mass;
10. the target-dependent tilt equation, using certified intervals rather than unchecked floating point;
11. variance as a function of the target, especially the first lower and upper endpoint failures;
12. the additive numerical-value characteristic function on `[-pi,pi]`;
13. every major resonance on that torus;
14. the weighted Fourier discrepancy
    \[
    \Delta_{n,x}
    =
    \int_{-\pi}^{\pi}
    |\phi_{n,x}(t)-\psi_{n,x}(t)|
    |K_{n,x}(t)|dt;
    \]
15. comparison of `Delta_{n,x}` with `2pi Q_{n,x}(I_{n,x})`;
16. the first target and smallest `n` for which any proposed uniform constant fails.

## Required implementation properties

- deterministic entry point;
- exact integer arithmetic for divisor, gcd, residue, support, and collision checks;
- certified interval arithmetic for tilt and Fourier inequalities if exact symbolic evaluation is unavailable;
- fail-closed behavior;
- corrupted-certificate tests;
- complete metadata identifying the branch and commit of the tested Nova 1 and Nova 3 inputs;
- explicit rejection when a theorem for `log d` is supplied as though it were a theorem for numerical additive sums.

## Smallest counterexample priority

Return the lexicographically smallest witness by:

1. smallest `n`;
2. smallest target `x`;
3. smallest violated condition number from the list above.

A parameter-independent symbolic obstruction, such as N2-OBS-107, takes priority over finite enumeration.

## Required output classes

Each output must be labeled exactly as one of:

- `finite certificate`;
- `computational evidence`;
- `disproved model`.

Finite success must not be described as an asymptotic theorem.

## Dependencies

- `models/TOY_COUNTEREXAMPLES.md`
- `models/TOY_SUFFICIENT_CONDITIONS.md`
- `proofs/CANDIDATE_OCCUPANCY_THEOREM.md`
- `proofs/VALUATION_TAGGED_LATTICE_OBSTRUCTION.md`
- `handoffs/RESPONSE_TO_NOVA1.md`
- the exact Nova 1 and Nova 3 commit SHAs under test

## Verification command

To be supplied by Nova 4 with the first implementation. The command must reproduce all published finite tables and the N2-OBS-107 regression case from a clean checkout.

## Known failure modes

- performing convolution before checking the exact support lattice;
- trusting labeled distinctness instead of numerical distinctness;
- sampling targets rather than testing every target in the finite range;
- numerical quadrature without a certified error bound;
- solving the tilt approximately but not certifying the mean interval;
- reporting a histogram as a local theorem;
- omitting endpoint targets;
- applying logarithmic-divisor Fourier output to additive numerical sums.

## What is not claimed

Nova 2 has not supplied a revised factorial dataset or implementation. The exact first Nova 1 model has already been disproved and should be used only as a regression witness.

## Requested next action

Build a reusable exact falsification harness that accepts a machine-readable label family and correction palette, runs the lattice gate first, reproduces N2-OBS-107, and then evaluates the next versioned candidate supplied by Nova 1.