# Transformed Dyadic Resonance Ladder

## Scope

This file continues the exact odd-lattice normalization from `N3-ANA-025`. It studies the numerical marker-three quotient law after conditioning on the odd component, subtracting one, and dividing by two. It does not use logarithmic divisor size as a surrogate.

Imported heads:

- Nova 1: `nova/factorial-structure@1b81ec74f907d57d520bcf6c51f2e6e71f0474a7`
- Nova 2: `nova/additive-occupancy@e443674f86b2ee3c7037ac94ee47f6b8a4b3b29f`

The factorial half-range theorem and Erdős Problem 18 remain open.

## Frozen notation

For every integer `n>=120368`, set

\[
\rho_n=\lceil4\log n\rceil,
\qquad
M_n=\lceil16(\log n)^2\rceil,
\]

\[
X_n=\lfloor\sqrt{n!}\rfloor,
\qquad
Y_n=\left\lfloor\frac{X_n}{3}\right\rfloor,
\qquad
W_n=\left\lfloor\frac{2^{\rho_n}-3}{3}\right\rfloor.
\]

Let `m_n` be the largest odd integer at most `n`, and put

\[
L_n=m_n(2^{M_n}-1),
\qquad
P_n=L_n+W_n.
\]

The exact final-only target range is

\[
P_n+1\le q\le Y_n.
\]

The original quotient layers are

\[
B_t(n)=
\{2^{t-1}u:
 u\text{ odd},\ 3u\mid n!,\ 2^{t-1}u\le Y_n\}.
\]

By `N3-ANA-025`, after conditioning on `Z_1\ne0`, define

\[
\widetilde Z_1=\frac{Z_1-1}{2},
\qquad
\widetilde Z_t=\frac{Z_t}{2}
\quad(t\ge2),
\]

and

\[
\widetilde T=\sum_{t=1}^{M_n}\widetilde Z_t.
\]

The transformed coordinates remain independent and have common tilt

\[
\widetilde\lambda_{n,q}=2\lambda_{n,q}.
\]

Their supports are

\[
\widetilde B_1(n)
=
\left\{\frac{u-1}{2}:
 u\text{ odd},\ 3u\mid n!,\ u\le Y_n\right\},
\]

and, for `t>=2`,

\[
\widetilde B_t(n)
=
\{0\}
\cup
\{2^{t-2}u:
 u\text{ odd},\ 3u\mid n!,\ 2^{t-1}u\le Y_n\}.
\]

Write

\[
\widetilde\phi_{t,n,q}(\theta)
=\mathbb E e^{i\theta\widetilde Z_t},
\qquad
\widetilde\Phi_{n,q}(\theta)
=\prod_{t=1}^{M_n}\widetilde\phi_{t,n,q}(\theta).
\]

For one transformed layer define

\[
\widetilde{\mathcal D}_{t,n,q}(\theta)
=
\sum_{a,b}
P(\widetilde Z_t=a)P(\widetilde Z_t=b)
\sin^2\left(\frac{(a-b)\theta}{2}\right).
\]

Then exactly

\[
|\widetilde\phi_{t,n,q}(\theta)|^2
=1-2\widetilde{\mathcal D}_{t,n,q}(\theta).
\]

## Legal low-state block

Let

\[
k_n=\frac{m_n+1}{2}.
\]

For every odd `u` with `1<=u<=m_n`, one has `3u|n!`. Indeed, `u|n!`, and

\[
v_3(u)\le\log_3 n
<\left\lfloor\frac n3\right\rfloor
\le v_3(n!),
\]

so one factor of `3` remains beyond those already occurring in `u`.

Also

\[
m_n2^{M_n-1}<L_n<P_n<Y_n.
\]

Therefore every layer contains all states

\[
2^{t-1}u
\qquad
(1\le t\le M_n,
\ 1\le u\le m_n,
\ u\text{ odd}).
\]

Consequently:

1. the first transformed support contains `0,1,...,k_n-1`;
2. every transformed layer `t>=2` contains `0` and every `2^{t-2}u` with odd `1<=u<=m_n`.

This block is used only for lower bounds on partition functions. It is not treated as the full menu.

## Uniform zero-state estimate

From `N3-ANA-020`,

\[
\widetilde\lambda_{n,q}
>-
\frac{16M_n\log L_n}{L_n}.
\]

For `t>=2`, define

\[
\eta_{n,t}
=
\frac{16M_n\log L_n}{2^{M_n}-1}
2^{t-2}.
\]

Every displayed small positive state in transformed layer `t` is at most `2^{t-2}m_n`, so its tilted weight is at least `e^{-\eta_{n,t}}`.

Let

\[
p_{t,n,q}^{(0)}
=P_{\widetilde\lambda_{n,q}}(\widetilde Z_t=0).
\]

The transformed layer partition function contains the zero state and `k_n` displayed positive states. Hence

\[
p_{t,n,q}^{(0)}
\le
\frac{1}{1+k_ne^{-\eta_{n,t}}}
\le
\frac{2e^{\eta_{n,t}}}{m_n+1}.
\]

## N3-ANA-026: exact dyadic finite-prefix factorization

Result class: **proved theorem**.

For

\[
\theta_j=\frac{\pi}{2^{j-1}}
=\frac{2\pi}{2^j},
\qquad
1\le j\le M_n-1,
\]

one has:

\[
\widetilde\phi_{j+1,n,q}(\theta_j)
=2p_{j+1,n,q}^{(0)}-1,
\]

\[
\widetilde\phi_{t,n,q}(\theta_j)=1
\qquad(t\ge j+2),
\]

and

\[
\widetilde\Phi_{n,q}(\theta_j)
=
\left(
\prod_{t=1}^{j}
\widetilde\phi_{t,n,q}(\theta_j)
\right)
\left(2p_{j+1,n,q}^{(0)}-1\right).
\]

### Proof

Every nonzero matching-layer state has the form `2^{j-1}u` with `u` odd. Thus

\[
e^{i\theta_j2^{j-1}u}=e^{i\pi u}=-1.
\]

The zero state has phase `1`, which gives the matching-layer formula.

For `t>=j+2`, every nonzero transformed state is `2^{t-2}u`, so

\[
\theta_j2^{t-2}u
=
\pi2^{t-j-1}u
\]

is an integer multiple of `2\pi`. Every later-layer phase is therefore `1`. Multiplying the coordinate factors proves the factorization. `QED`

### Exact resonance classification

The transformed first support contains both `0` and `1` with positive probability. Hence no nonzero dyadic frequency is an exact modulus-one resonance of the full transformed law.

Every reduced dyadic frequency nevertheless has an exact tail resonance because all layers after `j+1` are invisible there.

## N3-ANA-027: matching-layer near-pure sign and tail collapse

Result class: **proved theorem and disproved route estimate**.

Define

\[
J_n
=
\min\left(
M_n-1,
\left\lfloor
1+
\log_2\left(
\frac{2^{M_n}-1}{16M_n\log L_n}
\right)
\right\rfloor
\right).
\]

Then

\[
J_n=M_n-O(\log\log n).
\]

For every `1<=j<=J_n` and every post-prefix target,

\[
\eta_{n,j+1}\le1,
\]

\[
p_{j+1,n,q}^{(0)}
\le
\frac{2e}{m_n+1},
\]

\[
\left|
\widetilde\phi_{j+1,n,q}(\theta_j)
\right|
\ge
1-
\frac{4e}{m_n+1},
\]

and

\[
\sum_{t=j+1}^{M_n}
\widetilde{\mathcal D}_{t,n,q}(\theta_j)
=
2p_{j+1,n,q}^{(0)}
(1-p_{j+1,n,q}^{(0)})
\le
\frac{4e}{m_n+1}.
\]

### Proof

The definition of `J_n` is exactly the largest safe integer range for which

\[
\frac{16M_n\log L_n}{2^{M_n}-1}
2^{j-1}
\le1.
\]

The zero-state bound follows from the preceding partition estimate. Since this upper bound is below `1/2` throughout the stated range,

\[
|2p_{j+1,n,q}^{(0)}-1|
=1-2p_{j+1,n,q}^{(0)}
\ge
1-
\frac{4e}{m_n+1}.
\]

Every layer after `j+1` has zero dispersion at `\theta_j`. The matching layer has only the two phases `1` and `-1`, so its dispersion is exactly

\[
2p_{j+1,n,q}^{(0)}
(1-p_{j+1,n,q}^{(0)}).
\]

Finally,

\[
\log_2(16M_n\log L_n)=O(\log\log n),
\]

because both `M_n` and `log L_n` are of order `(log n)^2`. Therefore `M_n-J_n=O(log log n)`. `QED`

### Disproved route estimate

The following mechanism is false:

> Outside a zero major arc, a positive proportion of all transformed tail layers always contributes a fixed amount of phase dispersion.

At every `\theta_j`, the complete tail after the first `j` coordinates contributes at most `O(1/n)` dispersion for all `j<=J_n`.

This does not prove that the full characteristic function is large at `\theta_j`. Any decay may come from the first `j` transformed coordinates.

## N3-ANA-028: transformed-window dyadic kernel classification

Result class: **proved theorem**.

Let

\[
J_{n,q}
=
\left[
\left\lceil\frac{q-W_n-1}{2}\right\rceil,
\left\lfloor\frac{q-1}{2}\right\rfloor
\right]\cap\mathbb Z,
\qquad
N_{n,q}=|J_{n,q}|.
\]

### Case 1: `rho_n` odd

Then

\[
W_n=\frac{2^{\rho_n}-5}{3},
\qquad
N_{n,q}=\frac{2^{\rho_n-1}-1}{3},
\]

for both target parities. This length is odd.

### Case 2: `rho_n` even and `q` even

Then

\[
W_n=\frac{2^{\rho_n}-4}{3},
\qquad
N_{n,q}=\frac{W_n}{2}
=2\frac{2^{\rho_n-2}-1}{3},
\]

so

\[
v_2(N_{n,q})=1.
\]

### Case 3: `rho_n` even and `q` odd

Then

\[
N_{n,q}=\frac{W_n}{2}+1
=\frac{2^{\rho_n-1}+1}{3},
\]

which is odd.

Consequently,

\[
v_2(N_{n,q})\in\{0,1\}.
\]

Let

\[
\widetilde K_{n,q}(\theta)
=
\sum_{x\in J_{n,q}}e^{ix\theta}.
\]

At a reduced dyadic frequency

\[
\theta=\frac{2\pi a}{2^d},
\qquad
a\text{ odd},
\]

one has

\[
\widetilde K_{n,q}(\theta)=0
\quad\Longleftrightarrow\quad
2^d\mid N_{n,q}.
\]

Therefore no reduced dyadic frequency of denominator at least `4` is an exact transformed-kernel zero. At `\pi`, the kernel vanishes exactly when `\rho_n` and `q` are both even.

### Proof

The formulas for `W_n` follow from the two residues of powers of `2` modulo `3`.

When `\rho_n` is odd, the original interval has even length `W_n+1`, so exactly half its integers are odd.

When `\rho_n` is even, `W_n` is even and the original interval has odd length. If `q` is even, both endpoints are even and the number of odd integers is `W_n/2`. If `q` is odd, both endpoints are odd and the number is `W_n/2+1`.

For a consecutive interval of `N` integers, its Fourier kernel differs by a unit-modulus phase from

\[
1+e^{i\theta}+\cdots+e^{i(N-1)\theta}.
\]

At a reduced dyadic frequency of denominator `2^d`, this geometric sum vanishes exactly when `2^d` divides `N`. `QED`

## Combined route consequence

The odd-lattice normalization removes the forced original parity twin, but the transformed law retains an exact dyadic finite-prefix skeleton.

At `\theta_j`:

1. every layer after `j+1` is exactly invisible;
2. the matching layer is almost a pure sign for `j<=J_n`;
3. the complete transformed tail contributes only `O(1/n)` dispersion;
4. the transformed interval kernel does not cancel the point for `j>=2`.

A successful transformed Fourier theorem must control

\[
\prod_{t=1}^{j}
\widetilde\phi_{t,n,q}(\theta)
\]

in neighborhoods of the dyadic ladder frequencies. It cannot obtain a uniform minor-arc bound merely by accumulating dispersion from later layers.

The nonvanishing of a kernel at isolated points is not itself an integral obstruction. The next result must be neighborhood-sensitive and matched to the exact weighted inversion inequality.

## Claim boundary

This checkpoint does not prove:

- transformed local-window positivity;
- a transformed weighted Fourier inequality;
- target-local collision control;
- quotient occupancy;
- the factorial half-range theorem;
- Erdős Problem 18.