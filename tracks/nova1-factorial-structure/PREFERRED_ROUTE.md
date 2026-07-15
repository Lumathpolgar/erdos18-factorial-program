# Preferred Route

## Route ranking

### Rank 1: N1-CON-003, marker-three valuation rainbow

Result label: **heuristic** as the open half-range route.

This is now the preferred route because it passes the exact lattice-first structural gate:

1. every main divisor is legal;
2. different layers have different exact 2-adic valuations;
3. every main divisor is divisible by `3`, so the binary palette is numerically disjoint;
4. the exact main support lattice is `3Z`;
5. the palette attains every residue modulo `3`;
6. the first target is directly covered;
7. the remaining claim is a final-only quotient rainbow window theorem;
8. the selected-term cost is `O((log n)^2)`;
9. the necessary formal profile-capacity gate holds for every `n>=120368`.

### Rank 2: N1-CON-002, marked complement-pair menu clouds

Result label: **heuristic**.

This remains a globally nonsequential secondary route. It is ranked second because it requires an additional analytic construction of square centers and multiplier menus before its additive law can be frozen.

### Disproved predecessor: N1-CON-001

Result label: **disproved route**.

Nova 2 disproved the first preferred route at:

- branch: `nova/additive-occupancy`
- exact commit: `45c74a5fa747551422ffcad7d3ddf22788fbe622`
- theorem: `N2-ADD-115`
- obstruction: `N2-OBS-107`

The old addresses were `e_t=r_n+t`. Therefore every main sum was divisible by `2^(r_n+1)`, while the correction radius was only `2^r_n-1`. The first required window contained no main sum.

The fixed-family and polynomial-menu predecessors remain disproved by the counting-capacity and menu-entropy obstructions.

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

Result label: **proved theorem**.

For all sufficiently large `n`, `M_n-1<=v_2(n!)`. Every main term divides `n!`. Terms from different layers have distinct exact 2-adic valuations `t-1`. Every main term is divisible by `3`, while every palette term is a pure power of two.

### N1-STR-015: support lattice and residues

Result label: **proved theorem**.

The main support generates exactly `3Z` because every main term is divisible by `3` and the first layer contains `3`. The palette contains `1` and `2`, so the combined system attains every residue class modulo `3`.

### N1-RED-004: quotient-window correction

Result label: **proved theorem**.

Write

\[
x=3q+\delta,
\qquad
\delta\in\{0,1,2\}.
\]

If `q<=W_n`, then `x<=R_n` and the palette represents `x` directly.

If there is a quotient rainbow sum `s` with

\[
q-W_n\le s\le q,
\]

then the corresponding main sum is `3s`, and the residual satisfies

\[
0\le x-3s\le2+3W_n\le R_n.
\]

Thus the quotient-window theorem implies

\[
H_{n!}(X_n+1)\le M_n+r_n=O((\log n)^2).
\]

### N1-STR-016: odd-digit one-gap lemma

Result label: **proved theorem**.

For odd `m>=3`, the restricted positional set

\[
\left\{
\sum_{e=0}^{L-1}2^ea_e:
 a_e\in\{0,1,3,5,\ldots,m\}
\right\}
\]

has maximum downward gap at most one throughout

\[
[0,m(2^L-1)].
\]

### N1-STR-017: unconditional initial interval

Result label: **proved theorem**.

Let `m_n` be the largest odd integer at most `n`. For all sufficiently large `n`, the construction represents every integer

\[
0\le x\le3m_n(2^{M_n}-1)+2
\]

using at most `M_n+r_n` distinct divisors of `n!`.

This is an unconditional range of size `exp(O((log n)^2))`. It is far below `X_n=exp(Theta(n log n))` and is not the half-range theorem.

### N1-STR-018: explicit repaired menu lower bound

Result label: **proved theorem**.

Nova 3 proved, at branch `nova/analytic-density`, exact commit `e60069f797af878711e7a9d4abb1fb6188a1f724`, that for every integer `n>=120368`,

\[
\pi(n)-\pi(n/2)\ge\frac{n}{3\log n}.
\]

Nova 1 re-audited its use for the marker-three menus. For every `n>=120368` and every `1<=t<=M_n`,

\[
|U_t(n)|
\ge2^{\pi(n)-\pi(n/2)-1}
\ge2^{n/(3\log n)-1}.
\]

The proof uses complementary subset products of primes in `(n/2,n]`, reserves the factor `3` separately, and verifies the largest layer cutoff.

### N1-CAP-002: explicit profile-capacity gate

Result label: **proved theorem**.

For every integer `n>=120368`,

\[
2^{r_n}
\prod_{t=1}^{M_n}(|U_t(n)|+1)
\ge X_n+1.
\]

This closes the necessary counting-capacity requirement. It does not control collisions between profiles or prove numerical additive occupancy.

Proof location: `proofs/MARKER_THREE_MENU_CAPACITY.md`.

### Exact term cost

Result label: **proved theorem**.

The architecture uses at most

\[
M_n+r_n
=\lceil16(\log n)^2\rceil+
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

## Why this route survives the recorded obstructions

- It is not a maximum-gap greedy orbit.
- It does not decode independent CRT coordinates.
- It does not infer coverage from profile count.
- It does not use magnitude-separated high-prime shells.
- It does not impose a sequential partial-coverage invariant.
- It uses factorial-specific `Theta((log n)^2)` 2-adic addresses.
- It has an exact common lattice, exact attained residues, and a correction radius larger than every unresolved lattice residue gap.

The route may still fail through collision concentration, an endpoint support deficit, or quotient shell gaps larger than `W_n`.

## Computational evidence

The exact reduced-parameter verifier passes for every `7<=n<=14`. In those tests the quotient maximum downward distance is at most one, and the palette reconstructs the complete factorial half-range.

Files:

- `verification/marker_three_sanity.py`
- `verification/MARKER_THREE_FINITE_REPORT.md`

This is computational evidence only.

## Exact blockers

1. **Quotient rainbow occupancy:** prove or disprove the frozen `W_n`-window theorem.
2. **Endpoint support:** prove that the quotient support reaches every required endpoint window.
3. **Collision audit:** quantify collapse of formal rainbow profiles to numerical sums.
4. **Bounded-torus analytic input:** only after Nova 2 freezes the exact tilted numerical-value law.
5. **Track B reconstruction:** prove the current-notation local-to-global implication.
6. **Finite exceptions:** handle all `n<n_0` after an effective threshold exists.

## Next theorem target

The next target is the exact handoff `N1-REQ-N2-002`:

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

A general counterexample or asymptotic maximum-gap lower bound against this exact construction is equally valid.
