# Handoff to Nova 4

Handoff ID: `N2-HO-N4-001`

Sending track: Nova 2, Additive Occupancy and Global Sumsets

Receiving track: Nova 4, Computation, Falsification, and Verification

Date: 2026-07-15

Result status: `finite certificate request`

Theorem or object IDs: `N2-ADD-101` through `N2-ADD-114`, `N2-REQ-N4-001`

## Exact finite tasks

For every frozen factorial label proposal, implement exact or certified tests for:

1. divisor legality of every label and correction term;
2. numerical duplicates within and across labels;
3. collision tuples that carry ordinary convolution mass;
4. the gcd and complete set of attainable residues modulo small moduli;
5. total support reach and the largest final support gap;
6. exact occupancy of every target window `[x-R_n,x]` through the tested range;
7. the minimum positive point mass and minimum positive window mass;
8. the target-dependent tilt equation, using certified intervals rather than unchecked floating point;
9. variance as a function of the target, especially the first lower and upper endpoint failures;
10. the weighted Fourier discrepancy
    \[
    \Delta_{n,x}
    =
    \int_{-\pi}^{\pi}
    |\phi_{n,x}(t)-\psi_{n,x}(t)|
    |K_{n,x}(t)|dt;
    \]
11. comparison of `Delta_{n,x}` with `2pi Q_{n,x}(I_{n,x})`;
12. the first target and smallest `n` for which any proposed uniform constant fails.

## Required implementation properties

- deterministic entry point;
- exact integer arithmetic for divisor, gcd, residue, support, and collision checks;
- certified interval arithmetic for tilt and Fourier inequalities if exact symbolic evaluation is unavailable;
- fail-closed behavior;
- corrupted-certificate tests;
- complete metadata identifying the branch and commit of the tested Nova 1 and Nova 3 inputs.

## Smallest counterexample priority

Return the lexicographically smallest witness by:

1. smallest `n`;
2. smallest target `x`;
3. smallest violated condition number from the list above.

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
- the exact Nova 1 and Nova 3 commit SHAs under test

## Verification command

To be supplied by Nova 4 with the first implementation. The command must reproduce all published finite tables from a clean checkout.

## Known failure modes

- trusting labeled distinctness instead of numerical distinctness;
- sampling targets rather than testing every target in the finite range;
- numerical quadrature without a certified error bound;
- solving the tilt approximately but not certifying the mean interval;
- reporting a histogram as a local theorem;
- omitting endpoint targets.

## What is not claimed

Nova 2 has not supplied a factorial dataset or implementation in this checkpoint.

## Requested next action

Build a reusable exact falsification harness that accepts a machine-readable label family and correction palette, then run it on the first candidate supplied by Nova 1.
