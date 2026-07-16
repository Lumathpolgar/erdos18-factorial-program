# Nova 1 to Nova 4: n=53 Partition Replay Handoff

Handoff ID: `N1-HO-N4-007`

Sending track: Nova 1, Factorial Structure and Reduction.

Receiving track: Nova 4, Computation, Falsification, and Verification.

Result label: **finite certificate** request.

## Frozen source

- branch: `nova/factorial-structure`;
- construction: `N1-CON-003`;
- theorem: `N1-STR-023`;
- normalized theorem: `N1-STR-024`;
- finite certificate: `N1-FIN-008`.

## Exact claim to reconstruct

Nova 1 certifies

\[
H_{53!}(\lfloor\sqrt{53!}\rfloor+1)\le22.
\]

Exact data:

- total odd-core divisors: `310,003,200`;
- primary partition mask: `350`;
- alternate partition mask: `414`;
- split dimensions: `17,550 x 17,664`;
- emitted count: `255,794,579`;
- maximum heap: `17,550`;
- six layers;
- final margin: `257,219,713,671,656,581,137,253,687,630`.

The two partition masks produce identical carrier outputs after excluding partition metadata and resource measurements.

## Required Nova 4 audit

1. Independently reconstruct factorial valuations and `Y_53`.
2. Independently generate both half-divisor lists.
3. Verify unique product representation and exact sorted merge order.
4. Replay masks `350` and `414`.
5. Reject duplicate products, missing rows, changed masks, changed thresholds, corrupted counts, and altered margins.
6. Verify `N1-STR-024` integer identities for `n=51,52,53`.
7. Extend the exact finite boundary beginning at `n=54`.
8. Report resource exhaustion as unknown due to resource limits, never as mathematical failure.

## Reproduction

```text
g++ -O3 -std=c++20 \
  tracks/nova1-factorial-structure/verification/marker_three_mitm_prefix_u128.cpp \
  -o marker_three_mitm_prefix_u128

./marker_three_mitm_prefix_u128 53
./marker_three_mitm_prefix_u128 53 414
python tracks/nova1-factorial-structure/verification/test_mitm_n53_normalized.py
```

## Claim boundary

This is a finite audit request. It does not ask Nova 4 to infer an asymptotic theorem or claim that Erdős Problem 18 is solved.
