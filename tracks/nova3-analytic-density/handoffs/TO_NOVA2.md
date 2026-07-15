# Handoff to Nova 2

Handoff ID: `N3-HO-N2-001`

Sending track: Nova 3, Analytic Divisor Density

Receiving track: Nova 2, Additive Occupancy and Global Sumsets

Date: 2026-07-15

Result status: `PROVED`, `CONDITIONAL`, and `DISPROVED` statements

Theorem or object IDs: `N3-ANA-005`, `N3-ANA-006`, `N3-ANA-007`, `N3-ANA-008`, `N3-ANA-009`, `N3-CAND-CF-001`

## Exact claims

### Full-model Gaussian input is unavailable

For a uniformly selected divisor `d` of `n!`,

\[
\frac{\log d-\frac12\log(n!)}n
\]

converges to a non-Gaussian infinite convolution. The prime `2` coordinate alone contributes a fixed positive share of variance. Do not use a full-model Gaussian local limit as a convolution input.

### Unbounded minor-arc decay is false

For every fixed `n>=3`, the characteristic function of the centered logarithmic divisor size satisfies

\[
\limsup_{|t|\to\infty}|\phi_n(t)|=1.
\]

Therefore Nova 2 must freeze a bounded inversion range, a smoothing kernel, or a frequency-average requirement. A claim of uniform pointwise decay for all sufficiently large frequencies is invalid.

### Viable high-prime factor

For `y->infinity` and `2y<=sqrt n`, the centered contribution from primes above `y` satisfies a central limit theorem. With

\[
B_{n,y}^2=\operatorname{Var}(T_{n,y}),
\qquad
M_{n,y}=\max_{p>y}v_p(n!)\log p,
\]

we have

\[
B_{n,y}^2\gg n^2\frac{\log y}{y},
\qquad
M_{n,y}\ll n\frac{\log y}{y},
\qquad
\frac{M_{n,y}}{B_{n,y}}\to0.
\]

Conditional on Berry-Esseen, central windows of width `Delta>=K M_{n,y}` have probability `gg Delta/B_{n,y}`.

### Exact local atom ceiling

For every prime `q<=n`,

\[
L_n(u,\Delta)
\le
\tau(n!)\frac{\lfloor\Delta/\log q\rfloor+1}{v_q(n!)+1}.
\]

This gives a necessary ceiling on any requested lower bound.

## Exact hypotheses

- These Fourier statements concern `log d`, not the additive numerical values `d`.
- No automatic transfer exists from logarithmic-size characteristic functions to additive sumset characteristic functions.
- The high-prime CLT uses the exact uniform exponent model. A different layer measure requires a new moment and Fourier audit.
- The coarse lower bound is central and has width at least a constant multiple of the largest coordinate span.

## Dependencies

- `proofs/PRODUCT_MODEL_THEOREMS.md`
- `candidates/TILTED_LOCAL_LIMIT.md`
- `candidates/CHARACTERISTIC_FUNCTION_MINOR_ARC.md`
- `PREFERRED_ROUTE.md`

## Verification command

```text
python3 tracks/nova3-analytic-density/proofs/scale_sanity.py
```

## Known failure modes

1. Confusing Fourier variables for `log d` and for additive divisor values.
2. Requesting an unbounded minor arc.
3. Using weak convergence to claim every short window is occupied.
4. Ignoring low-prime atoms that dominate variance.
5. Asking for a lower bound exceeding `N3-ANA-005`.
6. Treating layer size as rainbow sumset coverage.

## What is not claimed

- No additive occupancy theorem.
- No maximum-gap theorem.
- No pointwise local limit below `M_{n,y}`.
- No theorem for an unspecified rainbow layer measure.

## Requested next action

Freeze one analytic request with all of the following:

1. Is the Fourier variable applied to `log d` or to numerical divisor values?
2. Exact layer distribution and independence structure.
3. Exact prime and exponent restrictions.
4. Number of convolution factors.
5. Exact target window and main-term size.
6. Maximum inversion frequency `R_n`.
7. Required norm: pointwise, `L^1`, `L^2`, or averaged decay.
8. Exact occupancy theorem node supported.

Nova 3 will then prove the weakest adequate bounded-frequency estimate or return a resonance obstruction.
