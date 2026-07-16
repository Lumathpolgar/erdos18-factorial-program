# Nova 3 Theorem Registry

## Registry rule

Every entry has one research result class. Symbolic proof, conditional implication, finite certificate, computational evidence, and disproved inference remain separate.

The factorial half-range theorem and Erdős Problem 18 remain open.

## Product and logarithmic divisor model

### N3-ANA-004, exact exponent product and exponential tilt

- Class: `proved theorem`
- Conclusion: exact independent factorial-prime exponent model, moments, factorized tilt, and unique saddle parameter for every interior logarithmic target
- Proof: `proofs/PRODUCT_MODEL_THEOREMS.md`

### N3-ANA-005, logarithmic local-count ceiling

- Class: `proved theorem`
- Conclusion:
  \[
  L_n(u,\Delta)
  \le
  \tau(n!)
  \frac{\lfloor\Delta/\log q\rfloor+1}{v_q(n!)+1}
  \]
- Proof: `proofs/PRODUCT_MODEL_THEOREMS.md`

### N3-ANA-006, non-Gaussian full-model limit

- Class: `proved theorem`
- Conclusion: the centered uniform log-divisor model divided by `n` converges to a non-Gaussian infinite convolution
- Proof: `proofs/PRODUCT_MODEL_THEOREMS.md`

### N3-ANA-007, unrestricted logarithmic minor-arc obstruction

- Class: `disproved estimate`
- Conclusion:
  \[
  \limsup_{|t|\to\infty}|\phi_n(t)|=1
  \]
  for every fixed `n>=3`
- Proof: `proofs/PRODUCT_MODEL_THEOREMS.md`

### N3-ANA-008, zero-tilt high-prime CLT

- Class: `proved theorem`
- Conclusion: after a growing low-prime cutoff, the high-prime logarithmic tail is asymptotically Gaussian and its largest coordinate is negligible relative to its standard deviation
- Proof: `proofs/PRODUCT_MODEL_THEOREMS.md`

### N3-ANA-009, coarse high-prime window positivity

- Class: `conditional theorem`
- Dependency: Berry-Esseen `N3-SRC-003`
- Conclusion: central windows wider than a constant multiple of the largest coordinate have mass comparable to width divided by standard deviation
- Proof: `proofs/PRODUCT_MODEL_THEOREMS.md`

## Explicit prime interval and old-address capacity

### N3-ANA-010, explicit upper-half prime interval

- Class: `proved theorem`
- Hypothesis: integer `n>=120368`
- Conclusion:
  \[
  \pi(n)-\pi(n/2)\ge\frac{n}{3\log n}
  \]
- Dependency: Dusart `N3-SRC-008`
- Proof: `proofs/EXPLICIT_PRIME_INTERVAL_AND_CAPACITY.md`

### N3-ANA-011, old-address formal capacity

- Class: `proved theorem`
- Status: `PROVED_BUT_STRUCTURAL_MODEL_SUPERSEDED`
- Conclusion: the old Nova 1 address model had enough formal menu capacity for `n>=120368`
- Boundary: Nova 2 later disproved its additive route by a lattice obstruction
- Proof: `proofs/EXPLICIT_PRIME_INTERVAL_AND_CAPACITY.md`

## Compact-tilt top-prime logarithmic model

### N3-ANA-012, compact-tilt Gaussian coarse windows

- Class: `proved theorem`
- Exact family: subset products of primes in `(n/2,n]`
- Hypotheses: fixed `|theta|<=theta_0<1`, fixed central displacement, `n>=120368`
- Conclusions: explicit variance lower bound, Berry-Esseen bound, and positive logarithmic-window mass for `Delta>=K_A log n`
- Proof: `proofs/COMPACT_TILT_TOP_PRIME_BAND.md`

### N3-ANA-013, unit-tilt freezing

- Class: `disproved estimate`
- Conclusion:
  \[
  T_{n,1}/B_{n,1}\to0
  \]
  in probability, with the symmetric statement at `theta=-1`
- Proof: `proofs/COMPACT_TILT_TOP_PRIME_BAND.md`

## Repaired marker-three capacity

### N3-ANA-014, repaired menu lower bound

- Class: `proved theorem`
- Conclusion for every `n>=120368` and `1<=t<=M_n`:
  \[
  M_n-1\le v_2(n!),
  \]
  \[
  |U_t^{(3)}(n)|
  \ge2^{h_n-1}
  \ge2^{n/(3\log n)-1}
  \]
- Key repair:
  \[
  n!/H_n\ge\lfloor n/2\rfloor!
  \]
- Proof: `proofs/MARKER_THREE_REPAIRED_CAPACITY_AUDIT.md`

### N3-ANA-015, repaired formal profile capacity

- Class: `proved theorem`
- Conclusion:
  \[
  2^{r_n}
  \prod_{t=1}^{M_n}(|U_t^{(3)}(n)|+1)
  \ge X_n+1
  \]
  for every `n>=120368`
- Boundary: formal capacity only
- Proof: `proofs/MARKER_THREE_REPAIRED_CAPACITY_AUDIT.md`

### N3-ANA-016, central-binomial shortcut obstruction

- Class: `disproved estimate`
- Disproved claim: every prime in `(n/2,n]` divides `binom(n,floor(n/2))`
- Counterexample family: `n=2p-1`, `p` prime, with
  \[
  v_p\binom{2p-1}{p-1}=0
  \]
- Proof: `proofs/MARKER_THREE_REPAIRED_CAPACITY_AUDIT.md`

## Marker-three numerical additive law

### N3-ANA-017, active contract compatibility

- Class: `proved theorem`
- Current Nova 1 inspected head: `1b81ec74f907d57d520bcf6c51f2e6e71f0474a7`
- Current Nova 2 inspected head: `e443674f86b2ee3c7037ac94ee47f6b8a4b3b29f`
- Conclusion: later structural, endpoint, carrier, streaming, and collision commits preserve the exact marker-three numerical labels
- Proofs: `proofs/MARKER_THREE_NUMERICAL_LAW_FOUNDATIONS.md`, `proofs/POST_PREFIX_TILT_AND_COLLISION.md`, `proofs/PARITY_TWIN_AND_ODD_REDUCTION.md`

### N3-ANA-018, tilt existence, span, and exact resonance set

- Class: `proved theorem`
- Mean map: continuous and strictly increasing from zero to the sum of layer maxima
- For every `W_n<q<=Y_n`, a unique finite tilt centers the mean at `q-W_n/2`
- Exact additive span: one
- Exact modulus-one resonance set on `[-pi,pi]`: `{0}`
- Proof: `proofs/MARKER_THREE_NUMERICAL_LAW_FOUNDATIONS.md`

### N3-ANA-019, endpoint-uniform minor-arc obstruction

- Class: `disproved estimate`
- Conclusion:
  \[
  \sup_{\lambda\in\mathbb R}
  |\Phi_{n,\lambda}(\theta)|=1
  \]
  for every fixed torus frequency
- Mechanism: freezing at zero and at the layer maxima
- Proof: `proofs/MARKER_THREE_NUMERICAL_LAW_FOUNDATIONS.md`

### N3-ANA-020, post-prefix tilt compression

- Class: `proved theorem`
- Deterministic prefix endpoint:
  \[
  P_n=m_n(2^{M_n}-1)+W_n
  \]
- Exact analytic range:
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
- Proof: `proofs/POST_PREFIX_TILT_AND_COLLISION.md`

### N3-ANA-021, binary-anchor coefficient collapse

- Class: `disproved estimate`
- Disproved inference: shrinking numerical tilt supplies a fixed lower bound for the zero-versus-minimum-state phase coefficient
- At zero tilt:
  \[
  P_0(Z_t=0)P_0(Z_t=2^{t-1})
  <2^{-2(h_n-1)}
  \]
- Consequence: the two-state bound from N3-ANA-018 cannot close the minor arc
- Proof: `proofs/POST_PREFIX_TILT_AND_COLLISION.md`

### N3-ANA-022, collision-aware tilted atom formula

- Class: `proved theorem`
- For exact profile multiplicity `C_n(s)`:
  \[
  P_\lambda(T=s)
  =
  \frac{C_n(s)e^{\lambda s}}
  {\prod_tZ_t(\lambda)}
  \]
- Nova 1 input:
  \[
  C_n(4^{\lfloor M_n/2\rfloor}-1)
  \ge2^{\lfloor M_n/2\rfloor}
  \]
- Consequence: every local reference law must retain or control numerical fiber multiplicity
- Proof: `proofs/POST_PREFIX_TILT_AND_COLLISION.md`

### N3-ANA-023, parity twin near-resonance

- Class: `disproved estimate with exact replacement identity`
- Put
  \[
  \varepsilon_n
  =
  \frac{8M_n\log L_n}{2^{M_n}-1}.
  \]
- Uniform first-layer zero-state bound:
  \[
  p^{(0)}_{n,q}
  \le
  \frac{2e^{\varepsilon_n}}{m_n+1}.
  \]
- Exact parity law:
  \[
  P(T\text{ even})=p^{(0)}_{n,q}.
  \]
- Exact nonzero-frequency value:
  \[
  \Phi(\pi)=2p^{(0)}-1.
  \]
- Uniform consequence:
  \[
  |\Phi(\pi)|
  \ge
  1-\frac{4e^{\varepsilon_n}}{m_n+1}
  \to1.
  \]
- Exact twin identity:
  \[
  \Phi(\pi+u)+\Phi(u)
  =
  2p^{(0)}\prod_{t=2}^{M_n}\phi_t(u).
  \]
- Consequence: an unnormalized minor arc containing `pi` cannot have a fixed aggregate-dispersion gap
- Proof: `proofs/PARITY_TWIN_AND_ODD_REDUCTION.md`

### N3-ANA-024, parity mismatch obstruction for reference laws

- Class: `proved obstruction`
- For every integer-valued reference law `G`:
  \[
  d_{TV}(\mathcal L(T),G)
  \ge
  |G(2\mathbb Z)-p^{(0)}|.
  \]
- Consequence: a reference law with fixed positive even mass cannot approximate the post-prefix law in total variation
- Boundary: this does not itself disprove a window-specific weighted Fourier inequality
- Proof: `proofs/PARITY_TWIN_AND_ODD_REDUCTION.md`

### N3-ANA-025, exact odd-lattice normalization

- Class: `proved theorem`
- Conditional transformation:
  \[
  \widetilde Z_1=(Z_1-1)/2
  \quad\text{given }Z_1\ne0,
  \qquad
  \widetilde Z_t=Z_t/2\quad(t>=2).
  \]
- Exact transformed sum:
  \[
  \widetilde T=(T-1)/2
  \quad\text{given }T\text{ odd}.
  \]
- The transformed coordinates remain independent and have common tilt `2 lambda`
- The transformed first support contains `0` and `1`, so the transformed law has exact span one
- Exact transformed window:
  \[
  J_{n,q}
  =
  \left[
  \left\lceil\frac{q-W_n-1}{2}\right\rceil,
  \left\lfloor\frac{q-1}{2}\right\rfloor
  \right]\cap\mathbb Z.
  \]
- Positivity transfer:
  \[
  P_\lambda(T\in I_{n,q})
  \ge
  (1-p^{(0)})
  P_{2\lambda}(\widetilde T\in J_{n,q}).
  \]
- Proof: `proofs/PARITY_TWIN_AND_ODD_REDUCTION.md`

## Transformed dyadic resonance ladder

### N3-ANA-026, exact dyadic finite-prefix factorization

- Class: `proved theorem`
- For
  \[
  \theta_j=\frac{\pi}{2^{j-1}},
  \qquad1\le j\le M_n-1,
  \]
  the matching layer satisfies
  \[
  \widetilde\phi_{j+1}(\theta_j)
  =2p_{j+1}^{(0)}-1,
  \]
  every layer `t>=j+2` satisfies
  \[
  \widetilde\phi_t(\theta_j)=1,
  \]
  and
  \[
  \widetilde\Phi(\theta_j)
  =
  \left(\prod_{t=1}^{j}\widetilde\phi_t(\theta_j)\right)
  (2p_{j+1}^{(0)}-1).
  \]
- Exact global conclusion: there is no nonzero dyadic modulus-one resonance because the first transformed support contains `0` and `1`
- Structural conclusion: every nonzero dyadic frequency has an exact tail resonance
- Proof: `proofs/TRANSFORMED_DYADIC_RESONANCE_LADDER.md`

### N3-ANA-027, matching-layer near-pure sign and tail collapse

- Class: `proved theorem and disproved route estimate`
- Define
  \[
  J_n
  =
  \min\left(
  M_n-1,
  \left\lfloor
  1+\log_2
  \frac{2^{M_n}-1}{16M_n\log L_n}
  \right\rfloor
  \right).
  \]
- Then
  \[
  J_n=M_n-O(\log\log n).
  \]
- Uniformly for `1<=j<=J_n`:
  \[
  p_{j+1}^{(0)}\le\frac{2e}{m_n+1},
  \]
  \[
  |\widetilde\phi_{j+1}(\theta_j)|
  \ge1-\frac{4e}{m_n+1},
  \]
  and
  \[
  \sum_{t=j+1}^{M_n}
  \widetilde{\mathcal D}_t(\theta_j)
  \le\frac{4e}{m_n+1}.
  \]
- Disproved mechanism: a fixed positive proportion of all transformed tail layers contributes fixed phase dispersion at every nonzero minor-arc frequency
- Boundary: full-product decay may still come from the first `j` transformed coordinates
- Proof: `proofs/TRANSFORMED_DYADIC_RESONANCE_LADDER.md`

### N3-ANA-028, transformed-window dyadic kernel classification

- Class: `proved theorem`
- Let
  \[
  N_{n,q}=|J_{n,q}|.
  \]
- Exact valuation:
  \[
  v_2(N_{n,q})\in\{0,1\}.
  \]
- More precisely, `v_2(N_{n,q})=1` exactly when `rho_n` and `q` are both even; otherwise `N_{n,q}` is odd
- At a reduced dyadic frequency `2pi a/2^d`, the transformed interval kernel vanishes exactly when `2^d|N_{n,q}`
- Consequence: it never vanishes at reduced dyadic frequencies with denominator at least `4`; at `pi` it vanishes only in the even-even case
- Boundary: nonvanishing at isolated points is not itself an integral obstruction
- Proof: `proofs/TRANSFORMED_DYADIC_RESONANCE_LADDER.md`

## Finite certificates

### N3-FIN-001

- Exact factorial-divisor checks for every `2<=n<=12`
- Verifier: `proofs/scale_sanity.py`

### N3-FIN-002

- Exact explicit-threshold checks for every `120368<=n<=1000000`
- Verifier: `proofs/prime_interval_capacity_sanity.py`

### N3-FIN-003

- Exact small top-prime tilt grid
- Verifier: `proofs/compact_tilt_sanity.py`

### N3-FIN-004

- Exact repaired capacity threshold audit at `n=120368`
- Verifier: `proofs/marker_three_capacity_sanity.py`

### N3-FIN-005

- Exact marker-three support and span checks for `n in {12,15}`
- Verifier: `proofs/marker_three_numerical_law_sanity.py`

### N3-FIN-006

- Exact threshold and collision checks for the post-prefix tilt theorem
- Verifier: `proofs/post_prefix_tilt_sanity.py`

### N3-FIN-007

- Exact small support construction for `n in {12,15}`
- Checks: parity structure, `pi` identity, parity-twin identity, transformed coordinate law, and transformed interval map
- Verifier: `proofs/parity_twin_sanity.py`

### N3-FIN-008

- Exact transformed dyadic checks for `n in {12,15}`
- Checks: matching-layer factor, exact later-layer invisibility, finite-prefix product identity, transformed window length, and dyadic kernel-zero criterion
- Verifier: `proofs/transformed_dyadic_sanity.py`

## Computational evidence

- `N3-COMP-001`: full logarithmic model scales
- `N3-COMP-002`: compact top-prime tilt scales
- `N3-COMP-003`: repaired capacity margins
- `N3-COMP-004`: small numerical marker-three tilt grids
- `N3-COMP-005`: post-prefix tilt scales
- `N3-COMP-006`: parity-zero ceiling and `pi` modulus floors at selected large `n`
- `N3-COMP-007`: dyadic safe-depth, matching-layer modulus, tail-dispersion, and transformed-window valuation rows for `n in {120368,200000,500000,1000000}`

## Open candidate contracts

### N3-CAND-LDC-001

Fine exact-factorial logarithmic lower windows remain open below current coarse scales.

### N3-CAND-LLT-001

Compact-tilt coarse logarithmic windows are proved for the top-prime band. Fine windows and the full bounded-exponent model remain open.

### N3-CAND-CF-001

The unnormalized numerical law has a forced parity twin at `pi`. The normalized law has an exact dyadic finite-prefix skeleton. The active candidate is a prefix-residue or prefix-characteristic theorem in neighborhoods of the dyadic ladder frequencies, matched to the transformed window kernel and a collision-aware reference law.

## Promotion rule

N3-ANA-023 rejects a zero-only major-arc partition for the unnormalized law. N3-ANA-025 supplies the exact parity normalization. N3-ANA-026 through N3-ANA-028 reject a many-tail-layers dispersion mechanism at the transformed dyadic ladder and freeze the exact kernel cancellation pattern.

None of N3-ANA-014 through N3-ANA-028 proves transformed local-window positivity, the strict weighted Fourier inequality, quotient occupancy, the factorial half-range theorem, or `INT-002`.