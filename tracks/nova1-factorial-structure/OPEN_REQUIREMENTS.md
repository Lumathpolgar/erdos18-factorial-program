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
 u\text{ odd},
 3u\mid n!,
 3\cdot2^{t-1}u\le X_n
\right\}.
\]

Selection restriction: zero or one term from each layer.

Full statement: `handoffs/TO_NOVA2.md`.

### Closed predecessor N1-REQ-N2-001-A

Result label: **disproved route**.

The old request was rejected by Nova 2 theorem `N2-ADD-115` at branch `nova/additive-occupancy`, commit `45c74a5fa747551422ffcad7d3ddf22788fbe622`.

## Nova 3 requirement

### Closed N1-REQ-N3-001-A

Result label: **proved theorem**.

Nova 3 proved that for every integer `n>=120368`,

\[
\pi(n)-\pi(n/2)\ge\frac{n}{3\log n}.
\]

Exact source:

- branch: `nova/analytic-density`
- commit: `e60069f797af878711e7a9d4abb1fb6188a1f724`
- theorems: `N3-ANA-010`, `N3-ANA-011`
- response: `N3-HO-N1-002`

Nova 1 re-audited the repaired transfer and proved `N1-STR-018` and `N1-CAP-002`.

### Next analytic request

No additive analytic request is active until Nova 2 accepts the repaired structure and freezes the exact target-dependent quotient numerical-value law.

The next request must specify:

1. exact layer measures;
2. exact target-dependent tilt;
3. exact integer lattice span;
4. exact bounded-torus characteristic function;
5. all major arcs and internal resonances;
6. a weighted minor-arc conclusion smaller than the reference window mass.

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
7. independently verify `N1-STR-019` multiplicative 3-density;
8. verify the first three quotient layers contain terms in `(X_n/9,X_n/3]` and cross the endpoint;
9. distinguish total endpoint reach from downward endpoint-window occupancy;
10. reject corrupted layer descriptions and repeated numerical divisors.

Nova 1 finite artifacts:

- `verification/marker_three_sanity.py`;
- `verification/MARKER_THREE_FINITE_REPORT.md`;
- `verification/endpoint_support_sanity.py`;
- `verification/ENDPOINT_SUPPORT_FINITE_REPORT.md`.

Nova 4 must reconstruct rather than trust the summaries.

## Internal Nova 1 requirement

### N1-REQ-N1-001

Result label: **conditional theorem** reconstruction requirement.

Reconstruct the archived Track B implication under the current frozen definitions:

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)=O((\log n)^2)
\Longrightarrow
h(n!)=O((\log n)^3).
\]

The archived source package must be inspected before promotion.

## Closed structural requirements

- factorial valuation atlas;
- numerical distinctness mechanism;
- exact support lattice and residue audit;
- correction palette;
- direct first-target coverage;
- fixed-family capacity audit;
- minimum menu entropy;
- explicit prime-interval threshold at `n=120368`;
- repaired formal profile-capacity gate;
- total quotient endpoint reach through `floor(X_n/3)`;
- two complete structural candidates.

## Open structural requirements

- uniform quotient maximum downward gap at most `W_n`;
- downward endpoint-window occupancy in `[floor(X_n/3)-W_n,floor(X_n/3)]`;
- collision-loss control for numerical sums;
- exact target-dependent numerical-value law;
- Track B current-notation reconstruction;
- finite exceptions after an effective asymptotic threshold.

## Rule

No requirement may be weakened, strengthened, or reinterpreted silently. A changed hypothesis, constant, endpoint, layer definition, or conclusion receives a new versioned requirement.