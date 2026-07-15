# Handoff to Nova 3

Handoff ID: `N1-HO-N3-001`

Sending track: Nova 1, Factorial Structure and Reduction

Receiving track: Nova 3, Analytic Divisor Density

Date: 2026-07-15

Result status: **conditional theorem** request

Theorem or object IDs: `N1-STR-009`, `N1-REQ-N3-001-A`

## Exact theorem request

Prove an effective prime-interval theorem of the following exact form:

> There exists an explicit integer `n_3` such that, for every integer `n>=n_3`,
> \[
> \pi(n)-\pi(n/2)\ge\frac{n}{3\log n}.
> \]

All logarithms are natural. The proof may use an external prime-number theorem estimate only if the source, exact theorem statement, hypotheses, constants, and compatibility with this interval are recorded.

## Required menu conclusion

For every `n>=n_3`, define

\[
X_n=\lfloor\sqrt{n!}\rfloor,
\qquad
V_n=v_2(n!),
\]

\[
r_n=\lceil4\log n\rceil,
\qquad
M_n=\lceil16(\log n)^2\rceil,
\qquad
 e_t=r_n+t.
\]

For every sufficiently large `n` with

\[
e_{M_n}\le\lfloor V_n/2\rfloor-1,
\]

define

\[
U_t(n)=
\left\{
 u\in\mathbb Z_{>0}:
 u\mid n!,\ u\text{ odd},\ u>1,\ 2^{e_t}u\le X_n
\right\}.
\]

Using the prime-interval theorem and the proved high-prime subset-product argument, certify the explicit lower bound

\[
|U_t(n)|
\ge
2^{\pi(n)-\pi(n/2)-1}-1
\ge
2^{n/(3\log n)-1}-1
\]

for every `1<=t<=M_n` and every integer `n>=n_4`, where `n_4` is explicit and incorporates the address-range condition.

Then verify that, for every `n>=n_5` with explicit `n_5`,

\[
\prod_{t=1}^{M_n}(|U_t(n)|+1)\,2^{r_n}
\ge X_n+1.
\]

This final inequality is only a necessary capacity certificate.

## Variables and ranges

- `n`: every integer `n>=n_5`;
- `t`: every integer `1<=t<=M_n`;
- `pi(y)`: the number of primes at most the real number `y`;
- `X_n`, `V_n`, `r_n`, `M_n`, `e_t`, and `U_t(n)`: exactly as defined above.

## Required outputs

1. a proved prime-interval bound with explicit threshold;
2. a checked derivation of the uniform menu lower bound;
3. a checked derivation of the profile-capacity inequality;
4. all constants and thresholds used;
5. a statement of which estimates are external and which are proved in the artifact.

## Dependencies

- `proofs/VALUATION_BUDGET_LEMMAS.md`
- `proofs/HIGH_PRIME_MENU_CAPACITY.md`
- `proofs/COUNTING_CAPACITY_OBSTRUCTION.md`
- `proofs/MENU_ENTROPY_REQUIREMENT.md`
- `PREFERRED_ROUTE.md`

## Verification command

Provide a symbolic proof artifact and, if explicit numerical thresholds are obtained by computation, provide deterministic code that verifies every integer or interval required below the asymptotic threshold.

## Known failure modes

- quoting `pi(n)~n/log n` without extracting a valid explicit interval bound;
- using a threshold that is not uniform in `n`;
- overlooking the floor in `X_n`;
- failing to enforce `e_{M_n}<=floor(V_n/2)-1`;
- confusing formal profile capacity with distinct-sum occupancy.

## What is not claimed

The requested theorem does not prove additive coverage, maximum-gap control, or the factorial half-range theorem.

## Requested next action

Prove the exact statement or return the strongest explicit bound actually established, with a written check of whether it still makes the capacity inequality pass for the frozen constants `16` and `4`.