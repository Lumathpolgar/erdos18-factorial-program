# Nova 4 Open Requirements

## N4-REQ-N2-001

Owner: Nova 2

Frozen source head: `45c74a5fa747551422ffcad7d3ddf22788fbe622`

Handoff: `N2-HO-N4-001-v2`

Status: `RECEIVED_READY_FOR_AUDIT`

Build a reusable exact lattice and residue falsification gate, reproduce `N2-OBS-107`, and apply the gate before any convolution or Fourier computation.

## N4-REQ-N1-001

Owner: Nova 1

Frozen source head: `fa11f4b2cb86a2dd791df189ada12757be791804`

Handoff: `N1-HO-N4-001`

Status: `RECEIVED_READY_FOR_AUDIT`

Run the exact capacity-threshold audit and reduced rainbow model under the frozen formulas and ranges.

## N4-REQ-N3-001

Owner: Nova 3

Frozen source head: `0ce88b28dc2e6641093526f5777bb31f658e3515`

Handoff: `N3-HO-N4-001`

Status: `RECEIVED_READY_FOR_AUDIT`

Independently reconstruct the product-model formulas, exact finite moments, local-count ceiling, and requested analytic evidence tables.

## N4-REQ-INT-001

Owner: Integration

Status: `BLOCKED_MISSING_SOURCE_ARTIFACT`

Reconstruct the Track B half-range-to-global implication. The archive index exists, but the named source ZIP and verifier are not present in the repository.

## N4-REQ-CMP-001

Owner: Nova 4

Result class: `unknown due to resource limits`

Extend exact profiles to `n=14` with a more memory-efficient witness strategy, a target-partitioned proof certificate, or a different exact algorithm.

## Rule

Nova 4 reports mismatches and counterexamples to the owning track. It does not silently revise another track's statement or status.
