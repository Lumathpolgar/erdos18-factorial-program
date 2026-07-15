# Construction N1-CON-001: Valuation-Tagged Address Packets

Result label: **heuristic** as a half-range route.

The divisor legality, term budget, numerical distinctness, and correction reduction used by this construction are proved theorems. Uniform coverage is not proved.

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

Choose an odd core `u_t` satisfying

\[
u_t>1,
\qquad
u_t\mid n!,
\qquad
2^{e_t}u_t\le X_n.
\]

Define the addressed divisor

\[
d_t=2^{e_t}u_t.
\]

The main family is

\[
\mathcal A_n=\{d_t:1\le t\le M_n\}.
\]

The selectable main sums are arbitrary subset sums

\[
\Sigma(\mathcal A_n)=\left\{\sum_{t\in T}d_t:T\subseteq\{1,\ldots,M_n\}\right\}.
\]

The correction palette is

\[
\mathcal C_{r_n}=\{1,2,\ldots,2^{r_n-1}\}.
\]

The index set may be partitioned into bookkeeping packets of size `O(log n)`, but the mathematical selection is global. No ordered one-choice packet rule is part of the construction.

## 2. Factorial-specific multiplicity

Result label: **proved theorem**.

For every fixed `A,B`,

\[
r_n+M_n\le v_2(n!)
\]

for all sufficiently large `n`, because `v_2(n!)=n-s_2(n)` and `(log n)^2=o(n)`.

The construction therefore has `Theta((log n)^2)` distinct 2-adic addresses. This is unavailable in

\[
L_n=\operatorname{lcm}(1,\ldots,n),
\]

where `v_2(L_n)=floor(log_2 n)`.

## 3. Legal divisor proof

Result label: **proved theorem** under the explicit core hypotheses.

Each `u_t` is odd and divides `n!`. Since `e_t<=v_2(n!)`, and the 2-adic and odd-prime valuations are disjoint coordinates,

\[
d_t=2^{e_t}u_t\mid n!.
\]

Every correction term `2^j`, `0<=j<r_n`, divides `n!` because `r_n-1<=v_2(n!)`.

The construction never multiplies two selected summands, so shared odd factors between different cores do not create a legality violation.

## 4. Numerical distinctness proof

Result label: **proved theorem**.

For every `t`,

\[
v_2(d_t)=e_t.
\]

The exponents `e_t` are pairwise distinct, so the `d_t` are pairwise distinct. Every `d_t` has odd part greater than one, whereas every correction term is a pure power of two. Therefore main and correction terms are numerically disjoint.

This proof remains valid even if several cores `u_t` are equal.

## 5. Packet and selection budget

At most `M_n` main terms and at most `r_n` correction terms can be selected. The exact architecture bound is

\[
M_n+r_n
\le A(\log n)^2+B\log n+2.
\]

There is no recursive multiplier in this count.

## 6. Represented scale

To place a main divisor near a prescribed scale `Y_t`, it is enough to find an odd divisor core in

\[
\frac{Y_t}{2^{e_t}}
\le u_t\le
\frac{Y_t+W_t}{2^{e_t}}.
\]

Then

\[
Y_t\le d_t\le Y_t+W_t.
\]

The 2-adic address is used for collision prevention, not for scale generation. The odd divisor lattice must supply the coarse magnitude.

A schedule may use `J=ceil(C log n)` logarithmic scale blocks, each containing `ceil(C' log n)` addressed divisors. This gives `O(log n)` choices per scale and `O((log n)^2)` total terms without imposing a sequential decoding order.

## 7. Collision analysis

- Within a packet: distinct 2-adic addresses prevent equality.
- Across packets: the global address set is pairwise distinct, so packet boundaries are irrelevant to equality.
- With correction terms: impossible because every main term has odd part greater than one.
- Hidden coordinate dependence: cores may share primes, but this affects neither equality nor legality because tags are distinct and summands are not multiplied.
- Duplicate subset sums: possible and not prohibited. The target requires distinct divisors within a representation, not injectivity of the subset-sum map. Duplicate sums reduce effective capacity and must be measured by Nova 2 or Nova 4.

## 8. Correction mechanism

Result label: **conditional theorem**.

Assume every integer `x` with

\[
2^{r_n}\le x\le X_n
\]

admits a main subset sum `y in Sigma(A_n)` with

\[
x-(2^{r_n}-1)\le y\le x.
\]

Then the proved binary correction lemma gives

\[
H_{n!}(X_n+1)\le M_n+r_n=O((\log n)^2).
\]

The residual is represented by the unique binary subset of `C_{r_n}`.

## 9. Exact missing additive theorem

### N1-REQ-N2-001-A

For fixed absolute constants `A,B>0`, and for every sufficiently large `n`, let `A_n` be the exact addressed divisor family committed with this construction. Prove that for every integer

\[
2^{r_n}\le x\le X_n,
\]

there is a subset `T_x subseteq {1,...,M_n}` such that

\[
x-(2^{r_n}-1)
\le\sum_{t\in T_x}d_t\le x.
\]

The conclusion must be uniform in every target `x`. It must use no more than `M_n` main terms, and it must apply to the frozen numerical family, not merely to an abstract family with the same cardinality.

A stronger exact representation statement is unnecessary.

## 10. Exact missing analytic theorem

### N1-REQ-N3-001-A

Given the frozen scale windows

\[
I_t(n)=[L_t(n),U_t(n)]
\]

for `1<=t<=M_n`, prove that for all sufficiently large `n` every window contains an odd divisor `u_t` of `n!` satisfying

\[
u_t>1,
\qquad
2^{e_t}u_t\le X_n.
\]

The cores need not be distinct. No additive conclusion is requested. The final handoff freezes `L_t` and `U_t` after Nova 2 identifies the weakest useful scale schedule.

## 11. Known historical obstruction audit

### Phase 12K

The construction does not request sub-integer entry windows. Any eventual analytic window schedule must nevertheless verify integer nonemptiness.

### Phase 12L

No maximum-gap greedy orbit is part of the definition. A proof that sorts the divisors and applies the historical greedy recurrence would re-enter the obstruction.

### Phase 12M

The construction does not infer coverage from `2^{M_n}` formal subsets. Effective occupancy is the exact missing theorem.

### Phase 12N

Magnitude-separated scale blocks may still have shell gaps. The downward-window theorem must explicitly rule them out.

### Phase 12O

Finite mixed-scale success motivates testing, but supplies no asymptotic step.

### Phase 12P

The route is not defined as a one-choice sequential ladder. If a future proof selects one item from each ordered packet and extends a covered interval step by step, the Phase 12P hypotheses must be checked again.

## 12. Mandatory falsification duties

The route fails if any of the following occurs for infinitely many `n`:

1. `r_n+M_n>v_2(n!)`;
2. a chosen core is even, equal to one, not a divisor of `n!`, or places `d_t>X_n`;
3. two address exponents coincide;
4. a main divisor is a pure power of two;
5. the gcd or residue span of the main family creates inaccessible downward windows;
6. the maximum gap in the main subset-sum set exceeds `2^{r_n}-1` somewhere below `X_n`;
7. the only available proof uses more than `M_n` main terms;
8. a finite successful schedule is promoted without uniform asymptotic proof.

## 13. Finite test plan

For a sequence of moderate `n` values:

1. compute exact `v_p(n!)`;
2. generate the frozen cores and addressed divisors;
3. assert `d_t|n!`, `d_t<=X_n`, odd core greater than one, and pairwise numerical distinctness;
4. assert disjointness from `C_{r_n}`;
5. compute reachable subset sums up to `X_n` by a fail-closed bitset or meet-in-the-middle method;
6. record the first target whose downward distance to the attainable set exceeds `2^{r_n}-1`;
7. compute residue-class occupancy modulo small moduli;
8. report term counts for actual witnesses, not only reachability.

Finite success is computational evidence only.

## 14. Asymptotic failure condition

Result label: **disproved route** if one proves that, for every admissible addressed family with `M_n=O((log n)^2)` and `r_n=O(log n)`, there are infinitely many `n` and targets `x<=X_n` for which

\[
[x-(2^{r_n}-1),x]\cap\Sigma(\mathcal A_n)=\varnothing.
\]

Such a theorem would eliminate the entire address-packet architecture, not merely one scale schedule.