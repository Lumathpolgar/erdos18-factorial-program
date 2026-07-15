# Nova 3 Open Requirements

## Requirements from Nova 1

### N3-REQ-N1-001

Status: `AWAITING_FROZEN_CONSTRUCTION`

Required input:

1. exact cutoff `y(n)` or prime bands;
2. permitted low-prime exponent family;
3. exact logarithmic target range;
4. exact window width;
5. weakest sufficient lower or upper count;
6. named structural theorem node closed by the estimate.

Current available input: N3-ANA-005 gives an exact upper ceiling; N3-ANA-009 gives a conditional coarse central-window lower bound after low-prime conditioning.

### N3-REQ-N1-002

Status: `OPEN`

Determine whether a structural construction can use windows of width

\[
\Delta\gg n\log y/y
\]

after fixing primes at most `y`. If yes, the current coarse theorem may already overlap the construction.

## Requirements from Nova 2

### N3-REQ-N2-001

Status: `AWAITING_FROZEN_MODEL`

Required input:

1. whether the Fourier variable acts on `log d` or on numerical divisor values;
2. exact layer measure;
3. independence or dependency graph;
4. prime and exponent restrictions;
5. number of convolution factors;
6. exact inversion cutoff;
7. required norm and main-term error scale;
8. named occupancy theorem node closed by the estimate.

### N3-REQ-N2-002

Status: `OPEN`

Freeze a bounded-frequency characteristic-function contract. An unbounded pointwise minor arc is disproved by N3-ANA-007.

## Requirements from Nova 4

### N3-REQ-N4-001

Status: `READY_FOR_INDEPENDENT_AUDIT`

Run and independently reproduce:

```text
python3 tracks/nova3-analytic-density/proofs/scale_sanity.py
```

Return a separate verdict for N3-ANA-004 through N3-ANA-009. Exact requested tests are frozen in `handoffs/TO_NOVA4.md`.

### N3-REQ-N4-002

Status: `OPEN`

Reconstruct the source compatibility audit for N3-SRC-004 through N3-SRC-007 without relying on Nova 3's conclusions.

## Self-owned requirements

### N3-SELF-001

Status: `CLOSED`

Create the factorial divisor scale map, including valuation bands, entropy, exact moments, effective dimension, lattice analysis, and candidate window widths.

Closed by `FACTORIAL_DIVISOR_SCALE_MAP.md`.

### N3-SELF-002

Status: `CLOSED`

Prove a nontrivial uniform upper bound for local factorial-divisor counts.

Closed by N3-ANA-005.

### N3-SELF-003

Status: `CLOSED`

Determine whether the full uniform-divisor model supports a Gaussian local-limit architecture.

Closed negatively by N3-ANA-006.

### N3-SELF-004

Status: `CLOSED`

Determine whether an unrestricted global minor-arc estimate is possible.

Closed negatively by N3-ANA-007.

### N3-SELF-005

Status: `OPEN`

Prove a bounded-frequency high-prime characteristic-function estimate under an explicit compact tilt, after receiving the inversion range from Nova 2.

### N3-SELF-006

Status: `OPEN`

Extend N3-ANA-009 to nonzero compact tilts and quantify all uniform constants.

### N3-SELF-007

Status: `OPEN`

Reconstruct the complete Phase 12L and Phase 12P small-divisor lemmas from their archived source packages when those packages become repository-accessible.

## Rule

Do not solve an undefined stronger problem. Every incoming request must specify the exact estimate needed, its complete parameter range, and the theorem dependency it closes.
