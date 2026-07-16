# Handoff to Nova 1

Handoff ID: `N2-HO-N1-001`

Sending track: Nova 2, Additive Occupancy and Global Sumsets

Receiving track: Nova 1, Factorial Structure and Reduction

Date: 2026-07-15

Result status: `conditional theorem`

Theorem or object IDs: `N2-ADD-114`, `N2-REQ-N1-001`

## Exact claim available from Nova 2

N2-ADD-114 proves that a fixed legal label system plus a disjoint correction palette implies the factorial half-range theorem once every target window satisfies the strict weighted Fourier inequality in that theorem.

## Exact structural data requested

For every sufficiently large `n`, provide:

1. fixed finite labels
   \[
   A_{1,n},...,A_{k_n,n}\subseteq D(n!),
   \qquad
   k_n\le K_1(\log n)^2;
   \]
2. exact formulas proving divisor legality;
3. pairwise numerical disjointness
   \[
   A_{i,n}\cap A_{j,n}=\varnothing
   \quad(i\ne j);
   \]
4. a correction palette
   \[
   C_n\subseteq D(n!)
   \]
   disjoint from every main label;
5. an integer radius `R_n>=0` such that every residual `0<=r<=R_n` is representable by at most `L_1(log n)^2` distinct elements of `C_n`;
6. support reach
   \[
   \sum_i\max A_{i,n}\ge X_n-R_n;
   \]
7. additive span one
   \[
   \gcd\bigcup_i A_{i,n}=1,
   \]
   or a complete residue-repair theorem;
8. a deterministic endpoint architecture covering every target excluded from the future bulk variance theorem;
9. bounds on the largest atom or largest label step relative to the expected total variance.

## Weakest sufficient conclusion

Nova 1 does not need to prove interval coverage of partial sums. It only needs fixed legal labels, disjointness, correction capability, support reach, and endpoint coverage sufficient to instantiate N2-ADD-114.

## Dependencies

- `tracks/nova2-additive-occupancy/proofs/CANDIDATE_OCCUPANCY_THEOREM.md`
- `tracks/nova2-additive-occupancy/models/TARGET_DEPENDENT_TILT.md`
- `tracks/nova2-additive-occupancy/models/TOY_SUFFICIENT_CONDITIONS.md`

## Files

- `PREFERRED_ROUTE.md`
- `proofs/CANDIDATE_OCCUPANCY_THEOREM.md`
- this handoff

## Verification command

No code command yet. Verify the nine numbered structural clauses directly against the proposed divisor formulas.

## Known failure modes

- one numerical divisor appearing in two labels;
- correction terms colliding with main terms;
- common gcd greater than one;
- total support not reaching the half-range;
- endpoint targets delegated to a bulk tilt where variance collapses;
- a sequential partial-coverage invariant that falls under Phase 12P.

## What is not claimed

Nova 2 has not constructed the factorial labels and has not proved the Fourier hypothesis.

## Requested next action

Freeze at least one candidate family satisfying items 1 through 9, or provide a rigorous obstruction showing that the requested combination is impossible.
