# Nova 1 to Nova 4: n=51 Streaming Reconstruction

Handoff ID: `N1-HO-N4-005`

Sending track: Nova 1, Factorial Structure and Reduction

Receiving track: Nova 4, Computational Verification

## Exact source

- branch: `nova/factorial-structure`
- checkpoint commit: `748a69d831dbe8f099dddcbb2dac1d9fa82a227f`
- theorem: `N1-STR-022`
- finite certificate: `N1-FIN-006`
- verifier: `tracks/nova1-factorial-structure/verification/marker_three_streaming_prefix_u128.cpp`
- report: `tracks/nova1-factorial-structure/verification/FULL_CORE_N51_REPORT.md`
- raw certificate: `tracks/nova1-factorial-structure/verification/full_core_n51.txt`

## Required independent reconstruction

1. Reconstruct the unique-parent exponent-vector theorem.
2. Verify duplicate-free increasing divisor emission.
3. Verify exact rational certification of `r_51=16` and `M_51=248`.
4. Verify `v_2(51!)=47`.
5. Verify the total odd-core divisor count `124,001,280`.
6. Verify `108,924,509` emitted cores through `Y_51`.
7. Verify all `874` record-gap updates and maximum frontier `13,602,843`.
8. Verify every layer cutoff, threshold, connected maximum, connected count, blocking gap, and carrier endpoint.
9. Verify the six connected-prefix sizes:
   `46,990`, `824,638`, `6,936,398`, `30,013,231`, `70,529,067`, `101,350,643`.
10. Verify the exact endpoint margin and term bound `22`.
11. Corrupt one parent rule, one record left count, and one blocking gap and require fail-closed rejection.
12. Extend the exact streaming audit beginning at `n=52`.

## Required classification

Return separately:

- `ACCEPTED`, `NEEDS_REPAIR`, or `REJECTED` for `N1-STR-022`;
- `ACCEPTED`, `NEEDS_REPAIR`, or `REJECTED` for `N1-FIN-006`;
- `finite certificate`, `resource-limited unknown`, or exact failure for `n=52` and every later attempted parameter.

Resource exhaustion is not a mathematical counterexample.

## Claim boundary

Finite success does not prove a uniform connected-prefix theorem or solve Erdős Problem 18.