# Response to Nova 1 Block and Collision Checkpoint

Response ID: `N2-HO-N1-003-RESPONSE`

Sending track: Nova 2, Additive Occupancy and Global Sumsets

Receiving track: Nova 1, Factorial Structure and Reduction

Date: 2026-07-15

## Inspected source

- branch: `nova/factorial-structure`
- inspected head: `351a6c092508706a85da6f1294cdd195d3ae2d98`
- PR checkpoint: carrier-block obstruction and rainbow collision checkpoint

## Intake decisions

### N1-STR-021

Outcome: `ACCEPTED_WITH_RESTRICTIONS`.

The factorial arithmetic block is a legal connected subfamily when its exact threshold condition holds. It is useful as a lower-bound carrier certificate but does not describe the complete odd-core connected component.

### N1-DIS-006

Outcome: `ACCEPTED` for the one-block-per-layer proof engine only.

The stated `exp(O((log n)^3))` ceiling rejects any asymptotic argument that uses only one factorial arithmetic block per layer. It does not reject N2-ADD-120, which scans the complete connected odd-core component, and it does not reject the final-only marker-three model.

### N1-COL-001

Outcome: `ACCEPTED_WITH_RESTRICTIONS`.

The exact carry identity proves exponential lower bounds on profile-fiber multiplicity. Therefore raw profile count cannot be treated as support cardinality. This does not by itself disprove occupancy, because many profiles may collide while every target window remains occupied.

## New finite evidence from Nova 2

Nova 2 has now proved N2-ADD-121 and N2-FIN-203.

At `n=46`, the complete connected-core stream uses `24,567,748` odd cores below the quotient cutoff. Six complete-menu layers reach the full quotient endpoint and give

\[
H_{46!}(\lfloor\sqrt{46!}\rfloor+1)\le22.
\]

Thus, at least in this finite case, the complete connected core escapes the restricted one-block mechanism. This is finite evidence only and does not contradict the asymptotic one-block ceiling.

Proof and certificate:

- `proofs/MARKER_THREE_STREAMING_N46_AUDIT.md`
- `verification/data/marker_three_streaming_n46.json`

## Updated open Nova 1 input

The next structural result with highest value to Nova 2 is an upper bound on target-local collision energy or on the maximum fiber size for sums in a window `[q-W_n,q]`, not a raw global profile count.

A second high-value input is a uniform theorem bounding record gaps between consecutive odd divisors of `n!/3` below the layer cutoffs. Such a theorem could promote the complete N2-ADD-120 recursion beyond finite computation.

## Claim boundary

This response does not promote N2-ADD-120 asymptotically, does not show that collisions are harmless, and does not claim the factorial half-range theorem.
