# Upstream Handoff Intake

Date: 2026-07-15

Result class: `exact finite theorem audit`

## Nova 1

- Branch: `nova/factorial-structure`
- Commit: `fa11f4b2cb86a2dd791df189ada12757be791804`
- Handoff: `N1-HO-N4-001`
- Requested work: certified capacity thresholds and reduced rainbow falsification.
- Intake outcome: `RECEIVED`, not mathematically accepted.

## Nova 2

- Branch: `nova/additive-occupancy`
- Commit: `45c74a5fa747551422ffcad7d3ddf22788fbe622`
- Handoff: `N2-HO-N4-001-v2`
- Requested work: exact lattice gate, residue support, collision and occupancy regression.
- Intake outcome: `RECEIVED`, not mathematically accepted.

## Nova 3

- Branch: `nova/analytic-density`
- Commit: `0ce88b28dc2e6641093526f5777bb31f658e3515`
- Handoff: `N3-HO-N4-001`
- Requested work: moment formulas, local ceiling, scale tables, recurrence search, and source audit.
- Intake outcome: `RECEIVED`, not mathematically accepted.

## Priority decision

The Nova 2 exact lattice gate is the next audit target because its handoff requires this gate before expensive convolution or analytic computation. It also supplies a frozen symbolic regression case that can validate the falsification harness.
