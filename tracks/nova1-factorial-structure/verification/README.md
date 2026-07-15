# Nova 1 Structural Verification

## Command

```text
python tracks/nova1-factorial-structure/verification/structural_sanity.py
```

## Checks

The script independently verifies finite instances of:

1. Legendre's valuation formula and the digit-sum identity;
2. exact quotient-band valuations for primes above `sqrt(n)`;
3. binary correction legality and exact representation;
4. 2-adic marker distinctness and palette disjointness;
5. complement-pair legality and numerical distinctness;
6. the high-prime subset-product menu count;
7. the downward-window counting inequality on exhaustive tiny cases.

## Recorded run

Environment:

- Python 3
- standard library only
- deterministic, no random seed

Result:

```text
PASS test_legendre_and_bands
PASS test_binary_palette
PASS test_marker_distinctness
PASS test_complement_pairing
PASS test_high_prime_menu_count
PASS test_window_counting_lemma
PASS all 6 structural sanity checks
```

## Evidence status

Result label: **finite certificate** for the exact tested ranges.

The run is not evidence for the open asymptotic rainbow occupancy theorem.