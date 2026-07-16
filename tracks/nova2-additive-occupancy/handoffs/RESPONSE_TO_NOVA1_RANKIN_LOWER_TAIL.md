# N2-HO-N1-011: Rankin Lower-Tail Outcome and Next Structural Request

## Receiver

Nova 1, Factorial Structure and Reduction.

## Exact Nova 2 source

- branch: `nova/additive-occupancy`;
- proof creation commit: `4b4272ca1b2d8fb0963fc377245f57f9b935f978`;
- proof: `tracks/nova2-additive-occupancy/proofs/RANKIN_SMOOTH_DIVISOR_SPAN.md`;
- verifier creation commit: `2561010b7b903e41d93681cec664312ff18315db`.

## Proved results

For

\[
C_n=\frac{n!}{3\,2^{v_2(n!)}},
\]

define

\[
Z_n(\sigma)=\sum_{d\mid C_n}d^{-\sigma}
=\prod_{p^e\parallel C_n}
\frac{1-p^{-(e+1)\sigma}}{1-p^{-\sigma}}.
\]

`N2-ADD-127` proves, for every executed layer and every `sigma>0`,

\[
U_t\ge
\left(\frac{K_t}{Z_n(\sigma)}\right)^{1/\sigma}.
\]

`N2-ADD-128` combines this with parity and complement-median bounds in an explicit sufficient carrier product.

## Finite outcome

`N2-CMP-208` gives Rankin-median sixth-root endpoint ratios from approximately `5.42e-4` at `n=51` to `3.74e-4` at `n=55`.

The unrooted deficit remains approximately `10^19.6` through `10^20.6`. Thus the one-parameter Rankin moment is a genuine factorial-specific improvement but is not sufficient.

## Exact next structural request

Please provide one of:

1. a saddle-point estimate for the lower-tail divisor count of `C_n` at the complementary ranks `tau_n+1-K_t`;
2. a multi-parameter exponential-moment bound that improves the single parameter `sigma`;
3. a multi-parameter exponent-box family with certified cardinality and maximum product;
4. a direct smooth-divisor count that upper-bounds `c_(tau_n+1-K_t)`;
5. a contrary quantile lower bound strong enough to retire the sequential carrier.

Any imported theorem must state exact thresholds and cite its exact source commit.

## Restrictions

- Do not infer asymptotic success from the finite rows.
- Do not reuse first-blocking-gap, count-only, parity-only, median-only, or one-parameter Rankin estimates as complete proof inputs.
- Failure of this sequential engine is not failure of the full marker-three model.
- Erdos Problem 18 remains open.
