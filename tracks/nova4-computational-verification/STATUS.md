# Nova 4 Status

Date: 2026-07-16

## Track

Computation, Falsification, and Verification

## Branch

`nova/computational-verification`

## Overall state

`READY_TO_MERGE_SUBJECT_TO_CURRENT_HEAD_GREEN_GATE_AND_AUTHORIZED_APPROVAL`

## Completed research package

All theorem IDs requested in frozen handoff `N3-HO-N4-002` have independent Nova 4 decisions:

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

The track preserves exact finite representation profiles through `n=13`, lattice and reduced-model counterexamples, complete finite threshold sweeps, source-scope audits, recurrence evidence, proof audits, and fail-closed semantic certificates.

## Final Nova 3 closure

`N3-ANA-008` proves the separately truncated high-prime-tail central limit theorem under `y->infinity` and `2y<=sqrt(n)`.

`N3-ANA-009` proves the coarse-window lower bound only when `Delta>=K M_{n,y}`, with `K=4 C_BE/phi(2)`, and retains the external Berry-Esseen dependency.

```text
high-prime audit SHA-256: a9c089489b38990c6de044611a21d8a488166dd0ad570456fee54a0020dc9dd2
N3-ANA-008 claim SHA-256: 5723c037725e1bc262bd109b65510d74833a28d8869f27903cd86c33473bf930
N3-ANA-009 claim SHA-256: b3775b62ef887fbaa92e39e1ab729d6f093f360d778edfdc4a52a2a1e3397d7d
```

## Integration gate

The exact GitHub-generated PR merge tree was executed by the repository workflow:

```text
workflow: Nova 4 integration gate
run id: 29513110373
run number: 6
PR merge commit tested: b612eef02c6b825bb4057840eee00e7abe3b9067
candidate head tested: 5d297a8f8c4e599245701c651fd42670a8bcfb3c
main head tested: 7ef3ce6238bbf820be346b5beb2fa8b97b12789e
job conclusion: success
```

Successful steps:

```text
checkout exact PR merge ref
record merge-tree snapshot
compile all Nova 4 source and test files
run complete Nova 4 unittest discovery suite
cleanup
```

The workflow reruns on every later candidate push and relevant PR synchronization. Therefore the current branch remains ready to merge only while the latest workflow run for the current head is green.

## Pull-request state

```text
PR: #4
state: open
ready for review: true
merged: false
GitHub mergeable: true
unresolved inline review threads: 0
submitted reviews requesting changes: 0
```

No merge into `main` has been performed by Nova 4. The final merge requires an authorized integration action and must use the exact head covered by the latest successful workflow run.

## Scientific limitations

- No asymptotic factorial half-range theorem is proved.
- No artifact proves profile injectivity, distinct numerical sums, or additive occupancy.
- Request G remains a finite certificate.
- Request C remains computational evidence and its frozen ratio is `2M/B`, not `M/B`.
- `N3-ANA-009` does not reach windows below the largest-coordinate scale.
- The `n=14` exact representation profile remains unknown due to resource limits.
