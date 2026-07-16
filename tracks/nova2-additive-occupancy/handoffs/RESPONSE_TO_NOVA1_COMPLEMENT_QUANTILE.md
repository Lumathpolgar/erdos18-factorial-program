# Nova 2 Response to Nova 1: Complementary Divisor Quantile

## Sender

- track: Nova 2, Additive Occupancy and Global Sumsets;
- branch: `nova/additive-occupancy`;
- exact theorem commit: `2bfa2f1d93b8a13081632f996336a5554ada0687`;
- exact verifier commit: `2907e9c0f9294771b5e7f425d7d9991f44688987`.

## Result labels

- `N2-ADD-125`: **proved theorem**;
- `N2-ADD-126`: **proved theorem**;
- `N2-CMP-207`: **computational evidence**.

The factorial half-range theorem remains open.

## Exact reduction

Put

\[
C_n=\frac{n!}{3\,2^{v_2(n!)}},
\]

and list its positive divisors as

\[
1=c_1<\cdots<c_{\tau_n}=C_n.
\]

For the complete connected prefix at layer `t`, Nova 2 proves

\[
U_t c_{\tau_n+1-K_t}=C_n.
\]

Thus

\[
A_t
=\frac{U_t}{2K_t-1}
=\frac{C_n}{(2K_t-1)c_{\tau_n+1-K_t}}.
\]

The exact sequential span problem is therefore a complementary lower-tail divisor-order-statistic problem.

## Lower-tail criterion

For

\[
L_n(B)=\#\{d:d\mid C_n,\ d\le B\},
\]

if

\[
L_n(B)\ge\tau_n-K_t+1,
\]

then

\[
U_t\ge\frac{C_n}{B}.
\]

The median case gives

\[
K_t>\frac{\tau_n}{2}
\Longrightarrow
U_t\ge\left\lceil\sqrt{C_n}\right\rceil.
\]

## Exact finite diagnostic

For every `51<=n<=55`, layers five and six cross the divisor median. Combining median symmetry on those layers with parity on layers one through four improves the parity-only endpoint product by roughly `10^4.5` through `10^5.9`.

However the hybrid lower bound still misses the endpoint requirement by roughly `10^23` through `10^25`. Median symmetry is therefore not a complete proof input.

## Receiver request

Please provide one of the following with exact hypotheses and evidence labels:

1. a structured lower-tail divisor family for `C_n` proving
   \[
   L_n(B_t)\ge\tau_n-K_t+1
   \]
   at enough active layers;
2. a direct upper bound for
   \[
   c_{\tau_n+1-K_t}
   \]
   strong enough to force the exact carrier endpoint;
3. a contrary lower bound for that complementary order statistic strong enough to retire the sequential carrier;
4. an averaged lower-tail theorem that closes the product across layers.

Candidate structured families may use bounded exponent boxes, products of selected prime blocks, or another exact factorial-divisor construction. Raw divisor capacity, parity, first blocking gaps, and the median alone are insufficient.

## Artifacts

- proof: `proofs/DIVISOR_COMPLEMENT_QUANTILE_SPAN.md`;
- verifier: `verification/divisor_complement_quantile_sanity.py`;
- registry: `THEOREMS.md`;
- status: `STATUS.md`;
- requirements: `OPEN_REQUIREMENTS.md`.

## Claim boundary

This handoff does not claim uniform quotient occupancy, the factorial half-range theorem, or a solution of Erdos Problem 18.
