# Parity Twin Resonance and Exact Odd-Lattice Reduction

## Scope

This file studies the exact marker-three numerical quotient law. It does not substitute logarithmic divisor size.

Imported current heads:

- Nova 1: `nova/factorial-structure@1b81ec74f907d57d520bcf6c51f2e6e71f0474a7`;
- Nova 2: `nova/additive-occupancy@e443674f86b2ee3c7037ac94ee47f6b8a4b3b29f`.

Dependencies: `N3-ANA-018` and `N3-ANA-020`.

The factorial half-range theorem remains open.

## Frozen notation

For every integer `n>=120368`, define

\[
Y_n=\left\lfloor\frac{\lfloor\sqrt{n!}\rfloor}{3}\right\rfloor,
\qquad
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

The exact final-only target range is

\[
P_n+1\le q\le Y_n.
\]

For `1<=t<=M_n`, define

\[
B_t(n)=
\{2^{t-1}u:
 u\text{ odd},\ 3u\mid n!,\ 2^{t-1}u\le Y_n\}.
\]

Under a real common tilt `lambda`, let independent variables satisfy

\[
\mathbb P_\lambda(Z_t=b)
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
=\mathbb E_\lambda e^{i\theta T_{n,\lambda}}.
\]

For every post-prefix target, let `lambda_{n,q}` be the unique centering tilt from `N3-ANA-018`.

## Uniform first-layer zero-state bound

Define

\[
s_n=\frac{8M_n\log L_n}{L_n},
\qquad
\varepsilon_n=s_nm_n
=\frac{8M_n\log L_n}{2^{M_n}-1}.
\]

By `N3-ANA-020`,

\[
\lambda_{n,q}>-s_n.
\]

The first-layer menu contains

\[
1,3,5,\ldots,m_n.
\]

There are

\[
k_n=\frac{m_n+1}{2}
\]

such states. For each of them,

\[
e^{\lambda_{n,q}b}\ge e^{-\varepsilon_n}.
\]

Let

\[
p_{n,q}^{(0)}
=\mathbb P_{\lambda_{n,q}}(Z_1=0).
\]

Then

\[
p_{n,q}^{(0)}
\le
\frac{1}{1+k_ne^{-\varepsilon_n}}
\le
\frac{2e^{\varepsilon_n}}{m_n+1}.
\]

The quantity `epsilon_n` tends to zero faster than every negative power of `n`.

## N3-ANA-023: parity twin near-resonance

Result class: **disproved estimate with exact replacement identity**.

### Exact parity law

Every nonzero state in `B_1(n)` is odd. Every state in `B_t(n)` for `t>=2` is even. Therefore

\[
T_{n,\lambda}\text{ is even}
\quad\Longleftrightarrow\quad
Z_1=0.
\]

Consequently,

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
1-\frac{2e^{\varepsilon_n}}{m_n+1}.
\]

The law has exact span one but is asymptotically concentrated on odd integers.

### Exact value at `pi`

For every `t>=2`,

\[
\phi_{t,\lambda}(\pi)=1.
\]

For the first layer,

\[
\phi_{1,\lambda}(\pi)
=2p^{(0)}-1.
\]

Hence

\[
\Phi_{n,\lambda_{n,q}}(\pi)
=2p_{n,q}^{(0)}-1,
\]

and

\[
\left|\Phi_{n,\lambda_{n,q}}(\pi)\right|
\ge
1-\frac{4e^{\varepsilon_n}}{m_n+1}.
\]

Uniformly over the post-prefix target range,

\[
\inf_{P_n<q\le Y_n}
\left|\Phi_{n,\lambda_{n,q}}(\pi)\right|
\longrightarrow1.
\]

Thus no minor arc containing `pi` can have a fixed positive aggregate-dispersion lower bound.

### Exact dispersion collapse

Define

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

At `theta=pi`, every layer `t>=2` has zero dispersion and

\[
\mathcal D_{1,\lambda}(\pi)
=2p^{(0)}(1-p^{(0)}).
\]

Therefore

\[
\sum_{t=1}^{M_n}
\mathcal D_{t,\lambda_{n,q}}(\pi)
\le
\frac{4e^{\varepsilon_n}}{m_n+1}.
\]

### Exact twin identity

Let

\[
R_{n,\lambda}(u)
=
\prod_{t=2}^{M_n}\phi_{t,\lambda}(u).
\]

Odd first-layer states give

\[
\phi_{1,\lambda}(\pi+u)
=2p^{(0)}-\phi_{1,\lambda}(u),
\]

while even later-layer states give

\[
\phi_{t,\lambda}(\pi+u)
=\phi_{t,\lambda}(u)
\qquad(t>=2).
\]

Hence

\[
\Phi_{n,\lambda}(\pi+u)
+
\Phi_{n,\lambda}(u)
=
2p^{(0)}R_{n,\lambda}(u).
\]

In particular,

\[
\left|
\Phi_{n,\lambda_{n,q}}(\pi+u)
+
\Phi_{n,\lambda_{n,q}}(u)
\right|
\le
\frac{4e^{\varepsilon_n}}{m_n+1}.
\]

The characteristic function is uniformly almost anti-periodic under translation by `pi`.

## N3-ANA-024: parity mismatch obstruction

Result class: **proved obstruction**.

Let `G` be any integer-valued reference law. Since total variation dominates the discrepancy of every event,

\[
d_{\rm TV}
\left(\mathcal L(T_{n,\lambda_{n,q}}),G\right)
\ge
\left|G(2\mathbb Z)-p_{n,q}^{(0)}\right|.
\]

If `G(2Z)>=eta_n`, then

\[
d_{\rm TV}
\left(\mathcal L(T_{n,\lambda_{n,q}}),G\right)
\ge
\eta_n-\frac{2e^{\varepsilon_n}}{m_n+1}.
\]

Thus a reference law assigning a fixed positive mass to even integers cannot approximate the post-prefix law in total variation.

This does not by itself disprove a window-specific weighted Fourier inequality. It forces parity into the reference law or major-arc decomposition.

## N3-ANA-025: exact odd-lattice normalization

Result class: **proved theorem**.

Condition on `Z_1!=0` and define

\[
\widetilde Z_1=\frac{Z_1-1}{2},
\qquad
\widetilde Z_t=\frac{Z_t}{2}
\quad(t>=2).
\]

Then

\[
\widetilde T
=\sum_{t=1}^{M_n}\widetilde Z_t
=\frac{T_{n,\lambda}-1}{2}
\]

under the odd conditional law.

### Transformed supports and span

The first transformed support is

\[
\widetilde B_1(n)
=
\left\{\frac{b-1}{2}:b\in B_1(n)\right\}.
\]

For `t>=2`, the transformed support is

\[
\widetilde B_t(n)
=
\{0\}\cup
\left\{\frac b2:b\in B_t(n)\right\}.
\]

Since `1,3 in B_1(n)`, the first transformed support contains `0` and `1`. The transformed product law has exact span one.

### Transformed independence and tilt

For the first coordinate, write `b=2x+1`. Then

\[
e^{\lambda b}=e^\lambda e^{2\lambda x},
\]

and the common factor cancels under conditioning. For every later coordinate, write `b=2y`, so

\[
e^{\lambda b}=e^{2\lambda y}.
\]

The transformed coordinates remain independent and share common tilt

\[
\widetilde\lambda=2\lambda.
\]

Thus, on the post-prefix range,

\[
-\frac{16M_n\log L_n}{L_n}
<\widetilde\lambda_{n,q}<
\frac{32(n\log n+\log14)}{2^{M_n}}.
\]

### Transformed target window

Let

\[
I_{n,q}=[q-W_n,q]\cap\mathbb Z.
\]

The odd integers in `I_{n,q}` correspond under `m=2x+1` to

\[
J_{n,q}
=
\left[
\left\lceil\frac{q-W_n-1}{2}\right\rceil,
\left\lfloor\frac{q-1}{2}\right\rfloor
\right]\cap\mathbb Z.
\]

Therefore

\[
\mathbb P_\lambda\{T_{n,\lambda}\in I_{n,q}\}
\ge
(1-p^{(0)})
\mathbb P_{2\lambda}\{\widetilde T\in J_{n,q}\}.
\]

Since

\[
1-p^{(0)}
\ge
1-\frac{2e^{\varepsilon_n}}{m_n+1},
\]

positive transformed-window mass proves positive original-window mass.

The transformed window has either floor or ceiling of `(W_n+1)/2` integer points.

## Route consequence

The correct final-only Fourier route is:

1. isolate the negligible even component;
2. condition on the odd component;
3. subtract one and divide by two;
4. audit all transformed secondary resonances;
5. prove transformed aggregate phase dispersion or a transformed weighted integral estimate;
6. use a collision-aware transformed reference law.

The normalization removes the forced original `pi` twin. It does not prove that no transformed secondary resonance remains.

## Claim boundary

Still open:

- the transformed resonance audit;
- transformed aggregate phase dispersion;
- transformed moments;
- collision-aware local approximation;
- the strict transformed weighted Fourier inequality;
- quotient occupancy;
- the factorial half-range theorem;
- Erdős Problem 18.
