"""Exact arithmetic for factorial prime valuations and divisors."""

from __future__ import annotations

from math import isqrt, prod
from typing import Iterable


def _require_int(name: str, value: object, *, minimum: int | None = None) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")
    if minimum is not None and value < minimum:
        raise ValueError(f"{name} must be at least {minimum}")
    return value


def prime_sieve(limit: int) -> list[int]:
    """Return all primes p <= limit using an exact deterministic sieve."""
    limit = _require_int("limit", limit, minimum=0)
    if limit < 2:
        return []
    flags = bytearray(b"\x01") * (limit + 1)
    flags[0:2] = b"\x00\x00"
    bound = isqrt(limit)
    for p in range(2, bound + 1):
        if flags[p]:
            start = p * p
            flags[start : limit + 1 : p] = b"\x00" * (((limit - start) // p) + 1)
    return [i for i, flag in enumerate(flags) if flag]


def valuation_of_factorial(n: int, p: int) -> int:
    """Compute v_p(n!) by Legendre's exact formula."""
    n = _require_int("n", n, minimum=0)
    p = _require_int("p", p, minimum=2)
    total = 0
    quotient = n
    while quotient:
        quotient //= p
        total += quotient
    return total


def factorial_prime_valuations(n: int) -> dict[int, int]:
    """Return {p: v_p(n!)} for every prime p <= n."""
    n = _require_int("n", n, minimum=0)
    return {p: valuation_of_factorial(n, p) for p in prime_sieve(n)}


def factor_over_primes(value: int, primes: Iterable[int]) -> tuple[dict[int, int], int]:
    """Factor value over the supplied primes and return (exponents, residual)."""
    value = _require_int("value", value, minimum=1)
    residual = value
    exponents: dict[int, int] = {}
    for p in primes:
        exponent = 0
        while residual % p == 0:
            residual //= p
            exponent += 1
        if exponent:
            exponents[p] = exponent
        if residual == 1:
            break
    return exponents, residual


def is_divisor_of_factorial(value: int, n: int) -> bool:
    """Return whether positive integer value divides n!, using valuation budgets."""
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        return False
    if isinstance(n, bool) or not isinstance(n, int) or n < 0:
        return False
    budgets = factorial_prime_valuations(n)
    exponents, residual = factor_over_primes(value, budgets)
    if residual != 1:
        return False
    return all(exponents[p] <= budgets[p] for p in exponents)


def generate_divisors_from_valuations(
    valuations: dict[int, int], *, max_value: int | None = None
) -> list[int]:
    """Generate sorted divisors from exact prime-exponent budgets.

    If max_value is supplied, only divisors <= max_value are generated. The pruning is
    safe because all prime factors and partial products are positive integers >= 1.
    """
    if max_value is not None:
        max_value = _require_int("max_value", max_value, minimum=1)
    divisors = [1]
    for p in sorted(valuations):
        exponent = _require_int(f"valuations[{p}]", valuations[p], minimum=0)
        prior = divisors
        expanded: list[int] = []
        power = 1
        for _ in range(exponent + 1):
            for d in prior:
                candidate = d * power
                if max_value is None or candidate <= max_value:
                    expanded.append(candidate)
            power *= p
        divisors = sorted(expanded)
    return divisors


def divisors_of_factorial(n: int, *, max_value: int | None = None) -> list[int]:
    """Generate the positive divisors of n!, optionally truncated by value."""
    n = _require_int("n", n, minimum=0)
    return generate_divisors_from_valuations(
        factorial_prime_valuations(n), max_value=max_value
    )


def divisor_count_from_valuations(valuations: dict[int, int]) -> int:
    """Return tau from a prime valuation mapping."""
    return prod(exponent + 1 for exponent in valuations.values())
