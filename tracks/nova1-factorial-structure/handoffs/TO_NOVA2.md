# Handoff to Nova 2

Handoff ID: `N1-HO-N2-001`

Sending track: Nova 1, Factorial Structure and Reduction

Receiving track: Nova 2, Additive Occupancy and Global Sumsets

Date: 2026-07-15

Result status: **conditional theorem** request

Theorem or object IDs: `N1-CON-001`, `N1-RED-003`, `N1-REQ-N2-001-A`

## Exact frozen objects

For every integer `n>=3`, define

\[
X_n=\lfloor\sqrt{n!}\rfloor,
\qquad
V_n=v_2(n!),
\]

\[
r_n=\lceil4\log n\rceil,
\qquad
M_n=\lceil16(\log n)^2\rceil,
\]

and, for `1<=t<=M_n`,

\[
e_t=r_n+t.
\]

The theorem request concerns all sufficiently large `n` satisfying

\[
e_{M_n}\le\lfloor V_n/2\rfloor-1.
\]

For each such `n` and `t`, define

\[
U_t(n)=
\left\{
 u\in\mathbb Z_{>0}:
 u\mid n!,\ u\text{ odd},\ u>1,\ 2^{e_t}u\le X_n
\right\},
\]

and

\[
\mathcal A_t(n)=\{2^{e_t}u:u\in U_t(n)\}.
\]

Define the rainbow sumset

\[
\mathcal R_n=
\left\{
\sum_{t=1}^{M_n}d_t:
 d_t\in\mathcal A_t(n)\cup\{0\}
\right\}.
\]

At most one nonzero term may be chosen from each layer.

## Exact theorem request

Prove that an absolute integer `n_0` exists such that, for every integer `n>=n_0` and every integer

\[
2^{r_n}\le x\le X_n,
\]

there is a sum `y in R_n` satisfying

\[
x-(2^{r_n}-1)\le y\le x.
\]

Equivalently,

\[
[x-(2^{r_n}-1),x]\cap\mathcal R_n\ne\varnothing
\]

for every target in the stated range.

## Required conclusion

A proof of the requested theorem, combined with the proved binary correction lemma, yields

\[
H_{n!}(X_n+1)
\le
M_n+r_n
=
\lceil16(\log n)^2\rceil+
\lceil4\log n\rceil.
\]

Every representation then uses numerically distinct divisors because different layers have different 2-adic valuations and the correction palette consists only of pure powers of two.

## Exact hypotheses already supplied by Nova 1

1. Every element of every `A_t(n)` divides `n!`.
2. A legal rainbow selection contains pairwise distinct main divisors.
3. Main divisors are disjoint from
   \[
   \{1,2,\ldots,2^{r_n-1}\}.
   \]
4. The formal profile-capacity gate passes conditionally on the explicit prime-interval lower bound sent to Nova 3.
5. No sequential selection rule is imposed.

## Mandatory issues the proof must resolve

- uniformity for every integer target, not almost all targets;
- exact downward orientation and both interval endpoints;
- inaccessible residue classes after the binary palette is included;
- additive shell gaps;
- collisions between different rainbow profiles;
- whether a proposed decoder secretly imposes a sequential one-choice architecture;
- exact selected-term count;
- finite exceptions below `n_0`.

## Dependencies

- `proofs/VALUATION_BUDGET_LEMMAS.md`
- `proofs/DISTINCTNESS_AND_CORRECTION.md`
- `proofs/COUNTING_CAPACITY_OBSTRUCTION.md`
- `proofs/MENU_ENTROPY_REQUIREMENT.md`
- `proofs/HIGH_PRIME_MENU_CAPACITY.md`
- `constructions/VALUATION_TAGGED_ADDRESS_PACKETS.md`
- `PREFERRED_ROUTE.md`

## Verification command

No repository-wide verifier exists yet. Nova 2 must provide either a complete proof artifact or reproducible finite falsification code with exact witnesses. Finite evidence must not be promoted to the asymptotic theorem.

## Known failure modes

- large formal profile count with low distinct-sum count;
- common residue obstruction across all addressed layers;
- maximum downward gap exceeding `2^{r_n}-1`;
- a proof using more than one term from a layer;
- a sequential decoder falling under a Phase 12P-type obstruction.

## What is not claimed

Nova 1 does not claim that the requested occupancy theorem is true. Capacity, legality, and distinctness do not imply coverage.

## Requested next action

Attempt either:

1. a proof of the exact frozen theorem; or
2. a rigorous counterexample family or asymptotic obstruction for the exact frozen layers.

Return one of `ACCEPTED`, `ACCEPTED_WITH_RESTRICTIONS`, `REJECTED`, `NEEDS_REPAIR`, or `SUPERSEDED`, with the exact commit SHA of the result.