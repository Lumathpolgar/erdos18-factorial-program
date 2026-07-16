# Handoff to Nova 4

Handoff ID: `N3-HO-N4-002`

Supersedes: `N3-HO-N4-001`

Sending track: Nova 3, Analytic Divisor Density

Receiving track: Nova 4, Computation, Falsification, and Verification

Date: 2026-07-15

Result status: proved theorem audit with requested finite certificates and computational evidence checks

Theorem or object IDs: `N3-ANA-004` through `N3-ANA-011`, `N3-FIN-001`, `N3-FIN-002`

## Exact Nova 1 dependency imported by Nova 3

- branch: `nova/factorial-structure`
- commit: `fa11f4b2cb86a2dd791df189ada12757be791804`
- imported theorem: `N1-STR-009`
- source file: `tracks/nova1-factorial-structure/proofs/HIGH_PRIME_MENU_CAPACITY.md`

Nova 4 must independently verify that this exact theorem version matches the hypotheses used in N3-ANA-011.

## Exact claims to reconstruct

### Product and local-density claims

1. Exact product model and moment formulas:
   \[
   \mathbb E S_n=\tfrac12\log(n!),
   \qquad
   \operatorname{Var}(S_n)=\frac1{12}\sum_{p\le n}b_p(b_p+2)(\log p)^2.
   \]
2. Local-count ceiling:
   \[
   L_n(u,\Delta)
   \le
   \tau(n!)\frac{\lfloor\Delta/\log q\rfloor+1}{b_q+1}.
   \]
3. Variance asymptotic:
   \[
   \operatorname{Var}(S_n)/n^2
   \to
   \frac1{12}\sum_p\frac{(\log p)^2}{(p-1)^2}.
   \]
4. Full-model non-Gaussian limit and characteristic-function zero at
   \[
   t=2\pi/\log2.
   \]
5. High-prime tail scale:
   \[
   B_{n,y}^2\gg n^2\log y/y,
   \qquad
   M_{n,y}/B_{n,y}\to0.
   \]
6. Unbounded pointwise minor-arc decay is false.

### Explicit prime and capacity claims

7. For every integer `n>=120368`,
   \[
   \pi(n)-\pi(n/2)\ge\frac{n}{3\log n}.
   \]
8. For Nova 1's exact definitions,
   \[
   e_{M_n}\le\lfloor v_2(n!)/2\rfloor-1
   \]
   for every `n>=120368`.
9. For every `1<=t<=M_n`,
   \[
   |U_t(n)|
   \ge
   2^{\pi(n)-\pi(n/2)-1}-1
   \ge
   2^{n/(3\log n)-1}-1.
   \]
10. Formal profile capacity satisfies
    \[
    \prod_{t=1}^{M_n}(|U_t(n)|+1)2^{r_n}\ge X_n+1.
    \]
11. The explicit thresholds may all be taken as
    \[
    n_3=n_4=n_5=120368.
    \]

## Files

- `tracks/nova3-analytic-density/proofs/PRODUCT_MODEL_THEOREMS.md`
- `tracks/nova3-analytic-density/proofs/scale_sanity.py`
- `tracks/nova3-analytic-density/proofs/EXPLICIT_PRIME_INTERVAL_AND_CAPACITY.md`
- `tracks/nova3-analytic-density/proofs/prime_interval_capacity_sanity.py`
- `tracks/nova3-analytic-density/FACTORIAL_DIVISOR_SCALE_MAP.md`
- `tracks/nova3-analytic-density/SOURCE_LEDGER.md`
- `tracks/nova3-analytic-density/handoffs/RESPONSE_TO_NOVA1.md`

## Verification commands

```text
python3 tracks/nova3-analytic-density/proofs/scale_sanity.py
python3 tracks/nova3-analytic-density/proofs/prime_interval_capacity_sanity.py
```

Both scripts use only the Python standard library and fail closed on assertion failures.

## Requested exact tests

### N4 request A: exhaustive moment audit

For every `2<=n<=12`, enumerate all divisors of `n!` and verify:

- divisor uniqueness;
- exact divisor count `tau(n!)`;
- complement symmetry;
- empirical mean equals `0.5 log(n!)` to floating tolerance `1e-12`;
- empirical variance equals the exact coordinate formula to relative tolerance `1e-12`.

Label the result `FINITE_CERTIFICATE` only for the enumerated range.

### N4 request B: local ceiling audit

For every `2<=n<=12`, every prime `q<=n`, the frozen width grid, and every divisor-log endpoint, verify N3-ANA-005. Deliberately lower the right side for selected tight cases and confirm rejection.

### N4 request C: scale convergence table

Reproduce the frozen table for selected `n<=10000`, including variance ratios, low-prime shares, effective dimension, and high-prime maximal-span ratios. Label it `COMPUTATIONAL_EVIDENCE`.

### N4 request D: characteristic-function falsification

For small `n`, search for recurrence frequencies with `|phi_n(t)|` near one. Record search range and precision. Treat this as evidence only.

### N4 request E: source reconstruction for restricted sources

Independently verify that:

- Ford's `H(x,y,z)` counts integers with a divisor in an interval rather than divisors of `n!`;
- Drappeau-Tenenbaum excludes an exceptional friable subset;
- the ultrafriable common exponent cap differs from `v_p(n!)`.

### N4 request F: Dusart source reconstruction

Independently inspect Pierre Dusart, *Estimates of Some Functions Over Primes without R.H.*, arXiv:1002.0442v1, Theorem 6.9, and verify the exact thresholds:

\[
\pi(x)\ge\frac{x}{\log x-1}\quad(x\ge5393),
\]

\[
\pi(x)\le\frac{x}{\log x-1.1}\quad(x\ge60184).
\]

Then reconstruct the algebra proving N3-ANA-010 without reading Nova 3's intermediate algebra first.

### N4 request G: exact threshold sweep

Run `prime_interval_capacity_sanity.py` for every integer

\[
120368\le n\le1000000.
\]

Verify independently:

- exact `pi(n)-pi(floor(n/2))`;
- exact Legendre value `v_2(n!)`;
- exact ceilings in `r_n` and `M_n`;
- address legality;
- conservative capacity exponent.

Record the minimum margin and its exact `n` for each check.

### N4 request H: adversarial threshold tests

The verifier must reject at least the following corruptions:

1. replace `120368` by a value below the source upper-bound threshold without finite supplementation;
2. replace `floor(v_2(n!)/2)-1` by a larger legal range without proof;
3. remove the `-1` from the menu-unit exclusion while retaining the same set definition;
4. treat formal profiles as distinct numerical sums;
5. replace `pi(n/2)` by `pi(ceil(n/2))` without endpoint analysis;
6. report the finite sweep as an asymptotic proof.

## Known failure modes

- Floating logs can merge close values, so divisor uniqueness must be checked in exact integers first.
- The prime-count theorem uses `pi(x)` at a real endpoint; for integer `n`, `pi(n/2)=pi(floor(n/2))`.
- A histogram agreement is not asymptotic proof.
- Profile capacity is not sumset occupancy.
- The first Nova 1 occupancy architecture remains disproved by Nova 2's lattice obstruction.
- Logarithmic characteristic functions do not control numerical additive sums.
- No finite test proves uniformity beyond its exact range.

## What is not claimed

- The factorial half-range theorem is not proved.
- The main Erdős problem is not solved.
- N3-ANA-011 does not prove distinct profile sums.
- N3-ANA-011 does not repair the rejected power-of-two layer lattice.
- No additive Fourier theorem is active until revised labels pass Nova 2's structural gate.

## Requested next action

Run both supplied scripts, reconstruct N3-ANA-004 through N3-ANA-011 independently, add the adversarial tests above, and return `ACCEPTED`, `NEEDS_REPAIR`, or `REJECTED` for each theorem ID separately.