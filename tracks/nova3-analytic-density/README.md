# Nova 3: Analytic Divisor Density

## Branch

`nova/analytic-density`

## Mission

Prove exact counting, distribution, and Fourier estimates for factorial divisors, matched to versioned structural and additive theorem contracts.

## Current proved frontier

The branch now contains:

- the exact factorial-divisor exponent product and exponential-tilt model;
- a uniform logarithmic local-count ceiling;
- a non-Gaussian full-model limit;
- an obstruction to unrestricted logarithmic minor-arc decay;
- a high-prime zero-tilt central limit theorem and coarse-window theorem;
- the explicit prime interval bound
  \[
  \pi(n)-\pi(n/2)\ge n/(3\log n)
  \qquad(n\ge120368);
  \]
- explicit old-address and repaired marker-three formal-capacity theorems;
- a compact-tilt top-prime logarithmic Gaussian theorem for every fixed `|theta|<=theta_0<1`;
- a unit-tilt freezing obstruction;
- an exact repair of Nova 1's marker-three capacity proof;
- an infinite counterexample family to the proposed central-binomial divisibility shortcut;
- the active marker-three numerical product law;
- unique target-dependent numerical tilt for every nontrivial quotient target;
- exact additive span one and exact torus resonance set `{0}`;
- an explicit all-frequency characteristic-function bound;
- a proof that no minor-arc modulus gap can hold uniformly over all tilts.

## Active numerical contract

The active cross-track law is Nova 2 handoff `N2-HO-N3-003` at commit

`fb73e6906105c983bacbd46a96ef8d5d87567fae`.

It uses the numerical quotient supports

\[
B_t(n)=\{2^{t-1}u:u\text{ odd},\ 3u\mid n!,\ 2^{t-1}u\le Y_n\}.
\]

For every

\[
W_n<q\le Y_n,
\]

the common exponential family has a unique finite tilt centered inside `[q-W_n,q]`.

The only exact torus resonance is zero. Quantitative minor-arc control still requires a compact tilt range or an equivalent phase-dispersion lower bound on the final analytic target interval.

## Mandatory distinction

Logarithmic divisor density and numerical additive occupancy are different objects.

A theorem for

\[
\mathbb E e^{it\log d}
\]

does not control

\[
\mathbb E e^{itd}
\]

or a numerical rainbow sum. The active additive inversion domain is the integer torus `[-pi,pi]`.

## Active theorem target

After Nova 1 and Nova 2 freeze the exact transition from deterministic coverage to analytic responsibility, prove one of:

1. a compact bound on the target-dependent numerical tilt;
2. a direct phase-dispersion lower bound for enough active coordinates;
3. an exact target family where variance or minor-arc coefficients collapse.

Only then can the strict weighted Fourier inequality for constant-width quotient windows be attempted.

## Required files

- `STATUS.md`
- `THEOREMS.md`
- `SOURCE_LEDGER.md`
- `OPEN_REQUIREMENTS.md`
- `PREFERRED_ROUTE.md`
- candidate files under `candidates/`
- proofs and verifiers under `proofs/`
- versioned handoffs under `handoffs/`

## Verification

```text
python3 tracks/nova3-analytic-density/proofs/scale_sanity.py
python3 tracks/nova3-analytic-density/proofs/prime_interval_capacity_sanity.py
python3 tracks/nova3-analytic-density/proofs/compact_tilt_sanity.py
python3 tracks/nova3-analytic-density/proofs/marker_three_capacity_sanity.py
python3 tracks/nova3-analytic-density/proofs/marker_three_numerical_law_sanity.py
```

Finite checks and computational tables remain explicitly separated from symbolic proof.

## Claim boundary

The factorial half-range theorem and Erdős Problem 18 remain open. Formal capacity, logarithmic density, exact centering, span one, and resonance classification do not by themselves imply quotient occupancy or maximum-gap control.