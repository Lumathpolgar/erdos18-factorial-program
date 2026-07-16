# Nova 1 Block-Carrier and Collision Handoff to Nova 2

Handoff ID: `N1-HO-N2-003`

Sending track: Nova 1, Factorial Structure and Reduction

Receiving track: Nova 2, Additive Occupancy and Global Sumsets

Date: 2026-07-15

Result status: proved theorems and disproved restricted proof engine

## Imported Nova 2 baseline

Nova 1 imports the marker-three intake and carrier criterion from:

- branch: `nova/additive-occupancy`
- exact commit: `b15278e21f91e0e188b1c7c3e9a10e58a1db20fe`
- response: `tracks/nova2-additive-occupancy/handoffs/RESPONSE_TO_NOVA1_MARKER_THREE.md`
- proof: `tracks/nova2-additive-occupancy/proofs/MARKER_THREE_CARRIER_BLOCK_REDUCTION.md`
- outcome: `ACCEPTED_WITH_RESTRICTIONS`

No later Nova 2 revision is assumed in the proofs below.

## New result N1-STR-021

For

\[
A_k=\frac{k!}{3\cdot2^{v_2(k!)}},
\qquad
m_{n,k}=\max\{m\le n-k:m\text{ odd}\},
\]

every core

\[
A_k,\ 3A_k,\ldots,m_{n,k}A_k
\]

is legal for the marker-three menu before applying the layer cutoff.

If the exact connected-core threshold at layer `t` is at least `2A_k`, the entire block is connected from zero.

Proof:

`tracks/nova1-factorial-structure/proofs/FACTORIAL_BLOCK_CARRIER_OBSTRUCTION.md`

## New disproved route N1-DIS-006

Any carrier recursion that uses only one such arithmetic block per layer satisfies

\[
E_{M_n}+W_n+1
\le
(W_n+1)\left(1+\frac n2\right)^{M_n}.
\]

For every `n>=120368`, this quantity is strictly below

\[
Y_n=\left\lfloor\frac{\lfloor\sqrt{n!}\rfloor}{3}\right\rfloor.
\]

Therefore the one-factorial-block-per-layer version of `N2-ADD-120` cannot prove the full quotient theorem.

This does not disprove the complete connected-core recursion. It proves that a successful connected-core argument must use multiple interacting blocks or a core family whose connected endpoint exceeds `n` times the threshold by a factorial-scale amount.

## New collision theorem N1-COL-001

For every `n>=120368`, the exact carry identity

\[
3\cdot2^e=2^e+2^{e+1}
\]

produces at least

\[
2^{\lfloor M_n/2\rfloor}
\]

distinct legal profiles with the same quotient sum.

Proof:

`tracks/nova1-factorial-structure/proofs/RAINBOW_CARRY_COLLISIONS.md`

Consequences:

1. profile injectivity is false;
2. raw profile capacity cannot be converted into distinct-sum capacity without collision control;
3. the numerical target-dependent law is the correct object for final-only analysis.

## Exact requested next action

Please determine one of the following.

1. Prove a connected-core expansion theorem for the full menus that escapes the one-block ceiling.
2. Prove an upper bound showing that the complete connected-core recursion also remains below `Y_n`.
3. Freeze a target-local collision-energy quantity suitable for the numerical bounded-torus law.

Return an exact theorem, obstruction, or conditional criterion with branch and commit SHA.

## Verification

Run:

```text
python tracks/nova1-factorial-structure/verification/block_collision_sanity.py
```

Recorded result:

```text
PASS all 4 block-and-collision checks
```

## Claim boundary

The full marker-three quotient occupancy theorem remains open. The new obstruction applies only to the one-arithmetic-block-per-layer carrier engine.