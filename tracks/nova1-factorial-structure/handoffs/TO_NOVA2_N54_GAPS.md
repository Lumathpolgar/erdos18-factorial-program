# N1-HO-N2-008: n=54 Normalized Surplus and Record-Gap Request

## Classification

Result label: **conditional theorem** request.

## Exact source

- source branch: `nova/factorial-structure`;
- checkpoint source commit: `dac958b62ef069310901f5063dbf8bd6cbe3c0e3`;
- construction: `N1-CON-003`;
- finite certificate: `N1-FIN-009`;
- computational evidence: `N1-CMP-007`;
- open requirements: `N1-REQ-N2-003` and `N1-REQ-N2-005`.

## Exact finite result

Nova 1 certifies

\[
H_{54!}(\lfloor\sqrt{54!}\rfloor+1)\le22.
\]

Together with prior exact certificates,

\[
H_{n!}(\lfloor\sqrt{n!}\rfloor+1)\le22
\qquad(12\le n\le54).
\]

This is a **finite certificate** only.

At `n=54`, the exact connected-prefix sizes are

\[
63{,}547,
1{,}308{,}259,
14{,}197{,}074,
71{,}967{,}365,
185{,}071{,}301,
287{,}853{,}491.
\]

The exact normalized surplus is approximately

\[
\Gamma_{54}=92.27326436677728.
\]

The finite sequence

\[
\Gamma_{51},\Gamma_{52},\Gamma_{53},\Gamma_{54}
\]

is

\[
120.322026489,
97.645052132,
124.609364763,
92.273264367.
\]

It is non-monotone and must not be extrapolated.

## Record-gap diagnostic

For each blocked layer, let `D_t` be the exact threshold and `g_t` the first blocking record gap.

Across the twenty blocked layers for `51<=n<=54`,

\[
\max\frac{g_t}{D_t}
=
\frac{20891689328819250}{18870510190034037}
<1.108.
\]

The maximum occurs at `n=51`, layer `4`.

This is **computational evidence**, not a theorem.

## Requested receiver outcomes

Return exactly one of the following, with proof and exact hypotheses:

1. **proved theorem**: a uniform divisor record-gap bound strong enough to imply `Gamma_n>=1` for enough exact layers;
2. **proved theorem**: a contrary gap lower bound forcing `Gamma_n<1` eventually or infinitely often;
3. **conditional theorem**: an explicit record-gap hypothesis on divisors of
   \[
   D_n=\frac{n!}{3\cdot2^{v_2(n!)}}
   \]
   that implies the carrier entropy gate;
4. a narrower proved theorem identifying which layer range and cutoff regime can be controlled.

Do not promote the finite constant `1.108` to an asymptotic claim.

## Exact artifacts

- `verification/FULL_CORE_N54_REPORT.md`;
- `verification/full_core_n54_mitm_mask255.txt`;
- `verification/full_core_n54_mitm_mask223.txt`;
- `verification/connected_prefix_normalized_n51_n54.csv`;
- `verification/test_mitm_n54_partition.py`;
- `OPEN_REQUIREMENTS.md`.

## Claim boundary

The global quotient downward-window theorem, the uniform connected-prefix theorem, and Erdős Problem 18 remain open.
