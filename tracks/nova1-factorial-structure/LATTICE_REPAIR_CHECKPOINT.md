# Nova 1 Lattice Repair Checkpoint

Date: 2026-07-15

Branch: `nova/factorial-structure`

Result status: mixed research checkpoint containing **proved theorems**, **conditional theorem**, **computational evidence**, and **disproved route**.

The factorial half-range theorem and Erdős Problem 18 remain open.

## Triggering cross-track result

Nova 2 rejected the first frozen valuation-tagged route by a deterministic lattice obstruction:

- branch: `nova/additive-occupancy`
- exact commit: `45c74a5fa747551422ffcad7d3ddf22788fbe622`
- theorem: `N2-ADD-115`
- disproved model: `N2-OBS-107`

The old main support lay in

\[
2^{r_n+1}\mathbb Z,
\]

while the correction radius was only

\[
2^{r_n}-1.
\]

The first requested target window contained no main sum. The old construction `N1-CON-001` is permanently retired.

## Repaired construction

The replacement is `N1-CON-003`, the marker-three valuation rainbow.

For

\[
X_n=\lfloor\sqrt{n!}\rfloor,
\quad
r_n=\lceil4\log n\rceil,
\quad
M_n=\lceil16(\log n)^2\rceil,
\]

set

\[
R_n=2^{r_n}-1,
\qquad
W_n=\left\lfloor\frac{R_n-2}{3}\right\rfloor.
\]

Layer `t` contains

\[
A_t^{(3)}(n)=
\left\{
3\cdot2^{t-1}u:
 u\text{ odd},\ 3u\mid n!,\ 3\cdot2^{t-1}u\le X_n
\right\}.
\]

The correction palette is

\[
\{1,2,4,\ldots,2^{r_n-1}\}.
\]

## Closed structural gates

### Divisor legality

Result label: **proved theorem**.

Every main term divides `n!` for all sufficiently large `n`.

### Numerical distinctness

Result label: **proved theorem**.

Layer `t` has exact 2-adic valuation `t-1`. Different layers cannot contain the same numerical divisor. Main terms are divisible by `3`; palette terms are not.

### Exact support lattice

Result label: **proved theorem**.

The main support generates exactly

\[
3\mathbb Z.
\]

The first layer contains `3`.

### Exact attained residues

Result label: **proved theorem**.

Palette subset sums attain residues `0`, `1`, and `2` modulo `3`. The correction radius exceeds every unresolved lattice residue gap.

### First-target coverage

Result label: **proved theorem**.

Targets with quotient `q<=W_n` satisfy `x<=R_n` and are represented directly by the palette.

### Quotient reduction

Result label: **proved theorem**.

If every integer quotient target

\[
W_n+1\le q\le\left\lfloor X_n/3\right\rfloor
\]

has a quotient rainbow sum in `[q-W_n,q]`, then

\[
H_{n!}(X_n+1)
\le
M_n+r_n.
\]

### Term cost

Result label: **proved theorem**.

The exact bound is

\[
\lceil16(\log n)^2\rceil+
\lceil4\log n\rceil.
\]

### Initial exact range

Result label: **proved theorem**.

For all sufficiently large `n`, every target through

\[
3m_n(2^{M_n}-1)+2
\]

is represented, where `m_n` is the largest odd integer at most `n`.

This range is only `exp(O((log n)^2))`, not the factorial half-range.

### Formal menu capacity

Result label: **proved theorem**.

Nova 3 supplied the prime interval theorem from:

- branch: `nova/analytic-density`
- exact commit: `e60069f797af878711e7a9d4abb1fb6188a1f724`
- theorem: `N3-ANA-010`

For every `n>=120368`,

\[
\pi(n)-\pi(n/2)
\ge
\frac{n}{3\log n}.
\]

Nova 1 proved for the repaired menus that

\[
|U_t(n)|
\ge
2^{\pi(n)-\pi(n/2)-1}
\]

and

\[
2^{r_n}
\prod_{t=1}^{M_n}(|U_t(n)|+1)
\ge X_n+1.
\]

This is profile capacity only.

## Computational evidence

The exact reduced-parameter verifier exhausts every quotient target for `7<=n<=14`.

Observed maximum downward quotient distance:

- `0` for `n=7`;
- `1` for every `8<=n<=14`.

The binary palette then reconstructs every original target through `X_n` in the tested domain.

Files:

- `verification/marker_three_sanity.py`
- `verification/MARKER_THREE_FINITE_REPORT.md`

Result label: **computational evidence**.

## Revised handoffs

- Nova 2: `N1-HO-N2-002`, exact quotient occupancy request.
- Nova 3: `N1-HO-N3-002`, independent repaired capacity reconstruction.
- Nova 4: `N1-HO-N4-002`, old-obstruction regression and repaired finite falsification.

## Exact remaining theorem

The active local theorem request is:

\[
\forall n\ge n_0,
\quad
\forall q\in
\left[W_n+1,\left\lfloor X_n/3\right\rfloor\right]
\cap\mathbb Z,
\]

\[
[q-W_n,q]
\cap
\Sigma_{\rm rb}
(B_1(n),\ldots,B_{M_n}(n))
\ne\varnothing.
\]

This theorem remains open.

The construction must be rejected if a persistent endpoint deficit, residue obstruction, collision collapse, or maximum downward gap larger than `W_n` is proved.
