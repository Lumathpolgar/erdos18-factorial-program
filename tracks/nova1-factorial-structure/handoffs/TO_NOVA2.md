# Handoff to Nova 2

Handoff ID: `N1-HO-N2-002`

Supersedes: `N1-HO-N2-001`

Sending track: Nova 1, Factorial Structure and Reduction

Receiving track: Nova 2, Additive Occupancy and Global Sumsets

Date: 2026-07-15

Result status: **conditional theorem** request

Theorem or object IDs: `N1-CON-003`, `N1-STR-014`, `N1-STR-015`, `N1-RED-004`, `N1-RED-005`, `N1-STR-019`, `N1-STR-020`, `N1-RED-006`, `N1-REQ-N2-002`

## Prior handoff disposition

`N1-HO-N2-001` was rejected by Nova 2 at:

- branch: `nova/additive-occupancy`
- exact commit: `45c74a5fa747551422ffcad7d3ddf22788fbe622`
- theorem: `N2-ADD-115`
- disproved model: `N2-OBS-107`

The old common factor was `2^(r_n+1)`, larger than the old correction radius plus one. This revised handoff changes the construction and has a new ID.

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
 u\text{ odd},
 3u\mid n!,
 3\cdot2^{t-1}u\le X_n
\right\},
\]

\[
B_t(n)=
\left\{
2^{t-1}u:u\in U_t(n)
\right\}.
\]

Define the quotient rainbow sumset

\[
\mathcal Q_n=
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
[q-W_n,q]\cap\mathcal Q_n\ne\varnothing.
\]

A proof of exact representation is stronger than required.

## Required conclusion

Nova 1 proved that the requested theorem implies

\[
H_{n!}(X_n+1)
\le
M_n+r_n
=
\lceil16(\log n)^2\rceil+
\lceil4\log n\rceil.
\]

Write `x=3q+delta`, with `delta in {0,1,2}`. If `q<=W_n`, the palette handles `x` directly. Otherwise a quotient sum `s in [q-W_n,q]` gives residual

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
7. The correction radius exceeds every unresolved lattice residue gap.
8. The first requested target is directly covered.
9. The quotient support has lattice span one because `1 in B_1(n)`.
10. No sequential partial-coverage invariant is imposed by the frozen theorem request.
11. Total selected-term cost is at most `M_n+r_n`.
12. Necessary formal profile capacity holds for every `n>=120368`.

## New endpoint-support theorem

Nova 1 proved:

### N1-STR-019

For every `n>=6`,

\[
D_n=\frac{n!}{3\cdot2^{v_2(n!)}}
\]

is multiplicatively `3`-dense.

### N1-STR-020

For every `n>=12`, each of `B_1(n)`, `B_2(n)`, and `B_3(n)` contains a legal term `b_t` satisfying

\[
X_n/9<b_t\le X_n/3.
\]

The three terms are numerically distinct and

\[
b_1+b_2+b_3>X_n/3.
\]

Hence

\[
\max\mathcal Q_n
\ge
\left\lfloor X_n/3\right\rfloor+1.
\]

Therefore the target range is not outside the total attainable support.

This does not prove that the downward endpoint window

\[
[\lfloor X_n/3\rfloor-W_n,\lfloor X_n/3\rfloor]
\]

contains a sum. That remains part of the requested occupancy theorem.

Proof:

`tracks/nova1-factorial-structure/proofs/QUOTIENT_ENDPOINT_SUPPORT.md`

## Coarse deterministic reduction

`N1-RED-006` proves that a deterministic increasing-layer procedure leaves residual

\[
\rho_L<\max\{(2/3)^Lq,2^L\}.
\]

This is rigorous but too weak to reach the polynomial radius `W_n`. It must not be presented as closing the requested theorem.

## Unconditional initial range

For all sufficiently large `n`, every integer

\[
0\le x\le3m_n(2^{M_n}-1)+2
\]

is represented, where `m_n` is the largest odd integer at most `n`.

This is not the half-range theorem.

## Finite evidence

Run:

```text
python tracks/nova1-factorial-structure/verification/marker_three_sanity.py
python tracks/nova1-factorial-structure/verification/endpoint_support_sanity.py
```

The finite audits cover:

- reduced quotient occupancy for `7<=n<=14`;
- multiplicative 3-density for `6<=n<=20`;
- endpoint crossing for `12<=n<=20`;
- exhaustive coarse contraction for all quotient targets with `12<=n<=14` and `1<=L<=6`.

Result labels: **computational evidence** and **finite certificate** only.

## Mandatory issues the proof must resolve

- uniformity for every integer quotient target;
- exact downward orientation and endpoints;
- downward endpoint-window occupancy, not merely total endpoint reach;
- additive shell gaps larger than `W_n`;
- collision concentration between different rainbow profiles;
- exact integer lattice and all resonances of any proposed probability law;
- whether any decoder secretly imposes sequential partial coverage;
- finite exceptions below `n_0`.

## Dependencies

- `proofs/MARKER_THREE_LATTICE_REPAIR.md`
- `proofs/MARKER_THREE_MENU_CAPACITY.md`
- `proofs/QUOTIENT_ENDPOINT_SUPPORT.md`
- `proofs/VALUATION_BUDGET_LEMMAS.md`
- `proofs/COUNTING_CAPACITY_OBSTRUCTION.md`
- `proofs/MENU_ENTROPY_REQUIREMENT.md`
- `constructions/MARKER_THREE_VALUATION_RAINBOW.md`
- `PREFERRED_ROUTE.md`

## Verification requirement

Before analytic work, audit the structural gate independently. If it passes, freeze the exact quotient numerical-value probability law, lattice span, target-dependent tilt, and bounded-torus characteristic function.

A finite counterexample must include the exact `n`, quotient target `q`, downward distance, generated layers, and an independently replayable verifier.

## Known failure modes

- a quotient maximum gap exceeding `W_n`;
- a downward endpoint-window deficit despite total support crossing the endpoint;
- large formal profile count with few numerical sums;
- an overlooked quotient residue obstruction;
- illegal reuse of one layer or numerical divisor;
- a sequential proof falling under a Phase 12P-type information ceiling.

## What is not claimed

Nova 1 does not claim the quotient occupancy theorem is true. Structural compatibility, endpoint reach, and finite evidence do not imply asymptotic coverage.

## Requested next action

Return one of:

- `ACCEPTED`;
- `ACCEPTED_WITH_RESTRICTIONS`;
- `REJECTED`;
- `NEEDS_REPAIR`;
- `SUPERSEDED`.

Include the exact branch, commit SHA, proof or counterexample location, and first unresolved theorem node.