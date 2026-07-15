# Product-Model Theorems for Divisors of `n!`

## N3-ANA-004, exact tilted product model

- Result class: `proved theorem`
- Repository status: `PROVED`
- Hypotheses: integer `n>=2`; primes `p<=n`; `b_p=v_p(n!)`; exponent vectors `0<=a_p<=b_p`.
- Constants: exact; no ineffective constants.
- Distinctness mechanism: unique factorization gives a bijection between exponent vectors and numerical divisors.
- Boundary treatment: all finite `n>=2` are included.

### Statement

Under the uniform measure on divisors of `n!`, the exponent coordinates `A_p` are independent and uniform on `{0,...,b_p}`. For

\[
S_n=\sum_{p\le n}A_p\log p,
\]

we have

\[
\mathbb E S_n=\frac12\log(n!),
\]

\[
\operatorname{Var}(S_n)=\frac1{12}\sum_{p\le n}b_p(b_p+2)(\log p)^2.
\]

For real `theta`, define

\[
K_n(\theta)=\sum_{p\le n}\log\sum_{j=0}^{b_p}e^{\theta j\log p}.
\]

Then the exponential tilt

\[
\mathbb P_\theta(A_p=j)=
\frac{e^{\theta j\log p}}{\sum_{r=0}^{b_p}e^{\theta r\log p}}
\]

has independent coordinates and satisfies

\[
K_n'(\theta)=\mathbb E_\theta S_n,
\qquad K_n''(\theta)=\operatorname{Var}_\theta(S_n)>0.
\]

Thus `K_n'` is strictly increasing from `0` to `log(n!)`, and every `u` in that open interval has a unique saddle parameter.

### Proof

The divisor-vector bijection makes the uniform measure the product of the uniform coordinate measures. The mean and variance of a uniform integer on `{0,...,b}` are `b/2` and `b(b+2)/12`. Independence gives the displayed formulas.

The tilted partition function factors coordinatewise. Differentiation of its logarithm gives the mean and variance. Strict positivity follows because at least one coordinate is nonconstant for `n>=2`. The endpoint limits follow by concentration of each finite coordinate distribution at `0` as `theta->-infinity` and at `b_p` as `theta->+infinity`.

## N3-ANA-005, exact uniform local-count ceiling

- Result class: `proved theorem`
- Repository status: `PROVED`
- Hypotheses: integer `n>=2`; real `u`; real `Delta>=0`; prime `q<=n`.
- Constants: exact.
- Parameter range: all stated parameters.
- Boundary treatment: closed logarithmic window `[u,u+Delta]`.

### Statement

Let

\[
L_n(u,\Delta)=\#\{d\mid n!:e^u\le d\le e^{u+\Delta}\}.
\]

Then

\[
L_n(u,\Delta)
\le
\tau(n!)\frac{\lfloor\Delta/\log q\rfloor+1}{v_q(n!)+1}.
\]

In particular, for fixed `Delta`,

\[
L_n(u,\Delta)\ll_\Delta \frac{\tau(n!)}n
\]

uniformly in `u`.

### Proof

Fix every exponent except `a_q`. For the fixed remaining coordinates, membership in the window restricts `a_q log q` to an interval of length `Delta`. The possible values are separated by `log q`, so there are at most `floor(Delta/log q)+1` admissible values of `a_q`. There are exactly `tau(n!)/(b_q+1)` choices of the remaining coordinates. Multiplication gives the bound. For `q=2`, Legendre's formula gives `b_2(n!)=n-s_2(n)`, hence `b_2+1` is of order `n`.

### Sharp endpoint obstruction

For `0<=Delta<log 2`,

\[
L_n(0,\Delta)=1.
\]

Therefore no lower bound growing with `tau(n!)` can hold uniformly from `u=0` in fixed-width windows.

## N3-ANA-006, non-Gaussian limit for the full uniform-divisor model

- Result class: `proved theorem`
- Repository status: `PROVED`
- Hypotheses: `n->infinity`; uniform divisor of `n!`.
- Constants: exact limiting series.
- External dependencies: none beyond elementary convergence and unique factorization.

### Statement

Let

\[
X_n=\frac{S_n-\frac12\log(n!)}n.
\]

For every prime `p`, let `U_p` be independent and uniform on

\[
\left[-\frac1{2(p-1)},\frac1{2(p-1)}\right].
\]

Then

\[
X_n\Rightarrow X:=\sum_p(\log p)U_p,
\]

where the infinite sum converges in `L^2`. The characteristic function is

\[
\phi_X(t)=\prod_p
\frac{\sin\left(t\log p/[2(p-1)]\right)}{t\log p/[2(p-1)]}.
\]

The limit is not Gaussian.

### Proof

For each fixed finite prime set, `b_p/n->1/(p-1)` and the centered discrete uniform variable `(A_p-b_p/2)/n` converges to `U_p`. Independence gives joint convergence of every finite truncation.

The limiting variance series

\[
\sum_p\frac{(\log p)^2}{12(p-1)^2}
\]

converges. Uniformly in `n`, the variance contributed by primes above a fixed cutoff is bounded by a constant multiple of the tail of this convergent series plus a term tending to zero. Finite-truncation convergence and the converging-together theorem yield the asserted weak limit and `L^2` construction.

The product formula follows from independence. Its convergence on compact `t`-sets follows from `1-sinc(x)=O(x^2)` and the variance-series convergence.

At

\[
t=\frac{2\pi}{\log2},
\]

the factor belonging to `p=2` is zero. A nondegenerate Gaussian characteristic function is never zero. Hence the limit is not Gaussian.

### Consequence

Any full-model Gaussian local-limit theorem centered at `0.5 log(n!)` is false, even before asking for shrinking-window uniformity.

## N3-ANA-007, global minor-arc decay is impossible

- Result class: `disproved estimate`
- Repository status: `DISPROVED`
- Disproved claim: for fixed `n`, there exist `T<infinity` and `rho<1` such that the uniform-divisor characteristic function satisfies `|phi_n(t)|<=rho` for every `|t|>=T`.
- Parameter range: every fixed `n>=3`.

### Statement

For the centered characteristic function

\[
\phi_n(t)=\mathbb E\exp\left(it\left(S_n-\frac12\log(n!)\right)\right),
\]

we have

\[
\limsup_{|t|\to\infty}|\phi_n(t)|=1.
\]

### Proof

The exact coordinate factor is

\[
\phi_{p,n}(t)=
\frac{\sin((b_p+1)t\log p/2)}{(b_p+1)\sin(t\log p/2)}
\]

up to a unit complex phase removed by centering. The finite vector of frequencies `log p/(2pi)` admits simultaneous returns arbitrarily close to the origin modulo `1` by Dirichlet simultaneous approximation. These return times are unbounded because an exact common period would give a nontrivial integer relation among prime logarithms, contradicting unique factorization.

Choose a return so accurate that every `t log p` is within `o(1/(b_p+1))` of a multiple of `2pi`. Every normalized Dirichlet-kernel factor then has modulus `1-o(1)`. Their finite product has modulus `1-o(1)`, proving the limsup statement.

### Legal substitute

A usable minor-arc theorem must specify a bounded frequency range, smoothing, frequency averaging, or a growing prime subfamily with quantitative Diophantine separation. An unbounded pointwise minor arc is unavailable.

## N3-ANA-008, high-prime tail central limit theorem

- Result class: `proved theorem`
- Repository status: `PROVED`
- Hypotheses: `y=y(n)->infinity` and `2y<=sqrt(n)`.
- External dependency: the prime number theorem in the weak form `pi(2y)-pi(y) >> y/log y`.
- Constants: absolute but not optimized.

### Statement

Let

\[
T_{n,y}=\sum_{y<p\le n}\left(A_p-\frac{b_p}{2}\right)\log p,
\qquad B_{n,y}^2=\operatorname{Var}(T_{n,y}).
\]

Then

\[
\frac{T_{n,y}}{B_{n,y}}\Rightarrow N(0,1).
\]

Furthermore,

\[
B_{n,y}^2\gg n^2\frac{\log y}{y},
\]

and, with

\[
M_{n,y}=\max_{p>y}\frac{b_p\log p}{2},
\]

\[
M_{n,y}\ll n\frac{\log y}{y},
\qquad
\frac{M_{n,y}}{B_{n,y}}\ll\sqrt{\frac{\log y}{y}}.
\]

### Proof

For `y<p<=2y`, the hypothesis `2y<=sqrt(n)` gives `floor(n/p)>=n/(2p)` for all sufficiently large `n`. Therefore each such prime contributes at least a constant multiple of

\[
\frac{n^2(\log y)^2}{y^2}
\]

to the variance. The prime number theorem supplies `>>y/log y` primes in the band, proving the lower bound for `B_{n,y}^2`.

For `p>y`,

\[
b_p\le\frac{n}{p-1},
\]

and `log p/(p-1)` is decreasing for large `p`, proving the bound for `M_{n,y}`. Thus `M_{n,y}/B_{n,y}->0`.

Every centered summand is bounded in modulus by `M_{n,y}`. For each fixed `epsilon>0`, eventually `M_{n,y}<epsilon B_{n,y}`, so the Lindeberg sum is zero. The Lindeberg-Feller theorem gives the conclusion.

## N3-ANA-009, coarse central-window lower bound for the high-prime tail

- Result class: `conditional theorem`
- Repository status: `CONDITIONAL`
- External dependency: a Berry-Esseen inequality for independent, non-identically distributed centered variables with universal constant `C_BE`.
- Hypotheses: those of N3-ANA-008; `0<Delta<=B_{n,y}`; `|x|<=B_{n,y}`.

### Statement

There is an absolute constant `K` such that, whenever

\[
\Delta\ge K M_{n,y},
\]

we have

\[
\mathbb P\{T_{n,y}\in[x,x+\Delta]\}
\gg \frac{\Delta}{B_{n,y}}
\]

uniformly for `|x|<=B_{n,y}`.

### Proof

For a centered summand `Y_p`,

\[
\mathbb E|Y_p|^3\le M_{n,y}\mathbb E Y_p^2.
\]

Hence Berry-Esseen gives Kolmogorov distance at most

\[
C_{BE}\frac{M_{n,y}}{B_{n,y}}.
\]

On standardized intervals with left endpoint in `[-1,1]` and length at most `1`, the standard normal density is bounded below by an absolute positive constant. Therefore the normal interval mass is `>>Delta/B_{n,y}`. Subtracting the two endpoint errors proves the claim once `Delta` exceeds a sufficiently large constant multiple of `M_{n,y}`.

### Limitation

This theorem does not reach windows below the largest coordinate span. It is a rigorous substitute for a local limit theorem only at coarse logarithmic resolution.
