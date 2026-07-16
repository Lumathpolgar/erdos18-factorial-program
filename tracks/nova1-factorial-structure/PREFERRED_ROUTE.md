# Preferred Route

## Route ranking

### Rank 1: N1-CON-003, marker-three valuation rainbow

Result label: **heuristic** as the open half-range route.

This is the preferred route because it passes the structural compatibility gates:

1. every main divisor is legal;
2. different layers have different exact 2-adic valuations;
3. every main divisor is divisible by `3`, so the binary palette is numerically disjoint;
4. the exact main support lattice is `3Z`;
5. the palette attains every residue modulo `3`;
6. the first target is directly covered;
7. total quotient support reaches beyond the final target;
8. the selected-term cost is `O((log n)^2)`;
9. the necessary formal profile-capacity gate holds for every `n>=120368`;
10. the remaining central claim is final-only numerical quotient occupancy.

### Rank 2: N1-CON-002, marked complement-pair menu clouds

Result label: **heuristic**.

This is a globally nonsequential secondary route. It requires an additional analytic construction of square centers and multiplier menus before its additive law can be frozen.

### Disproved predecessor: N1-CON-001

Result label: **disproved route**.

Nova 2 disproved the first preferred route at:

- branch: `nova/additive-occupancy`
- exact commit: `45c74a5fa747551422ffcad7d3ddf22788fbe622`
- theorem: `N2-ADD-115`
- obstruction: `N2-OBS-107`

The old addresses were `e_t=r_n+t`. Every main sum was divisible by `2^(r_n+1)`, while the correction radius was only `2^r_n-1`. The first requested window contained no main sum.

## Frozen preferred construction

For every integer `n>=3`, define

\[
X_n=\lfloor\sqrt{n!}\rfloor,
\qquad
r_n=\lceil4\log n\rceil,
\qquad
M_n=\lceil16(\log n)^2\rceil,
\]

\[
R_n=2^{r_n}-1,
\qquad
W_n=\left\lfloor\frac{R_n-2}{3}\right\rfloor.
\]

For `1<=t<=M_n`, define

\[
U_t(n)=
\left\{
 u\ge1:
 u\text{ odd},\ 3u\mid n!,\ 3\cdot2^{t-1}u\le X_n
\right\},
\]

\[
A_t^{(3)}(n)=
\{3\cdot2^{t-1}u:u\in U_t(n)\},
\]

and the quotient layer

\[
B_t(n)=
\{2^{t-1}u:u\in U_t(n)\}.
\]

A main sum chooses at most one divisor from each `A_t^(3)(n)`. The correction palette is

\[
C_n=\{1,2,4,\ldots,2^{r_n-1}\}.
\]

## Proved structural nodes

### N1-STR-014: legality and distinctness

For all sufficiently large `n`, `M_n-1<=v_2(n!)`. Every main term divides `n!`. Different layers have exact 2-adic valuations `t-1`. Every main term is divisible by `3`, while every palette term is a pure power of two.

### N1-STR-015: support lattice and residues

The main support generates exactly `3Z` because every main term is divisible by `3` and the first layer contains `3`. The palette contains `1` and `2`, so the combined system attains every residue modulo `3`.

### N1-RED-004: quotient-window correction

Write

\[
x=3q+\delta,
\qquad
\delta\in\{0,1,2\}.
\]

If `q<=W_n`, the palette represents `x` directly. If a quotient rainbow sum `s` satisfies

\[
q-W_n\le s\le q,
\]

then

\[
0\le x-3s\le2+3W_n\le R_n,
\]

so the palette represents the residual. Therefore the quotient-window theorem implies

\[
H_{n!}(X_n+1)\le M_n+r_n.
\]

### N1-STR-016 and N1-STR-017: initial interval

For odd `m>=3`, positional sums with digits `{0,1,3,5,...,m}` have maximum downward gap one on

\[
[0,m(2^L-1)].
\]

Consequently, for all sufficiently large `n`, the construction represents every integer

\[
0\le x\le3m_n(2^{M_n}-1)+2
\]

using at most `M_n+r_n` terms, where `m_n` is the largest odd integer at most `n`.

This range is `exp(O((log n)^2))`, far below the factorial half-range.

### N1-STR-018 and N1-CAP-002: explicit menu capacity

Nova 3 proved at branch `nova/analytic-density`, exact commit `e60069f797af878711e7a9d4abb1fb6188a1f724`, that for every `n>=120368`,

\[
\pi(n)-\pi(n/2)\ge\frac{n}{3\log n}.
\]

Nova 1 translated this to the repaired menus. For every `n>=120368` and every layer,

\[
|U_t(n)|
\ge2^{\pi(n)-\pi(n/2)-1}
\ge2^{n/(3\log n)-1},
\]

and

\[
2^{r_n}\prod_{t=1}^{M_n}(|U_t(n)|+1)
\ge X_n+1.
\]

This closes only the necessary counting-capacity gate.

### N1-STR-019: multiplicative 3-density

For every `n>=6`, define

\[
D_n=\frac{n!}{3\cdot2^{v_2(n!)}}.
\]

Every real `1<=z<=D_n` has a divisor `d|D_n` satisfying

\[
z/3<d\le z.
\]

The proof builds `D_n` prime power by prime power. Powers of `3` are 3-dense, and adjoining `p^a` preserves 3-density whenever `p<=3D_prefix`. The factorial valuation of `3` guarantees this condition for every later prime.

### N1-STR-020: endpoint support

Let

\[
Q_n=\left\lfloor\frac{X_n}{3}\right\rfloor.
\]

For every `n>=12`, each of the first three quotient layers contains a legal term

\[
b_t\in B_t(n)
\]

with

\[
X_n/9<b_t\le X_n/3.
\]

Their exact 2-adic valuations are `0`, `1`, and `2`, so they are distinct. Therefore

\[
b_1+b_2+b_3>X_n/3\ge Q_n.
\]

Thus the maximum quotient rainbow sum satisfies

\[
S_n^{\max}\ge Q_n+1.
\]

The final target is not outside the total attainable support.

This does not prove a sum in

\[
[Q_n-W_n,Q_n].
\]

Maximum support and downward endpoint-window occupancy are different statements.

### N1-RED-006: deterministic coarse contraction

For `n>=12` and `0<=q<=Q_n`, a deterministic increasing-layer selection leaves residual

\[
\rho_L<\max\{(2/3)^Lq,2^L\}
\]

after `L` layers.

This supplies a rigorous coarse reduction, but it does not reach the polynomial radius `W_n`. It is not the proposed final proof architecture.

### Exact term cost

The construction uses at most

\[
M_n+r_n
=
\lceil16(\log n)^2\rceil+
\lceil4\log n\rceil
\]

terms. There is no recursion or hidden multiplicative cost.

## Frozen conditional theorem

### N1-RED-005

Result label: **conditional theorem**.

Assume there is an absolute `n_0` such that for every integer `n>=n_0` and every integer

\[
W_n+1\le q\le\left\lfloor\frac{X_n}{3}\right\rfloor,
\]

there are choices

\[
b_t\in B_t(n)\cup\{0\}
\]

with at most one nonzero choice per layer and

\[
q-W_n\le\sum_{t=1}^{M_n}b_t\le q.
\]

Then

\[
H_{n!}(X_n+1)=O((\log n)^2).
\]

After reconstruction of the archived Track B implication, this would yield

\[
h(n!)=O((\log n)^3).
\]

## Why the route survives the recorded obstructions

- It is not a maximum-gap greedy orbit.
- It does not decode independent CRT coordinates.
- It does not infer coverage from profile count.
- It does not use magnitude-separated high-prime shells.
- The frozen occupancy request is final-only and does not impose a sequential partial-coverage invariant.
- It uses factorial-specific `Theta((log n)^2)` 2-adic addresses.
- It has an exact common lattice, exact attained residues, direct first-target coverage, and total endpoint reach.

The route may still fail through collision concentration or quotient shell gaps larger than `W_n`.

## Computational evidence

Exact finite checks include:

- reduced quotient occupancy for every `7<=n<=14`;
- multiplicative 3-density for every `6<=n<=20`;
- endpoint crossing for every `12<=n<=20`;
- exhaustive coarse contraction for all quotient targets with `12<=n<=14` and `1<=L<=6`.

Files:

- `verification/marker_three_sanity.py`
- `verification/MARKER_THREE_FINITE_REPORT.md`
- `verification/endpoint_support_sanity.py`
- `verification/ENDPOINT_SUPPORT_FINITE_REPORT.md`

These are finite evidence only.

## Exact blockers

1. **Quotient rainbow occupancy:** prove or disprove the frozen `W_n`-window theorem.
2. **Downward endpoint window:** prove a sum exists in `[Q_n-W_n,Q_n]`; total endpoint reach is closed.
3. **Collision audit:** quantify collapse of formal rainbow profiles to numerical sums.
4. **Bounded-torus analytic input:** begin only after Nova 2 freezes the exact numerical-value law.
5. **Track B reconstruction:** prove the current-notation local-to-global implication.
6. **Finite exceptions:** handle all `n<n_0` after an effective threshold exists.

## Next theorem target

Prove or disprove

\[
\forall n\ge n_0\ \forall q\in
\left[W_n+1,\left\lfloor X_n/3\right\rfloor\right]\cap\mathbb Z,
\]

\[
[q-W_n,q]
\cap
\Sigma_{\rm rb}(B_1(n),\ldots,B_{M_n}(n))
\ne\varnothing.
\]

The support endpoint is closed. The remaining node is numerical downward-window occupancy.