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

Implementation: `src/factorial_lab/n3_sources.py` and `src/replay_n3_sources.py`.

Checks Ford’s ambient quantifier, the friable exceptional-set qualifier, the ultrafriable common-cap mismatch, exact witnesses, source classifications, frozen metadata, and semantic checksums.

## N4-AUD-009: Nova 3 Dusart primary-source verifier

Status: `ACTIVE`.

Result class: `primary-source theorem audit`.

Frozen input:

```text
branch: nova/analytic-density
handoff: N3-HO-N4-002
handoff commit: 7469dada02fa4caca08ed391ef8b0cb0f1e855b2
source-ledger commit: 697e7ed8bdb03f54b2389b2fcdd8b685dadcebc4
proof file blob: e36daf98db86da16bd5ed8c6c82f43530d745f66
request: F
object: N3-ANA-010
```

Implementation:

```text
src/factorial_lab/n3_dusart.py
src/replay_n3_dusart.py
```

Schemas:

```text
data/analytic/n3_dusart_prime_interval_audit.schema.json
certificates/analytic/n3_dusart_prime_interval_claim.schema.json
```

Independent checks:

- exact primary-source metadata for arXiv:1002.0442v1, Theorem 6.9, equation (6.6);
- source thresholds `5393` and `60184` and their application at `n` and `n/2`;
- source-derived integer threshold `120368` and failure of unsupplemented predecessor coverage;
- rational certificate `log(2)<7/10`, `b<9/5`, `log(n)>4`, and `Q(L)>0`;
- exact sieve counts `pi(120368)=11330` and `pi(60184)=6076`;
- 80-digit source and target margins;
- frozen handoff, source-ledger, proof-file metadata, and semantic checksums.

Corruption behavior:

- rehashed threshold `120367` is rejected;
- rehashed source upper threshold `60183` is rejected;
- rehashed predecessor-coverage claim is rejected;
- wrong frozen-source metadata is rejected.

Replay:

```bash
PYTHONPATH=src python3 src/replay_n3_dusart.py verify \
  data/analytic/n3_dusart_prime_interval_audit.json
PYTHONPATH=src python3 src/replay_n3_dusart.py verify-claim \
  certificates/analytic/n3_dusart_prime_interval_claim.json \
  --audit data/analytic/n3_dusart_prime_interval_audit.json
```

## Test command

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

Every verifier fails closed on malformed input, checksum mismatch, frozen-source disagreement, or semantic disagreement.
