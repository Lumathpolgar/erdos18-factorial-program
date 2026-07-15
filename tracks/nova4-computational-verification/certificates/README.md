# Representation Certificates

Result class: `finite certificate`

Each certificate uses exact integer arithmetic and the schema:

```text
erdos18.factorial.representation.v1
```

The verifier ignores labels as mathematical identities and rejects repeated numerical divisor values even when labels differ.

Replay all certificates:

```bash
PYTHONPATH=src python3 src/replay.py verify-tree certificates
```
