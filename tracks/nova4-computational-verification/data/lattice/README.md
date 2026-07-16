# Lattice Audit Data

`n2_obs_107_range_n3_n10000.json` is an exact finite theorem audit of every integer `3 <= n <= 10000` for the side conditions used in the frozen `N2-OBS-107` witness.

Generation command:

```bash
PYTHONPATH=src python3 src/replay.py audit-n2-obs-107 \
  --n-min 3 --n-max 10000 \
  --output data/lattice/n2_obs_107_range_n3_n10000.json
```

The dataset does not promote finite success to an asymptotic theorem.
