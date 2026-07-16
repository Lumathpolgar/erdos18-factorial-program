# Candidate 3: Transformed Dyadic Prefix Control

## Contract

- Candidate ID: `N3-CAND-CF-001`
- Original unrestricted logarithmic form: `DISPROVED`
- Unnormalized numerical form with only the zero major arc: `DISPROVED`
- Normalized many-tail-layers form: `DISPROVED`
- Active transformed prefix form: `OPEN`
- Intended consumer: Nova 2

## Original numerical law

For

\[
B_t(n)=
\{2^{t-1}u:u\text{ odd},\ 3u\mid n!,\ 2^{t-1}u\le Y_n\},
\]

let independent coordinates satisfy

\[
P_\lambda(Z_t=b)
=
\frac{e^{\lambda b}}
{1+\sum_{a\in B_t(n)}e^{\lambda a}},
\qquad
b\in B_t(n)\cup\{0\}.
\]

Set

\[
T_{n,\lambda}=\sum_{t=1}^{M_n}Z_t.
\]

The exact final-only target range is

\[
P_n+1\le q\le Y_n,
\qquad
P_n=m_n(2^{M_n}-1)+W_n.
\]

## Closed unnormalized obstruction

N3-ANA-023 proves

\[
P(T\text{ even})
=p^{(0)}_{n,q}
\le
\frac{2e^{\varepsilon_n}}{m_n+1},
\]

\[
\Phi(\pi)=2p^{(0)}_{n,q}-1,
\]

and

\[
|\Phi(\pi)|
\ge
1-
\frac{4e^{\varepsilon_n}}{m_n+1}
\to1.
\]

Thus the unnormalized zero-only major-arc route is false.

N3-ANA-024 forces parity into every viable reference law or major-arc decomposition.

## Exact active normalization

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

N3-ANA-025 proves:

1. the transformed coordinates remain independent;
2. their common exact tilt is `2 lambda`;
3. the transformed first support contains `0` and `1`;
4. the transformed law has exact span one;
5. the transformed tilt tends uniformly to zero.

The transformed target interval is

\[
J_{n,q}
=
\left[
\left\lceil\frac{q-W_n-1}{2}\right\rceil,
\left\lfloor\frac{q-1}{2}\right\rfloor
\right]\cap\mathbb Z.
\]

Positive transformed-window mass implies positive original-window mass.

## Closed dyadic resonance audit

For

\[
\theta_j=\frac{\pi}{2^{j-1}},
\qquad
1\le j\le M_n-1,
\]

N3-ANA-026 proves

\[
\widetilde\Phi_{n,q}(\theta_j)
=
\left(
\prod_{t=1}^{j}
\widetilde\phi_{t,n,q}(\theta_j)
\right)
(2p_{j+1,n,q}^{(0)}-1).
\]

Every layer `t>=j+2` has factor exactly `1` at `theta_j`.

There is no nonzero exact dyadic modulus-one resonance because the transformed first support contains `0` and `1`. However, every dyadic point has an exact tail resonance.

## Closed many-tail-layers obstruction

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

N3-ANA-027 proves

\[
J_n=M_n-O(\log\log n)
\]

and, uniformly for `j<=J_n`,

\[
|2p_{j+1,n,q}^{(0)}-1|
\ge
1-rac{4e}{m_n+1},
\]

\[
\sum_{t=j+1}^{M_n}
\widetilde{\mathcal D}_{t,n,q}(\theta_j)
\le
\frac{4e}{m_n+1}.
\]

Thus the transformed tail does not accumulate useful dispersion at the dyadic ladder. Any decay must come from the first `j` transformed coordinates.

## Exact transformed-kernel interaction

Let

\[
N_{n,q}=|J_{n,q}|.
\]

N3-ANA-028 proves

\[
v_2(N_{n,q})\in\{0,1\}.
\]

At a reduced dyadic frequency `2pi a/2^d`, the transformed interval kernel vanishes exactly when `2^d|N_{n,q}`.

Therefore:

1. no reduced dyadic frequency of denominator at least `4` is an exact kernel zero;
2. `pi` is a kernel zero only when `rho_n` and `q` are both even.

Pointwise nonvanishing is not itself an integral obstruction. It proves that the next theorem cannot discard higher dyadic frequencies by exact kernel cancellation.

## Active prefix object

For each dyadic scale, define the prefix characteristic

\[
\widetilde\Phi_{n,q}^{\langle j\rangle}(\theta)
=
\prod_{t=1}^{j}
\widetilde\phi_{t,n,q}(\theta).
\]

The active theorem must control this prefix in a neighborhood of

\[
\theta_j=\pi/2^{j-1}.
\]

Equivalent residue formulation:

Let

\[
S_j=\sum_{t=1}^{j}\widetilde Z_t.
\]

Then

\[
\widetilde\Phi_{n,q}^{\langle j\rangle}(\theta_j)
=
\sum_{r\bmod 2^j}
P(S_j\equiv r\bmod2^j)
e^{2\pi ir/2^j}.
\]

A quantitative prefix theorem may therefore be stated as residue spreading modulo `2^j` or as direct characteristic decay.

## Exact missing theorem

Prove one of the following uniformly for every post-prefix target.

1. A neighborhood estimate
   \[
   \left|
   \widetilde\Phi_{n,q}^{\langle j\rangle}
   (\theta_j+u)
   \right|
   \le E_{n,j}(u)
   \]
   whose weighted integral is below the transformed reference-window mass.
2. Quantitative residue spreading of `S_j mod 2^j` sufficient to bound the prefix characteristic.
3. A measure bound for neighborhoods where prefix dispersion is weak.
4. A transformed prefix concentration or additive-energy obstruction.
5. A non-dyadic rational obstruction that requires enlarging the transformed major-arc set.

## Mandatory tests

- Keep the exact post-prefix target range.
- Track common transformed tilt `2 lambda`.
- Analyze the first `j` coordinates, not the invisible tail.
- Match every neighborhood estimate to the transformed interval kernel.
- Do not treat nonzero pointwise kernel values as an integral lower bound.
- Retain numerical collision multiplicity.
- Do not use logarithmic divisor phases.
- Do not infer quantitative dispersion from exact span one.

## Current route decision

The preferred route is the exact odd-lattice normalization, followed by target-uniform prefix residue control near the complete dyadic ladder, a non-dyadic resonance audit, and a collision-aware transformed weighted Fourier theorem.