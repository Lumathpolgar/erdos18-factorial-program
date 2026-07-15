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
- unique target-dependent numerical tilt;
- exact additive span one and exact torus resonance set `{0}`;
- an exact deterministic-to-analytic post-prefix boundary;
- a uniform shrinking-tilt theorem on the complete post-prefix range;
- a proof that the single binary anchor has exponentially collapsing weight;
- an exact collision-aware tilted atom formula.

## Active numerical contract

Current exact sources:

- Nova 1 branch `nova/factorial-structure`, commit `e3a0e3f5fb335b23afdd9e1fe418ac46ca1c766a`;
- Nova 2 branch `nova/additive-occupancy`, commit `82603c631a106c3bff4676bdeeb9cc791fc98f3c`;
- Nova 2 handoff `N2-HO-N3-003`.

The numerical quotient supports are

\[
B_t(n)=
\{2^{t-1}u:u\text{ odd},\ 3u\mid n!,\ 2^{t-1}u\le Y_n\}.
\]

Nova 2's deterministic small-core chain covers through

\[
P_n=m_n(2^{M_n}-1)+W_n.
\]

The asymptotic final-only analytic range is

\[
P_n+1\le q\le Y_n.
\]

For every target in this range, N3-ANA-020 proves

\[
-\frac{8M_n\log L_n}{L_n}
<\lambda_{n,q}<
\frac{16(n\log n+\log14)}{2^{M_n}},
\qquad
L_n=m_n(2^{M_n}-1),
\]

so the common numerical tilt tends uniformly to zero.

## Current analytic obstruction

Uniformly small tilt does not make individual state probabilities uniform in a useful quantitative sense.

At zero tilt,

\[
P_0(Z_t=0)P_0(Z_t=2^{t-1})
<2^{-2(n/(3\log n)-1)}.
\]

Therefore the existing one-pair characteristic-function estimate cannot close the minor arc.

The full numerical atom also contains exact collision multiplicity:

\[
P_\lambda(T=s)
=
\frac{C_n(s)e^{\lambda s}}
{\prod_tZ_t(\lambda)}.
\]

Any local reference law must retain or control `C_n(s)`.

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

Prove aggregate phase dispersion for the complete tilted odd-core menus on the post-prefix target range.

The primary candidate is

\[
\mathcal D_{t,\lambda}(\theta)
=
\sum_{a,b}p_t(a)p_t(b)
\sin^2\left(\frac{(a-b)\theta}{2}\right),
\]

with

\[
|\phi_{t,\lambda}(\theta)|^2
=1-2\mathcal D_{t,\lambda}(\theta).
\]

A successful theorem must aggregate many support differences or residue classes and remain collision-aware. A failure result must produce an explicit target-local concentration or additive-energy obstruction.

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
python3 tracks/nova3-analytic-density/proofs/post_prefix_tilt_sanity.py
```

Finite checks and computational tables remain explicitly separated from symbolic proof.

## Claim boundary

The factorial half-range theorem and Erdős Problem 18 remain open. Formal capacity, logarithmic density, compact numerical tilt, span one, exact resonances, and collision identities do not by themselves imply quotient occupancy or maximum-gap control.