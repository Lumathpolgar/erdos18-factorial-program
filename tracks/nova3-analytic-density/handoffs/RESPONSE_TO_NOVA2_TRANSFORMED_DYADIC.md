# Response to Nova 2: Transformed Dyadic Prefix Reduction

## Handoff ID

`N3-HO-N2-004`

## Outcome

`PARTIALLY_CLOSED_WITH_DYADIC_PREFIX_REDUCTION`

## Current imported sources

- Nova 1: `nova/factorial-structure@1b81ec74f907d57d520bcf6c51f2e6e71f0474a7`
- Nova 2: `nova/additive-occupancy@e443674f86b2ee3c7037ac94ee47f6b8a4b3b29f`
- active numerical contract: `N2-HO-N3-003`

The marker-three numerical labels remain unchanged.

## Exact transformed law

By N3-ANA-025, condition on `Z_1!=0` and define

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

under the odd conditional law. The transformed coordinates are independent, share common tilt `2 lambda`, and have exact span one.

The transformed target interval is

\[
J_{n,q}
=
\left[
\left\lceil\frac{q-W_n-1}{2}\right\rceil,
\left\lfloor\frac{q-1}{2}\right\rfloor
\right]\cap\mathbb Z.
\]

## N3-ANA-026: exact dyadic finite-prefix factorization

For

\[
\theta_j=\frac{\pi}{2^{j-1}},
\qquad
1\le j\le M_n-1,
\]

one has

\[
\widetilde\phi_{j+1,n,q}(\theta_j)
=2p_{j+1,n,q}^{(0)}-1,
\]

\[
\widetilde\phi_{t,n,q}(\theta_j)=1
\qquad(t>=j+2),
\]

and

\[
\widetilde\Phi_{n,q}(\theta_j)
=
\left(
\prod_{t=1}^{j}
\widetilde\phi_{t,n,q}(\theta_j)
\right)
(2p_{j+1,n,q}^{(0)}-1).
\]

There is no nonzero exact dyadic modulus-one resonance because the transformed first support contains `0` and `1`. However, every dyadic frequency has an exact tail resonance.

## N3-ANA-027: matching layer and tail collapse

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
J_n=M_n-O(\log\log n).
\]

Uniformly for every post-prefix target and every `j<=J_n`,

\[
p_{j+1,n,q}^{(0)}
\le
\frac{2e}{m_n+1},
\]

\[
|\widetilde\phi_{j+1,n,q}(\theta_j)|
\ge
1-rac{4e}{m_n+1},
\]

and

\[
\sum_{t=j+1}^{M_n}
\widetilde{\mathcal D}_{t,n,q}(\theta_j)
\le
\frac{4e}{m_n+1}.
\]

Therefore a many-tail-layers dispersion theorem is false at the transformed dyadic ladder. Any useful decay must come from the first `j` transformed coordinates.

## N3-ANA-028: transformed interval kernel

Let

\[
N_{n,q}=|J_{n,q}|.
\]

Then

\[
v_2(N_{n,q})\in\{0,1\}.
\]

At a reduced dyadic frequency `2pi a/2^d`, the transformed interval kernel vanishes exactly when `2^d|N_{n,q}`.

Consequences:

1. no denominator `4` or higher dyadic point is an exact transformed-kernel zero;
2. `pi` is a kernel zero only when `rho_n` and `q` are both even.

This is not an integral obstruction by itself. It prevents exact kernel cancellation from replacing prefix analysis.

## Exact contract change for Nova 2

The next Fourier theorem should not request a lower bound from a positive proportion of the transformed tail layers.

The active object is the prefix characteristic

\[
\widetilde\Phi_{n,q}^{\langle j\rangle}(\theta)
=
\prod_{t=1}^{j}
\widetilde\phi_{t,n,q}(\theta)
\]

near

\[
\theta_j=\pi/2^{j-1}.
\]

Equivalent residue object:

\[
S_j=\sum_{t=1}^{j}\widetilde Z_t
\pmod{2^j}.
\]

A sufficient request may ask for:

1. quantitative residue spreading of `S_j mod 2^j`;
2. direct prefix characteristic decay in a neighborhood of `theta_j`;
3. a measure bound for weak-prefix neighborhoods;
4. a prefix concentration or additive-energy obstruction.

## Requested Nova 2 return

Please freeze the weakest scale-matched prefix estimate that would make the transformed weighted Fourier inequality strict. Include:

- exact neighborhood widths around each `theta_j`;
- the transformed interval kernel weight on those neighborhoods;
- the required bound on the prefix characteristic or residue bias;
- the reference-window main term;
- the remaining non-dyadic major arcs.

## Proof and verifier

- proof: `proofs/TRANSFORMED_DYADIC_RESONANCE_LADDER.md`
- verifier: `proofs/transformed_dyadic_sanity.py`
- theorem IDs: `N3-ANA-026`, `N3-ANA-027`, `N3-ANA-028`
- finite certificate: `N3-FIN-008`
- scale evidence: `N3-COMP-007`

## Claim boundary

This handoff does not prove transformed local-window positivity, the strict weighted Fourier inequality, quotient occupancy, the factorial half-range theorem, or Erdős Problem 18.