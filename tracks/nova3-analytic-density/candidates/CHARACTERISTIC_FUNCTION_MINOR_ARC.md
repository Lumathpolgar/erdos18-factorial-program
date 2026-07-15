# Candidate 3: Characteristic-Function and Minor-Arc Theorem

## Theorem contract

- Candidate ID: `N3-CAND-CF-001`
- Original unrestricted form: `disproved estimate`
- Corrected bounded-frequency form: `open`
- Intended consumer: Nova 2

For a frozen prime family `P=P(n)` and independent exponent variables under a specified product or tilted product measure, define

\[
T_P=\sum_{p\in P}(A_p-\mathbb E A_p)\log p,
\qquad
\phi_P(t)=\mathbb E e^{itT_P}.
\]

For uniform exponent variables with cap `b_p`, the exact coordinate modulus is

\[
\left|
\frac{\sin((b_p+1)t\log p/2)}{(b_p+1)\sin(t\log p/2)}
\right|.
\]

## Disproved unrestricted theorem

The following statement is false for every fixed `n>=3`:

> There exist `T<infinity` and `rho<1` such that the characteristic function of the full uniform divisor measure satisfies `|phi_n(t)|<=rho` for every `|t|>=T`.

By `N3-ANA-007`,

\[
\limsup_{|t|\to\infty}|\phi_n(t)|=1.
\]

The obstruction is simultaneous almost-periodic recurrence, not a common lattice span.

## Corrected candidate conclusion

Nova 2 must first freeze a maximum inversion frequency `R_n`. A viable theorem would have the following form.

Let `P(n)` contain primes in a stated interval, for example `(y,2y]`, with `y->infinity` and `2y<=sqrt n`. Let

\[
B_P^2=\operatorname{Var}(T_P),
\qquad
M_P=\max_{p\in P}b_p\log p.
\]

For fixed `epsilon>0`, prove an integrable estimate

\[
\int_{\epsilon/B_P\le |t|\le R_n}
|\phi_P(t)|\,dt
\le \mathcal E_n,
\]

where

\[
\mathcal E_n=o(1/B_P)
\]

or, for a target window of width `Delta`, the stronger scale-matched condition

\[
\mathcal E_n=o(\Delta/B_P).
\]

A pointwise substitute of the form

\[
|\phi_P(t)|
\le
\exp\left(-c\sum_{p\in P}
\min\{1,\|t\log p/(2\pi)\|^2b_p^2\}
\right)
\]

is exact up to absolute inequalities near the coordinate resonances, but it is useful only after proving a lower bound for the displayed phase-dispersion sum on the bounded frequency range.

## Exact hypotheses required

1. The prime family and exponent caps are explicit.
2. The probability measure is explicit, including any tilt.
3. The frequency interval is bounded above by a displayed `R_n`.
4. The estimate is matched to a stated smoothing kernel or inversion formula.
5. The constants do not depend on a target or frequency hidden inside the interval.
6. The result excludes major arcs where many `t log p` are simultaneously near multiples of `2 pi`, or it measures their total contribution separately.

## Known derivation

For real `x`, the elementary inequality

\[
\left|\frac{\sin((b+1)x/2)}{(b+1)\sin(x/2)}\right|
\le
\exp\{-c\min(1,b^2\|x/(2\pi)\|^2)\}
\]

holds with an absolute constant after reducing to the nearest multiple of `2 pi`. Multiplying coordinate bounds gives the proposed phase-dispersion envelope.

The unproved part is a uniform lower bound for the sum of phase dispersions over many prime logarithms throughout the inversion range.

## Strongest primary source that partially applies

Giuliano and Weber use characteristic-function methods for weighted Bernoulli models and demonstrate why a weak central limit theorem is inadequate for thin local events. Their theorem hypotheses are not automatically satisfied by the factorial exponent coordinates. No external minor-arc theorem has been found that supplies the required uniform phase-dispersion estimate for the logarithms of primes in the exact factorial model.

See `SOURCE_LEDGER.md`, entry `N3-SRC-007`.

## Exact missing step

Prove one of the following, with a frequency range supplied by Nova 2:

1. a deterministic lower bound on
   \[
   \sum_{p\in P}\min\{1,b_p^2\|t\log p/(2\pi)\|^2\};
   \]
2. a measure bound for the resonant frequency set;
3. an averaged Fourier estimate adequate for the chosen smoothing kernel;
4. a randomized or partitioned prime-family theorem that becomes deterministic after freezing a successful family.

## Falsification duties

- Reject any theorem stated for all unbounded frequencies.
- Do not replace nonlattice structure by quantitative Diophantine separation.
- Check whether the inversion cutoff exceeds the first simultaneous recurrence scale.
- Check whether a pointwise bound integrates to less than the desired local main term.
- Check hidden dependence on the chosen prime family.
- Distinguish characteristic-function decay of logarithmic divisor sizes from Fourier decay of additive divisor values.

## Feed to Nova 2

A proved bounded-frequency estimate can control the minor-arc contribution in a smoothed convolution or rainbow occupancy model. Nova 2 must specify whether its Fourier variable acts on logarithmic sizes or on additive divisor values. The present theorem concerns the former. No legal transfer between those two Fourier problems is automatic.
