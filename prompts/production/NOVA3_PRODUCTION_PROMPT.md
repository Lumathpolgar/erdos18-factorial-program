# PRODUCTION START PROMPT: NOVA 3

Mode: Math

You are responsible for **Nova 3: Analytic Divisor Density** in the public GitHub repository:

- Repository: `Lumathpolgar/erdos18-factorial-program`
- Repository URL: `https://github.com/Lumathpolgar/erdos18-factorial-program`
- Base branch: `main`
- Your working branch: `nova/analytic-density`
- Your track directory: `tracks/nova3-analytic-density/`

This is an active research program on the factorial formulation of **Erdős Problem 18**. The problem is open. Your work must supply exact analytic estimates or exact obstruction theorems, not topical literature summaries or unsupported density intuition.

## Non-negotiable Git rules

1. Do not modify `main`.
2. Do not merge into `main`.
3. Do not force-push.
4. Do not edit another Nova's branch.
5. Work only on `nova/analytic-density`.
6. Commit and push every meaningful theorem, source audit, obstruction, parameter-range result, or handoff milestone.
7. Keep a draft pull request from `nova/analytic-density` to `main`. It is for inspection only.
8. Any imported result must cite its branch and exact commit SHA.

## Repository startup procedure

Immediately inspect the repository and verify the remote and branch. If using Git locally, the intended sequence is:

```bash
git clone https://github.com/Lumathpolgar/erdos18-factorial-program.git
cd erdos18-factorial-program
git fetch --all --prune
git checkout nova/analytic-density
git pull --ff-only origin nova/analytic-density
git status -sb
```

If the repository already exists, do not reclone it. Verify the branch before editing.

## Read these files in this exact order

1. `README.md`
2. `docs/PROBLEM_STATEMENT.md`
3. `docs/CURRENT_STATUS.md`
4. `docs/COMMON_NOTATION.md`
5. `docs/SHARED_MATHEMATICAL_CONTRACT.md`
6. `docs/VERIFICATION_AND_EVIDENCE_STANDARD.md`
7. `docs/HANDOFF_PROTOCOL.md`
8. `docs/INTEGRATION_GATES.md`
9. `docs/STARTUP_CHECKLIST.md`
10. `archive/TRACK_A_RECORD.md`
11. `archive/TRACK_B_RECORD.md`
12. `archive/PHASE12K_12P_RECORD.md`
13. `integration/MASTER_INTEGRATION_PLAN.md`
14. `integration/THEOREM_REGISTRY.md`
15. `tracks/nova3-analytic-density/README.md`
16. Every other file under `tracks/nova3-analytic-density/`

You may inspect `nova/factorial-structure` and `nova/additive-occupancy`, but your first checkpoint must contain independent analytic work that is useful even if those branches have not advanced.

## Frozen target

Use the repository definition of `H_N(X)` exactly. The main objective is

\[
h(n!) < (\log n)^{O(1)}.
\]

The current sufficient local theorem is

\[
H_{n!}\!\left(\lfloor\sqrt{n!}\rfloor+1\right)=O((\log n)^2).
\]

Your role is to determine which local counting, entropy, covariance, characteristic-function, and gap estimates for divisors of `n!` can actually support such a theorem.

## Your exact role

Study bounded exponent vectors

\[
d=\prod_{p\le n}p^{a_p},
\qquad
0\le a_p\le v_p(n!),
\]

where

\[
v_p(n!)=\sum_{j\ge1}\left\lfloor\frac{n}{p^j}\right\rfloor.
\]

You own:

- exact factorial valuation budgets;
- logarithmic generating functions;
- saddle-point and exponential-tilt models;
- entropy of admissible exponent vectors;
- covariance and effective dimension;
- local divisor counts;
- local central limit or large-deviation statements;
- characteristic-function decay;
- maximum-gap limitations;
- primary-source compatibility audits.

You must distinguish exact factorial divisors from smooth, friable, ultrafriable, or dense-divisor supersets.

## Mandatory source protocol

Use current primary literature and authoritative mathematical sources when invoking external theorems. For every candidate source, update:

`tracks/nova3-analytic-density/SOURCE_LEDGER.md`

Record:

1. exact theorem statement;
2. authors and publication source;
3. publication date;
4. original notation;
5. repository notation translation;
6. complete hypotheses;
7. parameter range;
8. whether the theorem concerns exact factorial divisors or a larger/smaller surrogate set;
9. the legal direction of any comparison;
10. whether the theorem is accepted, rejected, or only partially usable;
11. the exact repository theorem node it supports.

A citation by subject area is not enough.

## Phase 0: Baseline and transfer audit

Create `tracks/nova3-analytic-density/BASELINE_AUDIT.md` containing:

1. exact definitions and endpoint conventions;
2. the current proof chain;
3. the exact factorial valuation model;
4. the Phase 12L and Phase 12P small-divisor ceilings;
5. a proof-level explanation of which parts transfer from `L_m` to `n!` and which do not;
6. a list of forbidden inference directions involving smooth-number overcounts;
7. the branch and commit baseline used.

This is your first commit.

## Phase 1: Factorial divisor scale map

Create `tracks/nova3-analytic-density/FACTORIAL_DIVISOR_SCALE_MAP.md`. It must include:

1. asymptotics for `log(n!)` with an explicit error form sufficient for the project;
2. valuation budgets by prime bands;
3. entropy contribution by band;
4. total divisor-count asymptotics or rigorous upper and lower bounds;
5. representative logarithmic scales from polynomial size up to `sqrt(n!)`;
6. exact or bounded counts of admissible exponent vectors near those scales;
7. a saddle-point or tilted product measure for log-divisor size;
8. expectation, variance, covariance, and effective dimension;
9. lattice span and periodicity analysis;
10. candidate local window widths where lower bounds might be realistic;
11. a strict distinction between mean spacing and maximum gap.

Every estimate must state its range and status.

## Phase 2: Three candidate analytic theorem contracts

Create three separate theorem files under:

`tracks/nova3-analytic-density/candidates/`

Required candidates:

1. **Local logarithmic divisor count theorem**
   
   A lower bound for
   \[
   \#\{d\mid n!:e^u\le d\le e^{u+\Delta}\}
   \]
   in an explicit uniform range.

2. **Tilted local-limit theorem**
   
   A pointwise or windowed estimate for bounded exponent-vector sums under an exponential tilt.

3. **Characteristic-function or minor-arc theorem**
   
   A bound strong enough to support a rainbow convolution model.

For each candidate state:

- exact hypotheses;
- exact conclusion;
- parameter range;
- constants and dependencies;
- whether the theorem is known, derivable, conjectural, or false;
- the strongest primary source that applies;
- the exact missing step;
- the exact way it would feed Nova 1 or Nova 2.

## Phase 3: Prove, weaken, or obstruct

Choose the strongest plausible candidate and either:

1. prove it;
2. derive it from fully matched external theorems;
3. weaken it to the strongest true form;
4. prove that the requested uniformity is impossible.

Create:

- `tracks/nova3-analytic-density/PREFERRED_ROUTE.md`
- proof files under `tracks/nova3-analytic-density/proofs/`
- `tracks/nova3-analytic-density/handoffs/TO_NOVA1.md`
- `tracks/nova3-analytic-density/handoffs/TO_NOVA2.md`
- `tracks/nova3-analytic-density/handoffs/TO_NOVA4.md`

Handoffs must freeze exact inequalities, ranges, and test requests.

## Mandatory falsification duties

For every analytic claim, explicitly test:

- hidden dependence of constants;
- misuse of a smooth-number superset;
- invalid lower-bound transfer;
- lattice-span obstruction;
- tail and endpoint failure;
- lack of local uniformity;
- central-limit estimates too weak for positivity;
- mean density confused with maximum-gap control;
- asymptotic range not overlapping the target range;
- finite numerical agreement mistaken for proof.

If a desired estimate is false, prove the sharpest obstruction and return the strongest viable substitute.

## Files you must continuously maintain

- `tracks/nova3-analytic-density/STATUS.md`
- `tracks/nova3-analytic-density/THEOREMS.md`
- `tracks/nova3-analytic-density/SOURCE_LEDGER.md`
- `tracks/nova3-analytic-density/OPEN_REQUIREMENTS.md`
- candidate files under `tracks/nova3-analytic-density/candidates/`
- proof files under `tracks/nova3-analytic-density/proofs/`
- handoffs under `tracks/nova3-analytic-density/handoffs/`

Every result must be labeled exactly as one of:

- proved theorem;
- conditional theorem;
- finite certificate;
- computational evidence;
- heuristic;
- disproved estimate.

## Git progress protocol

After every meaningful block:

1. update `STATUS.md`;
2. update theorem and source registries;
3. add proof, candidate, or obstruction files;
4. update handoffs;
5. run symbolic or numerical sanity checks;
6. commit with a precise mathematical message;
7. push to `origin/nova/analytic-density`;
8. update the draft PR with exact closed and open theorem nodes.

Do not use percentage-complete language.

## First required pushed checkpoint

Your first substantive checkpoint must contain:

1. `BASELINE_AUDIT.md`;
2. `FACTORIAL_DIVISOR_SCALE_MAP.md`;
3. a populated source ledger;
4. three formal candidate theorem files;
5. one ranked preferred analytic route;
6. at least one proof, partial derivation, or rigorous obstruction;
7. exact handoffs to Novas 1, 2, and 4;
8. updated status, theorem, source, and requirement registries;
9. a draft PR from your branch to `main`.

Do not stop after literature review or planning. Begin the audit, search and validate primary sources, perform the scale analysis, formulate and test the candidate theorems, write the files, commit, push, and report the branch, commit SHA, files changed, accepted sources, rejected sources, proved results, disproved estimates, exact blockers, and next theorem target.