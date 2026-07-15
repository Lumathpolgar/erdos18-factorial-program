# Nova 4 Verification Request Queue

Date: 2026-07-15

Nova 4 never changes another track's theorem status. Every request freezes the sending branch and exact commit SHA before testing.

## N4-REQ-N1-001

Sending track: Nova 1

Frozen branch: `nova/factorial-structure`

Frozen commit: `f2e011d689d56af07ed01de08e00c05457ca9c80`

Status: `AWAITING_FROZEN_ARTIFACT`

Requested input:

- exact theorem or construction statement;
- divisor formulas and parameter ranges;
- selection and correction rules;
- claimed distinctness mechanism;
- expected term bound;
- replay or construction command.

Planned audit:

- exact divisor legality;
- numerical collision search;
- exact target and endpoint checks;
- smallest failing parameter search;
- term-count recomputation.

## N4-REQ-N2-001

Sending track: Nova 2

Frozen branch: `nova/additive-occupancy`

Frozen commit: `71370633b1e6726bf6f9e3b334d42cfc34512c06`

Status: `AWAITING_FROZEN_ARTIFACT`

Requested input:

- exact finite layer or sumset model;
- selection multiplicities;
- target interval and window orientation;
- completeness claim;
- pruning or convolution assumptions.

Planned audit:

- exact support generation;
- first uncovered target;
- lattice obstruction detection;
- duplicate numerical divisor detection;
- exhaustive finite-domain classification.

## N4-REQ-N3-001

Sending track: Nova 3

Frozen branch: `nova/analytic-density`

Frozen commit: `c79cddee6e8940e27ff256c29a85a3fc93766f7b`

Status: `READY_FOR_PARAMETER_REQUEST`

Available exact data:

- prime valuations of `n!`;
- divisor counts;
- eligible half-range divisor counts;
- exact `lambda_{n!}(x)` profiles for `1 <= n <= 13`;
- exact maxima and hardest-target lists;
- greedy failure counts.

Requested input:

- exact analytic expression to test;
- finite parameter range;
- rounding and endpoint conventions;
- error metric and claimed inequality.

Planned audit:

- exact finite comparison;
- transition-range stress test;
- smallest inequality failure;
- status separation between evidence and theorem.
