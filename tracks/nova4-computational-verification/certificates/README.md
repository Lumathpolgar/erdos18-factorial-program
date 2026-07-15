# Nova 4 Certificates

Representation certificates are stored in this directory root. Specialized certificate families are stored in subdirectories.

## Representation replay

```bash
PYTHONPATH=src python3 src/replay.py verify-tree certificates
```

The representation verifier ignores labels as mathematical identities and rejects repeated numerical divisor values even when labels differ.

## Lattice replay

```bash
PYTHONPATH=src python3 src/replay.py verify-n2-obs-107 \
  certificates/lattice/n2_obs_107_n1892.json
```

See `certificates/lattice/README.md` for the explicit label-family verifier.

## Capacity replay

```bash
PYTHONPATH=src python3 src/replay.py verify-n1-capacity \
  certificates/capacity/n1_capacity_audit_n3_n1000000.json
```

See `certificates/capacity/README.md` for the frozen source and independent recomputation contract.

## Reduced-rainbow replay

```bash
PYTHONPATH=src python3 src/replay_rainbow.py verify-failure \
  certificates/rainbow/n1_reduced_rainbow_first_failure_n20.json
```

See `certificates/rainbow/README.md` for the exact frozen Study B scope and corruption-rejection contract.
