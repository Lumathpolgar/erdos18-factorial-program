# Reduced-Rainbow Certificates

Frozen source:

```text
branch: nova/factorial-structure
commit: fa11f4b2cb86a2dd791df189ada12757be791804
handoff: N1-HO-N4-001, Study B
```

The first-failure certificate records the lexicographically first exact occupancy failure in the audited range `20 <= n <= 80`.

```text
n = 20
r_star = 3
M_star = 5
common gcd = 16
correction radius = 7
first target = 8
empty downward window = [1,8]
```

Replay command:

```bash
cd tracks/nova4-computational-verification
PYTHONPATH=src python3 src/replay_rainbow.py verify-failure \
  certificates/rainbow/n1_reduced_rainbow_first_failure_n20.json
```

The verifier recomputes the entire `n=20` reduced family, exact bitset support, factorial divisibility, layer addresses, numerical distinctness, witness rules, and the independent common-lattice obstruction. It rejects altered claims even when the attacker recomputes the outer checksum.

Result class: `disproved finite claim` for the exact frozen reduced model only.
