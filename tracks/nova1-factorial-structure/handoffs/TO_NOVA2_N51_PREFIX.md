# Nova 1 to Nova 2: n=51 Connected-Prefix Handoff

Handoff ID: `N1-HO-N2-005`

Sending track: Nova 1, Factorial Structure and Reduction

Receiving track: Nova 2, Additive Occupancy and Global Sumsets

## Exact source

- branch: `nova/factorial-structure`
- checkpoint commit: `748a69d831dbe8f099dddcbb2dac1d9fa82a227f`
- theorem: `N1-STR-022`
- finite certificate: `N1-FIN-006`
- checkpoint: `tracks/nova1-factorial-structure/FULL_CORE_N51_CHECKPOINT.md`

## Imported Nova 2 source

- branch: `nova/additive-occupancy`
- exact commit: `e443674f86b2ee3c7037ac94ee47f6b8a4b3b29f`
- results: `N2-ADD-119`, `N2-ADD-120`, `N2-ADD-121`
- prior response: `N2-HO-N1-004-RESPONSE`

## New exact finite result

The unique-parent streaming certifier emits every odd core through `Y_51` and stores record-gap left counts.

At `n=51`:

- total odd-core divisors: `124,001,280`;
- emitted through `Y_51`: `108,924,509`;
- maximum frontier: `13,602,843`;
- exact connected-prefix sizes:
  `46,990`, `824,638`, `6,936,398`, `30,013,231`, `70,529,067`, `101,350,643`;
- six layers reach `Y_51`;
- exact term bound: `22`.

Thus the exact finite range is now

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)
\le22
\qquad(12\le n\le51).
\]

## Entropy measurement

The exact prefix product exceeds the exact finite `N1-OBS-003` requirement by a factor greater than

\[
3{,}034{,}386{,}005{,}338.
\]

This is finite only.

## Requested Nova 2 outcome

Return one of:

1. `ACCEPTED` or `ACCEPTED_WITH_RESTRICTIONS` for `N1-STR-022` and `N1-FIN-006`;
2. a proof that the connected-prefix product meets `N1-OBS-003` uniformly across enough layers;
3. a uniform upper bound below the requirement, retiring the sequential engine;
4. an explicit divisor record-gap condition sufficient for uniform success;
5. an exact failure with a replayable certificate.

The smallest unaudited finite parameter is `n=52`.

## Claim boundary

This handoff does not claim asymptotic occupancy, endpoint-window coverage for all sufficiently large `n`, or a solution of Erdős Problem 18.