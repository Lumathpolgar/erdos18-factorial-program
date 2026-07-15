# Candidate 1: Local Logarithmic Divisor Count Theorem

## Theorem contract

- Candidate ID: `N3-CAND-LDC-001`
- Result class: `open`
- Current status: `OPEN`
- Owner: Nova 3
- Intended consumers: Nova 1 and Nova 2
- Exact set counted: divisors of `n!`, not all `n`-smooth, friable, or ultrafriable integers

For real `u` and `Delta>=0`, write

\[
L_n(u,\Delta)=\#\{d\mid n!:u\le\log d\le u+\Delta\}.
\]

Let

\[
K_n(\theta)=\sum_{p\le n}\log\sum_{j=0}^{v_p(n!)}e^{\theta j\log p},
\]

and let `theta_n(u)` be the unique solution of `K_n'(theta)=u` for `0<u<log(n!)`.

## Proposed conclusion

Fix constants `0<eta<1/2` and `A>=1`. There should exist constants

\[
c=c(\eta,A)>0,\qquad C=C(\eta,A)>0,
\]

and an explicit window threshold `Delta_min(n,u)` such that for every sufficiently large `n`, every

\[
\eta\log(n!)\le u\le(1-\eta)\log(n!),
\]

and every

\[
\Delta_{\min}(n,u)\le\Delta\le A B_n(\theta_n(u)),
\]

one has

\[
L_n(u,\Delta)
\ge
c\,e^{K_n(\theta_n(u))-\theta_n(u)u}
\min\left(1,\frac{\Delta}{B_n(\theta_n(u))}\right),
\]

where

\[
B_n(\theta)^2=K_n''(\theta).
\]

The desired strongest form would have `Delta_min` polylogarithmic in `n`. No such form is currently proved.

## Exact hypotheses that cannot be omitted

1. The target must remain away from `0` and `log(n!)`. For `0<=Delta<log 2`,
   \[
   L_n(0,\Delta)=1.
   \]
2. The theorem counts exact exponent vectors satisfying
   \[
   0\le a_p\le v_p(n!).
   \]
3. Uniformity constants may depend only on the displayed fixed bulk and window parameters.
4. A lower bound must come from the exact tilted measure, not from a smooth-number superset.
5. The chosen window convention must remain closed at both ends, or any endpoint conversion must be proved.

## Exact change-of-measure reduction

For every real `theta`,

\[
L_n(u,\Delta)=e^{K_n(\theta)}
\mathbb E_\theta\left[e^{-\theta S_n}
\mathbf1_{[u,u+\Delta]}(S_n)\right].
\]

If `theta>=0`, then

\[
L_n(u,\Delta)
\ge e^{K_n(\theta)-\theta(u+\Delta)}
\mathbb P_\theta\{u\le S_n\le u+\Delta\}.
\]

If `theta<=0`, then

\[
L_n(u,\Delta)
\ge e^{K_n(\theta)-\theta u}
\mathbb P_\theta\{u\le S_n\le u+\Delta\}.
\]

Thus the candidate reduces to a uniform tilted-window lower bound with the correct sign-dependent exponential factor.

## What is proved now

### Exact upper ceiling

By `N3-ANA-005`, for every prime `q<=n`,

\[
L_n(u,\Delta)
\le
\tau(n!)\frac{\lfloor\Delta/\log q\rfloor+1}{v_q(n!)+1}.
\]

For fixed `Delta`, this is `O_Delta(tau(n!)/n)` uniformly in `u`.

### Symmetry

The complement map `d -> n!/d` gives

\[
L_n(u,\Delta)=L_n(\log(n!)-u-\Delta,\Delta).
\]

### Coarse conditional substitute

After fixing low-prime exponents and retaining only a high-prime tail, `N3-ANA-009` gives a central-window probability lower bound when the window width is at least a sufficiently large constant multiple of the largest remaining coordinate span.

## Strongest primary source compatibility

The closest source is Drappeau and Tenenbaum's Gaussian law for divisors of almost all friable integers. It does not select the deterministic factorial sequence, and therefore cannot prove this candidate. Ford's theorem counts integers possessing a divisor in an interval, not divisors of the fixed integer `n!`, and is legally irrelevant to the desired lower bound.

See `SOURCE_LEDGER.md`, entries `N3-SRC-004` and `N3-SRC-005`.

## Exact missing step

Prove a uniform lower bound for

\[
\mathbb P_{\theta_n(u)}\{u\le S_n\le u+\Delta\}
\]

throughout a bulk range, after resolving the following obstruction:

- the full product model has bounded effective dimension;
- its central normalized law is not Gaussian;
- low-prime coordinates have spans comparable with the full standard deviation;
- unrestricted characteristic-function minor arcs recur arbitrarily close to one.

The viable formulation must condition on low-prime coordinates or convolve them exactly with a high-prime local theorem.

## Falsification tests

- Hidden constants: reject any proof whose lower-bound constant depends on `u`, `n`, or an unfrozen cutoff.
- Smooth superset misuse: reject lower bounds imported from friable or ultrafriable supersets.
- Endpoint failure: verify explicitly that the stated bulk range excludes the one-divisor endpoint windows.
- Lattice analysis: rational independence of prime logarithms is insufficient without quantitative Fourier control.
- Local uniformity: a central limit theorem for cumulative distribution functions is insufficient for positivity in every requested window.
- Target overlap: verify that the resulting `u` range actually includes the structural layers requested by Nova 1 or Nova 2.

## Feed to Nova 1

If proved for a frozen window width and target band, this theorem gives a deterministic lower bound on the number of legal exact factorial divisors available in each structural logarithmic layer. Nova 1 must still establish numerical distinctness and additive usefulness.

## Feed to Nova 2

If proved, the theorem supplies minimum layer cardinalities and tilted masses for a convolution or rainbow occupancy model. It does not by itself imply additive interval coverage.
