#!/usr/bin/env python3
"""Deterministic finite checks for N1-STR-019, N1-STR-020, and N1-RED-006.

Evidence status: finite certificate only.
"""

from __future__ import annotations

import math
from typing import Iterable


def primes_up_to(n: int) -> list[int]:
    sieve = [True] * (n + 1)
    if n >= 0:
        sieve[0] = False
    if n >= 1:
        sieve[1] = False
    for p in range(2, math.isqrt(n) + 1):
        if sieve[p]:
            for multiple in range(p * p, n + 1, p):
                sieve[multiple] = False
    return [p for p in range(2, n + 1) if sieve[p]]


def factorial_valuation(n: int, p: int) -> int:
    total = 0
    q = n
    while q:
        q //= p
        total += q
    return total


def divisors_from_factorization(factors: Iterable[tuple[int, int]]) -> list[int]:
    divisors = [1]
    for p, exponent in factors:
        old = list(divisors)
        divisors = []
        power = 1
        for _ in range(exponent + 1):
            divisors.extend(power * d for d in old)
            power *= p
    return sorted(divisors)


def odd_reserved_core_divisors(n: int) -> list[int]:
    factors: list[tuple[int, int]] = []
    for p in primes_up_to(n):
        if p == 2:
            continue
        exponent = factorial_valuation(n, p)
        if p == 3:
            exponent -= 1
        if exponent > 0:
            factors.append((p, exponent))
    return divisors_from_factorization(factors)


def largest_at_most(sorted_values: list[int], cutoff: int) -> int:
    lo = 0
    hi = len(sorted_values)
    while lo < hi:
        mid = (lo + hi) // 2
        if sorted_values[mid] <= cutoff:
            lo = mid + 1
        else:
            hi = mid
    if lo == 0:
        raise AssertionError(f"no positive divisor at most cutoff={cutoff}")
    return sorted_values[lo - 1]


def test_three_density() -> None:
    for n in range(6, 21):
        divisors = odd_reserved_core_divisors(n)
        for left, right in zip(divisors, divisors[1:]):
            assert right <= 3 * left, (n, left, right)


def endpoint_terms(n: int) -> tuple[int, list[int]]:
    factorial = math.factorial(n)
    x_n = math.isqrt(factorial)
    quotient_endpoint = x_n // 3
    divisors = odd_reserved_core_divisors(n)

    terms: list[int] = []
    for t in (1, 2, 3):
        scale = 1 << (t - 1)
        cutoff = x_n // (3 * scale)
        u = largest_at_most(divisors, cutoff)
        b = scale * u
        assert 3 * scale * u <= x_n
        assert x_n < 9 * b
        assert b <= x_n // 3
        assert factorial % (3 * b) == 0
        assert (b & -b).bit_length() - 1 == t - 1
        terms.append(b)

    assert len(set(terms)) == 3
    assert sum(terms) > quotient_endpoint
    return quotient_endpoint, terms


def test_endpoint_support() -> None:
    for n in range(12, 21):
        endpoint_terms(n)


def greedy_residual(n: int, q: int, layers: int) -> int:
    divisors = odd_reserved_core_divisors(n)
    residual = q
    for t in range(1, layers + 1):
        scale = 1 << (t - 1)
        if residual < scale:
            continue
        cutoff = residual // scale
        u = largest_at_most(divisors, cutoff)
        b = scale * u
        assert b <= residual
        assert residual < 3 * b
        residual -= b
    return residual


def test_coarse_contraction() -> None:
    for n in range(12, 15):
        x_n = math.isqrt(math.factorial(n))
        endpoint = x_n // 3
        for q in range(endpoint + 1):
            for layers in range(1, 7):
                residual = greedy_residual(n, q, layers)
                # Exact integer surrogate for
                # residual < max((2/3)^layers q, 2^layers).
                if residual >= 1 << layers:
                    assert residual * (3**layers) < q * (2**layers)


def main() -> None:
    tests = [
        test_three_density,
        test_endpoint_support,
        test_coarse_contraction,
    ]
    for test in tests:
        test()
        print(f"PASS {test.__name__}")
    print(f"PASS all {len(tests)} endpoint-support checks")


if __name__ == "__main__":
    main()
