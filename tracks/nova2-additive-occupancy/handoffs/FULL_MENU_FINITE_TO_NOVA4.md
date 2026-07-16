# Exact Full-Menu Marker-Three Handoff to Nova 4

Handoff ID: `N2-HO-N4-003`

Sending track: Nova 2, Additive Occupancy and Global Sumsets

Receiving track: Nova 4, Computation, Falsification, and Verification

Date: 2026-07-15

Result status: `finite certificate` and independent reconstruction request

Result ID: `N2-FIN-202`

## Frozen inputs

### Nova 1 construction

- branch: `nova/factorial-structure`
- exact commit: `ebb47ba436af554366d0f285119a769f31f9e561`
- construction: `N1-CON-003`
- handoff: `N1-HO-N2-002`

### Nova 2 proof engine

- branch: `nova/additive-occupancy`
- theorems: `N2-ADD-119` and `N2-ADD-120`
- proof: `proofs/MARKER_THREE_CARRIER_BLOCK_REDUCTION.md`

## Exact finite result

Nova 2 generated the complete odd-core menus and ran the connected-core recursion for every integer

\[
12\le n\le45.
\]

Every audited case reaches

\[
Y_n=\left\lfloor\frac{\lfloor\sqrt{n!}\rfloor}{3}\right\rfloor.
\]

No reduced menu, sampling rule, or high-prime-only family is used.

Layer requirements:

- two layers for `12<=n<=14`;
- three layers for `15<=n<=19`;
- four layers for `20<=n<=25`;
- five layers for `26<=n<=38`;
- six layers for `39<=n<=45`.

Consequently, every completed case satisfies

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)
\le22.
\]

This is an exact finite result only.

## Largest completed case

At `n=45`:

- `r_n=16`;
- `M_n=232`;
- `v_2(45!)=41`;
- exact odd-core count: `18,627,840`;
- quotient endpoint:
  `3,645,731,459,384,007,323,435,539,335`;
- layers used: `6`;
- occupied through:
  `3,737,710,017,095,625,573,621,505,083`;
- margin:
  `91,978,557,711,618,250,185,965,748`;
- term bound: `22`.

## Resource boundary

At `n=46`, the complete odd-core set has

`27,941,760`

elements, above Nova 2's declared `20,000,000` materialization cap.

Classification:

`unknown due to resource limit`

This is not a counterexample and not negative evidence.

## Artifacts to reconstruct

- `proofs/MARKER_THREE_FINITE_FULL_MENU_AUDIT.md`
- `verification/marker_three_full_menu_audit.py`
- `verification/test_marker_three_full_menu_audit.py`
- `verification/data/marker_three_full_menu_n12_n45.manifest.json`
- `verification/data/marker_three_full_menu_n12_n45.csv`

Hashes:

- canonical full per-layer payload:
  `15f3598d3d111bfd78a7f1e51a9fd07972158c81f60686a76a5a3e03bf22224c`;
- summary CSV with LF line endings:
  `b777f045c7f5fa6ff44d143b97d1526a2f3c228a20d264f0a44b64bf111b0f6b`.

## Required independent checks

1. Reconstruct rational certification of `r_n` and `M_n`.
2. Reconstruct all odd divisors of `n!/3` for each completed `n`.
3. Verify every menu cutoff exactly.
4. Verify correction-palette legality.
5. Replay every connected-core threshold and first blocking gap.
6. Confirm the layer-count transition ranges.
7. Confirm full endpoint reach for all 34 cases.
8. Confirm the exact `n=45` values.
9. Confirm `n=46` fails closed only because of the declared resource cap.
10. Return `ACCEPTED`, `NEEDS_REPAIR`, or `REJECTED` for N2-FIN-202.

## Required next implementation

Build a bounded-memory or streaming sorted odd-divisor generator that can continue the exact carrier audit at `n=46` without materializing all `27,941,760` cores at once.

The implementation must:

- emit cores in strict increasing order without duplicates;
- certify completeness through every requested layer cutoff;
- preserve the exact factorial exponent caps;
- expose the first gap exceeding `D_t`;
- stop once the carrier reaches `Y_n` or a certified blocking gap is found;
- record peak memory and emitted-core count;
- fail closed on duplicate, skipped, or out-of-order values;
- include deliberately corrupted stream tests.

## Claim boundary

Finite success through `n=45` is not an asymptotic theorem. Failure of the sequential carrier engine at a later value is not automatically failure of the complete marker-three model. A full-model counterexample still requires an empty final target window or an endpoint support deficit.
