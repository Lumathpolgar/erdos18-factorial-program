# Streaming n=46 Handoff to Nova 4

Handoff ID: `N2-HO-N4-004`

Sending track: Nova 2, Additive Occupancy and Global Sumsets

Receiving track: Nova 4, Computational Verification

Date: 2026-07-15

Result status: **finite certificate plus proved algorithmic theorem**

Result IDs: `N2-ADD-121`, `N2-FIN-203`

## Frozen sources

Marker-three construction:

- repository: `Lumathpolgar/erdos18-factorial-program`
- branch: `nova/factorial-structure`
- commit: `ebb47ba436af554366d0f285119a769f31f9e561`
- construction: `N1-CON-003`

Final Nova 2 artifacts:

- streaming implementation commit: `e4539447d231acb87702179132d7c03e22c855e5`
- frozen certificate commit: `8fbc943f16e48bcd46198847237ad5dd1916408e`
- replay test commit: `7650330963f5c4dfbbbf46d51037562e65f50aab`
- corrected proof record commit: `89be707222c9989e743fa943466762799211a4ba`
- theorem registry commit: `fda6806cf509016fff337f48dc23dcab2913147f`

Files:

- `proofs/MARKER_THREE_STREAMING_N46_AUDIT.md`
- `verification/marker_three_streaming_audit.cpp`
- `verification/test_marker_three_streaming_audit.py`
- `verification/data/marker_three_streaming_n46.json`

## N2-ADD-121

Represent each odd divisor of `n!/3` after removing all powers of two by its bounded exponent vector. Every nonzero vector has a unique parent obtained by decrementing its largest nonzero coordinate.

Starting from zero, a state whose largest nonzero coordinate is `j` generates increments only in coordinates `k>=j`. This produces every bounded vector exactly once. A minimum priority queue therefore emits all odd cores in exact increasing numerical order.

The stream retains only:

1. the active priority frontier;
2. counts and final values at requested layer bounds;
3. consecutive gaps that set a new record.

The first gap exceeding any carrier threshold is necessarily a record gap. These data therefore replay every N2-ADD-120 connected component exactly without storing the completed divisor prefix.

## N2-FIN-203 exact result

At `n=46`:

\[
r_{46}=16,
\qquad
M_{46}=235,
\qquad
v_2(46!)=42,
\]

\[
Y_{46}
=
24{,}726{,}553{,}787{,}403{,}193{,}575{,}874{,}580{,}719,
\qquad
W_{46}=21{,}844.
\]

Exact stream data:

- complete odd-core family: `27,941,760`;
- cores at most `Y_46`: `24,567,748`;
- record gaps retained: `631`;
- maximum active frontier: `3,373,952`.

Six legal main layers give

\[
E_6
=
24{,}938{,}550{,}582{,}416{,}882{,}103{,}407{,}926{,}139,
\]

\[
E_6+W_{46}
=
24{,}938{,}550{,}582{,}416{,}882{,}103{,}407{,}947{,}983
>
Y_{46}.
\]

Thus

\[
H_{46!}(\lfloor\sqrt{46!}\rfloor+1)
\le22.
\]

This is an exact finite theorem only.

## Required Nova 4 reconstruction

Return separate verdicts for:

1. exact certification of `r_46=16` and `M_46=235`;
2. exact odd-core exponent bounds and total count `27,941,760`;
3. unique-parent generation with no duplicate or omitted exponent vector;
4. increasing numerical output through `Y_46`;
5. prefix counts at all six used layer bounds;
6. all five first blocking gaps and absence of a sixth-layer block;
7. final carrier endpoint and positive margin;
8. term bound `22`;
9. fail-closed frontier-cap behavior.

Return one of `ACCEPTED`, `ACCEPTED_WITH_RESTRICTIONS`, `NEEDS_REPAIR`, or `REJECTED`. A disagreement must identify the first exact mismatching field and include a replayable witness.

## Required next extension

The smallest unaudited parameter is

\[
n=47.
\]

The bounded execution did not complete at `n=47`; this is `unknown due to resource limits`, not failure.

Implement one or more of:

1. a lower-memory frontier encoding;
2. an external-memory priority frontier;
3. a segmented exact merge of prime-power divisor streams;
4. an independently replayable record-gap certificate;
5. a proved divisor-gap bound replacing enumeration.

For `n=47`, return endpoint success, the first exact carrier failure, a full-model counterexample, or a fail-closed resource-limit certificate. Failure of the sequential carrier criterion alone is not failure of the complete marker-three model.

## Reproduction commands

```text
g++ -O3 -std=c++20 \
  tracks/nova2-additive-occupancy/verification/marker_three_streaming_audit.cpp \
  -o marker_three_streaming_audit

./marker_three_streaming_audit --n 46 \
  > marker_three_streaming_n46.replayed.json

python3 tracks/nova2-additive-occupancy/verification/test_marker_three_streaming_audit.py
```

## Claim boundary

N2-FIN-203 does not prove uniform occupancy, establish `n=47`, or remove the Phase 12P audit for asymptotic use of N2-ADD-120.
