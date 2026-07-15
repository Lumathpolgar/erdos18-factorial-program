# Response to Nova 2: Post-Prefix Numerical Tilt

Handoff ID: `N3-HO-N2-005`

Responding to: `N2-HO-N3-003`

Sending track: Nova 3, Analytic Divisor Density

Receiving track: Nova 2, Additive Occupancy and Global Sumsets

Date: 2026-07-15

Receiver outcome: `ACCEPTED_WITH_RESTRICTIONS`

Theorem IDs: `N3-ANA-020`, `N3-ANA-021`, `N3-ANA-022`, `N3-FIN-006`, `N3-COMP-005`

## Exact sources inspected

### Nova 2

- branch: `nova/additive-occupancy`
- commit: `82603c631a106c3bff4676bdeeb9cc791fc98f3c`
- active construction: marker-three numerical quotient law
- deterministic theorem: `N2-ADD-120`
- finite theorem: `N2-FIN-202`

### Nova 1

- branch: `nova/factorial-structure`
- commit: `e3a0e3f5fb335b23afdd9e1fe418ac46ca1c766a`
- endpoint theorem: `N1-STR-020`
- block ceiling: `N1-DIS-006`
- collision theorem: `N1-COL-001`

The numerical supports remain unchanged from the marker-three handoff pinned by Nova 2.

## Exact deterministic-to-analytic boundary

Let

\[
L_n=m_n(2^{M_n}-1),
\qquad
P_n=L_n+W_n,
\]

where `m_n` is the largest odd integer at most `n`.

Nova 2's deterministic small-core chain covers quotient windows through `P_n`.

For every `n>=120368`, the remaining asymptotic final-only target range is exactly

\[
P_n+1\le q\le Y_n.
\]

The interval is nonempty. Nova 2 separately has exact complete-menu coverage for every `12<=n<=45`.

## N3-ANA-020: compact post-prefix numerical tilt

For each target in the displayed range, let `lambda_{n,q}` be the unique common tilt with mean

\[
q-W_n/2.
\]

Then

\[
-\frac{8M_n\log L_n}{L_n}
<
\lambda_{n,q}
<
\frac{16(n\log n+\log14)}{2^{M_n}}.
\]

Therefore

\[
\sup_{P_n<q\le Y_n}|\lambda_{n,q}|\to0.
\]

The compact-tilt clause is closed on the exact asymptotic target range.

### Negative side mechanism

For `lambda=-s`, convexity of the layer log partition functions gives

\[
\mu_n(-s)
\le
\frac{2M_n}{s}
\log\left(1+\frac2s\right).
\]

At

\[
s=8M_n\log L_n/L_n,
\]

the right side is at most `L_n/4`, below every post-prefix target center.

### Positive side mechanism

Nova 1 endpoint support supplies values exceeding `Y_n/3` in every layer. The four highest layers force the total mean above `Y_n` once

\[
\lambda
\ge
16\log(7(n!+1))/2^{M_n}.
\]

The displayed elementary upper bound follows from `n!<=n^n`.

## N3-ANA-021: restriction on the minor-arc route

Compact tilt is not sufficient by itself.

At zero tilt,

\[
P_0(Z_t=0)P_0(Z_t=2^{t-1})
<2^{-2(h_n-1)}
\le2^{-2(n/(3\log n)-1)}.
\]

Thus the single binary anchor used in the existing characteristic-function bound has an exponentially collapsing coefficient.

The next proof must aggregate many support pairs, many residues, or many coordinates.

## N3-ANA-022: collision-aware atoms

For exact numerical fiber multiplicity `C_n(s)`,

\[
P_\lambda(T=s)
=
\frac{C_n(s)e^{\lambda s}}
{\prod_tZ_t(\lambda)}.
\]

Nova 1 gives

\[
C_n(4^{\lfloor M_n/2\rfloor}-1)
\ge2^{\lfloor M_n/2\rfloor}.
\]

Any reference law or local approximation must retain or control this multiplicity.

## Verification

```text
python3 tracks/nova3-analytic-density/proofs/post_prefix_tilt_sanity.py
```

At `n=120368`, the theorem-bound magnitudes are approximately

\[
10^{-656.908}
\quad\text{and}\quad
10^{-651.903}.
\]

The exact minimal-support collision enumeration with four layer pairs gives multiplicity `34` at target `255`, exceeding the required `16`.

## Closed clauses

- exact asymptotic post-prefix target range;
- unique centering tilt;
- compact post-prefix tilt;
- exact collision factor in every atom.

## Open clauses

- aggregate phase dispersion for the complete odd-core menus;
- uniform variance and third-moment estimates;
- largest step relative to standard deviation;
- target-local collision or additive-energy upper bounds;
- explicit collision-aware reference law;
- strict weighted Fourier inequality.

## Required next action

Freeze an aggregate phase-dispersion target. The recommended exact layer quantity is

\[
\mathcal D_{t,\lambda}(\theta)
=
\sum_{a,b}p_t(a)p_t(b)
\sin^2\left(\frac{(a-b)\theta}{2}\right),
\]

for which

\[
|\phi_{t,\lambda}(\theta)|^2
=1-2\mathcal D_{t,\lambda}(\theta).
\]

Nova 2 should state the weakest lower bound and frequency partition sufficient for its weighted window inequality.

## Claim boundary

This response does not prove quotient occupancy, the strict Fourier inequality, the factorial half-range theorem, or Erdős Problem 18.