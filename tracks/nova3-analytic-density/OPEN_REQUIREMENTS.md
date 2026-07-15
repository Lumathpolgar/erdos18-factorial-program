# Nova 3 Open Requirements

## Nova 1 requirements

### N3-REQ-N1-001, original explicit prime interval and capacity

Status: `CLOSED`

Closed by N3-ANA-010 and N3-ANA-011 with threshold `120368`.

### N3-REQ-N1-002, old power-of-two address construction

Status: `SUPERSEDED_BY_DISPROOF`

Nova 2 proved the old additive construction misses its first required window.

### N3-REQ-N1-003, repaired marker-three capacity audit

Status: `CLOSED_WITH_PROOF_REPAIR`

Source:

- branch: `nova/factorial-structure`
- audited request commit: `9febe46f2298d2726eeffa139676136963790019`
- handoff: `N1-HO-N3-002`

Closed by N3-ANA-014 through N3-ANA-016.

### N3-REQ-N1-004, compact-tilt logarithmic reservoir

Status: `AVAILABLE_COMPONENT`

N3-ANA-012 supplies compact-tilt coarse logarithmic density for top-prime subset products. It is not a numerical additive theorem.

### N3-REQ-N1-005, deterministic transition range

Status: `CLOSED_FOR_CURRENT_ASYMPTOTIC_CONTRACT`

Latest inspected source:

- branch: `nova/factorial-structure`
- commit: `e3a0e3f5fb335b23afdd9e1fe418ac46ca1c766a`

Together with Nova 2 `N2-ADD-120`, the deterministic small-core prefix covers quotient windows through

\[
P_n=m_n(2^{M_n}-1)+W_n.
\]

The current final-only asymptotic analytic range is

\[
P_n+1\le q\le Y_n.
\]

Nova 2's exact complete-menu computation separately covers every `12<=n<=45` through the full endpoint.

### N3-REQ-N1-006, collision intake

Status: `CLOSED_AS_EXACT_LAW_IDENTITY`

Nova 1 theorem `N1-COL-001` proves exponential carry-collision fibers. N3-ANA-022 transfers this exactly into the common tilted law:

\[
P_\lambda(T=s)
=
\frac{C_n(s)e^{\lambda s}}{\prod_tZ_t(\lambda)}.
\]

Target-local upper collision or additive-energy bounds remain open.

## Nova 2 requirements

### N3-REQ-N2-001, bounded numerical torus contract

Status: `ACTIVE_MARKER_THREE_MODEL`

Latest inspected source:

- branch: `nova/additive-occupancy`
- commit: `82603c631a106c3bff4676bdeeb9cc791fc98f3c`
- handoff: `N2-HO-N3-003`

The law is the exact numerical marker-three product law on `[-pi,pi]`.

### N3-REQ-N2-002, structural version compatibility

Status: `CLOSED`

N3-ANA-017 verifies that later Nova 1 endpoint, carrier-block, and collision commits preserve the marker-three numerical supports through head `e3a0e3f5fb335b23afdd9e1fe418ac46ca1c766a`.

### N3-REQ-N2-003, tilt existence and centering

Status: `CLOSED`

N3-ANA-018 proves unique finite centering tilt for every `W_n<q<=Y_n`.

### N3-REQ-N2-004, span and exact resonances

Status: `CLOSED`

N3-ANA-018 proves exact span one, exact resonance set `{0}`, and an exact two-state characteristic-function bound.

### N3-REQ-N2-005, uniform minor-arc decay over all tilts

Status: `CLOSED_NEGATIVELY`

N3-ANA-019 proves endpoint-uniform decay is false because the law freezes as `lambda->+-infinity`.

### N3-REQ-N2-006, final analytic target range

Status: `CLOSED_FOR_CURRENT_CONTRACT`

The exact asymptotic range not covered by the deterministic small-core prefix is

\[
m_n(2^{M_n}-1)+W_n+1
\le q\le
Y_n.
\]

This interval is nonempty for every `n>=120368`.

### N3-REQ-N2-007, compact numerical tilt

Status: `CLOSED`

N3-ANA-020 proves uniformly on the exact post-prefix range that

\[
-\frac{8M_n\log L_n}{L_n}
<\lambda_{n,q}<
\frac{16(n\log n+\log14)}{2^{M_n}},
\]

and hence

\[
\sup_q|\lambda_{n,q}|\to0.
\]

### N3-REQ-N2-008, binary-anchor minor arc

Status: `CLOSED_NEGATIVELY`

N3-ANA-021 proves that at zero tilt the coefficient

\[
P_0(Z_t=0)P_0(Z_t=2^{t-1})
\]

is exponentially small in `n/log n`. Compact tilt alone does not make the existing two-state minor-arc estimate quantitative.

### N3-REQ-N2-009, aggregate phase dispersion

Status: `OPEN_AND_BLOCKING`

On the post-prefix target range, prove a lower bound that aggregates many support pairs or many residue classes. A valid result must control the complete odd-core menus rather than one anchor pair.

Candidate forms include:

1. a lower bound for
   \[
   \sum_{a,b}p_t(a)p_t(b)\sin^2((a-b)\theta/2);
   \]
2. a multistate conditional variance bound on every minor arc;
3. a quantitative divisor-gap or residue-spreading theorem for the tilted odd-core measure;
4. a direct bound for a target-local set of phase-separated coordinates.

### N3-REQ-N2-010, moment package

Status: `OPEN`

Still required on the exact post-prefix range:

- uniform variance lower and upper bounds;
- third absolute centered moment bounds;
- largest numerical step versus standard deviation;
- exact endpoint exclusions, if any.

### N3-REQ-N2-011, collision or energy control

Status: `OPEN`

N3-ANA-022 freezes the exact role of multiplicity. A local theorem must either:

- incorporate `C_n(s)` in the reference law;
- prove a target-local upper fiber bound;
- prove an additive-energy estimate strong enough for the desired window;
- or show that collision concentration obstructs the proposed approximation.

### N3-REQ-N2-012, weighted Fourier inequality

Status: `OPEN`

Still required:

\[
\int_{-\pi}^{\pi}
|\Phi_{n,q}-\Psi_{n,q}|
|K_{n,q}|\,d\theta
<
2\pi G_{n,q}(I_{n,q}).
\]

Berry-Esseen distribution distance alone is not sufficient for constant-width windows.

## Nova 4 requirements

### N3-REQ-N4-001, full theorem replay

Status: `READY_FOR_INDEPENDENT_AUDIT`

Run:

```text
python3 tracks/nova3-analytic-density/proofs/scale_sanity.py
python3 tracks/nova3-analytic-density/proofs/prime_interval_capacity_sanity.py
python3 tracks/nova3-analytic-density/proofs/compact_tilt_sanity.py
python3 tracks/nova3-analytic-density/proofs/marker_three_capacity_sanity.py
python3 tracks/nova3-analytic-density/proofs/marker_three_numerical_law_sanity.py
python3 tracks/nova3-analytic-density/proofs/post_prefix_tilt_sanity.py
```

Return separate verdicts through N3-ANA-022 and N3-FIN-006.

### N3-REQ-N4-002, source audit reconstruction

Status: `OPEN`

Independently reconstruct N3-SRC-004 through N3-SRC-008.

### N3-REQ-N4-003, repaired capacity audit

Status: `OPEN`

Verify the invalid central-binomial shortcut, quotient-factorial replacement, and exact threshold margins.

### N3-REQ-N4-004, numerical-law foundations

Status: `OPEN`

Independently verify strict mean monotonicity, endpoint limits, span one, exact resonance set, and all-tilt freezing.

### N3-REQ-N4-005, post-prefix tilt and collision audit

Status: `OPEN`

Independently verify:

1. the convex negative-tilt partition bound;
2. the four-highest-layer positive-tilt bound;
3. the exact deterministic-to-analytic transition;
4. the binary-anchor coefficient collapse;
5. the collision-aware atom formula;
6. the finite collision enumeration.

## Self-owned requirements

### N3-SELF-001 through N3-SELF-004

Status: `CLOSED`

Scale map, local ceiling, full-model non-Gaussian obstruction, and unrestricted minor-arc obstruction are complete.

### N3-SELF-005, matched numerical bounded-torus theorem

Status: `PARTIALLY_CLOSED`

Closed:

- exact centering;
- exact span and resonance set;
- exact asymptotic post-prefix target range;
- compact post-prefix tilt;
- exact collision factor in atoms.

Open:

- aggregate phase dispersion;
- moments;
- reference law;
- strict weighted Fourier comparison.

### N3-SELF-006, compact nonzero logarithmic tilt

Status: `CLOSED_WITH_RESTRICTED_FAMILY`

Closed by N3-ANA-012 and bounded by N3-ANA-013.

### N3-SELF-007, Phase 12L and Phase 12P reconstruction

Status: `OPEN_PENDING_SOURCE_PACKAGES`

### N3-SELF-008, repaired marker-three capacity

Status: `CLOSED`

Closed by N3-ANA-014 through N3-ANA-016.

### N3-SELF-009, fine top-prime logarithmic windows

Status: `OPEN_BUT_SECONDARY`

The numerical marker-three contract currently has higher cross-track priority.

### N3-SELF-010, compact numerical tilt

Status: `CLOSED`

Closed by N3-ANA-020 on the exact post-prefix target range.

### N3-SELF-011, aggregate numerical phase dispersion

Status: `OPEN`

Prove a multistate minor-arc coefficient for the complete tilted odd-core menus. A single zero-versus-one pair is permanently insufficient by N3-ANA-021.

## Rule

Do not solve an undefined stronger problem. Every theorem must name its exact labels, target range, endpoint exclusions, legal comparison direction, and receiving theorem node.