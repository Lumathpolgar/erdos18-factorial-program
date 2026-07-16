# Nova 3: Analytic Divisor Density

## Branch

`nova/analytic-density`

## Mission

Prove exact counting, distribution, and Fourier estimates for factorial divisors, matched to versioned structural and additive theorem contracts.

## Current proved frontier

The branch contains:

- the exact factorial-divisor exponent product and exponential-tilt model;
- a uniform logarithmic local-count ceiling;
- a non-Gaussian full-model limit;
- an obstruction to unrestricted logarithmic minor-arc decay;
- a high-prime zero-tilt central limit theorem and coarse windows;
- the explicit prime interval theorem
  \[
  \pi(n)-\pi(n/2)\ge n/(3\log n)
  \qquad(n\ge120368);
  \]
- old-address and repaired marker-three formal-capacity theorems;
- compact-tilt top-prime logarithmic coarse windows;
- a unit-tilt freezing obstruction;
- the active marker-three numerical product law;
- exact target-dependent centering;
- the exact deterministic-to-analytic post-prefix boundary;
- uniform post-prefix tilt compression;
- exact collision-aware numerical atoms;
- an exact parity-twin obstruction at `pi`;
- an exact odd-lattice normalization with common tilt `2 lambda`.

## Current cross-track sources

- Nova 1: `nova/factorial-structure@1b81ec74f907d57d520bcf6c51f2e6e71f0474a7`
- Nova 2: `nova/additive-occupancy@e443674f86b2ee3c7037ac94ee47f6b8a4b3b29f`
- Active request: `N2-HO-N3-003`

The marker-three quotient supports are

\[
B_t(n)=
\{2^{t-1}u:u\text{ odd},\ 3u\mid n!,\ 2^{t-1}u\le Y_n\}.
\]

The exact final-only asymptotic range is

\[
m_n(2^{M_n}-1)+W_n+1
\le q\le Y_n.
\]

## Compact numerical tilt

For every target in the exact post-prefix range,

\[
-\frac{8M_n\log L_n}{L_n}
<\lambda_{n,q}<
\frac{16(n\log n+\log14)}{2^{M_n}},
\qquad
L_n=m_n(2^{M_n}-1).
\]

Thus the common numerical tilt tends uniformly to zero.

## Parity twin obstruction

The exact span-one statement conceals severe parity concentration.

Every nonzero first-layer state is odd. Every later-layer state is even. Hence

\[
P(T\text{ even})=P(Z_1=0).
\]

Uniformly on the post-prefix range,

\[
P(Z_1=0)
\le
\frac{2e^{\varepsilon_n}}{m_n+1},
\qquad
\varepsilon_n
=
\frac{8M_n\log L_n}{2^{M_n}-1}.
\]

At the nonzero torus frequency `pi`,

\[
\Phi(\pi)=2P(Z_1=0)-1,
\]

so

\[
|\Phi(\pi)|\to1.
\]

The exact twin identity is

\[
\Phi(\pi+u)+\Phi(u)
=
2P(Z_1=0)
\prod_{t=2}^{M_n}\phi_t(u).
\]

Therefore the unnormalized zero-only major-arc plan is invalid.

## Exact odd-lattice repair

Condition on `Z_1!=0` and define

\[
\widetilde Z_1=(Z_1-1)/2,
\qquad
\widetilde Z_t=Z_t/2\quad(t>=2).
\]

Then

\[
\widetilde T=(T-1)/2
\]

under the odd conditional law.

The transformed coordinates remain independent and have common exact tilt

\[
\widetilde\lambda=2\lambda.
\]

The transformed first support contains `0` and `1`, so the transformed law has exact span one.

The target window maps to

\[
J_{n,q}
=
\left[
\left\lceil\frac{q-W_n-1}{2}\right\rceil,
\left\lfloor\frac{q-1}{2}\right\rfloor
\right]\cap\mathbb Z.
\]

Positive transformed-window mass implies positive original-window mass.

## Active theorem target

Audit the normalized odd-lattice law for every remaining rational or dyadic secondary resonance. Then prove one of:

1. aggregate transformed phase dispersion outside all genuine transformed major arcs;
2. a measure bound for weak transformed dispersion;
3. a transformed weighted Fourier estimate;
4. a target-local transformed concentration or additive-energy obstruction.

The final local law must remain collision-aware.

## Mandatory distinction

A theorem for

\[
\mathbb E e^{it\log d}
\]

does not control

\[
\mathbb E e^{itd}
\]

or a numerical rainbow sum. The active inversion domain is the integer torus `[-pi,pi]`.

## Verification

```text
python3 tracks/nova3-analytic-density/proofs/scale_sanity.py
python3 tracks/nova3-analytic-density/proofs/prime_interval_capacity_sanity.py
python3 tracks/nova3-analytic-density/proofs/compact_tilt_sanity.py
python3 tracks/nova3-analytic-density/proofs/marker_three_capacity_sanity.py
python3 tracks/nova3-analytic-density/proofs/marker_three_numerical_law_sanity.py
python3 tracks/nova3-analytic-density/proofs/post_prefix_tilt_sanity.py
python3 tracks/nova3-analytic-density/proofs/parity_twin_sanity.py
```

Finite checks and computational tables remain separate from symbolic proof.

## Claim boundary

The factorial half-range theorem and Erdős Problem 18 remain open. Formal capacity, compact numerical tilt, span one, exact parity normalization, and collision identities do not by themselves prove quotient occupancy or maximum-gap control.
