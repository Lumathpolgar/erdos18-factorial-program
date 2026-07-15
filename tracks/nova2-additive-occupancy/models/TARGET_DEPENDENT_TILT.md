# Model T: Target-Dependent Exponential Tilt

## Status

**Result label: conditional theorem.**

## Frozen model

Let fixed, pairwise numerically disjoint labels `A_1,...,A_k subseteq D(n!)` and positive base weights `w_i(a)` be given. For `theta in R`, define

\[
\mu_{i,\theta}(a)=
\frac{w_i(a)e^{\theta a}}
{Z_i(\theta)},
\qquad
Z_i(\theta)=\sum_{b\in A_i\cup\{0\}}w_i(b)e^{\theta b}.
\]

Let independent `Y_{i,theta}` have these laws and put

\[
S_\theta=\sum_iY_{i,\theta},
\quad
m(\theta)=\mathbb E S_\theta,
\quad
v(\theta)=\operatorname{Var}(S_\theta).
\]

For target `x`, select `theta_x` so that `m(theta_x)` lies near the midpoint of `[x-R,x]`.

## Mean-map facts

The log-partition function

\[
F(\theta)=\sum_i\log Z_i(\theta)
\]

satisfies

\[
F'(\theta)=m(\theta),
\qquad
F''(\theta)=v(\theta)\ge0.
\]

Thus the mean map is nondecreasing and is strictly increasing wherever the variance is positive.

## Required theorem

For every integer target `R<=x<=X=floor(sqrt(n!))`, find `theta_x` such that

\[
\mathbb P_{\theta_x}(S_{\theta_x}\in[x-R,x])>0,
\]

uniformly in `x`, with `k` and correction cost totaling `O((log n)^2)`.

## Lattice and collision contract

- `gcd(union_i A_i)=1`, or a complete residue-repair theorem is supplied.
- The labels are pairwise disjoint numerically.
- If overlapping labels are unavoidable, the product tilt is invalid and must be replaced by a collision-free global Gibbs law.

## Endpoint theorem that must not be skipped

In the Bernoulli case `A_i={a_i}`, write

\[
p_i(\theta)=\frac{w_i(a_i)e^{\theta a_i}}
{w_i(0)+w_i(a_i)e^{\theta a_i}}.
\]

Then

\[
v(\theta)=\sum_i a_i^2p_i(1-p_i).
\]

If `a_max=max_i a_i` and `m=m(theta)`, then

\[
v(\theta)\le a_{\max}m.
\]

If `A=sum_i a_i`, then also

\[
v(\theta)\le a_{\max}(A-m).
\]

Therefore variance necessarily collapses as the target mean approaches either endpoint. A single bulk local limit theorem cannot remain uniform all the way to `0` and `A`.

## Required regime split

1. Lower endpoint handled by the correction palette.
2. Bulk handled by tilted Fourier or local-limit estimates with a variance lower bound.
3. Upper endpoint handled either by a complementary deterministic construction or by a separate deficit tilt with its own variance theorem.

## Exact analytic inequalities required

For the target window `I_x=[x-R,x] cap Z`, choose a lattice reference law `Q_x` with characteristic function `psi_x`. Prove

\[
\int_{-\pi}^{\pi}
|\phi_{\theta_x}(t)-\psi_x(t)|
|K_{I_x}(t)|\,dt
<2\pi Q_x(I_x),
\]

where

\[
K_{I_x}(t)=\sum_{m\in I_x}e^{-imt}.
\]

This strict inequality implies positive target-window mass.

## Input contracts

### Nova 1

Provide fixed pairwise disjoint supports, correction palette, support reach, and an endpoint architecture.

### Nova 3

Prove uniform tilt existence, bulk variance, major-arc approximation, minor-arc decay, and the weighted Fourier inequality.

### Nova 4

Certify the mean equation, variance, exact window occupancy, and the first endpoint where the proposed bulk constants fail.

## Route decision

This is the preferred model, used with a Fourier window criterion rather than an unsupported Gaussian approximation.
