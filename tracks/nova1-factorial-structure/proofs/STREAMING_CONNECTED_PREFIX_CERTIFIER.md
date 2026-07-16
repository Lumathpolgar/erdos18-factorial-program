# Streaming Connected-Prefix Certifier

## Result ID

- `N1-STR-022`: proved theorem

## Imported precursor

Nova 2 proved the unique-parent streaming divisor theorem as `N2-ADD-121` at:

- branch: `nova/additive-occupancy`
- exact commit: `e443674f86b2ee3c7037ac94ee47f6b8a4b3b29f`
- proof: `tracks/nova2-additive-occupancy/proofs/MARKER_THREE_STREAMING_N46_AUDIT.md`

The argument below independently reconstructs the theorem in the Nova 1 notation and extends the stored record to include the exact connected-prefix cardinality required by `N1-OBS-003`.

## Bounded exponent box

Let

\[
D=\prod_{i=1}^s p_i^{a_i}
\]

with distinct increasing primes `p_i` and nonnegative exponents `a_i`. Associate to

\[
e=(e_1,\ldots,e_s),\qquad 0\le e_i\le a_i,
\]

the divisor

\[
V(e)=\prod_{i=1}^s p_i^{e_i}.
\]

For a nonzero exponent vector define

\[
j(e)=\max\{i:e_i>0\}
\]

and

\[
P(e)=e-\mathbf e_{j(e)}.
\]

At the zero vector every coordinate may be incremented. At a nonzero vector `e`, generate a child `e+e_k` only when

\[
k\ge j(e)
\]

and the exponent bound remains legal.

## Unique-parent theorem

Every legal nonzero exponent vector is generated from exactly one parent.

### Proof

Let `e` be nonzero and put `j=j(e)`. The vector

\[
P(e)=e-\mathbf e_j
\]

is legal. Its largest nonzero coordinate is at most `j`, so its child rule permits incrementing coordinate `j`. Hence `P(e)` generates `e`.

Suppose another parent generated `e` by incrementing coordinate `k`.

If `k<j`, then the parent still has the nonzero coordinate `j`, so its largest nonzero coordinate exceeds `k`. The child rule forbids that increment.

If `k>j`, then `e_k=0`, so no legal parent can be obtained by decrementing coordinate `k`.

Therefore `k=j`, and the parent is exactly `P(e)`. `QED`

## Increasing stream theorem

Insert the zero vector into a minimum priority queue keyed by the exact integer value `V(e)`. Whenever a vector is removed, insert all of its legal children under the unique-parent rule.

Then:

1. every divisor of `D` is inserted exactly once;
2. every removal emits the least remaining divisor;
3. the emitted values are strictly increasing;
4. stopping when the least active value exceeds `B` emits exactly the divisors of `D` not exceeding `B`.

### Proof

The unique-parent theorem gives complete generation without duplicate exponent vectors. Unique factorization gives distinct numerical divisor values. A minimum priority queue therefore removes the least un-emitted divisor at every step. The cutoff conclusion follows immediately. `QED`

## Record-gap compression

Write the emitted divisors as

\[
0=d_0<d_1<d_2<\cdots.
\]

Store a gap only when

\[
d_i-d_{i-1}>
\max_{1\le j<i}(d_j-d_{j-1}).
\]

For each stored record retain:

- the gap;
- the left endpoint `d_(i-1)`;
- the right endpoint `d_i`;
- the number `i-1` of positive divisors at most the left endpoint.

Fix a core cutoff `B` and an additive threshold `T`.

The first consecutive divisor gap exceeding `T`, if one occurs with right endpoint at most `B`, is necessarily a record gap. Otherwise an earlier gap would already be larger and would also exceed `T`.

Consequently the zero-connected divisor prefix under threshold `T` is recovered exactly as follows.

- If a first stored record gap greater than `T` has right endpoint at most `B`, the connected maximum is its left endpoint and the connected-prefix cardinality is its stored left count.
- Otherwise the connected maximum is the last emitted divisor at most `B`, and the connected-prefix cardinality is the total emitted count through `B`.

Thus record gaps, their left counts, and cutoff checkpoints exactly recover both

\[
u_t^*
\]

and

\[
K_t
\]

for every layer of the Nova 2 connected-core recursion.

## Application to the marker-three core

For

\[
D_n=\frac{n!}{3\cdot2^{v_2(n!)}},
\]

the odd quotient cores are exactly the divisors of `D_n`.

At layer `t`, use

\[
B_t=\left\lfloor\frac{Y_n}{2^{t-1}}\right\rfloor
\]

and

\[
T_t=\left\lfloor
\frac{E_{t-1}+W_n+1}{2^{t-1}}
\right\rfloor.
\]

The record-gap rule returns the exact complete connected maximum and its exact cardinality. Updating

\[
E_t=E_{t-1}+2^{t-1}u_t^*
\]

therefore reproduces the `N2-ADD-120` carrier recursion without materializing the complete divisor list.

## Complexity statement

If `N(B)` divisors are emitted through the maximum cutoff, `F` is the largest active priority-queue frontier, `R` is the number of record gaps, and `L` is the number of requested layer cutoffs, then the certifier uses:

\[
O(N(B)\log F)
\]

time and

\[
O(F+R+L)
\]

stored records.

This is an exact algorithmic theorem. It is not an asymptotic connected-prefix lower bound and does not prove quotient occupancy for all sufficiently large `n`.