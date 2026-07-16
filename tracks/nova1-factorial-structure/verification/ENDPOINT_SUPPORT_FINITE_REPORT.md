# Endpoint Support Finite Report

## Evidence label

**finite certificate** for the exact ranges below.

This report is not an asymptotic proof. The symbolic proofs are in `proofs/QUOTIENT_ENDPOINT_SUPPORT.md`.

## Command

```text
python tracks/nova1-factorial-structure/verification/endpoint_support_sanity.py
```

## Environment

- Python 3
- standard library only
- deterministic
- exact integer arithmetic
- no random seed

## Checks

### 1. Multiplicative 3-density

For every integer

\[
6\le n\le20,
\]

the verifier constructs every divisor of

\[
D_n=\frac{n!}{3\cdot2^{v_2(n!)}}
\]

and verifies that consecutive divisors satisfy

\[
d_{i+1}\le3d_i.
\]

### 2. Three-layer endpoint support

For every integer

\[
12\le n\le20,
\]

the verifier finds terms

\[
b_t\in B_t(n),
\qquad t=1,2,3,
\]

satisfying

\[
X_n/9<b_t\le X_n/3,
\]

checks exact divisor legality and 2-adic distinctness, and verifies

\[
b_1+b_2+b_3>\lfloor X_n/3\rfloor.
\]

Recorded witnesses:

| `n` | `floor(X_n/3)` | `b_1` | `b_2` | `b_3` |
|---:|---:|---:|---:|---:|
| 12 | 7,295 | 6,237 | 6,930 | 6,300 |
| 13 | 26,303 | 25,025 | 24,570 | 25,740 |
| 14 | 98,419 | 96,525 | 95,550 | 97,020 |
| 15 | 381,178 | 375,375 | 378,378 | 374,220 |
| 16 | 1,524,714 | 1,488,375 | 1,433,250 | 1,501,500 |
| 17 | 6,286,559 | 6,185,025 | 6,265,350 | 5,953,500 |
| 18 | 26,671,611 | 26,582,985 | 26,507,250 | 26,025,300 |
| 19 | 116,258,858 | 115,540,425 | 116,093,250 | 115,783,668 |
| 20 | 519,925,422 | 518,450,625 | 519,626,250 | 514,377,500 |

Each individual witness term is at most the endpoint. Their three-term sum crosses the endpoint.

### 3. Coarse deterministic contraction

For every integer

\[
12\le n\le14,
\]

every quotient target

\[
0\le q\le\lfloor X_n/3\rfloor,
\]

and every layer count

\[
1\le L\le6,
\]

the verifier checks the exact integer form of

\[
\rho_L
<
\max\left\{
(2/3)^Lq,
2^L
\right\}.
\]

## Recorded output

```text
PASS test_three_density
PASS test_endpoint_support
PASS test_coarse_contraction
PASS all 3 endpoint-support checks
```

## Claim boundary

The endpoint maximum exceeds the final quotient target. This proves the target range is not outside the total support.

It does not prove that a sum lies in

\[
[\lfloor X_n/3\rfloor-W_n,\lfloor X_n/3\rfloor].
\]

That downward endpoint-window statement remains part of the open global quotient occupancy theorem.
