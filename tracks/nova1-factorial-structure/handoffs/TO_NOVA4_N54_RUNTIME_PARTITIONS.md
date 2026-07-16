# N1-HO-N4-008: n=54 Runtime-Aware Partition Replay

## Classification

Result label: **finite certificate** request.

## Exact source

- source branch: `nova/factorial-structure`;
- checkpoint source commit: `dac958b62ef069310901f5063dbf8bd6cbe3c0e3`;
- finite certificate: `N1-FIN-009`;
- finite computational diagnostic: `N1-CMP-007`;
- current finite requirement: `N1-REQ-N4-006`.

## Exact Nova 1 certificate

At `n=54`:

- `r_54=16`;
- `M_54=255`;
- `v_2(54!)=50`;
- quotient endpoint `Y_54=160153987475679647486755841698814824`;
- correction radius `W_54=21844`;
- odd-core divisor count: `350,438,400`;
- six layers;
- term bound: `22`;
- positive margin: `321802717811173461556306445531`.

Exact connected-prefix sizes:

\[
63{,}547,
1{,}308{,}259,
14{,}197{,}074,
71{,}967{,}365,
185{,}071{,}301,
287{,}853{,}491.
\]

Therefore

\[
H_{54!}(\lfloor\sqrt{54!}\rfloor+1)\le22.
\]

## Partition replays

Primary mask `255`:

- `128 x 2,737,800`;
- wall time `15.31` seconds;
- peak resident memory `49,032 KiB`.

Alternate mask `223`:

- `512 x 684,450`;
- wall time `18.57` seconds;
- peak resident memory `18,056 KiB`.

The two runs agree on every mathematical field after excluding partition and environment metadata.

The balanced `18,720 x 18,720` partition emitted `230,000,000` divisors before the six-minute execution boundary and did not complete. Classify this only as unknown due to resource limits for that partition.

## Required independent reconstruction

1. Recompute the prime exponents and odd-core divisor count independently.
2. Choose two explicit masks different from `255` and `223` when possible.
3. Verify unique half-list divisors and exact product count.
4. Verify strict global order, no duplicates, and no omitted rows.
5. Recompute every threshold, blocking gap, connected maximum, and `K_t`.
6. Recompute the endpoint, margin, entropy product, finite requirement, and normalized surplus.
7. Corrupt one partition mask, one half-list divisor, one row successor, one blocking gap, and one connected count. Each corruption must fail closed.
8. Verify the finite first-blocking-gap ratio diagnostic independently.
9. Extend exact certification beginning at `n=55` using the runtime-aware partition planner.

## Replay artifacts

- `verification/marker_three_mitm_prefix_u128.cpp`;
- `verification/plan_mitm_partition.py`;
- `verification/FULL_CORE_N54_REPORT.md`;
- `verification/full_core_n54_mitm_mask255.txt`;
- `verification/full_core_n54_mitm_mask223.txt`;
- `verification/test_mitm_n54_partition.py`.

## Receiver outcome

Return one of:

- `ACCEPTED`;
- `ACCEPTED_WITH_RESTRICTIONS`;
- `NEEDS_REPAIR`;
- `REJECTED`.

Include the exact imported commit, verifier paths, selected masks, resource envelope, and first unresolved finite target.

## Claim boundary

This request concerns exact finite certification only. It does not establish asymptotic occupancy or solve Erdős Problem 18.
