# Nova 1 Theorem Registry

## Active statements

### N1-STR-001

- Status: `OPEN`
- Type: structural construction
- Goal: Construct labeled divisor families of `n!` across enough logarithmic scales to support uniform half-range representation with total polylogarithmic term cost.
- Required outputs: legality, cross-family distinctness, scale range, selection budget, and exact additive requirement.

### N1-STR-002

- Status: `OPEN`
- Type: correction architecture
- Goal: Reserve a divisor palette that represents every residual in a stated interval while remaining disjoint from all main construction terms.

### N1-RED-001

- Status: `OPEN_RECONSTRUCTION`
- Type: conditional reduction
- Goal: Reconstruct the archived implication
  \[
  H_{n!}(\lfloor\sqrt{n!}\rfloor+1)=O((\log n)^2)
  \Longrightarrow
  h(n!)=O((\log n)^3)
  \]
  under the frozen definition of `H_N`.

## Promotion requirements

Each statement must be moved to a separate theorem artifact using `docs/templates/THEOREM_TEMPLATE.md` before promotion to `PROVED` or `CONDITIONAL`.
