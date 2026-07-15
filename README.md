# Erdős 18 Factorial Program

A collaborative proof program for the factorial formulation of Erdős Problem 18.

## Primary target

Let `h(N)` denote the least integer such that every integer below the practical number `N` can be written as a sum of at most `h(N)` distinct divisors of `N`.

The primary objective is to prove

```text
h(n!) < (log n)^{O(1)}.
```

The current conditional endgame would follow from the direct factorial half-range theorem

```text
H_{n!}(floor(sqrt(n!)) + 1) = O((log n)^2),
```

which would yield

```text
h(n!) = O((log n)^3).
```

## Current status

The problem is not solved.

A complete conditional Track B has been built and independently audited. It converts a suitable half-range representation theorem into a polylogarithmic bound for `h(n!)`.

The prior Track A program studied the stronger lcm core

```text
L_m = lcm(1, 2, ..., m).
```

Phases 12K through 12P rigorously eliminated several plausible greedy and sequential additive mechanisms. Those negative results are retained because they prevent repeated work and clarify what a successful proof must avoid.

The program is now attacking the richer divisor lattice of `n!` directly through four parallel Nova tracks.

## Four Nova tracks

1. [Nova 1: Factorial Structure and Reduction](tracks/nova1-factorial-structure/README.md)
2. [Nova 2: Additive Occupancy and Global Sumsets](tracks/nova2-additive-occupancy/README.md)
3. [Nova 3: Analytic Divisor Density](tracks/nova3-analytic-density/README.md)
4. [Nova 4: Computation, Falsification, and Verification](tracks/nova4-computational-verification/README.md)

The full operating plan is in [FOUR_NOVA_PARALLEL_PROGRAM.md](docs/FOUR_NOVA_PARALLEL_PROGRAM.md).

## Required shared documents

- [Problem statement](docs/PROBLEM_STATEMENT.md)
- [Current status](docs/CURRENT_STATUS.md)
- [Common notation](docs/COMMON_NOTATION.md)
- [Shared mathematical contract](docs/SHARED_MATHEMATICAL_CONTRACT.md)
- [Research rules](docs/RESEARCH_RULES.md)
- [Verification and evidence standard](docs/VERIFICATION_AND_EVIDENCE_STANDARD.md)
- [Cross-track handoff protocol](docs/CROSS_TRACK_HANDOFF_PROTOCOL.md)
- [Integration gates](docs/INTEGRATION_GATES.md)
- [Startup checklist](docs/STARTUP_CHECKLIST.md)

## Integration

- [Master integration plan](integration/MASTER_INTEGRATION_PLAN.md)
- [Theorem registry](integration/THEOREM_REGISTRY.md)
- [Handoff queue](integration/HANDOFF_QUEUE.md)

## Repository map

- `docs/`: definitions, contracts, protocols, templates, and current status
- `archive/`: indexed historical research records for Track A, Track B, and Phases 12K through 12P
- `tracks/`: the four independent Nova workspaces
- `integration/`: cross-track theorem integration and final proof audits
- `.github/`: pull-request review standard

The original ZIP packages remain source artifacts outside this repository for now. Their mathematical status and contents are indexed under `archive/`.

## Truth-status rule

Every result must be labeled as exactly one of:

1. proved theorem
2. conditional theorem
3. finite certificate
4. computational evidence
5. heuristic
6. failed conjecture or disproved route
7. open

No finite computation, heuristic, conditional implication, or percentage-complete estimate may be presented as an unconditional solution.

## Branch policy

No Nova works directly on `main`.

- `nova/factorial-structure`
- `nova/additive-occupancy`
- `nova/analytic-density`
- `nova/computational-verification`

Launch prompts will be written only after the repository operating system is reviewed and accepted.
