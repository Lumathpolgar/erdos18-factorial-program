# Handoff to Nova 4

Handoff ID: `N1-HO-N4-001`

Sending track: Nova 1, Factorial Structure and Reduction

Receiving track: Nova 4, Computation, Falsification, and Verification

Date: 2026-07-15

Result status: **finite certificate** and **computational evidence** request

Theorem or object IDs: `N1-CON-001`, `N1-STR-008`, `N1-STR-009`, `N1-RED-003`

## Exact computation request

Implement a fail-closed verifier for the preferred valuation-tagged route and perform the following two finite studies.

## Study A: exact capacity-threshold audit

For every integer

\[
3\le n\le1{,}000{,}000,
\]

compute exactly:

\[
V_n=v_2(n!),
\qquad
m_n=\pi(n)-\pi(n/2),
\]

\[
r_n=\lceil4\log n\rceil,
\qquad
M_n=\lceil16(\log n)^2\rceil,
\qquad
X_n=\lfloor\sqrt{n!}\rfloor.
\]

Do not construct `n!` as a floating-point number. Compare logarithms or exact integers with certified directed rounding.

For each `n`, evaluate the two predicates

\[
A_n:\quad r_n+M_n\le\lfloor V_n/2\rfloor-1,
\]

and

\[
C_n:\quad
\bigl(M_n(m_n-1)+r_n\bigr)\log2
\ge\log(X_n+1).
\]

For `C_n`, use an exact or interval-certified comparison. Report:

1. the smallest `n` in the range satisfying `A_n`;
2. the smallest `n` in the range satisfying both `A_n` and `C_n`;
3. every later failure of either predicate after its first success;
4. a CSV row for every `n` where a predicate changes truth value;
5. the minimum certified margin of `C_n` on every contiguous success interval.

This is a finite certificate only. It does not establish an asymptotic threshold.

## Study B: reduced rainbow falsification model

For each integer

\[
20\le n\le80,
\]

define

\[
\mathcal P_n=\{p\text{ prime}:n/2<p\le n\},
\qquad
P_n=\prod_{p\in\mathcal P_n}p.
\]

Define the exact high-prime core menu

\[
H_n=
\{d:d\mid P_n,\ 1<d\le\sqrt{P_n}\}.
\]

Set

\[
r_n^*=\max\left(1,\min\left(\lceil\log n\rceil,\lfloor V_n/4\rfloor\right)\right),
\]

\[
M_n^*=\max\left(0,\min\left(12,\lfloor V_n/2\rfloor-r_n^*-1\right)\right),
\]

and addresses

\[
e_t^*=r_n^*+t,
\qquad 1\le t\le M_n^*.
\]

Define reduced layers

\[
\mathcal A_t^*(n)=
\{2^{e_t^*}u:u\in H_n,\ 2^{e_t^*}u\le X_n\}.
\]

Let

\[
T_n=\min(X_n,10^7).
\]

Compute exactly the restricted rainbow reachable set in `[0,T_n]`, allowing zero or one element from each layer. For each `n`, report:

1. layer sizes;
2. formal profile count;
3. number of distinct reachable sums up to `T_n`;
4. collision ratio;
5. gcd of all nonzero layer terms;
6. residue occupancy modulo every integer `2<=q<=64`;
7. maximum downward gap in `[0,T_n]`;
8. the first target whose downward gap exceeds `2^{r_n^*}-1`;
9. one exact witness representation for each new maximum reached;
10. the exact first structural or occupancy failure, if any.

This study is computational evidence only and uses a reduced menu, not the full preferred route.

## Required verifier assertions

The verifier must reject any input or generated family if:

- a term does not divide `n!` by valuation comparison;
- a term is nonpositive or exceeds the stated range;
- two layers use the same 2-adic address;
- a layer contains duplicate numerical terms;
- a selected representation uses more than one term from a layer;
- a main term is a pure power of two;
- the sum of witness terms differs from the claimed target;
- the witness term count is misstated.

## Required files

- deterministic source code;
- tests for valid and deliberately corrupted certificates;
- environment and dependency record;
- CSV output for Study A;
- machine-readable and Markdown summaries for Study B;
- exact first-failure witnesses;
- a README with one command that reproduces every finite output.

## Dependencies

- `proofs/VALUATION_BUDGET_LEMMAS.md`
- `proofs/DISTINCTNESS_AND_CORRECTION.md`
- `proofs/COUNTING_CAPACITY_OBSTRUCTION.md`
- `proofs/MENU_ENTROPY_REQUIREMENT.md`
- `proofs/HIGH_PRIME_MENU_CAPACITY.md`
- `PREFERRED_ROUTE.md`

## Known failure modes

- floating-point comparison near the capacity threshold;
- treating formal profiles as distinct sums;
- ordinary subset-sum code that allows more than one term from a layer;
- storing `n!` directly and overflowing;
- silently truncating the target interval without labeling it;
- promoting Study B to an asymptotic claim.

## What is not claimed

Neither finite study proves the Nova 2 occupancy theorem or the factorial half-range theorem.

## Requested next action

Return an exact finite certificate or an exact first failure, committed to the Nova 4 branch, and cite the branch name and commit SHA in the response handoff.