# Nova 4 Merge-Readiness Audit

Date: 2026-07-16

## Disposition

```text
research milestone: COMPLETE
scientific package: READY FOR INTEGRATION
Git conflict status: MERGEABLE
runtime integration status: NOT YET VALIDATED
final recommendation: DO NOT MERGE YET
```

The branch has reached a stable, meaningful checkpoint. All theorem IDs requested in `N3-HO-N4-002` have independent decisions, the exact finite datasets and certificates are committed, and all known theorem-scope restrictions are explicit.

The remaining blocker is an integration-validation blocker, not an unfinished mathematical audit.

## Frozen integration snapshot

```text
repository: Lumathpolgar/erdos18-factorial-program
base branch: main
working branch: nova/computational-verification
pull request: #4
candidate status head: 89e95dea30c1ccb5a5139ff21cbc9dde2931d240
current main head inspected: 7ef3ce6238bbf820be346b5beb2fa8b97b12789e
common merge base: cd5576d4f7934e26e9d4ef3b065c2ad4cee36c67
candidate commits beyond current main: 268
current main commits absent from candidate: 350
```

The very large behind count arose because `main` integrated substantial Nova 1 and Nova 2 research while Nova 4 remained on its isolated branch.

## Pull-request state

At the inspected snapshot:

```text
state: open
draft: true
merged: false
GitHub mergeable: true
changed files: 216
additions: 13,870
deletions: 0
unresolved inline review threads: 0
submitted reviews: 0
```

Every changed file in PR #4 is under:

```text
tracks/nova4-computational-verification/
```

The current `main` changes inspected by reverse comparison are in repository documentation, prompts, Nova 1, and Nova 2 paths. No overlapping Nova 4 path was found. This explains the conflict-free mergeability result.

## Completed theorem decisions

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

Final high-prime closure:

```text
B_ny^2 >> n^2 log(y)/y
M_ny = max_{p>y} b_p log(p)/2
M_ny/B_ny -> 0
T_ny/B_ny => N(0,1)
Delta >= (4 C_BE/phi(2)) M_ny gives the coarse central-window lower bound
```

Semantic hashes:

```text
N3-ANA-008/009 audit: a9c089489b38990c6de044611a21d8a488166dd0ad570456fee54a0020dc9dd2
N3-ANA-008 claim: 5723c037725e1bc262bd109b65510d74833a28d8869f27903cd86c33473bf930
N3-ANA-009 claim: b3775b62ef887fbaa92e39e1ab729d6f093f360d778edfdc4a52a2a1e3397d7d
```

## Test evidence available

The branch records passing isolated or component runs for every verifier family. The final high-prime package has:

```text
13 isolated tests passing
8 committed semantic corruptions rejected
audit replay passing
N3-ANA-008 claim replay passing
N3-ANA-009 claim replay passing
```

Historical component suites for the earlier checkpoints also record passing runs.

## Missing merge evidence

The final candidate commit has:

```text
configured commit status checks: none
pull-request workflow runs: none
```

A fresh complete Nova 4 test replay has not been run against the final combined tree formed from current `main` and PR #4. The execution environment used for this audit could not clone the public repository because DNS resolution for `github.com` was unavailable, so this gate could not be completed locally.

GitHub's `mergeable=true` result checks merge conflicts. It does not execute the Python verifier suite and does not establish compatibility with the 350 newer `main` commits.

## Required integration replay

From a fresh checkout containing current `main` plus PR #4:

```bash
PYTHONPATH=tracks/nova4-computational-verification/src \
python3 -m unittest discover \
  -s tracks/nova4-computational-verification/tests -v
```

Any repository-level checks introduced on current `main` must also pass.

The final integration operator should verify that the PR remains confined to the Nova 4 track, inspect the generated merge commit, and preserve all finite, conditional, and non-occupancy scope language.

## Merge decision rule

The branch becomes ready to merge only when all of the following are true:

1. the combined-tree full Nova 4 suite passes;
2. any repository-level checks pass;
3. GitHub continues to report the PR mergeable;
4. no new unresolved review thread or requested change exists;
5. the exact head tested is the exact head merged;
6. an authorized integration action explicitly approves the merge.

Until then, PR #4 should remain draft and unmerged.

## Scope preserved

This integration checkpoint does not claim that the factorial half-range theorem is proved. It does not claim profile injectivity, distinct numerical sums, additive occupancy, or a solution to Erdős Problem 18. The exact `n=14` profile remains unknown due to resource limits.
