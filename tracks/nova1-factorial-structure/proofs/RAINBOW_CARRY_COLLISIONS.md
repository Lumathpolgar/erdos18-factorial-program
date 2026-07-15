# Rainbow Carry Collisions

## Result ID

`N1-COL-001`

## Result label

**proved theorem**

## Purpose

The marker-three quotient construction has enormous formal profile capacity. Formal profiles are not automatically distinct numerical sums.

This file proves an explicit family of exact carry collisions inside the frozen quotient layers. The result does not disprove occupancy, but it permanently rules out any claim that the profile map is injective.

## Frozen quotient layers

For

\[
Y_n=\left\lfloor\frac{\lfloor\sqrt{n!}\rfloor}{3}\right\rfloor,
\]

let

\[
U_t(n)=
\{u\ge1:u\text{ odd},\ 3u\mid n!,\ 2^{t-1}u\le Y_n\},
\]

\[
B_t(n)=\{2^{t-1}u:u\in U_t(n)\}.
\]

A quotient profile chooses zero or one term from each layer.

## Local carry identity

For every integer `e>=0`,

\[
3\cdot2^e
=
1\cdot2^e+1\cdot2^{e+1}.
\]

When the cores `1` and `3` occur in the required layers, this identity gives two different legal local profiles with the same numerical sum:

1. choose core `3` in layer `e+1` and choose zero in layer `e+2`;
2. choose core `1` in both layers `e+1` and `e+2`.

The first profile uses one term. The second profile uses two distinct terms with different exact 2-adic valuations.

## N1-COL-001: exponential collision multiplicity

### Statement

Let `L` be a positive integer satisfying

\[
2L\le M_n
\]

and

\[
3\cdot2^{2L-2}\le Y_n.
\]

Then there exist at least

\[
2^L
\]

distinct legal quotient profiles with the same numerical sum

\[
S_L=4^L-1.
\]

For every integer `n>=120368`, the conditions hold with

\[
L=\left\lfloor\frac{M_n}{2}\right\rfloor.
\]

Consequently the maximum collision multiplicity of the frozen profile-to-sum map is at least

\[
2^{\lfloor M_n/2\rfloor}
=
\exp(\Omega((\log n)^2)).
\]

### Proof

Partition the first `2L` layers into disjoint pairs

\[
(1,2),(3,4),\ldots,(2L-1,2L).
\]

For pair `j`, put

\[
e_j=2j-2.
\]

The cutoff hypothesis guarantees that core `3` is available in the lower layer of every pair. Core `1` is then also available in both layers.

For each pair choose independently one of the following two local profiles:

\[
\mathcal P_j^{(0)}:
\quad
3\cdot2^{e_j},\ 0,
\]

or

\[
\mathcal P_j^{(1)}:
\quad
1\cdot2^{e_j},\ 1\cdot2^{e_j+1}.
\]

Both local profiles sum to

\[
3\cdot2^{e_j}.
\]

There are `2^L` independent choices across the disjoint layer pairs. Different bit strings give different layer-core assignments, so the profiles are distinct. Every profile respects the one-choice-per-layer rule.

All profiles have the same total

\[
\sum_{j=1}^L3\cdot2^{2j-2}
=3\sum_{j=0}^{L-1}4^j
=4^L-1.
\]

This proves the finite statement.

For `n>=120368`,

\[
M_n\le16(\log n)^2+1
\]

while

\[
\log Y_n\ge\frac{9n}{40}\log n-\log4.
\]

The right side dominates `M_n log2+log3` throughout this range. Hence

\[
3\cdot2^{M_n-1}\le Y_n,
\]

so the cutoff condition holds for `L=floor(M_n/2)`. `QED`

## Numerical distinctness inside each profile

The collision is between profiles, not within a single representation.

Within every profile:

- at most one term is chosen per layer;
- chosen terms in different layers have different exact 2-adic valuations;
- therefore all selected numerical quotient terms are distinct;
- multiplying by the fixed marker `3` preserves distinctness for the corresponding main divisors.

Thus the collision is valid under the frozen distinct-divisor rules.

## Capacity interpretation

The theorem proves that raw profile count overstates numerical sum count by at least

\[
\exp(\Omega((\log n)^2))
\]

at some fibers.

This loss is much smaller than the available formal entropy lower bound of factorial scale, so it does not by itself violate the necessary capacity inequality.

However, it establishes three permanent restrictions.

1. Profile injectivity is false.
2. A counting proof must include an upper bound on collision multiplicity or additive energy.
3. A Fourier or probabilistic proof must analyze the numerical sum law rather than the abstract profile space.

## What is not claimed

This theorem does not prove that typical fibers have exponential multiplicity. It gives an explicit lower bound for the maximum fiber.

It does not prove an upper bound on the number of distinct sums.

It does not disprove quotient-window occupancy or the marker-three construction.

## Next collision target

The next useful theorem is an upper bound for target-local collision energy in windows of width `W_n`, or a counterexample showing that a positive proportion of profiles concentrate on too few numerical sums.