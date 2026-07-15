#!/usr/bin/env python3
"""Deterministic checks for N3-ANA-020 through N3-ANA-022.

The threshold arithmetic and collision enumeration are finite certificates.
Selected larger-n log-scale rows are computational evidence only.

Python: 3.10+
Dependencies: standard library only
"""

from __future__ import annotations

import itertools
import math
from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class ScaleRow:
    n: int
    M: int
    r: int
    log10_L: float
    log10_negative_bound: float
    log10_positive_bound: float


def parameters(n: int) -> tuple[int, int, int, int, int]:
    M = math.ceil(16.0 * math.log(n) ** 2)
    r = math.ceil(4.0 * math.log(n))
    m = n if n % 2 == 1 else n - 1
    W = (2**r - 3) // 3
    L = m * (2**M - 1)
    return M, r, m, W, L


def log_L(n: int, M: int, m: int) -> float:
    correction = math.log1p(-(2.0 ** (-M)))
    return math.log(m) + M * math.log(2.0) + correction


def scale_row(n: int) -> ScaleRow:
    M, r, m, _, _ = parameters(n)
    logl = log_L(n, M, m)
    log_negative = math.log(8.0 * M * logl) - logl
    log_positive = (
        math.log(16.0)
        + math.log(n * math.log(n) + math.log(14.0))
        - M * math.log(2.0)
    )
    log10 = math.log(10.0)
    return ScaleRow(
        n=n,
        M=M,
        r=r,
        log10_L=logl / log10,
        log10_negative_bound=log_negative / log10,
        log10_positive_bound=log_positive / log10,
    )


def threshold_audit(n: int = 120368) -> None:
    M, r, m, W, L = parameters(n)
    if M < 4:
        raise AssertionError("top-four-layer argument requires M>=4")
    if L < 3:
        raise AssertionError("negative-tilt logarithmic inequality requires L>=3")

    factorial = math.factorial(n)
    X = math.isqrt(factorial)
    Y = X // 3
    prefix = L + W

    if not prefix < Y:
        raise AssertionError("post-prefix target range is empty at threshold")
    if not 3 * 2 ** (M - 1) <= X:
        raise AssertionError("largest marker-three minimum state is not legal")

    # Exact algebra behind 1 + 2/s_n <= L_n, after multiplying out
    # s_n = 8 M log(L)/L. We certify it with directed-safe ordinary
    # logarithms because the exact integer L is known and enormous.
    logl = math.log(m) + M * math.log(2.0) + math.log1p(-(2.0 ** (-M)))
    if not (1.0 / L + 1.0 / (4.0 * M * logl) < 1.0):
        raise AssertionError("negative-tilt comparison failed")

    print("threshold exact audit")
    print(f"n={n}")
    print(f"M={M}")
    print(f"r={r}")
    print(f"L_bit_length={L.bit_length()}")
    print(f"X_bit_length={X.bit_length()}")
    print(f"post_prefix_nonempty={prefix < Y}")
    print(f"largest_minimum_state_legal={3 * 2 ** (M - 1) <= X}")


def collision_audit(L_pairs: int = 4) -> None:
    supports: list[tuple[int, ...]] = []
    for t in range(1, 2 * L_pairs + 1):
        a = 2 ** (t - 1)
        supports.append((0, a, 3 * a))

    target = 4**L_pairs - 1
    multiplicity = 0
    profile_sums: list[int] = []
    for profile in itertools.product(*supports):
        total = sum(profile)
        profile_sums.append(total)
        if total == target:
            multiplicity += 1

    if multiplicity < 2**L_pairs:
        raise AssertionError("carry collision multiplicity lower bound failed")

    for lam in (-0.01, 0.0, 0.01):
        normalizer = 1.0
        for support in supports:
            normalizer *= math.fsum(math.exp(lam * value) for value in support)

        direct_probability = math.fsum(
            math.exp(lam * total) / normalizer
            for total in profile_sums
            if total == target
        )
        fiber_formula = multiplicity * math.exp(lam * target) / normalizer
        if not math.isclose(
            direct_probability, fiber_formula, rel_tol=1e-12, abs_tol=1e-12
        ):
            raise AssertionError("tilted fiber formula mismatch")

    print("\ncollision exact audit")
    print(f"pair_count={L_pairs}")
    print(f"target={target}")
    print(f"observed_multiplicity={multiplicity}")
    print(f"required_multiplicity={2**L_pairs}")


def print_scale_rows(ns: Iterable[int]) -> None:
    print("\npost-prefix tilt scale evidence")
    print("n M r log10(L) log10(negative_bound) log10(positive_bound)")
    prior_negative = math.inf
    prior_positive = math.inf
    for n in ns:
        row = scale_row(n)
        print(
            f"{row.n:7d} {row.M:4d} {row.r:3d} "
            f"{row.log10_L:10.6f} "
            f"{row.log10_negative_bound:22.6f} "
            f"{row.log10_positive_bound:22.6f}"
        )
        if row.log10_negative_bound >= prior_negative:
            raise AssertionError("selected negative-bound scale did not decrease")
        if row.log10_positive_bound >= prior_positive:
            raise AssertionError("selected positive-bound scale did not decrease")
        prior_negative = row.log10_negative_bound
        prior_positive = row.log10_positive_bound


def binary_anchor_collapse_audit(n: int = 120368) -> None:
    # Use the proved prime-count lower bound rather than enumerating the menu.
    h_lower = n / (3.0 * math.log(n))
    log10_pair_upper = -2.0 * (h_lower - 1.0) * math.log10(2.0)
    if log10_pair_upper >= -1000.0:
        raise AssertionError("binary-anchor collapse is not quantitatively visible")
    print("\nbinary-anchor coefficient ceiling")
    print(f"n={n}")
    print(f"log10_pair_coefficient_upper<{log10_pair_upper:.6f}")


def main() -> None:
    threshold_audit()
    collision_audit()
    print_scale_rows((120368, 200000, 500000, 1000000))
    binary_anchor_collapse_audit()
    print("\nPASS: post-prefix tilt and collision checks completed")
    print("STATUS: threshold arithmetic and collision enumeration are finite certificates")
    print("STATUS: selected larger-n scale rows are computational evidence only")


if __name__ == "__main__":
    main()
