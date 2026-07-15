# Post-Prefix Numerical Tilt Compression and Collision Law

## Scope

This file works with the exact marker-three numerical quotient law. It does not use logarithmic divisor size as a surrogate.

Imported structural and additive sources:

- Nova 1 branch `nova/factorial-structure`, commit `e3a0e3f5fb335b23afdd9e1fe418ac46ca1c766a`;
- Nova 2 branch `nova/additive-occupancy`, commit `82603c631a106c3bff4676bdeeb9cc791fc98f3c`;
- Nova 1 results `N1-STR-020`, `N1-DIS-006`, and `N1-COL-001`;
- Nova 2 results `N2-ADD-119` and `N2-ADD-120`;
- Nova 3 results `N3-ANA-014` and `N3-ANA-018`.

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

Nova 2 proves deterministic quotient-window occupancy through `P_n`. Thus the first asymptotic targets requiring a final-only analytic argument are

\[
P_n+1\le q\le Y_n.
\]

This interval is nonempty. Indeed, Nova 1 theorem `N1-DIS-006` gives

\[
(W_n+1)(1+n/2)^{M_n}<Y_n.
\]

For the present range, the elementary inequality

\[
P_n+1\le(W_n+1)(1+n/2)^{M_n}
\]

holds, so `P_n<Y_n`.

For `1<=t<=M_n`, define

\[
B_t(n)=
\{2^{t-1}u:
 u\text{ odd},\ 3u\mid n!,\ 2^{t-1}u\le Y_n\}.
\]

Under the common numerical exponential tilt `lambda`, let independent variables satisfy

\[
\mathbb P_\lambda(Z_t=b)=
\frac{e^{\lambda b}}
{Z_t(\lambda)},
\qquad
b\in B_t(n)\cup\{0\},
\]

where

\[
Z_t(\lambda)=
1+\sum_{b\in B_t(n)}e^{\lambda b}.
\]

Write

\[
T_{n,\lambda}=\sum_{t=1}^{M_n}Z_t,
\qquad
\mu_n(\lambda)=\mathbb E_\lambda T_{n,\lambda}.
\]

For a target `q`, freeze the center

\[
\xi_{n,q}=q-\frac{W_n}{2}.
\]

By `N3-ANA-018`, there is a unique finite `lambda_{n,q}` with

\[
\mu_n(\lambda_{n,q})=\xi_{n,q}.
\]

## N3-ANA-020: uniform post-prefix tilt compression

Result class: **proved theorem**.

For every integer `n>=120368` and every integer target

\[
P_n+1\le q\le Y_n,
\]

the unique common numerical tilt satisfies

\[
-\frac{8M_n\log L_n}{L_n}
<
\lambda_{n,q}
<
\frac{16\bigl(n\log n+\log14\bigr)}{2^{M_n}}.
\]

Consequently

\[
\sup_{P_n<q\le Y_n}|\lambda_{n,q}|\to0
\qquad(n\to\infty).
\]

Thus the entire asymptotic post-prefix target range is centered by a common tilt that shrinks uniformly to zero.

### Lower bound on the tilt

Put `lambda=-s` with `s>0`. For one layer define

\[
f_t(s)=\log Z_t(-s).
\]

The function `f_t` is convex and

\[
f_t'(s)=-\mathbb E_{-s}Z_t.
\]

The tangent inequality at `s` evaluated at `s/2` gives

\[
f_t(s/2)
\ge
f_t(s)+\frac{s}{2}\mathbb E_{-s}Z_t.
\]

Since `f_t(s)>=0`,

\[
\mathbb E_{-s}Z_t
\le
\frac{2}{s}f_t(s/2).
\]

Every state in layer `t` is a nonnegative multiple of

\[
a_t=2^{t-1}.
\]

Therefore

\[
Z_t(-s/2)
\le
\sum_{k=0}^{\infty}e^{-sa_tk/2}
=
\frac1{1-e^{-sa_t/2}}.
\]

Using

\[
1-e^{-x}\ge\frac{x}{1+x}
\qquad(x>0),
\]

we obtain

\[
f_t(s/2)
\le
\log\left(1+\frac{2}{sa_t}\right)
\le
\log\left(1+\frac2s\right).
\]

Summing over the layers gives the universal negative-tilt estimate

\[
\mu_n(-s)
\le
\frac{2M_n}{s}
\log\left(1+\frac2s\right).
\]

Set

\[
s_n=\frac{8M_n\log L_n}{L_n}.
\]

For `L_n>=3`,

\[
1+\frac2{s_n}
=
1+\frac{L_n}{4M_n\log L_n}
\le L_n.
\]

Hence

\[
\mu_n(-s_n)
\le
\frac{2M_n}{s_n}\log L_n
=
\frac{L_n}{4}.
\]

For every post-prefix target,

\[
\xi_{n,q}
=q-\frac{W_n}{2}
\ge
L_n+1+\frac{W_n}{2}
>L_n.
\]

Since `mu_n` is strictly increasing, its solution cannot satisfy `lambda_{n,q}<=-s_n`. This proves the lower bound.

### Upper bound on the tilt

By Nova 1 theorem `N1-STR-020`, every admissible layer contains a value `b_t` satisfying

\[
\frac{Y_n}{3}<b_t\le Y_n.
\]

All states in layer `t` are multiples of `a_t=2^{t-1}`. Split the states into those below `b_t` and those at least `b_t`.

The number of layer states is at most

\[
|B_t(n)|+1\le n!+1.
\]

For `lambda>=0`, the total weight below `b_t` is at most

\[
(n!+1)e^{\lambda(b_t-a_t)},
\]

while the weight at or above `b_t` is at least `e^{\lambda b_t}`. Therefore

\[
\mathbb P_\lambda\{Z_t\ge b_t\}
\ge
\frac1{1+(n!+1)e^{-\lambda a_t}}.
\]

Use the four highest layers

\[
t=M_n-3,M_n-2,M_n-1,M_n.
\]

For each of them,

\[
a_t\ge2^{M_n-4}.
\]

If

\[
\lambda
\ge
\frac{16\log(7(n!+1))}{2^{M_n}},
\]

then every one of these four layers satisfies

\[
(n!+1)e^{-\lambda a_t}\le\frac17,
\]

and hence

\[
\mathbb P_\lambda\{Z_t\ge b_t\}\ge\frac78.
\]

It follows that

\[
\mu_n(\lambda)
>
4\cdot\frac78\cdot\frac{Y_n}{3}
=
\frac76Y_n
>Y_n.
\]

But every required center satisfies `xi_{n,q}<=Y_n`. Therefore

\[
\lambda_{n,q}
<
\frac{16\log(7(n!+1))}{2^{M_n}}.
\]

Finally,

\[
\log(7(n!+1))
\le n\log n+\log14,
\]

which gives the displayed elementary upper bound.

### Uniform convergence

The lower magnitude is

\[
\frac{8M_n\log L_n}{L_n}
=
\exp(-\Omega((\log n)^2)),
\]

because `L_n` contains the factor `2^{M_n}`.

The upper magnitude satisfies

\[
\frac{16(n\log n+\log14)}{2^{M_n}}
=
\exp(-\Omega((\log n)^2)).
\]

Both tend to zero uniformly.

## N3-ANA-021: compact tilt does not preserve the binary-anchor coefficient

Result class: **disproved estimate**.

The following inference is false:

> A common numerical tilt confined to a compact interval, or even tending uniformly to zero, automatically gives a positive uniform lower bound for the zero-versus-minimum-state coefficient in the minor-arc estimate.

At zero tilt, every state in layer `t` is equiprobable. Since `N3-ANA-014` gives

\[
|B_t(n)|\ge2^{h_n-1},
\qquad
h_n=\pi(n)-\pi(n/2),
\]

we have

\[
\mathbb P_0(Z_t=0)
=
\mathbb P_0(Z_t=2^{t-1})
=
\frac1{|B_t(n)|+1}.
\]

Thus

\[
\mathbb P_0(Z_t=0)
\mathbb P_0(Z_t=2^{t-1})
<
2^{-2(h_n-1)}
\le
2^{-2(n/(3\log n)-1)}.
\]

This tends to zero exponentially in `n/log n`.

Therefore the two-state estimate from `N3-ANA-018`, although exact, cannot by itself provide a target-uniform quantitative minor-arc bound merely from the conclusion `lambda_{n,q}->0`.

A successful proof must aggregate many phase-separated states, use a divisor-gap theorem, or control a target-local collection of coordinate probabilities.

## N3-ANA-022: collision multiplicity enters the tilted atom exactly

Result class: **proved theorem**.

Let

\[
\mathcal A_n=
\prod_{t=1}^{M_n}(B_t(n)\cup\{0\})
\]

be the profile space. For an integer `s`, define the exact profile multiplicity

\[
C_n(s)=
\#\left\{
(b_1,\ldots,b_{M_n})\in\mathcal A_n:
\sum_tb_t=s
\right\}.
\]

Under the common tilt,

\[
\mathbb P_\lambda\{T_{n,\lambda}=s\}
=
\frac{C_n(s)e^{\lambda s}}
{\prod_{t=1}^{M_n}Z_t(\lambda)}.
\]

Indeed, every profile in the fiber over `s` has the same numerator `e^{lambda s}`.

Nova 1 theorem `N1-COL-001` gives, with

\[
J_n=\left\lfloor\frac{M_n}{2}\right\rfloor,
\qquad
S_n=4^{J_n}-1,
\]

\[
C_n(S_n)\ge2^{J_n}.
\]

Consequently, for every real tilt,

\[
\mathbb P_\lambda\{T_{n,\lambda}=S_n\}
\ge
\frac{2^{J_n}e^{\lambda S_n}}
{\prod_{t=1}^{M_n}Z_t(\lambda)}.
\]

This does not obstruct occupancy. It proves that any local reference law or saddle-point approximation must be collision-aware: the atom coefficient is the exact numerical fiber multiplicity, not the number of abstract profile choices treated as distinct sums.

## Interpretation

`N3-ANA-020` closes the compact-tilt part of `N3-NEXT-005` on the exact asymptotic post-prefix target range.

It does not close the local theorem. `N3-ANA-021` shows why: numerical tilt compression alone does not preserve the simplest phase-dispersion coefficient.

The next analytic task is to replace the single binary anchor by an aggregate phase-dispersion theorem for the complete odd-core menus, while retaining the exact collision multiplicities from `N3-ANA-022`.

## Claim boundary

No result in this file proves:

- marker-three quotient occupancy;
- a uniform variance lower bound;
- the strict weighted Fourier inequality;
- the factorial half-range theorem;
- Erdős Problem 18.