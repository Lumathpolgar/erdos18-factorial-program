# Nova 3 Analytic Certificates

## Tight local-ceiling certificate

The first exact equality case is `n=2`, `q=2`, `delta=0`, endpoint divisor `1`, with actual count and theorem ceiling both equal to `1`.

```bash
PYTHONPATH=src python3 src/replay_n3.py verify-local-claim \
  certificates/analytic/n3_local_ceiling_tight_n2.json
```

## Characteristic recurrence candidate

The request D candidate records the best bounded-grid recurrence found for `n=12`:

```text
q = 1,161,483
|phi_12(t)| approximately 0.9963479152311605
divisor exponent vectors = 792
```

```bash
PYTHONPATH=src python3 src/replay_n3_recurrence.py verify-candidate \
  certificates/analytic/n3_recurrence_candidate_n12.json
```

## Restricted-source compatibility certificate

The request E certificate records that none of the three audited restricted sources directly selects the deterministic factorial sequence.

```text
N3-SRC-004: Ford ambient count, direct factorial use rejected
N3-SRC-005: Drappeau–Tenenbaum method only, fixed sequence not certified
N3-SRC-006: ultrafriable common-cap model, direct factorial use rejected
```

Its exact ultrafriable witness uses `n=10`: `v_2(10!)=8`, so `256` must be included, while any common cap large enough to include `256` also includes prime `11`, which does not divide `10!`.

```bash
PYTHONPATH=src python3 src/replay_n3_sources.py verify-claim \
  certificates/analytic/n3_restricted_source_compatibility.json
```

The adversarial fixture changes the direct-use conclusion to true, recomputes the outer checksum, and must still fail semantic verification.

These certificates preserve finite evidence and source-scope decisions only. They do not prove the factorial half-range theorem.