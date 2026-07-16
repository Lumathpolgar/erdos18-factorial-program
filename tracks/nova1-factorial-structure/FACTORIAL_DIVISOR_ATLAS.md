# Factorial Divisor-Lattice Atlas

## Scope

This atlas records the exact factorial valuation resources, independent coordinates, legal divisor criteria, numerical distinctness mechanisms, correction reserve, capacity obstructions, and the two surviving large-menu packet architectures.

The frozen target interval is

\[
0\le x\le X_n:=\lfloor\sqrt{n!}\rfloor.
\]

No count in this file is treated as additive coverage.

## 1. Valuation budgets

### N1-STR-003: Legendre budget

Result label: **proved theorem**.

For every prime `p<=n`,

\[
v_p(n!)=
\sum_{j\ge1}\left\lfloor\frac n{p^j}\right\rfloor
=
\frac{n-s_p(n)}{p-1},
\]

where `s_p(n)` is the base-`p` digit sum. Hence

\[
\frac n{p-1}-\lfloor\log_p n\rfloor-1
\le v_p(n!)
\le\frac n{p-1}.
\]

If `p>sqrt(n)`, then

\[
v_p(n!)=\left\lfloor\frac np\right\rfloor.
\]

Proof: `proofs/VALUATION_BUDGET_LEMMAS.md`.

### Exact quotient bands

For `1<=q<sqrt(n)`, define

\[
B_q(n)=
\left\{
 p\text{ prime}:
 \max(\sqrt n,n/(q+1))<p\le n/q
\right\}.
\]

Every `p in B_q(n)` has exact valuation

\[
v_p(n!)=q.
\]

Thus each such prime supplies one independent coordinate with exactly `q+1` exponent states.

### Dyadic prime bands

For `k>=0`, let

\[
I_k(n)=
(n/2^{k+1},n/2^k]
\cap\{p\text{ prime}:p>\sqrt n\}.
\]

For every `p in I_k(n)`,

\[
2^k\le v_p(n!)\le2^{k+1}-1.
\]

### Small-prime multiplicity

For each fixed prime `p`,

\[
v_p(n!)=\frac n{p-1}+O(\log n).
\]

In particular,

\[
v_2(n!)=n-s_2(n).
\]

Therefore `n!` supplies `Theta((log n)^2)` distinct 2-adic marker exponents for all sufficiently large `n`. The lcm core does not:

\[
v_2(\operatorname{lcm}(1,\ldots,n))
=\lfloor\log_2n\rfloor.
\]

This is the factorial-specific multiplicity used by the preferred route.

## 2. Independent divisor coordinates

### N1-STR-004: Valuation-box theorem

Result label: **proved theorem**.

Let `P` be a finite prime set and choose integers

\[
0\le a_p\le v_p(n!).
\]

Every exponent vector

\[
(e_p)_{p\in P}
\in
\prod_{p\in P}\{0,1,\ldots,a_p\}
\]

produces the legal divisor

\[
d(e)=\prod_{p\in P}p^{e_p}\mid n!,
\]

and unique factorization makes the map injective. The box therefore contains exactly

\[
\prod_{p\in P}(a_p+1)
\]

divisors.

The logarithmic size range is contained in

\[
0\le\log d\le
\sum_{p\in P}a_p\log p.
\]

The endpoints occur, but intermediate logarithmic occupancy is not asserted.

### Prime-power dependence

Result label: **disproved route**.

The prime powers `p,p^2,p^3,...` are not independent coordinates. They consume one shared exponent budget. Multiplying selected atoms `p` and `p^2` uses exponent three. The independence rank of a prime-power band is the number of underlying primes, not the number of prime powers.

## 3. Legality under allocated budgets

### N1-STR-005: Valuation-budget partition

Result label: **proved theorem**.

If

\[
a_{p,1}+\cdots+a_{p,L}\le v_p(n!)
\]

and a divisor component in layer `ell` uses exponent at most `a_{p,ell}` at every prime, then the product of one component from each layer divides `n!`.

For additive representations, selected summands are not multiplied. Shared prime factors between two summands do not cause illegality; each summand is checked separately.

## 4. Numerical distinctness

### N1-STR-006: Marker-signature lemma

Result label: **proved theorem**.

Let marker-prime signatures be pairwise distinct and let cores avoid the marker primes. Equality of two labeled divisors would force equality of every marker valuation, so different signatures imply different numerical divisors.

The preferred one-prime form is

\[
d=2^eu,
\]

where `u` is odd. Distinct addresses `e` give distinct divisors even when two layers reuse the same odd core.

Proof: `proofs/DISTINCTNESS_AND_CORRECTION.md`.

### Exact cross-packet criterion

Packets or layers are numerically separated if they use disjoint marker-signature regions. Labels without distinct signatures provide no protection.

## 5. Correction palette

### N1-COR-001: Binary palette

Result label: **proved theorem**.

If `r-1<=v_2(n!)`, then

\[
\mathcal C_r=\{1,2,4,\ldots,2^{r-1}\}
\]

consists of legal distinct divisors and represents every integer

\[
0\le t<2^r
\]

with at most `r` terms.

If every main term has odd part greater than one, the main family is disjoint from the palette.

### N1-RED-002: Downward-window reduction

Result label: **proved theorem**.

Suppose every target `x` with

\[
2^r\le x\le X_n
\]

has a main sum `y` using at most `K(n)` terms and satisfying

\[
x-(2^r-1)\le y\le x.
\]

Then

\[
H_{n!}(X_n+1)\le K(n)+r.
\]

The residual `x-y` is represented by the binary palette. The correction term count is included.

## 6. Capacity gates

### N1-OBS-002: Downward-window counting

Result label: **proved theorem**.

If a finite attainable set `S` is downward `R`-dense on `[0,X]`, then

\[
|S|(R+1)\ge X+1.
\]

A rainbow system with `c_i` nonzero choices in layer `i` has at most

\[
\prod_i(c_i+1)
\]

formal profiles, so coverage requires

\[
\sum_i\log(c_i+1)
\ge
\log(X+1)-\log(R+1).
\]

Proof: `proofs/COUNTING_CAPACITY_OBSTRUCTION.md`.

### Fixed-family obstruction

Result label: **disproved route**.

A fixed pool of `O((log n)^2)` binary or ternary choices has only

\[
\exp(O((\log n)^2))
\]

profiles. Even with quasipolynomial correction, it cannot cover

\[
X_n=\exp(\Theta(n\log n)).
\]

The original fixed-divisor and fixed-pair candidate versions are permanently retired.

### N1-STR-008: Menu entropy requirement

Result label: **proved theorem**.

For `M_n<=A(log n)^2` layers and polynomial correction width, the average layer-state entropy must satisfy

\[
\frac1{M_n}
\sum_{i=1}^{M_n}\log(c_i(n)+1)
\ge
\frac{n}{3A\log n}
\]

for all sufficiently large `n`.

Thus the geometric mean menu size must be

\[
\exp(\Omega(n/\log n)).
\]

Polynomial-size menus are a disproved route.

Proof: `proofs/MENU_ENTROPY_REQUIREMENT.md`.

## 7. High-prime menu source

### N1-STR-009

Result label: **proved theorem**.

Write

\[
n!=2^{V_n}O_n
\]

with `O_n` odd, and let

\[
m_n=\pi(n)-\pi(n/2).
\]

For an address

\[
e\le\lfloor V_n/2\rfloor-1,
\]

define

\[
U_e(n)=
\{u:u\mid O_n,\ u>1,\ 2^eu\le X_n\}.
\]

Then

\[
|U_e(n)|\ge2^{m_n-1}-1.
\]

The proof uses subset products of the primes in `(n/2,n]`, paired around the square root of their product.

Proof: `proofs/HIGH_PRIME_MENU_CAPACITY.md`.

Result label: **conditional theorem** for the explicit capacity asymptotic.

If

\[
m_n\ge\frac{n}{3\log n}
\]

for all sufficiently large `n`, then the frozen preferred constants

\[
M_n=\lceil16(\log n)^2\rceil,
\qquad
r_n=\lceil4\log n\rceil
\]

pass the necessary profile-capacity gate.

## 8. Construction A: full-menu valuation-tagged layers

Result label: **heuristic** as a half-range route.

For

\[
e_t=r_n+t,
\qquad1\le t\le M_n,
\]

define

\[
\mathcal A_t(n)=
\{2^{e_t}u:u\in U_{e_t}(n)\}.
\]

A representation chooses zero or one term from each layer.

### Legal terms

Every layer term divides `n!`.

### Distinctness

Within a layer, different cores give different values. Across layers, 2-adic addresses differ. Palette collision is impossible because cores are greater than one and odd.

### Independent choices

The available choices are the odd cores. The address is a label that certifies numerical distinctness; it is not an additional selectable coordinate.

### Logarithmic scale range

The full menu contains every admissible addressed odd divisor up to `X_n`. Windowed submenus can be defined by imposing

\[
L\le u\le U,
\]

which produces terms in

\[
2^{e_t}L\le d\le2^{e_t}U.
\]

### Maximum selected terms

At most

\[
M_n+r_n
=
\lceil16(\log n)^2\rceil+
\lceil4\log n\rceil
\]

terms are selected.

### Missing additive theorem

For every `x` in `[2^{r_n},X_n]`, prove a rainbow sum in

\[
[x-(2^{r_n}-1),x].
\]

### Exact failure point

Capacity is sufficient at the formal-profile level, but no theorem controls collisions, residue classes, or maximum downward gaps.

Full construction: `constructions/VALUATION_TAGGED_ADDRESS_PACKETS.md`.

## 9. Construction B: complement-pair menu clouds

Result label: **heuristic** as a half-range route.

Choose `M_n=O((log n)^2)` square centers

\[
R_s^2\mid n!
\]

with distinct 2-adic center tags and `5|R_s`. Give each slot a large menu of odd multipliers

\[
Z_s(n)\subseteq\{z:z\mid R_s,\ \gcd(z,10)=1,\ 1<z\le X_n/R_s\}.
\]

The slot menu is

\[
\mathcal B_s(n)=
\{R_s/z:z\in Z_s(n)\}
\cup
\{R_sz:z\in Z_s(n)\}.
\]

Choose zero or one term from each slot.

### Legal terms

Both reciprocal terms divide `R_s^2`, hence divide `n!`.

### Distinctness

Low terms lie below `R_s`, high terms lie above it, and distinct multipliers give distinct values. Cross-slot equality is prevented by distinct 2-adic center tags. Every term is divisible by `5`, so the palette is disjoint.

### Scale range

A multiplier window `[L,U]` simultaneously produces low terms in

\[
[R_s/U,R_s/L]
\]

and high terms in

\[
[R_sL,R_sU].
\]

### Maximum selected terms

At most `M_n+r_n=O((log n)^2)`.

### Missing analytic theorem

Construct center and multiplier menus of geometric-mean size `exp(Omega(n/log n))` across the required scale windows.

### Missing additive theorem

Prove the corresponding global rainbow sumset is downward `2^{r_n}-1` dense on `[2^{r_n},X_n]`.

### Exact failure point

The route adds square-center and multiplier-distribution obligations beyond Construction A. Complement geometry does not itself imply density.

Full construction: `constructions/MARKED_COMPLEMENT_PAIR_CLOUDS.md`.

## 10. Term-cost table

| Route | Available choices | Maximum selected main terms | Correction terms | Total selected terms |
|---|---:|---:|---:|---:|
| Full-menu addressed layers | `sum_t |U_t(n)|` | `M_n` | `r_n` | `M_n+r_n` |
| Complement-pair menu clouds | `sum_s 2|Z_s(n)|` | `M_n` | `r_n` | `M_n+r_n` |

Large available menus do not increase selected-term cost because at most one term is chosen per labeled layer.

## 11. Mandatory falsification ledger

- Divisor legality: proved under exact menu definitions.
- Repeated numerical divisors across labels: prevented by 2-adic signatures.
- Hidden coordinate dependence: prime-power dependence recorded; sum correlations remain open.
- Additive shell gaps: open and explicitly requested from Nova 2.
- Inaccessible residues: open and mandatory to test.
- Capacity versus coverage: separated by proved counting gates.
- Recursive cost: neither route uses recursion.
- Sequential obstruction: both routes are frozen as global rainbow systems; any sequential decoder requires a Phase 12P audit.
- Finite promotion: prohibited.

## 12. Atlas conclusion

The factorial structure resolves three issues rigorously:

1. enough marker valuations exist to label `O((log n)^2)` selected layers;
2. full odd-divisor menus can have the necessary `exp(Omega(n/log n))` scale;
3. binary correction converts downward window occupancy into exact representation.

The preferred route is Construction A. Its exact remaining blocker is uniform additive occupancy of the frozen full-menu rainbow sumset.