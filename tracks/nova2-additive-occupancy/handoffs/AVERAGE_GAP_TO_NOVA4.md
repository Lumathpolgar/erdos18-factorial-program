# Handoff to Nova 4: Average-Gap Utilization

Handoff ID: `N2-HO-N4-006`

## Frozen Nova 2 source

- branch: `nova/additive-occupancy`;
- proof commit: `9a1382836f8c83bbaafc9592d79895224158c3fa`;
- exact-check commit: `1a6d128d1d4a846c2123090d0986f15a1c8be31d`;
- results: `N2-OBS-109`, `N2-ADD-123`;
- proof: `proofs/AVERAGE_GAP_UTILIZATION_CRITERION.md`;
- verifier: `verification/average_gap_utilization_sanity.py`.

## Imported finite source

- Nova 1 branch: `nova/factorial-structure`;
- `n=54` source commit: `dac958b62ef069310901f5063dbf8bd6cbe3c0e3`;
- `n=55` source commit: `6b31a320fa4c4bd4c9b2395e60faa174198e022e`;
- finite certificates: `N1-FIN-009`, `N1-FIN-010`.

## Reconstruction tasks

1. Reconstruct the two odd-core families in N2-OBS-109.
2. Verify they have identical threshold `D`, prefix count `K`, and first blocking gap `D+2`.
3. Verify one utilization factor tends to zero and the other tends to one.
4. Reconstruct the exact floor bound
   \[
   D/(D+1)<\phi\le1.
   \]
5. Reconstruct both sides of the N2-ADD-123 utilization sandwich.
6. Reject corrupted fixtures with an even core, an internal gap above `D`, an incorrect blocking gap, or a false utilization formula.
7. Independently replay `n=54` and `n=55` if resources permit.
8. Extend the exact finite boundary from `n=56` using fail-closed resource handling.

## Required output

Return separate decisions for:

- `N2-OBS-109`;
- `N2-ADD-123`;
- `N1-FIN-009`;
- `N1-FIN-010`;
- finite extension beginning at `n=56`.

A resource limit is `UNKNOWN_DUE_TO_RESOURCE_LIMITS`, not a counterexample.

## Claim boundary

The requested audit concerns one sequential sufficient engine. Failure of its utilization condition does not disprove the complete marker-three model or the final-only routes.