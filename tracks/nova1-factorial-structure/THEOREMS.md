# Nova 1 Theorem Registry

## Frozen proved results

### N1-STR-003: Factorial valuation budget

- Result label: **proved theorem**
- Hypotheses: integer `n>=1`, prime `p<=n`
- Conclusion: Legendre formula, digit-sum formula, quotient bands, dyadic bands, and `Theta((log n)^2)` available 2-adic marker exponents for large `n`
- Constants effective: yes in the exact formulas; asymptotic threshold not optimized
- Proof: `proofs/VALUATION_BUDGET_LEMMAS.md`

### N1-STR-004: Valuation-box uniqueness

- Result label: **proved theorem**
- Hypotheses: finite prime set `P`, allocations `0<=a_p<=v_p(n!)`
- Conclusion: exactly `product_p(a_p+1)` unique legal divisors
- Distinctness mechanism: unique factorization
- Proof: `FACTORIAL_DIVISOR_ATLAS.md`

### N1-STR-005: Valuation-budget partition

- Result label: **proved theorem**
- Hypotheses: nonnegative allocations summing to at most `v_p(n!)` at every prime
- Conclusion: every assembled product remains a divisor of `n!`
- Proof: `FACTORIAL_DIVISOR_ATLAS.md`

### N1-STR-006: Marker-signature distinctness

- Result label: **proved theorem**
- Hypotheses: pairwise distinct marker-prime signatures; cores avoid marker primes
- Conclusion: labeled divisors are numerically distinct
- Proof: `proofs/DISTINCTNESS_AND_CORRECTION.md`

### N1-STR-007: Complement pairing

- Result label: **proved theorem**
- Hypotheses: `Q=R^2|n!`, distinct `z_i|R`, `1<z_i<=X/R`
- Conclusion: `R/z_i` and `Rz_i` are legal, bounded, and pairwise distinct
- Proof: `proofs/COMPLEMENT_PAIRING_LEMMA.md`

### N1-COR-001: Binary correction palette

- Result label: **proved theorem**
- Hypotheses: `r-1<=v_2(n!)`
- Conclusion: every `0<=t<2^r` is a sum of at most `r` distinct powers of two dividing `n!`
- Boundary treatment: exact endpoints `0` and `2^r-1`
- Proof: `proofs/DISTINCTNESS_AND_CORRECTION.md`

### N1-RED-002: Downward-window correction

- Result label: **proved theorem**
- Hypotheses: main sums are downward `2^r-1` dense, legal, distinct, and palette-disjoint
- Conclusion: `H_{n!}(X_n+1)<=K(n)+r`
- Endpoint convention: exact frozen `H_N` convention
- Proof: `proofs/DISTINCTNESS_AND_CORRECTION.md`

### N1-OBS-002: Capacity obstruction

- Result label: **proved theorem**
- Hypotheses: finite attainable set downward `R`-dense on `[0,X]`
- Conclusion: `|S|(R+1)>=X+1`
- Proof: `proofs/COUNTING_CAPACITY_OBSTRUCTION.md`

### N1-STR-008: Menu entropy lower bound

- Result label: **proved theorem**
- Hypotheses: at most `A(log n)^2` layers and polynomial residual width
- Conclusion: geometric-mean layer-state count is at least `exp(n/(3A log n))` for all sufficiently large `n`
- Proof: `proofs/MENU_ENTROPY_REQUIREMENT.md`

### N1-STR-009: High-prime menu capacity

- Result label: **proved theorem**
- Hypotheses: admissible address in the stated factorial range
- Conclusion:
  \[
  |U_e(n)|\ge2^{\pi(n)-\pi(n/2)-1}-1
  \]
- Proof: `proofs/HIGH_PRIME_MENU_CAPACITY.md`

### N1-STR-014: Marker-three legality and distinctness

- Result label: **proved theorem**
- Hypotheses: `M_n-1<=v_2(n!)`; cores are odd and satisfy `3u|n!`
- Conclusion: every `3*2^(t-1)*u` is a legal divisor; different layers and the palette are numerically disjoint
- Distinctness mechanism: exact 2-adic valuation across layers and divisibility by `3` against the palette
- Proof: `proofs/MARKER_THREE_LATTICE_REPAIR.md`

### N1-STR-015: Exact support lattice and residues

- Result label: **proved theorem**
- Hypotheses: marker-three layers, `3<=X_n`, `r_n>=2`
- Conclusion: main support generates exactly `3Z`; palette subset sums attain every residue modulo `3`
- Proof: `proofs/MARKER_THREE_LATTICE_REPAIR.md`

### N1-RED-004: Quotient-window correction theorem

- Result label: **proved theorem**
- Hypotheses: every quotient target `q` has a rainbow sum in `[q-W_n,q]`
- Conclusion:
  \[
  H_{n!}(X_n+1)\le M_n+r_n
  \]
- Exact radius:
  \[
  W_n=\left\lfloor\frac{2^{r_n}-3}{3}\right\rfloor
  \]
- Boundary treatment: palette handles `q<=W_n`; quotient theorem handles the remaining range through `floor(X_n/3)`
- Proof: `proofs/MARKER_THREE_LATTICE_REPAIR.md`

### N1-STR-016: Odd-digit one-gap lemma

- Result label: **proved theorem**
- Hypotheses: odd `m>=3`, integer `L>=1`
- Conclusion: sums `sum 2^e a_e`, with `a_e in {0,1,3,...,m}`, have maximum downward gap at most one on `[0,m(2^L-1)]`
- Proof: `proofs/MARKER_THREE_LATTICE_REPAIR.md`

### N1-STR-017: Unconditional marker-three initial interval

- Result label: **proved theorem**
- Hypotheses: sufficiently large `n` so all odd `u<=m_n` occur in every layer and the scale cutoff holds
- Conclusion: every integer
  \[
  0\le x\le3m_n(2^{M_n}-1)+2
  \]
  is a sum of at most `M_n+r_n` distinct divisors of `n!`
- Range status: `exp(O((log n)^2))`, not the factorial half-range
- Proof: `proofs/MARKER_THREE_LATTICE_REPAIR.md`

### N1-STR-018: Repaired high-prime menu bound

- Result label: **proved theorem**
- Imported dependency: `N3-ANA-010` from branch `nova/analytic-density`, exact commit `e60069f797af878711e7a9d4abb1fb6188a1f724`
- Hypotheses: integer `n>=120368`, `1<=t<=M_n`
- Conclusion:
  \[
  |U_t(n)|\ge2^{\pi(n)-\pi(n/2)-1}
  \ge2^{n/(3\log n)-1}
  \]
- Legality mechanism: complementary subset products of primes in `(n/2,n]`, with the factor `3` reserved separately
- Cutoff proof: the upper-half prime product divides the central binomial coefficient and is at most `2^n`
- Proof: `proofs/MARKER_THREE_MENU_CAPACITY.md`

### N1-CAP-002: Explicit repaired profile-capacity gate

- Result label: **proved theorem**
- Hypotheses: integer `n>=120368`
- Conclusion:
  \[
  2^{r_n}\prod_{t=1}^{M_n}(|U_t(n)|+1)\ge X_n+1
  \]
- Constants effective: yes, threshold `120368`
- What is not claimed: profile injectivity, numerical occupancy, maximum-gap control
- Proof: `proofs/MARKER_THREE_MENU_CAPACITY.md`

## Frozen conditional results

### N1-RED-005: Marker-three half-range reduction

- Result label: **conditional theorem**
- Hypothesis: the exact quotient rainbow statement in `handoffs/TO_NOVA2.md`
- Conclusion:
  \[
  H_{n!}(\lfloor\sqrt{n!}\rfloor+1)
  \le
  \lceil16(\log n)^2\rceil+
  \lceil4\log n\rceil
  \]
  for all sufficiently large `n`
- Dependencies: `N1-STR-014`, `N1-STR-015`, `N1-COR-001`, `N1-RED-004`
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
- Status note: not reconstructed

## Computational evidence

### N1-CMP-003: Marker-three reduced quotient audit

- Result label: **computational evidence**
- Exact finite domain: every `7<=n<=14` with reduced legal parameters `r=3` and `M=min(6,v_2(n!)+1)`
- Conclusion: no quotient-window failure; maximum downward distance at most one; reconstructed full half-range exact
- Verifier: `verification/marker_three_sanity.py`
- Report: `verification/MARKER_THREE_FINITE_REPORT.md`
- What is not claimed: asymptotic occupancy

## Disproved routes

### N1-DIS-001

- Result label: **disproved route**
- Claim rejected: prime powers of one prime are independent coordinates
- Location: `FACTORIAL_DIVISOR_ATLAS.md`

### N1-DIS-002

- Result label: **disproved route**
- Claim rejected: a fixed pool of `O((log n)^2)` binary or ternary choices covers the half-range
- Location: `proofs/COUNTING_CAPACITY_OBSTRUCTION.md`

### N1-DIS-003

- Result label: **disproved route**
- Claim rejected: polynomial-size menus in `O((log n)^2)` layers cover the half-range with polynomial correction
- Location: `proofs/MENU_ENTROPY_REQUIREMENT.md`

### N1-DIS-004

- Result label: **disproved route**
- Claim rejected: complement pairing by itself implies additive density
- Location: `proofs/COMPLEMENT_PAIRING_LEMMA.md`

### N1-DIS-005: Original valuation-tagged lattice

- Result label: **disproved route**
- Claim rejected: the frozen `N1-CON-001` layers with addresses `e_t=r_n+t` satisfy the radius `2^r_n-1` occupancy request
- Countertheorem: `N2-ADD-115`
- Exact imported source: branch `nova/additive-occupancy`, commit `45c74a5fa747551422ffcad7d3ddf22788fbe622`
- Failure: the first requested window contains no multiple of the common main factor `2^(r_n+1)`

## Historical conditional artifact

### N1-RED-003

- Result label: **conditional theorem**
- Status: retired because its exact occupancy hypothesis was disproved
- Logical implication remains valid, but it has no surviving route to its false frozen hypothesis
- Replacement: `N1-RED-005`

## Promotion rule

No conditional theorem becomes a proved theorem until every named dependency is proved and independently reconstructed. No finite certificate or computational evidence is promoted to an asymptotic theorem.
