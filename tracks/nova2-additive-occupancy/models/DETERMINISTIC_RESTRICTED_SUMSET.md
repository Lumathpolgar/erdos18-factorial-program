# Model D: Deterministic Restricted-Sumset Growth

## Status

**Result label: conditional theorem.**

## Frozen object

For labeled finite sets `A_1,...,A_k subseteq D(n!)`, define

\[
\Sigma^{\!*}(A_1,\ldots,A_k)
=
\left\{
\sum_{i=1}^k a_i:
 a_i\in A_i\cup\{0\},
 a_i=a_j\ne0\Rightarrow i=j
\right\}.
\]

The theorem concerns only this final support. No interval property is imposed on partial sumsets.

## Required conclusion

For a correction radius `R` and `X=floor(sqrt(n!))`, prove

\[
\Sigma^{\!*}(A_1,\ldots,A_k)\cap[x-R,x]\ne\varnothing
\]

for every integer `R<=x<=X`.

## Structural assumptions that must be explicit

1. Exact formulas proving every element of every `A_i` divides `n!`.
2. Pairwise numerical disjointness, or a collision-deletion argument.
3. `k<=K(log n)^2`.
4. `sum_i max A_i>=X-R`.
5. Additive span one, or a complete residue correction theorem.
6. Any additive-energy, small-doubling, progression, or entropy hypothesis used by the proof.

## Permitted proof mechanisms

- direct restricted-sumset expansion;
- entropy inequalities with an injective or bounded-multiplicity decoding theorem;
- inverse theorems after verifying their ambient-group and density hypotheses;
- additive-energy bounds that produce interval or window inclusion;
- deterministic covering lemmas for labeled families.

## Forbidden transfers

- Cauchy-Davenport in a prime cyclic group without a valid reduction from the integer problem;
- unlabeled subset-sum theorems without preserving one choice per label;
- interval inclusion in an unrestricted sumset without checking numerical collisions;
- raw cardinality growth without a maximum-gap theorem;
- sequential coverage invariants that re-enter the Phase 12P architecture.

## Exact falsification checklist

- proper common divisor;
- concentration in a short arithmetic progression;
- large additive energy producing little growth;
- repeated numerical values across labels;
- support gaps wider than `R`;
- a proposed inverse theorem whose conclusion is only structural, not covering;
- an argument proving almost-all rather than every-target coverage.

## Inputs

### Nova 1

Explicit labels, correction palette, additive structure, and any progression or energy bounds available from factorial valuations.

### Nova 3

Counts in the exact scales, entropy estimates, and exclusion of concentration on a proper progression.

### Nova 4

Exact restricted-sumset enumeration, maximum-gap measurements, and smallest counterexamples to proposed growth inequalities.

## Route decision

This is the principal deterministic fallback. It ranks second because a successful theorem would be exceptionally robust, but no currently frozen factorial input verifies the hypotheses of a strong enough restricted-sumset covering theorem.
