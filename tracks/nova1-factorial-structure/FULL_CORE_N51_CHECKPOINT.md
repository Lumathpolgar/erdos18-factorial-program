# Full-Core n=51 Checkpoint

## Checkpoint classification

This checkpoint contains:

- `N1-STR-022`: **proved theorem**;
- `N1-FIN-006`: **finite certificate**.

The factorial half-range theorem remains open.

## Imported response

Nova 2 accepted `N1-OBS-003` and `N1-FIN-005` with the exact boundaries recorded at:

- branch: `nova/additive-occupancy`;
- exact commit: `e443674f86b2ee3c7037ac94ee47f6b8a4b3b29f`;
- response: `tracks/nova2-additive-occupancy/handoffs/RESPONSE_TO_NOVA1_CONNECTED_PREFIX.md`;
- outcome: `ACCEPTED_WITH_RESTRICTIONS`.

Nova 2 also supplied `N2-ADD-121`, the unique-parent increasing divisor stream.

## New theorem

`N1-STR-022` independently reconstructs the unique-parent theorem and adds exact record-gap left counts.

The stored data recover both:

\[
u_t^*,
\]

the complete zero-connected maximum core, and

\[
K_t,
\]

the number of positive cores in that connected prefix.

Proof:

`proofs/STREAMING_CONNECTED_PREFIX_CERTIFIER.md`.

## New finite certificate

At `n=51`, the exact stream certifies:

- `r_51=16`;
- `M_51=248`;
- `v_2(51!)=47`;
- total odd-core divisors: `124,001,280`;
- emitted cores through `Y_51`: `108,924,509`;
- record gaps: `874`;
- maximum frontier: `13,602,843`.

The exact connected-prefix sizes are

\[
46{,}990,
824{,}638,
6{,}936{,}398,
30{,}013{,}231,
70{,}529{,}067,
101{,}350{,}643.
\]

Six layers reach the complete quotient endpoint with margin

\[
10{,}322{,}820{,}258{,}187{,}136{,}041{,}755{,}833{,}363.
\]

Therefore

\[
H_{51!}(\lfloor\sqrt{51!}\rfloor+1)
\le22.
\]

Combined with the prior exact finite range,

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)
\le22
\qquad(12\le n\le51).
\]

## Entropy measurement

The exact finite connected-prefix product is

\[
57{,}666{,}029{,}159{,}716{,}720{,}889{,}778{,}527{,}039{,}222{,}918{,}886{,}144.
\]

It exceeds the exact finite requirement from `N1-OBS-003` by a factor greater than

\[
3{,}034{,}386{,}005{,}338.
\]

This does not prove an asymptotic prefix lower bound.

## Artifacts

- `proofs/STREAMING_CONNECTED_PREFIX_CERTIFIER.md`;
- `verification/marker_three_streaming_prefix_u128.cpp`;
- `verification/FULL_CORE_N51_REPORT.md`;
- `verification/full_core_n51.txt`.

## Exact open boundary

1. The smallest unaudited finite parameter is `n=52`.
2. Uniform connected-prefix entropy remains open.
3. Global quotient downward-window occupancy remains open.
4. The final endpoint window remains open asymptotically.
5. Target-local collision upper bounds remain open.
6. The collision-aware weighted Fourier theorem remains open.

## Next exact step

Extend the streaming certificate to `n=52` while seeking a uniform theorem for the connected-prefix cardinalities `K_t` strong enough to meet `N1-OBS-003`.