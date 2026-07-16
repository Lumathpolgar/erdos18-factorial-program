#!/usr/bin/env python3
import math


def primes_up_to(n: int) -> list[int]:
    sieve = bytearray(b"\x01") * (n + 1)
    if n >= 0:
        sieve[0] = 0
    if n >= 1:
        sieve[1] = 0
    for p in range(2, int(math.isqrt(n)) + 1):
        if sieve[p]:
            sieve[p * p : n + 1 : p] = b"\x00" * (((n - p * p) // p) + 1)
    return [i for i in range(2, n + 1) if sieve[i]]


def vp_factorial(n: int, p: int) -> int:
    total = 0
    power = p
    while power <= n:
        total += n // power
        power *= p
    return total


def digit_sum_base(n: int, p: int) -> int:
    total = 0
    while n:
        total += n % p
        n //= p
    return total


def divides_factorial(d: int, n: int) -> bool:
    if d <= 0:
        return False
    remaining = d
    for p in primes_up_to(n):
        exponent = 0
        while remaining % p == 0:
            remaining //= p
            exponent += 1
        if exponent > vp_factorial(n, p):
            return False
    return remaining == 1


def test_legendre_and_bands() -> None:
    for n in range(2, 151):
        for p in primes_up_to(n):
            lhs = vp_factorial(n, p)
            rhs = (n - digit_sum_base(n, p)) // (p - 1)
            assert lhs == rhs, (n, p, lhs, rhs)
            if p * p > n:
                assert lhs == n // p
        for q in range(1, int(math.isqrt(n)) + 1):
            for p in primes_up_to(n):
                if max(math.sqrt(n), n / (q + 1)) < p <= n / q:
                    assert vp_factorial(n, p) == q, (n, q, p)


def test_binary_palette() -> None:
    for n in range(2, 80):
        max_r = min(vp_factorial(n, 2) + 1, 14)
        for r in range(1, max_r + 1):
            palette = [1 << j for j in range(r)]
            assert all(divides_factorial(d, n) for d in palette)
            for target in range(1 << r):
                selected = [1 << j for j in range(r) if (target >> j) & 1]
                assert sum(selected) == target
                assert len(selected) == len(set(selected)) <= r


def test_marker_distinctness() -> None:
    odd_cores = [3, 5, 9, 15, 21, 25]
    exponents = list(range(7, 7 + len(odd_cores)))
    values = [core * (1 << exponent) for core, exponent in zip(odd_cores, exponents)]
    assert len(values) == len(set(values))
    assert [((value & -value).bit_length() - 1) for value in values] == exponents
    palette = {1 << j for j in range(7)}
    assert palette.isdisjoint(values)


def test_complement_pairing() -> None:
    n = 10
    r_center = (2**4) * (3**2)
    q_square = r_center * r_center
    assert divides_factorial(q_square, n)
    multipliers = [3, 9]
    upper = 5000
    terms = []
    for z in multipliers:
        assert r_center % z == 0
        low = r_center // z
        high = r_center * z
        assert low < r_center < high <= upper
        assert divides_factorial(low, n)
        assert divides_factorial(high, n)
        terms.extend([low, high])
    assert len(terms) == len(set(terms))


def subset_products(values: list[int]) -> list[int]:
    products = [1]
    for value in values:
        products += [x * value for x in products]
    return products


def test_high_prime_menu_count() -> None:
    for n in range(4, 81):
        high_primes = [p for p in primes_up_to(n) if n / 2 < p <= n]
        if not high_primes:
            continue
        product = math.prod(high_primes)
        low_products = [d for d in subset_products(high_primes) if d <= math.isqrt(product)]
        expected = 1 << (len(high_primes) - 1)
        assert len(low_products) == expected, (n, high_primes, len(low_products), expected)
        assert len([d for d in low_products if d > 1]) == expected - 1


def test_window_counting_lemma() -> None:
    universe = list(range(8))
    for mask in range(1, 1 << len(universe)):
        sums = [universe[i] for i in range(len(universe)) if (mask >> i) & 1]
        for residual in range(4):
            for upper in range(8):
                covered = all(
                    any(target - residual <= value <= target for value in sums)
                    for target in range(upper + 1)
                )
                if covered:
                    assert len(sums) * (residual + 1) >= upper + 1


def main() -> None:
    tests = [
        test_legendre_and_bands,
        test_binary_palette,
        test_marker_distinctness,
        test_complement_pairing,
        test_high_prime_menu_count,
        test_window_counting_lemma,
    ]
    for test in tests:
        test()
        print(f"PASS {test.__name__}")
    print(f"PASS all {len(tests)} structural sanity checks")


if __name__ == "__main__":
    main()
