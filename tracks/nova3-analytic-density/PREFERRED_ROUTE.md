# Preferred Analytic Route

## Route decision

- Decision ID: `N3-ROUTE-006`
- Status: `PROVED` as a route ranking and obstruction decision
- Final quotient occupancy: `OPEN`
- Date: 2026-07-15

## Mandatory model distinction

The active cross-track object is the numerical marker-three quotient law

\[
\mathbb E e^{i\theta T_n},
\qquad
\theta\in[-\pi,\pi].
\]

It is not the logarithmic divisor characteristic function

\[
\mathbb E e^{it\log d}.
\]

## Ranked routes

### 1. Exact odd-lattice normalized marker-three law

Status: `ACTIVE_CROSS_TRACK_ROUTE`.

Exact sources:

- Nova 1: `nova/factorial-structure@1b81ec74f907d57d520bcf6c51f2e6e71f0474a7`;
- Nova 2: `nova/additive-occupancy@e443674f86b2ee3c7037ac94ee47f6b8a4b3b29f`;
- active contract: `N2-HO-N3-003`.

The unnormalized supports are

\[
B_t(n)=
\{2^{t-1}u:u\text{ odd},\ 3u\mid n!,\ 2^{t-1}u\le Y_n\}.
\]

The exact post-prefix target range is

\[
m_n(2^{M_n}-1)+W_n+1
\le q\le Y_n.
\]

Closed foundations:

- unique finite centering tilt, N3-ANA-018;
- uniform post-prefix tilt compression, N3-ANA-020;
- exact collision factor in atoms, N3-ANA-022;
- exact parity twin obstruction, N3-ANA-023;
- parity mismatch restriction on reference laws, N3-ANA-024;
- exact odd-lattice normalization, N3-ANA-025.

Condition on `Z_1!=0` and define

\[
\widetilde Z_1=(Z_1-1)/2,
\qquad
\widetilde Z_t=Z_t/2\quad(t>=2).
\]

Then

\[
\widetilde T=(T-1)/2
\]

under the odd conditional law. The transformed coordinates remain independent, share exact tilt `2 lambda`, and have exact span one.

The transformed target interval is

\[
J_{n,q}
=
\left[
\left\lceil\frac{q-W_n-1}{2}\right\rceil,
\left\lfloor\frac{q-1}{2}\right\rfloor
\right]\cap\mathbb Z.
\]

This is now the preferred final-only law.

### 2. Complete transformed resonance audit

Status: `NEXT_REQUIRED_COMPONENT`.

Parity normalization removes the forced `pi` twin from the original law, but it does not prove all transformed rational or dyadic resonances are harmless.

The next theorem must:

1. identify every exact and approximate transformed secondary resonance;
2. determine transformed residue concentration modulo small integers;
3. freeze all transformed major arcs;
4. define the complementary transformed minor arcs.

### 3. Aggregate transformed phase dispersion

Status: `OPEN_REQUIRED_COMPONENT`.

For transformed coordinate probabilities, define

\[
\widetilde{\mathcal D}_{t,\lambda}(\theta)
=
\sum_{a,b}
\widetilde p_t(a)\widetilde p_t(b)
\sin^2\left(\frac{(a-b)\theta}{2}\right).
\]

Then

\[
|\widetilde\Phi_{n,\lambda}(\theta)|^2
\le
\exp\left(
-2\sum_t
\widetilde{\mathcal D}_{t,\lambda}(\theta)
\right).
\]

A successful route may prove a pointwise lower bound, a measure bound for weak-dispersion frequencies, or a weighted integral estimate.

### 4. Collision-aware transformed reference law

Status: `COEQUAL_REQUIRED_COMPONENT`.

For numerical fiber multiplicity `C_n(s)`, the exact atom is

\[
P_\lambda(T=s)
=
\frac{C_n(s)e^{\lambda s}}
{\prod_tZ_t(\lambda)}.
\]

A final local theorem must:

- retain collision multiplicity in the reference law;
- or prove target-local upper fiber bounds;
- or control transformed additive energy;
- or prove collision concentration is negligible relative to transformed window mass.

### 5. Deterministic-to-analytic decomposition

Status: `CLOSED_INTERFACE_FOR_CURRENT_CONTRACT`.

Nova 2 covers every quotient target through

\[
P_n=m_n(2^{M_n}-1)+W_n.
\]

The final-only transformed law is responsible for every later target through `Y_n`.

Finite exact marker-three coverage now reaches `12<=n<=52`, but these computations do not prove the asymptotic theorem.

### 6. Sequential connected-core route

Status: `USEFUL_FINITE_ENGINE_WITH_ASYMPTOTIC_RESTRICTIONS`.

Nova 1 and Nova 2 have exact streaming and meet-in-the-middle engines through `n=52` and a necessary connected-prefix entropy condition.

This remains a finite and conditional asymptotic engine. It is not substituted for the final-only transformed Fourier route.

### 7. Repaired marker-three capacity

Status: `PROVED_SUPPORTING_ROUTE`.

N3-ANA-014 and N3-ANA-015 prove legal menus and formal capacity for every `n>=120368`.

Capacity is not occupancy.

### 8. Compact top-prime logarithmic reservoir

Status: `PROVED_INTRINSIC_COMPONENT`.

N3-ANA-012 gives compact-tilt coarse logarithmic density for exact top-prime subset products. It does not transfer directly to numerical quotient sums.

### 9. Fine top-prime logarithmic local analysis

Status: `OPEN_BUT_SECONDARY`.

## Rejected or disproved routes

### Old power-of-two address construction

Status: `DISPROVED_BY_NOVA_2`.

### Uniform all-tilt numerical minor-arc gap

Status: `DISPROVED_BY_N3-ANA-019`.

### One binary anchor under compact tilt

Status: `DISPROVED_BY_N3-ANA-021`.

### Unnormalized zero-only major-arc partition

Status: `DISPROVED_BY_N3-ANA-023`.

At `pi`,

\[
|\Phi(\pi)|\to1
\]

uniformly over the post-prefix target range.

### Parity-blind reference law

Status: `REJECTED_BY_N3-ANA-024`.

### Profile injectivity

Status: `DISPROVED_BY_N1-COL-001`.

### Full logarithmic Gaussian model

Status: `DISPROVED_BY_N3-ANA-006`.

### Unrestricted logarithmic minor-arc decay

Status: `DISPROVED_BY_N3-ANA-007`.

### Smooth-number lower-bound transfer

Status: `REJECTED`.

## Stop conditions

Abandon or repair any proposed theorem if it:

- analyzes `log d` instead of numerical quotient values;
- ignores the exact post-prefix boundary;
- ignores the original parity twin at `pi`;
- assumes odd-lattice normalization removes every transformed resonance;
- assumes exact span one gives quantitative dispersion;
- ignores collision multiplicity;
- uses Berry-Esseen distribution distance as a constant-width local theorem;
- presents finite connected-core success as an asymptotic final-only proof.

## Next theorem target

`N3-NEXT-007`: perform the complete resonance audit for the exact odd-lattice normalized product law. Prove aggregate transformed dispersion or a weighted transformed integral estimate outside every genuine transformed major arc, or return the first exact transformed residue concentration that blocks the route.
