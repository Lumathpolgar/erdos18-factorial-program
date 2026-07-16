#!/usr/bin/env python3
"""Deterministic sanity checks for Nova 3 factorial-divisor theorems.

Result class: finite certificates and computational evidence only.
This program does not prove any asymptotic theorem.

Python: 3.10+
Dependencies: standard library only
"""

from __future__ import annotations

import bisect
import math
from dataclasses import dataclass
from typing import Iterable, Sequence


@dataclass(frozen=True)
class ScaleRow:
    n: int
    log_tau_ratio: float
    variance_ratio: float
    share_2: float
    share_3: float
    effective_dimension: float


def primes_up_to(n: int) -> list[int]:
    if n < 2:
        return []
    sieve = bytearray(b"\x01") * (n + 1)
    sieve[0:2] = b"\x00\x00"
    limit = math.isqrt(n)
    for p in range(2, limit + 1):
        if sieve[p]:
            start = p * p
            sieve[start : n + 1 : p] = b"\x00" * (((n - start) // p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def valuation_factorial(n: int, p: int) -> int:
    total = 0
    power = p
    while power <= n:
        total += n // power
        if power > n // p:
            break
        power *= p
    return total


def factorial_factorization(n: int) -> list[tuple[int, int]]:
    return [(p, valuation_factorial(n, p)) for p in primes_up_to(n)]


def tau_from_factorization(factors: Sequence[tuple[int, int]]) -> int:
    result = 1
    for _, exponent in factors:
        result *= exponent + 1
    return result


def all_divisors(factors: Sequence[tuple[int, int]]) -> list[int]:
    divisors = [1]
    for p, exponent in factors:
        old = divisors
        divisors = []
        power = 1
        for _ in range(exponent + 1):
            divisors.extend(d * power for d in old)
            power *= p
    divisors.sort()
    if len(divisors) != len(set(divisors)):
        raise AssertionError("duplicate exact divisors generated")
    return divisors


def exact_log_moments(factors: Sequence[tuple[int, int]]) -> tuple[float, float]:
    mean = 0.0
    variance = 0.0
    for p, b in factors:
        logp = math.log(p)
        mean += 0.5 * b * logp
        variance += b * (b + 2) * logp * logp / 12.0
    return mean, variance


def empirical_log_moments(divisors: Sequence[int]) -> tuple[float, float]:
    logs = [math.log(d) for d in divisors]
    mean = math.fsum(logs) / len(logs)
    variance = math.fsum((x - mean) ** 2 for x in logs) / len(logs)
    return mean, variance


def assert_close(actual: float, expected: float, *, rel: float, abs_: float) -> None:
    if not math.isclose(actual, expected, rel_tol=rel, abs_tol=abs_):
        raise AssertionError(f"not close: actual={actual!r}, expected={expected!r}")


def exhaustive_moment_audit(max_n: int = 12) -> None:
    for n in range(2, max_n + 1):
        factors = factorial_factorization(n)
        divisors = all_divisors(factors)
        tau = tau_from_factorization(factors)
        if len(divisors) != tau:
            raise AssertionError(f"tau mismatch for n={n}")

        factorial_n = math.factorial(n)
        divisor_set = set(divisors)
        if any(factorial_n // d not in divisor_set for d in divisors):
            raise AssertionError(f"complement symmetry failed for n={n}")

        exact_mean, exact_variance = exact_log_moments(factors)
        empirical_mean, empirical_variance = empirical_log_moments(divisors)
        assert_close(empirical_mean, exact_mean, rel=1e-12, abs_=1e-12)
        assert_close(empirical_variance, exact_variance, rel=1e-12, abs_=1e-12)

        stirling_target = 0.5 * math.lgamma(n + 1)
        assert_close(exact_mean, stirling_target, rel=1e-12, abs_=1e-12)


def local_window_count(sorted_logs: Sequence[float], u: float, delta: float) -> int:
    epsilon = 2e-13 * max(1.0, abs(u), abs(u + delta))
    left = bisect.bisect_left(sorted_logs, u - epsilon)
    right = bisect.bisect_right(sorted_logs, u + delta + epsilon)
    return right - left


def exhaustive_local_ceiling_audit(max_n: int = 12) -> None:
    widths = (0.0, 0.25, 0.5, 1.0, 2.0)
    for n in range(2, max_n + 1):
        factors = factorial_factorization(n)
        divisors = all_divisors(factors)
        sorted_logs = [math.log(d) for d in divisors]
        tau = len(divisors)
        exponent_by_prime = dict(factors)

        for q, bq in factors:
            for delta in widths:
                coordinate_choices = math.floor(delta / math.log(q) + 1e-13) + 1
                ceiling = tau * coordinate_choices // (bq + 1)
                if tau * coordinate_choices % (bq + 1) != 0:
                    raise AssertionError("coordinate fiber count must divide tau")
                for u in sorted_logs:
                    actual = local_window_count(sorted_logs, u, delta)
                    if actual > ceiling:
                        raise AssertionError(
                            f"local ceiling failed: n={n}, q={q}, delta={delta}, "
                            f"u={u}, actual={actual}, ceiling={ceiling}"
                        )

        if exponent_by_prime[2] + 1 <= 0:
            raise AssertionError("invalid 2-adic valuation")


def log_tau_factorial(n: int, primes: Sequence[int] | None = None) -> float:
    ps = list(primes) if primes is not None else primes_up_to(n)
    return math.fsum(math.log(valuation_factorial(n, p) + 1) for p in ps)


def variance_contributions(n: int, primes: Sequence[int] | None = None) -> dict[int, float]:
    ps = list(primes) if primes is not None else primes_up_to(n)
    result: dict[int, float] = {}
    for p in ps:
        b = valuation_factorial(n, p)
        result[p] = b * (b + 2) * math.log(p) ** 2 / 12.0
    return result


def scale_row(n: int, primes: Sequence[int] | None = None) -> ScaleRow:
    ps = list(primes) if primes is not None else primes_up_to(n)
    log_tau = log_tau_factorial(n, ps)
    contributions = variance_contributions(n, ps)
    variance = math.fsum(contributions.values())
    square_sum = math.fsum(value * value for value in contributions.values())
    effective_dimension = variance * variance / square_sum
    return ScaleRow(
        n=n,
        log_tau_ratio=log_tau / (n / math.log(n)),
        variance_ratio=variance / (n * n),
        share_2=contributions.get(2, 0.0) / variance,
        share_3=contributions.get(3, 0.0) / variance,
        effective_dimension=effective_dimension,
    )


def high_prime_tail_ratio(n: int, y: int, primes: Sequence[int] | None = None) -> float:
    ps = list(primes) if primes is not None else primes_up_to(n)
    variance = 0.0
    maximum_span = 0.0
    for p in ps:
        if p <= y:
            continue
        b = valuation_factorial(n, p)
        logp = math.log(p)
        variance += b * (b + 2) * logp * logp / 12.0
        maximum_span = max(maximum_span, b * logp)
    if variance <= 0.0:
        raise AssertionError(f"empty high-prime tail for n={n}, y={y}")
    return maximum_span / math.sqrt(variance)


def asymptotic_sanity_table(ns: Iterable[int]) -> list[ScaleRow]:
    rows: list[ScaleRow] = []
    max_n = max(ns)
    all_primes = primes_up_to(max_n)
    for n in ns:
        ps = [p for p in all_primes if p <= n]
        rows.append(scale_row(n, ps))
    return rows


def print_table(rows: Sequence[ScaleRow]) -> None:
    print("n logtau/(n/logn) Var/n^2 share2 share3 deff")
    for row in rows:
        print(
            f"{row.n:5d} {row.log_tau_ratio:16.9f} "
            f"{row.variance_ratio:10.9f} {row.share_2:7.4f} "
            f"{row.share_3:7.4f} {row.effective_dimension:8.4f}"
        )


def main() -> None:
    exhaustive_moment_audit()
    exhaustive_local_ceiling_audit()

    ns = (50, 100, 200, 500, 1000, 2000, 5000, 10000)
    rows = asymptotic_sanity_table(ns)
    print_table(rows)

    primes_10000 = primes_up_to(10000)
    print("\nhigh-prime maximum-span / standard-deviation ratios")
    for n, cutoffs in ((1000, (5, 10, 20)), (5000, (10, 20, 50)), (10000, (10, 25, 50))):
        ps = [p for p in primes_10000 if p <= n]
        values = ", ".join(
            f"y={y}: {high_prime_tail_ratio(n, y, ps):.6f}" for y in cutoffs
        )
        print(f"n={n}: {values}")

    print("\nPASS: exhaustive finite checks and deterministic scale computations completed")
    print("STATUS: finite certificate for n<=12; larger tables are computational evidence")


if __name__ == "__main__":
    main()
