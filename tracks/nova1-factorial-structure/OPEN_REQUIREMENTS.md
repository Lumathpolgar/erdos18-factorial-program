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

and quotient layers

\[
B_t(n)=
\{2^{t-1}u:u\text{ odd},\ 3u\mid n!,\ 2^{t-1}u\le Y_n\},
\]

prove that an absolute `n_0` exists such that every integer

\[
W_n+1\le q\le Y_n
\]

has a legal rainbow sum in

\[
[q-W_n,q].
\]

At most one nonzero term may be selected from each layer.

The structural model is accepted with restrictions by Nova 2. The global occupancy theorem remains open.

## Connected-prefix entropy requirement

### N1-REQ-N2-003

Result label: **conditional theorem** request.

Imported engine:

- branch: `nova/additive-occupancy`;
- exact accepted head: `e443674f86b2ee3c7037ac94ee47f6b8a4b3b29f`;
- results: `N2-ADD-119`, `N2-ADD-120`, `N2-ADD-121`.

For executed layers define

\[
P_n=\prod_{t=1}^{L}(1+K_t),
\qquad
Q_n=\left\lceil\frac{Y_n+1}{W_n+1}\right\rceil.
\]

`N1-OBS-003` proves that sequential success requires

\[
P_n\ge Q_n.
\]

`N1-STR-024` defines

\[
\Gamma_n=(P_n/Q_n)^{1/L}
\]

and proves

\[
P_n\ge Q_n\iff\Gamma_n\ge1.
\]

For every `n>=120368`, success within the frozen layer budget also requires geometric-mean connected-prefix size at least

\[
\exp\left(\frac{n}{85\log n}\right).
\]

Accepted next outcomes are:

1. a **proved theorem** giving a uniform lower bound `Gamma_n>=1` for enough exact layers;
2. a **proved theorem** giving `Gamma_n<1` eventually or infinitely often, retiring the sequential engine;
3. a **conditional theorem** reducing `Gamma_n>=1` to an explicit divisor-gap statement;
4. an exact counterexample with a replayable certificate.

Finite values `Gamma_51` through `Gamma_54` are non-monotone. They must not be extrapolated as an asymptotic trend.

## Divisor record-gap requirement

### N1-REQ-N2-005

Result label: **conditional theorem** request.

Let `D_t` be the exact carrier threshold and let `g_t` be the first record-breaking consecutive divisor gap strictly larger than `D_t`, when such a gap occurs before the layer cutoff.

Prove one of:

1. a uniform upper bound on `g_t/D_t` strong enough to force connected-prefix growth meeting `N1-OBS-003`;
2. a uniform lower obstruction showing record gaps force `Gamma_n<1` eventually or infinitely often;
3. a conditional theorem reducing the carrier to an explicit theorem about divisor record gaps of
   \[
   D_n=\frac{n!}{3\cdot2^{v_2(n!)}}.
   \]

Finite diagnostic `N1-CMP-007` gives

\[
\max_{51\le n\le54,\ 1\le t\le5}\frac{g_t}{D_t}<1.108.
\]

This is **computational evidence** only. The maximum occurs at `n=51`, layer `4`.

## Finite complete-core requirement

### N1-REQ-N4-006

Result label: **finite certificate** request.

Current exact coverage:

- Nova 2 `N2-FIN-202`: every `12<=n<=45`;
- Nova 1 `N1-FIN-005`: every `46<=n<=50`;
- Nova 1 `N1-FIN-006`: `n=51`;
- Nova 1 `N1-FIN-007`: `n=52`;
- Nova 1 `N1-FIN-008`: `n=53`;
- Nova 1 `N1-FIN-009`: `n=54`.

Therefore

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)
\le22
\qquad(12\le n\le54).
\]

Nova 4 must independently reconstruct:

1. exact rational certification of `r_n` and `M_n`;
2. factorial valuations and `Y_n`;
3. both half-divisor lists;
4. unique product representation;
5. exact sorted row merge;
6. duplicate and omission rejection;
7. every layer threshold and cutoff;
8. connected maxima and exact `K_t` values;
9. blocking gaps, endpoints, margins, and term bounds;
10. two distinct explicit partition replays;
11. exact normalized surplus identities;
12. runtime-aware partition planning with explicit column bounds;
13. fail-closed integer and resource boundaries.

Current artifacts:

- `proofs/MEET_IN_THE_MIDDLE_CONNECTED_PREFIX_STREAM.md`;
- `proofs/NORMALIZED_CONNECTED_PREFIX_SURPLUS.md`;
- `verification/marker_three_mitm_prefix_u128.cpp`;
- `verification/plan_mitm_partition.py`;
- `verification/FULL_CORE_N54_REPORT.md`;
- `verification/full_core_n54_mitm_mask255.txt`;
- `verification/full_core_n54_mitm_mask223.txt`;
- `verification/test_mitm_n54_partition.py`.

The next finite target is `n=55`. Resource exhaustion must be reported as unknown due to resource limits, never as mathematical failure.

## Collision requirement

### N1-REQ-N2-004

Result label: **conditional theorem** request.

`N1-COL-001` proves profile injectivity is false and supplies a fiber of size at least

\[
2^{\lfloor M_n/2\rfloor}.
\]

The next required result is a target-local upper bound on one of:

- maximum fiber size;
- additive energy;
- second moment of target representation counts;
- weighted collision contribution under the exact tilted numerical-value law.

Raw global profile counts are not occupancy evidence.

## Nova 3 numerical-law requirement

### N1-REQ-N3-003

Result label: **conditional theorem** request.

Current imported foundation:

- exact head inspected: `003b9c0e1179314d6c119c8a356e0f41231e3ad6`;
- results: `N3-ANA-017`, `N3-ANA-018`, `N3-ANA-019`;
- outcome: `ACCEPTED_WITH_RESTRICTIONS`.

Closed clauses:

- unique finite exponential tilt for every required target;
- exact additive span one;
- exact torus resonance set `{0}`;
- explicit first-layer characteristic-function bound.

Disproved shortcut:

- no fixed target-independent minor-arc modulus gap can hold uniformly over every real tilt.

Open clauses:

1. freeze the exact target range after deterministic coverage;
2. prove compact tilt or quantitative phase dispersion there;
3. prove variance, third-moment, and maximal-step bounds;
4. construct a positive reference lattice law;
5. prove a strict weighted Fourier inequality whose error is smaller than the reference window mass.

## Internal Track B requirement

### N1-REQ-N1-001

Result label: **conditional theorem** reconstruction request.

Reconstruct

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)=O((\log n)^2)
\Longrightarrow
h(n!)=O((\log n)^3)
\]

under the current frozen endpoint convention.

## Closed structural requirements

- factorial valuation atlas;
- numerical distinctness;
- exact support lattice and residues;
- correction palette;
- direct first-target coverage;
- formal profile capacity;
- explicit prime-interval threshold;
- total quotient endpoint reach;
- one-factorial-block ceiling;
- profile noninjectivity;
- connected-prefix entropy necessity;
- unique-parent exact stream;
- meet-in-the-middle exact stream;
- layer-normalized entropy identity;
- exact complete-core carrier coverage through `n=54`.

## Open structural requirements

- uniform normalized connected-prefix lower or upper bounds;
- uniform divisor record-gap control;
- exact finite extension beginning at `n=55`;
- uniform quotient maximum downward gap at most `W_n`;
- downward endpoint-window occupancy;
- target-local collision control;
- compact numerical tilt or direct phase dispersion;
- strict weighted bounded-torus Fourier inequality;
- Track B reconstruction;
- finite exceptions after an effective asymptotic threshold.

## Rule

No requirement may be weakened, strengthened, or reinterpreted silently. Any changed hypothesis, constant, endpoint, layer definition, or conclusion receives a new versioned requirement.
