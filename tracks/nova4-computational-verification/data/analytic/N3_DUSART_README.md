# Nova 3 Dusart source audit

Request F independently reconstructs the exact use of Pierre Dusart's Theorem 6.9 in `N3-ANA-010`.

Frozen Nova 3 source:

```text
handoff: N3-HO-N4-002
handoff commit: 7469dada02fa4caca08ed391ef8b0cb0f1e855b2
source-ledger commit: 697e7ed8bdb03f54b2389b2fcdd8b685dadcebc4
proof file blob: e36daf98db86da16bd5ed8c6c82f43530d745f66
```

Primary source:

```text
Pierre Dusart
Estimates of Some Functions Over Primes without R.H.
arXiv:1002.0442v1
Theorem 6.9, equation (6.6), PDF page 9
```

Replay:

```bash
PYTHONPATH=src python3 src/replay_n3_dusart.py generate \
  --audit /tmp/n3_dusart_prime_interval_audit.json \
  --claim /tmp/n3_dusart_prime_interval_claim.json
PYTHONPATH=src python3 src/replay_n3_dusart.py verify \
  data/analytic/n3_dusart_prime_interval_audit.json
PYTHONPATH=src python3 src/replay_n3_dusart.py verify-claim \
  certificates/analytic/n3_dusart_prime_interval_claim.json \
  --audit data/analytic/n3_dusart_prime_interval_audit.json
```

The audit accepts `N3-ANA-010`. The threshold `120368` is the smallest integer threshold supplied directly by the two unsupplemented source hypotheses because the upper estimate is applied at `n/2` and requires `n/2>=60184`. It is not claimed to be the smallest possible theorem threshold after finite supplementation.
