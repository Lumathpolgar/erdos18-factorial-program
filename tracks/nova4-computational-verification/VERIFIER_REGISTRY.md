# Nova 4 Verifier Registry

## N4-VER-001: Representation certificate verifier

Status: `ACTIVE`

Result class: `finite certificate`

Implementation and schema:

```text
src/factorial_lab/certificates.py
certificates/representation_certificate.schema.json
```

Checks strict integers, positivity, exact factorial divisibility, numerical distinctness regardless of labels, exact sum equality, target range, term count, and cached fields.

## N4-VER-002: Exact profile replay

Status: `ACTIVE`

Result class: `exact finite theorem audit`

Implementation: `src/factorial_lab/dataset.py`.

Independent methods: minimum-cardinality 0/1 dynamic programming and exact-cardinality bitsets. Recomputes all `lambda` values, interval maxima, hardest targets, valuations, divisor counts, eligible counts, greedy failures, and checksum.

## N4-VER-003: Arithmetic core

Status: `ACTIVE`

Implementation: `src/factorial_lab/arithmetic.py`.

Checks deterministic prime sieving, Legendre valuations, exact divisor generation, divisor-count identities, and factorial divisibility.

## N4-VER-004: Lattice-first label-family verifier

Status: `ACTIVE`

Result class: `finite certificate`

Implementation and schema:

```text
src/factorial_lab/lattice.py
certificates/lattice/label_family.schema.json
```

Checks source metadata, factorial legality, target bounds, numerical duplicates, correction collisions, gcd, residue support, exact one-or-zero-per-layer finite support, every downward window, and cached failure claims. Explicit state-limit overflow reports `unknown due to resource limits`.

## N4-AUD-002: Frozen Nova 2 lattice-obstruction replay

Status: `ACTIVE`

Result class: `exact finite theorem audit`

Implementation:

```text
src/factorial_lab/logcert.py
src/factorial_lab/n2_audit.py
```

Recomputes `N2-ADD-115` and `N2-OBS-107` against exact source SHAs and proves the failing window is disjoint from the common lattice.

## N4-AUD-003: Nova 1 capacity-threshold verifier

Status: `ACTIVE`

Result class: `exact finite theorem audit`

Frozen input: `nova/factorial-structure@fa11f4b2cb86a2dd791df189ada12757be791804`, Study A.

Implementation:

```text
src/factorial_lab/logcert.py
src/factorial_lab/n1_capacity.py
```

Checks exact prime counts, `v_2(n!)`, certified logarithmic ceilings, predicates `A_n` and `C_n`, transition rows, later failures, minimum certified margins, checksum, and frozen source metadata.

## N4-AUD-004: Nova 1 reduced-rainbow verifier

Status: `ACTIVE`

Result classes: `computational evidence` and `disproved finite claim`.

Frozen input: `nova/factorial-structure@fa11f4b2cb86a2dd791df189ada12757be791804`, Study B.

Implementation:

```text
src/factorial_lab/n1_rainbow.py
src/replay_rainbow.py
```

Checks certified parameters, exact high-prime menus, addresses, factorial legality, no numerical collisions, exact target-truncated bitset support, formal profiles, gcd, residues for every `2<=q<=64`, maximum gaps, first failure, and exact witnesses. The bitset result is independently checked against the common-lattice obstruction.

## N4-AUD-005: Nova 3 product-moment and local-ceiling verifier

Status: `ACTIVE`

Result class: `finite certificate` supporting accepted theorem audits.

Frozen input:

```text
nova/analytic-density@0ce88b28dc2e6641093526f5777bb31f658e3515
handoff: N3-HO-N4-001
objects: N3-ANA-004 and N3-ANA-005
```

Implementation:

```text
src/factorial_lab/n3_moments.py
src/replay_n3.py
```

Schemas:

```text
data/analytic/n3_moment_local_audit.schema.json
certificates/analytic/n3_local_ceiling_claim.schema.json
```

Independent checks:

- exact divisor-vector enumeration and numerical uniqueness;
- exact `tau(n!)` and complement symmetry;
- exact rational coordinate means and second moments;
- exact vanishing of all cross covariances;
- 80-digit decimal replay of log mean and variance;
- certified `floor(Delta/log q)` using rational log bounds;
- certified `floor(d exp(Delta))` using rational exponential bounds;
- exact integer local-window counts for every requested endpoint;
- full semantic checksum and exact frozen source metadata.

Corruption behavior:

- lowering a tight upper bound by one is rejected even after recomputing its outer checksum;
- corrupting the cached actual count is rejected;
- a valid tight certificate replays independently.

Replay:

```bash
PYTHONPATH=src python3 src/replay_n3.py verify \
  data/analytic/n3_moment_local_n2_n12.json

PYTHONPATH=src python3 src/replay_n3.py verify-local-claim \
  certificates/analytic/n3_local_ceiling_tight_n2.json
```

## Test command

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

Every verifier fails closed on malformed input, checksum mismatch, or semantic disagreement.
