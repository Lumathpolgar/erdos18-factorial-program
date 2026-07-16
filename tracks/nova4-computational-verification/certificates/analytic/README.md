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

```bash
PYTHONPATH=src python3 src/replay_n3_sources.py verify-claim \
  certificates/analytic/n3_restricted_source_compatibility.json
```

## Dusart prime-interval theorem certificate

The request F certificate records the independently accepted theorem:

```text
N3-ANA-010: ACCEPTED
pi(n)-pi(n/2) >= n/(3 log n) for every integer n>=120368
source thresholds: 5393 and 60184
endpoint prime count: 5254
```

```bash
PYTHONPATH=src python3 src/replay_n3_dusart.py verify-claim \
  certificates/analytic/n3_dusart_prime_interval_claim.json \
  --audit data/analytic/n3_dusart_prime_interval_audit.json
```

## Exact threshold-sweep certificate

The request G certificate records the exact minima over every integer `120368 <= n <= 1000000`:

```text
minimum prime margin: n=120370
minimum Legendre proof margin: n=131071
minimum address slack: 57942 at n=120368..120371
minimum capacity margin: n=120370
```

```bash
PYTHONPATH=src python3 src/replay_n3_threshold.py verify-claim \
  certificates/analytic/n3_threshold_sweep_claim.json \
  --audit data/analytic/n3_threshold_sweep_n120368_n1000000.json
```

The committed adversarial fixture lowers the exact minimum address slack, recomputes the outer checksum, and must still fail semantic verification.

These certificates preserve finite evidence, source-scope decisions, theorem audits, and finite sweep results. They do not prove the factorial half-range theorem, formal-profile injectivity, or additive occupancy.
