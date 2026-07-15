# Parallel Research Tracks

This directory contains four isolated but interoperable Nova workstreams.

## Tracks

1. [Nova 1: Factorial Structure and Reduction](nova1-factorial-structure/README.md)
   - Branch: `nova/factorial-structure`
2. [Nova 2: Additive Occupancy and Global Sumsets](nova2-additive-occupancy/README.md)
   - Branch: `nova/additive-occupancy`
3. [Nova 3: Analytic Divisor Density](nova3-analytic-density/README.md)
   - Branch: `nova/analytic-density`
4. [Nova 4: Computation, Falsification, and Verification](nova4-computational-verification/README.md)
   - Branch: `nova/computational-verification`

## Shared rules

Every track must:

- work only on its assigned branch;
- use the definitions in `docs/COMMON_NOTATION.md`;
- follow `docs/SHARED_MATHEMATICAL_CONTRACT.md`;
- classify evidence under `docs/VERIFICATION_AND_EVIDENCE_STANDARD.md`;
- submit cross-track dependencies through `docs/CROSS_TRACK_HANDOFF_PROTOCOL.md`;
- update the theorem registry for frozen results;
- preserve failed routes and counterexamples;
- avoid any claim that the full problem is solved before integration passes all gates.

## Initial files each Nova creates on its branch

- `STATUS.md`
- `THEOREMS.md` or the charter's track-specific registry
- `OPEN_REQUIREMENTS.md`
- proof, code, dataset, or source ledgers required by the charter

Templates are available under `docs/templates/`.

## Integration

Accepted results are assembled under `integration/`. A track's completion does not imply completion of Erdős Problem 18.
