#!/usr/bin/env python3
"""Exact finite checks for N3-ANA-032 through N3-ANA-034.

Standard library only. The script verifies the transformed interval central-lobe
cutoff, the selected-coordinate 3-adic chain identity, and the sign-dependent
chain-endpoint characteristic bounds.
"""

from __future__ import annotations

import cmath
import math
from collections import defaultdict
from typing import Dict, List, Optional, Sequence, Tuple


State = Tuple[int, Optional[int]]


def prime_factorial_exponents(n: int) -> Dict[int, int]:
    exps: Dict[int, int] = {}
    for x0 in range(2, n + 1):
        x = x0
        p = 2
        while p * p <= x:
            while x % p == 0:
                exps[p] = exps.get(p, 0) + 1
                x //= p
            p += 1
        if x > 1:
            exps[x] = exps.get(x, 0) + 1
    return exps


def divisors_from_exponents(exps: Dict[int, int]) -> List[int]:
    values = [1]
    for p, a in sorted(exps.items()):
        values = [d * p**e for d in values for e in range(a + 1)]
    return sorted(values)


def odd_marker_core_divisors(n: int) -> List[int]:
    exps = prime_factorial_exponents(n)
    exps.pop(2, None)
    exps[3] = exps.get(3, 0) - 1
    if exps[3] == 0:
        del exps[3]
    return divisors_from_exponents(exps)


def parameters(n: int) -> Tuple[int, int, int, int, int]:
    rho = math.ceil(4 * math.log(n))
    M = math.ceil(16 * math.log(n) ** 2)
    X = math.isqrt(math.factorial(n))
    Y = X // 3
    W = (2**rho - 3) // 3
    return rho, M, X, Y, W


def ceil_div2(x: int) -> int:
    return -((-x) // 2)


def transformed_window_length(q: int, W: int) -> int:
    lo = ceil_div2(q - W - 1)
    hi = (q - 1) // 2
    return hi - lo + 1


def selected_states(n: int, j: int) -> List[State]:
    _, _, _, Y, _ = parameters(n)
    cores = odd_marker_core_divisors(n)

    if j == 1:
        return [((u - 1) // 2, u) for u in cores if u <= Y]

    a = 2 ** (j - 2)
    cutoff = Y // (2 ** (j - 1))
    positives = [(a * u, u) for u in cores if u <= cutoff]
    return [(0, None)] + positives


def probabilities(states: Sequence[State], tilt: float) -> List[float]:
    logs = [tilt * x for x, _ in states]
    shift = max(logs)
    weights = [math.exp(value - shift) for value in logs]
    total = sum(weights)
    return [weight / total for weight in weights]


def characteristic(
    states: Sequence[State], probs: Sequence[float], theta: float
) -> complex:
    return sum(
        p * cmath.exp(1j * theta * x)
        for (x, _), p in zip(states, probs)
    )


def lower_endpoint_mass(states: Sequence[State], probs: Sequence[float]) -> float:
    return sum(
        p
        for (_, core), p in zip(states, probs)
        if core is None or core % 3 != 0
    )


def upper_endpoint_mass(states: Sequence[State], probs: Sequence[float]) -> float:
    legal = {core for _, core in states if core is not None}
    return sum(
        p
        for (_, core), p in zip(states, probs)
        if core is None or 3 * core not in legal
    )


def strip_threes(u: int) -> Tuple[int, int]:
    exponent = 0
    while u % 3 == 0:
        exponent += 1
        u //= 3
    return u, exponent


def verify_chain_identity(
    states: Sequence[State], probs: Sequence[float], theta: float
) -> None:
    direct_positive = sum(
        p * cmath.exp(1j * theta * x)
        for (x, core), p in zip(states, probs)
        if core is not None
    )

    chains: Dict[int, List[Tuple[int, int, float]]] = defaultdict(list)
    for (x, core), p in zip(states, probs):
        if core is None:
            continue
        base, exponent = strip_threes(core)
        chains[base].append((exponent, x, p))

    rebuilt = 0j
    for entries in chains.values():
        entries.sort()
        exponents = [entry[0] for entry in entries]
        assert exponents == list(range(exponents[-1] + 1))

        first_phase = cmath.exp(1j * theta * entries[0][1])
        for index, (_, x, _) in enumerate(entries):
            phase = cmath.exp(1j * theta * x)
            assert abs(phase - ((-1) ** index) * first_phase) < 1e-10
        rebuilt += sum(
            p * cmath.exp(1j * theta * x) for _, x, p in entries
        )

    assert abs(direct_positive - rebuilt) < 1e-10


def exact_small_checks() -> None:
    for n in (12, 15, 18):
        rho, M, _, _, W = parameters(n)

        for q in (1000, 1001):
            length = transformed_window_length(q, W)
            assert 2 ** (rho - 3) < length < 2 ** (rho - 2)
            first_zero = 2 * math.pi / length
            assert 2 * math.pi / (2 ** (rho - 3)) > first_zero
            assert 2 * math.pi / (2 ** (rho - 2)) < first_zero

        max_j = min(rho - 3, 8)
        for j in range(1, max_j + 1):
            states = selected_states(n, j)
            if len(states) <= 1:
                break
            theta = 2 * math.pi / (2**j)

            for tilt in (-1e-4, 0.0, 1e-4):
                probs = probabilities(states, tilt)
                factor = characteristic(states, probs, theta)
                verify_chain_identity(states, probs, theta)

                low = lower_endpoint_mass(states, probs)
                high = upper_endpoint_mass(states, probs)

                if tilt <= 0:
                    assert abs(factor) <= low + 1e-10
                if tilt >= 0:
                    assert abs(factor) <= high + 1e-10

        print(
            "PASS exact chain-endpoint checks",
            f"n={n}",
            f"rho={rho}",
            f"secondary_scales={rho-3}",
            f"M={M}",
        )


def selected_large_scales() -> None:
    for n in (120368, 200000, 500000, 1000000):
        rho = math.ceil(4 * math.log(n))
        M = math.ceil(16 * math.log(n) ** 2)
        secondary = rho - 3
        central_lobe_ladder_points = (M - 1) - secondary
        assert secondary > 0
        assert central_lobe_ladder_points > 0
        print(
            "SCALE",
            f"n={n}",
            f"rho={rho}",
            f"M={M}",
            f"secondary_dyadic_scales={secondary}",
            f"central_lobe_ladder_points={central_lobe_ladder_points}",
        )


if __name__ == "__main__":
    exact_small_checks()
    selected_large_scales()
    print("PASS dyadic central-lobe and chain-endpoint sanity")
