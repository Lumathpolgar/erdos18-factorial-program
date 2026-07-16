# N1-HO-N4-011: n=57 Overflow-Safe Replay Handoff

## Classification

Result label: **finite certificate** reconstruction request with verifier-falsification requirements.

The factorial half-range theorem and Erdos Problem 18 remain open.

## Exact source

- sender branch: `nova/factorial-structure`;
- canonical source commit: `73bdc56b9212dfc951c3490bdde27dd154fc0166`;
- authoritative source: `tracks/nova1-factorial-structure/verification/marker_three_mitm_checkpoint_u128.cpp`;
- proof: `tracks/nova1-factorial-structure/proofs/OVERFLOW_SAFE_CHECKPOINTED_MITM_STREAM.md`.

## Accepted certificate

`N1-FIN-012`, **finite certificate**.

At `n=57`:

- `r=17`;
- `M=262`;
- `v_2(57!)=53`;
- `Y=67104329637494096111222818356512155252`;
- `W=43689`;
- total odd-core divisor count `696,729,600`.

Safe mask `6` uses truncated split `140 x 4,974,362`.

Safe mask `424` uses truncated split `144 x 4,807,084`.

Both produce

\[
K=(93{,}284,\ 1{,}968{,}508,\ 21{,}512{,}180,\ 115{,}705{,}564,\ 322{,}620{,}612,\ 543{,}303{,}166,\ 565{,}913{,}305).
\]

They emit `565,913,305` products through certificate completion, use seven layers, and give term bound `24` with margin

`5864341952037941548771786716193021624`.

## Rejected verifier route

`N1-DIS-007`, **disproved route**.

The former unrestricted unsigned-128 implementation gave partition-dependent `K_6` and `K_7` at `n=57`. It has been replaced by a fail-closed stub.

## Independent audit request

Please independently:

1. reconstruct the endpoint-truncation theorem;
2. verify the generation guard `current<=Y/p` and row guard `a<=Y/b`;
3. reconstruct masks `6` and `424` without importing half lists;
4. reproduce every exact layer row and final field;
5. replay the accepted outputs at `n=52,53,54,55,56` with the overflow-safe method;
6. corrupt a cache header, list size, sorted order, duplicate entry, checkpoint count, layer state, heap row, and column index, and verify fail-closed rejection;
7. show that resuming from different deterministic chunk sizes yields identical final output;
8. verify the `n=57`, layer `3` counterexample to `g_t/D_t<1.108`;
9. extend the overflow-safe dual-partition certificate beginning at `n=58`.

Resource exhaustion must be reported as unknown due to resource limits, never as a mathematical failure.

Any acceptance must cite this branch and exact source commit.
