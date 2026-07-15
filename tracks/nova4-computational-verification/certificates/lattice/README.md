# Lattice and Occupancy Certificates

The files in this directory are verified independently of solver metadata.

## Frozen Nova 2 regression

```bash
PYTHONPATH=src python3 src/replay.py verify-n2-obs-107 \
  certificates/lattice/n2_obs_107_n1892.json
```

The certificate recomputes the logarithmic ceilings using rigorous rational bounds, recomputes `v_2(n!)`, verifies the frozen source SHAs, and checks that the entire target window is disjoint from the common support lattice.

## Explicit label-family verifier

```bash
PYTHONPATH=src python3 src/replay.py verify-label-family \
  tests/lattice_fixtures/valid_common_gcd_failure.json
```

The verifier checks factorial divisibility, target range, duplicates within and across labels, correction collisions, common gcd, reachable residues, and exact finite window coverage.
