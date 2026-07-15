# Nova 1 Open Requirements

## Global quotient requirement

### N1-REQ-N2-002

Result label: **conditional theorem** request.

For

\[
X_n=\lfloor\sqrt{n!}\rfloor,
\qquad
Y_n=\left\lfloor\frac{X_n}{3}\right\rfloor,
\]

\[
r_n=\lceil4\log n\rceil,
\qquad
M_n=\lceil16(\log n)^2\rceil,
\qquad
W_n=\left\lfloor\frac{2^{r_n}-3}{3}\right\rfloor,
\]

and

\[
B_t(n)=
\left\{
2^{t-1}u:
 u\text{ odd},
 3u\mid n!,
 2^{t-1}u\le Y_n
\right\},
\]

prove that an absolute `n_0` exists such that every integer

\[
W_n+1\le q\le Y_n
\]

has a final rainbow sum in

\[
[q-W_n,q].
\]

At most one nonzero term may be selected from each layer.

Full statement: `handoffs/TO_NOVA2.md`.

Nova 2 accepted the structural model with restrictions at exact commit

`b15278e21f91e0e188b1c7c3e9a10e58a1db20fe`.

The global occupancy theorem remains open.

## Connected-core carrier requirement

### N1-REQ-N2-003

Result label: **conditional theorem** request.

Imported engine:

- Nova 2 branch: `nova/additive-occupancy`;
- exact commit: `82603c631a106c3bff4676bdeeb9cc791fc98f3c`;
- results: `N2-ADD-119`, `N2-ADD-120`, `N2-FIN-202`.

Let `K_t` be the number of positive cores in the complete zero-connected prefix under the exact layer threshold

\[
D_t=\left\lfloor
\frac{E_{t-1}+W_n+1}{2^{t-1}}
\right\rfloor.
\]

Nova 1 theorem `N1-OBS-003` proves that complete carrier success requires

\[
\prod_{t=1}^{L}(1+K_t)
\ge
\frac{Y_n+1}{W_n+1}.
\]

For every `n>=120368`, success within `M_n` layers requires geometric-mean connected-prefix size at least

\[
\exp\left(\frac{n}{85\log n}\right).
\]

The next accepted outcome must be one of:

1. a **proved theorem** giving a uniform connected-prefix lower bound that meets this requirement;
2. a **proved theorem** upper-bounding complete connected prefixes below the requirement, thereby retiring the sequential engine;
3. a narrower **conditional theorem** that isolates an explicit divisor-gap statement strong enough to imply success;
4. an exact counterexample with a replayable certificate.

A one-factorial-block argument is insufficient by `N1-DIS-006`.

## Finite complete-core requirement

### N1-REQ-N4-003

Result label: **finite certificate** request.

Current exact coverage:

- Nova 2 `N2-FIN-202`: every `12<=n<=45`, exact commit `82603c631a106c3bff4676bdeeb9cc791fc98f3c`;
- Nova 1 `N1-FIN-005`: every `46<=n<=50`.

Nova 4 must independently reconstruct:

1. exact rational certification of `r_n` and `M_n`;
2. complete odd-core valuation vectors;
3. truncated core generation through `Y_n`;
4. duplicate rejection;
5. exact per-layer thresholds;
6. connected-prefix cardinalities;
7. first blocking gaps;
8. carrier endpoints and margins;
9. fail-closed resource limits;
10. the distinction between a finite carrier certificate and an asymptotic theorem.

Nova 1 artifacts:

- `verification/marker_three_full_core_u128.cpp`;
- `verification/FULL_CORE_N46_N50_REPORT.md`;
- `verification/full_core_n46_n50_summary.csv`;
- `verification/full_core_n46_n50_layers.csv`.

The next finite target is `n>=51` using a lower-memory sorted divisor generator. Resource exhaustion must be reported as `unknown due to resource limits`, not as failure.

## Collision requirement

### N1-REQ-N2-004

Result label: **conditional theorem** request.

`N1-COL-001` proves that profile injectivity is false and that one quotient sum has at least

\[
2^{\lfloor M_n/2\rfloor}
\]

legal preimages.

The next required result is a target-local upper bound on one of:

- maximum fiber size;
- additive energy;
- second moment of target representation counts;
- weighted collision contribution under the exact tilted numerical-value law.

A global profile count without collision control is not accepted as occupancy evidence.

## Nova 3 numerical-law requirement

### N1-REQ-N3-003

Result label: **conditional theorem** request.

Current imported numerical foundation:

- branch: `nova/analytic-density`;
- exact head inspected: `003b9c0e1179314d6c119c8a356e0f41231e3ad6`;
- results: `N3-ANA-017`, `N3-ANA-018`, `N3-ANA-019`;
- outcome: `ACCEPTED_WITH_RESTRICTIONS`.

Closed clauses:

- unique finite exponential tilt for every required target;
- exact additive span one;
- exact torus resonance set `{0}`;
- an explicit first-layer characteristic-function bound.

Disproved analytic shortcut:

- no fixed target-independent minor-arc modulus gap can hold uniformly over every real tilt.

Open clauses:

1. freeze the exact target range left after deterministic coverage;
2. prove compact tilt or quantitative phase dispersion there;
3. prove variance, third-moment, and maximal-step bounds;
4. construct a positive reference lattice law;
5. prove a strict weighted Fourier inequality whose error is smaller than the reference window mass.

Bounds for logarithmic divisor values are not substitutes for numerical additive bounds.

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
- numerical distinctness;
- exact support lattice and residues;
- correction palette;
- direct first-target coverage;
- formal profile capacity;
- explicit prime-interval threshold;
- total quotient endpoint reach;
- one-factorial-block carrier ceiling;
- profile noninjectivity;
- connected-prefix entropy necessity;
- exact complete-core carrier coverage through `n=50`.

## Open structural requirements

- uniform connected-prefix lower or upper bounds meeting `N1-OBS-003`;
- uniform quotient maximum downward gap at most `W_n`;
- downward endpoint-window occupancy;
- target-local collision control;
- compact numerical tilt or direct phase dispersion;
- strict weighted bounded-torus Fourier inequality;
- Track B reconstruction;
- finite exceptions after an effective asymptotic threshold.

## Rule

No requirement may be weakened, strengthened, or reinterpreted silently. A changed hypothesis, constant, endpoint, layer definition, or conclusion receives a new versioned requirement.