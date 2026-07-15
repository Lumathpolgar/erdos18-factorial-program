# Nova 3 Theorem Registry

## Registry rule

Every entry has one research result class. Finite computation, asymptotic proof, conditional implication, and disproved inference remain separate.

## Exact factorial-divisor product model

### N3-ANA-004, exact exponent product and exponential tilt

- Result class: `proved theorem`
- Status: `PROVED`
- Hypotheses: integer `n>=2`; exact caps `0<=a_p<=v_p(n!)`
- Conclusion: divisor exponents are independent under the uniform measure; exact mean and variance hold; the exponential tilt factors; every interior logarithmic target has a unique saddle parameter
- Proof: `proofs/PRODUCT_MODEL_THEOREMS.md`

### N3-ANA-005, uniform logarithmic local-count ceiling

- Result class: `proved theorem`
- Status: `PROVED`
- Conclusion:
  \[
  L_n(u,\Delta)
  \le
  \tau(n!)\frac{\lfloor\Delta/\log q\rfloor+1}{v_q(n!)+1}
  \]
  for every prime `q<=n`, real `u`, and `Delta>=0`
- Proof: `proofs/PRODUCT_MODEL_THEOREMS.md`

### N3-ANA-006, non-Gaussian full-model limit

- Result class: `proved theorem`
- Status: `PROVED`
- Conclusion:
  \[
  \frac{\log d-\frac12\log(n!)}n
  \Rightarrow
  \sum_p(\log p)U_p,
  \]
  where the limit is a non-Gaussian infinite convolution
- Proof: `proofs/PRODUCT_MODEL_THEOREMS.md`

### N3-ANA-007, unrestricted minor-arc obstruction

- Result class: `disproved estimate`
- Status: `DISPROVED`
- Conclusion: for every fixed `n>=3`,
  \[
  \limsup_{|t|\to\infty}|\phi_n(t)|=1
  \]
- Proof: `proofs/PRODUCT_MODEL_THEOREMS.md`

### N3-ANA-008, zero-tilt high-prime central limit theorem

- Result class: `proved theorem`
- Status: `PROVED`
- Hypotheses: `y=y(n)->infinity` and `2y<=sqrt(n)`
- Conclusion:
  \[
  T_{n,y}/B_{n,y}\Rightarrow N(0,1),
  \]
  with
  \[
  B_{n,y}^2\gg n^2\frac{\log y}{y},
  \qquad
  M_{n,y}/B_{n,y}\to0
  \]
- Proof: `proofs/PRODUCT_MODEL_THEOREMS.md`

### N3-ANA-009, coarse high-prime window positivity

- Result class: `conditional theorem`
- Status: `CONDITIONAL`
- Dependency: accepted Berry-Esseen theorem N3-SRC-003
- Conclusion: central windows with `Delta>=K M_{n,y}` have probability `>>Delta/B_{n,y}`
- Proof: `proofs/PRODUCT_MODEL_THEOREMS.md`

## Explicit top-prime and capacity theorems

### N3-ANA-010, explicit upper-half prime interval

- Result class: `proved theorem`
- Status: `PROVED`
- Hypotheses: integer `n>=120368`
- Conclusion:
  \[
  \pi(n)-\pi(n/2)\ge\frac{n}{3\log n}
  \]
- Dependency: Dusart Theorem 6.9, N3-SRC-008
- Proof: `proofs/EXPLICIT_PRIME_INTERVAL_AND_CAPACITY.md`

### N3-ANA-011, superseded old-address capacity theorem

- Result class: `proved theorem`
- Status: `PROVED_BUT_STRUCTURAL_MODEL_SUPERSEDED`
- Imported model: Nova 1 old address system at commit `fa11f4b2cb86a2dd791df189ada12757be791804`
- Conclusion: the old menus had legal formal capacity for `n>=120368`
- Boundary: Nova 2 later disproved the old additive construction by a power-of-two lattice obstruction
- Proof: `proofs/EXPLICIT_PRIME_INTERVAL_AND_CAPACITY.md`

## Compact-tilt top-prime distribution

### N3-ANA-012, compact-tilt Gaussian coarse windows

- Result class: `proved theorem`
- Status: `PROVED`
- Exact family: subset products of primes in `(n/2,n]`
- Hypotheses: fixed `0<=theta_0<1`, fixed `A>=0`, `n>=120368`, and `|theta|<=theta_0`
- Variance:
  \[
  B_{n,\theta}^2\ge\frac1{48}n^{1-\theta_0}\log n
  \]
- Berry-Esseen:
  \[
  \sup_z\left|P_\theta(T/B\le z)-\Phi(z)\right|
  \le C_{BE}\sqrt{\frac{48\log n}{n^{1-\theta_0}}}
  \]
- Window conclusion: for `|x|<=AB` and `K_A log n<=Delta<=B`,
  \[
  P_\theta\{T\in[x,x+\Delta]\}
  \ge\frac{c_A}{2}\frac{\Delta}{B}
  \]
- Proof: `proofs/COMPACT_TILT_TOP_PRIME_BAND.md`

### N3-ANA-013, unit-tilt freezing

- Result class: `disproved estimate`
- Status: `DISPROVED`
- Disproved estimate: uniform Gaussian behavior on a fixed tilt range reaching `|theta|=1`
- Conclusion:
  \[
  T_{n,1}/B_{n,1}\to0
  \]
  in probability, with the same statement at `theta=-1`
- Proof: `proofs/COMPACT_TILT_TOP_PRIME_BAND.md`

## Repaired marker-three audit

### N3-ANA-014, repaired marker-three menu lower bound

- Result class: `proved theorem`
- Status: `PROVED`
- Imported request: Nova 1 `N1-HO-N3-002`, branch `nova/factorial-structure`, commit `9febe46f2298d2726eeffa139676136963790019`
- Hypotheses: integer `n>=120368`; `1<=t<=M_n`; repaired core menu
  \[
  U_t^{(3)}(n)=\{u\ge1:u\text{ odd},\ 3u\mid n!,\ 3\cdot2^{t-1}u\le X_n\}
  \]
- Conclusions:
  \[
  M_n-1\le v_2(n!),
  \]
  \[
  |U_t^{(3)}(n)|\ge2^{h_n-1}
  \ge2^{n/(3\log n)-1}
  \]
- Key repair:
  \[
  n!/H_n\ge\lfloor n/2\rfloor!
  \]
  replaces the invalid central-binomial divisibility shortcut
- Proof: `proofs/MARKER_THREE_REPAIRED_CAPACITY_AUDIT.md`

### N3-ANA-015, repaired marker-three profile capacity

- Result class: `proved theorem`
- Status: `PROVED`
- Hypotheses: those of N3-ANA-014
- Conclusion:
  \[
  2^{r_n}
  \prod_{t=1}^{M_n}(|U_t^{(3)}(n)|+1)
  \ge X_n+1
  \]
  for every `n>=120368`
- Claim boundary: formal profile capacity only
- Proof: `proofs/MARKER_THREE_REPAIRED_CAPACITY_AUDIT.md`

### N3-ANA-016, central-binomial shortcut obstruction

- Result class: `disproved estimate`
- Status: `DISPROVED`
- Disproved claim: every prime in `(n/2,n]` divides `binom(n,floor(n/2))`
- Counterexample family: `n=2p-1` with prime `p`; then
  \[
  v_p\binom{2p-1}{p-1}=0
  \]
- Consequence: Nova 1's requested statements remain true, but that proof step must be replaced
- Proof: `proofs/MARKER_THREE_REPAIRED_CAPACITY_AUDIT.md`

## Finite certificates

### N3-FIN-001

- Range: every `2<=n<=12`
- Checks: divisor uniqueness, exact moments, symmetry, and local ceiling
- Verifier: `proofs/scale_sanity.py`

### N3-FIN-002

- Range: every `120368<=n<=1000000`
- Checks: explicit prime interval, old address legality, and old formal capacity
- Verifier: `proofs/prime_interval_capacity_sanity.py`

### N3-FIN-003

- Range: listed small top-prime models and tilt grid
- Checks: exact tilted normalization, mean, variance, and third-moment ceiling
- Verifier: `proofs/compact_tilt_sanity.py`

### N3-FIN-004

- Exact threshold: `n=120368`
- Checks:
  - exact prime-band size `h_n=5254`;
  - exact repaired cutoff after squaring;
  - exact address slack `118171`;
  - exact profile-capacity bit margin `10575208`;
  - exact central-binomial counterexample family for tested primes
- Verifier: `proofs/marker_three_capacity_sanity.py`

## Computational evidence

### N3-COMP-001

- Selected `n<=10000`
- Content: full-model scale and effective-dimension tables
- Verifier: `proofs/scale_sanity.py`

### N3-COMP-002

- Selected `n<=1000000` and compact tilt grid
- Content: compact-tilt variance and Berry-Esseen scale tables
- Verifier: `proofs/compact_tilt_sanity.py`

### N3-COMP-003

- Selected `n in {120368,200000,500000,1000000}`
- Content: repaired prime-count, address, monotonic-cutoff, and capacity margins
- Verifier: `proofs/marker_three_capacity_sanity.py`
- What is not claimed: selected rows do not replace the symbolic monotonic proof

## Open candidate contracts

### N3-CAND-LDC-001

Fine exact-factorial logarithmic lower windows remain open below the current coarse scales.

### N3-CAND-LLT-001

Compact-tilt coarse windows are proved for the top-prime band. Fine windows and the full bounded-exponent high-prime model remain open.

### N3-CAND-CF-001

Unbounded decay is false. A matched bounded-frequency theorem remains open. Nova 2's future additive object is numerical and periodic on `[-pi,pi]`, not logarithmic.

## Promotion rule

N3-ANA-014 and N3-ANA-015 close the repaired Nova 1 capacity request only. They do not prove profile injectivity, quotient occupancy, numerical additive coverage, the factorial half-range theorem, or `INT-002`.