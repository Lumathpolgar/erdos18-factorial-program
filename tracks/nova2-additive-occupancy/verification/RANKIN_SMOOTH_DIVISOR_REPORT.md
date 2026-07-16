# Rankin Smooth-Divisor Replay Report

## Result

`N2-CMP-208`, **computational evidence**.

The committed verifier

`tracks/nova2-additive-occupancy/verification/rankin_smooth_divisor_sanity.py`

was executed with Python 3 and completed successfully.

## Recorded output

```text
PASS n=51 root=5.421357863321800448E-4 log10_ratio=-19.595351544212
PASS n=52 root=4.886080232946827492E-4 log10_ratio=-19.866236435260
PASS n=53 root=4.431912887571141921E-4 log10_ratio=-20.120452707393
PASS n=54 root=4.381316012309708998E-4 log10_ratio=-20.150372527332
PASS n=55 root=3.741841256267769778E-4 log10_ratio=-20.561487845627
PASS N2-ADD-127 Rankin lower bounds
PASS N2-ADD-128 carrier product
PASS N2-CMP-208 fixed-parameter rows
```

## Checks performed

- reconstructed the exact prime exponents of
  \[
  C_n=\frac{n!}{3\,2^{v_2(n!)}},
  \]
  for every `51<=n<=55`;
- evaluated each frozen finite Euler product at 80-decimal precision;
- checked every Rankin lower bound against the exact connected maximum;
- retained the stronger complement-median bound when applicable;
- reconstructed the six-layer carrier lower-bound product;
- matched every expected sixth-root and unrooted endpoint ratio within the committed fail-closed tolerances.

## Interpretation

The Rankin-median product improves the complement-median lower bound, but still falls below the exact endpoint requirement by approximately `10^19.6` through `10^20.6`.

This report is finite computational evidence only. It does not prove an asymptotic divisor estimate, quotient occupancy, the factorial half-range theorem, or Erdos Problem 18.
