# Nova 3 Source Ledger

Every external theorem is recorded with its legal comparison direction. No source below is treated as a theorem about the deterministic sequence `n!` unless that is stated explicitly.

## N3-SRC-001, Robbins explicit Stirling bounds

- Authors: Herbert Robbins
- Title: *A Remark on Stirling's Formula*
- Publication: American Mathematical Monthly 62 (1955), 26-29
- Publication date: 1955
- Exact statement used: for every integer `n>=1`,
  \[
  \frac1{12n+1}<r_n<\frac1{12n}
  \]
  in
  \[
  n!=\sqrt{2\pi}\,n^{n+1/2}e^{-n+r_n}.
  \]
- Repository translation:
  \[
  \log(n!)=(n+1/2)\log n-n+(1/2)\log(2\pi)+r_n.
  \]
- Complete hypotheses: integer `n>=1`
- Parameter range: all positive integers
- Exact factorial divisors or surrogate: exact factorial size, not a divisor-distribution theorem
- Legal direction: direct
- Effective constants: yes
- Status: `ACCEPTED`
- Supports: N3-ANA-004 and `FACTORIAL_DIVISOR_SCALE_MAP.md`

## N3-SRC-002, prime number theorem

- Authors: Jacques Hadamard; Charles-Jean de la Vallée Poussin, independently
- Primary publications: Hadamard, *Sur la distribution des zéros de la fonction zêta(s) et ses conséquences arithmétiques*, Bulletin de la Société Mathématique de France 24 (1896), 199-220; de la Vallée Poussin, *Recherches analytiques sur la théorie des nombres premiers* (1896)
- Publication date: 1896
- Exact statement used:
  \[
  \pi(x)\sim\frac{x}{\log x}.
  \]
  Consequences used are
  \[
  \pi(2x)-\pi(x)\sim\frac{x}{\log x}
  \]
  and, for each fixed integer `k>=1`,
  \[
  \pi(x/k)-\pi(x/(k+1))
  \sim\frac{x}{\log x}\frac1{k(k+1)}.
  \]
- Original notation: prime-counting function `pi(x)`
- Repository translation: counts primes in factorial valuation bands `(n/(k+1),n/k]`
- Complete hypotheses: real `x->infinity`; fixed `k` for the band consequence
- Parameter range: asymptotic
- Exact factorial divisors or surrogate: prime-band input to exact factorial valuation formulas
- Legal direction: direct after the exact band identity is established
- Effective constants: not supplied by the asymptotic theorem
- Status: `ACCEPTED`
- Supports: N3-ANA-004 and N3-ANA-008

## N3-SRC-003, Berry-Esseen inequality for independent summands

- Authors: Andrew C. Berry; Carl-Gustav Esseen
- Primary sources: Berry, *The Accuracy of the Gaussian Approximation to the Sum of Independent Variates*, Transactions of the American Mathematical Society 49 (1941), 122-136; Esseen, *On the Liapunoff limit of error in the theory of probability* (1942/1944)
- Publication date: 1941-1944
- Exact statement used: there is an absolute constant `C_BE` such that, for independent centered real variables `X_j` with finite third absolute moments and `B^2=sum Var(X_j)>0`,
  \[
  \sup_x\left|\mathbb P\left\{\frac{\sum_jX_j}{B}\le x\right\}-\Phi(x)\right|
  \le C_{BE}\frac{\sum_j\mathbb E|X_j|^3}{B^3}.
  \]
- Original notation: normalized sums of independent variates and the standard normal distribution function
- Repository translation: centered logarithmic prime-exponent coordinates, including the tilted Bernoulli coordinates `X_{p,theta}=(A_{p,theta}-E_theta A_{p,theta}) log p` on `(n/2,n]`
- Complete hypotheses: independence, zero mean, positive total variance, finite third absolute moments
- Parameter range: finite triangular arrays
- Exact factorial divisors or surrogate: applies directly after the exact exponent-coordinate model and prime range are frozen
- Legal direction: direct
- Effective constants: universal; the repository leaves `C_BE` symbolic and all downstream constants explicit in terms of it
- Status: `ACCEPTED`
- Supports: N3-ANA-009 and N3-ANA-012

## N3-SRC-004, Ford divisor-in-an-interval theorem

- Author: Kevin Ford
- Title: *The distribution of integers with a divisor in a given interval*
- Publication: Annals of Mathematics (2) 168 (2008), 367-433; arXiv:math/0401223v5
- Publication date: 2008
- Exact theorem audited: the paper determines the order of magnitude of `H(x,y,z)`, which counts integers `m<=x` having at least one divisor in `(y,z]`, with additional multiplicity results
- Original notation: `H(x,y,z)` and `H_r(x,y,z)`
- Repository translation attempted: none is legal for `L_n(u,Delta)`, which counts divisors of the one fixed integer `n!`
- Complete hypotheses: averaging over all integers `m<=x`
- Parameter range: as stated in the paper
- Exact factorial divisors or surrogate: neither; it is a different counting problem
- Legal direction: cannot supply a lower or upper bound for local divisors of `n!` without a new argument
- Status: `REJECTED_FOR_DIRECT_USE`
- Supports: no theorem node; retained to prevent citation misuse

## N3-SRC-005, Gaussian laws for divisors of friable integers

- Authors: Sary Drappeau, Gérald Tenenbaum
- Title: *Lois de répartition des diviseurs des entiers friables*
- Preprint: arXiv:1604.04204
- Publication date: submitted 2016
- Exact theorem audited: Theorem 1.1 gives a Gaussian tail approximation for the logarithm of a uniformly selected divisor for all but a quantified exceptional subset of `y`-friable integers
- Original notation: `D_m`, `S(x,y)`, `sigma_m`, and `w_m`
- Repository translation: `m=n!` is one deterministic member of a friable set, but the theorem does not identify it as nonexceptional
- Complete hypotheses: friability and exclusion of an exceptional subset
- Parameter range: `2<=y<=x`, with the theorem's stated normalized deviation range
- Exact factorial divisors or surrogate: almost all friable integers, not the factorial sequence
- Legal direction: cannot infer a Gaussian law for `n!`; the independent-coordinate method is compatible only at a methodological level
- Status: `PARTIALLY_USABLE_METHOD_ONLY`
- Supports: candidate design in `candidates/TILTED_LOCAL_LIMIT.md`

## N3-SRC-006, ultrafriable arithmetic-progression estimates

- Authors: Cécile Dartyge, David Feutrie, Gérald Tenenbaum
- Title: *Entiers ultrafriables en progressions arithmétiques*
- Preprint: arXiv:2001.04435
- Publication date: 2020
- Exact statement audited from the abstract: uniform arithmetic-progression estimates are proved in stated modulus and `(x,y)` ranges for integers whose occurring prime powers are at most one common parameter `y`
- Original notation: `y`-ultrafriable integers
- Repository translation: divisors of `n!` obey prime-dependent caps `a_p<=v_p(n!)`, not the common cap `p^{a_p}<=y`
- Complete hypotheses: common ultrafriability parameter and arithmetic-progression setting
- Parameter range: as stated in the paper
- Exact factorial divisors or surrogate: different bounded-prime-power set
- Legal direction: lower bounds do not transfer from a larger ultrafriable set to exact factorial divisors
- Status: `REJECTED_FOR_DIRECT_LOCAL_COUNTS`
- Supports: source-audit warning only

## N3-SRC-007, weighted local-limit methods

- Authors: Rita Giuliano, Michel Weber
- Title: *Local Limit Theorems in some Random models from Number Theory*
- Preprint: arXiv:1502.05939
- Publication date: 2015, with later manuscript revisions on arXiv
- Exact statement audited: model-specific characteristic-function local limits for weighted Bernoulli sums, including warnings that central limit information can be too weak on thin sets
- Original notation: weighted independent Bernoulli sums
- Repository translation: the top-prime model in N3-ANA-012 is Bernoulli, but no Giuliano-Weber theorem is imported because its exact weight and characteristic-function hypotheses have not been matched
- Complete hypotheses: theorem-specific weight and characteristic-function assumptions must be independently verified
- Parameter range: as stated in each theorem
- Exact factorial divisors or surrogate: probabilistic method, not a factorial-divisor theorem
- Legal direction: method only for the fine-window target below `K_A log n`
- Status: `PARTIALLY_USABLE_METHOD_ONLY`
- Supports: missing-step analysis for N3-CAND-LLT, N3-CAND-CF, and N3-NEXT-003

## N3-SRC-008, Dusart explicit prime-counting bounds

- Author: Pierre Dusart
- Title: *Estimates of Some Functions Over Primes without R.H.*
- Publication or preprint: arXiv:1002.0442v1
- Publication date: submitted 2 February 2010; manuscript dated 24 January 2007
- Exact theorem: Theorem 6.9 includes
  \[
  \pi(x)\ge\frac{x}{\log x-1}\qquad(x\ge5393)
  \]
  and
  \[
  \pi(x)\le\frac{x}{\log x-1.1}\qquad(x\ge60184).
  \]
- Original notation: `pi(x)` is the number of primes not exceeding the real number `x`
- Repository notation translation: apply the lower bound at `x=n` and the upper bound at `x=n/2`
- Complete hypotheses: real `x>=5393` for the lower bound and real `x>=60184` for the upper bound
- Parameter range used: every integer `n>=120368`, so both source hypotheses hold
- Exact factorial divisors or surrogate: prime-interval input to exact high-prime divisor families of `n!`
- Legal direction: direct subtraction of a lower bound for `pi(n)` and an upper bound for `pi(n/2)`
- Derived repository statement:
  \[
  \pi(n)-\pi(n/2)\ge\frac{n}{3\log n}
  \qquad(n\ge120368).
  \]
- Effective constants: yes
- Compatibility proofs: `proofs/EXPLICIT_PRIME_INTERVAL_AND_CAPACITY.md` and `proofs/COMPACT_TILT_TOP_PRIME_BAND.md`
- Status: `ACCEPTED`
- Supports: N3-ANA-010, N3-ANA-011, N3-ANA-012, N3-ANA-013, and Nova 1 request `N1-REQ-N3-001-A`

## Source conclusions

Accepted external inputs are Robbins explicit Stirling bounds, the prime number theorem, Berry-Esseen, and Dusart's explicit prime-counting inequalities. N3-ANA-012 and N3-ANA-013 otherwise use direct calculations in the exact top-prime factorial divisor model. Ford's interval theorem, friable almost-all Gaussian laws, and ultrafriable progression estimates do not provide deterministic lower bounds for exact divisors of `n!`.