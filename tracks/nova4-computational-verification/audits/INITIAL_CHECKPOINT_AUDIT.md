# Initial Checkpoint Audit

Date: 2026-07-15

Result class: `exact finite theorem audit`

## Checks completed

- startup definitions and endpoints reconstructed;
- branch heads frozen by exact SHA;
- source-path mismatch recorded;
- exact arithmetic core implemented;
- representation schema implemented;
- corrupted certificates rejected;
- two independent exact search methods agree;
- exact half-range profiles completed for `1 <= n <= 13`;
- 109,947 targets replayed;
- smallest descending-greedy counterexample published;
- `n=14` timeout recorded as unknown.

## Tests

```text
21 tests passed
0 tests failed
```

## Prohibited inference

The finite equality `H = 3` for `8 <= n <= 13` is not evidence of eventual constancy and is not promoted to an asymptotic claim.
