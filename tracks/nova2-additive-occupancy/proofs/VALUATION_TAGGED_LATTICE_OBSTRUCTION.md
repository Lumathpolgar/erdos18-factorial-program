# Valuation-Tagged Lattice Obstruction

## Theorem ID

`N2-ADD-115`

## Result label

**proved theorem**

## Corollary status

`N2-OBS-107`: **disproved model**

## Imported object and exact baseline

This proof audits the frozen handoff `N1-HO-N2-001` from:

- repository: `Lumathpolgar/erdos18-factorial-program`
- branch: `nova/factorial-structure`
- exact commit: `b939574eb88a08bb03abda5bbe6ff2ca97444e08`
- source file: `tracks/nova1-factorial-structure/handoffs/TO_NOVA2.md`
- source objects: `N1-CON-001`, `N1-RED-003`, `N1-REQ-N2-001-A`

No later Nova 1 revision is assumed.

## Frozen construction

For every integer `n>=3`, let

\[
X_n=\lfloor\sqrt{n!}\rfloor,
\qquad
r_n=\lceil4\log n\rceil,
\qquad
M_n=\lceil16(\log n)^2\rceil.
\]

For `1<=t<=M_n`, set

\[
e_t=r_n+t.
\]

The frozen layers are

\[
\mathcal A_t(n)
=
\{2^{e_t}u:
 u\mid n!,\ u>1,\ u\text{ odd},\ 2^{e_t}u\le X_n\}.
\]

The final restricted rainbow sumset is

\[
\mathcal R_n
=
\left\{
\sum_{t=1}^{M_n}d_t:
 d_t\in\mathcal A_t(n)\cup\{0\}
\right\}.
\]

The requested occupancy statement is that for every integer

\[
2^{r_n}\le x\le X_n
\]

there exists `y in R_n` with

\[
x-(2^{r_n}-1)\le y\le x.
\]

## General downward-window lattice lemma

Let `g>=2` and let `S subseteq g Z`. Let `R` be an integer with

\[
0\le R\le g-2.
\]

Then the target

\[
x=R+1
\]

satisfies

\[
[x-R,x]=[1,R+1]\subseteq[1,g-1],
\]

and therefore

\[
[x-R,x]\cap S=\varnothing.
\]

Thus no subset of `g Z` can meet every downward window of radius `R` over a target range containing `R+1` when `R<g-1`.

### Proof

The only multiple of `g` in `[0,g-1]` is `0`. The interval `[1,R+1]` is contained in `[1,g-1]` and excludes `0`. Hence it contains no element of `g Z`, and therefore no element of `S`. `QED`

## Application to the frozen Nova 1 layers

For every `t>=1`,

\[
e_t=r_n+t\ge r_n+1.
\]

Hence every nonzero element of every layer `A_t(n)` is divisible by

\[
g_n=2^{r_n+1}.
\]

Zero is also divisible by `g_n`. Therefore every restricted rainbow sum satisfies

\[
\mathcal R_n\subseteq g_n\mathbb Z.
\]

The requested correction radius is

\[
R_n=2^{r_n}-1.
\]

Since

\[
g_n=2^{r_n+1},
\qquad
R_n+1=2^{r_n}=g_n/2,
\]

we have

\[
R_n\le g_n-2.
\]

Apply the general lemma with `S=R_n`, `g=g_n`, and `R=R_n`. The failing target is

\[
x_n=R_n+1=2^{r_n}.
\]

Its required window is

\[
[x_n-R_n,x_n]
=[1,2^{r_n}].
\]

This interval contains no multiple of `2^{r_n+1}`. Consequently

\[
[1,2^{r_n}]\cap\mathcal R_n=\varnothing.
\]

The empty rainbow sum `0` does not repair the failure because `0` is outside the downward window.

## The target is genuinely inside the asymptotic range

The frozen theorem is intended for all sufficiently large `n` satisfying

\[
r_n+M_n\le\lfloor v_2(n!)/2\rfloor-1.
\]

This side condition holds for all sufficiently large `n` because

\[
v_2(n!)\ge\lfloor n/2\rfloor
\]

while

\[
r_n+M_n=O((\log n)^2)=o(n).
\]

Also, for all sufficiently large `n`,

\[
2^{r_n}\le X_n.
\]

Indeed,

\[
2^{r_n}\le 2^{4\log n+1}=2n^{4\log2}<2n^3,
\]

whereas

\[
\sqrt{n!}
\ge
\left(\frac n2\right)^{n/4}
\]

for even `n`, with an immaterial floor adjustment and the same eventual conclusion for all integers. The right-hand side eventually exceeds `2n^3`.

Therefore the failing target `x_n=2^{r_n}` lies in the requested target range for all sufficiently large admissible `n`.

## Exact conclusion

There is no absolute `n_0` such that the frozen theorem request in `N1-HO-N2-001` holds for every `n>=n_0`.

The failure is deterministic, occurs at the first requested target, and is independent of:

- the sizes of the odd menus `U_t(n)`;
- profile capacity;
- collisions between different profiles;
- major-arc estimates;
- minor-arc estimates;
- local central limit approximations;
- target-dependent tilting;
- finite computation.

No analytic input from Nova 3 can repair a support lattice that assigns zero mass to the entire requested window.

## Handoff decision

`N1-HO-N2-001`: **REJECTED**.

Reason: inaccessible residue classes caused by the common factor `2^{r_n+1}`.

## Minimal structural repairs that remove only this obstruction

The following are necessary design changes, not sufficient occupancy theorems.

### Repair A: enlarge the correction radius

Keeping the current layers requires a correction radius at least

\[
g_n-1=2^{r_n+1}-1
\]

for a generic all-residue downward-window bridge. A binary palette through `2^{r_n}` has this residual capacity and costs one additional correction term. The remaining problem would then be occupancy of the appropriate multiples of `g_n`.

### Repair B: lower the common 2-adic address

If the lowest layer address is changed so the common lattice span is at most `2^{r_n}`, then the current radius `2^{r_n}-1` is no longer ruled out by the common-gcd test. Endpoint support and menu minima would still need a separate proof.

### Repair C: add residue-breaking main labels

Add legal labels whose combined support generates all residues needed modulo `2^{r_n+1}`, while preserving numerical distinctness and the total term budget. A statement that the gcd is `1` is necessary but not by itself sufficient for short-window occupancy.

## What is not claimed

This theorem does not disprove the factorial half-range theorem, valuation tagging in general, target-dependent tilting in general, or the corrected versions above. It disproves only the exact frozen occupancy contract imported from Nova 1 at commit `b939574eb88a08bb03abda5bbe6ff2ca97444e08`.