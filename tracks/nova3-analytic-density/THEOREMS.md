# Nova 3 Theorem Registry

## Label rule

Every entry carries exactly one research result class from the track contract. Repository evidence codes are included separately only when needed for integration.

## N3-ANA-004, exact factorial divisor product and tilt model

- Result class: `proved theorem`
- Repository status: `PROVED`
- Hypotheses: integer `n>=2`; exact exponent caps `0<=a_p<=v_p(n!)`
- Conclusion: uniform divisor exponents are independent; exact mean and variance formulas hold; the exponential tilt factors; every interior logarithmic target has a unique saddle parameter
- Constants: exact and effective
- Distinctness: unique factorization
- Boundaries: all finite `n>=2`; saddle parameter only for `0<u<log(n!)`
- Dependencies: none
- Proof: `proofs/PRODUCT_MODEL_THEOREMS.md`

## N3-ANA-005, local logarithmic divisor-count ceiling

- Result class: `proved theorem`
- Repository status: `PROVED`
- Hypotheses: integer `n>=2`, prime `q<=n`, real `u`, real `Delta>=0`
- Conclusion:
  \[
  L_n(u,\Delta)
  \le
  \tau(n!)\frac{\lfloor\Delta/\log q\rfloor+1}{v_q(n!)+1}.
  \]
- Constants: exact
- Uniformity: all `u`
- Distinctness: exact exponent-vector bijection
- Boundaries: closed window `[u,u+Delta]`
- Dependencies: N3-ANA-004
- Proof: `proofs/PRODUCT_MODEL_THEOREMS.md`

## N3-ANA-006, non-Gaussian full-model limit

- Result class: `proved theorem`
- Repository status: `PROVED`
- Hypotheses: uniformly selected divisor of `n!`; `n->infinity`
- Conclusion:
  \[
  \frac{\log d-\frac12\log(n!)}n
  \Rightarrow
  \sum_p(\log p)U_p,
  \]
  where the independent `U_p` are uniform on `[-1/(2(p-1)),1/(2(p-1))]`; the limit is not Gaussian
- Constants: exact limiting variance series
- Dependencies: N3-ANA-004
- Proof: `proofs/PRODUCT_MODEL_THEOREMS.md`

## N3-ANA-007, obstruction to unrestricted minor arcs

- Result class: `disproved estimate`
- Repository status: `DISPROVED`
- Hypotheses: fixed integer `n>=3`; characteristic function of centered uniform logarithmic divisor size
- Disproved estimate: existence of `T<infinity` and `rho<1` with `|phi_n(t)|<=rho` for every `|t|>=T`
- Exact conclusion:
  \[
  \limsup_{|t|\to\infty}|\phi_n(t)|=1.
  \]
- Dependencies: N3-ANA-004; Dirichlet simultaneous approximation
- Proof: `proofs/PRODUCT_MODEL_THEOREMS.md`

## N3-ANA-008, high-prime tail central limit theorem

- Result class: `proved theorem`
- Repository status: `PROVED`
- Hypotheses: `y=y(n)->infinity` and `2y<=sqrt(n)`
- Conclusion: the centered log contribution from primes `p>y`, normalized by its standard deviation, converges to `N(0,1)`; moreover
  \[
  B_{n,y}^2\gg n^2\frac{\log y}{y},
  \qquad
  M_{n,y}\ll n\frac{\log y}{y},
  \qquad
  M_{n,y}/B_{n,y}\to0.
  \]
- Constants: absolute, not optimized
- Dependencies: prime number theorem, N3-SRC-002
- Proof: `proofs/PRODUCT_MODEL_THEOREMS.md`

## N3-ANA-009, coarse high-prime window lower bound

- Result class: `conditional theorem`
- Repository status: `CONDITIONAL`
- Hypotheses: N3-ANA-008; `0<Delta<=B_{n,y}`; `|x|<=B_{n,y}`; `Delta>=K M_{n,y}`
- Conclusion:
  \[
  \mathbb P\{T_{n,y}\in[x,x+\Delta]\}
  \gg \Delta/B_{n,y}.
  \]
- Constants: absolute and effective after choosing a Berry-Esseen constant
- Dependencies: N3-ANA-008 and N3-SRC-003
- Proof: `proofs/PRODUCT_MODEL_THEOREMS.md`

## N3-ANA-010, explicit upper-half prime interval count

- Result class: `proved theorem`
- Repository status: `PROVED`
- Hypotheses: integer `n>=120368`
- Conclusion:
  \[
  \pi(n)-\pi(n/2)\ge\frac{n}{3\log n}.
  \]
- Constants: explicit and effective
- Uniformity: every integer `n>=120368`
- Boundaries: `pi(x)` counts primes not exceeding the real number `x`
- Dependencies: N3-SRC-008, Dusart Theorem 6.9
- Proof: `proofs/EXPLICIT_PRIME_INTERVAL_AND_CAPACITY.md`

## N3-ANA-011, explicit Nova 1 menu-capacity threshold

- Result class: `proved theorem`
- Repository status: `PROVED`
- Imported structural dependency: `N1-STR-009`, branch `nova/factorial-structure`, commit `fa11f4b2cb86a2dd791df189ada12757be791804`
- Hypotheses: integer `n>=120368`; Nova 1 definitions of `X_n`, `V_n`, `r_n`, `M_n`, `e_t`, and `U_t(n)`
- Conclusions:
  \[
  e_{M_n}\le\lfloor V_n/2\rfloor-1,
  \]
  \[
  |U_t(n)|\ge2^{\pi(n)-\pi(n/2)-1}-1
  \ge2^{n/(3\log n)-1}-1,
  \]
  and
  \[
  \prod_{t=1}^{M_n}(|U_t(n)|+1)2^{r_n}\ge X_n+1.
  \]
- Thresholds: `n_3=n_4=n_5=120368`
- Constants: explicit and effective
- Distinctness: inherited only for the exact divisor menus from N1-STR-009; profile-sum injectivity is not claimed
- Boundaries: every integer `n>=120368` and every `1<=t<=M_n`
- Dependencies: N3-ANA-010 and imported N1-STR-009
- Proof: `proofs/EXPLICIT_PRIME_INTERVAL_AND_CAPACITY.md`
- Handoff: `handoffs/RESPONSE_TO_NOVA1.md`

## N3-ANA-012, compact-tilt top-prime Gaussian window theorem

- Result class: `proved theorem`
- Repository status: `PROVED`
- Exact divisor family: subset products of primes in `(n/2,n]`, each with factorial valuation one
- Hypotheses: fixed `0<=theta_0<1`, fixed `A>=0`, integer `n>=120368`, and `|theta|<=theta_0`
- Variance conclusion:
  \[
  B_{n,\theta}^2\ge\frac1{48}n^{1-\theta_0}\log n.
  \]
- Berry-Esseen conclusion:
  \[
  \sup_z\left|\mathbb P_\theta\{T_{n,\theta}/B_{n,\theta}\le z\}-\Phi(z)\right|
  \le C_{BE}\frac{\log n}{B_{n,\theta}}
  \le C_{BE}\sqrt{\frac{48\log n}{n^{1-\theta_0}}}.
  \]
- Window conclusion: with
  \[
  c_A=(2\pi)^{-1/2}e^{-(A+1)^2/2},
  \qquad K_A=4C_{BE}/c_A,
  \]
  whenever
  \[
  |x|\le AB_{n,\theta},
  \qquad K_A\log n\le\Delta\le B_{n,\theta},
  \]
  then
  \[
  \mathbb P_\theta\{T_{n,\theta}\in[x,x+\Delta]\}
  \ge\frac{c_A}{2}\frac{\Delta}{B_{n,\theta}}.
  \]
- Count conclusion: the same window contains an explicit positive number of distinct top-prime subset products after division by the maximum tilted atom
- Constants: effective in terms of an accepted universal `C_BE`
- Distinctness: unique factorization; every selected prime has exponent zero or one
- Dependencies: N3-ANA-010 and N3-SRC-003
- Proof: `proofs/COMPACT_TILT_TOP_PRIME_BAND.md`

## N3-ANA-013, unit-tilt freezing obstruction

- Result class: `disproved estimate`
- Repository status: `DISPROVED`
- Disproved estimate: a uniform Gaussian theorem on a fixed top-prime tilt range reaching `|theta|=1`
- Exact conclusion:
  \[
  T_{n,1}/B_{n,1}\to0
  \]
  in probability, and the same holds at `theta=-1`
- Mechanism: with probability tending to one, every Bernoulli coordinate takes its favored endpoint; the centered favored atom is `o(B_{n,1})`
- Dependencies: N3-ANA-010 and N3-SRC-008
- Proof: `proofs/COMPACT_TILT_TOP_PRIME_BAND.md`

## N3-FIN-001, factorial divisor verifier certificate

- Result class: `finite certificate`
- Repository status: `FINITE_CERTIFICATE`
- Range: every integer `2<=n<=12`
- Conclusion: exact divisor count, unique divisors, complement symmetry, log moment formulas, and deterministic local-ceiling test grid pass
- Dependencies: Python standard library only
- Verifier: `proofs/scale_sanity.py`

## N3-FIN-002, explicit threshold verifier certificate

- Result class: `finite certificate`
- Repository status: `FINITE_CERTIFICATE`
- Range: every integer `120368<=n<=1000000`
- Conclusion: exact upper-half prime counts satisfy N3-ANA-010; exact 2-adic valuations satisfy the address condition; the conservative profile-capacity comparison passes
- Minimum observed prime-count margin: greater than `1824`
- Minimum observed address slack: `57942`
- Minimum observed conservative capacity margin: greater than `10,488,000` bits
- Dependencies: Python standard library only
- Verifier: `proofs/prime_interval_capacity_sanity.py`
- What is not claimed: computation is not used to extrapolate beyond the checked range

## N3-FIN-003, compact-tilt moment certificate

- Result class: `finite certificate`
- Repository status: `FINITE_CERTIFICATE`
- Exhaustive range: `n in {11,17,29,43}` and `theta in {-0.75,-0.25,0,0.25,0.75}`
- Conclusion: direct subset enumeration matches the exact tilted normalization, mean, variance, and third-moment ceiling
- Dependencies: Python standard library only
- Verifier: `proofs/compact_tilt_sanity.py`

## N3-COMP-001, asymptotic-scale sanity tables

- Result class: `computational evidence`
- Repository status: `COMPUTATIONAL_EVIDENCE`
- Range: selected `n<=10000`
- Observation: variance ratio, small-prime variance shares, and effective dimension numerically approach the constants predicted in the scale map
- What is not claimed: no asymptotic theorem follows from the finite table
- Verifier: `proofs/scale_sanity.py`

## N3-COMP-002, compact-tilt scale tables

- Result class: `computational evidence`
- Repository status: `COMPUTATIONAL_EVIDENCE`
- Range: selected `n in {120368,200000,500000,1000000}` and `theta_0 in {0.25,0.50,0.75,0.90}`
- Observation: all variance and third-moment inequalities pass; the Berry-Esseen ratios decrease slowly near `theta_0=0.9`; unit-tilt favored-endpoint concentration is visible
- What is not claimed: the selected table is not an asymptotic proof or a fine local limit
- Verifier: `proofs/compact_tilt_sanity.py`

## Open candidate contracts

### N3-CAND-LDC-001

- Result class: `heuristic`
- Status: a coarse weighted count theorem is now proved for top-prime subset products by N3-ANA-012; a fine exact-factorial lower-window theorem for the full bounded-exponent model remains open
- File: `candidates/LOCAL_LOGARITHMIC_DIVISOR_COUNT.md`

### N3-CAND-LLT-001

- Result class: `heuristic`
- Status: compact-tilt coarse windows are closed on the top-prime band by N3-ANA-012; fine windows below `K_A log n` and the full high-prime bounded-exponent model remain open
- File: `candidates/TILTED_LOCAL_LIMIT.md`

### N3-CAND-CF-001

- Result class: `disproved estimate` for the unrestricted version
- Status: bounded-frequency replacement remains open, but Nova 2 requires the numerical additive-value characteristic function on `[-pi,pi]`, not the logarithmic-size characteristic function
- File: `candidates/CHARACTERISTIC_FUNCTION_MINOR_ARC.md`

## Promotion rule

N3-ANA-010 and N3-ANA-011 close Nova 1's explicit capacity dependency. N3-ANA-012 closes the compact-tilt coarse logarithmic-window node only for the exact top-prime subset-product family. None of these results implies numerical additive interval coverage or closes `INT-002`.