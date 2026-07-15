# Nova 1 Theorem Registry

## Status rule

Every item is labeled as one of:

- **proved theorem**;
- **conditional theorem**;
- **finite certificate**;
- **computational evidence**;
- **disproved route**.

No finite result is promoted to an asymptotic theorem. No formal profile count is treated as numerical additive occupancy.

## Structural and reduction theorems

### N1-STR-003: Factorial valuation budget

- Result label: **proved theorem**
- Conclusion: exact Legendre and digit-sum formulas, quotient bands, dyadic bands, and factorial 2-adic multiplicity
- Proof: `proofs/VALUATION_BUDGET_LEMMAS.md`

### N1-STR-004: Valuation-box uniqueness

- Result label: **proved theorem**
- Conclusion: exponent boxes produce exactly `product_p(a_p+1)` unique legal divisors
- Proof: `FACTORIAL_DIVISOR_ATLAS.md`

### N1-STR-005: Valuation-budget partition

- Result label: **proved theorem**
- Conclusion: allocated valuation budgets preserve divisor legality
- Proof: `FACTORIAL_DIVISOR_ATLAS.md`

### N1-STR-006: Marker-signature distinctness

- Result label: **proved theorem**
- Conclusion: pairwise distinct marker signatures force numerical distinctness
- Proof: `proofs/DISTINCTNESS_AND_CORRECTION.md`

### N1-STR-007: Complement pairing

- Result label: **proved theorem**
- Conclusion: if `R^2|n!` and `z|R`, then `R/z` and `Rz` are legal; the stated conditions give range and distinctness
- Proof: `proofs/COMPLEMENT_PAIRING_LEMMA.md`

### N1-COR-001: Binary correction palette

- Result label: **proved theorem**
- Conclusion: every `0<=t<2^r` has a unique subset representation using `{1,2,...,2^(r-1)}`
- Proof: `proofs/DISTINCTNESS_AND_CORRECTION.md`

### N1-RED-002: Downward-window correction

- Result label: **proved theorem**
- Conclusion: downward `2^r-1` main occupancy plus the binary palette yields exact local coverage
- Proof: `proofs/DISTINCTNESS_AND_CORRECTION.md`

### N1-OBS-002: Counting-capacity obstruction

- Result label: **proved theorem**
- Conclusion: if a finite attainable set is downward `R`-dense on `[0,X]`, then `|S|(R+1)>=X+1`
- Proof: `proofs/COUNTING_CAPACITY_OBSTRUCTION.md`

### N1-STR-008: Menu entropy lower bound

- Result label: **proved theorem**
- Conclusion: `O((log n)^2)` layers with polynomial correction require geometric-mean menu size `exp(Omega(n/log n))`
- Proof: `proofs/MENU_ENTROPY_REQUIREMENT.md`

### N1-STR-009: High-prime menu capacity

- Result label: **proved theorem**
- Conclusion: admissible layers contain at least `2^(pi(n)-pi(n/2)-1)-1` high-prime cores
- Proof: `proofs/HIGH_PRIME_MENU_CAPACITY.md`

## Marker-three route

### N1-STR-014: Marker-three legality and distinctness

- Result label: **proved theorem**
- Conclusion: every `3*2^(t-1)*u` is legal; exact 2-adic valuations distinguish layers; divisibility by `3` separates main terms from the binary palette
- Proof: `proofs/MARKER_THREE_LATTICE_REPAIR.md`

### N1-STR-015: Exact support lattice and residues

- Result label: **proved theorem**
- Conclusion: the main support generates exactly `3Z`; palette sums attain every residue modulo `3`
- Proof: `proofs/MARKER_THREE_LATTICE_REPAIR.md`

### N1-RED-004: Quotient-window correction theorem

- Result label: **proved theorem**
- Hypothesis: quotient rainbow sums meet every interval `[q-W_n,q]`
- Conclusion: `H_{n!}(X_n+1)<=M_n+r_n`
- Exact radius: `W_n=floor((2^r_n-3)/3)`
- Proof: `proofs/MARKER_THREE_LATTICE_REPAIR.md`

### N1-STR-016: Odd-digit one-gap lemma

- Result label: **proved theorem**
- Conclusion: positional sums with digits `{0,1,3,5,...,m}` have maximum downward gap one on `[0,m(2^L-1)]`
- Proof: `proofs/MARKER_THREE_LATTICE_REPAIR.md`

### N1-STR-017: Unconditional initial interval

- Result label: **proved theorem**
- Conclusion: every integer through `3m_n(2^M_n-1)+2` has a legal representation using at most `M_n+r_n` terms
- Range status: `exp(O((log n)^2))`, not the factorial half-range
- Proof: `proofs/MARKER_THREE_LATTICE_REPAIR.md`

### N1-STR-018: Repaired high-prime menu bound

- Result label: **proved theorem**
- Imported dependency: `N3-ANA-010` from branch `nova/analytic-density`, exact commit `e60069f797af878711e7a9d4abb1fb6188a1f724`
- Hypotheses: `n>=120368`, `1<=t<=M_n`
- Conclusion: `|U_t(n)|>=2^(pi(n)-pi(n/2)-1)>=2^(n/(3 log n)-1)`
- Proof: `proofs/MARKER_THREE_MENU_CAPACITY.md`

### N1-CAP-002: Explicit repaired profile-capacity gate

- Result label: **proved theorem**
- Hypotheses: `n>=120368`
- Conclusion: `2^r_n product_t(|U_t(n)|+1)>=X_n+1`
- What is not claimed: injectivity, occupancy, or maximum-gap control
- Proof: `proofs/MARKER_THREE_MENU_CAPACITY.md`

### N1-STR-019: Multiplicative 3-density

- Result label: **proved theorem**
- Hypotheses: `n>=6`
- Object: `D_n=n!/(3*2^v_2(n!))`
- Conclusion: every real `1<=z<=D_n` has a divisor `d|D_n` with `z/3<d<=z`
- Proof: `proofs/QUOTIENT_ENDPOINT_SUPPORT.md`

### N1-STR-020: Quotient endpoint support

- Result label: **proved theorem**
- Hypotheses: `n>=12`
- Conclusion: three distinct legal quotient terms have total greater than `X_n/3`, so maximum support exceeds `floor(X_n/3)`
- What is not claimed: a sum in the final downward endpoint window
- Proof: `proofs/QUOTIENT_ENDPOINT_SUPPORT.md`

### N1-RED-006: Coarse deterministic contraction

- Result label: **proved theorem**
- Conclusion: after `L` increasing quotient layers, a legal selection leaves residual below `max((2/3)^L q,2^L)`
- Limitation: this does not reach the polynomial radius `W_n`
- Proof: `proofs/QUOTIENT_ENDPOINT_SUPPORT.md`

### N1-STR-021: Factorial arithmetic core blocks

- Result label: **proved theorem**
- Object:
  \[
  A_k=\frac{k!}{3\cdot2^{v_2(k!)}},
  \qquad
  m_{n,k}=\max\{m\le n-k:m\text{ odd}\}
  \]
- Conclusion: `A_k,3A_k,...,m_{n,k}A_k` are legal odd cores and form a connected carrier block whenever the threshold is at least `2A_k`
- Imported criterion: Nova 2 `N2-ADD-119` at exact commit `b15278e21f91e0e188b1c7c3e9a10e58a1db20fe`
- Proof: `proofs/FACTORIAL_BLOCK_CARRIER_OBSTRUCTION.md`

### N1-COL-001: Exponential carry collisions

- Result label: **proved theorem**
- Hypotheses: `n>=120368`
- Identity: `3*2^e=2^e+2^(e+1)`
- Conclusion: at least `2^floor(M_n/2)` distinct legal quotient profiles map to the same numerical sum `4^floor(M_n/2)-1`
- Consequence: profile injectivity is false; maximum collision multiplicity is at least `exp(Omega((log n)^2))`
- Proof: `proofs/RAINBOW_CARRY_COLLISIONS.md`

## Conditional results

### N1-RED-005: Marker-three half-range reduction

- Result label: **conditional theorem**
- Hypothesis: the exact quotient rainbow occupancy statement in `handoffs/TO_NOVA2.md`
- Conclusion:
  \[
  H_{n!}(\lfloor\sqrt{n!}\rfloor+1)
  \le
  \lceil16(\log n)^2\rceil+\lceil4\log n\rceil
  \]
- Location: `PREFERRED_ROUTE.md`

### N1-RED-001: Track B reconstruction

- Result label: **conditional theorem** under reconstruction
- Goal:
  \[
  H_{n!}(\lfloor\sqrt{n!}\rfloor+1)=O((\log n)^2)
  \Longrightarrow h(n!)=O((\log n)^3)
  \]
- Dependency: archived Track B source package and current endpoint audit

## Finite and computational results

### N1-CMP-003: Marker-three reduced quotient audit

- Result label: **computational evidence**
- Domain: every `7<=n<=14` under reduced legal parameters
- Conclusion: maximum downward quotient distance at most one
- Verifier: `verification/marker_three_sanity.py`

### N1-CMP-004: Endpoint support finite audit

- Result label: **finite certificate**
- Checks: 3-density for `6<=n<=20`, endpoint crossing for `12<=n<=20`, and exhaustive coarse contraction for `12<=n<=14`
- Verifier: `verification/endpoint_support_sanity.py`

### N1-CMP-005: Block and collision audit

- Result label: **finite certificate**
- Checks: factorial block legality, exact carrier ceiling, explicit carry collisions, and scale separation
- Verifier: `verification/block_collision_sanity.py`
- Report: `verification/BLOCK_COLLISION_FINITE_REPORT.md`

## Disproved routes

### N1-DIS-001

- Result label: **disproved route**
- Claim rejected: prime powers of one prime are independent coordinates

### N1-DIS-002

- Result label: **disproved route**
- Claim rejected: a fixed pool of `O((log n)^2)` binary or ternary choices covers the half-range

### N1-DIS-003

- Result label: **disproved route**
- Claim rejected: polynomial-size menus in `O((log n)^2)` layers cover the half-range with polynomial correction

### N1-DIS-004

- Result label: **disproved route**
- Claim rejected: complement pairing by itself implies additive density

### N1-DIS-005: Original valuation-tagged lattice

- Result label: **disproved route**
- Claim rejected: old addresses `e_t=r_n+t` satisfy the radius `2^r_n-1` request
- Countertheorem: Nova 2 `N2-ADD-115`
- Exact source: branch `nova/additive-occupancy`, commit `45c74a5fa747551422ffcad7d3ddf22788fbe622`

### N1-DIS-006: One factorial block per carrier layer

- Result label: **disproved route**
- Claim rejected: one factorial arithmetic block per layer can make the Nova 2 carrier recursion reach `Y_n` within `M_n` layers
- Exact ceiling:
  \[
  E_{M_n}+W_n+1
  \le
  (W_n+1)(1+n/2)^{M_n}
  <Y_n
  \]
  for every `n>=120368`
- What remains possible: the complete connected core, multiple interacting blocks, and final-only proofs
- Proof: `proofs/FACTORIAL_BLOCK_CARRIER_OBSTRUCTION.md`

## Historical conditional artifact

### N1-RED-003

- Result label: **conditional theorem**
- Status: retired because its exact occupancy hypothesis was disproved
- Replacement: `N1-RED-005`

## Promotion rule

No conditional theorem becomes proved until every dependency is proved and independently reconstructed. No finite certificate or computational evidence is promoted to an asymptotic theorem.