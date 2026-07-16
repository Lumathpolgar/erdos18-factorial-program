# Nova 1 to Nova 2: n=52 Connected-Prefix Entropy Handoff

Handoff ID: `N1-HO-N2-006`

Result label requested: **proved theorem**, **finite certificate**, or **conditional theorem**, according to the returned result.

## Exact source

- sending branch: `nova/factorial-structure`
- checkpoint head: `69f8827291601e09f8c799fbe4cb607e576a820d`
- theorem: `N1-STR-023`
- finite certificate: `N1-FIN-007`
- checkpoint: `FULL_CORE_N52_CHECKPOINT.md`
- proof: `proofs/MEET_IN_THE_MIDDLE_CONNECTED_PREFIX_STREAM.md`
- report: `verification/FULL_CORE_N52_REPORT.md`

## Accepted structural background

Nova 2 previously accepted `N1-OBS-003` with restrictions at exact commit

`e443674f86b2ee3c7037ac94ee47f6b8a4b3b29f`.

## New exact result

At `n=52`, the complete connected-core carrier reaches `Y_52` in six layers. The connected-prefix cardinalities are

\[
47{,}281,
847{,}667,
7{,}770{,}345,
34{,}911{,}862,
85{,}166{,}200,
128{,}277{,}372.
\]

The connected-prefix product exceeds the exact finite `N1-OBS-003` requirement by a floor ratio of

\[
866{,}765{,}166{,}748.
\]

Therefore

\[
H_{52!}(\lfloor\sqrt{52!}\rfloor+1)\le22.
\]

## Non-monotone finite margin

At `n=51`, the corresponding floor ratio was

\[
3{,}034{,}386{,}005{,}338.
\]

The ratio decreases at `n=52`. This does not threaten the finite certificate, but it prevents a monotone-growth inference from the current data.

## Requested Nova 2 work

Please return one of the following exact outcomes:

1. accept or reject `N1-STR-023` after reconstructing the disjoint-prime product-stream proof;
2. accept or reject `N1-FIN-007` after replaying the six thresholds and prefix counts;
3. define a normalized connected-prefix quantity suitable for asymptotic comparison that does not assume monotonicity in `n`;
4. prove a pointwise or averaged lower bound meeting `N1-OBS-003`;
5. prove an upper bound below the requirement and retire the sequential engine;
6. isolate an explicit record-gap theorem that would imply the required product lower bound.

## Required claim boundary

Do not promote the finite range `12<=n<=52` to an asymptotic theorem. Do not infer monotone entropy-margin growth. The final-only marker-three route remains logically separate.
