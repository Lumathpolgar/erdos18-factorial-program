# Candidate 2: Tilted Local-Limit Theorem

## Theorem contract

- Candidate ID: `N3-CAND-LLT-001`
- Result class: `conditional theorem`
- Current status: `OPEN` in the desired fine-window form
- Proved substitute: `N3-ANA-009`
- Intended consumers: Nova 1 and Nova 2

Fix a cutoff `y=y(n)` and a low-prime exponent vector

\[
\alpha=(a_p)_{p\le y},\qquad 0\le a_p\le v_p(n!).
\]

For `p>y`, let the independent tilted exponent variables satisfy

\[
\mathbb P_\theta(A_p=j)=
\frac{p^{\theta j}}{1+p^\theta+\cdots+p^{\theta v_p(n!)}},
\qquad 0\le j\le v_p(n!).
\]

Define

\[
T_{n,y,\theta}=\sum_{y<p\le n}
\bigl(A_p-\mathbb E_\theta A_p\bigr)\log p,
\]

\[
B_{n,y}(\theta)^2=\operatorname{Var}_\theta(T_{n,y,\theta}),
\]

and

\[
M_{n,y}=\max_{p>y}v_p(n!)\log p.
\]

## Desired conclusion

For a frozen compact tilt range `|theta|<=theta_0`, a cutoff satisfying

\[
y\to\infty,\qquad 2y\le\sqrt n,
\]

and windows satisfying

\[
\Delta_{\min}(n,y,\theta)\le\Delta=o(B_{n,y}(\theta)),
\]

prove uniformly for `|x|<=A B_{n,y}(theta)` that

\[
\mathbb P_\theta\{T_{n,y,\theta}\in[x,x+\Delta]\}
=
\frac{\Delta}{\sqrt{2\pi}B_{n,y}(\theta)}
\exp\left(-\frac{x^2}{2B_{n,y}(\theta)^2}\right)
+o\left(\frac{\Delta}{B_{n,y}(\theta)}\right).
\]

The constants and error term must be uniform in the displayed ranges. The low-prime vector `alpha` affects only the deterministic shift and must not enter hidden constants.

## Known status

### At zero tilt

`N3-ANA-008` proves

\[
\frac{T_{n,y,0}}{B_{n,y}(0)}\Rightarrow N(0,1)
\]

when `y->infinity` and `2y<=sqrt n`.

### Coarse-window lower bound

`N3-ANA-009`, conditional on the standard Berry-Esseen inequality, proves uniformly for `|x|<=B_{n,y}(0)` that

\[
\mathbb P\{T_{n,y,0}\in[x,x+\Delta]\}
\gg\frac{\Delta}{B_{n,y}(0)}
\]

provided

\[
\Delta\ge K M_{n,y}.
\]

This is a genuine windowed positivity result, but it is not a fine local limit.

## Why the full unconditioned theorem is false

The full uniform-divisor model retains a fixed proportion of variance in the exponents of `2`, `3`, and other small primes. By `N3-ANA-006`, normalization by `n` converges to a non-Gaussian infinite convolution. Consequently a Gaussian tilted local limit cannot be asserted for all prime coordinates without conditioning or an exact low-prime convolution.

## Exact missing step

The remaining task is to control the Fourier inversion integral on frequencies where Berry-Esseen gives no positivity. Let

\[
\phi_{n,y,\theta}(t)=
\mathbb E_\theta e^{itT_{n,y,\theta}}.
\]

The proof needs an integrable bound over a bounded frequency interval whose upper endpoint grows at least like `1/Delta`. Rational independence alone gives no rate. The required estimate must exploit many high-prime coordinates and survive the bounded but nonidentical exponent caps.

## Strongest primary source that partially applies

Giuliano and Weber develop local-limit methods for weighted sums of independent Bernoulli variables using characteristic functions. Their variables and hypotheses do not match the bounded uniform or tilted exponent variables here without a new decomposition and a proof of every weight condition. The source is methodologically relevant but is not imported as a theorem.

Drappeau and Tenenbaum prove Gaussian divisor laws for almost all friable integers, not for the deterministic factorial sequence. Their saddle-point decomposition motivates the tilt but does not supply the local theorem.

See `SOURCE_LEDGER.md`, entries `N3-SRC-005` and `N3-SRC-007`.

## Constants and dependencies

A valid theorem must state:

- the compact tilt range;
- the cutoff range for `y`;
- lower and upper bounds for `B_{n,y}(theta)`;
- the exact minimum window width;
- the central displacement range in `x`;
- all dependence on fixed constants `A` and `theta_0`;
- whether the error is effective.

## Falsification duties

1. Verify `B_{n,y}(theta)` does not collapse at the edge of the tilt range.
2. Verify the largest coordinate span is `o(B)`.
3. Verify a local theorem, not only weak convergence.
4. Check that smoothing is removed with a quantitatively controlled error.
5. Check all endpoint conventions in converting log windows to divisor counts.
6. Do not infer positivity when the main term is smaller than the Fourier error.
7. Confirm the permitted window widths overlap the additive model's needs.

## Feed to Nova 1

After fixing low-prime exponents, the theorem would provide quantitative counts in translated high-prime log windows. Nova 1 could combine exact low-prime structure with a diffuse high-prime reservoir.

## Feed to Nova 2

The theorem supplies pointwise or windowed atom control for a convolution factor. It is the most direct analytic input for a rainbow convolution argument, provided Nova 2 freezes the required `Delta`, frequency cutoff, and number of independent layers.
