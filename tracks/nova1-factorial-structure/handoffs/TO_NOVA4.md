# Handoff to Nova 4

Handoff ID: `N1-HO-N4-002`

Supersedes: `N1-HO-N4-001`

Sending track: Nova 1, Factorial Structure and Reduction

Receiving track: Nova 4, Computation, Falsification, and Verification

Date: 2026-07-15

Result status: **finite certificate** and **computational evidence** request

Theorem or object IDs: `N1-CON-001`, `N1-CON-003`, `N2-ADD-115`, `N2-OBS-107`, `N1-STR-014`, `N1-STR-015`, `N1-RED-004`, `N1-CMP-003`

## Exact source baselines

### Disproved predecessor

- Nova 1 branch: `nova/factorial-structure`
- old handoff commit audited by Nova 2: `b939574eb88a08bb03abda5bbe6ff2ca97444e08`
- Nova 2 branch: `nova/additive-occupancy`
- Nova 2 exact result commit: `45c74a5fa747551422ffcad7d3ddf22788fbe622`
- theorem: `N2-ADD-115`
- disproved model: `N2-OBS-107`

### Repaired construction

- construction: `N1-CON-003`
- file: `constructions/MARKER_THREE_VALUATION_RAINBOW.md`
- proof: `proofs/MARKER_THREE_LATTICE_REPAIR.md`
- initial verifier: `verification/marker_three_sanity.py`
- initial report: `verification/MARKER_THREE_FINITE_REPORT.md`

Nova 4 must cite the exact Nova 1 commit it imports. Do not use a moving branch name as the only identifier.

## Study A: mandatory old-obstruction regression

Reconstruct the old layers

\[
e_t=r_n+t,
\qquad
A_t(n)=\{2^{e_t}u:u\text{ odd},\ u>1,\ 2^{e_t}u\le X_n\}.
\]

Verify symbolically and computationally that every old main sum lies in

\[
2^{r_n+1}\mathbb Z.
\]

For every tested admissible `n` with `2^r_n<=X_n`, verify that the target

\[
x=2^{r_n}
\]

has old downward window

\[
[1,2^{r_n}],
\]

which contains no old main sum.

This regression must fail if the implementation accidentally includes zero inside the window or lowers an old address.

Expected result: exact reproduction of `N2-OBS-107`.

## Study B: exact repaired structural gate

For the repaired construction, define

\[
X_n=\lfloor\sqrt{n!}\rfloor,
\]

and reduced legal parameters

\[
r_n^*=3,
\qquad
M_n^*=\min(12,v_2(n!)+1).
\]

For `1<=t<=M_n^*`, define the full repaired layer whenever full divisor enumeration is feasible:

\[
A_t^{(3),*}(n)=
\left\{
3\cdot2^{t-1}u:
 u\text{ odd},\ 3u\mid n!,\ 3\cdot2^{t-1}u\le X_n
\right\}.
\]

Define quotient layers by dividing every main term by `3`.

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
7. palette subset sums attain all residues modulo `3`;
8. the quotient support has additive span one;
9. the maximum downward quotient distance;
10. the first target exceeding
   \[
   W^*=\left\lfloor\frac{(2^3-1)-2}{3}\right\rfloor=1;
   \]
11. exact reconstruction of every original target `0<=x<=X_n`.

The expected initial report is maximum downward distance zero for `n=7` and one for every `8<=n<=14`.

## Study C: enlarged reduced-menu falsification

For every integer

\[
15\le n\le80,
\]

construct a deterministic reduced core catalogue containing:

1. `u=1`;
2. every odd `u<=n` satisfying `3u|n!`;
3. every subset product of primes in `(n/2,n]` not exceeding the layer cutoff;
4. no duplicate numerical core.

Use

\[
M_n^*=\min(12,v_2(n!)+1),
\qquad
T_n=\min\left(\left\lfloor X_n/3\right\rfloor,10^7\right).
\]

Compute exact quotient rainbow reachability in `[0,T_n]`. Report:

1. every layer size;
2. formal profile count;
3. distinct reachable quotient sums;
4. collision ratio;
5. exact support gcd;
6. residue occupancy modulo every `2<=m<=64`;
7. maximum downward distance;
8. first target with distance greater than `W^*=1`;
9. maximum attainable sum and endpoint deficit;
10. one exact witness for every new maximum gap;
11. the first structural or occupancy failure.

This is a reduced catalogue, not the full asymptotic menu. A failure disproves the reduced model only unless its witness also applies to the full frozen menu.

## Study D: adversarial corruption tests

The verifier must fail closed on:

- a core with `3u` not dividing `n!`;
- an even core;
- a main term above `X_n`;
- two layers assigned the same 2-adic address;
- duplicate terms inside a layer;
- a main term not divisible by `3`;
- a main term equal to a palette term;
- a witness selecting two terms from one layer;
- a repeated numerical divisor under different labels;
- a false target sum;
- an understated term count;
- a truncated target interval presented as complete.

## Required files

- deterministic source code;
- tests for valid and deliberately corrupted inputs;
- environment and dependency record;
- exact machine-readable summaries;
- exact first-failure witnesses;
- a README with one reproduction command;
- a response handoff citing the exact imported Nova 1 commit.

## Dependencies

- `proofs/MARKER_THREE_LATTICE_REPAIR.md`
- `proofs/MARKER_THREE_MENU_CAPACITY.md`
- `constructions/MARKER_THREE_VALUATION_RAINBOW.md`
- `PREFERRED_ROUTE.md`
- `verification/marker_three_sanity.py`

## What is not claimed

No finite study proves the asymptotic quotient-window theorem, the factorial half-range theorem, the Track B implication, or the main Erdős problem.

## Requested next action

Return an exact finite certificate, exact counterexample, or exact resource-limit report. State the receiver outcome, branch name, exact commit SHA, verifier path, and the first unresolved theorem node.
