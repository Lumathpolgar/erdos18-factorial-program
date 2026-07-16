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

Implementation: `src/factorial_lab/n3_dusart.py` and `src/replay_n3_dusart.py`.

Checks the exact primary-source thresholds, their application at `n` and `n/2`, rational positivity of the cleared-denominator polynomial, exact endpoint prime counts, source metadata, and semantic checksums.

## N4-AUD-010: Nova 3 exact threshold-sweep verifier

Status: `ACTIVE`.

Result class: `finite certificate`.

Frozen input:

```text
branch: nova/analytic-density
handoff: N3-HO-N4-002
handoff commit: 7469dada02fa4caca08ed391ef8b0cb0f1e855b2
Nova 3 proof blob: e36daf98db86da16bd5ed8c6c82f43530d745f66
Nova 3 sanity script blob: 519c900b616a33d95f3b2a8a8dec10d04a0a24f5
Nova 1 theorem: N1-STR-009
Nova 1 commit: fa11f4b2cb86a2dd791df189ada12757be791804
Nova 1 proof blob: 4255e76ff18f675ae80a0192381070d9a934fc97
request: G
object: N3-ANA-011
```

Implementation: `src/factorial_lab/n3_threshold.py` and `src/replay_n3_threshold.py`.

Checks every integer `120368 <= n <= 1000000`, exact prime counts, dual exact valuations, rigorous logarithmic ceilings, address legality, conservative capacity, minima, runners-up, source metadata, and semantic checksums.

The verifier records request G as a finite certificate only. It does not infer distinct numerical sums or additive occupancy from formal profile capacity.

## N4-AUD-011: Nova 3 semantic adversarial theorem verifier

Status: `ACTIVE`.

Result class: `semantic adversarial theorem audit`.

Frozen input:

```text
branch: nova/analytic-density
handoff: N3-HO-N4-002
handoff commit: 7469dada02fa4caca08ed391ef8b0cb0f1e855b2
Nova 3 proof blob: e36daf98db86da16bd5ed8c6c82f43530d745f66
Nova 3 sanity script blob: 519c900b616a33d95f3b2a8a8dec10d04a0a24f5
Nova 1 theorem: N1-STR-009
Nova 1 commit: fa11f4b2cb86a2dd791df189ada12757be791804
Nova 1 proof blob: 4255e76ff18f675ae80a0192381070d9a934fc97
request G audit: e26653648c2cc9ebc30b03f01904dbb5bcca65737ead57abc9cdbc0b2f218bb0
request G claim: e41f7e639c605ed4e70e4ac2cc6afe20d83ef8bf4f22e991fe0986449b9c1e88
request: H
object: N3-ANA-011
```

Implementation:

```text
src/factorial_lab/n3_adversarial.py
src/replay_n3_adversarial.py
```

Schemas:

```text
data/analytic/n3_ana_011_contract.schema.json
data/analytic/n3_threshold_adversarial_audit.schema.json
certificates/analytic/n3_ana_011_final_claim.schema.json
```

Independent checks:

- uniform address proof from exact ceiling and Legendre bounds;
- exact definition match between Nova 3 menus and imported `N1-STR-009`;
- preservation of the unit-exclusion correction `2^(m_n-1)-1`;
- formal profile capacity without injectivity or distinct-sum inflation;
- exact endpoint semantics `pi(n/2)=pi(floor(n/2))`;
- witness `n=120417`, where `ceil(n/2)=60209` is prime;
- finite request G evidence remains finite only;
- frozen source metadata and semantic checksums.

Corruption behavior:

- rehashed threshold `120367` without supplementation is rejected;
- rehashed larger legal address range is rejected;
- rehashed removed menu-unit correction is rejected;
- rehashed profile-injectivity claim is rejected;
- rehashed ceil endpoint substitution is rejected;
- rehashed finite-asymptotic claim is rejected.

Replay:

```bash
PYTHONPATH=src python3 src/replay_n3_adversarial.py verify \
  data/analytic/n3_threshold_adversarial_audit.json
PYTHONPATH=src python3 src/replay_n3_adversarial.py verify-contract \
  data/analytic/n3_ana_011_contract.json
PYTHONPATH=src python3 src/replay_n3_adversarial.py verify-claim \
  certificates/analytic/n3_ana_011_final_claim.json
PYTHONPATH=src python3 src/replay_n3_adversarial.py verify-fixtures \
  tests/n3_adversarial_fixtures
```

## Test command

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

Every verifier fails closed on malformed input, checksum mismatch, frozen-source disagreement, or semantic disagreement.
