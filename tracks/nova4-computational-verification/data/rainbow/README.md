# Reduced-Rainbow Study B Data

Frozen source: `nova/factorial-structure@fa11f4b2cb86a2dd791df189ada12757be791804`, handoff `N1-HO-N4-001`.

Files:

- `n1_reduced_rainbow_summary_n20_n80.csv`: one exact summary row for each `20<=n<=80`;
- `n1_reduced_rainbow_index.json`: source metadata, checksums, complete residue-occupancy encoding, generation command, and first-failure pointer;
- `n1_reduced_rainbow.schema.json`: schema for the full generated audit.

The full detailed audit is generated deterministically because it includes record-gap witnesses and exact residue sets for every modulus `2<=q<=64`. Its semantic SHA-256 is:

```text
cfc5dcbcadf9e6572a94a478eafd7632551b8e657bf41b3a69129ede088ce0f7
```

Generate and replay:

```bash
PYTHONPATH=src python3 src/replay_rainbow.py audit \
  --n-min 20 --n-max 80 \
  --output-json /tmp/n1_reduced_rainbow_full.json \
  --output-csv data/rainbow/n1_reduced_rainbow_summary_n20_n80.csv \
  --output-failure certificates/rainbow/n1_reduced_rainbow_first_failure_n20.json

PYTHONPATH=src python3 src/replay_rainbow.py verify \
  /tmp/n1_reduced_rainbow_full.json
```

Result class: `computational evidence`. The exact first failure is separately labeled `disproved finite claim`.
