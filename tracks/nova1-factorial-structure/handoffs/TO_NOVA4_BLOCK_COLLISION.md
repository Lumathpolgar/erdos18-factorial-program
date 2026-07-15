# Nova 1 Block and Collision Verification Handoff to Nova 4

Handoff ID: `N1-HO-N4-003`

Sending track: Nova 1, Factorial Structure and Reduction

Receiving track: Nova 4, Computation, Falsification, and Verification

Date: 2026-07-15

Result status: independent finite reconstruction request

## Objects to reconstruct

### N1-STR-021

For

\[
A_k=\frac{k!}{3\cdot2^{v_2(k!)}},
\qquad
m_{n,k}=\max\{m\le n-k:m\text{ odd}\},
\]

verify that every odd core `A_k j`, with odd `1<=j<=m_{n,k}`, satisfies

\[
3A_kj\mid n!.
\]

Verify that the block is connected from zero whenever the core-gap threshold is at least `2A_k`.

### N1-DIS-006

For the exact Nova 2 carrier threshold

\[
D_t=\left\lfloor\frac{E_{t-1}+W_n+1}{2^{t-1}}\right\rfloor,
\]

implement the strongest one-factorial-block-per-layer recursion and verify the one-step ceiling

\[
E_t+W_n+1
\le
\left(1+\frac n2\right)(E_{t-1}+W_n+1).
\]

Report:

1. the first `n` where the strongest block-only recursion fails to reach `Y_n` within `M_n` layers;
2. every later return to success, if any, over the tested range;
3. the best block parameter `k_t` at each layer;
4. the ratio `(E_{M_n}+W_n)/Y_n`;
5. exact resource limits.

A block-only failure is not a failure of the full connected-core recursion.

### N1-COL-001

Independently generate the carry-collision profiles based on

\[
3\cdot2^e=2^e+2^{e+1}.
\]

For disjoint layer pairs, verify that `2^L` distinct legal profiles have the common sum

\[
4^L-1.
\]

Test corrupted fixtures that:

- reuse one layer twice;
- replace an odd core by an even core;
- exceed the layer cutoff;
- claim an incorrect common sum;
- merge duplicate profiles;
- use core `3` when `9` does not divide `n!`.

## Exact source files

- `proofs/FACTORIAL_BLOCK_CARRIER_OBSTRUCTION.md`
- `proofs/RAINBOW_CARRY_COLLISIONS.md`
- `verification/block_collision_sanity.py`
- `verification/BLOCK_COLLISION_FINITE_REPORT.md`

Nova 4 must import the exact Nova 1 commit containing this handoff, not only the moving branch name.

## Required output

Return:

- exact imported branch and commit SHA;
- independent verifier paths;
- exact tested ranges;
- first block-only failure;
- collision multiplicity checks;
- corrupted-fixture results;
- separate verdicts for `N1-STR-021`, `N1-DIS-006`, and `N1-COL-001`.

## Claim boundary

The requested computation audits a restricted sequential proof engine and an explicit collision family. It cannot prove or disprove the full marker-three quotient occupancy theorem.