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

Independent checks exact divisor-vector enumeration, exact moments, complement symmetry, vanishing cross covariances, 80-digit log replay, certified integer window endpoints, all requested local counts, semantic checksum, and frozen source metadata. Rehashed downward-bound and cached-count corruption are rejected.

## N4-AUD-006: Nova 3 scale-evidence verifier

Status: `ACTIVE`

Result class: `computational evidence`.

Frozen input:

```text
nova/analytic-density@0ce88b28dc2e6641093526f5777bb31f658e3515
handoff: N3-HO-N4-001
request: C
objects: N3-ANA-006 and N3-ANA-008
```

Implementation:

```text
src/factorial_lab/n3_scale.py
src/replay_n3_scale.py
```

Index schema:

```text
data/analytic/n3_scale_evidence_index.schema.json
```

Independent checks:

- exact prime sieve and Legendre valuations;
- 80-digit Decimal `log tau`, variance contributions, variance shares, and effective dimension;
- all eight requested `n` rows;
- all 63 nonempty cutoff-grid rows;
- eight admissible `y_n=floor(sqrt(n))/2` path rows;
- theorem-defined `M=max b_p log(p)/2` and exact stored factor two against the frozen script span;
- direct numerical cross-check of frozen float scale rows and nine printed tail points;
- one-million-prime truncated variance proxy;
- full semantic checksum and frozen source metadata.

Corruption behavior:

- rehashed `M/B` corruption is rejected;
- rehashed low-prime variance-share corruption is rejected;
- wrong source SHA is rejected.

Replay:

```bash
PYTHONPATH=src python3 src/replay_n3_scale.py generate \
  --output-json /tmp/n3_scale_evidence.json \
  --scale-csv /tmp/n3_scale_rows.csv \
  --tail-csv /tmp/n3_high_prime_tail_rows.csv
PYTHONPATH=src python3 src/replay_n3_scale.py verify /tmp/n3_scale_evidence.json
```

The verifier records the frozen script's tail-ratio label as `NEEDS_REPAIR_FOR_TAIL_RATIO_LABEL`; it does not reject the theorem statement from that implementation mismatch.

## N4-AUD-007: Nova 3 characteristic-recurrence verifier

Status: `ACTIVE`

Result classes: `proved theorem audit` and `computational evidence`.

Frozen input:

```text
branch: nova/analytic-density
superseding handoff: N3-HO-N4-002
handoff commit: 7469dada02fa4caca08ed391ef8b0cb0f1e855b2
proof commit: ff57005b975c4917341306bd0eceb6d05a9b18f6
request: D
object: N3-ANA-007
```

Implementation:

```text
src/factorial_lab/n3_recurrence.py
src/replay_n3_recurrence.py
```

Schemas:

```text
data/analytic/n3_characteristic_recurrence_index.schema.json
data/analytic/n3_characteristic_recurrence_evidence.schema.json
certificates/analytic/n3_recurrence_candidate.schema.json
```

Independent checks:

- exact prime sieve and factorial valuations;
- declared contiguous bounded `q` range and frequency blocks;
- exhaustive binary64 ranking of every `q` for every `3<=n<=12`;
- exact prime-2 recurrence under `t_q=2*pi*q/log(2)`;
- top-eight finalist retention for every `n` and block;
- 80-digit Decimal logarithms, Machin-formula pi, and sine-series reevaluation;
- exact exponent-vector counts and direct complex averaging;
- full semantic checksum and frozen handoff/proof metadata;
- independently recomputed candidate fields and modulus range.

Corruption behavior:

- rehashed false characteristic modulus is rejected;
- rehashed changed frequency parameter is rejected;
- rehashed direct-average corruption is rejected;
- wrong frozen-source metadata is rejected.

Replay:

```bash
PYTHONPATH=src python3 src/replay_n3_recurrence.py audit \
  --output /tmp/n3_characteristic_recurrence_evidence.json \
  --block-csv /tmp/n3_characteristic_recurrence_blocks.csv \
  --best-csv /tmp/n3_characteristic_recurrence_best.csv \
  --candidate /tmp/n3_recurrence_candidate_n12.json
PYTHONPATH=src python3 src/replay_n3_recurrence.py verify \
  /tmp/n3_characteristic_recurrence_evidence.json
PYTHONPATH=src python3 src/replay_n3_recurrence.py verify-candidate \
  certificates/analytic/n3_recurrence_candidate_n12.json
```

Theorem acceptance rests on an independent reconstruction of the simultaneous-recurrence proof. The bounded scan is supporting evidence only and does not certify an unbounded recurrence rate or a maximum outside the grid.

## Test command

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

Every verifier fails closed on malformed input, checksum mismatch, or semantic disagreement.
