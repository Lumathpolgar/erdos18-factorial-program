# Nova 4 Certificates

Representation certificates are stored in this directory root. Lattice and occupancy certificates are stored under `certificates/lattice/`.

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
