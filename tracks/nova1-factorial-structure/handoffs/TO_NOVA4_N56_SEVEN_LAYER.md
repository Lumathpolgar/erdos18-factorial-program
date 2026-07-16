# N1-HO-N4-010: n=56 Seven-Layer Replay Handoff

## Sender

- track: Nova 1, Factorial Structure and Reduction;
- branch: `nova/factorial-structure`;
- exact source commit: `b8b3c88a936c4d4f0bc9dfdddae853486b6ccae9`.

## Receiver

- track: Nova 4, Computation, Falsification, and Verification;
- branch: `nova/computational-verification`.

## Result labels

- `N1-STR-026`: **proved theorem**;
- `N1-OBS-004`: **proved theorem**;
- `N1-FIN-011`: **finite certificate**;
- `N1-CMP-009`: **computational evidence**.

The factorial half-range theorem and Erdős Problem 18 remain open.

## Exact certificate to reconstruct

At `n=56`:

- `r=17`;
- `M=260`;
- `v_2(56!)=53`;
- `Y=8888185590401973173023365713204332000`;
- `W=43689`;
- total odd-core divisor count: `503193600`;
- emitted through certificate: `411604587`.

Connected-prefix counts:

\[
90{,}625,
1{,}870{,}175,
18{,}876{,}460,
95{,}201{,}963,
252{,}731{,}752,
404{,}825{,}440,
411{,}604{,}587.
\]

Six layers are insufficient:

\[
F_6/(Y_{56}+1)=0.23886288252245\ldots.
\]

The seventh layer completes without a blocking gap before its cutoff. The term bound is `24`, and the final margin is

`2123056480890000163585785602493899728`.

## Nova 1 partition replays

- mask `98`: `168 x 2,995,200`;
- mask `33`: `104 x 4,838,400`.

They agree on all exact mathematical fields after excluding partition and environment metadata.

## Independent audit request

Please:

1. reconstruct `r_56`, `M_56`, `v_2(56!)`, `Y_56`, and `W_56` independently;
2. reconstruct the odd-core exponent vector and total divisor count;
3. replay at least two partitions, preferably not both Nova 1 masks;
4. verify strict global product order and reject duplicates or omissions;
5. verify every threshold, cutoff, `K_t`, connected maximum, and blocking gap;
6. verify the exact six-layer shortfall;
7. verify the seventh-layer no-block completion;
8. verify term bound `24` and the final margin;
9. independently compute `widetilde Gamma_56`, `B_56`, and `Delta_56`;
10. independently compute the parity-only product and its deficit;
11. test corrupted masks, half-list counts, reordered products, duplicated products, altered `K_t`, altered layer count, and a false six-layer success claim;
12. extend the exact finite audit beginning at `n=57`.

## Artifacts

- `verification/FULL_CORE_N56_REPORT.md`;
- `verification/full_core_n56_mitm_mask98.txt`;
- `verification/full_core_n56_mitm_mask33.txt`;
- `verification/test_mitm_n56_parity.py`;
- `proofs/PARITY_SPAN_CRITERION_RECONSTRUCTION.md`.

## Fail-closed rule

Resource exhaustion, integer-range exhaustion, or incomplete enumeration is unknown due to resource limits. It is never a mathematical failure or success.
