# Nova 4 Verifier Registry

## Verifier entry fields

```text
Verifier ID:
Status:
Purpose:
Input schema:
Output schema:
Exact arithmetic:
Failure behavior:
Test command:
Corruption tests:
Owner:
```

## Planned verifiers

### N4-VER-001: Representation certificate verifier

Status: `PLANNED`

Checks that all selected integers are positive, numerically distinct divisors of `n!`, that their exact sum equals the target, and that the claimed term bound holds.

### N4-VER-002: Interval coverage verifier

Status: `PLANNED`

Checks completeness of a finite interval certificate and rejects missing targets, duplicate divisors, or unverified summary counts.

### N4-VER-003: Layer contract verifier

Status: `PLANNED`

Checks factorial valuation budgets, support ranges, cross-layer collisions, correction-palette collisions, and per-layer selection constraints.

### N4-VER-004: Handoff package verifier

Status: `PLANNED`

Checks that required handoff fields, file references, theorem IDs, statuses, and verification commands are present.

### N4-AUD-001: Track B clean reconstruction

Status: `PLANNED`

Reconstructs the conditional half-range-to-global implication under the frozen repository notation.

## Fail-closed rule

Missing files, malformed inputs, overflow risks, timeouts, inconsistent metadata, or failed assertions produce a failure status. They never produce a qualified pass.
