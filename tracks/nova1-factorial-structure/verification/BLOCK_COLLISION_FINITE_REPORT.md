# Block and Collision Finite Report

## Evidence label

**finite certificate** for the exact tested ranges.

The asymptotic theorems are proved symbolically in:

- `proofs/FACTORIAL_BLOCK_CARRIER_OBSTRUCTION.md`
- `proofs/RAINBOW_CARRY_COLLISIONS.md`

The finite verifier is not the source of the asymptotic conclusions.

## Command

```text
python tracks/nova1-factorial-structure/verification/block_collision_sanity.py
```

## Environment

- Python 3
- standard library only
- deterministic
- exact integer arithmetic for factorial, divisibility, blocks, profiles, and sums
- floating-point logarithms used only for the recorded coarse scale-separation check at `n=120368`

## Exact tested ranges

### Factorial arithmetic blocks

For every integer

\[
6\le n\le20
\]

and every

\[
3\le k<n,
\]

the verifier checks every odd

\[
1\le j\le m_{n,k}
\]

and confirms

\[
3A_kj\mid n!.
\]

### Block carrier ceiling

For every

\[
12\le n\le50
\]

and the first at most `30` frozen layers, the verifier constructs the strongest available single factorial block under the exact carrier threshold and checks

\[
E_t+W_n+1
\le
\left(1+\frac n2\right)(E_{t-1}+W_n+1)
\]

at every step.

### Carry collisions

For every

\[
1\le K\le8,
\]

the verifier enumerates all `2^K` carry choices across `K` disjoint layer pairs and confirms:

- every profile is distinct;
- every profile uses at most one term per layer;
- every selected core is odd;
- every profile has the same numerical sum;
- the common sum is exactly
  \[
  4^K-1.
  \]

### Scale separation

At the imported explicit threshold

\[
n=120368,
\]

the verifier checks the coarse logarithmic inequality used to separate the block-carrier ceiling from the factorial endpoint.

## Recorded output

```text
PASS test_factorial_blocks
PASS test_block_connectivity_and_ceiling
PASS test_exponential_carry_collisions
PASS test_asymptotic_scale_separation
PASS all 4 block-and-collision checks
```

## Interpretation

The checks support four exact implementation claims.

1. The factorial blocks are legal submenus.
2. Their carrier recurrence obeys the proved one-step ceiling.
3. Exponentially many valid profiles can collide at one numerical sum.
4. The asymptotic scale comparison is already separated by a large margin at `n=120368`.

## Claim boundary

The finite report does not prove that the complete connected core fails.

It does not estimate typical collision multiplicity.

It does not prove or disprove the full marker-three quotient-window theorem.