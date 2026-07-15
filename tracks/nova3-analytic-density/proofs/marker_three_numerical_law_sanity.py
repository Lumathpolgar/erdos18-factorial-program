#!/usr/bin/env python3
"""Finite checks for N3-ANA-017 through N3-ANA-019.

These calculations verify exact finite supports and numerical consequences for
small factorials. They are finite certificates or computational evidence only.
The symbolic theorems are in MARKER_THREE_NUMERICAL_LAW_FOUNDATIONS.md.

Python: 3.10+
Dependencies: standard library only.
"""

from __future__ import annotations

import cmath
import math
from functools import reduce
from math import gcd
from typing import Sequence


def factorization(n: int) -> list[tuple[int, int]]:
    factors: list[tuple[int, int]] = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            exponent = 0
            while n % p == 0:
                n //= p
                exponent += 1
            factors.append((p, exponent))
        p = 3 if p == 2 else p + 2
    if n > 1:
        factors.append((n, 1))
    return factors


def divisors_from_factorization(factors: Sequence[tuple[int, int]]) -> list[int]:
    divisors = [1]
    for p, exponent in factors:
        base = tuple(divisors)
        multiplier = 1
        for _ in range(exponent):
            multiplier *= p
            divisors.extend(d * multiplier for d in base)
    return sorted(divisors)


def marker_three_layers(n: int) -> tuple[int, int, int, list[list[int]]]:
    factorial = math.factorial(n)
    x_n = math.isqrt(factorial)
    y_n = x_n // 3

    odd_part = factorial
    while odd_part % 2 == 0:
        odd_part //= 2
    d_n = odd_part // 3

    divisors = divisors_from_factorization(factorization(d_n))
    m_n = math.ceil(16.0 * math.log(n) ** 2)
    r_n = math.ceil(4.0 * math.log(n))
    w_n = ((1 << r_n) - 3) // 3

    layers: list[list[int]] = []
    for t in range(1, m_n + 1):
        scale = 1 << (t - 1)
        values = [scale * u for u in divisors if scale * u <= y_n]
        if not values:
            break
        layers.append(values)

    return y_n, w_n, m_n, layers


def layer_distribution(
    values: Sequence[int], tilt: float
) -> tuple[list[int], list[float]]:
    support = [0, *values]
    exponents = [tilt * value for value in support]
    maximum = max(exponents)
    weights = [math.exp(exponent - maximum) for exponent in exponents]
    normalizer = math.fsum(weights)
    probabilities = [weight / normalizer for weight in weights]
    return support, probabilities


def total_moments(layers: Sequence[Sequence[int]], tilt: float) -> tuple[float, float]:
    total_mean = 0.0
    total_variance = 0.0
    for values in layers:
        support, probabilities = layer_distribution(values, tilt)
        mean = math.fsum(p * value for p, value in zip(probabilities, support))
        variance = math.fsum(
            p * (value - mean) ** 2
            for p, value in zip(probabilities, support)
        )
        total_mean += mean
        total_variance += variance
    return total_mean, total_variance


def solve_tilt(layers: Sequence[Sequence[int]], target: float) -> float:
    lower = -1.0
    upper = 1.0

    while total_moments(layers, lower)[0] > target:
        lower *= 2.0
    while total_moments(layers, upper)[0] < target:
        upper *= 2.0

    for _ in range(120):
        midpoint = (lower + upper) / 2.0
        if total_moments(layers, midpoint)[0] < target:
            lower = midpoint
        else:
            upper = midpoint
    return (lower + upper) / 2.0


def characteristic_function(
    layers: Sequence[Sequence[int]], tilt: float, theta: float
) -> complex:
    product = 1.0 + 0.0j
    for values in layers:
        support, probabilities = layer_distribution(values, tilt)
        factor = sum(
            p * cmath.exp(1j * theta * value)
            for p, value in zip(probabilities, support)
        )
        product *= factor
    return product


def support_span(layers: Sequence[Sequence[int]]) -> int:
    differences: list[int] = []
    for values in layers:
        differences.extend(values)
    return reduce(gcd, differences, 0)


def finite_model_audit(n: int) -> list[tuple[int, float, float, float]]:
    y_n, w_n, _, layers = marker_three_layers(n)
    if not layers:
        raise AssertionError(f"no active layers for n={n}")
    if 1 not in layers[0]:
        raise AssertionError(f"first layer does not contain 1 for n={n}")
    if support_span(layers) != 1:
        raise AssertionError(f"support span is not one for n={n}")

    support_maximum = sum(max(layer) for layer in layers)
    if support_maximum <= y_n:
        raise AssertionError(f"endpoint support does not cross Y_n for n={n}")

    target_candidates = sorted(
        {
            w_n + 1,
            min(y_n, w_n + 1000),
            y_n,
        }
    )

    rows: list[tuple[int, float, float, float]] = []
    for q in target_candidates:
        if not (w_n < q <= y_n):
            continue
        center = q - w_n / 2.0
        tilt = solve_tilt(layers, center)
        mean, variance = total_moments(layers, tilt)

        if not math.isclose(mean, center, rel_tol=1e-10, abs_tol=1e-7):
            raise AssertionError(
                f"tilt centering failed for n={n}, q={q}: {mean} vs {center}"
            )
        if variance <= 0.0:
            raise AssertionError(f"variance collapsed for n={n}, q={q}")

        for theta in (-math.pi, -1.0, -0.25, 0.25, 1.0, math.pi):
            modulus = abs(characteristic_function(layers, tilt, theta))
            if modulus >= 1.0 - 1e-12:
                raise AssertionError(
                    f"unexpected sampled nonzero resonance for n={n}, q={q}, theta={theta}"
                )

        rows.append((q, tilt, mean, variance))

    # Endpoint concentration evidence. The theorem uses the exact limit as
    # |lambda|->infinity; the large finite values below merely exercise it.
    test_theta = 0.7
    negative_modulus = abs(characteristic_function(layers, -20.0, test_theta))
    positive_modulus = abs(characteristic_function(layers, 1.0, test_theta))
    if negative_modulus < 0.999999:
        raise AssertionError(f"negative endpoint concentration not visible for n={n}")
    if positive_modulus < 0.999999:
        raise AssertionError(f"positive endpoint concentration not visible for n={n}")

    return rows


def main() -> None:
    for n in (12, 15):
        rows = finite_model_audit(n)
        print(f"n={n}")
        print("q tilt mean variance")
        for q, tilt, mean, variance in rows:
            print(f"{q:8d} {tilt: .12e} {mean: .6f} {variance: .6f}")
        print()

    print("PASS: marker-three numerical-law finite checks completed")
    print("STATUS: exact supports and span checked for n in {12,15}")
    print("STATUS: tilt and resonance grids are finite computational evidence")
    print("STATUS: symbolic endpoint-uniform obstruction is proved separately")


if __name__ == "__main__":
    main()
