# Candidate 3: Parity-Normalized Marker-Three Dispersion

## Contract

- Candidate ID: `N3-CAND-CF-001`
- Original unrestricted logarithmic form: `DISPROVED`
- Unnormalized numerical form with only the zero major arc: `DISPROVED`
- Active parity-normalized numerical form: `OPEN`
- Intended consumer: Nova 2

## Original numerical law

For

\[
B_t(n)=
\{2^{t-1}u:u\text{ odd},\ 3u\mid n!,\ 2^{t-1}u\le Y_n\},
\]

let

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
T_{n,\lambda}=\sum_{t=1}^{M_n}Z_t,
\qquad
\Phi_{n,\lambda}(\theta)
=E_\lambda e^{i\theta T_{n,\lambda}}.
\]

The exact final-only target range is

\[
P_n+1\le q\le Y_n,
\qquad
P_n=m_n(2^{M_n}-1)+W_n.
\]

`N3-ANA-020` proves that the unique centering tilt tends uniformly to zero on this range.

## Newly disproved unnormalized minor arc

`N3-ANA-023` proves that compact tilt does not remove the secondary parity resonance.

Every nonzero first-layer state is odd, while every later-layer state is even. Therefore

\[
P(T\text{ even})=P(Z_1=0)=p^{(0)}_{n,q},
\]

with

\[
p^{(0)}_{n,q}
\le
\frac{2e^{\varepsilon_n}}{m_n+1},
\qquad
\varepsilon_n
=
\frac{8M_n\log L_n}{2^{M_n}-1}.
\]

At the nonzero torus frequency `pi`,

\[
\Phi(\pi)=2p^{(0)}-1,
\]

so

\[
|\Phi(\pi)|
\ge
1-rac{4e^{\varepsilon_n}}{m_n+1}
\to1.
\]

The exact twin identity is

\[
\Phi(\pi+u)+\Phi(u)
=
2p^{(0)}\prod_{t=2}^{M_n}\phi_t(u).
\]

Thus a minor arc containing `pi` cannot have a target-uniform positive dispersion gap. Exact span one does not prevent asymptotic concentration on one parity class.

## Reference-law restriction

`N3-ANA-024` proves that any integer-valued reference law `G` satisfies

\[
d_{TV}(\mathcal L(T),G)
\ge
|G(2\mathbb Z)-p^{(0)}|.
\]

A parity-blind discretized Gaussian or other reference law with a fixed positive even mass cannot approximate the exact post-prefix law in total variation.

A window-specific Fourier comparison may still succeed, but it must encode the parity bias or explicitly treat the `pi` major arc.

## Exact active normalization

Condition on the odd event `Z_1!=0` and define

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

`N3-ANA-025` proves:

1. the transformed coordinates remain independent;
2. their common exact tilt is `2 lambda`;
3. the first transformed support contains `0` and `1`;
4. the transformed law has exact span one;
5. the transformed tilt also tends uniformly to zero.

The original target window

\[
I_{n,q}=[q-W_n,q]\cap\mathbb Z
\]

maps to

\[
J_{n,q}
=
\left[
\left\lceil\frac{q-W_n-1}{2}\right\rceil,
\left\lfloor\frac{q-1}{2}\right\rfloor
\right]\cap\mathbb Z.
\]

Positive transformed-window mass implies positive original-window mass through

\[
P_\lambda(T\in I_{n,q})
\ge
(1-p^{(0)})
P_{2\lambda}(\widetilde T\in J_{n,q}).
\]

## Active transformed supports

The first transformed support is

\[
\widetilde B_1(n)
=
\{(b-1)/2:b\in B_1(n)\}.
\]

For `t>=2`,

\[
\widetilde B_t(n)
=
\{0\}\cup\{b/2:b\in B_t(n)\}.
\]

The next theorem must analyze this exact product law, not the unnormalized law.

## Exact dispersion identity

For transformed coordinate probabilities `\widetilde p_t(a)`, define

\[
\widetilde{\mathcal D}_{t,\lambda}(\theta)
=
\sum_{a,b}
\widetilde p_t(a)\widetilde p_t(b)
\sin^2\left(\frac{(a-b)\theta}{2}\right).
\]

Then

\[
|\widetilde\phi_{t,\lambda}(\theta)|^2
=1-2\widetilde{\mathcal D}_{t,\lambda}(\theta),
\]

and

\[
|\widetilde\Phi_{n,\lambda}(\theta)|^2
\le
\exp\left(
-2\sum_t
\widetilde{\mathcal D}_{t,\lambda}(\theta)
\right).
\]

## Exact missing theorem

Prove one of the following for every transformed post-prefix target.

1. A complete list of the remaining major arcs and a lower bound for
   \[
   \sum_t\widetilde{\mathcal D}_{t,2\lambda_{n,q}}(\theta)
   \]
   outside them.
2. A measure bound for frequencies where transformed aggregate dispersion is small.
3. A weighted integral estimate directly matched to the transformed interval kernel.
4. A collision-aware local reference law and strict Fourier comparison.
5. A target-local concentration or additive-energy obstruction showing that the transformed route still fails.

## Mandatory tests

- Do not assume the parity normalization removes every secondary resonance.
- Determine the residue distribution of the transformed first coordinate modulo small integers.
- Track the exact transformed common tilt `2 lambda`.
- Compare the final error with the transformed reference-window mass.
- Retain numerical collision multiplicity.
- Do not use logarithmic divisor phases.
- Do not infer quantitative dispersion from span one.

## Current route decision

The unnormalized aggregate-dispersion route is rejected unless it includes both zero and `pi` as major arcs and uses a parity-aware reference law.

The preferred route is the exact odd-lattice normalization from `N3-ANA-025`, followed by a fresh resonance audit and transformed weighted Fourier theorem.
