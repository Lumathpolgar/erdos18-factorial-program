# Quotient Endpoint Support Checkpoint

## Research status

The factorial half-range theorem remains open.

This checkpoint closes total endpoint support for the preferred marker-three quotient construction. It does not close downward endpoint-window occupancy.

## New theorem nodes

### N1-STR-019: multiplicative 3-density

For every integer `n>=6`,

\[
D_n=\frac{n!}{3\cdot2^{v_2(n!)}}
\]

is multiplicatively `3`-dense. Every real `1<=z<=D_n` has a divisor `d|D_n` satisfying

\[
z/3<d\le z.
\]

### N1-STR-020: endpoint support

For every integer `n>=12`, the first three quotient layers contain distinct legal terms

\[
b_t\in B_t(n),
\qquad t=1,2,3,
\]

with

\[
X_n/9<b_t\le X_n/3.
\]

Therefore

\[
b_1+b_2+b_3>X_n/3
\]

and

\[
\max\Sigma_{\rm rb}(B_1(n),\ldots,B_{M_n}(n))
\ge
\left\lfloor X_n/3\right\rfloor+1.
\]

The frozen quotient target range is not beyond the total support.

### N1-RED-006: coarse deterministic contraction

For every `n>=12`, every integer `0<=q<=floor(X_n/3)`, and every layer count `L`, a deterministic increasing-layer selection leaves residual

\[
\rho_L<\max\{(2/3)^Lq,2^L\}.
\]

This bound is too weak to reach the polynomial correction radius `W_n` and is not a proof of occupancy.

## Proof mechanism

1. Powers of `3` are multiplicatively 3-dense.
2. If `D` is 3-dense and `p<=3D`, then adjoining any power `p^a` preserves 3-density.
3. The factorial valuation of `3` is large enough that every later odd prime `p<=n` satisfies the extension condition.
4. The reserved odd core `D_n` is therefore 3-dense.
5. Applying density at cutoffs `X_n/(3*2^(t-1))` for `t=1,2,3` produces three quotient terms above `X_n/9`.

## Exact finite verification

Run:

```text
python tracks/nova1-factorial-structure/verification/endpoint_support_sanity.py
```

Recorded result:

```text
PASS test_three_density
PASS test_endpoint_support
PASS test_coarse_contraction
PASS all 3 endpoint-support checks
```

Exact finite ranges:

- 3-density: `6<=n<=20`;
- endpoint crossing: `12<=n<=20`;
- exhaustive coarse contraction: every quotient target for `12<=n<=14` and `1<=L<=6`.

Evidence label: **finite certificate**.

## Closed gates

For `N1-CON-003`, the following are now closed:

- divisor legality;
- numerical distinctness;
- palette disjointness;
- exact main lattice;
- attained residue classes;
- first-target coverage;
- selected-term cost;
- formal profile capacity from `n>=120368`;
- total endpoint reach.

## Open theorem node

The central open statement remains

\[
[q-W_n,q]
\cap
\Sigma_{\rm rb}(B_1(n),\ldots,B_{M_n}(n))
\ne\varnothing
\]

for every

\[
W_n+1\le q\le\left\lfloor X_n/3\right\rfloor.
\]

In particular, the final downward endpoint window

\[
[\lfloor X_n/3\rfloor-W_n,\lfloor X_n/3\rfloor]
\]

remains open.

## Exact limitation

A maximum attainable sum above the endpoint does not imply that an attainable sum lies immediately below the endpoint. This checkpoint closes support reach only.

## Files

- `proofs/QUOTIENT_ENDPOINT_SUPPORT.md`
- `verification/endpoint_support_sanity.py`
- `verification/ENDPOINT_SUPPORT_FINITE_REPORT.md`
- `PREFERRED_ROUTE.md`
- `STATUS.md`
- `THEOREMS.md`
- `CONSTRUCTIONS.md`
- `OPEN_REQUIREMENTS.md`
- `handoffs/TO_NOVA2.md`
- `handoffs/TO_NOVA4.md`
