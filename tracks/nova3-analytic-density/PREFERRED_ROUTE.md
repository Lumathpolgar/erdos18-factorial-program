# Preferred Analytic Route

## Route decision

- Decision ID: `N3-ROUTE-007`
- Status: `PROVED` as a route ranking and obstruction decision
- Final quotient occupancy: `OPEN`
- Date: 2026-07-16

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

The exact post-prefix target range is

\[
m_n(2^{M_n}-1)+W_n+1
\le q\le Y_n.
\]

Condition on `Z_1!=0` and define

\[
\widetilde Z_1=(Z_1-1)/2,
\qquad
\widetilde Z_t=Z_t/2
\quad(t>=2).
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

This remains the preferred final-only law.

### 2. Prefix control at the transformed dyadic ladder

Status: `NEXT_REQUIRED_COMPONENT`.

For

\[
\theta_j=\frac{\pi}{2^{j-1}},
\qquad
1\le j\le M_n-1,
\]

N3-ANA-026 proves

\[
\widetilde\Phi(\theta_j)
=
\left(
\prod_{t=1}^{j}
\widetilde\phi_t(\theta_j)
\right)
(2p_{j+1}^{(0)}-1),
\]

while every layer `t>=j+2` is exactly invisible.

N3-ANA-027 proves that for

\[
J_n=M_n-O(\log\log n),
\]

and every `j<=J_n`,

\[
|2p_{j+1}^{(0)}-1|
\ge
1-rac{4e}{m_n+1},
\]

and

\[
\sum_{t=j+1}^{M_n}
\widetilde{\mathcal D}_t(\theta_j)
\le
\frac{4e}{m_n+1}.
\]

Thus tail accumulation is not the active mechanism at the dyadic ladder. The next theorem must control

\[
\prod_{t=1}^{j}
\widetilde\phi_t(\theta)
\]

in neighborhoods of each `theta_j`.

Candidate forms:

1. quantitative residue spreading of the first `j` coordinates modulo `2^j`;
2. direct prefix characteristic decay;
3. a measure bound for weak-prefix neighborhoods;
4. a prefix residue concentration obstruction.

### 3. Exact transformed interval-kernel matching

Status: `COEQUAL_REQUIRED_COMPONENT`.

N3-ANA-028 proves

\[
v_2(|J_{n,q}|)\in\{0,1\}.
\]

The transformed interval kernel never vanishes at a reduced dyadic frequency of denominator at least `4`. At `pi`, it vanishes only when `rho_n` and `q` are both even.

The next prefix estimate must therefore be neighborhood-sensitive and quantitatively matched to the kernel. Exact pointwise nonvanishing alone is not an integral obstruction.

### 4. Non-dyadic transformed resonance audit

Status: `OPEN_REQUIRED_COMPONENT`.

Parity normalization and the dyadic ladder theorem do not classify all rational frequencies. A complete result must still identify:

- non-dyadic rational residue concentrations;
- approximate resonances;
- the final transformed major-arc set;
- the complementary transformed minor arcs.

### 5. Collision-aware transformed reference law

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

### 6. Transformed moment package

Status: `OPEN_REQUIRED_COMPONENT`.

Still required:

- transformed variance lower and upper bounds;
- transformed third absolute moments;
- largest transformed step versus standard deviation;
- exact endpoint exclusions.

### 7. Deterministic-to-analytic decomposition

Status: `CLOSED_INTERFACE_FOR_CURRENT_CONTRACT`.

Nova 2 covers every quotient target through

\[
P_n=m_n(2^{M_n}-1)+W_n.
\]

The final-only transformed law is responsible for every later target through `Y_n`.

Finite exact marker-three coverage reaches `12<=n<=52`, but these computations do not prove the asymptotic theorem.

### 8. Sequential connected-core route

Status: `USEFUL_FINITE_ENGINE_WITH_ASYMPTOTIC_RESTRICTIONS`.

Nova 1 and Nova 2 have exact streaming and meet-in-the-middle engines through `n=52` and a necessary connected-prefix entropy condition.

This remains a finite and conditional asymptotic engine. It is not substituted for the final-only transformed Fourier route.

### 9. Repaired marker-three capacity

Status: `PROVED_SUPPORTING_ROUTE`.

N3-ANA-014 and N3-ANA-015 prove legal menus and formal capacity for every `n>=120368`.

Capacity is not occupancy.

### 10. Compact top-prime logarithmic reservoir

Status: `PROVED_INTRINSIC_COMPONENT`.

N3-ANA-012 gives compact-tilt coarse logarithmic density for exact top-prime subset products. It does not transfer directly to numerical quotient sums.

## Rejected or disproved routes

### Old power-of-two address construction

Status: `DISPROVED_BY_NOVA_2`.

### Uniform all-tilt numerical minor-arc gap

Status: `DISPROVED_BY_N3-ANA-019`.

### One binary anchor under compact tilt

Status: `DISPROVED_BY_N3-ANA-021`.

### Unnormalized zero-only major-arc partition

Status: `DISPROVED_BY_N3-ANA-023`.

### Parity-blind reference law

Status: `REJECTED_BY_N3-ANA-024`.

### Many-tail-layers transformed dispersion

Status: `DISPROVED_BY_N3-ANA-026_AND_N3-ANA-027`.

At each transformed dyadic ladder point, all layers after the matching layer are exactly invisible and the matching layer is almost a pure sign through all but `O(log log n)` top scales.

### Exact transformed-kernel cancellation of the dyadic ladder

Status: `DISPROVED_BY_N3-ANA-028`.

The transformed window length has 2-adic valuation at most one, so no reduced dyadic frequency of denominator at least `4` is a kernel zero.

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
- assumes later transformed layers accumulate dispersion at dyadic ladder points;
- assumes the transformed interval kernel cancels denominator `4` or higher dyadic points;
- assumes exact span one gives quantitative dispersion;
- ignores collision multiplicity;
- uses Berry-Esseen distribution distance as a constant-width local theorem;
- presents finite connected-core success as an asymptotic final-only proof.

## Next theorem target

`N3-NEXT-008`: prove a target-uniform prefix-residue or prefix-characteristic estimate in neighborhoods of every transformed dyadic ladder frequency, matched to the exact transformed interval kernel. If this fails, return the first exact prefix residue concentration or target-local additive-energy obstruction.