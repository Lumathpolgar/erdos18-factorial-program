# Parity Twin Resonance and Exact Odd-Lattice Reduction

## Scope

This file continues the exact marker-three numerical quotient analysis. It uses numerical quotient values, not logarithmic divisor size.

Imported sources:

- Nova 1 branch `nova/factorial-structure`, inspected head `1b81ec74f907d57d520bcf6c51f2e6e71f0474a7`;
- Nova 2 branch `nova/additive-occupancy`, inspected head `e443674f86b2ee3c7037ac94ee47f6b8a4b3b29f`;
- Nova 3 theorems `N3-ANA-018` and `N3-ANA-020`.

The factorial half-range theorem remains open.

## Frozen notation

For every integer `n>=120368`, define

\[
X_n=\lfloor\sqrt{n!}\rfloor,
\qquad
Y_n=\left\lfloor\frac{X_n}{3}\right\rfloor,
\]

\[
r_n=\lceil4\log n\rceil,
\qquad
M_n=\lceil16(\log n)^2\rceil,
\]

\[
W_n=\left\lfloor\frac{2^{r_n}-3}{3}\right\rfloor.
\]

Let `m_n` be the largest odd integer at most `n`, and put

\[
L_n=m_n(2^{M_n}-1),
\qquad
P_n=L_n+W_n.
\]

The exact asymptotic final-only target range is

\[
P_n+1\le q\le Y_n.
\]

For `1<=t<=M_n`, let

\[
B_t(n)=
\{2^{t-1}u:
 u\text{ odd},\ 3u\mid n!,\ 2^{t-1}u\le Y_n\}.
\]

For a real common tilt `lambda`, let the independent coordinates satisfy

\[
\mathbb P_\lambda(Z_t=b)
=
\frac{e^{\lambda b}}{Z_t(\lambda)},
\qquad
b\in B_t(n)\cup\{0\},
\]

where

\[
Z_t(\lambda)=1+\sum_{b\in B_t(n)}e^{\lambda b}.
\]

Set

\[
T_{n,\lambda}=\sum_{t=1}^{M_n}Z_t,
\qquad
\Phi_{n,\lambda}(\theta)
=
\mathbb E_\lambda e^{i\theta T_{n,\lambda}}.
\]

For every target `q` in the post-prefix range, let `lambda_{n,q}` be the unique tilt from `N3-ANA-018` whose mean is `q-W_n/2`.

## Uniform zero-state bound in the first layer

Define

\[
s_n=\frac{8M_n\log L_n}{L_n}
\]

and

\[
\varepsilon_n=s_nm_n
=
\frac{8M_n\log L_n}{2^{M_n}-1}.
\]

By `N3-ANA-020`, every post-prefix target tilt satisfies

\[
\lambda_{n,q}>-s_n.
\]

The first-layer menu contains

\[
1,3,5,\ldots,m_n.
\]

Write

\[
k_n=\frac{m_n+1}{2}.
\]

For every displayed small state `b<=m_n`, one has

\[
e^{\lambda_{n,q}b}\ge e^{-\varepsilon_n}.
\]

Indeed, this is immediate when the tilt is nonnegative, and when it is negative it follows from `lambda_{n,q}>-s_n`.

Let

\[
p_{n,q}^{(0)}
=
\mathbb P_{\lambda_{n,q}}(Z_1=0)
=
\frac1{Z_1(\lambda_{n,q})}.
\]

Then

\[
Z_1(\lambda_{n,q})
\ge
1+k_ne^{-\varepsilon_n},
\]

so

\[
p_{n,q}^{(0)}
\le
\frac1{1+k_ne^{-\varepsilon_n}}
\le
\frac{e^{\varepsilon_n}}{k_n}
=
\frac{2e^{\varepsilon_n}}{m_n+1}.
\]

The quantity `epsilon_n` tends to zero superpolynomially in `n` because `M_n` is quadratic in `log n` and the denominator is `2^{M_n}`.

## N3-ANA-023: parity twin near-resonance

Result class: **disproved estimate with exact replacement identity**.

### Exact parity law

Every nonzero value in `B_1(n)` is odd. Every value in `B_t(n)` for `t>=2` is even. Therefore

\[
T_{n,\lambda}\text{ is even}
\quad\Longleftrightarrow\quad
Z_1=0.
\]

Consequently, for every post-prefix target,

\[
\mathbb P_{\lambda_{n,q}}
\{T_{n,\lambda_{n,q}}\text{ is even}\}
=p_{n,q}^{(0)}
\le
\frac{2e^{\varepsilon_n}}{m_n+1},
\]

and

\[
\mathbb P_{\lambda_{n,q}}
\{T_{n,\lambda_{n,q}}\text{ is odd}\}
\ge
1-rac{2e^{\varepsilon_n}}{m_n+1}.
\]

Thus the law has exact span one but is asymptotically concentrated on the odd residue class modulo two.

### Exact value at `pi`

For every `t>=2`,

\[
\phi_{t,\lambda}(\pi)=1.
\]

For the first layer,

\[
\phi_{1,\lambda}(\pi)
=p^{(0)}-(1-p^{(0)})
=2p^{(0)}-1.
\]

Hence

\[
\Phi_{n,\lambda_{n,q}}(\pi)
=2p_{n,q}^{(0)}-1,
\]

and therefore

\[
\left|\Phi_{n,\lambda_{n,q}}(\pi)\right|
=1-2p_{n,q}^{(0)}
\ge
1-rac{4e^{\varepsilon_n}}{m_n+1}.
\]

Uniformly over the entire exact post-prefix target range,

\[
\inf_{P_n<q\le Y_n}
\left|\Phi_{n,\lambda_{n,q}}(\pi)\right|
\longrightarrow1.
\]

This disproves any aggregate-dispersion theorem asserting a fixed positive lower bound on the complete dispersion sum throughout a minor arc that contains `pi`.

### Exact dispersion collapse at `pi`

For one coordinate define

\[
\mathcal D_{t,\lambda}(\theta)
=
\sum_{a,b}p_{t,\lambda}(a)p_{t,\lambda}(b)
\sin^2\left(\frac{(a-b)\theta}{2}\right).
\]

Then

\[
|\phi_{t,\lambda}(\theta)|^2
=1-2\mathcal D_{t,\lambda}(\theta).
\]

At `theta=pi`, every layer `t>=2` has zero dispersion, while

\[
\mathcal D_{1,\lambda}(\pi)
=2p^{(0)}(1-p^{(0)}).
\]

Thus

\[
\sum_{t=1}^{M_n}
\mathcal D_{t,\lambda_{n,q}}(\pi)
=2p_{n,q}^{(0)}(1-p_{n,q}^{(0)})
\le
\frac{4e^{\varepsilon_n}}{m_n+1}.
\]

The aggregate dispersion tends to zero at the nonzero torus frequency `pi`.

### Exact parity-twin identity

Let

\[
R_{n,\lambda}(u)
=
\prod_{t=2}^{M_n}
\phi_{t,\lambda}(u).
\]

Because first-layer nonzero states are odd,

\[
\phi_{1,\lambda}(\pi+u)
=2p^{(0)}-\phi_{1,\lambda}(u).
\]

Because all later-layer states are even,

\[
\phi_{t,\lambda}(\pi+u)
=\phi_{t,\lambda}(u)
\qquad(t>=2).
\]

Multiplication gives the exact torus identity

\[
\Phi_{n,\lambda}(\pi+u)
+
\Phi_{n,\lambda}(u)
=
2p^{(0)}R_{n,\lambda}(u).
\]

Hence, for every real `u`,

\[
\left|
\Phi_{n,\lambda_{n,q}}(\pi+u)
+
\Phi_{n,\lambda_{n,q}}(u)
\right|
\le
2p_{n,q}^{(0)}
\le
\frac{4e^{\varepsilon_n}}{m_n+1}.
\]

The characteristic function is uniformly almost anti-periodic under translation by `pi`.

## N3-ANA-024: parity mismatch obstruction for reference laws

Result class: **proved obstruction**.

Let `G` be any integer-valued reference law, and write

\[
G_{\rm even}=G(2\mathbb Z).
\]

Total variation distance satisfies

\[
d_{\rm TV}
\left(
\mathcal L(T_{n,\lambda_{n,q}}),G
\right)
\ge
\left|G_{\rm even}-p_{n,q}^{(0)}\right|.
\]

Therefore, if a proposed reference family has

\[
G_{\rm even}\ge\eta_n,
\]

then

\[
d_{\rm TV}
\left(
\mathcal L(T_{n,\lambda_{n,q}}),G
\right)
\ge
\eta_n-rac{2e^{\varepsilon_n}}{m_n+1}.
\]

In particular, no reference law assigning a fixed positive proportion of its mass to even integers can approximate the marker-three law in total variation on the post-prefix range.

This does not by itself disprove a window-specific weighted Fourier inequality. It proves that the reference law must encode the parity bias, or that the Fourier argument must include the `pi` major arc explicitly.

## N3-ANA-025: exact odd-lattice normalization

Result class: **proved theorem**.

The parity obstruction has an exact repair.

Condition on the overwhelmingly likely event

\[
Z_1\ne0.
\]

Define independent transformed coordinates by

\[
\widetilde Z_1
=
\frac{Z_1-1}{2}
\quad\text{under the conditional law }Z_1\ne0,
\]

and, for `t>=2`,

\[
\widetilde Z_t
=
\frac{Z_t}{2}.
\]

Then

\[
\widetilde T
=
\sum_{t=1}^{M_n}\widetilde Z_t
=
\frac{T_{n,\lambda}-1}{2}
\quad\text{conditional on }T_{n,\lambda}\text{ odd}.
\]

### Exact transformed supports

The first transformed support is

\[
\widetilde B_1(n)
=
\left\{
\frac{b-1}{2}:b\in B_1(n)
\right\}.
\]

For `t>=2`, the transformed support is

\[
\widetilde B_t(n)
=
\left\{
\frac b2:b\in B_t(n)
\right\}
\cup\{0\}.
\]

Since `1,3 in B_1(n)`, the first transformed support contains `0` and `1`. Therefore the transformed product law has exact additive span one.

### Exact transformed tilt

For the first coordinate, writing `b=2x+1`,

\[
e^{\lambda b}
=e^\lambda e^{2\lambda x}.
\]

The common factor `e^lambda` cancels under conditioning on `Z_1\ne0`. For every later coordinate, writing `b=2y`,

\[
e^{\lambda b}=e^{2\lambda y}.
\]

Thus the transformed coordinates are independent and share the exact common tilt

\[
\widetilde\lambda=2\lambda.
\]

On the post-prefix target range, `N3-ANA-020` gives

\[
-\frac{16M_n\log L_n}{L_n}
<
\widetilde\lambda_{n,q}
<
\frac{32(n\log n+\log14)}{2^{M_n}}.
\]

Hence the normalized odd-lattice tilt also tends uniformly to zero.

### Exact target-window map

Let

\[
I_{n,q}
=[q-W_n,q]\cap\mathbb Z.
\]

The odd integers in this window correspond bijectively under `m=2x+1` to

\[
J_{n,q}
=
\left[
\left\lceil\frac{q-W_n-1}{2}\right\rceil,
\left\lfloor\frac{q-1}{2}\right\rfloor
\right]
\cap\mathbb Z.
\]

Therefore

\[
\mathbb P_\lambda
\{T_{n,\lambda}\in I_{n,q}\}
\ge
(1-p^{(0)})
\mathbb P_{2\lambda}
\{\widetilde T\in J_{n,q}\}.
\]

Since

\[
1-p^{(0)}
\ge
1-rac{2e^{\varepsilon_n}}{m_n+1},
\]

positive mass for the transformed interval proves positive mass for the original interval.

The transformed window has either

\[
\left\lfloor\frac{W_n+1}{2}\right\rfloor
\quad\text{or}\quad
\left\lceil\frac{W_n+1}{2}\right\rceil
\]

integer points.

### Interpretation

The exact span-one statement for the original law concealed an asymptotic parity collapse. The correct final-only Fourier route is:

1. isolate the negligible even component;
2. pass to the exact odd conditional law;
3. divide by two and shift by one;
4. prove aggregate phase dispersion for the normalized product law;
5. use a collision-aware reference law on the transformed integer lattice.

This normalization removes the forced `pi` twin resonance. It does not prove that no additional secondary resonance remains.

## Claim boundary

The following remain open:

- aggregate phase dispersion for the normalized odd-lattice law;
- uniform variance, third-moment, and maximal-step estimates;
- a collision-aware local reference law;
- the strict weighted Fourier inequality;
- quotient occupancy;
- the factorial half-range theorem;
- Erdős Problem 18.
