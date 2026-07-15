# Handoff to Nova 4

Handoff ID: `N1-HO-N4-002`

Supersedes: `N1-HO-N4-001`

Sending track: Nova 1, Factorial Structure and Reduction

Receiving track: Nova 4, Computation, Falsification, and Verification

Date: 2026-07-15

Result status: **finite certificate** and **computational evidence** request

Theorem or object IDs: `N1-CON-001`, `N1-CON-003`, `N2-ADD-115`, `N2-OBS-107`, `N1-STR-014`, `N1-STR-015`, `N1-RED-004`, `N1-STR-019`, `N1-STR-020`, `N1-RED-006`, `N1-CMP-003`, `N1-CMP-004`

## Exact source baselines

### Disproved predecessor

- Nova 1 old handoff commit: `b939574eb88a08bb03abda5bbe6ff2ca97444e08`
- Nova 2 branch: `nova/additive-occupancy`
- Nova 2 result commit: `45c74a5fa747551422ffcad7d3ddf22788fbe622`
- theorem: `N2-ADD-115`
- disproved model: `N2-OBS-107`

### Repaired construction

- construction: `N1-CON-003`
- construction file: `constructions/MARKER_THREE_VALUATION_RAINBOW.md`
- lattice proof: `proofs/MARKER_THREE_LATTICE_REPAIR.md`
- menu proof: `proofs/MARKER_THREE_MENU_CAPACITY.md`
- endpoint proof: `proofs/QUOTIENT_ENDPOINT_SUPPORT.md`
- initial quotient verifier: `verification/marker_three_sanity.py`
- endpoint verifier: `verification/endpoint_support_sanity.py`

Nova 4 must cite the exact Nova 1 commit it imports.

## Study A: old-obstruction regression

Reconstruct the old addresses

\[
e_t=r_n+t
\]

and verify that every old main sum lies in

\[
2^{r_n+1}\mathbb Z.
\]

For every tested admissible `n`, verify that the target `x=2^r_n` has required window

\[
[1,2^{r_n}],
\]

which contains no old main sum.

Expected result: exact reproduction of `N2-OBS-107`.

## Study B: repaired structural gate

For the repaired construction, define reduced legal parameters

\[
r^*=3,
\qquad
M_n^*=\min(12,v_2(n!)+1).
\]

For every `7<=n<=14`, exhaust the complete quotient interval

\[
0\le q\le\left\lfloor X_n/3\right\rfloor.
\]

Verify:

1. every generated term divides `n!`;
2. layer `t` has exact 2-adic valuation `t-1`;
3. different layers are numerically disjoint;
4. every main term is divisible by `3`;
5. the main support lattice is exactly `3Z`;
6. the palette `{1,2,4}` is disjoint from all main terms;
7. palette sums attain all residues modulo `3`;
8. quotient support has additive span one;
9. maximum downward quotient distance;
10. first target exceeding `W^*=1`;
11. exact reconstruction of every original target through `X_n`.

Expected initial result: maximum downward distance zero for `n=7` and one for `8<=n<=14`.

## Study C: enlarged reduced-menu falsification

For every integer

\[
15\le n\le80,
\]

construct a deterministic reduced core catalogue containing:

1. `u=1`;
2. every odd `u<=n` satisfying `3u|n!`;
3. every subset product of primes in `(n/2,n]` below the layer cutoff;
4. no duplicate numerical core.

Use

\[
M_n^*=\min(12,v_2(n!)+1),
\qquad
T_n=\min\left(\left\lfloor X_n/3\right\rfloor,10^7\right).
\]

Compute exact quotient rainbow reachability in `[0,T_n]`. Report:

- layer sizes;
- formal profile count;
- distinct reachable sums;
- collision ratio;
- support gcd;
- residue occupancy modulo `2<=m<=64`;
- maximum downward distance;
- first target with distance greater than one;
- maximum attainable sum and endpoint deficit;
- exact witnesses for new maximum gaps;
- first structural or occupancy failure.

A failure disproves the reduced model only unless it also applies to the full frozen menu.

## Study D: independent endpoint-support reconstruction

Independently reconstruct the following proved theorems.

### N1-STR-019

For every `n>=6`,

\[
D_n=\frac{n!}{3\cdot2^{v_2(n!)}}
\]

is multiplicatively `3`-dense.

Finite check:

- generate every divisor of `D_n` for each `6<=n<=20`;
- verify every consecutive divisor ratio is at most `3`.

### N1-STR-020

For every `n>=12`, each of the first three quotient layers contains a term

\[
X_n/9<b_t\le X_n/3.
\]

Verify exact legality, exact 2-adic valuations `0,1,2`, pairwise numerical distinctness, and

\[
b_1+b_2+b_3>\left\lfloor X_n/3\right\rfloor.
\]

The verdict must distinguish:

- **endpoint support passed:** maximum attainable quotient sum reaches beyond the endpoint;
- **endpoint-window occupancy open:** no conclusion yet about a sum in `[Q_n-W_n,Q_n]`.

### N1-RED-006

For every `12<=n<=14`, every quotient target, and `1<=L<=6`, verify the exact integer form of

\[
\rho_L<\max\{(2/3)^Lq,2^L\}.
\]

Do not promote this coarse contraction to the polynomial-window theorem.

## Study E: adversarial corruption tests

The verifier must fail closed on:

- a core with `3u` not dividing `n!`;
- an even core;
- a main term above `X_n`;
- duplicate 2-adic layer addresses;
- duplicate terms inside a layer;
- a main term not divisible by `3`;
- a main term equal to a palette term;
- selection of two terms from one layer;
- repeated numerical divisor under different labels;
- false target sum;
- understated term count;
- truncated interval presented as complete;
- reporting endpoint support as endpoint-window occupancy.

## Required files

- deterministic source code;
- valid and deliberately corrupted tests;
- environment record;
- machine-readable summaries;
- exact first-failure witnesses;
- one-command reproduction README;
- response handoff citing the exact imported Nova 1 commit.

## Dependencies

- `proofs/MARKER_THREE_LATTICE_REPAIR.md`
- `proofs/MARKER_THREE_MENU_CAPACITY.md`
- `proofs/QUOTIENT_ENDPOINT_SUPPORT.md`
- `constructions/MARKER_THREE_VALUATION_RAINBOW.md`
- `PREFERRED_ROUTE.md`
- `verification/marker_three_sanity.py`
- `verification/endpoint_support_sanity.py`

## What is not claimed

No finite study proves the asymptotic quotient-window theorem, factorial half-range theorem, Track B implication, or main Erdős problem.

## Requested next action

Return an exact finite certificate, exact counterexample, or exact resource-limit report. State the receiver outcome, branch name, exact commit SHA, verifier path, and first unresolved theorem node.