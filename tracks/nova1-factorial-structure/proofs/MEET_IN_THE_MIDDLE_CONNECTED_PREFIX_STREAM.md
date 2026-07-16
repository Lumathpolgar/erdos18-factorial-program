# Meet-in-the-Middle Connected-Prefix Stream

## Result ID

- `N1-STR-023`: **proved theorem**

## Scope

This theorem gives an exact low-memory enumeration and carrier-certification method for the marker-three odd cores. It is an algorithmic theorem. It does not prove asymptotic connected-prefix growth.

## Odd-core factorization

Let

\[
D_n=\frac{n!}{3\cdot2^{v_2(n!)}}.
\]

Write

\[
D_n=\prod_{i=1}^s p_i^{a_i}
\]

with all `p_i` odd. Partition the prime-power coordinates into two disjoint sets `I` and `J`. Define

\[
\mathcal A=\left\{\prod_{i\in I}p_i^{e_i}:0\le e_i\le a_i\right\},
\qquad
\mathcal B=\left\{\prod_{j\in J}p_j^{e_j}:0\le e_j\le a_j\right\}.
\]

Every divisor of `D_n` has a unique factorization

\[
d=ab,
\qquad a\in\mathcal A,\quad b\in\mathcal B.
\]

The uniqueness follows because the prime supports of `a` and `b` are disjoint.

## Theorem

Suppose

\[
1=a_1<a_2<\cdots<a_R
\]

and

\[
1=b_1<b_2<\cdots<b_C
\]

are the sorted half-divisor lists. For every row index `r`, the sequence

\[
a_r b_1<a_r b_2<\cdots<a_r b_C
\]

is strictly increasing. Initialize a minimum heap with the first term of every row. Whenever `a_r b_c` is removed, insert `a_r b_{c+1}` when it exists and remains below the declared cutoff.

Then:

1. every divisor of `D_n` below the cutoff is emitted;
2. every such divisor is emitted exactly once;
3. the emitted order is strictly increasing;
4. the active heap contains at most `min(R,C)` nodes after the smaller half is selected as the row family;
5. scanning the consecutive gaps in this exact order recovers every connected maximum `u_t^*` and connected-prefix cardinality `K_t` under the Nova 2 carrier threshold;
6. a gap that first exceeds the current threshold resolves the current layer at its left endpoint;
7. the same right endpoint is re-evaluated under the next threshold, so no gap is skipped during a layer transition;
8. reaching a layer cutoff before a blocking gap certifies that the complete menu through that cutoff is connected.

## Proof

The coordinate partition gives a bijection between bounded exponent vectors and pairs `(a,b)` in `A x B`. Therefore the product rows contain every divisor exactly once.

Each row is sorted because multiplication by a positive fixed integer preserves strict order. The standard k-way minimum-heap merge emits the least not-yet-emitted element among all rows. Induction on the number of heap removals proves globally increasing exact enumeration.

For a carrier layer, the zero-connected component consists exactly of the initial divisor segment before the first consecutive gap greater than the threshold. If the first excessive gap is `(d_i,d_{i+1})`, then

\[
u_t^*=d_i,
\qquad
K_t=i.
\]

If no excessive gap occurs before the layer cutoff, then the connected maximum and count are the last emitted divisor and the number emitted through that cutoff. The carrier endpoint update is then exactly

\[
E_t=E_{t-1}+2^{t-1}u_t^*.
\]

After a blocking gap resolves one layer, its right endpoint has not yet entered the connected prefix. Re-evaluating that same gap under the next threshold preserves exactness. This proves all clauses. `QED`

## Complexity

If the coordinate partition is balanced, then

\[
R\asymp C\asymp\sqrt{\tau(D_n)}.
\]

The memory used by the merge heap is

\[
O(\min(R,C)),
\]

rather than proportional to the unique-parent stream frontier or the full divisor family. The running time through `N` emitted divisors is

\[
O(N\log\min(R,C)).
\]

## Exact implementation

- verifier: `verification/marker_three_mitm_prefix_u128.cpp`
- implementation commit: `72bcf1d6142f06be3fc704cc5313d17f5281884b`

The implementation fails closed on:

- uncertified logarithmic parameters;
- unsigned 128-bit endpoint overflow;
- half-list count mismatch;
- duplicate half divisors;
- a non-increasing merged stream;
- a blocked-layer transition after the next cutoff has already passed;
- a no-block layer that does not finish the certificate.

## Claim boundary

`N1-STR-023` proves exact enumeration and exact recovery of finite connected prefixes. It does not prove that the connected-prefix cardinalities meet `N1-OBS-003` uniformly in `n`.
