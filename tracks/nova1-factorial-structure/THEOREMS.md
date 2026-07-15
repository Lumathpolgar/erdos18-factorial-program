# Nova 1 Theorem Registry

## Frozen proved results

### N1-STR-003: Factorial valuation budget

- Result label: **proved theorem**
- Hypotheses: integer `n>=1`, prime `p<=n`
- Conclusion: Legendre formula, digit-sum formula, quotient bands, dyadic bands, and `Theta((log n)^2)` available 2-adic marker exponents for large `n`
- Constants effective: yes in the exact formulas; asymptotic threshold not optimized
- Distinctness mechanism: not applicable
- Boundary treatment: exact for every `n,p`
- Proof: `proofs/VALUATION_BUDGET_LEMMAS.md`

### N1-STR-004: Valuation-box uniqueness

- Result label: **proved theorem**
- Hypotheses: finite prime set `P`, allocations `0<=a_p<=v_p(n!)`
- Conclusion: exactly `product_p(a_p+1)` unique legal divisors
- Constants effective: yes
- Distinctness mechanism: unique factorization
- Proof: `FACTORIAL_DIVISOR_ATLAS.md`

### N1-STR-005: Valuation-budget partition

- Result label: **proved theorem**
- Hypotheses: nonnegative allocations summing to at most `v_p(n!)` at every prime
- Conclusion: every assembled product remains a divisor of `n!`
- Constants effective: yes
- Proof: `FACTORIAL_DIVISOR_ATLAS.md`

### N1-STR-006: Marker-signature distinctness

- Result label: **proved theorem**
- Hypotheses: pairwise distinct marker-prime signatures; cores avoid marker primes
- Conclusion: labeled divisors are numerically distinct
- Constants effective: yes
- Distinctness mechanism: marker valuations
- Proof: `proofs/DISTINCTNESS_AND_CORRECTION.md`

### N1-STR-007: Complement pairing

- Result label: **proved theorem**
- Hypotheses: `Q=R^2|n!`, distinct `z_i|R`, `1<z_i<=X/R`
- Conclusion: `R/z_i` and `Rz_i` are legal, bounded, and pairwise distinct
- Constants effective: yes
- Distinctness mechanism: low/high separation and multiplier injectivity
- Proof: `proofs/COMPLEMENT_PAIRING_LEMMA.md`

### N1-COR-001: Binary correction palette

- Result label: **proved theorem**
- Hypotheses: `r-1<=v_2(n!)`
- Conclusion: every `0<=t<2^r` is a sum of at most `r` distinct powers of two dividing `n!`
- Constants effective: yes
- Distinctness mechanism: unique binary expansion
- Boundary treatment: exact endpoints `0` and `2^r-1`
- Proof: `proofs/DISTINCTNESS_AND_CORRECTION.md`

### N1-RED-002: Downward-window correction

- Result label: **proved theorem**
- Hypotheses: main sums are downward `2^r-1` dense on `[2^r,X_n]`, legal, distinct, and palette-disjoint
- Conclusion: `H_{n!}(X_n+1)<=K(n)+r`
- Constants effective: yes
- Endpoint convention: exact frozen `H_N` convention
- Proof: `proofs/DISTINCTNESS_AND_CORRECTION.md`

### N1-OBS-002: Capacity obstruction

- Result label: **proved theorem**
- Hypotheses: finite attainable set downward `R`-dense on `[0,X]`
- Conclusion: `|S|(R+1)>=X+1`; rainbow profile entropy must exceed target entropy minus correction entropy
- Constants effective: yes
- Proof: `proofs/COUNTING_CAPACITY_OBSTRUCTION.md`

### N1-STR-008: Menu entropy lower bound

- Result label: **proved theorem**
- Hypotheses: at most `A(log n)^2` layers and polynomial residual width
- Conclusion: geometric-mean layer-state count is at least `exp(n/(3A log n))` for all sufficiently large `n`
- Constants effective: proof uses an unoptimized sufficiently-large threshold
- Proof: `proofs/MENU_ENTROPY_REQUIREMENT.md`

### N1-STR-009: High-prime menu capacity

- Result label: **proved theorem**
- Hypotheses: admissible address `e<=floor(v_2(n!)/2)-1`
- Conclusion:
  \[
  |U_e(n)|\ge2^{\pi(n)-\pi(n/2)-1}-1
  \]
- Constants effective: exact in terms of the prime count
- Distinctness mechanism: subset products of distinct high primes
- Proof: `proofs/HIGH_PRIME_MENU_CAPACITY.md`

## Frozen conditional results

### N1-CAP-001: Explicit preferred-route capacity

- Result label: **conditional theorem**
- Hypothesis:
  \[
  \pi(n)-\pi(n/2)\ge n/(3\log n)
  \]
  for all sufficiently large `n`
- Conclusion: the preferred full menus satisfy the necessary profile-capacity inequality with
  \[
  M_n=\lceil16(\log n)^2\rceil,
  \qquad
  r_n=\lceil4\log n\rceil
  \]
- Dependency: `N1-STR-009`, explicit Nova 3 prime-interval audit
- What is not claimed: additive occupancy
- Location: `proofs/HIGH_PRIME_MENU_CAPACITY.md`

### N1-RED-003: Preferred-route half-range reduction

- Result label: **conditional theorem**
- Hypothesis: the exact rainbow occupancy statement in `handoffs/TO_NOVA2.md`
- Conclusion:
  \[
  H_{n!}(\lfloor\sqrt{n!}\rfloor+1)
  \le
  \lceil16(\log n)^2\rceil+
  \lceil4\log n\rceil
  \]
  for all sufficiently large `n`
- Dependencies: `N1-STR-003`, `N1-STR-006`, `N1-COR-001`, `N1-RED-002`
- Distinctness mechanism: one selected term per unique 2-adic address plus palette disjointness
- Boundary treatment: palette covers `0<=x<2^{r_n}`; occupancy covers through `X_n`
- Location: `PREFERRED_ROUTE.md`

### N1-RED-001: Track B reconstruction

- Result label: **conditional theorem** under reconstruction
- Goal:
  \[
  H_{n!}(\lfloor\sqrt{n!}\rfloor+1)=O((\log n)^2)
  \Longrightarrow
  h(n!)=O((\log n)^3)
  \]
- Dependency: archived Track B source package and current endpoint audit
- Status note: not reconstructed in this checkpoint

## Disproved routes

### N1-DIS-001

- Result label: **disproved route**
- Claim rejected: prime powers of one prime are independent coordinates
- Location: `FACTORIAL_DIVISOR_ATLAS.md`

### N1-DIS-002

- Result label: **disproved route**
- Claim rejected: a fixed pool of `O((log n)^2)` binary or ternary divisor choices can cover the half-range with quasipolynomial correction
- Location: `proofs/COUNTING_CAPACITY_OBSTRUCTION.md`

### N1-DIS-003

- Result label: **disproved route**
- Claim rejected: polynomial-size menus in `O((log n)^2)` layers can cover the half-range with polynomial correction
- Location: `proofs/MENU_ENTROPY_REQUIREMENT.md`

### N1-DIS-004

- Result label: **disproved route**
- Claim rejected: complement pairing by itself implies additive density
- Location: `proofs/COMPLEMENT_PAIRING_LEMMA.md`

## Promotion rule

No conditional theorem becomes a proved theorem until every named dependency is proved and an independent reconstruction is recorded. No finite certificate or computational evidence is promoted to an asymptotic theorem.