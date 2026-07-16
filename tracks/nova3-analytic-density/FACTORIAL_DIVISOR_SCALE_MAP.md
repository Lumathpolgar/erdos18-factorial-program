# Factorial Divisor Scale Map

## Status and notation

Status labels in this file are attached to each claim. Let

\[
b_p=v_p(n!),\qquad \mathcal A_n=\prod_{p\le n}\{0,1,\ldots,b_p\},
\]

\[
S_n(a)=\sum_{p\le n}a_p\log p,\qquad d(a)=e^{S_n(a)},
\]

and for `Delta >= 0`,

\[
L_n(u,\Delta)=\#\{a\in\mathcal A_n:u\le S_n(a)\le u+\Delta\}.
\]

This counts exact divisors of `n!` in the closed multiplicative window `[e^u,e^{u+Delta}]`.

## 1. Total logarithmic scale

### N3-ANA-004A, explicit factorial size

Status: `PROVED`.

Robbins' explicit Stirling bounds give, for every integer `n>=1`,

\[
\log(n!)=\left(n+\frac12\right)\log n-n+\frac12\log(2\pi)+r_n,
\]

with

\[
\frac1{12n+1}<r_n<\frac1{12n}.
\]

Consequently,

\[
\frac12\log(n!)=\frac n2\log n-\frac n2+O(\log n).
\]

The project half-range endpoint `sqrt(n!)` is therefore at logarithmic scale `Theta(n log n)`.

## 2. Exact valuation budgets by prime band

### Fixed-prime and low-prime regime

Status: `PROVED`.

For every prime `p<=n`,

\[
b_p=\frac{n}{p-1}+O\left(\frac{\log n}{\log p}\right).
\]

For fixed `p`, `b_p/n -> 1/(p-1)`.

### High-prime bands

Status: `PROVED`.

For `p>sqrt(n)`,

\[
b_p=\left\lfloor\frac np\right\rfloor.
\]

Thus for integers `1<=k<sqrt(n)`,

\[
\frac{n}{k+1}<p\le\frac nk
\quad\Longrightarrow\quad b_p=k.
\]

The exact entropy contribution of this band is

\[
E_k(n)=\log(k+1)\left\{\pi(n/k)-\pi(n/(k+1))\right\},
\]

up to the harmless endpoint restriction `p>sqrt(n)` when `k` approaches `sqrt(n)`.

Examples:

- `n/2<p<=n`: exponent budget `1`, entropy per prime `log 2`.
- `n/3<p<=n/2`: exponent budget `2`, entropy per prime `log 3`.
- `n/4<p<=n/3`: exponent budget `3`, entropy per prime `log 4`.

## 3. Total divisor entropy

### N3-ANA-004B, asymptotic divisor count

Status: `PROVED`, conditional only on the prime number theorem as an external theorem.

Define

\[
C_\tau=\sum_{k\ge1}\frac{\log(k+1)}{k(k+1)}=1.2577\ldots.
\]

Then

\[
\log\tau(n!)=C_\tau\frac{n}{\log n}+o\left(\frac n{\log n}\right).
\]

Proof outline: primes at most `sqrt(n)` contribute `O(sqrt(n))`. For larger primes, group by `b_p=k`. For each fixed `K`, the prime number theorem evaluates the bands `k<=K`; partial summation and `pi(x) << x/log x` bound the tail by

\[
O\left(\frac n{\log n}\frac{\log K}{K}\right)+O(\sqrt n\log n).
\]

First let `n` tend to infinity and then `K` tend to infinity.

Hence

\[
\tau(n!)=\exp\left((C_\tau+o(1))\frac n{\log n}\right).
\]

This is enormous but remains only a global profile count.

## 4. Exact product measure and exponential tilt

Choose a divisor uniformly from `D(n!)`. Equivalently, the exponent variables `A_p` are independent and uniform on `{0,...,b_p}`. Put

\[
S_n=\sum_{p\le n}A_p\log p.
\]

### Uniform mean and covariance

Status: `PROVED`.

\[
\mathbb E A_p=\frac{b_p}{2},\qquad
\operatorname{Var}(A_p)=\frac{b_p(b_p+2)}{12},
\]

and distinct exponent coordinates have covariance zero. Therefore

\[
\mathbb E S_n=\frac12\log(n!),
\]

\[
V_n:=\operatorname{Var}(S_n)
=\frac1{12}\sum_{p\le n}b_p(b_p+2)(\log p)^2.
\]

Moreover,

\[
\frac{V_n}{n^2}\longrightarrow
\sigma_*^2:=\frac1{12}\sum_p\frac{(\log p)^2}{(p-1)^2}
=0.11546\ldots.
\]

Thus the standard deviation of `log d` is `Theta(n)`, much smaller than the total half-range scale `Theta(n log n)`.

### Effective dimension

Status: `PROVED` for the limiting formula; numerical value is `COMPUTATIONAL_EVIDENCE`.

If the variance participation ratio is defined by

\[
d_{\mathrm{eff}}(n)=
\frac{V_n^2}{\sum_{p\le n}\operatorname{Var}(A_p\log p)^2},
\]

then

\[
d_{\mathrm{eff}}(n)\to
\frac{\left(\sum_p c_p\right)^2}{\sum_p c_p^2},
\qquad
c_p=\frac{(\log p)^2}{12(p-1)^2}.
\]

Numerically the limit is about `5.22`. The prime `2` alone contributes about `34.7%` of limiting variance and prime `3` about `21.8%`. The full uniform-divisor model therefore does not acquire growing effective dimension.

### Exponential tilt

Status: `PROVED`.

For real `theta`, define

\[
K_n(\theta)=\sum_{p\le n}\log\left(\sum_{j=0}^{b_p}e^{\theta j\log p}\right).
\]

The tilted product measure is

\[
\mathbb P_\theta(A_p=j)=
\frac{e^{\theta j\log p}}{\sum_{r=0}^{b_p}e^{\theta r\log p}}.
\]

Then

\[
M_n(\theta)=K_n'(\theta)=\mathbb E_\theta S_n,
\qquad
B_n(\theta)^2=K_n''(\theta)=\operatorname{Var}_\theta(S_n).
\]

`M_n(theta)` is continuous and strictly increasing from `0` to `log(n!)`. Therefore every target `u` strictly between those endpoints has a unique saddle parameter satisfying `M_n(theta)=u`.

The exact change-of-measure identity is

\[
L_n(u,\Delta)=e^{K_n(\theta)}
\mathbb E_\theta\left[e^{-\theta S_n}
\mathbf 1_{[u,u+\Delta]}(S_n)\right].
\]

The unresolved analytic task is a sufficiently uniform lower estimate for the tilted window probability.

## 5. Representative logarithmic scales

### Polynomial scale `u=A log n`

Status: `PROVED` bounds.

For fixed `A>0` and sufficiently large `n`, powers of `2` alone give

\[
\#\{d\mid n!:d\le n^A\}\ge
\left\lfloor\frac{A\log n}{\log2}\right\rfloor+1,
\]

because `b_2` is linear in `n`. The trivial exact-set upper bound is

\[
\#\{d\mid n!:d\le n^A\}\le\lfloor n^A\rfloor.
\]

These bounds are far apart. No uniform local asymptotic at polynomial scale is currently proved.

### Linear logarithmic scale `u=alpha n`

Status: `OPEN` for uniform local counts.

This is the natural scale of fluctuations under the uniform divisor measure. It is also where small-prime exponent coordinates dominate variance. A Gaussian model for the full exponent vector is false.

### Central scale

Status: `PROVED` symmetry and concentration.

The involution `d -> n!/d` gives

\[
L_n(u,\Delta)=L_n(\log(n!)-u-\Delta,\Delta).
\]

Chebyshev gives

\[
\#\left\{d\mid n!:\left|\log d-\frac12\log(n!)\right|\le2\sqrt{V_n}\right\}
\ge\frac34\tau(n!).
\]

This proves high average density in a central band of width `Theta(n)`, but not a lower bound for every subwindow.

### Half-range endpoint

Status: `PROVED` location; local density `OPEN`.

The endpoint is `u=floor`-equivalent to `0.5 log(n!)`. Divisor-complement symmetry places it exactly at the mean of the uniform model. This is favorable for global mass but does not eliminate possible short gaps.

## 6. Lattice span and periodicity

### No positive lattice span

Status: `PROVED`.

If integers `m_p` satisfy

\[
\sum_{p\le n}m_p\log p=0,
\]

then unique factorization gives `m_p=0` for every prime. In particular, `log2/log3` is irrational, so the weights do not lie in a common positive lattice.

### Quantitative warning

Status: `PROVED` obstruction.

For each fixed `n`, the characteristic function of `S_n` is almost periodic and has values arbitrarily close to `1` at arbitrarily large frequencies. Therefore no estimate of the form

\[
|\phi_n(t)|\le\rho<1\quad\text{for all }|t|\ge T
\]

can hold. Any minor-arc theorem must restrict the frequency range, average over frequencies, introduce smoothing, or exploit a growing subfamily with quantified Diophantine separation.

## 7. Corrected Gaussian component

Let `y=y(n)` tend to infinity and retain only primes `p>y`. Write

\[
T_{n,y}=\sum_{y<p\le n}\left(A_p-\frac{b_p}{2}\right)\log p,
\qquad B_{n,y}^2=\operatorname{Var}(T_{n,y}).
\]

### N3-ANA-008, high-prime tail central limit theorem

Status: `PROVED` when `y->infinity` and `2y<=sqrt(n)`.

\[
\frac{T_{n,y}}{B_{n,y}}\Rightarrow N(0,1).
\]

In this range,

\[
B_{n,y}^2\gg n^2\frac{\log y}{y},
\]

while the largest coordinate span is

\[
M_{n,y}\ll n\frac{\log y}{y}.
\]

Hence

\[
\frac{M_{n,y}}{B_{n,y}}\ll\sqrt{\frac{\log y}{y}}\to0,
\]

which gives the Lindeberg condition.

A Berry-Esseen argument yields useful coarse window positivity only when the window width is larger than a constant multiple of `M_{n,y}`. A true local theorem below that scale remains open.

## 8. Exact local-count ceiling

### N3-ANA-005

Status: `PROVED`.

For every prime `q<=n`, every real `u`, and every `Delta>=0`,

\[
L_n(u,\Delta)
\le
\tau(n!)\frac{\lfloor\Delta/\log q\rfloor+1}{b_q+1}.
\]

Condition on all exponent coordinates except `a_q`. The permitted values of `a_q log q` are separated by `log q`, so the window contains at most `floor(Delta/log q)+1` of the `b_q+1` equiprobable choices.

For fixed `Delta`, choosing `q=2` gives

\[
L_n(u,\Delta)\ll_\Delta\frac{\tau(n!)}{n}
\]

uniformly in `u`.

This is a ceiling, not a lower bound.

## 9. Mean spacing versus maximum gap

Status: `PROVED` obstruction.

The mean logarithmic spacing over the whole divisor range is

\[
\frac{\log(n!)}{\tau(n!)-1},
\]

which is exponentially small in `n/log n`. Nevertheless the first two logarithmic divisor values are `0` and `log2`, so the maximum logarithmic gap is at least `log2` for every `n>=2`.

Thus mean spacing cannot establish a global maximum-gap theorem. Even in the central band, high average occupancy from Chebyshev does not prevent an empty short window.

## 10. Candidate window widths

- Full uniform model, unconditioned: scale `Theta(n)` is natural, but the limit law is non-Gaussian.
- High-prime tail after cutoff `y`: standard deviation at least order `n sqrt(log y/y)`.
- Berry-Esseen-positive windows for that tail: currently require width `Delta >> n log y/y`.
- Windows substantially below the maximum coordinate span require a genuine characteristic-function or local-limit theorem.
- Fixed-width uniform lower bounds cannot include the endpoint `u=0`; for `0<=Delta<log2`, `L_n(0,Delta)=1`.

## 11. What this map does not claim

- It does not prove INT-002.
- It does not prove a maximum-gap bound for factorial divisors.
- It does not transfer smooth-number lower bounds to factorial divisors.
- It does not claim a local central limit theorem for the full exponent vector.
- It does not turn central divisor density into additive coverage.
