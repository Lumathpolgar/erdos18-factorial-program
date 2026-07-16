# Collision and Block-Carrier Checkpoint

## Checkpoint status

The factorial half-range theorem remains open.

This checkpoint closes two narrower questions:

1. whether explicit factorial arithmetic blocks can supply a complete carrier proof;
2. whether formal marker-three profiles are numerically injective.

Both questions now have exact negative answers in their stated forms.

## Cross-track intake

Nova 2 accepted the marker-three construction with restrictions from:

- branch: `nova/additive-occupancy`
- exact commit: `b15278e21f91e0e188b1c7c3e9a10e58a1db20fe`
- response: `handoffs/RESPONSE_TO_NOVA1_MARKER_THREE.md`
- carrier proof: `proofs/MARKER_THREE_CARRIER_BLOCK_REDUCTION.md`
- outcome: `ACCEPTED_WITH_RESTRICTIONS`

Nova 2 proved that connected core chains under the exact layer thresholds are sufficient for the quotient-window theorem, while warning that this is a sequential sufficient engine and not the full final-only model.

## New result N1-STR-021

For every `n>=6` and `3<=k<n`, define

\[
A_k=\frac{k!}{3\cdot2^{v_2(k!)}},
\]

and let `m_{n,k}` be the largest odd integer at most `n-k`.

Then every core

\[
A_k,\ 3A_k,\ldots,m_{n,k}A_k
\]

is legal for the marker-three construction before the layer cutoff is applied.

When the carrier threshold is at least `2A_k`, this entire arithmetic block is connected from zero.

## New disproved route N1-DIS-006

Any carrier proof using only one such factorial arithmetic block per layer satisfies

\[
E_{M_n}+W_n+1
\le
(W_n+1)\left(1+\frac n2\right)^{M_n}.
\]

For every `n>=120368`, this is strictly below

\[
Y_n=\left\lfloor\frac{\lfloor\sqrt{n!}\rfloor}{3}\right\rfloor.
\]

Therefore the one-block-per-layer carrier route cannot prove the frozen quotient theorem.

The ceiling is only

\[
\exp(O((\log n)^3)),
\]

while the target is

\[
\exp(\Theta(n\log n)).
\]

This does not reject the complete connected core or the final-only model.

## New result N1-COL-001

The exact carry identity

\[
3\cdot2^e=2^e+2^{e+1}
\]

produces independent collisions on disjoint pairs of layers.

For every `n>=120368`, at least

\[
2^{\lfloor M_n/2\rfloor}
\]

distinct legal profiles map to the same quotient sum

\[
4^{\lfloor M_n/2\rfloor}-1.
\]

Thus profile injectivity is false, and maximum collision multiplicity is at least

\[
\exp(\Omega((\log n)^2)).
\]

The collision loss remains much smaller than the known formal menu entropy, so this is not a capacity obstruction by itself.

## Verification

Run:

```text
python tracks/nova1-factorial-structure/verification/block_collision_sanity.py
```

Recorded output:

```text
PASS test_factorial_blocks
PASS test_block_connectivity_and_ceiling
PASS test_exponential_carry_collisions
PASS test_asymptotic_scale_separation
PASS all 4 block-and-collision checks
```

## Exact consequences

Closed:

- explicit legal large-core arithmetic blocks;
- exact carrier growth ceiling for the one-block-per-layer engine;
- profile injectivity;
- an explicit exponential lower bound for maximum collision multiplicity.

Still open:

- whether the complete core menu has connected components far larger than every single arithmetic block;
- whether multiple blocks can interact inside one layer to escape the ceiling;
- target-local collision energy;
- final-only quotient-window occupancy;
- the downward endpoint window;
- finite exceptions.

## Next theorem target

The next useful structural theorem must do one of the following:

1. prove a superpolynomial connected-core expansion using multiple interacting core blocks;
2. prove an upper bound showing that the full carrier recursion also remains below `Y_n`;
3. control target-local collision energy strongly enough to support the final-only numerical law.

The first priority is now the complete connected-core expansion, not another one-block carrier variant.