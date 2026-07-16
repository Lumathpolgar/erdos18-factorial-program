# Nova 3 Open Requirements

## Nova 1 requirements

### N3-REQ-N1-001, original explicit prime interval and capacity

Status: `CLOSED`

Closed by N3-ANA-010 and N3-ANA-011 with threshold `120368`.

### N3-REQ-N1-002, old power-of-two address construction

Status: `SUPERSEDED_BY_DISPROOF`

Nova 2 proved the old construction misses its first required window.

### N3-REQ-N1-003, repaired marker-three capacity

Status: `CLOSED_WITH_PROOF_REPAIR`

Closed by N3-ANA-014 through N3-ANA-016.

### N3-REQ-N1-004, compact logarithmic reservoir

Status: `AVAILABLE_COMPONENT`

N3-ANA-012 supplies compact-tilt logarithmic density for top-prime subset products. It is not a numerical additive theorem.

### N3-REQ-N1-005, deterministic transition range

Status: `CLOSED_FOR_CURRENT_ASYMPTOTIC_CONTRACT`

The deterministic marker-three prefix covers through

\[
P_n=m_n(2^{M_n}-1)+W_n.
\]

The current final-only asymptotic range is

\[
P_n+1\le q\le Y_n.
\]

Latest inspected structural head:

`nova/factorial-structure@1b81ec74f907d57d520bcf6c51f2e6e71f0474a7`.

### N3-REQ-N1-006, collision intake

Status: `CLOSED_AS_EXACT_LAW_IDENTITY`

N3-ANA-022 gives

\[
P_\lambda(T=s)
=
\frac{C_n(s)e^{\lambda s}}{\prod_tZ_t(\lambda)}.
\]

Target-local upper collision or additive-energy bounds remain open.

## Nova 2 requirements

### N3-REQ-N2-001, active bounded numerical torus contract

Status: `ACTIVE_MARKER_THREE_MODEL`

Latest inspected source:

- branch: `nova/additive-occupancy`
- commit: `e443674f86b2ee3c7037ac94ee47f6b8a4b3b29f`
- handoff: `N2-HO-N3-003`

### N3-REQ-N2-002, structural compatibility

Status: `CLOSED`

The exact marker-three numerical labels remain unchanged through the latest inspected Nova 1 and Nova 2 heads.

### N3-REQ-N2-003, tilt existence and centering

Status: `CLOSED`

N3-ANA-018 proves unique finite centering tilt for every `W_n<q<=Y_n`.

### N3-REQ-N2-004, exact span and modulus-one resonances

Status: `CLOSED`

N3-ANA-018 proves exact span one and exact modulus-one resonance set `{0}`.

### N3-REQ-N2-005, all-tilt minor-arc gap

Status: `CLOSED_NEGATIVELY`

N3-ANA-019 proves endpoint freezing prevents a fixed gap over all real tilts.

### N3-REQ-N2-006, exact final analytic range

Status: `CLOSED_FOR_CURRENT_CONTRACT`

\[
m_n(2^{M_n}-1)+W_n+1
\le q\le Y_n.
\]

### N3-REQ-N2-007, compact numerical tilt

Status: `CLOSED`

N3-ANA-020 proves

\[
\sup_q|\lambda_{n,q}|\to0
\]

uniformly on the exact post-prefix range.

### N3-REQ-N2-008, binary-anchor minor arc

Status: `CLOSED_NEGATIVELY`

N3-ANA-021 proves the zero-versus-minimum-state coefficient is exponentially small at zero tilt.

### N3-REQ-N2-009, unnormalized aggregate dispersion outside zero

Status: `CLOSED_NEGATIVELY`

N3-ANA-023 proves the unnormalized characteristic function has a secondary near-resonance at `pi`:

\[
|\Phi(\pi)|
\ge
1-rac{4e^{\varepsilon_n}}{m_n+1}
\to1.
\]

The exact aggregate dispersion at `pi` tends to zero. A minor arc containing `pi` cannot have a fixed positive dispersion lower bound.

### N3-REQ-N2-010, parity-aware reference law

Status: `CLOSED_AS_RESTRICTION`

N3-ANA-024 proves

\[
d_{TV}(\mathcal L(T),G)
\ge
|G(2\mathbb Z)-P(T\text{ even})|.
\]

Any reference law must match the asymptotic odd-parity concentration or explicitly include the `pi` major arc.

### N3-REQ-N2-011, exact odd-lattice normalization

Status: `CLOSED`

N3-ANA-025 proves that conditioning on `Z_1!=0`, subtracting one, and dividing by two gives an independent integer product law with common tilt `2 lambda` and exact span one.

The transformed interval is

\[
J_{n,q}
=
\left[
\left\lceil\frac{q-W_n-1}{2}\right\rceil,
\left\lfloor\frac{q-1}{2}\right\rfloor
\right]\cap\mathbb Z.
\]

### N3-REQ-N2-012, transformed resonance audit

Status: `OPEN_AND_BLOCKING`

For the exact normalized law from N3-ANA-025:

1. identify every remaining exact and approximate secondary resonance;
2. determine transformed residue concentration modulo small integers;
3. freeze complete transformed major and minor arcs;
4. do not assume parity normalization removes all rational resonances.

### N3-REQ-N2-013, transformed aggregate phase dispersion

Status: `OPEN_AND_BLOCKING`

Prove one of:

- a lower bound for the transformed dispersion sum outside all transformed major arcs;
- a measure bound for weak-dispersion frequencies;
- a weighted transformed integral estimate;
- a target-local transformed concentration obstruction.

### N3-REQ-N2-014, transformed moment package

Status: `OPEN`

Still required:

- uniform transformed variance bounds;
- transformed third absolute centered moments;
- largest transformed step versus standard deviation;
- exact endpoint exclusions.

### N3-REQ-N2-015, collision-aware transformed reference law

Status: `OPEN`

A local theorem must retain `C_n(s)`, prove a target-local upper fiber bound, establish an additive-energy estimate, or show collision concentration obstructs approximation.

### N3-REQ-N2-016, transformed weighted Fourier inequality

Status: `OPEN`

The final required inequality must be written for the transformed law and transformed interval kernel, then transferred back through

\[
P(T\in I_{n,q})
\ge
(1-p^{(0)})P(\widetilde T\in J_{n,q}).
\]

Berry-Esseen distribution distance alone remains insufficient.

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
python3 tracks/nova3-analytic-density/proofs/parity_twin_sanity.py
```

Return separate verdicts through N3-ANA-025 and N3-FIN-007.

### N3-REQ-N4-002, source audit reconstruction

Status: `OPEN`

Independently reconstruct N3-SRC-004 through N3-SRC-008.

### N3-REQ-N4-003, repaired capacity audit

Status: `OPEN`

Verify the invalid central-binomial shortcut, quotient-factorial replacement, and exact threshold margins.

### N3-REQ-N4-004, numerical-law foundations

Status: `OPEN`

Verify strict mean monotonicity, endpoint limits, exact span, exact resonance set, and endpoint freezing.

### N3-REQ-N4-005, post-prefix tilt and collision audit

Status: `OPEN`

Verify N3-ANA-020 through N3-ANA-022 and N3-FIN-006.

### N3-REQ-N4-006, parity twin and odd normalization audit

Status: `OPEN`

Verify N3-ANA-023 through N3-ANA-025 and N3-FIN-007. Handoff:

`handoffs/TO_NOVA4_PARITY_TWIN.md`.

## Self-owned requirements

### N3-SELF-001 through N3-SELF-004

Status: `CLOSED`

Scale map, local ceiling, full-model non-Gaussian obstruction, and unrestricted logarithmic minor-arc obstruction are complete.

### N3-SELF-005, matched numerical bounded-torus theorem

Status: `PARTIALLY_CLOSED`

Closed:

- exact centering;
- exact target range;
- compact numerical tilt;
- exact span and exact modulus-one resonances;
- collision factor in atoms;
- parity twin obstruction;
- exact odd-lattice normalization.

Open:

- transformed resonance audit;
- transformed aggregate dispersion;
- transformed moments;
- collision-aware reference law;
- strict transformed Fourier comparison.

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

### N3-SELF-010, compact numerical tilt

Status: `CLOSED`

Closed by N3-ANA-020.

### N3-SELF-011, unnormalized aggregate phase dispersion

Status: `CLOSED_NEGATIVELY`

Closed by the parity twin obstruction N3-ANA-023.

### N3-SELF-012, parity-normalized numerical phase dispersion

Status: `OPEN`

Audit and control the exact transformed law from N3-ANA-025.

## Rule

Do not solve an undefined stronger problem. Every theorem must name its exact labels, target range, transformed supports, resonance set, endpoint exclusions, legal comparison direction, and receiving theorem node.
