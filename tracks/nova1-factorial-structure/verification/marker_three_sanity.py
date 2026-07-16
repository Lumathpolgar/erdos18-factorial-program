#!/usr/bin/env python3
"""Deterministic exact checks for N1-CON-003.

Standard library only. All arithmetic is exact.
"""

from __future__ import annotations

import math
from typing import Dict, Iterable, List, Set, Tuple


def primes_up_to(n: int) -> List[int]:
    sieve = [True] * (n + 1)
    if n >= 0:
        sieve[0] = False
    if n >= 1:
        sieve[1] = False
    for p in range(2, math.isqrt(n) + 1):
        if sieve[p]:
            sieve[p * p : n + 1 : p] = [False] * (((n - p * p) // p) + 1)
    return [p for p, ok in enumerate(sieve) if ok]


def factorial_valuations(n: int) -> Dict[int, int]:
    vals: Dict[int, int] = {}
    for p in primes_up_to(n):
        q = n
        total = 0
        while q:
            q //= p
            total += q
        vals[p] = total
    return vals


def divisors_from_valuations(vals: Dict[int, int]) -> List[int]:
    divisors = [1]
    for p, exponent in vals.items():
        divisors = [d * (p**e) for d in divisors for e in range(exponent + 1)]
    return sorted(divisors)


def marker_three_layers(n: int, layer_count: int) -> Tuple[int, List[List[int]], List[List[int]]]:
    N = math.factorial(n)
    X = math.isqrt(N)
    vals = factorial_valuations(n)
    if layer_count - 1 > vals.get(2, 0):
        raise ValueError("layer count exceeds the 2-adic valuation budget")

    cores = [u for u in divisors_from_valuations(vals) if u % 2 == 1 and N % (3 * u) == 0]
    main_layers: List[List[int]] = []
    quotient_layers: List[List[int]] = []
    for t in range(1, layer_count + 1):
        scale = 1 << (t - 1)
        q_layer = [scale * u for u in cores if 3 * scale * u <= X]
        quotient_layers.append(q_layer)
        main_layers.append([3 * value for value in q_layer])
    return X, main_layers, quotient_layers


def rainbow_reachable(layers: Iterable[Iterable[int]], limit: int) -> Set[int]:
    reachable: Set[int] = {0}
    for layer in layers:
        next_reachable = set(reachable)
        for partial in reachable:
            for value in layer:
                total = partial + value
                if total <= limit:
                    next_reachable.add(total)
        reachable = next_reachable
    return reachable


def maximum_downward_gap(reachable: Set[int], limit: int) -> Tuple[int, int]:
    last = None
    maximum = 0
    witness = 0
    for x in range(limit + 1):
        if x in reachable:
            last = x
        elif last is None:
            gap = x + 1
            if gap > maximum:
                maximum, witness = gap, x
        else:
            gap = x - last
            if gap > maximum:
                maximum, witness = gap, x
    return maximum, witness


def test_legality_distinctness_and_lattice() -> None:
    for n in range(7, 15):
        vals = factorial_valuations(n)
        layers = min(6, vals[2] + 1)
        X, main, quotient = marker_three_layers(n, layers)
        N = math.factorial(n)

        seen: Set[int] = set()
        for t, layer in enumerate(main, start=1):
            for d in layer:
                assert d > 0 and d <= X and N % d == 0
                assert (d & -d).bit_length() - 1 == t - 1
                assert d % 3 == 0
                assert d not in seen
                seen.add(d)

        assert 3 in main[0]
        assert math.gcd(*seen) == 3
        assert all(value * 3 in main[t] for t, layer in enumerate(quotient) for value in layer)

        r = 3
        palette = [1 << e for e in range(r)]
        assert seen.isdisjoint(palette)
        residues = {sum(palette[e] for e in range(r) if mask & (1 << e)) % 3 for mask in range(1 << r)}
        assert residues == {0, 1, 2}


def test_odd_digit_one_gap() -> None:
    for m in range(3, 18, 2):
        digits = [0] + list(range(1, m + 1, 2))
        for layers in range(1, 9):
            reachable = {0}
            for e in range(layers):
                weight = 1 << e
                reachable = {s + weight * d for s in reachable for d in digits}
            limit = m * ((1 << layers) - 1)
            for q in range(limit + 1):
                assert q in reachable or (q > 0 and q - 1 in reachable)


def test_quotient_reduction_exhaustively() -> None:
    for n in range(7, 15):
        vals = factorial_valuations(n)
        layer_count = min(6, vals[2] + 1)
        r = 3
        R = (1 << r) - 1
        W = (R - 2) // 3
        X, main, quotient = marker_three_layers(n, layer_count)
        q_limit = X // 3
        q_reachable = rainbow_reachable(quotient, q_limit)

        first_failure = None
        for q in range(W + 1, q_limit + 1):
            if not any((q - delta) in q_reachable for delta in range(W + 1)):
                first_failure = q
                break
        assert first_failure is None

        main_reachable = {3 * q for q in q_reachable}
        palette_layers = [[1 << e] for e in range(r)]
        palette_reachable = rainbow_reachable(palette_layers, R)
        full_reachable = {a + b for a in main_reachable for b in palette_reachable if a + b <= X}
        assert all(x in full_reachable for x in range(X + 1))

        maximum, witness = maximum_downward_gap(q_reachable, q_limit)
        assert maximum <= W + 1, (n, maximum, witness)
        print(
            f"n={n} X={X} layers={layer_count} q_targets={q_limit + 1} "
            f"reachable_q={len(q_reachable)} max_downward_distance={maximum}"
        )


def main() -> None:
    tests = [
        test_legality_distinctness_and_lattice,
        test_odd_digit_one_gap,
        test_quotient_reduction_exhaustively,
    ]
    for test in tests:
        test()
        print(f"PASS {test.__name__}")
    print(f"PASS all {len(tests)} marker-three checks")


if __name__ == "__main__":
    main()
