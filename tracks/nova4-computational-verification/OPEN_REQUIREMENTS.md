# Nova 4 Open Requirements

## Requirements from Nova 1

### N4-REQ-N1-001

Status: `AWAITING_CONSTRUCTION`

Receive frozen divisor formulas, selection rules, and correction palettes. Implement exact legality, collision, range, and term-count checks.

## Requirements from Nova 2

### N4-REQ-N2-001

Status: `AWAITING_MODEL`

Receive frozen additive layer models. Compute exact supports for feasible parameters, detect lattice obstructions, and locate first uncovered windows.

## Requirements from Nova 3

### N4-REQ-N3-001

Status: `DRAFT`

Generate exact finite divisor-size and valuation-profile statistics for specified parameter ranges to test analytic formulas.

## Integration requirements

### N4-REQ-INT-001

Status: `READY`

Reconstruct the archived Track B half-range-to-global implication using the frozen `H_N` definition and report every mismatch.

### N4-REQ-INT-002

Status: `READY`

Define the universal certificate schema and fail-closed verifier standard used by all tracks.

## Rule

Nova 4 verifies claims but does not silently repair theorem statements. Any mismatch is returned to the owner through a versioned handoff.
