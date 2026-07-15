# Proofs: Marker Distinctness and Binary Correction

## N1-STR-006: Marker-signature lemma

Result label: **proved theorem**.

### Statement

Let `M` be a finite set of marker primes. For each label `t`, let

\[
\sigma_t=(e_{q,t})_{q\in M}
\]

be a nonnegative integer signature, let `u_t` be coprime to every prime in `M`, and define

\[
d_t=u_t\prod_{q\in M}q^{e_{q,t}}.
\]

If the signatures are pairwise distinct, then the integers `d_t` are pairwise distinct.

### Proof

Suppose `d_s=d_t`. Unique factorization gives

\[
v_q(d_s)=v_q(d_t)
\]

for every prime `q in M`. Since both cores are coprime to every marker prime,

\[
v_q(d_s)=e_{q,s},\qquad v_q(d_t)=e_{q,t}.
\]

Therefore `sigma_s=sigma_t`. Pairwise distinct signatures force `s=t`.

## Cross-packet version

Result label: **proved theorem**.

Suppose packet `j` uses signatures only from a region `Sigma_j`, and the regions are pairwise disjoint. Then no divisor from packet `j` equals a divisor from packet `k` for `j != k`. This follows because equality would force equal signatures, contradicting disjointness of the regions.

## N1-COR-001: Binary correction palette

Result label: **proved theorem**.

### Statement

Let `r>=1` and assume `r-1<=v_2(n!)`. Define

\[
\mathcal C_r=\{2^0,2^1,\ldots,2^{r-1}\}.
\]

Then:

1. every member of `C_r` is a positive divisor of `n!`;
2. every integer `t` with `0<=t<2^r` is a sum of a unique subset of `C_r`;
3. every such representation uses at most `r` terms;
4. any main divisor with odd part greater than one is numerically disjoint from `C_r`.

### Proof

The valuation hypothesis gives `2^j|n!` for every `0<=j<r`. Every integer `t` in the stated range has a unique binary expansion

\[
t=\sum_{j=0}^{r-1}\varepsilon_j2^j,
\qquad \varepsilon_j\in\{0,1\}.
\]

The selected powers are distinct, and their number is at most `r`. Every member of `C_r` has odd part equal to one, so a divisor with odd part greater than one cannot equal a palette term.

## N1-RED-002: Downward-window correction reduction

Result label: **proved theorem**.

### Statement

Let `A_n` be a family of pairwise distinct positive divisors of `n!`, disjoint from `C_r`. Suppose that every integer `x` with

\[
2^r\le x\le X_n
\]

has a representation

\[
y=\sum_{d\in S_x}d,
\qquad S_x\subseteq A_n,
\qquad |S_x|\le K(n),
\]

with

\[
x-(2^r-1)\le y\le x.
\]

Then

\[
H_{n!}(X_n+1)\le K(n)+r.
\]

### Proof

For `0<=x<2^r`, use the binary representation of `x` from `C_r`.

For `2^r<=x<=X_n`, choose `y` as in the hypothesis. The residual

\[
t=x-y
\]

satisfies `0<=t<2^r`, so write it as a subset sum of `C_r`. The main and correction families are disjoint, every selected divisor is legal, and every selected divisor is numerically distinct. The total number of terms is at most `K(n)+r`.

The interval endpoint is `X_n+1` because the frozen definition of `H_N(X)` maximizes over integers `x<X`.

## Failure audit

Result label: **disproved route** for any argument omitting one of the following checks.

The reduction is invalid if:

- the main sum can exceed `x`;
- the residual can equal or exceed `2^r`;
- a main term is a pure power of two used by the palette;
- the main family itself contains repeated numerical divisors;
- the correction term count is omitted from the final bound.