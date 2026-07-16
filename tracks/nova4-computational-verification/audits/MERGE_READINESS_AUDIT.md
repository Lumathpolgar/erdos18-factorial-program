# Nova 4 Merge-Readiness Audit

Date: 2026-07-16

## Disposition

```text
research milestone: COMPLETE
scientific package: READY FOR INTEGRATION
Git conflict status: MERGEABLE
runtime integration status: VALIDATED ON THE GITHUB PR MERGE TREE
final recommendation: READY TO MERGE AFTER AUTHORIZED INTEGRATION APPROVAL
```

All theorem IDs requested in `N3-HO-N4-002` have independent Nova 4 decisions. Exact finite datasets, proof audits, source audits, counterexamples, semantic certificates, corruption fixtures, and replay tools are committed. Every known scope restriction remains explicit.

The integration blocker recorded in the previous revision has been removed by an actual GitHub Actions run on the generated pull-request merge commit.

## Authoritative integration evidence

Workflow:

```text
name: Nova 4 integration gate
file: .github/workflows/nova4-integration.yml
run id: 29513110373
run number: 6
event: pull_request ready_for_review
conclusion: success
```

The successful run checked out GitHub's generated PR merge ref:

```text
refs/remotes/pull/4/merge
merge commit tested: b612eef02c6b825bb4057840eee00e7abe3b9067
candidate head tested: 5d297a8f8c4e599245701c651fd42670a8bcfb3c
current main head in the tested merge: 7ef3ce6238bbf820be346b5beb2fa8b97b12789e
```

The checkout log confirms that GitHub fetched the current repository branches and the exact PR merge ref, then detached at that merge revision.

The authoritative job completed every step successfully:

```text
checkout tested revision: success
record GitHub pull-request merge tree: success
compile all Nova 4 sources and tests: success
run complete Nova 4 verifier suite: success
cleanup: success
job conclusion: success
```

A separate push-triggered combined-tree run also completed successfully. The pull-request run is authoritative because it uses GitHub's exact generated merge commit.

## Continuous exact-head rule

This audit is followed by a documentation-only closure commit. The workflow is configured to rerun on every push to `nova/computational-verification` and on every relevant PR synchronization.

The branch is ready to merge only while the latest `Nova 4 integration gate` run for the current PR head is successful. Any later branch or `main` change requires a new successful run. The exact head merged must be the exact current head covered by the latest green gate.

## Pull-request state at closure

```text
repository: Lumathpolgar/erdos18-factorial-program
base branch: main
working branch: nova/computational-verification
pull request: #4
state: open
ready for review: true
merged: false
GitHub mergeable: true
unresolved inline review threads: 0
submitted reviews requesting changes: 0
```

The PR adds the Nova 4 track and one narrowly scoped integration workflow. The newer `main` work is concentrated in repository documentation, prompts, Nova 1, and Nova 2 paths. GitHub reports the PR conflict-free.

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

## Merge decision rule

The integration gate is satisfied when all of the following remain true:

1. the latest combined-tree Nova 4 workflow run succeeds;
2. GitHub continues to report the PR mergeable;
3. no unresolved requested change or review thread appears;
4. the exact current head is the exact head merged;
5. an authorized integration action explicitly approves the merge.

Conditions 1 through 4 are satisfied at this checkpoint, subject to the automatic exact-head rerun after the final documentation commit. Condition 5 belongs to the authorized integration operator.

## Scope preserved

This integration checkpoint does not claim that the factorial half-range theorem is proved. It does not claim profile injectivity, distinct numerical sums, additive occupancy, or a solution to Erdős Problem 18. The exact `n=14` profile remains unknown due to resource limits.
