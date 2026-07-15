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

Nova 2 artifacts:

- streaming implementation commit: `e4539447d231acb87702179132d7c03e22c855e5`
- frozen certificate commit: `8fbc943f16e48bcd46198847237ad5dd1916408e`
- replay test commit: `7650330963f5c4dfbbbf46d51037562e65f50aab`
- proof record commit: `5f51579397b3d1745a07d6b8d7cd5741adfcd090`

Files:

- `proofs/MARKER_THREE_STREAMING_N46_AUDIT.md`
- `verification/marker_three_streaming_audit.cpp`
- `verification/test_marker_three_streaming_audit.py`
- `verification/data/marker_three_streaming_n46.json`

## N2-ADD-121

The odd divisors of `n!/3` after removing all powers of two are represented by bounded exponent vectors. Every nonzero exponent vector has a unique parent obtained by decrementing its largest nonzero coordinate.

The streaming generator starts from the zero vector and, from a state whose largest nonzero index is `j`, increments only coordinates `k>=j`. This generates every bounded exponent vector exactly once. A minimum priority queue therefore emits all odd cores in exact increasing numerical order.

The stream stores only:

1. the active priority frontier;
2. counts and last values at requested layer bounds;
3. consecutive gaps that set a new record.

The first gap exceeding a carrier threshold is necessarily a record gap, so this compressed data replays every N2-ADD-120 connected component exactly.

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
\]

\[
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
6. all five first blocking gaps and the absence of a sixth-layer block;
7. final carrier endpoint and margin;
8. term bound `22`;
9. fail-closed frontier-cap behavior.

Use one of:

- `ACCEPTED`;
- `ACCEPTED_WITH_RESTRICTIONS`;
- `NEEDS_REPAIR`;
- `REJECTED`.

A disagreement must include the first exact mismatching field and an independently replayable witness.

## Required next extension

The smallest unaudited parameter is now

\[
n=47.
\]

The current bounded execution did not complete at `n=47`. This is `unknown due to resource limits`, not failure.

Implement one or more of:

1. a lower-memory frontier encoding;
2. an external-memory priority frontier;
3. a segmented exact merge of prime-power divisor streams;
4. an exact record-gap certificate that can be independently replayed without retaining the full frontier;
5. a proved divisor-gap bound replacing enumeration.

For `n=47`, return either:

- complete endpoint success;
- the first exact carrier-block failure;
- a full-model quotient counterexample;
- or a fail-closed resource-limit certificate.

Failure of the sequential carrier criterion alone is not failure of the full marker-three model.

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

N2-FIN-203 does not prove uniform occupancy, does not establish `n=47`, and does not remove the Phase 12P audit for asymptotic use of N2-ADD-120.
