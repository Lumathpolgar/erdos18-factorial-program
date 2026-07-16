#!/usr/bin/env python3
"""Deterministic checks for N3-ANA-014 through N3-ANA-016.

Result classes:
- exact finite certificate at n=120368;
- exact counterexample checks for the central-binomial shortcut;
- computational evidence for selected larger n.

The symbolic monotonic proof is in MARKER_THREE_REPAIRED_CAPACITY_AUDIT.md.
Python: 3.11+
Dependencies: standard library only.
"""

from __future__ import annotations

import math
from decimal import Decimal, getcontext
from typing import Iterable

N0 = 120_368
getcontext().prec = 70


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


def v2_factorial(n: int) -> int:
    total = 0
    while n:
        n //= 2
        total += n
    return total


def parameters(n: int) -> tuple[int, int]:
    logn = math.log(n)
    return math.ceil(16.0 * logn * logn), math.ceil(4.0 * logn)


def ceil_log2(y: int) -> int:
    if y < 1:
        raise ValueError("ceil_log2 requires y>=1")
    return (y - 1).bit_length()


def top_prime_band(n: int, primes: Iterable[int]) -> list[int]:
    return [p for p in primes if 2 * p > n and p <= n]


def exact_threshold_audit() -> dict[str, int | float | bool]:
    primes = primes_up_to(N0)
    band = top_prime_band(N0, primes)
    h = len(band)
    h_product = math.prod(band)
    factorial = math.factorial(N0)
    x_n = math.isqrt(factorial)
    m_n, r_n = parameters(N0)

    exact_cutoff = 9 * (1 << (2 * m_n - 2)) * h_product < factorial
    if not exact_cutoff:
        raise AssertionError("exact repaired cutoff failed at n=120368")

    address_slack = v2_factorial(N0) - (m_n - 1)
    if address_slack < 0:
        raise AssertionError("2-adic address legality failed at n=120368")

    profile_exponent = r_n + m_n * (h - 1)
    target_exponent = ceil_log2(x_n + 1)
    if profile_exponent < target_exponent:
        raise AssertionError("exact formal capacity failed at n=120368")

    logn = Decimal(N0).ln()
    prime_margin = Decimal(h) - Decimal(N0) / (Decimal(3) * logn)
    if prime_margin < 0:
        raise AssertionError("explicit prime interval inequality failed")

    quotient_log_margin = (
        Decimal(math.lgamma(N0 // 2 + 1))
        - Decimal(2) * Decimal(3).ln()
        - Decimal(2 * m_n - 2) * Decimal(2).ln()
    )

    return {
        "h": h,
        "M": m_n,
        "r": r_n,
        "prime_margin": float(prime_margin),
        "address_slack": address_slack,
        "profile_bit_margin": profile_exponent - target_exponent,
        "quotient_log_margin": float(quotient_log_margin),
        "exact_cutoff": exact_cutoff,
    }


def central_binomial_regression() -> None:
    primes = primes_up_to(101)
    tested = 0
    for p in primes:
        if p < 3:
            continue
        n = 2 * p - 1
        central = math.comb(n, n // 2)
        if central % p == 0:
            raise AssertionError(
                f"expected p={p} to cancel from C({n},{n//2})"
            )
        tested += 1
    if tested == 0:
        raise AssertionError("no central-binomial counterexamples tested")


def monotonic_certificate() -> None:
    if not N0 < 2**17:
        raise AssertionError("threshold logarithm bound not certified")
    if not 32 * 17**2 < N0 / 8:
        raise AssertionError("threshold log-square bound not certified")
    if not N0 > 12 * 17:
        raise AssertionError("threshold x/log x bound not certified")

    logn = math.log(N0)
    if not logn > 2:
        raise AssertionError("log-square ratio monotonicity not active")
    if not logn > 1:
        raise AssertionError("x/log x monotonicity not active")

    # d/dx ((log x)^2/x) has the sign of log x*(2-log x).
    if not logn * (2.0 - logn) < 0:
        raise AssertionError("(log x)^2/x is not decreasing at threshold")

    # d/dx (x/log x) has the sign of log x-1.
    if not logn - 1.0 > 0:
        raise AssertionError("x/log x is not increasing at threshold")


def selected_scale_rows(ns: Iterable[int]) -> list[tuple[int, int, float, int, float, float]]:
    ns = tuple(ns)
    primes = primes_up_to(max(ns))
    rows: list[tuple[int, int, float, int, float, float]] = []

    for n in ns:
        logn = Decimal(n).ln()
        band = top_prime_band(n, primes)
        h = len(band)
        m_n, r_n = parameters(n)

        prime_margin = Decimal(h) - Decimal(n) / (Decimal(3) * logn)
        address_slack = v2_factorial(n) - (m_n - 1)
        monotonic_margin = Decimal(n) / Decimal(8) - Decimal(32) * logn**2

        profile_lower = Decimal(r_n) + Decimal(m_n) * Decimal(h - 1)
        target_upper = (
            Decimal(1)
            + Decimal(n) * logn / (Decimal(2) * Decimal(2).ln())
        )
        capacity_margin = profile_lower - target_upper

        if prime_margin < 0:
            raise AssertionError(f"prime interval check failed at n={n}")
        if address_slack < 0:
            raise AssertionError(f"address legality failed at n={n}")
        if monotonic_margin < 0:
            raise AssertionError(f"log-square inequality failed at n={n}")
        if capacity_margin < 0:
            raise AssertionError(f"capacity comparison failed at n={n}")

        rows.append(
            (
                n,
                h,
                float(prime_margin),
                address_slack,
                float(monotonic_margin),
                float(capacity_margin),
            )
        )

    return rows


def main() -> None:
    central_binomial_regression()
    monotonic_certificate()
    exact = exact_threshold_audit()

    print("exact threshold audit")
    for key, value in exact.items():
        print(f"{key}: {value}")

    print("\nselected scale checks")
    print("n h prime_margin address_slack log_square_margin capacity_bit_margin")
    for row in selected_scale_rows((120_368, 200_000, 500_000, 1_000_000)):
        print(
            f"{row[0]:7d} {row[1]:6d} {row[2]:13.6f} "
            f"{row[3]:13d} {row[4]:17.6f} {row[5]:19.6f}"
        )

    print("\nPASS: marker-three repaired capacity checks completed")
    print("STATUS: exact finite certificate at n=120368")
    print("STATUS: central-binomial shortcut rejected on an exact prime family")
    print("STATUS: selected larger rows are computational evidence only")


if __name__ == "__main__":
    main()
