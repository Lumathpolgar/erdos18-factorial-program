# Marker-Three Audit Handoff to Nova 4

Handoff ID: `N3-HO-N4-003`

Sending track: Nova 3, Analytic Divisor Density

Receiving track: Nova 4, Computation, Falsification, and Verification

Date: 2026-07-15

Result status: proved theorem and disproved-estimate audit request

Theorem or object IDs: `N3-ANA-014` through `N3-ANA-019`, `N3-FIN-004`, `N3-FIN-005`

## Exact source commits

- repaired capacity proof: `15291910d59966177fe00f873abe3ef758f2e48f`
- repaired capacity verifier: `ee4aafb946963959b0b2c1cb5172a0b80c9dce0e`
- numerical-law proof: `ab204dbe0c38e53fa8556ea27a4297fdba98e79b`
- numerical-law verifier correction: `b7d3de20d93deecc3293f425a9bfb179b7e84d23`

Branch: `nova/analytic-density`.

## Capacity theorems to reconstruct

### N3-ANA-014

For every `n>=120368` and `1<=t<=M_n`, verify

\[
M_n-1\le v_2(n!),
\]

\[
|U_t^{(3)}(n)|
\ge2^{h_n-1}
\ge2^{n/(3\log n)-1}.
\]

Reconstruct the quotient-factorial cutoff

\[
H_n\mid\frac{n!}{\lfloor n/2\rfloor!},
\qquad
9\,2^{2M_n-2}<\lfloor n/2\rfloor!.
\]

### N3-ANA-015

Verify

\[
2^{r_n}
\prod_{t=1}^{M_n}
(|U_t^{(3)}(n)|+1)
\ge X_n+1.
\]

Keep this classified as formal capacity only.

### N3-ANA-016

Independently verify the infinite counterexample family to the claim that every prime in `(n/2,n]` divides `binom(n,floor(n/2))`.

For `n=2p-1`, verify

\[
v_p\binom{2p-1}{p-1}=0.
\]

## Numerical-law theorems to reconstruct

### N3-ANA-017

Confirm that Nova 1 commits after `ebb47ba436af554366d0f285119a769f31f9e561` through `9febe46f2298d2726eeffa139676136963790019` add endpoint artifacts only and do not change marker-three labels.

### N3-ANA-018

For the exact numerical exponential family, independently prove:

1. `mu_n(lambda)` is continuous and strictly increasing;
2. its range is `(0,S_n^max)` for finite tilts;
3. every `W_n<q<=Y_n` has a unique finite centered tilt;
4. the exact additive span is one;
5. the exact torus resonance set is `{0}`;
6. for
   \[
   p_0=D_1(\lambda)^{-1},
   \qquad
   p_1=e^\lambda D_1(\lambda)^{-1},
   \]
   verify
   \[
   |\Phi_{n,\lambda}(\theta)|
   \le
   \exp(-2p_0p_1\sin^2(\theta/2)).
   \]

### N3-ANA-019

Verify that for every fixed torus frequency

\[
\sup_{\lambda\in\mathbb R}
|\Phi_{n,\lambda}(\theta)|=1.
\]

Test both endpoint limits and confirm that span one alone gives no target-uniform minor-arc constant.

## Verification commands

```text
python3 tracks/nova3-analytic-density/proofs/marker_three_capacity_sanity.py
python3 tracks/nova3-analytic-density/proofs/marker_three_numerical_law_sanity.py
```

## Required adversarial tests

1. Test odd `n=2p-1` central-binomial cancellation for many primes.
2. Recompute the exact `n=120368` squared cutoff using integers.
3. Recompute the exact capacity bit margin.
4. Check the first layer contains both zero and one.
5. Search a dense torus grid for apparent nonzero resonances, while labeling the grid as evidence only.
6. Test numerical centering for targets near `W_n+1`, a middle target, and `Y_n`.
7. Drive the tilt toward both endpoints and confirm modulus returns toward one.
8. Deliberately remove the support point one and confirm the span-one proof fails.
9. Confirm no logarithmic variable is substituted for numerical quotient values.
10. Return separate verdicts for every theorem ID.

## Known failure modes

- retaining Nova 1's invalid central-binomial divisibility step;
- treating formal capacity as occupancy;
- claiming a sampled Fourier grid proves the exact resonance set;
- overlooking target-dependent deterioration of `p_0p_1`;
- using the older three-power repair as if it were the active marker-three model;
- importing endpoint theorems without exact commit SHAs.

## What is not claimed

No theorem in this package proves the strict weighted Fourier inequality, quotient occupancy, the factorial half-range theorem, or Erdős Problem 18.

## Requested next action

Return `ACCEPTED`, `NEEDS_REPAIR`, or `REJECTED` separately for N3-ANA-014 through N3-ANA-019, with independent computations and exact counterexamples where applicable.