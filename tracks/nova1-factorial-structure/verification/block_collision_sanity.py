from __future__ import annotations

import itertools
import math
from math import factorial, isqrt


def v2_factorial(n: int) -> int:
    total = 0
    while n:
        n //= 2
        total += n
    return total


def odd_factorial_part(n: int) -> int:
    return factorial(n) >> v2_factorial(n)


def largest_odd_leq(n: int) -> int:
    return n if n % 2 else n - 1


def test_factorial_blocks() -> None:
    for n in range(6, 21):
        N = factorial(n)
        for k in range(3, n):
            A = odd_factorial_part(k) // 3
            m = largest_odd_leq(n - k)
            if m < 1:
                continue
            for j in range(1, m + 1, 2):
                core = A * j
                assert core % 2 == 1
                assert N % (3 * core) == 0


def test_block_connectivity_and_ceiling() -> None:
    for n in range(12, 51):
        X = isqrt(factorial(n))
        Y = X // 3
        r = math.ceil(4 * math.log(n))
        M = min(30, math.ceil(16 * math.log(n) ** 2))
        W = ((1 << r) - 3) // 3
        E = 0
        for t in range(1, M + 1):
            a = 1 << (t - 1)
            F = E + W + 1
            D = F // a
            best = 0
            for k in range(3, n):
                A = odd_factorial_part(k) // 3
                m = largest_odd_leq(n - k)
                if m < 1:
                    continue
                endpoint = A * m
                if 2 * A <= D and a * endpoint <= Y:
                    best = max(best, endpoint)
            next_E = E + a * best
            assert next_E + W + 1 <= (1 + n / 2) * F
            E = next_E


def collision_profiles(K: int) -> list[tuple[tuple[int, int], ...]]:
    profiles: list[tuple[tuple[int, int], ...]] = []
    for bits in itertools.product((0, 1), repeat=K):
        terms: list[tuple[int, int]] = []
        for j, bit in enumerate(bits):
            e = 2 * j
            if bit == 0:
                terms.append((e, 3))
            else:
                terms.append((e, 1))
                terms.append((e + 1, 1))
        profiles.append(tuple(terms))
    return profiles


def test_exponential_carry_collisions() -> None:
    for K in range(1, 9):
        profiles = collision_profiles(K)
        sums = {
            sum((1 << e) * core for e, core in profile)
            for profile in profiles
        }
        assert len(profiles) == 1 << K
        assert len(set(profiles)) == 1 << K
        assert len(sums) == 1
        assert next(iter(sums)) == (1 << (2 * K)) - 1
        for profile in profiles:
            exponents = [e for e, _ in profile]
            assert len(exponents) == len(set(exponents))
            assert all(core % 2 == 1 for _, core in profile)


def test_asymptotic_scale_separation() -> None:
    n = 120_368
    L = math.log(n)
    upper = 16 * L**3 + 5 * L
    lower = (9 * n / 40) * L - math.log(4)
    assert lower > upper
    assert 1 - 2 / L > 0


def main() -> None:
    tests = [
        test_factorial_blocks,
        test_block_connectivity_and_ceiling,
        test_exponential_carry_collisions,
        test_asymptotic_scale_separation,
    ]
    for test in tests:
        test()
        print(f"PASS {test.__name__}")
    print(f"PASS all {len(tests)} block-and-collision checks")


if __name__ == "__main__":
    main()
