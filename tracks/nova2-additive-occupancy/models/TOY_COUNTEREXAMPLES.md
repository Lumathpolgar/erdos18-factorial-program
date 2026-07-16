# Toy Counterexamples and Obstructions

All statements in this file are independent of factorial-specific inputs.

## N2-ADD-101: Profile count does not imply interval coverage

**Result label: proved theorem.**

### Statement

For every integer `k>=2`, there exist pairwise disjoint singleton labels `A_1,...,A_k subseteq Z_{>0}` such that the number of legal rainbow profiles is larger than the number of targets in an initial interval, but that interval is not covered.

### Construction

Let

\[
A_i=\{2^i\},\qquad 1\le i\le k.
\]

The labels are pairwise disjoint. There are exactly `2^k` zero-or-one profiles. Every attainable sum is even. Consider

\[
I_k=\{0,1,\ldots,2^k-2\}.
\]

This interval contains `2^k-1` targets, so the profile count is strictly larger than the interval size. Nevertheless, every odd target in `I_k` is absent.

### Conclusion

Raw profile capacity, even with injective profiles and pairwise disjoint labels, does not imply interval coverage.

## N2-ADD-102: Lattice obstruction

**Result label: proved theorem.**

### Statement

Let `A_1,...,A_k` be finite subsets of `Z_{>0}` and define

\[
g=\gcd\bigcup_{i=1}^k A_i.
\]

Every rainbow sum from `A_i union {0}` is divisible by `g`. If `g>1`, no interval containing representatives of all residue classes modulo `g` can be covered.

### Proof

Every selected nonzero term is divisible by `g`, hence so is their sum. Therefore the final sumset is contained in `gZ`. Any integer not divisible by `g` is inaccessible. `square`

### Correction warning

A correction palette repairs this obstruction only if its own attainable residues, added to the main residues, cover every residue class needed by the target interval.

## N2-ADD-103: Ordinary convolution can certify an illegal repeated divisor

**Result label: proved theorem.**

### Statement

Positive mass in an ordinary labeled convolution does not imply a valid distinct-divisor representation when numerical supports overlap.

### Example

Take

\[
A_1=A_2=\{1\}
\]

and let each label choose `0` or `1` with positive probability. Then

\[
\mathbb P(Y_1+Y_2=2)>0.
\]

The only contributing tuple is `(1,1)`, which repeats the same numerical divisor. Thus `2` has positive ordinary convolution mass but no legal representation using these labels.

### Conclusion

Pairwise label names are not a distinctness proof. Either the nonzero supports must be pairwise disjoint or the probability law must delete collision tuples.

## N2-ADD-104: A local approximation is powerless when its error reaches the main atom

**Result label: proved theorem.**

### Statement

Let `q` be any probability mass function on `Z`, and let `m_0,m_1` be distinct integers with `q(m_0)>0`. Define `p` by

\[
p(m_0)=0,
\qquad
p(m_1)=q(m_1)+q(m_0),
\]

and `p(m)=q(m)` otherwise. Then

\[
\sup_m|p(m)-q(m)|=q(m_0),
\]

but `p(m_0)=0`.

### Proof

The only changed atoms are `m_0` and `m_1`; both change by exactly `q(m_0)`. `square`

### Consequence for local limits

A bound

\[
\sup_m|\mathbb P(S=m)-q(m)|\le\varepsilon
\]

cannot imply positivity at `m_0` unless

\[
\varepsilon<q(m_0).
\]

In Gaussian tails the reference atom can be exponentially smaller than a central local-limit error. Therefore a visually Gaussian distribution or an absolute `o(1/sigma)` estimate does not imply positivity in every target window.

## N2-ADD-105: Window approximation threshold

**Result label: proved theorem.**

### Statement

Let `Q` be a reference probability distribution, let `I` be a finite integer window with `Q(I)>0`, and let `epsilon>=Q(I)`. There exists a probability distribution `P` with

\[
|P(I)-Q(I)|\le\epsilon
\]

and `P(I)=0`.

### Proof

Move all mass `Q(I)` from `I` to one point outside `I`. The window error is exactly `Q(I)`. `square`

### Conclusion

A windowed local limit theorem implies occupancy only when its absolute error is strictly smaller than the reference window mass.

## N2-ADD-106: Endpoint variance collapse under Bernoulli tilting

**Result label: proved theorem.**

### Statement

Let independent variables `Y_i` take values in `{0,a_i}` with `a_i>0`, under any exponential tilt. Let

\[
S=\sum_iY_i,
\quad
m=\mathbb ES,
\quad
A=\sum_i a_i,
\quad
a_{\max}=\max_i a_i.
\]

Then

\[
\operatorname{Var}(S)
\le a_{\max}m
\]

and

\[
\operatorname{Var}(S)
\le a_{\max}(A-m).
\]

### Proof

Write `p_i=P(Y_i=a_i)`. Then

\[
\operatorname{Var}(S)=\sum_i a_i^2p_i(1-p_i)
\le a_{\max}\sum_i a_ip_i
=a_{\max}m.
\]

Also apply the same argument to the deficit variables `a_i-Y_i`, whose sum has mean `A-m` and the same variance. `square`

### Consequence

If a target-dependent tilt drives `m` to `0` or `A`, the variance tends to zero unless `a_max` diverges in a compensating way. A bulk local central limit theorem cannot be claimed uniformly to either endpoint without a separate argument.

## N2-ADD-107: Targetwise probability is not one random universal object

**Result label: disproved model.**

### Statement

Suppose that for each target `x` one constructs a different probability space and proves that some representation of `x` has positive probability. This proves a deterministic representation for each fixed `x`, but it does not prove that one random draw, one random family, or one shared certificate covers all targets simultaneously.

### Reason

The events live on different probability spaces unless an explicit coupling is supplied. A union bound is meaningful only after all target failure events are defined on one common random object.

## Summary of mandatory safeguards

Any surviving model must separately verify:

- support reach;
- lattice span;
- numerical distinctness;
- quantitative local error below main mass;
- endpoint variance;
- whether the randomness concerns selections from fixed labels or the random construction of the labels themselves.
