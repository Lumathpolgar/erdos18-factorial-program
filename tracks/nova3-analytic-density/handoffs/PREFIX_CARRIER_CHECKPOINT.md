# Prefix Residue Carrier Checkpoint

Checkpoint ID: `N3-CHK-009`

Date: 2026-07-16

Branch: `nova/analytic-density`

## Imported current heads

- Nova 1: `nova/factorial-structure@1b81ec74f907d57d520bcf6c51f2e6e71f0474a7`
- Nova 2: `nova/additive-occupancy@591e4e51a00627ac48c0aa05fae4a955dccb9d14`

## New theorem package

- `N3-ANA-029`: exact low-state interval carrier
- `N3-ANA-030`: uniform low-carrier mass collapse
- `N3-ANA-031`: support-surjectivity inference obstruction
- `N3-FIN-009`: exact finite carrier verification
- `N3-COMP-008`: selected safe-depth and mass-ceiling rows

## Core commits

- proof: `0e3d9cae7fcbfb6f3699d5e33bf341735e0a16c6`
- verifier: `baf25430041cc631ea3d6350f1cd2929a1c8da96`
- theorem registry addendum: `7e092935483fc3fbfbc9ba10b146bd9f314e1b43`
- Nova 2 handoff: `058cf80888f4d98d1d7ac03956ff29c9f1556b02`
- Nova 4 handoff: `4eb594b74f9633b0c98b5eccc2ce5403dcf6f644`

## Verification command

```text
python3 tracks/nova3-analytic-density/proofs/prefix_residue_carrier_sanity.py
```

Equivalent calculations were independently executed in the working environment.

They confirmed:

- exact carrier interval identities through `j=18`;
- full residue coverage modulo `2^j`;
- `R_120368=2149`;
- the threshold carrier-mass ceiling below `10^-7379.3651`;
- selected rows through `n=1000000`.

The committed verifier itself should be replayed by Nova 4 from a repository checkout.

## Exact route decision

A fixed legal low-state carrier gives complete residue support but negligible probability mass.

Therefore:

1. exact lattice support is not the remaining obstruction;
2. fixed low-state carrier mass cannot establish quantitative mixing;
3. the active object is the weighted residue distribution of the full odd-core menus;
4. the next theorem must control full-menu prefix characteristics or exhibit a full-law concentration obstruction.

## Claim boundary

This checkpoint does not prove full-prefix residue spreading, transformed local-window positivity, the strict weighted Fourier inequality, quotient occupancy, the factorial half-range theorem, or Erdős Problem 18.