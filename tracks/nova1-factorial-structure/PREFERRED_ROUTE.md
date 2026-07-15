# Preferred Route

## Route ranking

### Rank 1: N1-CON-001, full-menu valuation-tagged address packets

Result label: **heuristic** as the open half-range route.

This is the preferred route because it has the smallest structural dependency surface:

1. legality follows directly from factorial valuations;
2. numerical distinctness follows from unique 2-adic addresses;
3. the correction palette is exact and disjoint;
4. the menu is canonical, using all admissible odd divisor cores rather than an unproved hand-selected atlas;
5. the necessary profile-capacity gate can be passed using high primes in `(n/2,n]`;
6. the only central open theorem is the global rainbow occupancy statement.

### Rank 2: N1-CON-002, marked complement-pair menu clouds

Result label: **heuristic**.

This remains the strongest secondary route because it is globally nonsequential and populates reciprocal scales around each square center. It is ranked second because it requires additional analytic construction of square centers and multiplier menus before Nova 2 can attack occupancy.

### Retired predecessors

Result label: **disproved route**.

The fixed-family versions with only `O((log n)^2)` total available binary or ternary choices are impossible by the counting-capacity obstruction. Polynomial-size menus are also impossible.

## Frozen preferred construction

For every integer `n`, define

\[
X_n=\lfloor\sqrt{n!}\rfloor,
\qquad
V_n=v_2(n!),
\]

and set

\[
r_n=\lceil4\log n\rceil,
\qquad
M_n=\lceil16(\log n)^2\rceil.
\]

For all sufficiently large `n`,

\[
r_n+M_n\le\lfloor V_n/2\rfloor-1.
\]

For each `1<=t<=M_n`, define

\[
e_t=r_n+t
\]

and the full admissible odd-core menu

\[
U_t(n)=
\left\{
 u\in\mathbb Z_{>0}:
 u\mid n!,\ u\text{ odd},\ u>1,\ 2^{e_t}u\le X_n
\right\}.
\]

Define the addressed layer

\[
\mathcal A_t(n)=\{2^{e_t}u:u\in U_t(n)\}.
\]

A legal main sum chooses

\[
d_t\in\mathcal A_t(n)\cup\{0\}
\]

for each layer and forms

\[
y=\sum_{t=1}^{M_n}d_t.
\]

The correction palette is

\[
\mathcal C_n=\{1,2,4,\ldots,2^{r_n-1}\}.
\]

## Proved structural nodes

### Divisor legality

Result label: **proved theorem**.

Every nonzero `d_t` divides `n!` because `e_t<=v_2(n!)` and its odd core divides the odd part of `n!`.

### Numerical distinctness

Result label: **proved theorem**.

At most one term is selected per layer. Different layers have different 2-adic valuations, so selected main terms are numerically distinct. Every main term has odd part greater than one, so no main term is a correction power of two.

### Exact term cost

Result label: **proved theorem**.

The construction uses at most

\[
M_n+r_n
=\lceil16(\log n)^2\rceil+\lceil4\log n\rceil
\]

terms.

### Menu-capacity lower bound

Result label: **proved theorem** in terms of the exact prime count

\[
m_n=\pi(n)-\pi(n/2).
\]

Every layer satisfies

\[
|U_t(n)|\ge2^{m_n-1}-1.
\]

Therefore the formal rainbow profile count is at least

\[
2^{M_n(m_n-1)}.
\]

Result label: **conditional theorem** for the explicit asymptotic capacity gate.

Under the audited prime-interval bound

\[
m_n\ge\frac{n}{3\log n}
\]

for all sufficiently large `n`, the necessary profile-capacity inequality

\[
\prod_{t=1}^{M_n}(|U_t(n)|+1)\,2^{r_n}
\ge X_n+1
\]

holds with room to spare.

This is not an occupancy theorem.

## Frozen conditional theorem

### N1-RED-003

Result label: **conditional theorem**.

Assume that there exists `n_0` such that for every integer `n>=n_0` and every integer

\[
2^{r_n}\le x\le X_n,
\]

there are choices

\[
d_t\in\mathcal A_t(n)\cup\{0\}
\]

satisfying

\[
x-(2^{r_n}-1)
\le\sum_{t=1}^{M_n}d_t\le x.
\]

Then every integer `0<=x<=X_n` is a sum of at most

\[
M_n+r_n=O((\log n)^2)
\]

distinct divisors of `n!`. Equivalently,

\[
H_{n!}(X_n+1)=O((\log n)^2).
\]

The archived conditional endgame would then give

\[
h(n!)=O((\log n)^3)
\]

once its current-notation reconstruction is accepted.

## Why the route survives historical obstructions

- It is not a maximum-gap greedy orbit.
- It does not decode independent CRT coordinates separately.
- It does not infer coverage from raw profiles.
- It is not a magnitude-separated high-prime shell ladder.
- It is not a fixed one-choice sequential shared-core ladder.
- It uses factorial-specific `Theta((log n)^2)` 2-adic addresses unavailable in `L_n`.

The route can still fail through collision concentration, inaccessible residues, or additive shell gaps. These remain active blockers.

## Exact blockers

1. **Prime-interval audit:** certify an effective lower bound for `pi(n)-pi(n/2)` sufficient for the capacity calculation.
2. **Rainbow occupancy:** prove or disprove uniform downward-window coverage for the frozen full-menu layers.
3. **Residue audit:** determine whether the addressed layers plus the binary palette leave any persistent inaccessible residue class.
4. **Collision audit:** quantify how many formal profiles collapse to the same sum.
5. **Track B reconstruction:** freeze the direct implication from the half-range theorem to `h(n!)=O((log n)^3)` under current endpoints.

## Next theorem target

The next theorem target is the exact Nova 2 handoff statement:

\[
\forall n\ge n_0\ \forall x\in[2^{r_n},X_n]\cap\mathbb Z,
\quad
[x-(2^{r_n}-1),x]
\cap
\Sigma_{\rm rb}(\mathcal A_1(n),\ldots,\mathcal A_{M_n}(n))
\ne\varnothing.
\]

A counterexample family or a general maximum-gap lower bound against this frozen construction is equally valid and must be recorded as a disproved route.