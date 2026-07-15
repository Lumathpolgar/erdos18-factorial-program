# Nova 3 Theorem Registry

## Registry rule

Every entry has one research result class. Finite computation, asymptotic proof, conditional implication, and disproved inference remain separate.

## Product and logarithmic divisor model

### N3-ANA-004, exact exponent product and exponential tilt

- Class: `proved theorem`
- Status: `PROVED`
- Conclusion: exact independent exponent model, moments, factorized tilt, and unique saddle parameter for every interior logarithmic target
- Proof: `proofs/PRODUCT_MODEL_THEOREMS.md`

### N3-ANA-005, logarithmic local-count ceiling

- Class: `proved theorem`
- Status: `PROVED`
- Conclusion:
  \[
  L_n(u,\Delta)
  \le
  \tau(n!)\frac{\lfloor\Delta/\log q\rfloor+1}{v_q(n!)+1}
  \]
- Proof: `proofs/PRODUCT_MODEL_THEOREMS.md`

### N3-ANA-006, non-Gaussian full-model limit

- Class: `proved theorem`
- Status: `PROVED`
- Conclusion: the centered uniform log-divisor model divided by `n` converges to a non-Gaussian infinite convolution
- Proof: `proofs/PRODUCT_MODEL_THEOREMS.md`

### N3-ANA-007, unrestricted minor-arc obstruction

- Class: `disproved estimate`
- Status: `DISPROVED`
- Conclusion:
  \[
  \limsup_{|t|\to\infty}|\phi_n(t)|=1
  \]
  for every fixed `n>=3`
- Proof: `proofs/PRODUCT_MODEL_THEOREMS.md`

### N3-ANA-008, zero-tilt high-prime CLT

- Class: `proved theorem`
- Status: `PROVED`
- Conclusion: after a growing low-prime cutoff, the high-prime logarithmic tail is asymptotically Gaussian and its largest coordinate is negligible relative to its standard deviation
- Proof: `proofs/PRODUCT_MODEL_THEOREMS.md`

### N3-ANA-009, coarse high-prime window positivity

- Class: `conditional theorem`
- Status: `CONDITIONAL`
- Dependency: Berry-Esseen N3-SRC-003
- Conclusion: central windows with width at least a constant multiple of the largest coordinate span have mass `>>Delta/B`
- Proof: `proofs/PRODUCT_MODEL_THEOREMS.md`

## Explicit prime interval and old-address capacity

### N3-ANA-010, explicit upper-half prime interval

- Class: `proved theorem`
- Status: `PROVED`
- Hypothesis: integer `n>=120368`
- Conclusion:
  \[
  \pi(n)-\pi(n/2)\ge\frac{n}{3\log n}
  \]
- Dependency: Dusart N3-SRC-008
- Proof: `proofs/EXPLICIT_PRIME_INTERVAL_AND_CAPACITY.md`

### N3-ANA-011, old-address formal capacity

- Class: `proved theorem`
- Status: `PROVED_BUT_STRUCTURAL_MODEL_SUPERSEDED`
- Conclusion: the old Nova 1 address system had sufficient formal menu capacity for `n>=120368`
- Boundary: Nova 2 later disproved its additive occupancy route by a lattice obstruction
- Proof: `proofs/EXPLICIT_PRIME_INTERVAL_AND_CAPACITY.md`

## Compact-tilt top-prime logarithmic model

### N3-ANA-012, compact-tilt Gaussian coarse windows

- Class: `proved theorem`
- Status: `PROVED`
- Exact family: subset products of primes in `(n/2,n]`
- Hypotheses: fixed `|theta|<=theta_0<1`, fixed central displacement constant, `n>=120368`
- Conclusions: explicit variance lower bound, Berry-Esseen bound, and positive logarithmic-window mass for `Delta>=K_A log n`
- Proof: `proofs/COMPACT_TILT_TOP_PRIME_BAND.md`

### N3-ANA-013, unit-tilt freezing

- Class: `disproved estimate`
- Status: `DISPROVED`
- Conclusion:
  \[
  T_{n,1}/B_{n,1}\to0
  \]
  in probability, with the symmetric statement at `theta=-1`
- Proof: `proofs/COMPACT_TILT_TOP_PRIME_BAND.md`

## Repaired marker-three capacity

### N3-ANA-014, repaired menu lower bound

- Class: `proved theorem`
- Status: `PROVED`
- Imported request: Nova 1 `N1-HO-N3-002`, commit `9febe46f2298d2726eeffa139676136963790019`
- Conclusions:
  \[
  M_n-1\le v_2(n!),
  \]
  \[
  |U_t^{(3)}(n)|\ge2^{h_n-1}
  \ge2^{n/(3\log n)-1}
  \]
  for all `n>=120368` and `1<=t<=M_n`
- Key repair:
  \[
  n!/H_n\ge\lfloor n/2\rfloor!
  \]
- Proof: `proofs/MARKER_THREE_REPAIRED_CAPACITY_AUDIT.md`

### N3-ANA-015, repaired formal profile capacity

- Class: `proved theorem`
- Status: `PROVED`
- Conclusion:
  \[
  2^{r_n}\prod_{t=1}^{M_n}(|U_t^{(3)}(n)|+1)
  \ge X_n+1
  \]
  for every `n>=120368`
- Claim boundary: formal capacity only
- Proof: `proofs/MARKER_THREE_REPAIRED_CAPACITY_AUDIT.md`

### N3-ANA-016, central-binomial shortcut obstruction

- Class: `disproved estimate`
- Status: `DISPROVED`
- Disproved claim: every prime in `(n/2,n]` divides `binom(n,floor(n/2))`
- Counterexample family: `n=2p-1`, `p` prime, for which
  \[
  v_p\binom{2p-1}{p-1}=0
  \]
- Proof: `proofs/MARKER_THREE_REPAIRED_CAPACITY_AUDIT.md`

## Marker-three numerical additive law

### N3-ANA-017, active contract compatibility

- Class: `proved theorem`
- Status: `PROVED`
- Current Nova 2 source: branch `nova/additive-occupancy`, commit `82603c631a106c3bff4676bdeeb9cc791fc98f3c`
- Structural source: Nova 1 marker-three construction at `ebb47ba436af554366d0f285119a769f31f9e561`
- Latest compatible Nova 1 head inspected: `e3a0e3f5fb335b23afdd9e1fe418ac46ca1c766a`
- Conclusion: later Nova 1 endpoint, carrier-block, and carry-collision commits preserve the numerical label definitions
- Proofs: `proofs/MARKER_THREE_NUMERICAL_LAW_FOUNDATIONS.md` and `proofs/POST_PREFIX_TILT_AND_COLLISION.md`

### N3-ANA-018, tilt existence, span, and exact resonance set

- Class: `proved theorem`
- Status: `PROVED`
- Numerical law:
  \[
  P_\lambda(Z_t=b)
  =
  \frac{e^{\lambda b}}
  {1+\sum_{a\in B_t(n)}e^{\lambda a}}
  \]
- Mean map: continuous and strictly increasing from zero to the sum of layer maxima
- Target conclusion: for every
  \[
  W_n<q\le Y_n,
  \]
  there is a unique finite tilt centered at
  \[
  q-W_n/2\in[q-W_n,q]
  \]
- Lattice conclusion: exact additive span one
- Resonance conclusion: on `[-pi,pi]`, the only exact modulus-one point is `theta=0`
- Global bound:
  \[
  |\Phi_{n,\lambda}(\theta)|
  \le
  \exp\left(-2p_0(\lambda)p_1(\lambda)\sin^2(\theta/2)\right)
  \]
- Proof: `proofs/MARKER_THREE_NUMERICAL_LAW_FOUNDATIONS.md`

### N3-ANA-019, endpoint-uniform minor-arc obstruction

- Class: `disproved estimate`
- Status: `DISPROVED`
- Disproved estimate: a fixed `rho<1` minor-arc modulus bound uniform over all finite tilts
- Conclusion:
  \[
  \sup_{\lambda\in\mathbb R}
  |\Phi_{n,\lambda}(\theta)|=1
  \]
  for every fixed torus frequency
- Mechanism: the law freezes at zero as `lambda->-infinity` and at layer maxima as `lambda->+infinity`
- Consequence: the final analytic bulk must provide compact tilt or direct phase-dispersion bounds
- Proof: `proofs/MARKER_THREE_NUMERICAL_LAW_FOUNDATIONS.md`

### N3-ANA-020, post-prefix tilt compression

- Class: `proved theorem`
- Status: `PROVED`
- Deterministic prefix endpoint:
  \[
  P_n=m_n(2^{M_n}-1)+W_n
  \]
- Exact analytic target range:
  \[
  P_n+1\le q\le Y_n
  \]
- Conclusion:
  \[
  -\frac{8M_n\log L_n}{L_n}
  <\lambda_{n,q}<
  \frac{16(n\log n+\log14)}{2^{M_n}},
  \qquad
  L_n=m_n(2^{M_n}-1)
  \]
- Uniform consequence:
  \[
  \sup_{P_n<q\le Y_n}|\lambda_{n,q}|\to0
  \]
- Dependencies: N1-STR-020, N1-DIS-006, N2-ADD-120, N3-ANA-018
- Proof: `proofs/POST_PREFIX_TILT_AND_COLLISION.md`

### N3-ANA-021, binary-anchor coefficient collapse

- Class: `disproved estimate`
- Status: `DISPROVED`
- Disproved inference: compact numerical tilt, or even tilt tending to zero, automatically supplies a fixed lower bound for the zero-versus-minimum-state minor-arc coefficient
- At zero tilt:
  \[
  P_0(Z_t=0)P_0(Z_t=2^{t-1})
  <2^{-2(h_n-1)}
  \le2^{-2(n/(3\log n)-1)}
  \]
- Consequence: the exact two-state bound in N3-ANA-018 cannot close the minor arc without aggregate phase dispersion
- Proof: `proofs/POST_PREFIX_TILT_AND_COLLISION.md`

### N3-ANA-022, collision-aware tilted atom formula

- Class: `proved theorem`
- Status: `PROVED`
- For exact profile multiplicity `C_n(s)`:
  \[
  P_\lambda(T_{n,\lambda}=s)
  =
  \frac{C_n(s)e^{\lambda s}}
  {\prod_tZ_t(\lambda)}
  \]
- Nova 1 collision input: for
  \[
  J_n=\lfloor M_n/2\rfloor,
  \qquad S_n=4^{J_n}-1,
  \]
  one has
  \[
  C_n(S_n)\ge2^{J_n}
  \]
- Consequence: every local approximation must account for numerical fiber multiplicity
- Dependency: Nova 1 `N1-COL-001` at commit `e3a0e3f5fb335b23afdd9e1fe418ac46ca1c766a`
- Proof: `proofs/POST_PREFIX_TILT_AND_COLLISION.md`

## Finite certificates

### N3-FIN-001

- Exact range: every `2<=n<=12`
- Verifier: `proofs/scale_sanity.py`

### N3-FIN-002

- Exact range: every `120368<=n<=1000000`
- Content: explicit prime interval and old-address threshold checks
- Verifier: `proofs/prime_interval_capacity_sanity.py`

### N3-FIN-003

- Exact small top-prime tilt grid
- Verifier: `proofs/compact_tilt_sanity.py`

### N3-FIN-004

- Exact threshold: `n=120368`
- Content: repaired cutoff, address legality, formal capacity, and central-binomial regression
- Verifier: `proofs/marker_three_capacity_sanity.py`

### N3-FIN-005

- Exact supports: `n in {12,15}`
- Content: marker-three support span, endpoint crossing, and finite support construction
- Numerical evidence: tilt centering and sampled torus resonance checks
- Verifier: `proofs/marker_three_numerical_law_sanity.py`

### N3-FIN-006

- Exact threshold: `n=120368`
- Content: nonempty post-prefix range, largest minimum-state legality, lower-bound algebra, and exact carry-collision enumeration for four layer pairs
- Observed minimal-support collision multiplicity at target `255`: `34`, exceeding the required `16`
- Verifier: `proofs/post_prefix_tilt_sanity.py`

## Computational evidence

### N3-COMP-001

Full-model scale tables from `proofs/scale_sanity.py`.

### N3-COMP-002

Compact-tilt scale tables from `proofs/compact_tilt_sanity.py`.

### N3-COMP-003

Repaired marker-three capacity margins through selected `n<=1000000` from `proofs/marker_three_capacity_sanity.py`.

### N3-COMP-004

Small marker-three numerical-law tilt and characteristic-function grids from `proofs/marker_three_numerical_law_sanity.py`.

### N3-COMP-005

Post-prefix tilt bound scales at selected `n in {120368,200000,500000,1000000}` from `proofs/post_prefix_tilt_sanity.py`.

At `n=120368`, the logarithmic magnitudes satisfy approximately

\[
\log_{10}\Lambda_n^-<-656.90,
\qquad
\log_{10}\Lambda_n^+<-651.90.
\]

## Open candidate contracts

### N3-CAND-LDC-001

Fine exact-factorial logarithmic lower windows remain open below current coarse scales.

### N3-CAND-LLT-001

Compact-tilt coarse logarithmic windows are proved for the top-prime band. Fine windows and the full bounded-exponent model remain open.

### N3-CAND-CF-001

For the numerical marker-three law, the exact span, exact resonance set, active post-prefix target range, and uniform shrinking tilt are now known. The single binary anchor is quantitatively insufficient. The open node is an aggregate phase-dispersion theorem for the complete odd-core menus with collision-aware atoms.

## Promotion rule

N3-ANA-020 closes the compact-tilt clause on the exact post-prefix target range. N3-ANA-021 prevents promotion of the existing two-state minor-arc bound. N3-ANA-022 freezes how profile collisions enter numerical atoms. None of N3-ANA-014 through N3-ANA-022 proves the strict weighted Fourier inequality, quotient occupancy, the factorial half-range theorem, or `INT-002`.