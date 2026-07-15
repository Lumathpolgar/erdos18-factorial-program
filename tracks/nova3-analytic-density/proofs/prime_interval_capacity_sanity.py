#!/usr/bin/env python3
"""Finite sanity checks for N3-ANA-010 and N3-ANA-011.

Result class:
- finite certificate for every integer 120368 <= n <= 1000000
- no claim outside that range

Python: 3.10+
Dependencies: standard library only
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass

N0 = 120_368
DEFAULT_MAX_N = 1_000_000


@dataclass(frozen=True)
class AuditMinima:
    prime_margin: float
    prime_margin_n: int
    address_slack: int
    address_slack_n: int
    capacity_margin_bits: float
    capacity_margin_n: int


def prime_prefix(limit: int) -> list[int]:
    if limit < 2:
        return [0] * (limit + 1)
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, math.isqrt(limit) + 1):
        if sieve[p]:
            start = p * p
            sieve[start : limit + 1 : p] = b"\x00" * (
                ((limit - start) // p) + 1
            )
    prefix = [0] * (limit + 1)
    count = 0
    for value in range(limit + 1):
        count += int(sieve[value])
        prefix[value] = count
    return prefix


def valuation_two_factorial(n: int) -> int:
    total = 0
    value = n
    while value:
        value //= 2
        total += value
    return total


def parameters(n: int) -> tuple[int, int, int]:
    logn = math.log(n)
    r_n = math.ceil(4.0 * logn)
    m_layers = math.ceil(16.0 * logn * logn)
    max_address = r_n + m_layers
    return r_n, m_layers, max_address


def run_audit(max_n: int) -> AuditMinima:
    if max_n < N0:
        raise ValueError(f"max_n must be at least {N0}")

    pi = prime_prefix(max_n)

    prime_margin = math.inf
    prime_margin_n = -1
    address_slack = 1 << 62
    address_slack_n = -1
    capacity_margin_bits = math.inf
    capacity_margin_n = -1

    for n in range(N0, max_n + 1):
        logn = math.log(n)
        upper_half_primes = pi[n] - pi[n // 2]
        requested_lower = n / (3.0 * logn)
        current_prime_margin = upper_half_primes - requested_lower

        # The smallest observed margin exceeds 1800, so the numerical
        # comparison is far from floating-point ambiguity.
        if current_prime_margin < -1e-9:
            raise AssertionError(
                "prime interval inequality failed: "
                f"n={n}, exact_count={upper_half_primes}, "
                f"required={requested_lower}"
            )
        if current_prime_margin < prime_margin:
            prime_margin = current_prime_margin
            prime_margin_n = n

        r_n, m_layers, max_address = parameters(n)
        legal_max = valuation_two_factorial(n) // 2 - 1
        current_address_slack = legal_max - max_address
        if current_address_slack < 0:
            raise AssertionError(
                "address inequality failed: "
                f"n={n}, e_M={max_address}, legal_max={legal_max}"
            )
        if current_address_slack < address_slack:
            address_slack = current_address_slack
            address_slack_n = n

        profile_exponent = m_layers * (upper_half_primes - 1) + r_n

        # log2(X_n+1) <= 1 + 0.5 log2(n!) <= 1 + 0.5 n log2(n).
        conservative_required_bits = 1.0 + 0.5 * n * math.log2(n)
        current_capacity_margin = profile_exponent - conservative_required_bits
        if current_capacity_margin < -1e-6:
            raise AssertionError(
                "capacity inequality failed: "
                f"n={n}, exponent={profile_exponent}, "
                f"required_bits={conservative_required_bits}"
            )
        if current_capacity_margin < capacity_margin_bits:
            capacity_margin_bits = current_capacity_margin
            capacity_margin_n = n

    return AuditMinima(
        prime_margin=prime_margin,
        prime_margin_n=prime_margin_n,
        address_slack=address_slack,
        address_slack_n=address_slack_n,
        capacity_margin_bits=capacity_margin_bits,
        capacity_margin_n=capacity_margin_n,
    )


def source_bound_sanity() -> None:
    logn = math.log(N0)
    b = math.log(2.0) + 1.1
    if N0 // 2 < 60_184:
        raise AssertionError("Dusart upper-bound threshold not met")
    if logn <= b:
        raise AssertionError("source denominators are not positive")

    lower_difference = (
        1.0 / (logn - 1.0)
        - 1.0 / (2.0 * (logn - b))
        - 1.0 / (3.0 * logn)
    )
    if lower_difference <= 0.0:
        raise AssertionError("derived Dusart difference bound is nonpositive")

    q_value = logn * logn + (5.0 - 4.0 * b) * logn - 2.0 * b
    if q_value <= 0.0:
        raise AssertionError("cleared-denominator polynomial is nonpositive")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--max-n",
        type=int,
        default=DEFAULT_MAX_N,
        help=f"largest n to audit, default {DEFAULT_MAX_N}",
    )
    args = parser.parse_args()

    source_bound_sanity()
    minima = run_audit(args.max_n)

    print(f"range: every integer {N0} <= n <= {args.max_n}")
    print(
        "minimum exact prime-count margin: "
        f"{minima.prime_margin:.12f} at n={minima.prime_margin_n}"
    )
    print(
        "minimum legal-address slack: "
        f"{minima.address_slack} at n={minima.address_slack_n}"
    )
    print(
        "minimum conservative capacity margin in bits: "
        f"{minima.capacity_margin_bits:.12f} "
        f"at n={minima.capacity_margin_n}"
    )
    print("PASS: all finite prime interval, address, and capacity checks completed")
    print("STATUS: finite certificate only; asymptotic validity comes from the proof")


if __name__ == "__main__":
    main()
