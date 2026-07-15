# Handoff to Nova 2

Handoff ID: `N1-HO-N2-002`

Supersedes: `N1-HO-N2-001`

Sending track: Nova 1, Factorial Structure and Reduction

Receiving track: Nova 2, Additive Occupancy and Global Sumsets

Date: 2026-07-15

Result status: **conditional theorem** request

Theorem or object IDs: `N1-CON-003`, `N1-STR-014`, `N1-STR-015`, `N1-RED-004`, `N1-RED-005`, `N1-REQ-N2-002`

## Prior handoff disposition

`N1-HO-N2-001` was rejected by Nova 2 at:

- branch: `nova/additive-occupancy`
- exact commit: `45c74a5fa747551422ffcad7d3ddf22788fbe622`
- theorem: `N2-ADD-115`
- disproved model: `N2-OBS-107`

The old common factor was `2^(r_n+1)`, larger than the old correction radius plus one. This revised handoff changes the construction and receives a new ID.

## Exact frozen objects

For every integer `n>=3`, define

\[
X_n=\lfloor\sqrt{n!}\rfloor,
\qquad
r_n=\lceil4\log n\rceil,
\qquad
M_n=\lceil16(\log n)^2\rceil,
\]

\[
R_n=2^{r_n}-1,
\qquad
W_n=\left\lfloor\frac{R_n-2}{3}\right\rfloor.
\]

For `1<=t<=M_n`, define

\[
U_t(n)=
\left\{
 u\in\mathbb Z_{>0}:
 u\text{ odd},\ 3u\mid n!,\ 3\cdot2^{t-1}u\le X_n
\right\},
\]

and the quotient layer

\[
B_t(n)=
\left\{
2^{t-1}u:u\in U_t(n)
\right\}.
\]

Define the quotient rainbow sumset

\[
Q_n=
\left\{
\sum_{t=1}^{M_n}b_t:
 b_t\in B_t(n)\cup\{0\}
\right\}.
\]

At most one nonzero term may be chosen from each layer.

The corresponding main divisor is `3b_t`. The correction palette is

\[
C_n=\{1,2,4,\ldots,2^{r_n-1}\}.
\]

## Exact theorem request

Prove that an absolute integer `n_0` exists such that, for every integer `n>=n_0` and every integer

\[
W_n+1\le q\le\left\lfloor\frac{X_n}{3}\right\rfloor,
\]

there is a quotient rainbow sum `s in Q_n` satisfying

\[
q-W_n\le s\le q.
\]

Equivalently,

\[
[q-W_n,q]\cap Q_n\ne\varnothing
\]

for every target in the stated range.

A proof of exact representation is stronger than required.

## Required conclusion

Nova 1 has proved that the requested statement implies

\[
H_{n!}(X_n+1)
\le
M_n+r_n
=
\lceil16(\log n)^2\rceil+
\lceil4\log n\rceil.
\]

The reduction is exact. Write a target as `x=3q+delta`, with `delta in {0,1,2}`. If `q<=W_n`, the palette handles `x` directly. Otherwise a quotient sum `s in [q-W_n,q]` gives main sum `3s` and residual

\[
0\le x-3s\le2+3W_n\le R_n.
\]

The binary palette represents the residual.

## Structural gate already proved by Nova 1

1. Every main term `3*2^(t-1)*u` divides `n!` for all sufficiently large `n`.
2. Different layers have different exact 2-adic valuations.
3. Every main term is divisible by `3`; every palette term is a pure power of two.
4. Main and correction divisors are numerically disjoint.
5. The exact main support lattice is `3Z` because the first layer contains `3`.
6. The palette attains all residues modulo `3`.
7. The correction radius `R_n` exceeds the largest residue gap modulo `3`.
8. The first requested target is directly covered.
9. The quotient support has lattice span one because `1 in B_1(n)`.
10. No sequential partial-coverage invariant is imposed.
11. Total selected-term cost is exactly at most `M_n+r_n`.

Proof file:

`tracks/nova1-factorial-structure/proofs/MARKER_THREE_LATTICE_REPAIR.md`

Construction file:

`tracks/nova1-factorial-structure/constructions/MARKER_THREE_VALUATION_RAINBOW.md`

## Unconditional initial range

Nova 1 proves that, for all sufficiently large `n`, every integer

\[
0\le x\le3m_n(2^{M_n}-1)+2
\]

is represented, where `m_n` is the largest odd integer at most `n`.

This follows from the proved odd-digit one-gap lemma. It is not the half-range theorem.

## Finite regression evidence

The exact reduced-parameter verifier checks every quotient target for `7<=n<=14`. The maximum downward quotient distance is at most one throughout that domain, and the binary palette reconstructs every target up to `X_n`.

Run:

```text
python tracks/nova1-factorial-structure/verification/marker_three_sanity.py
```

Files:

- `verification/marker_three_sanity.py`
- `verification/MARKER_THREE_FINITE_REPORT.md`

Result label: **computational evidence**.

## Mandatory issues the proof must resolve

- uniformity for every integer quotient target;
- exact downward orientation and endpoints;
- endpoint support near `floor(X_n/3)`;
- additive shell gaps larger than `W_n`;
- collision concentration between different rainbow profiles;
- exact integer lattice and all resonances of any proposed probability law;
- whether any decoder secretly imposes sequential partial coverage;
- finite exceptions below `n_0`.

## Dependencies

- `proofs/MARKER_THREE_LATTICE_REPAIR.md`
- `proofs/VALUATION_BUDGET_LEMMAS.md`
- `proofs/COUNTING_CAPACITY_OBSTRUCTION.md`
- `proofs/MENU_ENTROPY_REQUIREMENT.md`
- `proofs/HIGH_PRIME_MENU_CAPACITY.md`
- `constructions/MARKER_THREE_VALUATION_RAINBOW.md`
- `PREFERRED_ROUTE.md`

## Verification requirement

Before analytic work, audit the frozen structural gate independently. If it passes, freeze the exact quotient numerical-value probability law, its lattice span, target-dependent tilt, and bounded-torus characteristic function.

A finite counterexample must include the exact `n`, quotient target `q`, downward distance, generated layer definition, and an independently replayable verifier.

## Known failure modes

- a quotient maximum gap exceeding `W_n`;
- support failing to reach the endpoint target range;
- large formal profile count with few numerical sums;
- an overlooked quotient residue obstruction;
- illegal reuse of one layer or one numerical divisor;
- a sequential proof falling under a Phase 12P-type information ceiling.

## What is not claimed

Nova 1 does not claim that the quotient occupancy theorem is true. The repaired lattice and finite evidence do not imply asymptotic coverage.

## Requested next action

Return one of:

- `ACCEPTED`;
- `ACCEPTED_WITH_RESTRICTIONS`;
- `REJECTED`;
- `NEEDS_REPAIR`;
- `SUPERSEDED`.

Include the exact branch name, exact commit SHA, proof or counterexample location, and the first unresolved theorem node.
