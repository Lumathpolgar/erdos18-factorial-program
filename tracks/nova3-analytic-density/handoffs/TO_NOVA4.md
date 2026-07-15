# Handoff to Nova 4

Handoff ID: `N3-HO-N4-001`

Sending track: Nova 3, Analytic Divisor Density

Receiving track: Nova 4, Computation, Falsification, and Verification

Date: 2026-07-15

Result status: `PROVED` theorem audit with requested `FINITE_CERTIFICATE` and `COMPUTATIONAL_EVIDENCE` checks

Theorem or object IDs: `N3-ANA-004` through `N3-ANA-009`

## Exact claims to reconstruct

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

## Files

- `tracks/nova3-analytic-density/proofs/PRODUCT_MODEL_THEOREMS.md`
- `tracks/nova3-analytic-density/proofs/scale_sanity.py`
- `tracks/nova3-analytic-density/FACTORIAL_DIVISOR_SCALE_MAP.md`
- `tracks/nova3-analytic-density/SOURCE_LEDGER.md`

## Verification command

```text
python3 tracks/nova3-analytic-density/proofs/scale_sanity.py
```

The script uses only the Python standard library and fails closed on assertion failures.

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

For every `2<=n<=12`, every prime `q<=n`, window widths

\[
\Delta\in\{0,0.25,0.5,1,2\},
\]

and every window endpoint induced by a divisor logarithm, verify

\[
L_n(u,\Delta)
\le
\tau(n!)\frac{\lfloor\Delta/\log q\rfloor+1}{b_q+1}.
\]

Deliberately perturb the right side downward by one for selected tight cases and verify the checker rejects the corrupted claim.

### N4 request C: scale convergence table

For

\[
n\in\{50,100,200,500,1000,2000,5000,10000\},
\]

compute:

- `log tau(n!)/(n/log n)`;
- `Var(S_n)/n^2`;
- variance shares of primes `2`, `3`, `5`, and `7`;
- participation-ratio effective dimension;
- for cutoffs `y` in a stated feasible grid, `M_{n,y}/B_{n,y}`.

Label this `COMPUTATIONAL_EVIDENCE`, not proof.

### N4 request D: characteristic-function falsification

For small `n`, search for simultaneous recurrence frequencies with `|phi_n(t)|` near one. Record the search range and numerical precision. This illustrates `N3-ANA-007` but does not prove it.

### N4 request E: source reconstruction

Independently verify that:

- Ford's `H(x,y,z)` counts integers with a divisor in an interval rather than divisors of `n!`;
- Drappeau-Tenenbaum's theorem excludes an exceptional friable subset and therefore does not select the factorial sequence;
- the ultrafriable exponent cap differs from `v_p(n!)`.

## Known failure modes

- Floating logs can merge very close values; divisor uniqueness must be checked in exact integers before taking logs.
- A histogram agreement is not an asymptotic proof.
- A found recurrence frequency is evidence only; the theorem uses simultaneous approximation.
- Do not infer additive divisor-sum coverage from logarithmic histograms.
- Do not describe any finite test as proving the open target.

## What is not claimed

- The factorial half-range theorem is not proved.
- The numerical limiting constants are not used as exact symbolic constants.
- No finite experiment verifies uniformity in all `u` or all `n`.

## Requested next action

Run the supplied script, reproduce its outputs independently, add adversarial tests, and return `ACCEPTED`, `NEEDS_REPAIR`, or `REJECTED` for each theorem ID separately.
