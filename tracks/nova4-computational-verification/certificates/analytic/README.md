# Nova 3 Analytic Certificates

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
