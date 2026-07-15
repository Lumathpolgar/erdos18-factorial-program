# Nova 4 Baseline Audit

Date: 2026-07-15

Result class: `exact finite theorem audit`

## Frozen definitions

For a positive integer `N`,

```text
D(N) = {d in Z_{>0} : d divides N}.
```

For an integer `x >= 0`,

```text
lambda_N(x) = min{|S| : S subset D(N), sum(S) = x},
```

where selected divisors are numerically distinct, the empty set represents `0`, and `lambda_N(x) = infinity` when no representation exists.

For real `X >= 1`,

```text
H_N(X) = max_{0 <= x < X, x integer} lambda_N(x).
```

For practical `N`, `h(N) = H_N(N)`.

For the factorial program:

```text
N_n = n!
X_n = floor(sqrt(n!))
v_p(n!) = sum_{j >= 1} floor(n / p^j)
```

The local target uses the inclusive integer range

```text
0 <= x <= floor(sqrt(n!)),
```

which is exactly the argument

```text
H_{n!}(floor(sqrt(n!)) + 1).
```

## Frozen target and proof chain

The main objective remains open:

```text
h(n!) < (log n)^{O(1)}.
```

The current sufficient local statement is also open:

```text
H_{n!}(floor(sqrt(n!)) + 1) = O((log n)^2).
```

The archived Track B implication is conditional and requires reconstruction under the frozen endpoint convention:

```text
H_{n!}(floor(sqrt(n!)) + 1) = O((log n)^2)
    implies
h(n!) = O((log n)^3).
```

No computation in this track is an asymptotic proof of either statement.

## Branch baseline

| Ref | Exact commit SHA | Relation to current `main` at startup |
|---|---|---|
| `main` | `68ace6c9c3b67636e298a406fee3bfe8e072741d` | baseline head |
| `nova/computational-verification` | `2acd1e4bb0853eda49c1a42e6080fcbaeec9dcc4` | 5 commits ahead, 12 behind, diverged |
| merge base | `cd5576d4f7934e26e9d4ef3b065c2ad4cee36c67` | common ancestor |
| `nova/factorial-structure` | `f2e011d689d56af07ed01de08e00c05457ca9c80` | frozen upstream audit head |
| `nova/additive-occupancy` | `71370633b1e6726bf6f9e3b334d42cfc34512c06` | frozen upstream audit head |
| `nova/analytic-density` | `c79cddee6e8940e27ff256c29a85a3fc93766f7b` | frozen upstream audit head |

The assigned branch cannot be updated from `main` by `git pull --ff-only` because it has diverged. No merge, rebase, force update, or edit to another branch is authorized or performed.

## Source audit

The required startup documents were read in the requested order. One path mismatch was found:

```text
docs/HANDOFF_PROTOCOL.md
```

does not exist. The operative repository document is:

```text
docs/CROSS_TRACK_HANDOFF_PROTOCOL.md
```

The track directory contained only:

```text
README.md
STATUS.md
DATASETS.md
VERIFIER_REGISTRY.md
COUNTEREXAMPLES.md
OPEN_REQUIREMENTS.md
```

No source implementation, tests, certificate schemas, certificates, machine-readable datasets, environment specification, benchmark report, request queue, or audit artifact existed at startup.

The historical ZIP packages named in `archive/` are indexed but are not present in the repository. No historical source code or certificate was imported into this checkpoint.

## Evidence language

This track uses the following exact labels:

- `exact finite theorem audit`: exhaustive exact verification of a frozen finite domain.
- `finite certificate`: a finite witness with an independently replayable verifier.
- `certified upper bound`: a verified construction proving a finite upper bound.
- `certified lower bound`: a rigorous finite exclusion of all smaller values.
- `computational evidence`: reproducible finite data that does not exhaust the stated claim.
- `heuristic`: an unproved model or search guide.
- `counterexample`: an exact witness refuting a frozen claim.
- `disproved finite claim`: an exhaustively refuted statement over its exact finite domain.
- `unknown due to resource limits`: no truth value inferred because the computation did not complete.

A mathematical proof is a deductive argument with explicit hypotheses and quantifiers. A certificate is a finite object checked by a verifier. Evidence supports but does not prove a larger claim. A timeout is only an incomplete computation and is always recorded as unknown.

## Baseline gate status

| Gate | Status | Reason |
|---|---|---|
| Definitions | `PASSED` for this track | frozen definitions and endpoint conventions are restated exactly |
| Divisor legality | `IN_PROGRESS` | trusted implementation created in the next checkpoint |
| Distinctness | `IN_PROGRESS` | trusted implementation created in the next checkpoint |
| Local coverage | `OPEN` asymptotically | finite exact domains can be audited only |
| Term count | `OPEN` asymptotically | finite exact optima can be certified only |
| Uniform asymptotics | `OPEN` | outside computational proof authority |
| Track B conversion | `NOT_STARTED` | archived source package unavailable in repository |
| Finite exceptions | `NOT_STARTED` | depends on a future effective threshold |
| Independent proof audit | `NOT_STARTED` | no frozen candidate theorem received |
| Computational audit | `IN_PROGRESS` | clean laboratory begins in this checkpoint |
