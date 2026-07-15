# Preferred Analytic Route

## Route decision

- Decision ID: `N3-ROUTE-005`
- Status: `PROVED` as a route ranking and obstruction decision; the final occupancy theorem remains `OPEN`
- Date: 2026-07-15

## Mandatory model distinction

Two Fourier objects remain separate:

1. logarithmic divisor size,
   \[
   \mathbb E e^{it\log d};
   \]
2. numerical marker-three quotient occupancy,
   \[
   \mathbb E e^{itT_n}.
   \]

The active cross-track target is the second object.

## Ranked routes

### 1. Aggregate phase dispersion for the marker-three numerical law

Status: `ACTIVE_CROSS_TRACK_ROUTE`.

Exact sources:

- Nova 1 branch `nova/factorial-structure`, commit `e3a0e3f5fb335b23afdd9e1fe418ac46ca1c766a`;
- Nova 2 branch `nova/additive-occupancy`, commit `82603c631a106c3bff4676bdeeb9cc791fc98f3c`;
- active handoff `N2-HO-N3-003`.

The supports are

\[
B_t(n)=
\{2^{t-1}u:u\text{ odd},\ 3u\mid n!,\ 2^{t-1}u\le Y_n\}.
\]

The exact post-prefix analytic range is

\[
m_n(2^{M_n}-1)+W_n+1
\le q\le Y_n.
\]

Closed foundations:

- unique finite centering tilt, N3-ANA-018;
- exact span one and exact resonance set `{0}`, N3-ANA-018;
- all-tilt endpoint freezing obstruction, N3-ANA-019;
- uniform post-prefix tilt compression `lambda_{n,q}->0`, N3-ANA-020;
- exact collision factor in every atom, N3-ANA-022.

The remaining positive route must aggregate many support pairs or residue classes. A single zero-versus-minimum anchor is insufficient by N3-ANA-021.

Candidate analytic quantity:

\[
\mathcal D_{t,\lambda}(\theta)
=
\sum_{a,b}
P_\lambda(Z_t=a)P_\lambda(Z_t=b)
\sin^2\left(\frac{(a-b)\theta}{2}\right).
\]

Since

\[
|\phi_{t,\lambda}(\theta)|^2
=1-2\mathcal D_{t,\lambda}(\theta),
\]

a lower bound for the aggregate dispersion over enough layers yields a product minor-arc estimate.

### 2. Collision-aware target-local reference law

Status: `COEQUAL_REQUIRED_COMPONENT`.

For profile multiplicity `C_n(s)`, N3-ANA-022 proves

\[
P_\lambda(T=s)
=
\frac{C_n(s)e^{\lambda s}}
{\prod_tZ_t(\lambda)}.
\]

Nova 1 proves explicit fibers of size at least

\[
2^{\lfloor M_n/2\rfloor}.
\]

A final local theorem must therefore do one of the following:

1. retain `C_n(s)` in the reference law;
2. prove a target-local upper fiber bound;
3. control additive energy in every required window;
4. prove that the collision contribution is negligible relative to the reference mass.

Raw profile entropy is not a numerical local law.

### 3. Deterministic-to-analytic quotient decomposition

Status: `CLOSED_INTERFACE_FOR_CURRENT_CONTRACT`.

Nova 2's small-core chain covers through

\[
P_n=m_n(2^{M_n}-1)+W_n.
\]

The final-only analytic law is responsible for every target from `P_n+1` through `Y_n`. Nova 2's exact full-menu computation separately closes every `12<=n<=45`.

### 4. Repaired marker-three capacity

Status: `PROVED_SUPPORTING_ROUTE`.

N3-ANA-014 and N3-ANA-015 prove legal repaired menus and formal capacity for every `n>=120368`.

The proof uses

\[
n!/H_n\ge\lfloor n/2\rfloor!
\]

rather than the false central-binomial divisibility shortcut rejected by N3-ANA-016.

Capacity does not imply occupancy.

### 5. Sequential connected-core carrier route

Status: `USEFUL_FINITE_ENGINE_WITH_ASYMPTOTIC_RESTRICTIONS`.

Nova 2 `N2-ADD-120` gives an exact sufficient recursion and proves full finite coverage through `n=45`.

Nova 1 `N1-DIS-006` shows that using only one factorial arithmetic block per layer reaches at most

\[
\exp(O((\log n)^3)),
\]

far below the factorial endpoint. This does not disprove the complete connected core, but it prevents promotion of the restricted block-only engine.

### 6. Compact-tilt top-prime logarithmic reservoir

Status: `PROVED_INTRINSIC_COMPONENT`.

N3-ANA-012 gives a Gaussian coarse-window theorem for exact top-prime subset products under `|theta|<=theta_0<1`. N3-ANA-013 proves failure at unit tilt.

This route remains useful for intrinsic divisor density but does not transfer directly to the numerical quotient law.

### 7. Fine top-prime logarithmic local analysis

Status: `OPEN_BUT_SECONDARY`.

Lowering the current `K_A log n` width remains valid, but the marker-three numerical contract has higher integration priority.

## Rejected or disproved routes

### Old power-of-two address construction

Status: `DISPROVED_BY_NOVA_2`.

### Uniform all-tilt minor-arc modulus gap

Status: `DISPROVED_BY_N3-ANA-019`.

### Compact tilt automatically bounds one anchor pair

Status: `DISPROVED_BY_N3-ANA-021`.

At zero tilt the anchor coefficient is exponentially small because every layer menu is exponentially large.

### Profile injectivity

Status: `DISPROVED_BY_N1-COL-001`.

### Full logarithmic Gaussian model

Status: `DISPROVED_BY_N3-ANA-006`.

### Unrestricted logarithmic minor-arc decay

Status: `DISPROVED_BY_N3-ANA-007`.

### Smooth-number lower-bound transfer

Status: `REJECTED`.

## Exact current deliverable

For the active numerical marker-three law, Nova 3 now provides:

1. exact post-prefix target range;
2. unique target-dependent centering;
3. uniform shrinking numerical tilt;
4. exact lattice span and resonance set;
5. exact endpoint-uniform obstruction;
6. exact collision-aware atom formula;
7. proof that one binary anchor is quantitatively inadequate.

The strict weighted Fourier inequality remains open.

## Stop conditions

Abandon or weaken any proposed next step if it:

- uses logarithmic divisor weights instead of numerical quotient values;
- ignores the exact post-prefix boundary;
- assumes span one gives quantitative minor-arc decay;
- assumes `lambda->0` gives fixed state probabilities;
- ignores carry-collision multiplicities;
- uses Berry-Esseen distribution distance as a constant-width local theorem;
- treats formal profile capacity as numerical sumset coverage;
- proves only a sequential block theorem and presents it as final-only occupancy.

## Next theorem target

`N3-NEXT-006`: prove an aggregate phase-dispersion lower bound for the complete tilted odd-core menus on the post-prefix range. Start from the exact multistate identity for `|phi_t(theta)|^2`, exploit many core differences or residue classes, and retain collision multiplicities. If this fails, produce an explicit target-local concentration or additive-energy obstruction.