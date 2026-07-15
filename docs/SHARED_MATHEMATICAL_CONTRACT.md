# Shared Mathematical Contract

## Primary theorem contract

The repository's primary objective is to prove that there exist absolute constants `C,K>0` and `n_0` such that

\[
h(n!)\le K(\log n)^C
\]

for every integer `n>=n_0`.

A track may prove a different theorem only if it provides a complete, audited implication to this objective.

## Current sufficient local contract

The current conditional endgame accepts the following input:

> There exist absolute constants `K_0,n_0` such that for every `n>=n_0`, every integer
> \[
> 0\le x\le\lfloor\sqrt{n!}\rfloor
> \]
> is a sum of at most `K_0(\log n)^2` distinct divisors of `n!`.

In repository notation this is

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)=O((\log n)^2).
\]

The archived Track B claims that this implies

\[
h(n!)=O((\log n)^3).
\]

Before final acceptance, the implication must be reconstructed from the archived source package and checked against the exact `H_N` convention in `COMMON_NOTATION.md`.

## Mandatory theorem fields

Every theorem artifact must state:

1. theorem ID;
2. status label;
3. exact hypotheses;
4. exact conclusion;
5. ranges of all variables;
6. dependencies by theorem ID;
7. whether constants are effective;
8. distinctness mechanism;
9. boundary and finite-exception treatment;
10. proof or verifier location.

## Prohibited assumption transfers

The following transfers are invalid unless separately proved:

- Many divisors imply additive interval coverage.
- Raw profile count implies distinct sums.
- Average spacing implies maximum-gap control.
- Finite success implies asymptotic success.
- A divisor of `L_m` construction transfers unchanged to `n!`, or conversely.
- Pairwise disjoint labels imply numerically distinct selected divisors.
- A probabilistic existence statement supplies a deterministic representation for every target without a uniform argument.
- A theorem for almost all targets implies a theorem for every target.

## Correction contract

Any proof that covers targets up to a residual error `R(n)` must provide a correction family satisfying all of the following:

- every correction term divides `n!`;
- the correction terms are distinct;
- correction terms do not collide with main terms;
- every residual in the claimed interval is representable;
- the number of correction terms is included in the final bound.

## Handoff acceptance

A result is eligible for cross-track use only after:

- the theorem statement is frozen;
- all dependencies exist in the theorem registry;
- a proof artifact is committed;
- a second track or Nova 4 has attempted independent reconstruction;
- any failed reconstruction is resolved in writing.

## Final-solution gate

No branch, pull request, README, or report may state that Erdős Problem 18 is solved until the full proof chain passes every gate in `docs/INTEGRATION_GATES.md`.
