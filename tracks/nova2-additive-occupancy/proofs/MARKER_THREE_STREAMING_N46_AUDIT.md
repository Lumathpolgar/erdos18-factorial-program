# Marker-Three Streaming Audit at n=46

## Result IDs

- `N2-ADD-121`: proved algorithmic theorem
- `N2-FIN-203`: finite certificate

## Frozen structural source

- repository: `Lumathpolgar/erdos18-factorial-program`
- Nova 1 branch: `nova/factorial-structure`
- Nova 1 commit: `ebb47ba436af554366d0f285119a769f31f9e561`
- construction: `N1-CON-003`
- Nova 2 carrier theorems: `N2-ADD-119` and `N2-ADD-120`

The factorial formulation of Erdős Problem 18 remains open. This file proves a finite exact result and an exact enumeration lemma. It does not prove uniform asymptotic occupancy.

## Previous exact boundary

`N2-FIN-202` materialized the complete odd-core list for every `12<=n<=45` and proved that the N2-ADD-120 recursion reaches the complete quotient endpoint in every case.

At `n=46`, the complete odd-core family has `27,941,760` members, above the former materialization cap of `20,000,000`. The prior status was therefore `unknown due to resource limits`, not failure.

## Odd-core factorization

The odd cores are exactly the divisors of

\[
\frac{46!}{2^{v_2(46!)}3}.
\]

Their prime-exponent bounds are

\[
3^{20}5^{10}7^6 11^4 13^3 17^2 19^2 23^2 29\,31\,37\,41\,43.
\]

Thus the exact profile count is

\[
21\cdot11\cdot7\cdot5\cdot4\cdot3^3\cdot2^5
=27{,}941{,}760.
\]

Only the three primes `17`, `19`, and `23` contribute a factor `3` to this product.

## N2-ADD-121: unique-parent streaming divisor theorem

Let

\[
\mathcal E=\prod_{i=1}^s\{0,1,\ldots,a_i\}
\]

and associate to an exponent vector `e` the divisor

\[
V(e)=\prod_{i=1}^s p_i^{e_i}.
\]

For a nonzero vector define

\[
j(e)=\max\{i:e_i>0\},
\qquad
P(e)=e-\mathbf e_{j(e)}.
\]

Start from the zero vector. From `e`, generate `e+e_k` for every `k>=j(e)` whose exponent remains legal; at the root every coordinate is allowed. Keep generated vectors in a minimum priority queue keyed by the exact integer `V(e)`.

### Theorem

1. Every bounded exponent vector is generated exactly once.
2. Priority-queue removal emits the divisors in strictly increasing order.
3. Stopping when the least active value exceeds `B` emits exactly the odd cores at most `B`.
4. The completed prefix and complete divisor family need not be stored.

### Proof

Every nonzero vector has the displayed parent because its largest nonzero coordinate is unique. Its parent has no nonzero coordinate above `j(e)`, so the child rule permits incrementing coordinate `j(e)`.

No different parent can produce `e`. Decrementing a coordinate below `j(e)` leaves the larger nonzero coordinate in place and violates the rule that the incremented coordinate be at least the parent's largest nonzero coordinate. A coordinate above `j(e)` is zero and cannot be decremented. Thus the parent is unique.

Induction from the root proves complete generation without duplication. Unique factorization makes numerical values distinct. The minimum priority queue therefore emits the remaining least divisor at every step. The cutoff statement follows. `QED`

## Record-gap compression

Let

\[
1=d_1<d_2<\cdots,
\qquad d_0=0.
\]

Store a gap only when

\[
d_i-d_{i-1}
>
\max_{j<i}(d_j-d_{j-1}).
\]

For a carrier threshold `D`, the first consecutive gap exceeding `D` is necessarily a new record. Therefore, for every layer bound `B`, the connected component from zero is recovered exactly from:

- the first stored record gap larger than `D` whose right endpoint is at most `B`; or
- the final divisor at most `B` when no such record exists.

Prefix counts, last values at requested bounds, and record gaps therefore suffice to replay N2-ADD-120 exactly.

## Exact parameters at n=46

Rational logarithm bounds certify

\[
r_{46}=16,
\qquad
M_{46}=235.
\]

Also,

\[
v_2(46!)=42,
\]

so the complete correction palette and the first `43` valuation addresses are legal.

The exact endpoints are

\[
X_{46}
=
74{,}179{,}661{,}362{,}209{,}580{,}727{,}623{,}742{,}159,
\]

\[
Y_{46}
=
24{,}726{,}553{,}787{,}403{,}193{,}575{,}874{,}580{,}719,
\]

and

\[
W_{46}=21{,}844.
\]

## Stream certificate

The bounded-memory stream emitted every odd core at most `Y_46`:

- complete odd-core count: `27,941,760`;
- cores emitted through `Y_46`: `24,567,748`;
- last emitted core:
  `24,726,431,646,655,352,806,770,703,125`;
- record gaps retained: `631`;
- maximum active frontier: `3,373,952` nodes.

No completed divisor prefix was retained.

## Exact carrier recursion

The six used layers are frozen in

`verification/data/marker_three_streaming_n46.json`.

Their thresholds and connected endpoints are:

| layer | threshold `D_t` | connected maximum core | carrier endpoint `E_t` |
|---:|---:|---:|---:|
| 1 | 21,845 | 49,786,217 | 49,786,217 |
| 2 | 24,904,031 | 377,630,859,375 | 755,311,504,967 |
| 3 | 188,827,881,703 | 9,327,107,601,883,071 | 37,309,185,719,037,251 |
| 4 | 4,663,648,214,882,387 | 329,182,348,809,878,825,625 | 2,633,496,099,664,749,642,251 |
| 5 | 164,593,506,229,046,854,006 | 13,250,220,558,903,267,737,706,909 | 212,006,162,438,551,948,552,952,795 |
| 6 | 6,625,192,576,204,748,392,280,457 | 772,704,513,124,322,817,339,217,917 | 24,938,550,582,416,882,103,407,926,139 |

The first five layers stop at exact record gaps exceeding their thresholds. No blocking gap occurs before the sixth-layer bound.

Adding the correction width gives

\[
E_6+W_{46}
=
24{,}938{,}550{,}582{,}416{,}882{,}103{,}407{,}947{,}983.
\]

This exceeds `Y_46` by

\[
211{,}996{,}795{,}013{,}688{,}527{,}533{,}367{,}264.
\]

## N2-FIN-203

Every marker-three quotient window through `Y_46` is occupied. Nova 1's exact correction reduction therefore gives

\[
H_{46!}(\lfloor\sqrt{46!}\rfloor+1)
\le6+r_{46}=22.
\]

This is an exact finite theorem.

## Compatibility replay

The streaming program also reproduced the N2-FIN-202 `n=45` values:

\[
E_6
=
3{,}737{,}710{,}017{,}095{,}625{,}573{,}621{,}483{,}239,
\]

\[
E_6+W_{45}
=
3{,}737{,}710{,}017{,}095{,}625{,}573{,}621{,}505{,}083.
\]

This independently checks compatibility between the materialized and streaming implementations.

## Reproducibility

```text
g++ -O3 -std=c++20 \
  tracks/nova2-additive-occupancy/verification/marker_three_streaming_audit.cpp \
  -o marker_three_streaming_audit

./marker_three_streaming_audit --n 46 \
  > tracks/nova2-additive-occupancy/verification/data/marker_three_streaming_n46.json

python3 tracks/nova2-additive-occupancy/verification/test_marker_three_streaming_audit.py
```

## Next exact boundary

The smallest unaudited parameter is `n=47`. A bounded run did not complete within the available execution limit. Its status is `unknown due to resource limits`, not failure.

The next computational improvement should reduce the active frontier, use an external-memory frontier, or replace enumeration with a theorem controlling record gaps of odd factorial divisors.

## Claim boundary

This file does not prove uniform marker-three occupancy, establish success at `n=47`, remove the Phase 12P audit, or solve Erdős Problem 18.
