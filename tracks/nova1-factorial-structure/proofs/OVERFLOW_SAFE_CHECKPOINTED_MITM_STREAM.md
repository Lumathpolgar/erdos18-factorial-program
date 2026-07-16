# Overflow-Safe Checkpointed Meet-in-the-Middle Stream

## Results

- `N1-STR-027`: **proved theorem**.
- `N1-DIS-007`: **disproved route**.

The factorial half-range theorem and Erdos Problem 18 remain open.

## Setup

Let the odd prime-power coordinates of

\[
D_n=\frac{n!}{3\cdot 2^{v_2(n!)}}
\]

be partitioned into two disjoint coordinate families. Let `A` and `B` be their half-divisor sets. Every divisor of `D_n` has a unique factorization `ab` with `a in A` and `b in B`.

The carrier verifier needs only products

\[
ab\le Y_n=\left\lfloor\frac{\lfloor\sqrt{n!}\rfloor}{3}\right\rfloor.
\]

## N1-STR-027: safe truncation theorem

Because every half divisor is a positive integer, any half divisor larger than `Y_n` cannot occur in a product `ab<=Y_n`. Therefore replacing `A` and `B` by

\[
A_{\le Y}=A\cap[1,Y_n],\qquad B_{\le Y}=B\cap[1,Y_n]
\]

preserves exactly the set and sorted order of all products `ab<=Y_n`.

During recursive half-list generation, the multiplication `x p` is performed only when

\[
x\le \left\lfloor\frac{Y_n}{p}\right\rfloor.
\]

During row advancement, `ab` is formed only when

\[
a\le \left\lfloor\frac{Y_n}{b}\right\rfloor.
\]

These division guards prove that every stored and merged product fits unsigned 128-bit arithmetic whenever `Y_n` does. No wrapped value can enter the stream.

## Exact checkpoint theorem

After an accepted product has been consumed, the future merge stream is determined by:

- the resolved carrier endpoint `E`;
- the previous product;
- the global emitted count;
- the active layer;
- the exact connected-prefix product;
- all already resolved layer rows;
- each active row and its current column index.

Serializing these fields and rebuilding the heap from the active row-column pairs recovers the identical next product and all later products. Deterministic checkpointing therefore preserves the exact stream, connected-prefix counts, blocking gaps, carrier endpoints, and final certificate.

## N1-DIS-007: unguarded u128 half-list route

The former verifier generated unrestricted half divisors and multiplied them in unsigned 128-bit arithmetic before checking the endpoint cutoff. At `n=57`, two exact coordinate partitions produced different connected-prefix counts:

| mask | `K_6` | `K_7` |
|---:|---:|---:|
| 6 | 543,303,167 | 565,913,312 |
| 424 | 543,303,171 | 565,913,374 |

A partition-independent divisor stream cannot have different counts. This rejects unrestricted unsigned-128 half-list multiplication as an exact verification route.

With overflow-safe truncation and division guards, both masks give

\[
K_6=543{,}303{,}166,
\qquad
K_7=565{,}913{,}305,
\]

and agree on every mathematical output field.

## Regression boundary

Overflow-safe replays at `n=52,53,54,55,56` reproduce every previously accepted mathematical field. Thus the prior finite conclusions remain valid, while their authoritative replay method is replaced by the overflow-safe checkpointed verifier.

`QED`
