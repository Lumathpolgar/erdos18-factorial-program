# Full-Core n=53 Checkpoint

## Status

The factorial formulation of Erdős Problem 18 remains open.

This checkpoint contains:

- `N1-STR-024`, proved theorem;
- `N1-FIN-008`, finite certificate;
- `N1-CMP-006`, computational evidence.

## Exact finite result

The meet-in-the-middle carrier certifier proves

\[
H_{53!}(\lfloor\sqrt{53!}\rfloor+1)\le22.
\]

Together with the previously frozen certificates,

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le22
\qquad(12\le n\le53).
\]

This is finite only.

## Exact n=53 data

- `r_53=16`;
- `M_53=253`;
- `v_2(53!)=49`;
- total odd-core divisors: `310,003,200`;
- balanced split: `17,550 x 17,664`;
- emitted through the certificate: `255,794,579`;
- layers used: `6`;
- term bound: `22`;
- occupied margin: `257,219,713,671,656,581,137,253,687,630`.

Connected-prefix cardinalities:

\[
63{,}547,
1{,}308{,}251,
14{,}186{,}800,
70{,}586{,}242,
175{,}389{,}561,
255{,}794{,}579.
\]

## Partition replay

Primary partition mask `350` and alternate mask `414` produce identical exact carrier outputs after removing the mask and environment-dependent resource fields.

## Normalized entropy

`N1-STR-024` defines

\[
\Gamma_n=
\left(
\frac{\prod_t(1+K_t)}{
\left\lceil(Y_n+1)/(W_n+1)\right\rceil}
\right)^{1/L}.
\]

Finite values:

| `n` | `Gamma_n` |
|---:|---:|
| 51 | 120.322026489 |
| 52 | 97.645052132 |
| 53 | 124.609364763 |

The finite sequence is non-monotone. No asymptotic trend is claimed.

## Artifacts

- `proofs/NORMALIZED_CONNECTED_PREFIX_SURPLUS.md`;
- `verification/marker_three_mitm_prefix_u128.cpp`;
- `verification/FULL_CORE_N53_REPORT.md`;
- `verification/full_core_n53_mitm.txt`;
- `verification/full_core_n53_mitm_mask414.txt`;
- `verification/connected_prefix_normalized_n51_n53.csv`;
- `verification/test_mitm_n53_normalized.py`.

## Next exact boundary

The smallest unaudited finite parameter is `n=54`.

The asymptotic connected-prefix requirement remains open.
