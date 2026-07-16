# Nova 3 Analytic Certificates

## Tight local-ceiling certificate

The tight local-ceiling certificate records the first exact equality case:

```text
n = 2
q = 2
delta = 0
endpoint divisor = 1
actual count = theorem ceiling = 1
```

Replay:

```bash
cd tracks/nova4-computational-verification
PYTHONPATH=src python3 src/replay_n3.py verify-local-claim \
  certificates/analytic/n3_local_ceiling_tight_n2.json
```

The adversarial fixture lowers the certified upper bound by one, recomputes its outer checksum, and must still fail semantic verification.

## Characteristic recurrence candidate

The request D candidate certificate records the best bounded-grid recurrence found for `n=12`:

```text
q = 1,161,483
t approximately 1.0528518509e7
|phi_12(t)| approximately 0.9963479152311605
divisor exponent vectors = 792
```

Frozen source:

```text
handoff: N3-HO-N4-002
handoff commit: 7469dada02fa4caca08ed391ef8b0cb0f1e855b2
proof commit: ff57005b975c4917341306bd0eceb6d05a9b18f6
object: N3-ANA-007
```

Replay:

```bash
PYTHONPATH=src python3 src/replay_n3_recurrence.py verify-candidate \
  certificates/analytic/n3_recurrence_candidate_n12.json
```

The verifier recomputes every high-precision coordinate factor, the product modulus, phase residuals, exact divisor-vector count, and the independent direct-vector average. The adversarial fixture changes the modulus to one, recomputes the outer checksum, and must still fail semantic verification.

This candidate is computational evidence only. It is not a proof of the unbounded recurrence theorem or a certified maximum outside the declared grid.
