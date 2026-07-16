# Full-Core n=54 Checkpoint

## State

Result label: **finite certificate**.

Checkpoint ID: `N1-FIN-009`.

The exact marker-three connected-core carrier now reaches the quotient endpoint for every

\[
12\le n\le54.
\]

The factorial half-range theorem remains open.

## Exact result

At `n=54`:

- `r_54=16`;
- `M_54=255`;
- `v_2(54!)=50`;
- total odd-core divisors: `350,438,400`;
- primary partition: mask `255`, `128 x 2,737,800`;
- alternate partition: mask `223`, `512 x 684,450`;
- divisors emitted through certificate completion: `287,853,491`;
- layers used: `6`;
- term bound: `22`.

The exact connected-prefix sizes are

\[
63{,}547,
1{,}308{,}259,
14{,}197{,}074,
71{,}967{,}365,
185{,}071{,}301,
287{,}853{,}491.
\]

The final positive margin is

\[
321802717811173461556306445531.
\]

Therefore

\[
H_{54!}(\lfloor\sqrt{54!}\rfloor+1)\le22.
\]

## Partition replay

The primary and alternate partitions agree on every exact mathematical field. They differ only in partition identity, row and column dimensions, heap size, runtime, and memory.

The balanced partition was not used as the final certificate because its row-heavy heap exceeded the six-minute execution boundary. That outcome is classified as unknown due to resource limits for that partition, not as mathematical failure.

## Normalized evidence

Result label: **computational evidence**.

The exact normalized surplus is approximately

\[
\Gamma_{54}=92.27326436677728.
\]

The values for `n=51,52,53,54` are

\[
120.322026489,
97.645052132,
124.609364763,
92.273264367.
\]

They are non-monotone.

Across the twenty blocked layers in this finite range, the first blocking-gap ratio remains below `1.108`. This is a candidate finite pattern only.

## Artifacts

- `verification/FULL_CORE_N54_REPORT.md`;
- `verification/full_core_n54_mitm_mask255.txt`;
- `verification/full_core_n54_mitm_mask223.txt`;
- `verification/plan_mitm_partition.py`;
- `verification/test_mitm_n54_partition.py`.

## Open boundary

The smallest unaudited finite parameter is `n=55`.

The first asymptotic requirement remains a uniform lower bound proving `Gamma_n>=1`, or a uniform upper bound that retires the sequential connected-core engine.
