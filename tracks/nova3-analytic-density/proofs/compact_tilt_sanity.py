#!/usr/bin/env python3
"""Deterministic checks for compact-tilt top-prime-band theorems.

Result classes:
- exhaustive finite certificate for the explicitly enumerated small cases;
- computational evidence for selected large n.

This script does not prove the asymptotic theorem.
Python: 3.10+
Dependencies: standard library only
"""

from __future__ import annotations

import itertools
import math
from dataclasses import dataclass
from typing import Iterable, Sequence


@dataclass(frozen=True)
class TiltRow:
    n: int
    theta: float
    band_size: int
    variance: float
    variance_lower_bound: float
    berry_ratio: float
    crude_ratio: float


def primes_up_to(n: int) -> list[int]:
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(n) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def top_band(n: int, primes: Sequence[int]) -> list[int]:
    return [p for p in primes if n / 2 < p <= n]


def bernoulli_parameters(p: int, theta: float) -> tuple[float, float]:
    q = p ** (-abs(theta))
    success = 1.0 / (1.0 + q) if theta >= 0 else q / (1.0 + q)
    variance = q / (1.0 + q) ** 2
    return success, variance


def formula_moments(
    n: int, theta: float, primes: Sequence[int]
) -> tuple[int, float, float, float]:
    band = top_band(n, primes)
    mean = 0.0
    variance = 0.0
    third_absolute_sum = 0.0
    for p in band:
        success, coordinate_variance = bernoulli_parameters(p, theta)
        logp = math.log(p)
        mean += success * logp
        variance += coordinate_variance * logp * logp
        third_absolute_sum += (
            success * (1.0 - success) ** 3
            + (1.0 - success) * success**3
        ) * logp**3
    return len(band), mean, variance, third_absolute_sum


def enumerated_moments(
    n: int, theta: float, primes: Sequence[int]
) -> tuple[float, float]:
    band = top_band(n, primes)
    states: list[tuple[float, float]] = []
    normalizer = 1.0
    for p in band:
        normalizer *= 1.0 + p**theta

    for bits in itertools.product((0, 1), repeat=len(band)):
        log_value = math.fsum(bit * math.log(p) for bit, p in zip(bits, band))
        weight = math.prod((p**theta if bit else 1.0) for bit, p in zip(bits, band))
        states.append((log_value, weight / normalizer))

    total_probability = math.fsum(weight for _, weight in states)
    if not math.isclose(total_probability, 1.0, rel_tol=1e-12, abs_tol=1e-12):
        raise AssertionError(f"probability normalization failed for n={n}, theta={theta}")

    mean = math.fsum(value * weight for value, weight in states)
    variance = math.fsum((value - mean) ** 2 * weight for value, weight in states)
    return mean, variance


def exhaustive_small_case_audit() -> None:
    max_n = 43
    primes = primes_up_to(max_n)
    thetas = (-0.75, -0.25, 0.0, 0.25, 0.75)
    for n in (11, 17, 29, 43):
        band = top_band(n, primes)
        if len(band) > 12:
            raise AssertionError("small exhaustive band unexpectedly large")
        for theta in thetas:
            _, formula_mean, formula_variance, rho = formula_moments(n, theta, primes)
            enum_mean, enum_variance = enumerated_moments(n, theta, primes)
            if not math.isclose(enum_mean, formula_mean, rel_tol=1e-12, abs_tol=1e-12):
                raise AssertionError(f"mean mismatch for n={n}, theta={theta}")
            if not math.isclose(
                enum_variance, formula_variance, rel_tol=1e-12, abs_tol=1e-12
            ):
                raise AssertionError(f"variance mismatch for n={n}, theta={theta}")
            if rho > math.log(n) * formula_variance * (1.0 + 1e-12):
                raise AssertionError(f"third-moment ceiling failed for n={n}, theta={theta}")


def large_scale_rows(
    ns: Iterable[int], theta0s: Iterable[float]
) -> tuple[list[TiltRow], list[tuple[int, float, float, float]]]:
    ns = tuple(ns)
    theta0s = tuple(theta0s)
    primes = primes_up_to(max(ns))
    rows: list[TiltRow] = []
    boundary_rows: list[tuple[int, float, float, float]] = []

    for n in ns:
        band = top_band(n, primes)
        if len(band) < n / (3.0 * math.log(n)):
            raise AssertionError(f"prime interval lower bound failed at n={n}")

        for theta0 in theta0s:
            for theta in (-theta0, 0.0, theta0):
                m, _, variance, rho = formula_moments(n, theta, primes)
                lower = n ** (1.0 - theta0) * math.log(n) / 48.0
                if variance + 1e-12 < lower:
                    raise AssertionError(
                        f"variance lower bound failed at n={n}, theta={theta}"
                    )
                if rho > math.log(n) * variance * (1.0 + 1e-12):
                    raise AssertionError(
                        f"third-moment ceiling failed at n={n}, theta={theta}"
                    )
                rows.append(
                    TiltRow(
                        n=n,
                        theta=theta,
                        band_size=m,
                        variance=variance,
                        variance_lower_bound=lower,
                        berry_ratio=rho / variance**1.5,
                        crude_ratio=math.log(n) / math.sqrt(variance),
                    )
                )

        _, _, variance_one, _ = formula_moments(n, 1.0, primes)
        expected_deficit = math.fsum(math.log(p) / (1.0 + p) for p in band)
        log_all_favored = math.fsum(math.log(p / (1.0 + p)) for p in band)
        exact_exception_probability = -math.expm1(log_all_favored)
        union_bound = 2.0 * len(band) / n
        if exact_exception_probability > union_bound + 1e-12:
            raise AssertionError(f"unit-tilt union bound failed at n={n}")
        boundary_rows.append(
            (
                n,
                exact_exception_probability,
                union_bound,
                expected_deficit / math.sqrt(variance_one),
            )
        )

    return rows, boundary_rows


def print_rows(rows: Sequence[TiltRow]) -> None:
    print("n theta m variance lower_bound rho/B^3 logn/B")
    for row in rows:
        print(
            f"{row.n:7d} {row.theta:6.2f} {row.band_size:6d} "
            f"{row.variance:13.6f} {row.variance_lower_bound:12.6f} "
            f"{row.berry_ratio:9.6f} {row.crude_ratio:9.6f}"
        )


def print_boundary(rows: Sequence[tuple[int, float, float, float]]) -> None:
    print("\nunit-tilt freezing evidence")
    print("n exact_P(any minority) union_bound centered_favored_atom")
    for n, exact_exception, union_bound, centered_atom in rows:
        print(
            f"{n:7d} {exact_exception:21.12f} "
            f"{union_bound:11.9f} {centered_atom:22.12f}"
        )


def main() -> None:
    exhaustive_small_case_audit()
    rows, boundary_rows = large_scale_rows(
        ns=(120368, 200000, 500000, 1000000),
        theta0s=(0.25, 0.50, 0.75, 0.90),
    )
    print_rows(rows)
    print_boundary(boundary_rows)
    print("\nPASS: compact-tilt deterministic checks completed")
    print("STATUS: exhaustive finite certificate for listed small n and theta grid")
    print("STATUS: selected large-n rows are computational evidence only")


if __name__ == "__main__":
    main()
