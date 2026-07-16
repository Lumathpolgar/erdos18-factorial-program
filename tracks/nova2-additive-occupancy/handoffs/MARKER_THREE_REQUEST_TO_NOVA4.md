# Marker-Three Verification Request to Nova 4

Handoff ID: `N2-HO-N4-002`

Sending track: Nova 2, Additive Occupancy and Global Sumsets

Receiving track: Nova 4, Computation, Falsification, and Verification

Date: 2026-07-15

Result status: finite certificate request, computational evidence request, and falsification request

## Frozen inputs

### Nova 1 marker-three model

- branch: `nova/factorial-structure`
- exact commit: `ebb47ba436af554366d0f285119a769f31f9e561`
- construction: `N1-CON-003`
- handoff: `N1-HO-N2-002`

### Nova 2 intake and reduction

- branch: `nova/additive-occupancy`
- structural outcome: `ACCEPTED_WITH_RESTRICTIONS`
- response: `handoffs/RESPONSE_TO_NOVA1_MARKER_THREE.md`
- theorem IDs: `N2-ADD-119`, `N2-ADD-120`
- proof: `proofs/MARKER_THREE_CARRIER_BLOCK_REDUCTION.md`

Every run must record the exact source branch and commit SHA.

## Exact marker-three objects

For each tested `n`, compute exactly:

\[
X_n=\lfloor\sqrt{n!}\rfloor,
\quad
Y_n=\lfloor X_n/3\rfloor,
\quad
r_n=\lceil4\log n\rceil,
\quad
M_n=\lceil16(\log n)^2\rceil,
\]

\[
W_n=\left\lfloor\frac{2^{r_n}-3}{3}\right\rfloor.
\]

For `1<=t<=M_n`, generate or certify

\[
U_t(n)=
\{u\ge1:u\text{ odd},\ 3u\mid n!,\ 2^{t-1}u\le Y_n\},
\]

\[
B_t(n)=\{2^{t-1}u:u\in U_t(n)\}.
\]

Distinguish full menus from any reduced-menu experiment.

## Study M1: structural replay

Independently verify:

1. every main term `3*2^(t-1)*u` divides `n!`;
2. exact 2-adic layer separation;
3. main-palette numerical disjointness;
4. exact main lattice `3 Z`;
5. quotient span one;
6. binary correction coverage `[0,2^{r_n}-1]`;
7. exact quotient reduction with radius `W_n`;
8. exact term budget `M_n+r_n`.

Return a separate verdict for each item.

## Study M2: connected-core carrier recursion

Set `E_0=0`. At layer `t`, compute

\[
D_t=
\left\lfloor
\frac{E_{t-1}+W_n+1}{2^{t-1}}
\right\rfloor.
\]

In the ordered set `{0} union U_t(n)`, find the connected component of zero under consecutive core gaps at most `D_t`. Let `u_t^*` be the largest certified core in that component and set

\[
E_t=E_{t-1}+2^{t-1}u_t^*.
\]

Report for every layer:

- `D_t`;
- `u_t^*`;
- `E_t`;
- the first blocking core gap, if one exists;
- the exact two cores on either side of that gap;
- whether `E_t+W_n>=Y_n`.

The first failed carrier gap is a failure of N2-ADD-120's proof engine only. It is not automatically a counterexample to the full rainbow model.

## Study M3: full quotient rainbow reachability

For feasible exact ranges, compute the full restricted sumset

\[
Q_n=
\left\{
\sum_{t=1}^{M_n}b_t:
 b_t\in B_t(n)\cup\{0\}
\right\}
\]

through a declared cutoff.

Report:

1. every layer size;
2. formal profile count;
3. number of distinct reachable sums;
4. collision multiplicity or collision ratio;
5. maximum downward gap;
6. the first target `q` with
   \[
   Q_n\cap[q-W_n,q]=\varnothing;
   \]
7. an exact witness for every new support maximum;
8. whether the computation used full or reduced menus.

A reduced-menu failure is not a failure of the full construction unless accompanied by a structural proof applying to all omitted choices.

## Study M4: deterministic prefix replay

Replay Nova 1's odd-digit theorem and Nova 2's final-window extension.

Let `m_n` be the largest odd integer at most `n`. Verify that the full model contains a downward one-dense quotient subset through

\[
A_n=m_n(2^{M_n}-1)
\]

whenever the stated structural conditions hold, and that required `W_n`-window occupancy therefore extends through

\[
A_n+W_n.
\]

No counterexample search may report a target at or below this protected bound.

## Study M5: endpoint support

Compute exact upper bounds and lower certificates for the maximum reachable quotient sum. Compare them with

\[
Y_n=\lfloor X_n/3\rfloor.
\]

If the maximum possible sum is below `Y_n-W_n`, return the exact endpoint counterexample. This would disprove the frozen model.

Do not infer endpoint reach from formal profile count.

## Required output classification

Use exactly one of:

- `finite certificate`;
- `computational evidence`;
- `disproved model`.

Also distinguish:

- failure of the carrier-block sufficient condition;
- failure of a reduced menu;
- failure of the full frozen marker-three model.

## Smallest-witness order

Return the lexicographically smallest witness by:

1. smallest `n`;
2. smallest quotient target `q`;
3. smallest layer `t` or violated gate;
4. smallest exact core gap.

A symbolic obstruction takes priority over finite enumeration.

## Implementation requirements

- exact integer arithmetic for legality, menus, gaps, and reachability;
- certified logarithmic ceilings;
- no unchecked floating-point square roots of factorials;
- deterministic resource limits;
- fail-closed certificates;
- corrupted-certificate tests;
- exact metadata for all imported artifacts.

## Requested next action

Implement Study M2 first because it scales without enumerating the full rainbow sumset. Then run Study M3 where feasible. Return separate verdicts for the carrier proof engine and the full marker-three construction.