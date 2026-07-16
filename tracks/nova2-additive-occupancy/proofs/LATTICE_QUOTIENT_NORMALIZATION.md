# Lattice Quotient Normalization and Minimal Binary Repair

## Result IDs

- `N2-ADD-116`: proved theorem
- `N2-ADD-117`: conditional theorem
- `N2-OBS-108`: disproved model

## Imported construction baseline

This analysis concerns the valuation-tagged construction retained on:

- repository: `Lumathpolgar/erdos18-factorial-program`
- branch: `nova/factorial-structure`
- current inspected head: `fa11f4b2cb86a2dd791df189ada12757be791804`
- original frozen handoff commit: `b939574eb88a08bb03abda5bbe6ff2ca97444e08`

The underlying main layers are unchanged from the rejected handoff. No uncommitted or later Nova 1 repair is assumed.

## N2-ADD-116: exact lattice quotient window equivalence

### Statement

Let `g,L` be positive integers. Let

\[
S\subseteq g\mathbb Z_{\ge0}
\]

and define the quotient support

\[
Q=\{s/g:s\in S\}\subseteq\mathbb Z_{\ge0}.
\]

Assume a correction family can represent every integer residual

\[
0\le c\le Lg-1.
\]

Fix an integer endpoint `X>=0`. Then the following are equivalent.

1. Every integer target `0<=x<=X` has a decomposition
   \[
   x=s+c,
   \qquad
   s\in S,
   \qquad
   0\le c\le Lg-1.
   \]
2. For every integer
   \[
   0\le m\le\lfloor X/g\rfloor,
   \]
   the quotient support satisfies
   \[
   Q\cap[\max(0,m-L+1),m]\ne\varnothing.
   \]

Equivalently, the downward gap from every quotient target `m` to the preceding point of `Q` is at most `L-1`.

### Proof

Write a target uniquely as

\[
x=gm+a,
\qquad
0\le a\le g-1.
\]

Suppose `s=gq` with `q in Q` and `0<=x-s<=Lg-1`. Then `q<=m`, and

\[
g(m-q)+a\le Lg-1.
\]

Since `m-q` is an integer and `a>=0`, this implies

\[
m-q\le L-1,
\]

so

\[
q\in[m-L+1,m].
\]

Because `q>=0`, condition 2 follows.

Conversely, suppose `q in Q` satisfies

\[
\max(0,m-L+1)\le q\le m.
\]

Set `s=gq`. Then

\[
0\le x-s=g(m-q)+a
\le g(L-1)+(g-1)
=Lg-1.
\]

The correction family represents this residual, proving condition 1. `QED`

## Term-count and distinctness clause

Assume every `s in S` is represented by at most `K` numerically distinct main terms, and every residual in `[0,Lg-1]` is represented by at most `J` numerically distinct correction terms. If the main and correction numerical supports are disjoint, then every target uses at most `K+J` numerically distinct terms.

This is immediate by concatenating the two representations.

## Application to valuation-tagged layers

Let

\[
r_n=\lceil4\log n\rceil,
\qquad
g_n=2^{r_n+1}.
\]

For the frozen layers,

\[
\mathcal A_t(n)
=
\{2^{r_n+t}u:
 u\mid n!,\ u>1,\ u\text{ odd},\ 2^{r_n+t}u\le X_n\}.
\]

Every main rainbow sum lies in `g_n Z`. Define the normalized quotient layers

\[
\mathcal B_t(n)
=
\{2^{t-1}u:
 u\mid n!,\ u>1,\ u\text{ odd},\ 2^{r_n+t}u\le X_n\},
\]

and their final rainbow sumset

\[
\mathcal Q_n
=
\left\{
\sum_{t=1}^{M_n}b_t:
 b_t\in\mathcal B_t(n)\cup\{0\}
\right\}.
\]

Then

\[
\mathcal R_n=g_n\mathcal Q_n.
\]

Every nonzero element of every quotient layer is at least `3`, because the odd core satisfies `u>1`. For all sufficiently large admissible `n`, the value `3` belongs to `B_1(n)`, so

\[
\min(\mathcal Q_n\setminus\{0\})=3.
\]

## Consecutive binary correction extensions

For an integer `k>=0`, let

\[
\mathcal C_k=\{2^0,2^1,\ldots,2^k\}.
\]

Its subset sums represent every integer in

\[
[0,2^{k+1}-1].
\]

Take `k=r_n+j`. Then

\[
2^{k+1}-1
=2^{r_n+j+1}-1
=2^j g_n-1.
\]

Thus N2-ADD-116 applies with

\[
L=2^j.
\]

### One added correction power fails

Extending the original palette only through `2^{r_n}` corresponds to `j=0` and `L=1`. Quotient coverage would require

\[
\mathcal Q_n\cap\{m\}\ne\varnothing
\]

for every quotient target `m`. At `m=1`, this fails because the quotient support contains `0` and has smallest positive point `3`.

Equivalently, the target `x=g_n` is not representable.

### Two added correction powers fail

Extending through `2^{r_n+1}=g_n` corresponds to `j=1` and `L=2`. Quotient coverage would require

\[
\mathcal Q_n\cap[m-1,m]\ne\varnothing
\]

for every `m`. At `m=2`, the interval `[1,2]` contains no point of `Q_n`.

Equivalently, the target `x=2g_n` is not representable.

These two failures are `N2-OBS-108`, a disproved-model result for the one-power and two-power consecutive binary repairs.

### Three added correction powers pass the initial support gate

Extending through `2^{r_n+2}=2g_n` corresponds to `j=2` and

\[
L=4.
\]

The exact remaining quotient condition is

\[
\mathcal Q_n\cap[\max(0,m-3),m]\ne\varnothing
\]

for every

\[
0\le m\le\lfloor X_n/g_n\rfloor.
\]

The initial targets `m=0,1,2` are covered by the quotient point `0`, and `m=3` is covered by the quotient point `3` for all sufficiently large admissible `n`. Thus this is the first consecutive binary extension not already disproved by the initial support gap.

It is not yet a proof of global occupancy.

## N2-ADD-117: repaired valuation-tagged reduction

### Statement

For sufficiently large admissible `n`, retain the frozen main layers `A_t(n)` and replace the original correction palette by

\[
\mathcal C_n^+
=
\{2^0,2^1,\ldots,2^{r_n+2}\}.
\]

Assume the normalized final rainbow sumset satisfies

\[
\mathcal Q_n\cap[\max(0,m-3),m]\ne\varnothing
\]

for every integer

\[
0\le m\le\lfloor X_n/g_n\rfloor.
\]

Then every integer target `0<=x<=X_n` is a sum of at most

\[
M_n+r_n+3
\]

numerically distinct divisors of `n!`. Consequently,

\[
H_{n!}(X_n+1)
\le
M_n+r_n+3
=O((\log n)^2).
\]

### Proof

The correction palette represents every residual in

\[
[0,2^{r_n+3}-1]=[0,4g_n-1].
\]

The quotient hypothesis and N2-ADD-116 give a main sum `s in R_n` whose residual from each target lies in this interval. The added correction terms are pure powers of two, while every nonzero main term has an odd factor greater than one, so main and correction supports are numerically disjoint. Distinct 2-adic addresses preserve distinctness among selected main terms. The main selection uses at most `M_n` terms and binary correction uses at most `r_n+3` terms. `QED`

## Exact new additive target

The repaired construction no longer asks Nova 2 to occupy windows on the original lattice blindly. Its exact unresolved theorem is:

> Prove that the normalized final rainbow sumset `Q_n` has maximum downward gap at most `3` throughout `[0,floor(X_n/g_n)]`.

This remains a final-only global statement. It imposes no interval-coverage requirement on intermediate partial sumsets and therefore does not become a Phase 12P sequential ladder merely by normalization.

## Analytic normalization

Any target-dependent convolution or Fourier law should now be defined on the quotient variables

\[
B_t(n)=A_t(n)/g_n,
\]

not on the original variables with a redundant common factor. The characteristic function is

\[
\Phi_{n,m}(\theta)
=
\mathbb E\exp(i\theta T_{n,m}),
\qquad
\theta\in[-\pi,\pi],
\]

where `T_{n,m}` is a target-dependent sum of quotient-layer choices. The target window is the fixed four-point set

\[
[\max(0,m-3),m]\cap\mathbb Z.
\]

All nonzero resonances of the quotient support must still be audited. Removing the common factor `g_n` does not prove span one.

## What is not claimed

This file does not prove the quotient maximum-gap theorem. It does not prove a local limit theorem, minor-arc estimate, or deterministic restricted-sumset theorem for `Q_n`. It proves the exact normalization, eliminates two inadequate repairs, and freezes the weakest consecutive-binary repair not already blocked by the initial lattice and minimum-support obstructions.
