# Nova 3 Source Ledger

Every external theorem is recorded with its legal comparison direction. No source below is treated as a theorem about the deterministic sequence `n!` unless that is stated explicitly.

## N3-SRC-001, Robbins' explicit Stirling bounds

- Authors: Herbert Robbins
- Title: *A Remark on Stirling's Formula*
- Publication: American Mathematical Monthly 62 (1955), 26-29
- Publication date: 1955
- Original notation: `n! = sqrt(2 pi) n^(n+1/2) e^(-n+r_n)`
- Exact statement used: for every integer `n>=1`,
  \[
  \frac1{12n+1}<r_n<\frac1{12n}.
  \]
- Repository translation:
  \[
  \log(n!)=(n+1/2)\log n-n+(1/2)\log(2\pi)+r_n.
  \]
- Complete hypotheses: integer `n>=1`
- Parameter range: all positive integers
- Exact factorial divisors or surrogate: exact factorial size, not a divisor-distribution theorem
- Legal direction: direct
- Status: `ACCEPTED`
- Supports: N3-ANA-004A in `FACTORIAL_DIVISOR_SCALE_MAP.md`

## N3-SRC-002, prime number theorem

- Authors: Jacques Hadamard; Charles-Jean de la Vallée Poussin, independently
- Primary publications: Hadamard, *Sur la distribution des zéros de la fonction zêta(s) et ses conséquences arithmétiques*, Bulletin de la Société Mathématique de France 24 (1896), 199-220; de la Vallée Poussin, *Recherches analytiques sur la théorie des nombres premiers*, 1896
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
- Legal direction: direct after exact band identity is established
- Effective constants: not required for the asymptotic statements used; an effective implementation may substitute published explicit estimates such as Christian Axler, *New estimates for some functions defined over primes*, arXiv:1703.08032v2 (2017)
- Status: `ACCEPTED`
- Supports: N3-ANA-004B and N3-ANA-008

## N3-SRC-003, Berry-Esseen inequality for independent summands

- Authors: Andrew C. Berry; Carl-Gustav Esseen
- Primary sources: Berry, *The Accuracy of the Gaussian Approximation to the Sum of Independent Variates*, Transactions of the American Mathematical Society 49 (1941), 122-136; Esseen, *On the Liapunoff limit of error in the theory of probability*, 1942/1944
- Publication date: 1941-1944
- Exact statement used: there is an absolute constant `C_BE` such that, for independent centered real variables `X_j` with finite third absolute moments, `B^2=sum Var(X_j)>0`,
  \[
  \sup_x\left|\mathbb P\left\{\frac{\sum_jX_j}{B}\le x\right\}-\Phi(x)\right|
  \le C_{BE}\frac{\sum_j\mathbb E|X_j|^3}{B^3}.
  \]
- Original notation: normalized sums of independent variates and the standard normal distribution function
- Repository translation: `X_j=(A_p-b_p/2) log p` over a selected prime range
- Complete hypotheses: independence, zero mean, positive total variance, finite third absolute moments
- Parameter range: finite triangular arrays
- Exact factorial divisors or surrogate: applies directly to the independent exponent-coordinate model after the prime range is frozen
- Legal direction: direct
- Effective constants: universal; no optimized numerical value is needed
- Status: `ACCEPTED`
- Supports: N3-ANA-009

## N3-SRC-004, Ford divisor-in-an-interval theorem

- Author: Kevin Ford
- Title: *The distribution of integers with a divisor in a given interval*
- Publication: Annals of Mathematics (2) 168 (2008), 367-433; arXiv:math/0401223v5
- Publication date: final version 2008
- Original notation: `H(x,y,z)` counts integers `m<=x` having at least one divisor in `(y,z]`; `H_r(x,y,z)` counts integers having exactly `r` such divisors
- Exact statement audited: the paper determines the order of magnitude of `H(x,y,z)` for all `x,y,z`, with additional results for `H_r` in stated ranges
- Repository translation attempted: none is legal for `L_n(u,Delta)`, which counts divisors of the one fixed integer `n!`
- Complete hypotheses: averaging over all integers `m<=x`
- Parameter range: as in the paper
- Exact factorial divisors or surrogate: neither; it is a different counting problem
- Legal direction: cannot supply either a lower or upper bound for local divisors of `n!` without a new argument
- Status: `REJECTED_FOR_DIRECT_USE`
- Supports: no theorem node; retained to prevent subject-area citation misuse

## N3-SRC-005, Gaussian laws for divisors of friable integers

- Authors: Sary Drappeau, Gérald Tenenbaum
- Title: *Lois de répartition des diviseurs des entiers friables*
- Preprint: arXiv:1604.04204
- Publication date: submitted 2016
- Original notation: for an integer `m`, `D_m` is the logarithm of a uniformly selected divisor; `S(x,y)` is the set of `y`-friable integers at most `x`; `sigma_m` is the divisor-log standard deviation; `w_m=sigma_m^4/m_{4,m}`
- Exact theorem audited, Theorem 1.1: uniformly for all but at most `<< exp(-c sqrt(bar u)) Psi(x,y)` integers `m in S(x,y)`,
  \[
  \mathbb P\left(D_m\ge\tfrac12\log m+z\sigma_m\right)
  =\Phi(z)+O\left(\frac{1+z^4}{w_m}\Phi(|z|)\right)
  \]
  for `z << w_m^(1/4)`
- Repository translation: `m=n!` would be one exceptional-or-nonexceptional member of a friable set, but the theorem does not identify which
- Complete hypotheses: friability plus exclusion of an exceptional subset
- Parameter range: `2<=y<=x`, with the theorem's stated `z` range
- Exact factorial divisors or surrogate: theorem about almost all friable integers, not the fixed factorial sequence
- Legal direction: cannot infer a Gaussian law for `n!`; the independent-coordinate decomposition is methodologically compatible
- Status: `PARTIALLY_USABLE_METHOD_ONLY`
- Supports: candidate design in `candidates/TILTED_LOCAL_LIMIT.md`, not a proved repository theorem

## N3-SRC-006, ultrafriable arithmetic-progression estimates

- Authors: Cécile Dartyge, David Feutrie, Gérald Tenenbaum
- Title: *Entiers ultrafriables en progressions arithmétiques*
- Preprint: arXiv:2001.04435
- Publication date: 2020
- Original notation: an integer is `y`-ultrafriable when every prime power in its canonical factorization is at most `y`
- Exact statement audited from the abstract: uniform arithmetic-progression estimates are proved for moduli `q<=y^{c/log_2 y}` when `log y<=(log x)^epsilon`, and for `q<=sqrt(y)` when `(log x)^{2+epsilon}<=y<=x`
- Repository translation: divisors of `n!` obey prime-dependent caps `a_p<=v_p(n!)`, not the common cap `p^{a_p}<=y`
- Complete hypotheses: common ultrafriability parameter and arithmetic-progression setting
- Exact factorial divisors or surrogate: a different bounded-prime-power set
- Legal direction: an inclusion may be used only after proving it for the chosen `x,y`; lower bounds do not transfer from the larger set
- Status: `REJECTED_FOR_DIRECT_LOCAL_COUNTS`
- Supports: source-audit warning only

## N3-SRC-007, weighted local-limit methods

- Authors: Rita Giuliano, Michel Weber
- Title: *Local Limit Theorems in some Random models from Number Theory*
- Preprint: arXiv:1502.05939
- Publication date: 2015, later manuscript revisions visible on arXiv
- Original notation: weighted sums of independent Bernoulli variables; local limit estimates proved under model-specific characteristic-function hypotheses
- Exact statement audited: the paper develops characteristic-function local limits for weighted Bernoulli sums and explicitly notes that standard central limit information can be too weak for probabilities on thin sets
- Repository translation: factorial exponent coordinates are bounded discrete uniforms, not Bernoulli variables, though Bernoulli-part extraction may be possible
- Complete hypotheses: theorem-specific weight and characteristic-function conditions must be verified before use
- Exact factorial divisors or surrogate: probabilistic method, not a factorial-divisor theorem
- Legal direction: no theorem is imported at this checkpoint
- Status: `PARTIALLY_USABLE_METHOD_ONLY`
- Supports: missing-step analysis for N3-CAND-LLT and N3-CAND-CF

## Source conclusions

Accepted external inputs are limited to explicit Stirling bounds, prime distribution, and a general Berry-Esseen inequality. The exact factorial-divisor theorems in this checkpoint are otherwise proved directly. Ford's interval theorem, friable almost-all Gaussian laws, and ultrafriable progression estimates do not legally provide the required deterministic lower bounds for divisors of `n!`.
