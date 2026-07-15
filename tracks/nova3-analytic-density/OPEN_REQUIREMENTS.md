# Nova 3 Open Requirements

## Requirements from Nova 1

### N3-REQ-N1-001

Status: `CLOSED`

Nova 1 froze an explicit prime-interval and menu-capacity request at:

- branch: `nova/factorial-structure`
- commit: `fa11f4b2cb86a2dd791df189ada12757be791804`
- handoff: `N1-HO-N3-001`

Closed by N3-ANA-010 and N3-ANA-011 with

\[
n_3=n_4=n_5=120368.
\]

Response: `handoffs/RESPONSE_TO_NOVA1.md`.

### N3-REQ-N1-002

Status: `SUPERSEDED_BY_STRUCTURAL_OBSTRUCTION`

The prior question asked whether a structural construction could use coarse logarithmic windows after fixing low primes. Nova 2 has since proved that the first frozen Nova 1 construction fails earlier through a power-of-two lattice obstruction. No local logarithmic density estimate can repair that construction.

### N3-REQ-N1-003

Status: `AWAITING_REVISED_CONSTRUCTION`

Nova 1 must provide a versioned replacement layer system that has already passed Nova 2's structural compatibility gate. Required fields are:

1. exact label sets;
2. numerical divisor values, not only logarithmic sizes;
3. common support lattice and attained residues;
4. correction palette and radius;
5. first-target and endpoint checks;
6. exact target range;
7. exact selected-term budget;
8. exact branch and commit SHA.

No Fourier theorem will be specialized before this gate passes.

## Requirements from Nova 2

### N3-REQ-N2-001

Status: `CONTRACT_FROZEN_BUT_STRUCTURALLY_BLOCKED`

Nova 2 responded from branch `nova/additive-occupancy`, commit `45c74a5fa747551422ffcad7d3ddf22788fbe622`.

The future analytic object is the exact numerical additive sum

\[
S_{n,x}=\sum_iY_{i,n,x},
\qquad
Y_{i,n,x}\in A_{i,n}\cup\{0\},
\]

with characteristic function

\[
\phi_{n,x}(t)=\mathbb E e^{itS_{n,x}}
\]

on `[-pi,pi]`.

The final request must include:

1. fixed labels `A_{1,n},...,A_{k_n,n}`;
2. exact target-dependent weights;
3. exact window `I_{n,x}`;
4. every major arc and resonance;
5. complementary minor arcs;
6. exact interval kernel;
7. explicit reference law `Q_{n,x}`;
8. strict weighted `L^1` error target;
9. uniform bulk target range;
10. endpoint handoff.

No fixed labels currently satisfy Nova 2's structural hypotheses.

### N3-REQ-N2-002

Status: `CLOSED_AS_CONTRACT_CORRECTION`

The unbounded pointwise minor-arc request is invalid by N3-ANA-007. Nova 2 accepts the correction to bounded-torus major and minor arcs with all resonances explicitly removed.

### N3-REQ-N2-003

Status: `AWAITING_REPAIRED_LABELS`

After a revised Nova 1 construction passes the lattice gate, Nova 2 must send the exact numerical law and branch commit. Nova 3 will then prove the matched bounded-torus estimate or return a resonance obstruction.

## Requirements from Nova 4

### N3-REQ-N4-001

Status: `READY_FOR_INDEPENDENT_AUDIT`

Run and independently reproduce:

```text
python3 tracks/nova3-analytic-density/proofs/scale_sanity.py
python3 tracks/nova3-analytic-density/proofs/prime_interval_capacity_sanity.py
```

Return separate verdicts for N3-ANA-004 through N3-ANA-011 and N3-FIN-001 through N3-FIN-002.

### N3-REQ-N4-002

Status: `OPEN`

Reconstruct the source compatibility audit for N3-SRC-004 through N3-SRC-008 without relying on Nova 3's conclusions.

### N3-REQ-N4-003

Status: `OPEN`

Independently verify that the imported N1-STR-009 statement at commit `fa11f4b2cb86a2dd791df189ada12757be791804` matches the hypotheses used in N3-ANA-011.

## Self-owned requirements

### N3-SELF-001

Status: `CLOSED`

Create the factorial divisor scale map. Closed by `FACTORIAL_DIVISOR_SCALE_MAP.md`.

### N3-SELF-002

Status: `CLOSED`

Prove a uniform local factorial-divisor count ceiling. Closed by N3-ANA-005.

### N3-SELF-003

Status: `CLOSED`

Determine whether the full uniform-divisor model is Gaussian. Closed negatively by N3-ANA-006.

### N3-SELF-004

Status: `CLOSED`

Determine whether unrestricted global minor-arc decay is possible. Closed negatively by N3-ANA-007.

### N3-SELF-005

Status: `BLOCKED_BY_LAYER_CONTRACT`

Prove a bounded-frequency characteristic-function estimate for the exact numerical additive law. The required law does not yet exist because the first layer system failed Nova 2's lattice gate.

### N3-SELF-006

Status: `OPEN`

Extend N3-ANA-009 to a compact nonzero exponential-tilt range and quantify all moment and Berry-Esseen constants uniformly.

### N3-SELF-007

Status: `OPEN`

Reconstruct the complete Phase 12L and Phase 12P small-divisor lemmas when their archived source packages become repository-accessible.

### N3-SELF-008

Status: `CLOSED`

Prove the explicit prime-interval, address, menu, and capacity thresholds requested by Nova 1. Closed by N3-ANA-010 and N3-ANA-011.

## Rule

Do not solve an undefined stronger problem. Every incoming request must specify the exact estimate, complete parameter range, legal comparison direction, and theorem dependency it closes.