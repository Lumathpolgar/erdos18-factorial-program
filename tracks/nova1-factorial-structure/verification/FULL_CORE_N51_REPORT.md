# Exact Full-Core Carrier Audit at n=51

## Result ID

- `N1-FIN-006`: finite certificate

The factorial half-range theorem remains open. This file records one exact finite case.

## Frozen inputs

Marker-three construction:

- branch: `nova/factorial-structure`
- construction: `N1-CON-003`
- structural handoff commit: `ebb47ba436af554366d0f285119a769f31f9e561`

Imported carrier package:

- branch: `nova/additive-occupancy`
- exact commit: `e443674f86b2ee3c7037ac94ee47f6b8a4b3b29f`
- results: `N2-ADD-119`, `N2-ADD-120`, `N2-ADD-121`

Nova 1 certifier:

- theorem: `N1-STR-022`
- proof commit: `d59ffc52b71602dc3fecd86413ab042db1b4c3c6`
- verifier commit: `61e23f26e2a609845011140b8e313683d6d47576`
- raw certificate commit: `63be6c61b2aff887577aac901147f77185adc566`

## Exact parameters

For `n=51`:

\[
r_{51}=16,
\qquad
M_{51}=248,
\qquad
v_2(51!)=47.
\]

The quotient endpoint and correction width are

\[
Y_{51}
=
415{,}146{,}393{,}628{,}852{,}899{,}831{,}187{,}352{,}563{,}934,
\]

\[
W_{51}=21{,}844.
\]

The reserved odd core

\[
D_{51}=\frac{51!}{3\cdot2^{v_2(51!)}}
\]

has exactly

\[
124{,}001{,}280
\]

positive divisors.

The exact increasing stream emitted

\[
108{,}924{,}509
\]

odd cores not exceeding `Y_51`.

The final emitted value was

\[
415{,}145{,}946{,}312{,}611{,}547{,}831{,}839{,}056{,}640{,}625.
\]

The stream retained `874` record gaps. Its maximum active priority-queue frontier was `13,602,843` nodes.

## Exact connected-core recursion

| layer | threshold | connected maximum core | connected-prefix size `K_t` | carrier endpoint |
|---:|---:|---:|---:|---:|
| 1 | 21,845 | 63,955,203 | 46,990 | 63,955,203 |
| 2 | 31,988,524 | 857,162,109,375 | 824,638 | 1,714,388,173,953 |
| 3 | 428,597,048,949 | 37,740,591,783,019,125 | 6,936,398 | 150,964,081,520,250,453 |
| 4 | 18,870,510,190,034,037 | 4,453,237,235,977,294,921,875 | 30,013,231 | 35,626,048,851,899,879,625,453 |
| 5 | 2,226,628,053,243,742,477,956 | 646,823,503,142,488,464,143,203,125 | 70,529,067 | 10,349,211,676,328,667,326,170,875,453 |
| 6 | 323,412,864,885,270,853,942,840,540 | 12,973,323,976,169,836,196,871,966,796,875 | 101,350,643 | 415,156,716,449,111,086,967,229,108,375,453 |

The sixth layer has no blocking gap before its exact core cutoff.

Adding the correction width gives

\[
E_6+W_{51}
=
415{,}156{,}716{,}449{,}111{,}086{,}967{,}229{,}108{,}397{,}297.
\]

This exceeds `Y_51` by

\[
10{,}322{,}820{,}258{,}187{,}136{,}041{,}755{,}833{,}363.
\]

Therefore the exact connected-core carrier and the marker-three correction theorem give

\[
H_{51!}(\lfloor\sqrt{51!}\rfloor+1)
\le
6+r_{51}
=
22.
\]

## Finite connected-prefix entropy

The exact connected-prefix product is

\[
\prod_{t=1}^{6}(1+K_t)
=
57{,}666{,}029{,}159{,}716{,}720{,}889{,}778{,}527{,}039{,}222{,}918{,}886{,}144.
\]

The exact necessary product threshold from `N1-OBS-003` is

\[
\left\lceil
\frac{Y_{51}+1}{W_{51}+1}
\right\rceil
=
19{,}004{,}183{,}732{,}151{,}654{,}833{,}196{,}949{,}076.
\]

Thus the finite prefix product exceeds the exact finite requirement by a factor greater than

\[
3{,}034{,}386{,}005{,}338.
\]

Its geometric mean is approximately

\[
6{,}215{,}651.76.
\]

This large finite margin is computationally informative, but it does not prove the asymptotic connected-prefix lower bound.

## Combined finite range

Nova 2 certificate `N2-FIN-202` and accepted Nova 1 certificate `N1-FIN-005` already establish the bound `22` for every `12<=n<=50`.

Adding `N1-FIN-006` gives the exact finite theorem

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)
\le22
\qquad
(12\le n\le51).
\]

This statement is finite only.

## Reproducibility

Compile:

```text
g++ -O3 -std=c++20 \
  tracks/nova1-factorial-structure/verification/marker_three_streaming_prefix_u128.cpp \
  -o marker_three_streaming_prefix_u128
```

Run:

```text
./marker_three_streaming_prefix_u128 51 30000000
```

Recorded resource envelope:

- wall time: `100.01` seconds;
- maximum resident set: `532,932` KiB;
- frontier cap: `30,000,000` nodes;
- observed maximum frontier: `13,602,843` nodes;
- exit status: success.

## Claim boundary

This finite certificate does not prove success at `n=52`, does not prove connected-prefix entropy uniformly, does not remove the Phase 12P audit, and does not solve Erdős Problem 18.