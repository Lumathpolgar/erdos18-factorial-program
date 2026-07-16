# Nova 4 Verifier Registry

Every verifier fails closed on malformed input, checksum mismatch, frozen-source disagreement, or semantic disagreement.

## Core verifiers

| ID | Status | Implementation | Scope |
|---|---|---|---|
| N4-VER-001 | `ACTIVE` | `src/factorial_lab/certificates.py` | Representation legality, distinctness, exact sums, and term bounds |
| N4-VER-002 | `ACTIVE` | `src/factorial_lab/dataset.py` | Exact profile replay by two independent methods |
| N4-VER-003 | `ACTIVE` | `src/factorial_lab/arithmetic.py` | Prime sieving, Legendre valuations, divisor generation, and factorial divisibility |
| N4-VER-004 | `ACTIVE` | `src/factorial_lab/lattice.py` | Label legality, collisions, gcd, residues, and exact window coverage |

## Theorem and evidence audits

| ID | Status | Implementation | Main result |
|---|---|---|---|
| N4-AUD-002 | `ACTIVE` | `n2_audit.py`, `logcert.py` | Frozen Nova 2 lattice obstruction |
| N4-AUD-003 | `ACTIVE` | `n1_capacity.py` | Nova 1 capacity threshold sweep |
| N4-AUD-004 | `ACTIVE` | `n1_rainbow.py`, `replay_rainbow.py` | Reduced-rainbow finite falsification |
| N4-AUD-005 | `ACTIVE` | `n3_moments.py`, `replay_n3.py` | `N3-ANA-004` and `N3-ANA-005` |
| N4-AUD-006 | `ACTIVE` | `n3_scale.py`, `replay_n3_scale.py` | Scale evidence and `2M/B` label diagnosis |
| N4-AUD-007 | `ACTIVE` | `n3_recurrence.py`, `replay_n3_recurrence.py` | `N3-ANA-007` and bounded recurrence evidence |
| N4-AUD-008 | `ACTIVE` | `n3_sources.py`, `replay_n3_sources.py` | Restricted-source compatibility |
| N4-AUD-009 | `ACTIVE` | `n3_dusart.py`, `replay_n3_dusart.py` | Dusart reconstruction and `N3-ANA-010` |
| N4-AUD-010 | `ACTIVE` | `n3_threshold.py`, `replay_n3_threshold.py` | Complete request G finite sweep |
| N4-AUD-011 | `ACTIVE` | `n3_adversarial.py`, `replay_n3_adversarial.py` | Request H and `N3-ANA-011` |
| N4-AUD-012 | `ACTIVE` | `n3_variance_limit.py`, `replay_n3_variance.py` | `N3-ANA-006` variance and non-Gaussian full limit |
| N4-AUD-013 | `ACTIVE` | `n3_high_prime.py`, `replay_n3_high_prime.py` | `N3-ANA-008` and `N3-ANA-009` |

## N4-AUD-013 frozen input

```text
branch: nova/analytic-density
handoff: N3-HO-N4-002
handoff commit: 7469dada02fa4caca08ed391ef8b0cb0f1e855b2
proof file: tracks/nova3-analytic-density/proofs/PRODUCT_MODEL_THEOREMS.md
proof file blob: 6260f8db0b377cf7dbc1850cbe25c91243099e10
source ledger blob: da81e6aaf2674fdae036d72df002547d4a71b18a
objects: N3-ANA-008 and N3-ANA-009
```

Independent checks:

- exact factorial valuations and independent prime sieve;
- theorem-defined half-span `M=max b_p log(p)/2` and full span `2M`;
- variance lower-bound reconstruction from the band `y<p<=2y`;
- monotonicity of `log(x)/(x-1)` and the half-span upper bound;
- `M/B -> 0` and the triangular-array Lindeberg argument;
- preservation of `y->infinity` and `2y<=sqrt(n)`;
- no inference from the tail CLT to a full-model Gaussian limit;
- Berry-Esseen third-moment reduction `sum E|Y_p|^3 <= M B^2`;
- two CDF endpoint errors;
- explicit coarse-window constant `K=4 C_BE/phi(2)`;
- finite diagnostic path through `n=10,000,000` classified as evidence only;
- frozen metadata and semantic checksums.

Corruption behavior:

- full span substituted for theorem half-span is rejected;
- missing `y->infinity` is rejected;
- false full-model Gaussian inference is rejected;
- finite diagnostics reported as proof are rejected;
- missing `Delta>=K M` is rejected;
- one-endpoint Berry-Esseen subtraction is rejected;
- removed Berry-Esseen dependency is rejected;
- claimed fine-window coverage below `M` is rejected.

Replay:

```bash
PYTHONPATH=src python3 src/replay_n3_high_prime.py verify \
  data/analytic/n3_high_prime_limit_audit.json
PYTHONPATH=src python3 src/replay_n3_high_prime.py verify-008 \
  certificates/analytic/n3_ana_008_final_claim.json \
  --audit data/analytic/n3_high_prime_limit_audit.json
PYTHONPATH=src python3 src/replay_n3_high_prime.py verify-009 \
  certificates/analytic/n3_ana_009_final_claim.json \
  --audit data/analytic/n3_high_prime_limit_audit.json
PYTHONPATH=src python3 src/replay_n3_high_prime.py verify-fixtures \
  tests/n3_high_prime_fixtures \
  --audit data/analytic/n3_high_prime_limit_audit.json
```

## Complete test command

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
```
