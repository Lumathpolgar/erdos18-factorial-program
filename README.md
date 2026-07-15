# Erdős 18 Factorial Program

A collaborative proof program for the factorial formulation of Erdős Problem 18.

## Primary target

Let `h(N)` denote the least integer such that every integer below the practical number `N` can be written as a sum of at most `h(N)` distinct divisors of `N`.

The primary objective is to prove

```text
h(n!) < (log n)^{O(1)}.
```

The current conditional endgame would follow from a direct factorial half-range theorem of the form

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

The program is now pivoting to a direct attack on the richer divisor lattice of `n!`.

## Repository map

- `docs/`: current definitions, status, proof dependencies, and research rules
- `archive/packages/`: complete historical research packages
- `archive/phase12K-12P/`: late Track A gate packages
- `tracks/`: workspace for the four parallel Nova research tracks
- `integration/`: cross-track theorem integration and final proof audits

## Truth-status rule

Every result must be labeled as exactly one of:

1. proved theorem
2. conditional theorem
3. finite certificate
4. computational evidence
5. heuristic
6. failed conjecture or disproved route

No finite computation, heuristic, or conditional implication may be presented as an unconditional solution.

## Immediate next step

Create four independent Nova assignments for:

1. factorial divisor structure and reductions
2. additive occupancy and global sumsets
3. analytic divisor density
4. computation, falsification, and verification
