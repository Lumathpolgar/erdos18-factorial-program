# Handoff to Nova 4

Handoff ID: `N2-HO-N4-001-v3`

Sending track: Nova 2, Additive Occupancy and Global Sumsets

Receiving track: Nova 4, Computation, Falsification, and Verification

Date: 2026-07-15

Result status: `finite certificate request`, `computational evidence request`, and exact obstruction regression request

Theorem or object IDs: `N2-ADD-101` through `N2-ADD-117`, `N2-OBS-107`, `N2-OBS-108`, `N2-MOD-QV-001`

## Exact imported baselines

### Nova 1 construction

- branch: `nova/factorial-structure`
- original handoff commit: `b939574eb88a08bb03abda5bbe6ff2ca97444e08`
- latest head inspected by Nova 2: `fa11f4b2cb86a2dd791df189ada12757be791804`
- construction: full-menu valuation-tagged address packets

### Nova 3 restrictions

- branch: `nova/analytic-density`
- commit inspected: `0ce88b28dc2e6641093526f5777bb31f658e3515`
- restriction: logarithmic divisor theorems are not additive numerical-sum theorems

Every run must record the exact input branch and commit SHA.

## Mandatory normalization gate

Before convolution, dynamic programming, tilting, or Fourier computation:

1. compute the common factor `g` of all nonzero main terms;
2. divide each main label by `g` exactly;
3. reject if any quotient is nonintegral;
4. construct the exact quotient labels;
5. compute the correction maximum `R`;
6. if `R=Lg-1`, reduce the required original-target theorem to quotient downward gaps at most `L-1` by N2-ADD-116;
7. test the first quotient targets through the minimum positive quotient sum;
8. only then run finite sumset or analytic work.

## Exact symbolic regression cases

For

\[
r_n=\lceil4\log n\rceil,
\qquad
g_n=2^{r_n+1},
\]

the verifier must reproduce all of the following.

### Regression A: original handoff

Original correction palette:

\[
\{2^0,\ldots,2^{r_n-1}\}.
\]

Correction maximum:

\[
2^{r_n}-1.
\]

Failure:

\[
x=2^{r_n},
\qquad
[1,2^{r_n}]\cap R_n=\varnothing.
\]

Result ID: `N2-OBS-107`.

### Regression B: one-power repair

Palette extended through `2^{r_n}`.

Correction maximum:

\[
g_n-1.
\]

Failure:

\[
x=g_n.
\]

The quotient target `m=1` cannot use quotient support `0` or a positive point at least `3`.

### Regression C: two-power repair

Palette extended through `2^{r_n+1}`.

Correction maximum:

\[
2g_n-1.
\]

Failure:

\[
x=2g_n.
\]

The quotient target `m=2` cannot use quotient support `0` or a positive point at least `3`.

Regressions B and C are `N2-OBS-108`.

### Regression D: three-power initial gate

Palette extended through `2^{r_n+2}`.

Correction maximum:

\[
4g_n-1.
\]

For every tested admissible `n` with `3 in B_1(n)`, verify that quotient windows at `m=0,1,2,3` are occupied by `0` or `3`.

This is only an initial gate, not a global success certificate.

## Exact normalized model

Define

\[
B_t(n)
=
\{2^{t-1}u:
 u\mid n!,\ u>1,\ u\text{ odd},\ g_n2^{t-1}u\le X_n\}.
\]

Let

\[
Q_n
=
\left\{
\sum_{t=1}^{M_n}b_t:
 b_t\in B_t(n)\cup\{0\}
\right\}.
\]

The exact finite occupancy question is whether

\[
Q_n\cap[\max(0,m-3),m]\ne\varnothing
\]

for every quotient target through the declared cutoff.

## Study Q1: exact quotient reachability

Choose and document a feasible finite range of `n`. For each `n`:

1. compute `v_2(n!)`, `r_n`, `M_n`, `g_n`, and `floor(X_n/g_n)` without unchecked floating point;
2. certify whether all three added powers divide `n!`;
3. construct every quotient label exactly or declare a transparent truncation rule;
4. report every layer size;
5. report the formal profile count;
6. compute the exact reachable quotient set through a declared cutoff `T_n`;
7. report the number of distinct reachable sums;
8. report collision multiplicity or collision ratio;
9. compute the maximum downward quotient gap;
10. return the first empty four-point window;
11. return one exact rainbow witness for every occupied target needed to certify a new maximum;
12. distinguish a full-family computation from a reduced-menu computation.

A reduced-menu failure is a failure of the reduced model only unless the witness is a structural obstruction that applies to the full family.

## Study Q2: quotient residues and resonances

For each tested `n`:

1. compute the gcd of the union of all nonzero quotient labels;
2. compute attainable residues of the final restricted sumset modulo every integer `2<=q<=64` through the exact finite reachability range;
3. list every modulus with a missing residue relevant to a four-point window;
4. evaluate the uniform or tilted quotient characteristic function on certified grids around all rational resonances `2pi a/q` for `q<=64`;
5. identify peaks not explained by the global gcd;
6. do not call grid evidence a minor-arc theorem.

## Study Q3: target-dependent tilt

Conditional on a finite quotient model:

1. solve the tilt equation with interval certification;
2. center inside `[m-3,m]`, preferably at `m-3/2`;
3. certify variance;
4. locate the first lower and upper endpoint variance failures;
5. compute or bound the minimum four-point window probability;
6. compare any approximation error directly with that probability;
7. reject any use of a characteristic function for `log d`.

## Study Q4: weighted Fourier comparison

For an explicit lattice reference law `G_{n,m}`, compute with certified error bounds

\[
\Delta_{n,m}
=
\int_{-\pi}^{\pi}
|\Phi_{n,m}(\theta)-\Psi_{n,m}(\theta)|
\left|\sum_{a=\max(0,m-3)}^m e^{-ia\theta}\right|d\theta.
\]

Compare with

\[
2\pi G_{n,m}([\max(0,m-3),m]).
\]

Uncertified numerical quadrature is computational evidence only.

## Required implementation properties

- deterministic entry point;
- exact integer arithmetic for legality, normalization, quotient labels, residues, gaps, and witnesses;
- no direct floating-point construction of `n!` or `sqrt(n!)`;
- certified interval arithmetic for boundary comparisons, tilts, and Fourier inequalities;
- fail-closed behavior;
- corrupted-certificate tests;
- exact metadata for every imported branch and SHA;
- explicit distinction between full and reduced menus;
- complete target scans within every declared finite range.

## Smallest counterexample priority

Return the lexicographically smallest witness by:

1. smallest `n`;
2. smallest quotient target `m`;
3. smallest violated gate or theorem condition.

A symbolic obstruction takes priority over finite enumeration.

## Required output classes

Each output must be labeled exactly as one of:

- `finite certificate`;
- `computational evidence`;
- `disproved model`.

Finite success must not be described as an asymptotic theorem.

## Dependencies

- `models/TOY_COUNTEREXAMPLES.md`
- `models/TOY_SUFFICIENT_CONDITIONS.md`
- `models/VALUATION_TAGGED_QUOTIENT_MODEL.md`
- `proofs/CANDIDATE_OCCUPANCY_THEOREM.md`
- `proofs/VALUATION_TAGGED_LATTICE_OBSTRUCTION.md`
- `proofs/LATTICE_QUOTIENT_NORMALIZATION.md`
- `handoffs/RESPONSE_TO_NOVA1.md`
- `handoffs/REPAIR_CONTRACT_TO_NOVA1.md`
- `handoffs/QUOTIENT_REQUEST_TO_NOVA3.md`

## Verification command

To be supplied by Nova 4 with the first implementation. One command must reproduce all symbolic regressions, finite tables, and valid/corrupted certificate tests from a clean checkout.

## Known failure modes

- performing convolution before quotient normalization;
- using the gcd of labels but not the exact final restricted residues;
- trusting labeled distinctness instead of numerical distinctness;
- sampling quotient targets rather than checking every target in the finite range;
- treating the three-power initial gate as global occupancy;
- silently replacing the full odd-divisor menu by a reduced high-prime menu;
- numerical quadrature without certified error;
- reporting a histogram as a local theorem;
- omitting endpoint targets;
- applying logarithmic-divisor Fourier output to additive quotient sums.

## What is not claimed

Nova 2 has proved the normalization and the repaired conditional implication. It has not proved the four-point quotient occupancy theorem, and it has not supplied a computational certificate for it.

## Requested next action

Build the quotient-normalized exact falsification harness, reproduce N2-OBS-107 and N2-OBS-108, then search for the smallest four-point quotient-window failure in the three-power repaired model.
