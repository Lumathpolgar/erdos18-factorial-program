# Nova 4 Status

Date: 2026-07-16

## Track

Computation, Falsification, and Verification

## Branch

`nova/computational-verification`

## Overall state

`READY_FOR_INTEGRATION_TESTING_NOT_YET_READY_TO_MERGE`

## Completed research package

All theorem IDs requested in frozen handoff `N3-HO-N4-002` now have independent Nova 4 decisions:

```text
N3-ANA-004: ACCEPTED
N3-ANA-005: ACCEPTED
N3-ANA-006: ACCEPTED
N3-ANA-007: ACCEPTED
N3-ANA-008: ACCEPTED
N3-ANA-009: ACCEPTED_WITH_EXTERNAL_BERRY_ESSEEN_DEPENDENCY
N3-ANA-010: ACCEPTED
N3-ANA-011: ACCEPTED_WITH_FORMAL_PROFILE_ONLY_SCOPE
```

The track also preserves exact finite representation profiles through `n=13`, lattice and reduced-model counterexamples, complete finite threshold sweeps, source-scope audits, recurrence evidence, and fail-closed semantic certificates.

## Final Nova 3 closure

`N3-ANA-008` proves the separately truncated high-prime tail central limit theorem under `y->infinity` and `2y<=sqrt(n)`.

`N3-ANA-009` proves the coarse-window lower bound only when `Delta>=K M_{n,y}`, with `K=4 C_BE/phi(2)`, and retains the external Berry-Esseen dependency.

```text
high-prime audit SHA-256: a9c089489b38990c6de044611a21d8a488166dd0ad570456fee54a0020dc9dd2
N3-ANA-008 claim SHA-256: 5723c037725e1bc262bd109b65510d74833a28d8869f27903cd86c33473bf930
N3-ANA-009 claim SHA-256: b3775b62ef887fbaa92e39e1ab729d6f093f360d778edfdc4a52a2a1e3397d7d
```

## Merge-readiness findings

```text
PR: #4
PR state: open and draft
GitHub mergeable: true
unresolved inline review threads: 0
submitted reviews: 0
configured commit status checks: 0
pull-request workflow runs on final candidate head: 0
PR changed files: 216
files outside tracks/nova4-computational-verification/: 0
common merge base: cd5576d4f7934e26e9d4ef3b065c2ad4cee36c67
current main head inspected: 7ef3ce6238bbf820be346b5beb2fa8b97b12789e
candidate content head before this status record: 1ef9c1a8dc8faf766b7d22e100b04c1315734f2c
candidate branch commits beyond current main: 268
current main commits absent from candidate branch: 350
```

GitHub reports the PR conflict-free because the branch changes are confined to the Nova 4 track and the newer `main` work is outside that path. However, conflict-free does not certify runtime compatibility.

## Blocking integration gate

A fresh full-repository replay has not been run on the final combined state of current `main` plus PR #4. The final candidate head has no configured CI checks and no GitHub Actions workflow run.

Therefore this branch is ready for integration testing, but Nova 4 does not yet recommend merging it into `main`.

Required final command from a fresh combined checkout:

```bash
PYTHONPATH=tracks/nova4-computational-verification/src \
python3 -m unittest discover \
  -s tracks/nova4-computational-verification/tests -v
```

Any repository-level integration tests must also pass. After that replay, the PR can leave draft status and be considered for an authorized merge.

## Scientific limitations

- No asymptotic factorial half-range theorem is proved.
- No artifact proves profile injectivity, distinct numerical sums, or additive occupancy.
- Request G remains a finite certificate.
- Request C remains computational evidence and its frozen ratio is `2M/B`, not `M/B`.
- `N3-ANA-009` does not reach windows below the largest coordinate scale.
- The `n=14` exact representation profile remains unknown due to resource limits.
