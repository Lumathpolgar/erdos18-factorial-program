# Nova 4 Dataset Registry

## Dataset entry fields

```text
Dataset ID:
Status:
Generator commit:
Parameter range:
Exact or sampled:
Arithmetic type:
Schema:
Checksum or stable identifier:
Verification command:
Known limitations:
```

## Planned datasets

### N4-DATA-001: Factorial divisor inventories

Status: `PLANNED`

Exact sorted divisor sets for feasible `n`, with prime-factorization metadata and independent divisor-count checks.

### N4-DATA-002: Exact representation profiles

Status: `PLANNED`

For feasible targets, record exact or certified bounds for `lambda_{n!}(x)`, along with witnesses.

### N4-DATA-003: Candidate layer occupancy

Status: `PLANNED`

For frozen layer systems, record attainable sums, collision multiplicities, minimum window occupancy, and first uncovered targets.

### N4-DATA-004: Valuation-profile statistics

Status: `PLANNED`

Histograms and moments for logarithmic divisor sizes and prime-exponent vectors, intended as evidence for Nova 3's asymptotic models.

## Rules

- Large generated data need not be committed directly if a deterministic generator and checksum are committed.
- Every exact claim must be reproducible from raw inputs.
- Sampled data must record the sampling method and seed.
