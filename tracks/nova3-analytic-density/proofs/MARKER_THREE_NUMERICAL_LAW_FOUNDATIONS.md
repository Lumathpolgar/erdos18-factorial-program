# Foundations of the Marker-Three Numerical-Value Law

## Imported contracts

### Nova 2 analytic request

- branch: `nova/additive-occupancy`
- exact commit: `fb73e6906105c983bacbd46a96ef8d5d87567fae`
- handoff: `N2-HO-N3-003`
- file: `tracks/nova2-additive-occupancy/handoffs/MARKER_THREE_REQUEST_TO_NOVA3.md`

### Nova 1 structural source

The Nova 2 request pins:

- branch: `nova/factorial-structure`
- commit: `ebb47ba436af554366d0f285119a769f31f9e561`
- construction: `N1-CON-003`

The latest inspected Nova 1 head is

\[
9febe46f2298d2726eeffa139676136963790019.
\]

The three commits after `ebb47...` add only:

- `proofs/QUOTIENT_ENDPOINT_SUPPORT.md`;
- `verification/ENDPOINT_SUPPORT_FINITE_REPORT.md`;
- `verification/endpoint_support_sanity.py`.

They do not change the marker-three layer definitions. Therefore the numerical label law in `N2-HO-N3-003` remains structurally compatible. The endpoint contract should be upgraded to include Nova 1 `N1-STR-019`, `N1-STR-020`, and `N1-RED-006` from the latest head.

No logarithmic divisor law is used in this file.

## Frozen numerical labels

For

\[
X_n=\lfloor\sqrt{n!}\rfloor,
\qquad
Y_n=\left\lfloor\frac{X_n}{3}\right\rfloor,
\]

let

\[
M_n=\lceil16(\log n)^2\rceil,
\qquad
r_n=\lceil4\log n\rceil,
\]

and

\[
U_t(n)=
\{u\ge1:u\text{ odd},\ 3u\mid n!,\ 2^{t-1}u\le Y_n\},
\]

\[
B_t(n)=\{2^{t-1}u:u\in U_t(n)\},
\qquad 1\le t\le M_n.
\]

Let independent variables `Z_{t,lambda}` have the numerical-value exponential law

\[
\mathbb P_\lambda\{Z_{t,\lambda}=b\}
=
\frac{e^{\lambda b}}
{1+\sum_{a\in B_t(n)}e^{\lambda a}},
\qquad b\in B_t(n),
\]

with

\[
\mathbb P_\lambda\{Z_{t,\lambda}=0\}
=
\frac1{1+\sum_{a\in B_t(n)}e^{\lambda a}}.
\]

Define

\[
T_{n,\lambda}=\sum_{t=1}^{M_n}Z_{t,\lambda},
\]

\[
K_n(\lambda)=
\sum_{t=1}^{M_n}
\log\left(1+\sum_{a\in B_t(n)}e^{\lambda a}\right),
\]

\[
\mu_n(\lambda)=K_n'(\lambda),
\qquad
\sigma_n^2(\lambda)=K_n''(\lambda).
\]

For all sufficiently large `n` covered by N3-ANA-014, every `B_t(n)` is nonempty because `u=1` is legal through the largest layer.

## N3-ANA-017, marker-three contract compatibility

- Result class: `proved theorem`
- Repository status: `PROVED`
- Conclusion: the label sets in Nova 2 `N2-HO-N3-003` agree with the latest inspected Nova 1 marker-three construction; only the endpoint-support package advanced after the pinned construction commit

### Proof

The exact compare from Nova 1 commit `ebb47...` to `9febe...` is a three-commit fast-forward whose changed files are exactly the three endpoint-support artifacts listed above. No construction, layer, preferred-route, or marker-three capacity file changed.

Thus the numerical supports `B_t(n)` are unchanged. The newer endpoint theorems may be imported without changing the probability law.

The older Nova 2 request `N2-HO-N3-002` concerns a different three-power repair of the superseded valuation-tagged construction. It is not the active law for `N1-CON-003`.

## N3-ANA-018, exact tilt existence, uniqueness, span, and resonance set

- Result class: `proved theorem`
- Repository status: `PROVED`
- Parameter range: every `n` for which the frozen layers are nonempty
- Constants: exact

### Statement A: exact mean map

Let

\[
S_n^{\max}=\sum_{t=1}^{M_n}\max B_t(n).
\]

Then `mu_n` is continuous and strictly increasing on the real line, with

\[
\lim_{\lambda\to-\infty}\mu_n(\lambda)=0,
\qquad
\lim_{\lambda\to+\infty}\mu_n(\lambda)=S_n^{\max}.
\]

For every real target center

\[
0<\xi<S_n^{\max},
\]

there exists a unique finite real parameter `lambda(xi)` satisfying

\[
\mu_n(\lambda(\xi))=\xi.
\]

### Proof

The finite partition function factors over the layers. Differentiating gives

\[
K_n'(\lambda)=\mathbb E_\lambda T_{n,\lambda},
\qquad
K_n''(\lambda)=\operatorname{Var}_\lambda(T_{n,\lambda}).
\]

Every active layer has at least two support points, zero and one positive value. Therefore its variance is positive for every finite `lambda`, and

\[
K_n''(\lambda)>0.
\]

Hence `mu_n` is continuous and strictly increasing. As `lambda` tends to negative infinity, each layer concentrates at zero. As `lambda` tends to positive infinity, each layer concentrates at its maximum support value. The endpoint limits and unique intermediate solution follow.

### Statement B: exact Nova 2 window centering

Let

\[
W_n=\left\lfloor\frac{2^{r_n}-3}{3}\right\rfloor,
\]

and for every integer `q>W_n` define

\[
\xi_{n,q}=q-\frac{W_n}{2}.
\]

Then

\[
\xi_{n,q}\in[q-W_n,q].
\]

Nova 1 `N1-STR-020` gives

\[
S_n^{\max}>Y_n.
\]

Therefore every integer

\[
W_n<q\le Y_n
\]

has a unique finite tilt `lambda_{n,q}` satisfying

\[
\mu_n(\lambda_{n,q})=\xi_{n,q}.
\]

This closes the tilt-existence and uniqueness clause for the entire nontrivial target interval. Deterministic prefix results may remove an initial subinterval from analytic work, but they are not needed for existence.

### Statement C: exact additive span

For every relevant `n`,

\[
1\in B_1(n).
\]

Indeed, `u=1` is odd, `3|n!`, and `1<=Y_n`. Because zero is also in the support, the total sum support contains two values differing by one. Hence the exact additive span is

\[
1.
\]

### Statement D: exact torus resonance set

Define

\[
\Phi_{n,\lambda}(\theta)
=
\mathbb E_\lambda e^{i\theta T_{n,\lambda}},
\qquad
\theta\in[-\pi,\pi].
\]

For finite `lambda`,

\[
|\Phi_{n,\lambda}(\theta)|=1
\]

if and only if

\[
\theta=0.
\]

The support of the first layer contains zero and one with positive probability. Equality in the triangle inequality for its characteristic function requires

\[
e^{i\theta\cdot0}=e^{i\theta\cdot1},
\]

so `e^{i theta}=1`. On `[-pi,pi]`, this forces `theta=0`. All other factors have modulus at most one.

Thus the only exact resonance is the origin. This does not by itself give quantitative minor-arc decay.

### Statement E: explicit global bound from the first layer

Write

\[
D_{1,n}(\lambda)
=1+\sum_{a\in B_1(n)}e^{\lambda a},
\]

\[
p_0(\lambda)=D_{1,n}(\lambda)^{-1},
\qquad
p_1(\lambda)=e^\lambda D_{1,n}(\lambda)^{-1}.
\]

For every `theta in [-pi,pi]`,

\[
|\Phi_{n,\lambda}(\theta)|
\le
\left(1-4p_0(\lambda)p_1(\lambda)
\sin^2(\theta/2)\right)^{1/2}
\]

and hence

\[
|\Phi_{n,\lambda}(\theta)|
\le
\exp\left(
-2p_0(\lambda)p_1(\lambda)
\sin^2(\theta/2)
\right).
\]

This follows from the exact identity

\[
|\mathbb E e^{i\theta Z_1}|^2
=1-2\sum_{a<b}p_ap_b(1-\cos(\theta(b-a)))
\]

by retaining only the support pair `0,1` and using `sqrt(1-x)<=e^{-x/2}`.

The bound includes all torus frequencies and all resonances. Its coefficient must still be bounded below on the final bulk target range.

## N3-ANA-019, endpoint-uniform minor-arc decay is impossible

- Result class: `disproved estimate`
- Repository status: `DISPROVED`
- Disproved estimate: a target-independent constant `rho<1` satisfying
  \[
  |\Phi_{n,\lambda}(\theta)|\le\rho
  \]
  on a fixed nonzero torus arc uniformly over all finite real tilts

### Proof

As `lambda->-infinity`, every layer concentrates at zero. Therefore

\[
\Phi_{n,\lambda}(\theta)\to1
\]

for every `theta`, uniformly on the compact torus because the supports are finite.

As `lambda->+infinity`, every layer concentrates at its maximum value. The characteristic function converges to a unit complex phase and its modulus again tends to one.

Consequently, for every fixed `theta`,

\[
\sup_{\lambda\in\mathbb R}
|\Phi_{n,\lambda}(\theta)|=1.
\]

Equivalently,

\[
p_0(\lambda)p_1(\lambda)	o0
\]

at both tilt endpoints. Span one and the absence of exact nonzero resonances do not yield a uniform quantitative minor-arc gap.

Any valid bulk theorem must prove one of the following on its declared target range:

1. a compact tilt bound;
2. a direct lower bound for a phase-dispersing collection of coordinate probabilities;
3. a variance and maximal-step condition strong enough to imply such dispersion.

Endpoint or deterministic-prefix handoffs are mandatory.

## Closed and open clauses from N2-HO-N3-003

Closed:

1. exact active structural version;
2. tilt existence and uniqueness for `W_n<q<=Y_n`;
3. exact additive span one;
4. complete exact resonance set `{0}`;
5. an explicit all-frequency characteristic-function bound with target-dependent coefficient.

Open:

1. uniform variance and third-moment bounds on the final analytic target range;
2. a lower bound for quantitative phase dispersion away from zero;
3. a major-arc reference law with constant-width window mass;
4. the strict weighted Fourier inequality;
5. the exact transition from deterministic prefix to analytic bulk after importing the latest endpoint package.

## Claim boundary

These theorems do not prove positive mass in every quotient window. They close only the product-law centering and exact lattice-resonance foundations and identify why a bulk restriction is necessary.