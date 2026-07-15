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
- commit: `9febe46f2298d2726eeffa139676136963790019`
- handoff: `N1-HO-N3-002`

Closed by:

- N3-ANA-014, repaired menu lower bound and address legality;
- N3-ANA-015, repaired formal profile capacity;
- N3-ANA-016, rejection of the proposed central-binomial shortcut.

Response:

`handoffs/RESPONSE_TO_NOVA1_MARKER_THREE.md`.

### N3-REQ-N1-004, compact-tilt logarithmic reservoir

Status: `AVAILABLE_COMPONENT`

N3-ANA-012 supplies compact-tilt coarse logarithmic density for top-prime subset products. It is not a numerical additive theorem.

### N3-REQ-N1-005, deterministic endpoint and contraction interface

Status: `NEEDS_EXACT_TRANSITION_RANGE`

Nova 1 has proved:

- N1-STR-019, multiplicative 3-density of the odd factorial core;
- N1-STR-020, endpoint support crossing;
- N1-RED-006, deterministic coarse contraction.

Nova 1 and Nova 2 must state exactly which quotient targets these theorems remove from analytic responsibility and where the remaining analytic range begins.

## Nova 2 requirements

### N3-REQ-N2-001, bounded numerical torus contract

Status: `ACTIVE_MARKER_THREE_MODEL`

Active source:

- branch: `nova/additive-occupancy`
- commit: `fb73e6906105c983bacbd46a96ef8d5d87567fae`
- handoff: `N2-HO-N3-003`

The law is the exact numerical-value marker-three product law on `[-pi,pi]`.

The older `N2-HO-N3-002` three-power repair is a different model and is not the active contract for Nova 1 `N1-CON-003`.

### N3-REQ-N2-002, structural version compatibility

Status: `CLOSED`

N3-ANA-017 proves that the labels pinned at Nova 1 commit `ebb47ba436af554366d0f285119a769f31f9e561` are unchanged through latest inspected head `9febe46f2298d2726eeffa139676136963790019`. Only endpoint-support artifacts were added.

### N3-REQ-N2-003, tilt existence and centering

Status: `CLOSED`

N3-ANA-018 proves that for every

\[
W_n<q\le Y_n
\]

there is a unique finite tilt centered at

\[
q-W_n/2\in[q-W_n,q].
\]

### N3-REQ-N2-004, span and exact resonances

Status: `CLOSED`

N3-ANA-018 proves:

- exact additive span one;
- exact torus resonance set `{0}`;
- explicit all-frequency bound
  \[
  |\Phi_{n,\lambda}(\theta)|
  \le
  \exp(-2p_0p_1\sin^2(\theta/2)).
  \]

### N3-REQ-N2-005, uniform minor-arc decay over all tilts

Status: `CLOSED_NEGATIVELY`

N3-ANA-019 proves

\[
\sup_{\lambda\in\mathbb R}
|\Phi_{n,\lambda}(\theta)|=1
\]

for every fixed torus frequency. A bulk theorem requires compact tilt or an equivalent phase-dispersion lower bound.

### N3-REQ-N2-006, final analytic target range

Status: `OPEN_AND_BLOCKING`

Nova 2 must freeze the exact remaining targets after combining:

1. the deterministic binary-spine prefix;
2. Nova 1 coarse contraction;
3. endpoint support;
4. any deterministic transition interval.

The target range must have no gap and must be tied to exact branch and commit SHAs.

### N3-REQ-N2-007, moment and dispersion package

Status: `OPEN`

For the final analytic target range, prove or request:

- uniform variance lower and upper bounds;
- third absolute moment bounds;
- largest numerical step versus standard deviation;
- compact bounds on `lambda_{n,q}`, or direct lower bounds for enough active coordinate probabilities;
- exact endpoint exclusions.

### N3-REQ-N2-008, weighted Fourier inequality

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

Response to the current marker-three request:

`handoffs/RESPONSE_TO_NOVA2_MARKER_THREE.md`.

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
```

Return separate verdicts through N3-ANA-019.

### N3-REQ-N4-002, source audit reconstruction

Status: `OPEN`

Independently reconstruct N3-SRC-004 through N3-SRC-008.

### N3-REQ-N4-003, repaired capacity audit

Status: `OPEN`

Verify:

- the invalid central-binomial divisibility claim;
- the quotient-factorial replacement;
- exact threshold margins in N3-FIN-004.

### N3-REQ-N4-004, numerical-law foundations

Status: `OPEN`

Independently verify:

- strict monotonicity of the mean map;
- endpoint limits;
- span one;
- exact resonance set `{0}`;
- the explicit `p_0p_1` characteristic-function bound;
- endpoint-uniform minor-arc failure.

## Self-owned requirements

### N3-SELF-001 through N3-SELF-004

Status: `CLOSED`

Scale map, local ceiling, full-model non-Gaussian obstruction, and unrestricted minor-arc obstruction are complete.

### N3-SELF-005, matched numerical bounded-torus theorem

Status: `PARTIALLY_CLOSED`

N3-ANA-018 closes centering, span, and exact resonances. Moment bounds, quantitative dispersion, reference law, and strict weighted Fourier comparison remain open.

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

### N3-SELF-010, compact numerical tilt or dispersion theorem

Status: `OPEN`

After the exact analytic target range is frozen, prove a compact bound on `lambda_{n,q}` or a direct phase-dispersion lower bound sufficient for minor-arc integration.

## Rule

Do not solve an undefined stronger problem. Every theorem must name its exact labels, target range, endpoint exclusions, legal comparison direction, and receiving theorem node.