# Nova 1 Theorem Registry

## Frozen proved results

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
- Conclusion: allocated valuation budgets preserve legality
- Proof: `FACTORIAL_DIVISOR_ATLAS.md`

### N1-STR-006: Marker-signature distinctness

- Result label: **proved theorem**
- Conclusion: pairwise distinct marker signatures force numerical distinctness
- Proof: `proofs/DISTINCTNESS_AND_CORRECTION.md`

### N1-STR-007: Complement pairing

- Result label: **proved theorem**
- Conclusion: if `R^2|n!` and `z|R`, then `R/z` and `Rz` are legal; stated conditions give range and distinctness
- Proof: `proofs/COMPLEMENT_PAIRING_LEMMA.md`

### N1-COR-001: Binary correction palette

- Result label: **proved theorem**
- Conclusion: every `0<=t<2^r` has a unique subset representation using `{1,2,...,2^(r-1)}`
- Proof: `proofs/DISTINCTNESS_AND_CORRECTION.md`

### N1-RED-002: Downward-window correction

- Result label: **proved theorem**
- Conclusion: downward `2^r-1` main occupancy plus the binary palette yields exact local coverage
- Proof: `proofs/DISTINCTNESS_AND_CORRECTION.md`

### N1-OBS-002: Capacity obstruction

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

### N1-STR-014: Marker-three legality and distinctness

- Result label: **proved theorem**
- Conclusion: every `3*2^(t-1)*u` is legal; exact 2-adic valuations distinguish layers; divisibility by `3` separates the main family from the binary palette
- Proof: `proofs/MARKER_THREE_LATTICE_REPAIR.md`

### N1-STR-015: Exact support lattice and residues

- Result label: **proved theorem**
- Conclusion: the main support generates exactly `3Z`, while palette sums attain every residue modulo `3`
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

### N1-STR-017: Unconditional marker-three initial interval

- Result label: **proved theorem**
- Conclusion: every integer through `3m_n(2^M_n-1)+2` has a legal representation using at most `M_n+r_n` terms
- Range status: `exp(O((log n)^2))`, not the factorial half-range
- Proof: `proofs/MARKER_THREE_LATTICE_REPAIR.md`

### N1-STR-018: Repaired high-prime menu bound

- Result label: **proved theorem**
- Imported dependency: `N3-ANA-010` from branch `nova/analytic-density`, commit `e60069f797af878711e7a9d4abb1fb6188a1f724`
- Hypotheses: `n>=120368`, `1<=t<=M_n`
- Conclusion: `|U_t(n)|>=2^(pi(n)-pi(n/2)-1)>=2^(n/(3 log n)-1)`
- Proof: `proofs/MARKER_THREE_MENU_CAPACITY.md`

### N1-CAP-002: Explicit repaired profile-capacity gate

- Result label: **proved theorem**
- Hypotheses: `n>=120368`
- Conclusion: `2^r_n product_t(|U_t(n)|+1)>=X_n+1`
- What is not claimed: injectivity, occupancy, or maximum-gap control
- Proof: `proofs/MARKER_THREE_MENU_CAPACITY.md`

### N1-STR-019: Multiplicative 3-density of the reserved odd core

- Result label: **proved theorem**
- Hypotheses: integer `n>=6`
- Object: `D_n=n!/(3*2^v_2(n!))`
- Conclusion: every real `1<=z<=D_n` has a divisor `d|D_n` with `z/3<d<=z`
- Mechanism: prime-power extension lemma and `p<=3D_prefix`
- Proof: `proofs/QUOTIENT_ENDPOINT_SUPPORT.md`

### N1-STR-020: Quotient endpoint support

- Result label: **proved theorem**
- Hypotheses: integer `n>=12`
- Conclusion: there are distinct legal terms `b_t in B_t(n)` for `t=1,2,3` with `b_t>X_n/9`, hence
  \[
  b_1+b_2+b_3>X_n/3
  \]
  and the maximum quotient rainbow sum is at least `floor(X_n/3)+1`
- Boundary status: total support reaches beyond the final target
- What is not claimed: a sum in the downward endpoint window
- Proof: `proofs/QUOTIENT_ENDPOINT_SUPPORT.md`

### N1-RED-006: Coarse deterministic quotient contraction

- Result label: **proved theorem**
- Hypotheses: `n>=12`, `0<=q<=floor(X_n/3)`
- Conclusion: after `L` increasing quotient layers, a deterministic legal selection leaves residual
  \[
  \rho_L<\max\{(2/3)^Lq,2^L\}
  \]
- Limitation: this does not reach the polynomial-width radius `W_n`
- Proof: `proofs/QUOTIENT_ENDPOINT_SUPPORT.md`

## Frozen conditional results

### N1-RED-005: Marker-three half-range reduction

- Result label: **conditional theorem**
- Hypothesis: the exact quotient rainbow occupancy statement in `handoffs/TO_NOVA2.md`
- Conclusion:
  \[
  H_{n!}(\lfloor\sqrt{n!}\rfloor+1)
  \le
  \lceil16(\log n)^2\rceil+\lceil4\log n\rceil
  \]
- Dependencies: `N1-STR-014`, `N1-STR-015`, `N1-COR-001`, `N1-RED-004`
- Location: `PREFERRED_ROUTE.md`

### N1-RED-001: Track B reconstruction

- Result label: **conditional theorem** under reconstruction
- Goal:
  \[
  H_{n!}(\lfloor\sqrt{n!}\rfloor+1)=O((\log n)^2)
  \Longrightarrow h(n!)=O((\log n)^3)
  \]
- Dependency: archived Track B source package and current endpoint audit

## Computational evidence

### N1-CMP-003: Marker-three reduced quotient audit

- Result label: **computational evidence**
- Exact finite domain: every `7<=n<=14` under reduced legal parameters
- Conclusion: maximum downward quotient distance at most one
- Verifier: `verification/marker_three_sanity.py`
- Report: `verification/MARKER_THREE_FINITE_REPORT.md`

### N1-CMP-004: Endpoint support finite audit

- Result label: **finite certificate**
- Exact checks:
  - 3-density for every `6<=n<=20`;
  - endpoint crossing for every `12<=n<=20`;
  - exhaustive coarse contraction for all targets with `12<=n<=14` and `1<=L<=6`
- Verifier: `verification/endpoint_support_sanity.py`
- Report: `verification/ENDPOINT_SUPPORT_FINITE_REPORT.md`

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
- Claim rejected: the old addresses `e_t=r_n+t` satisfy the radius `2^r_n-1` occupancy request
- Countertheorem: Nova 2 `N2-ADD-115`
- Exact source: branch `nova/additive-occupancy`, commit `45c74a5fa747551422ffcad7d3ddf22788fbe622`

## Historical conditional artifact

### N1-RED-003

- Result label: **conditional theorem**
- Status: retired because its exact occupancy hypothesis was disproved
- Replacement: `N1-RED-005`

## Promotion rule

No conditional theorem becomes proved until every dependency is proved and independently reconstructed. No finite certificate or computational evidence is promoted to an asymptotic theorem.