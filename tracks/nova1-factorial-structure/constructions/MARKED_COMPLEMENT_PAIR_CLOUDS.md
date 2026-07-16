# Construction N1-CON-002: Marked Complement-Pair Menu Clouds

Result label: **heuristic** as a half-range route.

This revision replaces the disproved fixed-pair family with `O((log n)^2)` labeled slots, each carrying a large menu of complement-paired choices. The selected-term count is polylogarithmic, while the available-choice count can meet the factorial capacity scale.

The construction is globally nonsequential.

## 1. Formal definition

Let

\[
X_n=\lfloor\sqrt{n!}\rfloor,
\qquad
r_n=\lceil B\log n\rceil,
\qquad
M_n\le C(\log n)^2.
\]

For every slot `1<=s<=M_n`, choose a square divisor

\[
Q_s=R_s^2\mid n!
\]

such that:

1. `R_s<=X_n`;
2. `5|R_s`;
3. the center tags
   \[
   E_s=v_2(R_s)
   \]
   are pairwise distinct.

Choose a finite multiplier menu `Z_s(n)` satisfying, for every `z in Z_s(n)`,

\[
z\mid R_s,
\qquad
\gcd(z,10)=1,
\qquad
1<z\le X_n/R_s.
\]

Define the slot menu

\[
\mathcal B_s(n)=
\{R_s/z:z\in Z_s(n)\}
\cup
\{R_sz:z\in Z_s(n)\}.
\]

A main representation selects either zero terms or exactly one term from each slot. The global rainbow sumset is

\[
\Sigma_{\rm cp}(n)=
\left\{
\sum_{s=1}^{M_n}c_s:
 c_s\in\mathcal B_s(n)\cup\{0\}
\right\}.
\]

The correction palette is

\[
\mathcal C_{r_n}=\{1,2,\ldots,2^{r_n-1}\}.
\]

## 2. Disproved predecessor

Result label: **disproved route**.

The predecessor with one frozen pair in each of `M_n=O((log n)^2)` slots had at most `3^{M_n}` formal profiles. With quasipolynomial or smaller correction width, it cannot cover the `exp(Theta(n log n))` factorial half-range. The proof is in `proofs/COUNTING_CAPACITY_OBSTRUCTION.md`.

The surviving route requires large multiplier menus.

## 3. Legal divisor proof

Result label: **proved theorem** under the slot hypotheses.

For `z|R_s`, write

\[
v_p(R_s)=A_p,
\qquad
v_p(z)=u_p.
\]

Then

\[
v_p(R_s/z)=A_p-u_p,
\qquad
v_p(R_sz)=A_p+u_p,
\]

and both exponents lie in `[0,2A_p]=[0,v_p(Q_s)]`. Therefore every menu term divides `Q_s`, hence divides `n!`.

The upper multiplier bound gives `R_sz<=X_n`; the reciprocal term is below `R_s<=X_n`.

## 4. Numerical distinctness proof

Result label: **proved theorem**.

Within one slot, distinct multipliers produce distinct low terms and distinct high terms. Every low term is below `R_s`, and every high term is above `R_s`, so low/high collisions are impossible.

Every multiplier is odd, hence every term in slot `s` has

\[
v_2(c)=E_s.
\]

Pairwise distinct center tags prevent equality across slots.

Because `5|R_s` and every multiplier is coprime to `5`, every slot term is divisible by `5`. Thus no main term equals a pure power of two from the correction palette.

## 5. Selectable term budget

At most one term is selected from each of `M_n` slots. Therefore the main cost is at most `M_n`, independent of the menu sizes. Including correction gives

\[
M_n+r_n
\le C(\log n)^2+B\log n+1.
\]

There is no recursion.

## 6. Necessary capacity gate

Result label: **proved theorem**.

Slot `s` has at most `1+2|Z_s(n)|` formal states, including zero. Thus

\[
P_n=\prod_{s=1}^{M_n}(1+2|Z_s(n)|)
\]

is an upper bound for the number of distinct attainable main sums.

Downward-window coverage with width

\[
R_n=2^{r_n}-1
\]

requires

\[
P_n(R_n+1)\ge X_n+1,
\]

or

\[
\sum_{s=1}^{M_n}\log(1+2|Z_s(n)|)
\ge
\log(X_n+1)-r_n\log2.
\]

This is necessary only. Arithmetic collisions can reduce the actual sumset.

## 7. Represented scale and complement geometry

Slot `s` supplies reciprocal terms around the center `R_s`:

\[
R_s/z<R_s<R_sz.
\]

A multiplier window `z in [L,U]` supplies low terms in

\[
[R_s/U,R_s/L]
\]

and high terms in

\[
[R_sL,R_sU].
\]

Thus one analytic multiplier menu populates two coupled magnitude ranges. This is materially different from a one-sided high-prime atlas.

If a representation uses a low term `R_s/z` and switches to the paired high term `R_sz`, the exact increment is

\[
\Delta_s(z)=R_sz-R_s/z.
\]

The menu contains many possible increments, but a legal representation chooses at most one state from the slot.

## 8. Global nonsequential structure

Result label: **proved theorem** as a classification of the frozen selection rule.

All slot choices are made jointly in one rainbow sumset. The definition has:

- no ordered interval-extension recurrence;
- no greedy target decoder;
- no requirement to choose a nonzero term from every slot;
- no fixed one-choice sequential ladder.

Therefore Phase 12P does not apply automatically. Any proof that later imposes an ordered sequential decoder must be audited separately.

## 9. Collision and dependence analysis

- Within a slot: low/low and high/high equality force equal multipliers; low/high equality is impossible.
- Across slots: distinct 2-adic center tags prevent equality.
- With the palette: divisibility by `5` prevents collision.
- Duplicate total sums: possible.
- Hidden dependence: multiplier menus may share prime supports, creating correlated increments and residue obstructions.
- Capacity versus coverage: the profile bound is only a necessary gate.
- Complement symmetry: it provides paired scales, not additive density by itself.

## 10. Correction mechanism

Result label: **conditional theorem**.

Assume that for every integer

\[
2^{r_n}\le x\le X_n
\]

there exists `s in Sigma_cp(n)` such that

\[
x-(2^{r_n}-1)\le s\le x.
\]

Then

\[
H_{n!}(X_n+1)
\le M_n+r_n
=O((\log n)^2)
\]

by the binary correction lemma.

## 11. Exact missing additive theorem

### N1-REQ-N2-001-B

For the exact frozen slot menus `B_s(n)`, prove that for every sufficiently large `n` and every integer

\[
2^{r_n}\le x\le X_n,
\]

there exist choices

\[
c_s\in\mathcal B_s(n)\cup\{0\}
\]

such that

\[
x-(2^{r_n}-1)
\le\sum_{s=1}^{M_n}c_s\le x.
\]

The theorem must preserve at most one selected term per slot and explicitly address gcd, residue-span, shell-gap, and collision-loss issues.

## 12. Exact missing analytic theorem

### N1-REQ-N3-001-B

For every sufficiently large `n`, construct square centers `R_s^2|n!` and multiplier menus `Z_s(n)` satisfying all of the following:

1. `M_n<=C(log n)^2`;
2. `R_s<=X_n`, `5|R_s`, and the values `v_2(R_s)` are pairwise distinct;
3. each multiplier is an odd divisor of `R_s`, coprime to `5`, and at most `X_n/R_s`;
4. for every frozen multiplier window `J_{s,k}(n)`,
   \[
   |Z_s(n)\cap J_{s,k}(n)|\ge Q_{s,k}(n);
   \]
5. the total menu sizes satisfy the necessary capacity inequality;
6. the bounds hold uniformly over all frozen slots and windows.

No additive conclusion is requested from Nova 3.

## 13. Known historical obstruction audit

### Phase 12K

Every center and multiplier window must contain actual integer divisors. No continuous mesh assumption is permitted.

### Phase 12L

The construction is not greedy. A sorted greedy decoder may inherit the historical lower bound.

### Phase 12M

The large formal profile count is not decoded independently and is not treated as coverage.

### Phase 12N

Reciprocal low/high menus weaken the old shell separation, but only the additive theorem can rule out shell gaps.

### Phase 12O

The shared-core idea survives in exact complement form. Finite success remains finite evidence.

### Phase 12P

The object is globally nonsequential and has large menus with zero allowed. A later sequential one-choice proof would require a new audit.

## 14. Mandatory falsification duties

The route fails if any of the following occurs:

1. a center square does not divide `n!`;
2. a multiplier is illegal, even, divisible by `5`, or too large;
3. two slots share a 2-adic center tag;
4. the capacity inequality fails;
5. menu correlations collapse most formal profiles;
6. a residue class remains inaccessible after correction;
7. a downward gap exceeds `2^{r_n}-1`;
8. more than one term from a slot is needed;
9. the total selected-term count exceeds `M_n+r_n`;
10. a sequential decoder is used without a Phase 12P audit;
11. finite success is promoted asymptotically.

## 15. Finite test plan

For each tested `n`:

1. compute exact factorial valuations;
2. generate and verify square centers;
3. generate multiplier menus and pair terms;
4. assert legality, upper range, within-slot uniqueness, cross-slot address separation, and palette disjointness;
5. check the necessary capacity inequality before occupancy search;
6. compute restricted rainbow reachability with at most one term per slot;
7. record maximum downward gap and first inaccessible residue class;
8. compare formal profiles with distinct sums to measure collision loss;
9. test whether any successful decoder secretly depends on sequential ordering;
10. retain exact witnesses and exact first failures.

Finite success is computational evidence only.

## 16. Asymptotic failure condition

Result label: **disproved route** if one proves that every admissible complement-menu system with

\[
M_n=O((\log n)^2),
\qquad
r_n=O(\log n)
\]

has infinitely many `n` and targets `x<=X_n` for which

\[
[x-(2^{r_n}-1),x]
\cap\Sigma_{\rm cp}(n)
=\varnothing.
\]

A persistent residue obstruction after correction also disproves the route.