# Factorial Divisor-Lattice Atlas

## Scope

This atlas records exact valuation resources, legal divisor-coordinate rules, collision criteria, correction reserves, and two structurally different packet architectures for `n!`.

The target interval is always

\[
0\le x\le X_n:=\lfloor\sqrt{n!}\rfloor.
\]

No divisor count or profile count in this document is asserted to imply additive coverage.

## 1. Exact valuation budgets

### N1-STR-003: Legendre budget and quotient bands

Result label: **proved theorem**.

For every prime `p <= n`,

\[
v_p(n!)=\sum_{j\ge1}\left\lfloor\frac{n}{p^j}\right\rfloor
=\frac{n-s_p(n)}{p-1},
\]

where `s_p(n)` is the sum of the base-`p` digits of `n`. Consequently,

\[
\frac{n}{p-1}-\lfloor\log_p n\rfloor-1
\le v_p(n!)\le \frac{n}{p-1}.
\]

If `p > sqrt(n)`, then `p^2 > n`, so

\[
v_p(n!)=\left\lfloor\frac np\right\rfloor.
\]

For an integer `q` satisfying `1 <= q < sqrt(n)`, define the quotient band

\[
B_q(n)=\left\{p\text{ prime}:\max(\sqrt n,n/(q+1))<p\le n/q\right\}.
\]

Every `p in B_q(n)` has the exact valuation

\[
v_p(n!)=q.
\]

This identifies prime bands whose coordinates have exactly `q+1` available exponent states.

### Dyadic prime intervals

For every integer `k >= 0`, define

\[
I_k(n)=\left(n/2^{k+1},n/2^k\right]\cap\{p\text{ prime}:p>\sqrt n\}.
\]

For every `p in I_k(n)`,

\[
2^k\le v_p(n!)\le 2^{k+1}-1.
\]

Thus a prime in `I_k(n)` supplies one independent prime coordinate with at least `2^k+1` legal exponent values.

### Small-prime multiplicity

For every fixed prime `p`,

\[
v_p(n!)=\frac{n}{p-1}+O(\log n).
\]

In particular,

\[
v_2(n!)=n-s_2(n)\ge n-\lfloor\log_2n\rfloor-1.
\]

Hence, for every fixed `A>0`,

\[
A(\log n)^2\le v_2(n!)
\]

for all sufficiently large `n`. This permits `Theta((log n)^2)` distinct 2-adic marker exponents. By contrast,

\[
v_2(\operatorname{lcm}(1,\ldots,n))=\lfloor\log_2 n\rfloor,
\]

so this marker budget is factorial-specific.

## 2. Independent coordinates and prime-power bands

### N1-STR-004: Valuation-box theorem

Result label: **proved theorem**.

Let `P` be a finite set of primes and let integers `a_p` satisfy

\[
0\le a_p\le v_p(n!)\qquad(p\in P).
\]

Then every exponent vector

\[
(e_p)_{p\in P}\in\prod_{p\in P}\{0,1,\ldots,a_p\}
\]

produces the legal divisor

\[
d(e)=\prod_{p\in P}p^{e_p}\mid n!,
\]

and distinct exponent vectors produce distinct numerical divisors. Therefore the box supplies exactly

\[
\prod_{p\in P}(a_p+1)
\]

legal divisors.

The number of independent coordinates is `|P|`, not the number of prime powers `p^j` appearing below `n`.

The generated logarithmic range is exactly contained in

\[
0\le\log d\le W(P,a):=\sum_{p\in P}a_p\log p.
\]

The endpoint values `1` and `exp(W(P,a))` occur as divisors, but the theorem does not assert that all intermediate logarithmic values occur.

### Prime-power dependence obstruction

Result label: **disproved route**.

Treating `p,p^2,p^3,...` as independent binary coordinates is invalid. They all consume the same coordinate `v_p`. For example, selecting the multiplicative atoms `p` and `p^2` creates exponent `3`, not two independent prime coordinates. Any packet construction built by multiplying prime-power atoms must prove that the total exponent used at each prime does not exceed `v_p(n!)`.

Prime-power bands remain useful as valuation increments, but their independence rank is the number of underlying primes.

## 3. Budget partition and divisor legality

### N1-STR-005: Valuation-budget partition lemma

Result label: **proved theorem**.

Suppose each prime budget is partitioned into nonnegative allocations

\[
a_{p,1}+\cdots+a_{p,L}\le v_p(n!).
\]

For each layer `ell`, let

\[
u_\ell=\prod_p p^{e_{p,\ell}},\qquad 0\le e_{p,\ell}\le a_{p,\ell}.
\]

Then every `u_ell` divides `n!`, and the product of one selected component from every layer also divides `n!` because the total exponent at `p` is at most `sum_ell a_{p,ell}`.

For additive representations, selected divisors are not multiplied together, so shared prime factors between two summands do not by themselves violate legality. Legality is checked separately for each summand. Budget partition is required only when a divisor is itself assembled multiplicatively from several allocated components.

## 4. Numerical distinctness mechanisms

### N1-STR-006: Marker-signature lemma

Result label: **proved theorem**.

Let `M` be a finite marker-prime set. For every label `t`, choose a signature

\[
\sigma_t=(e_{q,t})_{q\in M}
\]

and a core `u_t` coprime to every prime in `M`. Define

\[
d_t=u_t\prod_{q\in M}q^{e_{q,t}}.
\]

If the signatures `sigma_t` are pairwise distinct, then the numerical divisors `d_t` are pairwise distinct, because equality would force equality of every marker-prime valuation.

A one-prime specialization uses

\[
d_t=2^{e_t}u_t,
\]

with odd `u_t` and pairwise distinct `e_t`.

### Cross-packet distinctness criterion

Assign packet `j` a marker-signature region `Sigma_j` disjoint from every other packet's region. Require every core to avoid marker primes. Then any selections from different packets are numerically distinct. This remains true even when two cores are numerically equal.

### Failure condition

Labels alone provide no distinctness. If two labels use the same marker signature and the same core, they are the same divisor and cannot both appear in a legal sum.

## 5. Reserved correction palette

### N1-COR-001: Binary correction palette

Result label: **proved theorem**.

Let `r>=1` satisfy

\[
r-1\le v_2(n!).
\]

Define

\[
\mathcal C_r=\{1,2,4,\ldots,2^{r-1}\}.
\]

Every member of `C_r` divides `n!`, and every integer

\[
0\le t<2^r
\]

has a unique representation as a sum of a subset of `C_r`, using at most `r` terms.

If every main-construction divisor has odd part greater than one, then no main divisor belongs to `C_r`. Therefore the correction terms are automatically disjoint from the main terms.

### N1-RED-002: Downward-window correction reduction

Result label: **proved theorem**.

Let `A_n` be a legal, numerically distinct main family of divisors of `n!`, disjoint from `C_r`. Suppose every integer `x` with

\[
2^r\le x\le X_n
\]

has a main-family sum `y` satisfying

\[
x-(2^r-1)\le y\le x
\]

and using at most `K(n)` terms. Then every integer `0<=x<=X_n` is a sum of at most

\[
K(n)+r
\]

distinct divisors of `n!`.

Proof mechanism: represent `x-y` by the binary palette; for `x<2^r`, use the palette alone.

### Entropy cost of the reserve

The palette consumes only the pure powers `2^0,...,2^{r-1}` as summands. It does not consume those valuations from other divisors, because additive summands are checked separately. To avoid numerical collision, main terms must have odd part greater than one. For `r=Theta(log n)`, the palette corrects a polynomial-width residual with `Theta(log n)` terms. For `r=Theta((log n)^2)`, it corrects a quasipolynomial-width residual but consumes the full allowed order of terms.

## 6. Packet Construction A: factorial 2-adic address packets

Result label: **heuristic** as a complete route; its legality and distinctness sublemmas are proved theorems.

Choose constants `A,B>0`,

\[
r=\lceil B\log n\rceil,\qquad M=\lceil A(\log n)^2\rceil,
\]

and pairwise distinct exponents

\[
e_t=r+t,\qquad 1\le t\le M.
\]

For sufficiently large `n`, `e_M<=v_2(n!)`. Choose odd cores `u_t>1` satisfying

\[
u_t\mid n!,\qquad 2^{e_t}u_t\le X_n,
\]

and define

\[
d_t=2^{e_t}u_t.
\]

Partition the indices into `J=O(log n)` packets of `O(log n)` labels each, but allow a globally chosen subset of all labels rather than one sequential choice per packet.

### Legal divisor proof

Each `d_t` divides `n!` when

\[
e_t\le v_2(n!)
\]

and every odd-prime valuation in `u_t` is within the factorial budget.

### Independent coordinates supplied

The marker system supplies `M` distinct 2-adic addresses, while the odd cores are drawn from an independent odd-prime divisor box. The addresses certify distinctness but do not themselves imply distinct sums.

### Generated logarithmic scale

For prescribed target scales `Y_t`, a core in the interval

\[
Y_t/2^{e_t}\le u_t\le (Y_t+W_t)/2^{e_t}
\]

places `d_t` inside `[Y_t,Y_t+W_t]`. Existence of such odd divisors is an analytic input, not a structural consequence of the valuation count.

### Maximum legal selected terms

At most `M` main divisors plus `r` correction terms may be selected. Thus the exact cost is

\[
M+r\le A(\log n)^2+B\log n+2.
\]

### Reserved correction

Use `C_r`. Every main divisor has odd part `u_t>1`, so no collision with the palette occurs.

### Current failure point

The route has no proof that a subset of `{d_t}` lies in every downward window

\[
[x-(2^r-1),x]
\]

uniformly for every `x<=X_n`. The number of possible subsets is capacity, not coverage. This is the exact missing additive theorem.

## 7. Packet Construction B: marked complement-pair clouds

Result label: **heuristic** as a complete route; the complement-pair legality and distinctness statement is a proved theorem.

For `J=O(log n)`, choose square divisors

\[
Q_j=R_j^2\mid n!
\]

with pairwise distinct 2-adic center valuations

\[
E_j=v_2(R_j),
\]

and with `5|R_j`. For each cloud choose `m_j=O(log n)` distinct odd multipliers `z_{j,t}` such that

\[
z_{j,t}\mid R_j,\qquad \gcd(z_{j,t},10)=1,
\qquad 1<z_{j,t}\le X_n/R_j.
\]

Define the pair

\[
a_{j,t}=R_j/z_{j,t},\qquad b_{j,t}=R_jz_{j,t}.
\]

The selectable state for a pair is `0`, `a_{j,t}`, or `b_{j,t}`. Choices are made jointly across all pairs; there is no prescribed sequential ladder.

### Legal divisor proof

Because `z_{j,t}|R_j`, both `R_j/z_{j,t}` and `R_jz_{j,t}` divide `R_j^2=Q_j`, hence divide `n!`. The upper condition on `z_{j,t}` gives `b_{j,t}<=X_n`; the lower term is automatically below `R_j<=X_n`.

### Numerical distinctness

Within a cloud,

\[
a_{j,t}<R_j<b_{j,t}.
\]

Distinct multipliers give distinct low terms and distinct high terms, while low/high cross-collisions are impossible. Across clouds, every term has 2-adic valuation `E_j` because the multipliers are odd; distinct `E_j` therefore separate clouds numerically. Every term remains divisible by `5`, so no term collides with the binary correction palette.

### Switch-increment form

Choosing the low term in a pair and then switching to the high term changes the sum by

\[
\Delta_{j,t}=R_j\left(z_{j,t}-z_{j,t}^{-1}\right)
=b_{j,t}-a_{j,t}.
\]

This exposes the route as a globally coupled restricted subset-sum problem on the increments, not as a one-choice sequential growth recurrence.

### Maximum legal selected terms

At most one term is chosen from each pair. Therefore the main term cost is exactly bounded by

\[
\sum_{j=1}^Jm_j=O((\log n)^2).
\]

Adding `C_r` gives total cost

\[
\sum_jm_j+r.
\]

### Represented scale

The highest available term in cloud `j` is `R_j max_t z_{j,t}` and the lowest is `R_j/max_t z_{j,t}`. A family of centers and multipliers can in principle span the half-range, but the structural theorem does not prove that suitable legal multipliers exist in every required logarithmic band.

### Current failure point

Two separate statements are missing:

1. an analytic selection theorem producing legal `R_j` and `z_{j,t}` across all necessary scales with the stated marker restrictions;
2. an additive theorem proving that the three-choice restricted sumset is downward-window dense throughout `[2^r,X_n]`.

The construction is not automatically subject to Phase 12P because it is not an ordered one-choice ladder. A later proof that imposes a sequential decoding order would have to re-audit the Phase 12P hypotheses.

## 8. Full term-cost comparison

| Construction | Main terms | Correction terms | Total claimed architecture cost | Current status |
|---|---:|---:|---:|---|
| 2-adic address packets | `M=ceil(A(log n)^2)` | `r=ceil(B log n)` | `A(log n)^2+B log n+O(1)` | legality and distinctness proved; occupancy open |
| complement-pair clouds | `sum_j m_j`, with `J,m_j=O(log n)` | `r=ceil(B log n)` | `O((log n)^2)` | legality and distinctness proved; analytic selection and occupancy open |

## 9. Mandatory falsification summary

- Divisor legality: proved under explicit valuation conditions.
- Repeated numerical divisors across labels: prevented by 2-adic signatures.
- Hidden dependence between coordinates: prime-power dependence explicitly recorded.
- Additive shell gaps: not ruled out; they are part of the exact missing occupancy theorem.
- Inaccessible residue classes: not ruled out; Nova 2 must test the gcd and residue span of every frozen family.
- Capacity versus coverage: no coverage claim is made from profile count.
- Recursive term cost: neither preferred candidate uses recursive decoding in its present definition.
- Sequential obstruction: Construction B is globally nonsequential; Construction A also permits a global subset choice, but any sequential proof must be re-audited.
- Finite-to-asymptotic promotion: prohibited.

## 10. Atlas conclusion

The factorial lattice supplies a proved `Theta((log n)^2)` marker-address budget and a proved `Theta(log n)` binary correction palette. These remove divisor legality and numerical collision as primary obstacles for two broad architectures. The unresolved node is uniform additive occupancy, together with the analytic construction of cores or complement multipliers at the required scales.