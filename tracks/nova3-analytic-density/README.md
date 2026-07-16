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
- an exact odd-lattice normalization with common tilt `2 lambda`;
- an exact transformed dyadic finite-prefix factorization;
- a proof that transformed tail dispersion collapses at almost every dyadic layer scale;
- an exact transformed-window dyadic kernel classification.

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

The unnormalized zero-only major-arc plan is invalid.

## Exact odd-lattice repair

Condition on `Z_1!=0` and define

\[
\widetilde Z_1=(Z_1-1)/2,
\qquad
\widetilde Z_t=Z_t/2
\quad(t>=2).
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

## Transformed dyadic resonance ladder

For

\[
\theta_j=\frac{\pi}{2^{j-1}},
\qquad
1\le j\le M_n-1,
\]

N3-ANA-026 proves

\[
\widetilde\Phi(\theta_j)
=
\left(
\prod_{t=1}^{j}
\widetilde\phi_t(\theta_j)
\right)
(2p_{j+1}^{(0)}-1).
\]

Every layer after `j+1` is exactly invisible at `theta_j`.

Define

\[
J_n
=
\min\left(
M_n-1,
\left\lfloor
1+\log_2
\frac{2^{M_n}-1}{16M_n\log L_n}
\right\rfloor
\right).
\]

Then

\[
J_n=M_n-O(\log\log n),
\]

and, for every `j<=J_n`,

\[
|2p_{j+1}^{(0)}-1|
\ge
1-rac{4e}{m_n+1},
\]

\[
\sum_{t=j+1}^{M_n}
\widetilde{\mathcal D}_t(\theta_j)
\le
\frac{4e}{m_n+1}.
\]

Thus later layers do not supply useful aggregate dispersion at the dyadic ladder. Any decay must come from the first `j` transformed coordinates.

## Transformed interval kernel

Let

\[
N_{n,q}=|J_{n,q}|.
\]

N3-ANA-028 proves

\[
v_2(N_{n,q})\in\{0,1\}.
\]

The transformed interval kernel never vanishes at a reduced dyadic frequency of denominator at least `4`. At `pi`, it vanishes only when `rho_n` and `q` are both even.

Pointwise nonvanishing does not itself create an integral obstruction. It means that higher dyadic ladder neighborhoods must be controlled analytically rather than discarded by exact kernel zeros.

## Active theorem target

Prove target-uniform prefix control for

\[
\widetilde\Phi^{\langle j\rangle}_{n,q}(\theta)
=
\prod_{t=1}^{j}
\widetilde\phi_{t,n,q}(\theta)
\]

in neighborhoods of every transformed dyadic ladder frequency.

Equivalent formulations include:

1. residue spreading of the first `j` transformed coordinates modulo `2^j`;
2. direct prefix characteristic decay;
3. a measure bound for weak-prefix neighborhoods;
4. a prefix residue concentration or additive-energy obstruction.

The final local law must remain collision-aware and must be matched to the transformed interval kernel.

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
python3 tracks/nova3-analytic-density/proofs/transformed_dyadic_sanity.py
```

Finite checks and computational tables remain separate from symbolic proof.

## Claim boundary

The factorial half-range theorem and Erdős Problem 18 remain open. Formal capacity, compact numerical tilt, span one, parity normalization, dyadic factorization, and collision identities do not by themselves prove quotient occupancy or maximum-gap control.