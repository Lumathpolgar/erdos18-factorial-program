# Transformed Dyadic Checkpoint

Checkpoint ID: `N3-CHK-008`

Date: 2026-07-16

Branch: `nova/analytic-density`

## Imported current heads

- Nova 1: `nova/factorial-structure@1b81ec74f907d57d520bcf6c51f2e6e71f0474a7`
- Nova 2: `nova/additive-occupancy@e443674f86b2ee3c7037ac94ee47f6b8a4b3b29f`

## New theorem package

- `N3-ANA-026`: exact transformed dyadic finite-prefix factorization
- `N3-ANA-027`: matching-layer near-pure sign and transformed tail-dispersion collapse
- `N3-ANA-028`: exact transformed-window dyadic kernel classification
- `N3-FIN-008`: finite transformed dyadic verifier
- `N3-COMP-007`: selected safe-depth, modulus, dispersion, and window-valuation rows

## Core commits

- corrected proof: `bee2042c84aab681b5ddd8681a39d3808ef4a1fe`
- original proof milestone: `75d022af373a9bdba5307a3e0188c81a69ee8931`
- verifier: `192fb56e3efeb2c1bd4b1e9e6f3476356ac62fa3`
- theorem registry: `2e04b4ff0dcc28f6697c37de3268c9d555ab7077`
- status: `5ceda46868bccda804fa8e12a21bbb906917b9da`
- open requirements: `88d4987cb5ce31d43314541800f7a8364861fa8e`
- preferred route: `61c37f694ab6c7f94e60a11c390d397483da1002`
- candidate correction: `71fe783f13264cb127465fa182d285979d24997e`
- README: `3f16526967e9136d57a0b77980023a33dfb5e0b1`
- Nova 2 handoff: `5913db6656cd6cea4b89da974b35eca68b26aaf5`
- Nova 4 handoff: `d00de8dd80c8b845956c56e366ad88eb37a60089`

The correction commit repairs and tightens proof presentation without changing the theorem statements.

## Verification command

```text
python3 tracks/nova3-analytic-density/proofs/transformed_dyadic_sanity.py
```

The committed script was reproduced and run before upload. It returned:

```text
PASS exact transformed dyadic checks n=12, layers=13
PASS exact transformed dyadic checks n=15, layers=19
PASS transformed dyadic resonance ladder sanity
```

## Selected exact scale output

At `n=120368`:

- `rho_n=47`
- `M_n=2190`
- `J_n=2165`
- excluded top scales: `24`
- matching-layer modulus floor: `0.999926137628`
- tail-dispersion ceiling: `7.3862371786e-05`
- transformed window length: `23456248059221`
- transformed window 2-adic valuation: `0`

## Exact route decision

The transformed dyadic ladder does not admit a many-tail-layers dispersion proof.

At `theta_j=pi/2^(j-1)`:

1. every layer after `j+1` is exactly invisible;
2. the matching layer is almost a pure sign through all but `O(log log n)` top scales;
3. the complete transformed tail contributes only `O(1/n)` dispersion;
4. the transformed interval kernel has no exact zero for denominator `4` or higher.

The active object is now the prefix characteristic

\[
\prod_{t=1}^{j}
\widetilde\phi_{t,n,q}(\theta)
\]

in neighborhoods of each dyadic ladder point.

## Claim boundary

This checkpoint does not prove transformed local-window positivity, the strict transformed weighted Fourier inequality, quotient occupancy, the factorial half-range theorem, or Erdős Problem 18.