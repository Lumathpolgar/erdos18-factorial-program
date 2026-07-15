# Nova 4 Verifier Registry

## N4-VER-001: Representation certificate verifier

Status: `ACTIVE`

Result class: `finite certificate`

Purpose: verify exact sums of distinct positive divisors of `n!`.

Implementation:

```text
src/factorial_lab/certificates.py
```

Input schema:

```text
certificates/representation_certificate.schema.json
```

Checks:

- strict integer fields;
- positivity;
- exact factorial divisibility through prime valuations;
- duplicate numerical values across all labels;
- exact sum equality;
- target range membership;
- term count;
- optional cached field consistency.

Failure behavior: fail closed with nonzero replay status.

Corruption tests:

- duplicate numerical divisors with different labels;
- illegal divisor;
- wrong sum;
- exceeded term bound;
- false cached sum.

Test command:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

## N4-VER-002: Exact profile replay

Status: `ACTIVE`

Result class: `exact finite theorem audit`

Implementation:

```text
src/factorial_lab/dataset.py
```

Independent optimality basis:

- Method A minimum-cardinality dynamic programming;
- Method B exact-cardinality bitsets.

Recomputed fields:

- all `lambda` values;
- interval maximum;
- hardest targets;
- prime valuations;
- divisor count;
- eligible divisor count;
- greedy failure count and first failure;
- dataset checksum.

Replay command:

```bash
PYTHONPATH=src python3 src/replay.py verify-dataset \
  data/factorial_half_range_profiles_n1_n13.json
```

## N4-VER-003: Arithmetic core

Status: `ACTIVE`

Result class: `exact finite theorem audit`

Implementation:

```text
src/factorial_lab/arithmetic.py
```

Checks include prime sieve, Legendre valuations, exact divisor generation, divisor-count identity, and exact factorial divisibility.

## N4-VER-004: Lattice-first label-family verifier

Status: `ACTIVE`

Result class: `finite certificate`

Implementation:

```text
src/factorial_lab/lattice.py
```

Input schema:

```text
certificates/lattice/label_family.schema.json
```

Checks:

- exact source branch and commit metadata;
- positive integer terms and exact factorial divisibility;
- target-range bounds;
- duplicate numerical terms within and across labels;
- correction-palette collisions;
- main and final common gcd;
- exact reachable residues for declared moduli;
- exact finite reachable support with one or zero terms per layer;
- every downward target window in the finite domain;
- cached gcd and first-failure claims by recomputation.

Resource behavior: exceeding the explicit exact-state limit produces `unknown due to resource limits`, never a false claim.

Replay command:

```bash
PYTHONPATH=src python3 src/replay.py verify-label-family \
  tests/lattice_fixtures/valid_common_gcd_failure.json
```

## N4-AUD-002: Frozen Nova 2 lattice-obstruction replay

Status: `ACTIVE`

Result class: `exact finite theorem audit`

Implementation:

```text
src/factorial_lab/logcert.py
src/factorial_lab/n2_audit.py
```

Certificate schema:

```text
certificates/lattice/n2_obs_107.schema.json
```

The verifier uses rigorous rational bounds for the logarithmic ceilings, recomputes `v_2(n!)`, checks exact source SHAs, verifies target admissibility, and proves the target window is disjoint from the common lattice.

Replay command:

```bash
PYTHONPATH=src python3 src/replay.py verify-n2-obs-107 \
  certificates/lattice/n2_obs_107_n1892.json
```

## N4-AUD-003: Nova 1 capacity-threshold verifier

Status: `ACTIVE`

Result class: `exact finite theorem audit`

Frozen input: `nova/factorial-structure@fa11f4b2cb86a2dd791df189ada12757be791804`, handoff `N1-HO-N4-001`, Study A.

Implementation:

```text
src/factorial_lab/logcert.py
src/factorial_lab/n1_capacity.py
```

Checks:

- exact prime counts and `m_n`;
- exact `v_2(n!)=n-popcount(n)`;
- rationally certified transition tables for both logarithmic ceilings;
- exact truth values of `A_n` and `C_n`;
- all later failures after first success;
- all truth-state transition rows;
- certified minimum `C_n` margin on every success interval;
- semantic checksum and exact frozen source metadata.

Replay:

```bash
PYTHONPATH=src python3 src/replay.py verify-n1-capacity \
  certificates/capacity/n1_capacity_audit_n3_n1000000.json
```
