# Nova 3 restricted-source compatibility data

This package records request E of handoff `N3-HO-N4-002`.

It reconstructs the exact scope of three primary sources:

- Kevin Ford, arXiv:math/0401223v5;
- Sary Drappeau and Gérald Tenenbaum, arXiv:1604.04204v1;
- Cécile Dartyge, David Feutrie, and Gérald Tenenbaum, arXiv:2001.04435v1.

The audit distinguishes ambient counting theorems, almost-all friable theorems with exceptional sets, and common-cap ultrafriable theorems from deterministic divisor questions for the fixed sequence `n!`.

Replay:

```bash
PYTHONPATH=src python3 src/replay_n3_sources.py verify \
  data/analytic/n3_restricted_source_compatibility.json
PYTHONPATH=src python3 src/replay_n3_sources.py verify-claim \
  certificates/analytic/n3_restricted_source_compatibility.json
```

The result is a source-compatibility audit. It does not reprove the cited papers or establish any factorial divisor-density theorem.
