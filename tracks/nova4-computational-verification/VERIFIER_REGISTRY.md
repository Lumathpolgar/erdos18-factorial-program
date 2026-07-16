# Nova 4 Verifier Registry

## N4-VER-001: Representation certificate verifier

Status: `ACTIVE`.

Implementation: `src/factorial_lab/certificates.py`.

Checks strict integers, positivity, exact factorial divisibility, numerical distinctness, exact sum equality, target range, term count, and cached fields.

## N4-VER-002: Exact profile replay

Status: `ACTIVE`.

Implementation: `src/factorial_lab/dataset.py`.

Recomputes all exact `lambda` values and compares minimum-cardinality dynamic programming with exact-cardinality bitsets.

## N4-VER-003: Arithmetic core

Status: `ACTIVE`.

Implementation: `src/factorial_lab/arithmetic.py`.

Checks prime sieving, Legendre valuations, exact divisor generation, divisor-count identities, and factorial divisibility.

## N4-VER-004: Lattice-first label-family verifier

Status: `ACTIVE`.

Implementation: `src/factorial_lab/lattice.py`.

Checks source metadata, factorial legality, duplicates, correction collisions, gcd, residues, exact finite support, every downward window, and cached failure claims.

## N4-AUD-002: Frozen Nova 2 lattice-obstruction replay

Status: `ACTIVE`.

Implementation: `src/factorial_lab/n2_audit.py` and `src/factorial_lab/logcert.py`.

## N4-AUD-003: Nova 1 capacity-threshold verifier

Status: `ACTIVE`.

Implementation: `src/factorial_lab/n1_capacity.py`.

Frozen input: `nova/factorial-structure@fa11f4b2cb86a2dd791df189ada12757be791804`.

## N4-AUD-004: Nova 1 reduced-rainbow verifier

Status: `ACTIVE`.

Implementation: `src/factorial_lab/n1_rainbow.py` and `src/replay_rainbow.py`.

## N4-AUD-005: Nova 3 product-moment and local-ceiling verifier

Status: `ACTIVE`.

Implementation: `src/factorial_lab/n3_moments.py` and `src/replay_n3.py`.

Checks exact divisor vectors, moments, complement symmetry, covariances, certified integer window endpoints, and every requested local count.

## N4-AUD-006: Nova 3 scale-evidence verifier

Status: `ACTIVE`.

Implementation: `src/factorial_lab/n3_scale.py` and `src/replay_n3_scale.py`.

Checks exact valuations, 80-digit scale data, variance shares, effective dimensions, cutoff grids, theorem-path rows, and the frozen script’s factor-of-two tail normalization.

## N4-AUD-007: Nova 3 characteristic-recurrence verifier

Status: `ACTIVE`.

Implementation: `src/factorial_lab/n3_recurrence.py` and `src/replay_n3_recurrence.py`.

Checks the complete bounded `q` grid, finalist selection, 80-digit reevaluation, direct exact exponent-vector averaging, and frozen handoff/proof metadata.

## N4-AUD-008: Nova 3 restricted-source compatibility verifier

Status: `ACTIVE`.

Result class: `source compatibility audit`.

Frozen input:

```text
branch: nova/analytic-density
handoff: N3-HO-N4-002
handoff commit: 7469dada02fa4caca08ed391ef8b0cb0f1e855b2
source-ledger commit: 697e7ed8bdb03f54b2389b2fcdd8b685dadcebc4
request: E
```

Implementation:

```text
src/factorial_lab/n3_sources.py
src/replay_n3_sources.py
```

Schemas:

```text
data/analytic/n3_restricted_source_compatibility.schema.json
certificates/analytic/n3_source_compatibility_claim.schema.json
```

Independent checks:

- exact reconstruction of Ford’s ambient `H(x,y,z)` quantifier scope;
- exact witness `H(120,6,7)=17` while `tau(120;6,7)=0`;
- exact verification that `10!` is `10`-friable;
- preservation of the Drappeau–Tenenbaum exceptional-set qualifier;
- exact `v_2(10!)=8`, `256|10!`, and `11∤10!` ultrafriable mismatch;
- all three source classifications and legal comparison directions;
- frozen handoff and source-ledger metadata;
- full semantic checksums.

Corruption behavior:

- a rehashed claim that a restricted source directly selects `n!` is rejected;
- rehashed removal of the friable exceptional-set qualifier is rejected;
- rehashed assertion of exact ultrafriable/factorial support equality is rejected;
- wrong handoff metadata is rejected.

Replay:

```bash
PYTHONPATH=src python3 src/replay_n3_sources.py verify \
  data/analytic/n3_restricted_source_compatibility.json
PYTHONPATH=src python3 src/replay_n3_sources.py verify-claim \
  certificates/analytic/n3_restricted_source_compatibility.json
```

## Test command

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

Every verifier fails closed on malformed input, checksum mismatch, frozen-source disagreement, or semantic disagreement.