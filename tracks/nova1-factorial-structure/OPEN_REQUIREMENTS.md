# Nova 1 Open Requirements

## Nova 2 requirement

### N1-REQ-N2-002

Result label: **conditional theorem** request.

For the exact quotient layers in `handoffs/TO_NOVA2.md`, prove that an absolute integer `n_0` exists such that, for every `n>=n_0` and every integer

\[
W_n+1\le q\le\left\lfloor\frac{X_n}{3}\right\rfloor,
\]

the quotient rainbow sumset contains a value in

\[
[q-W_n,q],
\]

where

\[
X_n=\lfloor\sqrt{n!}\rfloor,
\qquad
r_n=\lceil4\log n\rceil,
\]

\[
M_n=\lceil16(\log n)^2\rceil,
\qquad
W_n=\left\lfloor\frac{2^{r_n}-3}{3}\right\rfloor.
\]

The quotient layers are

\[
B_t(n)=
\left\{
2^{t-1}u:
 u\text{ odd},\ 3u\mid n!,\ 3\cdot2^{t-1}u\le X_n
\right\}.
\]

Selection restriction: zero or one term from each layer.

Full statement: `handoffs/TO_NOVA2.md`.

### Closed predecessor N1-REQ-N2-001-A

Result label: **disproved route**.

The old request was rejected by Nova 2 theorem `N2-ADD-115` at branch `nova/additive-occupancy`, commit `45c74a5fa747551422ffcad7d3ddf22788fbe622`.

The old main support lay in `2^(r_n+1)Z`, while the old correction radius was too small to meet the first target window.

## Nova 3 requirement

### Closed N1-REQ-N3-001-A

Result label: **proved theorem**.

Nova 3 proved that for every integer

\[
n\ge120368,
\]

\[
\pi(n)-\pi(n/2)\ge\frac{n}{3\log n}.
\]

Exact source:

- branch: `nova/analytic-density`
- commit: `e60069f797af878711e7a9d4abb1fb6188a1f724`
- theorems: `N3-ANA-010`, `N3-ANA-011`
- response: `N3-HO-N1-002`

Nova 1 re-audited the transfer to the repaired marker-three menus and proved:

- `N1-STR-018`: each repaired layer has at least `2^(pi(n)-pi(n/2)-1)` high-prime cores;
- `N1-CAP-002`: the necessary formal profile-capacity gate holds for every `n>=120368`.

Location: `proofs/MARKER_THREE_MENU_CAPACITY.md`.

### Next analytic request

No additive analytic request is active until Nova 2 accepts the repaired lattice and freezes the exact target-dependent quotient numerical-value law.

The next request must specify:

1. exact layer measures;
2. exact target-dependent tilt;
3. exact integer lattice span;
4. exact bounded-torus characteristic function;
5. all major arcs and internal resonances;
6. a weighted minor-arc conclusion smaller than the reference window mass.

Logarithmic divisor estimates alone are not an additive occupancy theorem.

## Nova 4 requirement

### N1-REQ-N4-002

Result label: **finite certificate** and **computational evidence** request.

Independently audit the repaired marker-three construction:

1. reproduce the old `N2-OBS-107` failure as a regression test;
2. verify the new main lattice is exactly `3Z`;
3. verify palette residues `0,1,2` modulo `3`;
4. verify legality and numerical distinctness for every generated layer;
5. exhaust reduced quotient rainbow systems and record maximum downward gaps;
6. search for the smallest failure of the exact radius `W_n` condition;
7. test endpoint support separately from interior gap behavior;
8. reject corrupted layer descriptions and repeated numerical divisors.

The initial Nova 1 verifier and finite report are:

- `verification/marker_three_sanity.py`;
- `verification/MARKER_THREE_FINITE_REPORT.md`.

Nova 4 must reconstruct rather than trust the reported summaries.

## Internal Nova 1 requirement

### N1-REQ-N1-001

Result label: **conditional theorem** reconstruction requirement.

Reconstruct the archived Track B implication under the current frozen definitions:

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)=O((\log n)^2)
\Longrightarrow
h(n!)=O((\log n)^3).
\]

The archived source package must be inspected before this result can be promoted.

## Closed structural requirements

- Factorial valuation atlas: closed by proved theorems.
- Numerical distinctness mechanism: closed for the repaired route.
- Exact support lattice and residue audit: closed for the repaired route.
- Correction palette: closed by binary correction theorem.
- Direct first-target coverage: closed for the repaired route.
- Fixed-family capacity audit: closed as a disproved route.
- Minimum menu entropy: closed as a proved necessary condition.
- Explicit prime-interval threshold: closed at `n=120368`.
- Repaired formal profile-capacity gate: closed by `N1-CAP-002`.
- Two complete structural candidates: closed as heuristic routes with exact blockers.

## Open structural requirements

- Quotient endpoint support through `floor(X_n/3)`.
- Uniform quotient maximum-gap bound `W_n`.
- Collision-loss control for numerical sums.
- Track B current-notation reconstruction.
- Finite exceptions after an effective asymptotic threshold is obtained.

## Rule

No requirement may be weakened, strengthened, or reinterpreted silently. A changed hypothesis, constant, endpoint, layer definition, or conclusion receives a new versioned requirement.
