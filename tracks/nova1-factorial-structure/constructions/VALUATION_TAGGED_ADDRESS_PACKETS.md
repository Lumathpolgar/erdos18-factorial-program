# Construction N1-CON-001: Valuation-Tagged Address Packets

Result label: **heuristic** as a half-range route.

This revision replaces the disproved fixed-family version with large menus per address. The selected-term count remains `O((log n)^2)`, while the available-choice count can be exponentially larger.

## 1. Formal definition

Fix absolute constants `A,B>0`. For each sufficiently large integer `n`, set

\[
X_n=\lfloor\sqrt{n!}\rfloor,
\qquad
r_n=\lceil B\log n\rceil,
\qquad
M_n=\lceil A(\log n)^2\rceil.
\]

For `1<=t<=M_n`, define the factorial-specific 2-adic address

\[
e_t=r_n+t.
\]

Choose a finite menu `U_t(n)` of odd cores satisfying

\[
u>1,
\qquad
u\mid n!,
\qquad
2^{e_t}u\le X_n
\]

for every `u in U_t(n)`. Define the addressed layer

\[
\mathcal A_t(n)=\{2^{e_t}u:u\in U_t(n)\}.
\]

A main representation chooses either zero terms or exactly one term from each layer. Thus the rainbow sumset is

\[
\Sigma_{\rm rb}(\mathcal A_1,\ldots,\mathcal A_{M_n})
=
\left\{
\sum_{t=1}^{M_n}d_t:
 d_t\in\mathcal A_t(n)\cup\{0\}
\right\}.
\]

The correction palette is

\[
\mathcal C_{r_n}=\{1,2,\ldots,2^{r_n-1}\}.
\]

## 2. Disproved predecessor

Result label: **disproved route**.

The predecessor with only one frozen divisor in each of `M_n=O((log n)^2)` layers had at most `2^{M_n}` main profiles. Even with correction width `exp(O((log n)^2))`, the total number of targets it could cover was `exp(O((log n)^2))`, which is negligible compared with

\[
X_n=\exp(\Theta(n\log n)).
\]

The proof is in `proofs/COUNTING_CAPACITY_OBSTRUCTION.md`.

The surviving route requires large menus `U_t(n)`.

## 3. Factorial-specific multiplicity

Result label: **proved theorem**.

For every fixed `A,B`,

\[
r_n+M_n\le v_2(n!)
\]

for all sufficiently large `n`. Hence every layer can receive a distinct 2-adic address. This `Theta((log n)^2)` address budget is unavailable in `L_n`, where `v_2(L_n)=floor(log_2 n)`.

## 4. Legal divisor proof

Result label: **proved theorem** under the menu hypotheses.

Every layer element is

\[
d=2^{e_t}u
\]

with odd `u|n!` and `e_t<=v_2(n!)`, so `d|n!`. Shared odd prime factors between menu elements do not create a legality problem because selected summands are not multiplied.

Every correction term divides `n!` because `r_n-1<=v_2(n!)`.

## 5. Numerical distinctness proof

Result label: **proved theorem**.

Within one layer, distinct cores give distinct numerical divisors. Across different layers,

\[
v_2(d)=e_t,
\]

so distinct addresses prevent cross-layer equality. Every main term has odd part greater than one, while every correction term is a pure power of two. Therefore every legal rainbow selection combined with the palette uses numerically distinct divisors.

## 6. Selectable term budget

At most one main term is selected from each of `M_n` layers. Therefore the main cost is at most `M_n`, regardless of menu sizes. Including correction gives

\[
M_n+r_n
\le A(\log n)^2+B\log n+2.
\]

There is no recursive multiplier.

## 7. Necessary capacity gate

Result label: **proved theorem**.

The number of formal rainbow profiles is

\[
P_n=\prod_{t=1}^{M_n}(|U_t(n)|+1).
\]

Downward-window coverage with width

\[
R_n=2^{r_n}-1
\]

requires

\[
P_n(R_n+1)\ge X_n+1.
\]

Equivalently,

\[
\sum_{t=1}^{M_n}\log(|U_t(n)|+1)
\ge
\log(X_n+1)-r_n\log2.
\]

Since `log X_n=Theta(n log n)`, the menus must collectively carry `Theta(n log n)` logarithmic profile capacity. This condition is necessary, not sufficient, because different profiles may collide.

## 8. Represented scale

A layer may be divided into core windows

\[
U_t(n;Y,W)=
\left\{
 u\mid n!:u\text{ odd},u>1,
 Y/2^{e_t}\le u\le(Y+W)/2^{e_t}
\right\}.
\]

Every selected core from this menu produces a divisor in `[Y,Y+W]`. The 2-adic address supplies collision control; the odd divisor lattice supplies magnitude and menu entropy.

A viable schedule must combine menus from many logarithmic scales. Large menu cardinality at one scale is insufficient if it leaves shell gaps.

## 9. Collision analysis

- Within a layer: distinct cores give distinct divisors, but only one may be selected.
- Across layers: distinct 2-adic valuations prevent equality.
- With correction terms: impossible because every main term has odd part greater than one.
- Duplicate total sums: possible and potentially severe.
- Hidden dependence: menus can share odd primes and numerical cores; the addresses preserve term distinctness but not sum-map injectivity.
- Capacity versus coverage: the profile inequality is mandatory but never promoted to occupancy.

## 10. Correction mechanism

Result label: **conditional theorem**.

Assume every integer `x` with

\[
2^{r_n}\le x\le X_n
\]

has a rainbow main sum `y` satisfying

\[
x-(2^{r_n}-1)\le y\le x.
\]

Then the binary correction lemma gives

\[
H_{n!}(X_n+1)\le M_n+r_n=O((\log n)^2).
\]

## 11. Exact missing additive theorem

### N1-REQ-N2-001-A

For the exact frozen layer menus `A_t(n)`, prove that for every sufficiently large `n` and every integer

\[
2^{r_n}\le x\le X_n,
\]

there are choices

\[
d_t\in\mathcal A_t(n)\cup\{0\}
\]

such that

\[
x-(2^{r_n}-1)
\le\sum_{t=1}^{M_n}d_t\le x.
\]

The theorem must be uniform in `x`, preserve at most one selected term per layer, and explicitly rule out inaccessible residue classes and additive shell gaps.

## 12. Exact missing analytic theorem

### N1-REQ-N3-001-A

For the frozen list of core windows `I_{t,s}(n)=[L_{t,s}(n),U_{t,s}(n)]`, prove lower bounds

\[
|U_t(n)\cap I_{t,s}(n)|\ge Q_{t,s}(n)
\]

for every stated layer and scale window, where:

1. every counted integer is an odd divisor of `n!` greater than one;
2. every resulting addressed divisor is at most `X_n`;
3. the resulting menu sizes satisfy the necessary capacity inequality;
4. the bounds are uniform in all frozen indices.

No additive conclusion is requested.

## 13. Known historical obstruction audit

### Phase 12K

Every core window must contain actual integers and actual divisors. No sub-integer mesh is accepted.

### Phase 12L

The construction is not greedy. A maximum-gap greedy decoder would require a fresh audit and may fail.

### Phase 12M

The large profile count is used only as a necessary gate. Independent decoding or separable recursion is not assumed.

### Phase 12N

Menus spread across scales may still leave shell gaps. The additive theorem must eliminate them.

### Phase 12O

Finite mixed-scale success motivates menu scheduling but gives no asymptotic theorem.

### Phase 12P

The frozen object is a global rainbow sumset, not a one-choice sequential coverage ladder. A sequential proof strategy could re-enter the obstruction.

## 14. Mandatory falsification duties

The route fails if any of the following occurs:

1. an address exceeds `v_2(n!)`;
2. a menu contains an illegal, even, unit, or oversized core;
3. two layers share an address;
4. the profile-capacity inequality fails;
5. menu correlations collapse the effective sumset;
6. a residue class remains inaccessible after adding the palette;
7. a downward gap exceeds `2^{r_n}-1`;
8. the selected-term count exceeds `M_n+r_n`;
9. a sequential decoder is used without a Phase 12P audit;
10. finite success is promoted asymptotically.

## 15. Finite test plan

For each tested `n`:

1. compute exact factorial valuations;
2. build every frozen menu and assert legality;
3. verify within-layer uniqueness, address separation, and palette disjointness;
4. compute the profile-capacity lower bound before any expensive search;
5. run restricted rainbow reachability that allows at most one element from each layer;
6. record maximum downward gap and first missing residue class;
7. compare formal profile count with the number of distinct sums to measure collision loss;
8. record witness term counts.

Finite success is computational evidence only.

## 16. Asymptotic failure condition

Result label: **disproved route** if one proves that every admissible menu system with

\[
M_n=O((\log n)^2),
\qquad
r_n=O(\log n)
\]

has infinitely many `n` and targets `x<=X_n` for which

\[
[x-(2^{r_n}-1),x]
\cap
\Sigma_{\rm rb}(\mathcal A_1,\ldots,\mathcal A_{M_n})
=\varnothing.
\]

A persistent residue obstruction after correction also disproves the route.