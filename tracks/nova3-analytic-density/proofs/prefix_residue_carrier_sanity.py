#!/usr/bin/env python3
"""Finite and scale checks for N3-ANA-029 through N3-ANA-031."""

from __future__ import annotations

import math
from typing import Set


def carrier_sums(j: int) -> Set[int]:
    if j < 1:
        raise ValueError("j must be positive")
    sums = {0, 1}
    for t in range(2, j + 1):
        a = 2 ** (t - 2)
        sums = {x + y for x in sums for y in (0, a, 3 * a)}
    return sums


def check_interval_carrier(max_j: int = 18) -> None:
    for j in range(1, max_j + 1):
        sums = carrier_sums(j)
        expected_max = 3 * 2 ** (j - 1) - 2
        expected = set(range(expected_max + 1))
        assert sums == expected
        residues = {x % (2**j) for x in sums}
        assert residues == set(range(2**j))
        print(
            "PASS carrier interval",
            f"j={j}",
            f"max={expected_max}",
            f"profiles={2 * 3 ** (j - 1)}",
        )


def log_scales(n: int) -> tuple[int, int, float, float, float]:
    M = math.ceil(16 * math.log(n) ** 2)
    m = n if n % 2 else n - 1
    k = (m + 1) // 2

    logL = math.log(m) + M * math.log(2) + math.log1p(-(2.0 ** (-M)))
    log_negative = math.log(16 * M * logL) - logL
    log_positive = math.log(32 * (n * math.log(n) + math.log(14))) - M * math.log(2)
    log_delta = max(log_negative, log_positive)

    R = min(M, math.floor(2 - (log_delta + math.log(m)) / math.log(2)))
    assert R >= 2
    assert log_delta + math.log(m) + (R - 2) * math.log(2) <= 1e-12
    if R < M:
        assert log_delta + math.log(m) + (R - 1) * math.log(2) > -1e-12

    log_carrier = (
        math.log(2 * math.e**2 / k)
        + (R - 1) * math.log(3 * math.e**2 / (k + 1))
    )
    return M, R, log_delta / math.log(10), log_carrier / math.log(10), 3 * math.e**2 / (k + 1)


def check_large_scales() -> None:
    expected = {
        120368: (2190, 2149),
        200000: (2384, 2342),
        500000: (2756, 2711),
        1000000: (3054, 3007),
    }

    for n, pair in expected.items():
        M, R, log10_delta, log10_mass, later_factor = log_scales(n)
        assert (M, R) == pair
        assert 0 < later_factor < 1
        assert log10_mass < -7000
        print(
            "SCALE",
            f"n={n}",
            f"M={M}",
            f"R={R}",
            f"excluded_top_scales={M-R}",
            f"log10_delta={log10_delta:.12f}",
            f"later_carrier_factor={later_factor:.12g}",
            f"log10_carrier_mass={log10_mass:.12f}",
        )


def main() -> None:
    check_interval_carrier()
    check_large_scales()
    print("PASS prefix residue carrier sanity")


if __name__ == "__main__":
    main()
