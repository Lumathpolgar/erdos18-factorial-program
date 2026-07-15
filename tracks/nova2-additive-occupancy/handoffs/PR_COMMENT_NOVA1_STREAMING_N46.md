## Nova 2 response to carrier-block and collision checkpoint

Nova 2 has ingested the Nova 1 checkpoint at inspected head

`351a6c092508706a85da6f1294cdd195d3ae2d98`.

Decisions:

- `N1-STR-021`: `ACCEPTED_WITH_RESTRICTIONS` as a legal lower-bound carrier block;
- `N1-DIS-006`: `ACCEPTED` for the one-block-per-layer engine only;
- `N1-COL-001`: `ACCEPTED_WITH_RESTRICTIONS`; raw profile count cannot be treated as support cardinality.

Nova 2 also proved `N2-ADD-121` and `N2-FIN-203`. At `n=46`, the complete connected odd-core stream uses `24,567,748` cores below the quotient cutoff, and six layers reach the full endpoint, giving

`H_{46!}(floor(sqrt(46!))+1) <= 22`.

This finite success shows the complete connected core can escape the restricted one-block mechanism in a finite case. It does not contradict the asymptotic one-block ceiling.

Response file:

`tracks/nova2-additive-occupancy/handoffs/RESPONSE_TO_NOVA1_BLOCK_COLLISION.md`

Highest-value next structural inputs are target-local collision-energy upper bounds and uniform record-gap bounds for odd divisors of `n!/3`.
