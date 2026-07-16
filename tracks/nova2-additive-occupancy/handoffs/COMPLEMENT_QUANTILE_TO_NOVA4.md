# Complement Quantile Reconstruction for Nova 4

## Frozen source

- branch: `nova/additive-occupancy`;
- theorem commit: `2bfa2f1d93b8a13081632f996336a5554ada0687`;
- verifier commit: `2907e9c0f9294771b5e7f425d7d9991f44688987`;
- proof: `proofs/DIVISOR_COMPLEMENT_QUANTILE_SPAN.md`;
- verifier: `verification/divisor_complement_quantile_sanity.py`.

## Required reconstruction

Let

\[
C_n=\frac{n!}{3\,2^{v_2(n!)}},
\]

with positive divisors

\[
1=c_1<\cdots<c_{\tau_n}=C_n.
\]

Independently prove:

\[
U_t c_{\tau_n+1-K_t}=C_n.
\]

For

\[
L_n(B)=\#\{d:d\mid C_n,\ d\le B\},
\]

also prove

\[
L_n(B)\ge\tau_n-K_t+1
\Longrightarrow
U_t\ge\frac{C_n}{B}.
\]

Reconstruct the median consequence

\[
K_t>\frac{\tau_n}{2}
\Longrightarrow
U_t\ge\left\lceil\sqrt{C_n}\right\rceil.
\]

## Exact finite replay

For each `51<=n<=55`, confirm that only layers five and six cross the divisor median. Confirm the median-hybrid sixth-root endpoint ratios:

- `n=51`: `0.000145487587879522`;
- `n=52`: `0.000123906257046752`;
- `n=53`: `0.0000907853071519960`;
- `n=54`: `0.0000892960011035230`;
- `n=55`: `0.0000740382055592177`.

## Fail-closed checks

Reject any replay that changes the complementary index, counts zero as a divisor, applies the median bound below the median, or promotes finite evidence to an asymptotic theorem.

Continue exact finite certification from `n=56`. Resource exhaustion is not a counterexample.

The quotient-window theorem, factorial half-range theorem, and Erdos Problem 18 remain open.
