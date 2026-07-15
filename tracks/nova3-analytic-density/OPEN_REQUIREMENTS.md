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

The first frozen Nova 1 construction fails through a power-of-two lattice obstruction proved by Nova 2. No local logarithmic density estimate repairs that construction.

### N3-REQ-N1-003

Status: `AWAITING_REVISED_CONSTRUCTION`

Nova 1 must provide a versioned replacement layer system that has already passed Nova 2's structural compatibility gate. Required fields are:

1. exact label sets;
2. numerical divisor values;
3. common support lattice and attained residues;
4. correction palette and radius;
5. first-target and endpoint checks;
6. exact target range;
7. exact selected-term budget;
8. exact branch and commit SHA.

### N3-REQ-N1-004

Status: `AVAILABLE_ANALYTIC_COMPONENT`

N3-ANA-012 supplies a compact-tilt coarse logarithmic-window theorem for distinct subset products of primes in `(n/2,n]`.

Nova 1 must determine whether a repaired construction can use this exact divisor family without reintroducing a common-lattice or first-window obstruction. The theorem provides logarithmic multiplicative density only, not numerical additive occupancy.

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

### N3-REQ-N2-004

Status: `NO_DIRECT_TRANSFER`

N3-ANA-012 studies `E exp(it log d)` for top-prime subset products. It does not control `E exp(it d)` or a rainbow sum of numerical divisor values. Nova 2 may use it only after proving a separate bridge from logarithmic multiplicative structure to its exact additive law.

## Requirements from Nova 4

### N3-REQ-N4-001

Status: `READY_FOR_INDEPENDENT_AUDIT`

Run and independently reproduce:

```text
python3 tracks/nova3-analytic-density/proofs/scale_sanity.py
python3 tracks/nova3-analytic-density/proofs/prime_interval_capacity_sanity.py
python3 tracks/nova3-analytic-density/proofs/compact_tilt_sanity.py
```

Return separate verdicts for N3-ANA-004 through N3-ANA-013 and N3-FIN-001 through N3-FIN-003.

### N3-REQ-N4-002

Status: `OPEN`

Reconstruct the source compatibility audit for N3-SRC-004 through N3-SRC-008 without relying on Nova 3's conclusions.

### N3-REQ-N4-003

Status: `OPEN`

Independently verify that imported N1-STR-009 at commit `fa11f4b2cb86a2dd791df189ada12757be791804` matches the hypotheses used in N3-ANA-011.

### N3-REQ-N4-004

Status: `OPEN`

Reconstruct N3-ANA-012 and N3-ANA-013 from `proofs/COMPACT_TILT_TOP_PRIME_BAND.md`. In particular, test:

1. the variance constant `1/48`;
2. the third-moment inequality;
3. both endpoint errors in the Berry-Esseen window proof;
4. the tilted maximum-atom conversion to a count;
5. unit-tilt favored-endpoint concentration;
6. the prohibition on transferring the theorem to numerical additive sums.

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

Status: `CLOSED_WITH_RESTRICTED_FAMILY`

Extend the coarse logarithmic-window theorem to a compact nonzero exponential-tilt range. Closed by N3-ANA-012 for the exact top-prime Bernoulli band `(n/2,n]` and bounded sharply by N3-ANA-013 at `|theta|=1`.

The corresponding theorem for the full bounded-exponent high-prime tail remains open.

### N3-SELF-007

Status: `OPEN`

Reconstruct the complete Phase 12L and Phase 12P small-divisor lemmas when their archived source packages become repository-accessible.

### N3-SELF-008

Status: `CLOSED`

Prove the explicit prime-interval, address, menu, and capacity thresholds requested by Nova 1. Closed by N3-ANA-010 and N3-ANA-011.

### N3-SELF-009

Status: `OPEN`

For the top-prime compact-tilt model, determine the sharpest uniform result below width `K_A log n`. Required outcome:

1. a bounded-frequency local theorem with explicit range; or
2. a proved resonance, spacing, or maximum-gap obstruction; or
3. the strongest true intermediate width.

## Rule

Do not solve an undefined stronger problem. Every incoming request must specify the exact estimate, complete parameter range, legal comparison direction, and theorem dependency it closes.