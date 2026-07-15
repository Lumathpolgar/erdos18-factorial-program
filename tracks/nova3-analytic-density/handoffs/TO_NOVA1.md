# Handoff to Nova 1

Handoff ID: `N3-HO-N1-001`

Sending track: Nova 3, Analytic Divisor Density

Receiving track: Nova 1, Factorial Structure and Reduction

Date: 2026-07-15

Result status: `PROVED` statements plus one `CONDITIONAL` coarse-window theorem

Theorem or object IDs: `N3-ANA-004`, `N3-ANA-005`, `N3-ANA-006`, `N3-ANA-008`, `N3-ANA-009`, `N3-ROUTE-001`

## Exact claims

### Exact divisor-vector and tilt model

Every divisor of `n!` is uniquely

\[
d=\prod_{p\le n}p^{a_p},\qquad 0\le a_p\le v_p(n!).
\]

The exact tilted product measure and moment formulas are frozen in `proofs/PRODUCT_MODEL_THEOREMS.md`.

### Uniform local-count ceiling

For every prime `q<=n`, every real `u`, and every `Delta>=0`,

\[
\#\{d\mid n!:u\le\log d\le u+\Delta\}
\le
\tau(n!)\frac{\lfloor\Delta/\log q\rfloor+1}{v_q(n!)+1}.
\]

For fixed `Delta`, choosing `q=2` gives a uniform ceiling of order `tau(n!)/n`.

### Endpoint obstruction

For `0<=Delta<log2`,

\[
\#\{d\mid n!:0\le\log d\le\Delta\}=1.
\]

No growing fixed-width lower bound can include the lower endpoint.

### Corrected Gaussian reservoir

Let `y->infinity` and `2y<=sqrt n`. The centered logarithmic contribution of primes `p>y`, under the uniform exponent measure, satisfies a central limit theorem. If

\[
B_{n,y}^2=\operatorname{Var}\sum_{p>y}(A_p-v_p(n!)/2)\log p
\]

and

\[
M_{n,y}=\max_{p>y}v_p(n!)\log p,
\]

then

\[
B_{n,y}^2\gg n^2\frac{\log y}{y},
\qquad
M_{n,y}\ll n\frac{\log y}{y}.
\]

Conditional on Berry-Esseen, every central window of width

\[
\Delta\ge K M_{n,y}
\]

has probability `gg Delta/B_{n,y}`.

## Exact hypotheses

- Exact factorial exponent caps only.
- The coarse window is central relative to the high-prime tail mean.
- The low-prime exponents must be fixed, enumerated, or handled by a separate structural argument.
- `K` is absolute but not optimized.
- No additive representation claim is included.

## Dependencies

- Proof file: `tracks/nova3-analytic-density/proofs/PRODUCT_MODEL_THEOREMS.md`
- Scale map: `tracks/nova3-analytic-density/FACTORIAL_DIVISOR_SCALE_MAP.md`
- Source ledger: `tracks/nova3-analytic-density/SOURCE_LEDGER.md`

## Verification command

```text
python3 tracks/nova3-analytic-density/proofs/scale_sanity.py
```

## Known failure modes

- Full-vector Gaussian modeling is false.
- Fixed-width endpoint density is false.
- Layer cardinality does not imply additive usefulness or distinct sums.
- A high-prime log-size theorem does not prove additive coverage by numerical divisor values.

## What is not claimed

- No proof of the factorial half-range theorem.
- No maximum-gap bound.
- No polylogarithmic-width local lower bound.
- No transfer from smooth-number lower bounds.

## Requested next action

Freeze a proposed structural split by supplying:

1. the exact cutoff `y(n)`;
2. the permitted low-prime exponent set;
3. the exact logarithmic target range `u`;
4. the required window width `Delta`;
5. the minimum count needed per window;
6. the theorem node that this count closes.

Nova 3 will then determine whether `N3-ANA-009` already suffices or whether a finer tilted local theorem is required.
