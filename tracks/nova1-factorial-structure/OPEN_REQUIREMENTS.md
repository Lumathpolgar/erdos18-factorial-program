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

## Connected-prefix count requirement

### N1-REQ-N2-003

Result label: **conditional theorem** request.

Imported engine:

- branch: `nova/additive-occupancy`;
- exact accepted head: `2ab09dd980f7116b82530368e3d98bb53240bf0c`;
- results: `N2-ADD-119`, `N2-ADD-120`, `N2-ADD-121`, `N2-ADD-122`.

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

This remains a necessary count gate. By `N1-STR-025`, it is not sufficient because packing utilization can consume nearly all count surplus.

Finite count-surplus values through `n=55` are non-monotone. They must not be extrapolated as an asymptotic trend.

## Effective carrier-utilization requirement

### N1-REQ-N2-006

Result label: **conditional theorem** request.

Imported and independently reconstructed theorem:

- source branch: `nova/additive-occupancy`;
- exact source commit: `2ab09dd980f7116b82530368e3d98bb53240bf0c`;
- source theorem: `N2-ADD-122`;
- Nova 1 reconstruction: `N1-STR-025`.

Let

\[
F_0=W_n+1,
\qquad
F_t=F_{t-1}+s_tU_t,
\qquad
s_t=2^{t-1},
\]

and define

\[
a_t=\frac{s_tU_t}{F_{t-1}},
\qquad
b_t=\frac{1+a_t}{1+K_t}.
\]

Then exactly

\[
\frac{F_L}{W_n+1}
=
P_n\prod_{t=1}^{L}b_t.
\]

Put

\[
R_n=\frac{Y_n+1}{W_n+1},
\]

\[
\widetilde\Gamma_n=(P_n/R_n)^{1/L},
\qquad
\mathcal B_n=\left(\prod_tb_t\right)^{1/L},
\qquad
\Delta_n=\left(\frac{F_L}{Y_n+1}\right)^{1/L}.
\]

Then

\[
\Delta_n=\widetilde\Gamma_n\mathcal B_n,
\]

and endpoint success is equivalent to

\[
\Delta_n\ge1.
\]

Accepted next outcomes are:

1. a **proved theorem** giving a uniform lower bound `widetilde Gamma_n * B_n >= 1` for enough exact layers;
2. a **proved theorem** giving `widetilde Gamma_n * B_n < 1` eventually or infinitely often, retiring the sequential engine;
3. a **conditional theorem** reducing the effective product to an explicit average-gap or record-gap theorem;
4. an exact counterexample with a replayable certificate.

Finite diagnostics for `51<=n<=55` show count surplus between approximately `92` and `125`, utilization root between approximately `0.0080` and `0.0109`, and endpoint root surplus only slightly above one. No asymptotic trend is inferred.

## Divisor record-gap requirement

### N1-REQ-N2-005

Result label: **conditional theorem** request.

Let `D_t` be the exact carrier threshold and let `g_t` be the first record-breaking consecutive divisor gap strictly larger than `D_t`, when such a gap occurs before the layer cutoff.

Prove one of:

1. a uniform upper bound on `g_t/D_t`, or a stronger average-gap theorem, sufficient to control the utilization factors in `N1-STR-025`;
2. a uniform lower obstruction showing utilization forces `Delta_n<1` eventually or infinitely often;
3. a conditional theorem reducing the carrier to an explicit divisor-gap theorem for
   \[
   D_n=\frac{n!}{3\cdot2^{v_2(n!)}}.
   \]

Finite diagnostic `N1-CMP-008` gives

\[
\max_{51\le n\le55,\ 1\le t\le5}\frac{g_t}{D_t}
=
\frac{20891689328819250}{18870510190034037}
<1.108.
\]

This is **computational evidence** only. The maximum occurs at `n=51`, layer `4`. A first-blocking-gap ratio alone does not yet control average packing utilization.

## Finite complete-core requirement

### N1-REQ-N4-007

Result label: **finite certificate** request.

Current exact coverage:

- Nova 2 `N2-FIN-202`: every `12<=n<=45`;
- Nova 1 `N1-FIN-005`: every `46<=n<=50`;
- Nova 1 `N1-FIN-006`: `n=51`;
- Nova 1 `N1-FIN-007`: `n=52`;
- Nova 1 `N1-FIN-008`: `n=53`;
- Nova 1 `N1-FIN-009`: `n=54`;
- Nova 1 `N1-FIN-010`: `n=55`.

Therefore

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)
\le22
\qquad(12\le n\le54),
\]

and

\[
H_{55!}(\lfloor\sqrt{55!}\rfloor+1)
\le23.
\]

Consequently,

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)
\le23
\qquad(12\le n\le55).
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
11. exact `N1-STR-025` effective-factor identities;
12. the term-bound transition caused by `r_55=17`;
13. runtime-aware partition planning with explicit column bounds;
14. fail-closed integer and resource boundaries.

Current artifacts:

- `proofs/MEET_IN_THE_MIDDLE_CONNECTED_PREFIX_STREAM.md`;
- `proofs/NORMALIZED_CONNECTED_PREFIX_SURPLUS.md`;
- `proofs/EFFECTIVE_CARRIER_FACTORIZATION_RECONSTRUCTION.md`;
- `verification/marker_three_mitm_prefix_u128.cpp`;
- `verification/plan_mitm_partition.py`;
- `verification/FULL_CORE_N55_REPORT.md`;
- `verification/full_core_n55_mitm_mask9.txt`;
- `verification/full_core_n55_mitm_mask808.txt`;
- `verification/test_mitm_n55_effective.py`.

The next finite target is `n=56`. Resource exhaustion must be reported as unknown due to resource limits, never as mathematical failure.

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
- layer-normalized count identity;
- exact effective carrier factorization;
- exact complete-core carrier coverage through `n=55`.

## Open structural requirements

- uniform effective count-utilization lower or upper bounds;
- uniform divisor record-gap or average-gap control;
- exact finite extension beginning at `n=56`;
- uniform quotient maximum downward gap at most `W_n`;
- downward endpoint-window occupancy;
- target-local collision control;
- compact numerical tilt or direct phase dispersion;
- strict weighted bounded-torus Fourier inequality;
- Track B reconstruction;
- finite exceptions after an effective asymptotic threshold.

## Rule

No requirement may be weakened, strengthened, or reinterpreted silently. Any changed hypothesis, constant, endpoint, layer definition, or conclusion receives a new versioned requirement.
