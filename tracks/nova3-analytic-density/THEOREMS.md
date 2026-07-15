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
- Dependencies: prime number theorem, registered as N3-SRC-002; Lindeberg-Feller theorem proved through the displayed bounded-array verification
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

## N3-FIN-001, finite verifier certificate

- Result class: `finite certificate`
- Repository status: `FINITE_CERTIFICATE`
- Range: every integer `2<=n<=12`
- Conclusion: exact divisor count, unique divisors, complement symmetry, log moment formulas, and deterministic local-ceiling test grid pass
- Dependencies: Python standard library only
- Verifier: `proofs/scale_sanity.py`
- Command:
  ```text
  python3 tracks/nova3-analytic-density/proofs/scale_sanity.py
  ```

## N3-COMP-001, asymptotic-scale sanity tables

- Result class: `computational evidence`
- Repository status: `COMPUTATIONAL_EVIDENCE`
- Range: selected `n<=10000`
- Observation: variance ratio, small-prime variance shares, and effective dimension numerically approach the constants predicted in the scale map
- What is not claimed: no asymptotic theorem follows from the finite table
- Verifier: `proofs/scale_sanity.py`

## Open candidate contracts

### N3-CAND-LDC-001

- Result class: `heuristic`
- Status: desired exact tilted-window lower bound remains open
- File: `candidates/LOCAL_LOGARITHMIC_DIVISOR_COUNT.md`

### N3-CAND-LLT-001

- Result class: `heuristic`
- Status: fine tilted local limit remains open; N3-ANA-009 is the strongest current substitute
- File: `candidates/TILTED_LOCAL_LIMIT.md`

### N3-CAND-CF-001

- Result class: `disproved estimate` for the unrestricted version
- Status: bounded-frequency replacement remains open
- File: `candidates/CHARACTERISTIC_FUNCTION_MINOR_ARC.md`

## Promotion rule

No theorem in this registry implies additive interval coverage without a separate Nova 2 theorem. No result closes `INT-002` at this checkpoint.
