# Nova 3 request G threshold sweep

This finite certificate checks every integer `120368 <= n <= 1000000`.

It independently verifies exact upper-half prime counts, two exact formulas for `v_2(n!)`, rationally certified ceilings for `r_n=ceil(4 log n)` and `M_n=ceil(16(log n)^2)`, address legality, and the conservative formal-profile capacity exponent.

Replay:

```bash
PYTHONPATH=src python3 src/replay_n3_threshold.py verify \
  data/analytic/n3_threshold_sweep_n120368_n1000000.json
PYTHONPATH=src python3 src/replay_n3_threshold.py verify-claim \
  certificates/analytic/n3_threshold_sweep_claim.json \
  --audit data/analytic/n3_threshold_sweep_n120368_n1000000.json
```

The committed adversarial fixture lowers the exact minimum address slack, recomputes its outer checksum, and must still fail semantic verification.

This is a finite certificate only. It does not prove distinct numerical profile sums, additive occupancy, the factorial half-range theorem, or Erdős Problem 18.
