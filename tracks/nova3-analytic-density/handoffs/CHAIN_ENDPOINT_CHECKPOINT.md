# Dyadic Chain-Endpoint Checkpoint

Checkpoint ID: `N3-CHK-010`

Date: 2026-07-16

Branch: `nova/analytic-density`

## Imported heads

- Nova 1: `nova/factorial-structure@8c7ee8f64af56a8d082f1fa3adabb0b0309f6e27`
- Nova 2: `nova/additive-occupancy@591e4e51a00627ac48c0aa05fae4a955dccb9d14`
- Nova 4 inspected head: `nova/computational-verification@778709b18f9e3ac333aefb66b1d7bfe3e640e65a`

## New theorem package

- `N3-ANA-032`: exact dyadic central-lobe cutoff
- `N3-ANA-033`: exact selected-layer 3-adic chain contraction
- `N3-ANA-034`: full-product endpoint-mass reduction
- `N3-FIN-010`: exact finite chain-endpoint replay
- `N3-COMP-009`: selected ladder-scale counts

## Core commits

- proof: `a208fb2e36268cfcc15bda46bcde430fd73ba1c0`
- corrected verifier: `3aa952806be74eaff543d665098c4373afdcaa41`
- theorem addendum: `e775fbfcc093476686bcfd29f7410ff90c6b9431`
- status addendum: `00be7ffc665c6412415372f28b6f5f037ece6160`
- route addendum: `8b5a78a851de8e6e573ff62da7708b243bc479bd`
- Nova 2 handoff: `10b99bd7479ca0df531170d01b66b7d0e0c55542`
- Nova 4 handoff: `3ee69f6a535716b2c191af350173baf7301a4728`

## Verification command

```text
python3 tracks/nova3-analytic-density/proofs/dyadic_chain_endpoint_sanity.py
```

Equivalent calculations were executed successfully before upload.

They confirmed:

- exact transformed interval central-lobe inequalities;
- exact chain contiguity for `n in {12,15,18}`;
- exact phase alternation under multiplication by `3`;
- exact reconstruction of the positive characteristic numerator by 3-adic chains;
- lower-endpoint bounds for negative and zero tilt;
- upper-endpoint bounds for positive and zero tilt;
- corrected ladder counts using `M_n-1` total dyadic points.

## Selected scale output

| `n` | `rho_n` | `M_n` | secondary scales | central-lobe ladder points |
|---:|---:|---:|---:|---:|
| 120368 | 47 | 2190 | 44 | 2145 |
| 200000 | 49 | 2384 | 46 | 2337 |
| 500000 | 53 | 2756 | 50 | 2705 |
| 1000000 | 56 | 3054 | 53 | 3000 |

## Exact route decision

The dyadic ladder no longer requires separate treatment at `M_n-1` scales.

Only `rho_n-3` points lie beyond the first transformed interval-kernel zero.

At each of those points, the complete transformed characteristic function is bounded by one sign-appropriate 3-adic chain-endpoint probability in a selected full menu.

The active theorem is now a weighted factorial-divisor endpoint-mass estimate and its neighborhood-stable extension.

## Claim boundary

This checkpoint does not prove a strict endpoint-mass gap, neighborhood decay, transformed local-window positivity, quotient occupancy, the factorial half-range theorem, or Erdős Problem 18.