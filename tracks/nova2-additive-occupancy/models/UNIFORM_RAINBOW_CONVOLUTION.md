# Model U: Uniform Rainbow Convolution

## Status

**Result label: heuristic.**

## Frozen model

For fixed `n`, let `A_1,...,A_k subseteq D(n!)` be finite and pairwise numerically disjoint. Let `Y_i` be independent and uniform on `A_i union {0}`. Define

\[
S=\sum_{i=1}^kY_i,
\qquad
\phi(t)=\prod_{i=1}^k\frac{1+\sum_{a\in A_i}e^{ita}}{|A_i|+1}.
\]

Because the nonzero supports are pairwise disjoint, every atom of `S` is a legal distinct-divisor rainbow sum.

## Required theorem

For a correction radius `R` and target endpoint `X=floor(sqrt(n!))`, prove

\[
\mathbb P(S\in[x-R,x])>0
\]

for every integer `R<=x<=X`, with

\[
k+\ell_C\le K(\log n)^2,
\]

where `ell_C` is the correction-palette term bound.

## Necessary conditions

1. `sum_i max A_i >= X-R`.
2. `gcd(union_i A_i)=1`, unless the correction palette proves complete residue repair.
3. No numerical value occurs in two labels.
4. No final support gap in `[0,X]` exceeds `R+1`.
5. The smallest target-window mass, not the central mass, must be positive.

## Pointwise versus windowed target

The model seeks an all-target window theorem. A central limit theorem, an average statement, or positive mass for almost all windows does not suffice.

## Endpoint audit

A fixed uniform law has one mean. Unless the support has special structure, windows near `0` and near `X` lie in large-deviation tails. Any proof must quantify these tails or split off deterministic endpoint regimes.

## Exact failure tests

- gcd greater than one;
- empty residue classes;
- a repeated numerical divisor across labels;
- a single label carrying a macroscopic fraction of the variance;
- a support gap wider than the correction radius;
- a Gaussian approximation whose error exceeds the target-window main term.

## Input contracts

### Nova 1

Provide fixed pairwise disjoint labels, exact support bounds, `k`, and a disjoint correction palette.

### Nova 3

Provide a uniform lower bound for the minimum window mass, including tails and endpoints.

### Nova 4

Compute exact window minima and return the smallest empty window or collision witness.

## Route decision

This model remains a useful benchmark, but it is not preferred because one fixed law does not naturally provide uniform probability across the full half-range.
