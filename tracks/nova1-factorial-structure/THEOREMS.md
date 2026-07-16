# Nova 1 Theorem Registry

## Status rule

Every item is labeled exactly as one of:

- **proved theorem**;
- **conditional theorem**;
- **finite certificate**;
- **computational evidence**;
- **disproved route**.

No finite result is promoted to an asymptotic theorem. No formal profile count is treated as numerical additive occupancy.

## Structural and reduction theorems

| ID | Result label | Conclusion | Proof or source |
|---|---|---|---|
| N1-STR-003 | proved theorem | Exact Legendre budgets, quotient bands, dyadic bands, and factorial 2-adic multiplicity | `proofs/VALUATION_BUDGET_LEMMAS.md` |
| N1-STR-004 | proved theorem | Exponent boxes produce unique legal divisors | `FACTORIAL_DIVISOR_ATLAS.md` |
| N1-STR-005 | proved theorem | Allocated valuation budgets preserve divisor legality | `FACTORIAL_DIVISOR_ATLAS.md` |
| N1-STR-006 | proved theorem | Distinct marker signatures force numerical distinctness | `proofs/DISTINCTNESS_AND_CORRECTION.md` |
| N1-STR-007 | proved theorem | Square-center complement pairing gives legal bounded distinct reciprocal pairs | `proofs/COMPLEMENT_PAIRING_LEMMA.md` |
| N1-COR-001 | proved theorem | Binary powers represent every residual in `[0,2^r-1]` | `proofs/DISTINCTNESS_AND_CORRECTION.md` |
| N1-RED-002 | proved theorem | Downward main occupancy plus binary correction gives exact local coverage | `proofs/DISTINCTNESS_AND_CORRECTION.md` |
| N1-OBS-002 | proved theorem | Downward `R`-density on `[0,X]` requires `|S|(R+1)>=X+1` | `proofs/COUNTING_CAPACITY_OBSTRUCTION.md` |
| N1-STR-008 | proved theorem | `O((log n)^2)` layers with polynomial correction require geometric-mean menu size `exp(Omega(n/log n))` | `proofs/MENU_ENTROPY_REQUIREMENT.md` |
| N1-STR-009 | proved theorem | High-prime subset products supply exponentially many legal cores | `proofs/HIGH_PRIME_MENU_CAPACITY.md` |

## Marker-three route

| ID | Result label | Conclusion | Proof or source |
|---|---|---|---|
| N1-STR-014 | proved theorem | Marker-three divisors are legal, have exact layer valuations, and are disjoint from the palette | `proofs/MARKER_THREE_LATTICE_REPAIR.md` |
| N1-STR-015 | proved theorem | Main support generates exactly `3Z`; the palette attains every residue modulo `3` | `proofs/MARKER_THREE_LATTICE_REPAIR.md` |
| N1-RED-004 | proved theorem | Quotient occupancy in every `[q-W_n,q]` implies `H_{n!}(X_n+1)<=M_n+r_n` | `proofs/MARKER_THREE_LATTICE_REPAIR.md` |
| N1-STR-016 | proved theorem | Odd positional digits have maximum downward gap one | `proofs/MARKER_THREE_LATTICE_REPAIR.md` |
| N1-STR-017 | proved theorem | Unconditional coverage through `3m_n(2^{M_n}-1)+2` | `proofs/MARKER_THREE_LATTICE_REPAIR.md` |
| N1-STR-018 | proved theorem | For `n>=120368`, every repaired layer has at least `2^{n/(3 log n)-1}` legal high-prime cores | `proofs/MARKER_THREE_MENU_CAPACITY.md` |
| N1-CAP-002 | proved theorem | Formal profile-capacity gate holds for `n>=120368` | `proofs/MARKER_THREE_MENU_CAPACITY.md` |
| N1-STR-019 | proved theorem | `D_n=n!/(3*2^{v_2(n!)})` is multiplicatively 3-dense for `n>=6` | `proofs/QUOTIENT_ENDPOINT_SUPPORT.md` |
| N1-STR-020 | proved theorem | Three quotient-layer terms push maximum support past `floor(X_n/3)` for `n>=12` | `proofs/QUOTIENT_ENDPOINT_SUPPORT.md` |
| N1-RED-006 | proved theorem | After `L` increasing layers, a deterministic selection leaves residual below `max((2/3)^Lq,2^L)` | `proofs/QUOTIENT_ENDPOINT_SUPPORT.md` |
| N1-STR-021 | proved theorem | Explicit factorial arithmetic blocks are legal connected submenus under the exact carrier threshold | `proofs/FACTORIAL_BLOCK_CARRIER_OBSTRUCTION.md` |
| N1-COL-001 | proved theorem | At least `2^{floor(M_n/2)}` legal profiles collide at one quotient sum for `n>=120368` | `proofs/RAINBOW_CARRY_COLLISIONS.md` |
| N1-OBS-003 | proved theorem | Sequential carrier success requires geometric-mean connected-prefix size at least `exp(n/(85 log n))` for `n>=120368` | `proofs/CONNECTED_PREFIX_ENTROPY_REQUIREMENT.md` |
| N1-STR-022 | proved theorem | Unique-parent streaming plus record-gap left counts exactly recovers `u_t^*` and `K_t` without storing the complete divisor prefix | `proofs/STREAMING_CONNECTED_PREFIX_CERTIFIER.md` |
| N1-STR-023 | proved theorem | A balanced meet-in-the-middle product stream emits every odd core exactly once and recovers exact carrier prefixes with heap size `O(sqrt(tau(D_n)))` | `proofs/MEET_IN_THE_MIDDLE_CONNECTED_PREFIX_STREAM.md` |

## Detail for N1-OBS-003

Let `K_t` be the number of positive cores in the complete zero-connected prefix at layer `t`, and put

\[
F_t=E_t+W_n+1.
\]

Then

\[
F_t\le F_{t-1}(1+K_t).
\]

Success after `L` layers therefore requires

\[
\prod_{t=1}^{L}(1+K_t)
\ge
\frac{Y_n+1}{W_n+1}.
\]

For every `n>=120368`, success within the frozen layer budget requires

\[
\left(
\prod_{t=1}^{L}(1+K_t)
\right)^{1/L}
\ge
\exp\left(\frac{n}{85\log n}\right).
\]

This applies only to the sequential connected-core engine.

## Detail for N1-STR-022

For a bounded exponent vector, decrement the largest nonzero coordinate to define its unique parent. Generate children only by incrementing coordinates at least as large as the parent’s largest nonzero coordinate.

A minimum priority queue then emits every divisor exactly once in increasing order. Store only record-breaking consecutive gaps, their endpoints, and the number of divisors at the left endpoint. For any layer cutoff and threshold, the first record gap above the threshold recovers the exact connected maximum and exact connected-prefix cardinality.

Imported precursor:

- Nova 2 result: `N2-ADD-121`;
- branch: `nova/additive-occupancy`;
- exact commit: `e443674f86b2ee3c7037ac94ee47f6b8a4b3b29f`.

## Detail for N1-STR-023

Partition the odd prime-power coordinates of

\[
D_n=\frac{n!}{3\cdot2^{v_2(n!)}}
\]

into disjoint sets `I` and `J`. Their sorted half-divisor lists are `A` and `B`. Every divisor of `D_n` has a unique representation `ab` with `a in A` and `b in B`.

For each fixed `a`, the row `aB` is strictly increasing. A minimum-heap merge of the rows emits the complete divisor order exactly once. Scanning consecutive gaps resolves the first gap above each carrier threshold, re-evaluating the same right endpoint after every blocked-layer transition.

A balanced coordinate partition gives heap size

\[
O(\sqrt{\tau(D_n)}),
\]

rather than a frontier proportional to millions of exponent vectors.

## Conditional results

### N1-RED-005: Marker-three half-range reduction

- Result label: **conditional theorem**
- Hypothesis: every required quotient window `[q-W_n,q]` contains a legal rainbow sum
- Conclusion:
  \[
  H_{n!}(\lfloor\sqrt{n!}\rfloor+1)
  \le
  \lceil16(\log n)^2\rceil+\lceil4\log n\rceil
  \]
- Location: `PREFERRED_ROUTE.md`

### N1-RED-001: Track B reconstruction

- Result label: **conditional theorem** under reconstruction
- Goal:
  \[
  H_{n!}(\lfloor\sqrt{n!}\rfloor+1)=O((\log n)^2)
  \Longrightarrow
  h(n!)=O((\log n)^3)
  \]
- Dependency: archived Track B source and current endpoint convention

## Finite certificates and computational evidence

### N1-CMP-003: Reduced quotient audit

- Result label: **computational evidence**
- Domain: every `7<=n<=14` under reduced legal parameters
- Conclusion: maximum downward quotient distance at most one
- Verifier: `verification/marker_three_sanity.py`

### N1-CMP-004: Endpoint-support audit

- Result label: **finite certificate**
- Checks: 3-density for `6<=n<=20`, endpoint crossing for `12<=n<=20`, and exhaustive coarse contraction for `12<=n<=14`
- Verifier: `verification/endpoint_support_sanity.py`

### N1-CMP-005: Block and collision audit

- Result label: **finite certificate**
- Checks: factorial block legality, exact one-block carrier ceiling, carry collisions, and scale separation
- Verifier: `verification/block_collision_sanity.py`

### N2-FIN-202: Imported complete-menu carrier audit

- Result label: **finite certificate**
- Exact source: branch `nova/additive-occupancy`, commit `82603c631a106c3bff4676bdeeb9cc791fc98f3c`
- Domain: every `12<=n<=45`
- Conclusion: complete odd-core carrier reaches `Y_n` using two through six layers

### N1-FIN-005: Complete-core extension through n=50

- Result label: **finite certificate**
- Domain: every `46<=n<=50`
- Conclusion: complete truncated odd-core menus reach `Y_n` in six layers
- Largest case: `n=50`, `78,715,976` generated cores, exact term bound `22`
- Verifier: `verification/marker_three_full_core_u128.cpp`
- Report: `verification/FULL_CORE_N46_N50_REPORT.md`

### N1-FIN-006: Exact streaming certificate at n=51

- Result label: **finite certificate**
- Total odd-core divisors: `124,001,280`
- Emitted cores through `Y_51`: `108,924,509`
- Record gaps: `874`
- Maximum frontier: `13,602,843`
- Connected-prefix sizes:
  \[
  46{,}990,
  824{,}638,
  6{,}936{,}398,
  30{,}013{,}231,
  70{,}529{,}067,
  101{,}350{,}643
  \]
- Six layers reach `Y_51`
- Exact conclusion:
  \[
  H_{51!}(\lfloor\sqrt{51!}\rfloor+1)\le22
  \]
- Verifier: `verification/marker_three_streaming_prefix_u128.cpp`
- Report: `verification/FULL_CORE_N51_REPORT.md`
- Raw certificate: `verification/full_core_n51.txt`

### N1-FIN-007: Exact meet-in-the-middle certificate at n=52

- Result label: **finite certificate**
- Total odd-core divisors: `155,001,600`
- Balanced split: `12,420 x 12,480`
- Divisors emitted before certificate completion: `128,277,372`
- Maximum merge heap: `12,420`
- Connected-prefix sizes:
  \[
  47{,}281,
  847{,}667,
  7{,}770{,}345,
  34{,}911{,}862,
  85{,}166{,}200,
  128{,}277{,}372
  \]
- Six layers reach `Y_52`
- Exact conclusion:
  \[
  H_{52!}(\lfloor\sqrt{52!}\rfloor+1)\le22
  \]
- Entropy product floor ratio: `866,765,166,748`
- Verifier: `verification/marker_three_mitm_prefix_u128.cpp`
- Report: `verification/FULL_CORE_N52_REPORT.md`
- Raw certificate: `verification/full_core_n52_mitm.txt`

Combined exact finite range:

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)
\le22
\qquad(12\le n\le52).
\]

No conclusion is asserted for `n>=53`.

## Disproved routes

| ID | Result label | Claim rejected | Proof or source |
|---|---|---|---|
| N1-DIS-001 | disproved route | Prime powers of one prime behave as independent coordinates | `FACTORIAL_DIVISOR_ATLAS.md` |
| N1-DIS-002 | disproved route | A fixed pool of `O((log n)^2)` binary or ternary choices covers the half-range | `proofs/COUNTING_CAPACITY_OBSTRUCTION.md` |
| N1-DIS-003 | disproved route | Polynomial-size menus in `O((log n)^2)` layers cover the half-range with polynomial correction | `proofs/MENU_ENTROPY_REQUIREMENT.md` |
| N1-DIS-004 | disproved route | Complement pairing alone implies additive density | `proofs/COMPLEMENT_PAIRING_LEMMA.md` |
| N1-DIS-005 | disproved route | Original addresses `e_t=r_n+t` satisfy the old radius request | Nova 2 `N2-ADD-115` at `45c74a5fa747551422ffcad7d3ddf22788fbe622` |
| N1-DIS-006 | disproved route | One factorial arithmetic block per layer reaches `Y_n` within `M_n` layers | `proofs/FACTORIAL_BLOCK_CARRIER_OBSTRUCTION.md` |

## Historical conditional artifact

### N1-RED-003

- Result label: **conditional theorem**
- Status: retired because its exact occupancy hypothesis was disproved
- Replacement: `N1-RED-005`

## Promotion rule

No conditional theorem becomes a **proved theorem** until every named dependency is proved and independently reconstructed. No **finite certificate** or **computational evidence** is promoted to an asymptotic theorem.
