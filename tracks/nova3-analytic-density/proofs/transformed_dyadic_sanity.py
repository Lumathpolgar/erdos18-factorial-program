#!/usr/bin/env python3
"""Finite checks for the transformed marker-three dyadic resonance ladder.

Standard library only. Exact combinatorial checks are separated from selected
large-n scale evidence.
"""

from __future__ import annotations

import cmath
import math
from typing import Dict, List, Tuple


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
        powers = [p**e for e in range(a + 1)]
        values = [d * pe for d in values for pe in powers]
    return sorted(values)


def odd_marker_core_divisors(n: int) -> List[int]:
    exps = prime_factorial_exponents(n)
    exps.pop(2, None)
    exps[3] = exps.get(3, 0) - 1
    if exps[3] == 0:
        del exps[3]
    return divisors_from_exponents(exps)


def parameters(n: int) -> Tuple[int, int, int, int, int, int, int]:
    rho = math.ceil(4 * math.log(n))
    M = math.ceil(16 * math.log(n) ** 2)
    fact = math.factorial(n)
    X = math.isqrt(fact)
    Y = X // 3
    W = (2**rho - 3) // 3
    m = n if n % 2 else n - 1
    L = m * (2**M - 1)
    return rho, M, X, Y, W, m, L


def transformed_supports(n: int) -> Tuple[List[List[int]], Tuple[int, ...]]:
    rho, M, X, Y, W, m, L = parameters(n)
    divs = odd_marker_core_divisors(n)
    supports: List[List[int]] = []

    first_u = [u for u in divs if u <= Y]
    supports.append([(u - 1) // 2 for u in first_u])

    for t in range(2, M + 1):
        cutoff = Y // (2 ** (t - 1))
        us = [u for u in divs if u <= cutoff]
        supports.append([0] + [(2 ** (t - 2)) * u for u in us])

    return supports, (rho, M, X, Y, W, m, L)


def tilted_probabilities(support: List[int], tilt: float) -> List[float]:
    raw = [tilt * x for x in support]
    shift = max(raw)
    weights = [math.exp(v - shift) for v in raw]
    total = sum(weights)
    return [w / total for w in weights]


def characteristic_dyadic(
    support: List[int], probabilities: List[float], denominator_power: int
) -> complex:
    modulus = 2**denominator_power
    return sum(
        p * cmath.exp(2j * math.pi * (x % modulus) / modulus)
        for x, p in zip(support, probabilities)
    )


def ceil_div2(x: int) -> int:
    return -((-x) // 2)


def transformed_window(q: int, W: int) -> Tuple[int, int, int]:
    lo = ceil_div2(q - W - 1)
    hi = (q - 1) // 2
    return lo, hi, hi - lo + 1


def v2(x: int) -> int:
    if x <= 0:
        raise ValueError("v2 requires a positive integer")
    out = 0
    while x % 2 == 0:
        out += 1
        x //= 2
    return out


def exact_small_checks() -> None:
    for n in (12, 15):
        supports, params = transformed_supports(n)
        _, M, _, _, W, _, _ = params
        nonempty_layers = sum(1 for support in supports if len(support) > 1)
        max_j = min(6, nonempty_layers - 1, M - 1)
        assert max_j >= 1

        for tilt in (-0.001, 0.0, 0.001):
            probs = [tilted_probabilities(s, tilt) for s in supports]
            for j in range(1, max_j + 1):
                factors = [
                    characteristic_dyadic(s, p, j)
                    for s, p in zip(supports, probs)
                ]
                full = complex(1.0, 0.0)
                for factor in factors:
                    full *= factor

                prefix = complex(1.0, 0.0)
                for factor in factors[:j]:
                    prefix *= factor

                matching_support = supports[j]
                matching_probs = probs[j]
                p_zero = matching_probs[matching_support.index(0)]
                expected_matching = 2 * p_zero - 1
                assert abs(factors[j] - expected_matching) < 1e-11

                for factor in factors[j + 1 :]:
                    assert abs(factor - 1) < 1e-11

                assert abs(full - prefix * expected_matching) < 1e-10

        rho = params[0]
        for q in (1000, 1001):
            _, _, N = transformed_window(q, W)
            if rho % 2 == 1:
                expected = (2 ** (rho - 1) - 1) // 3
                assert N == expected
                assert v2(N) == 0
            elif q % 2 == 0:
                expected = 2 * ((2 ** (rho - 2) - 1) // 3)
                assert N == expected
                assert v2(N) == 1
            else:
                expected = (2 ** (rho - 1) + 1) // 3
                assert N == expected
                assert v2(N) == 0

            for d in range(1, 8):
                theta = 2 * math.pi / (2**d)
                kernel = sum(cmath.exp(1j * theta * x) for x in range(N))
                exact_zero = N % (2**d) == 0
                if exact_zero:
                    assert abs(kernel) < 1e-7
                else:
                    assert abs(kernel) > 1e-7

        print(
            f"PASS exact transformed dyadic checks n={n}, "
            f"layers={nonempty_layers}"
        )


def selected_large_scales() -> None:
    for n in (120368, 200000, 500000, 1000000):
        rho = math.ceil(4 * math.log(n))
        M = math.ceil(16 * math.log(n) ** 2)
        m = n if n % 2 else n - 1
        logL = math.log(m) + M * math.log(2) + math.log1p(-(2.0 ** (-M)))

        log2_prefactor = (
            math.log2(16 * M * logL)
            - M
            - math.log2(1 - 2.0 ** (-M))
        )
        J = min(M - 1, math.floor(1 - log2_prefactor))
        eta_J = 2 ** (log2_prefactor + J - 1)
        p_zero_ceiling = 2 * math.exp(eta_J) / (m + 1)
        matching_modulus_floor = 1 - 2 * p_zero_ceiling
        tail_dispersion_ceiling = 2 * p_zero_ceiling

        W = (2**rho - 3) // 3
        lengths = sorted(
            {transformed_window(1000 + parity, W)[2] for parity in (0, 1)}
        )
        length_v2 = [(N, v2(N)) for N in lengths]

        assert 1 <= J <= M - 1
        assert eta_J <= 1 + 1e-12
        assert matching_modulus_floor > 0
        assert all(power <= 1 for _, power in length_v2)

        print(
            "SCALE",
            f"n={n}",
            f"rho={rho}",
            f"M={M}",
            f"J={J}",
            f"uncontrolled_top_scales={M-1-J}",
            f"eta_J={eta_J:.12g}",
            f"p0_ceiling={p_zero_ceiling:.12g}",
            f"matching_modulus_floor={matching_modulus_floor:.12g}",
            f"tail_dispersion_ceiling={tail_dispersion_ceiling:.12g}",
            f"window_lengths_v2={length_v2}",
        )


if __name__ == "__main__":
    exact_small_checks()
    selected_large_scales()
    print("PASS transformed dyadic resonance ladder sanity")
