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

`N2-FIN-202` materialized the complete odd-core list for every `12<=n<=45` and proved that the N2-ADD-120 carrier recursion reaches the complete quotient endpoint in every case.

At `n=46`, the complete odd-core family has

\[
27{,}941{,}760
\]

members, above the former materialization cap of `20,000,000`. The prior status was therefore `unknown due to resource limits`, not failure.

## Odd-core factorization

Write

\[
\frac{46!}{2^{v_2(46!)}3}
=
\prod_{i=1}^{13}p_i^{a_i}.
\]

The odd cores are exactly the divisors

\[
u=\prod_{i=1}^{13}p_i^{e_i},
\qquad
0\le e_i\le a_i.
\]

For `n=46`, the exponent bounds are

\[
3^{20}5^{10}7^6 11^4 13^3 17^2 19^2 23^2 29\,31\,37\,41\,43.
\]

Their profile count is

\[
21\cdot11\cdot7\cdot5\cdot4\cdot3^4\cdot2^5
=27{,}941{,}760.
\]

## N2-ADD-121: unique-parent streaming divisor theorem

### Statement

Let

\[
\mathcal E=\prod_{i=1}^s\{0,1,\ldots,a_i\}
\]

and associate to an exponent vector `e` the numerical divisor

\[
V(e)=\prod_{i=1}^s p_i^{e_i}.
\]

For every nonzero vector `e`, let

\[
j(e)=\max\{i:e_i>0\}
\]

and define its parent by

\[
P(e)=e-\mathbf e_{j(e)}.
\]

Start from the zero vector. From a vector `e`, generate the child

\[
e+\mathbf e_k
\]

for every `k>=j(e)` whose exponent remains within its bound; at the root all indices are allowed. Order the active frontier by numerical value `V(e)`.

Then:

1. every exponent vector is generated exactly once;
2. removing the least frontier value emits the divisors in increasing numerical order;
3. stopping when the least frontier value exceeds a cutoff `B` emits exactly the odd cores at most `B`;
4. the algorithm need not store the completed prefix or the complete divisor family.

### Proof

Every nonzero vector has the displayed parent because its largest nonzero coordinate is unique. Conversely, let `e` be a generated vector whose largest nonzero coordinate is `j`. Its parent has no nonzero coordinate larger than `j`, so the child rule at that parent permits incrementing coordinate `j`.

No other parent can generate `e`. Any parent differs from `e` by decrementing one positive coordinate. If that coordinate is smaller than `j`, then the proposed parent still has a nonzero coordinate `j` larger than the incremented coordinate, violating the child condition. If it is larger than `j`, it was not positive in `e`. Thus the parent is unique.

Induction from the root proves that every vector is generated exactly once. Because the active frontier is a minimum priority queue keyed by the exact integer value `V(e)`, each removal emits the least not-yet-emitted divisor. Hence the emitted sequence is strictly increasing and complete. The cutoff conclusion follows immediately. `QED`

## Record-gap compression

Let

\[
1=d_1<d_2<\cdots
\]

be the streamed divisors, with `d_0=0`. A record gap is stored only when

\[
d_i-d_{i-1}
>
\max_{j<i}(d_j-d_{j-1}).
\]

For a carrier threshold `D`, the first consecutive gap exceeding `D`, if it occurs before a layer bound `B`, is exactly the first record gap whose size exceeds `D` and whose right endpoint is at most `B`.

Indeed, before the running maximum first exceeds `D`, every gap is at most `D`. The gap that first exceeds `D` is necessarily a new record. Therefore the full streamed list is not needed after the scan. Prefix counts, the last value at each requested layer bound, and record gaps suffice to replay every N2-ADD-120 connected component exactly.

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

so the complete binary correction palette and the first `43` valuation addresses are legal.

The exact endpoints are

\[
X_{46}
=
74{,}179{,}661{,}362{,}209{,}580{,}727{,}623{,}742{,}159,
\]

\[
Y_{46}
=
\left\lfloor\frac{X_{46}}3\right\rfloor
=
24{,}726{,}553{,}787{,}403{,}193{,}575{,}874{,}580{,}719,
\]

and

\[
W_{46}
=
\left\lfloor\frac{2^{16}-3}{3}\right\rfloor
=21{,}844.
\]

## Stream certificate

The bounded-memory stream emitted every odd core at most `Y_46`:

- total complete odd-core count: `27,941,760`;
- cores emitted through `Y_46`: `24,567,748`;
- final emitted core:
  `24,726,431,646,655,352,806,770,703,125`;
- record gaps retained: `631`;
- maximum active frontier: `3,373,952` nodes.

The maximum frontier is substantially smaller than both the complete family and the emitted prefix. No completed divisor prefix was retained.

## Exact carrier rows

### Layer 1

\[
D_1=21{,}845.
\]

The first blocking gap is

\[
49{,}809{,}375-49{,}786{,}217=23{,}158>D_1.
\]

Thus

\[
u_1^*=49{,}786{,}217,
\qquad
E_1=49{,}786{,}217.
\]

### Layer 2

\[
D_2=24{,}904{,}031,
\]

with first blocking gap

\[
377{,}656{,}336{,}629-377{,}630{,}859{,}375
=25{,}477{,}254.
\]

Hence

\[
E_2=755{,}311{,}504{,}967.
\]

### Layer 3

\[
D_3=188{,}827{,}881{,}703,
\]

and the first blocking gap is

\[
190{,}497{,}757{,}554.
\]

This gives

\[
E_3=37{,}309{,}185{,}719{,}037{,}251.
\]

### Layer 4

\[
D_4=4{,}663{,}648{,}214{,}882{,}387,
\]

and the first blocking gap is

\[
5{,}001{,}199{,}885{,}158{,}750.
\]

Thus

\[
E_4=2{,}633{,}496{,}099{,}664{,}749{,}642{,}251.
\]

### Layer 5

\[
D_5=164{,}593{,}506{,}229{,}046{,}854{,}006,
\]

and the first blocking gap is

\[
169{,}035{,}290{,}362{,}295{,}496{,}216.
\]

Thus

\[
E_5
=
212{,}006{,}162{,}438{,}551{,}948{,}552{,}952{,}795.
\]

### Layer 6

The threshold is

\[
D_6
=
6{,}625{,}192{,}576{,}204{,}748{,}392{,}280{,}457.
\]

No blocking gap occurs before the layer-six core bound. Therefore the connected component reaches the largest streamed core at that bound:

\[
u_6^*
=
772{,}704{,}513{,}124{,}322{,}817{,}339{,}217{,}917.
\]

The final carrier endpoint is

\[
E_6
=
24{,}938{,}550{,}582{,}416{,}882{,}103{,}407{,}926{,}139.
\]

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

The full-menu marker-three quotient windows are occupied for every quotient target through `Y_46`. Consequently every original target through `X_46` has a representation by distinct divisors of `46!` using at most

\[
6+r_{46}=22
\]

terms.

Equivalently,

\[
H_{46!}(\lfloor\sqrt{46!}\rfloor+1)
\le22.
\]

This conclusion follows from the exact N2-ADD-119 carrier blocks and Nova 1's marker-three correction reduction. It is an exact finite theorem.

## Compatibility replay

The same streaming program was run at `n=45`. It reproduced the N2-FIN-202 values:

\[
E_6
=
3{,}737{,}710{,}017{,}095{,}625{,}573{,}621{,}483{,}239,
\]

\[
E_6+W_{45}
=
3{,}737{,}710{,}017{,}095{,}625{,}573{,}621{,}505{,}083,
\]

with term bound `22`. This is an independent compatibility check between the materialized and streaming implementations.

## Reproducibility

Compile and run:

```text
g++ -O3 -std=c++20 \
  tracks/nova2-additive-occupancy/verification/marker_three_streaming_audit.cpp \
  -o marker_three_streaming_audit

./marker_three_streaming_audit --n 46 \
  > tracks/nova2-additive-occupancy/verification/data/marker_three_streaming_n46.json

python3 tracks/nova2-additive-occupancy/verification/test_marker_three_streaming_audit.py
```

Frozen certificate:

`verification/data/marker_three_streaming_n46.json`

## Next exact boundary

The smallest unaudited parameter is now `n=47`. A bounded run at `n=47` did not complete within the available execution limit and is classified as `unknown due to resource limits`, not failure.

The next computational improvement should reduce the active frontier, use an external-memory frontier, or replace enumeration with a theorem controlling record gaps of odd factorial divisors.

## Claim boundary

This file does not prove marker-three occupancy uniformly in `n`. It does not establish success at `n=47`. It does not remove the Phase 12P audit required before using the sequential carrier engine asymptotically. It does not solve Erdős Problem 18.
