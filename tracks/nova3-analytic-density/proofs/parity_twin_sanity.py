#!/usr/bin/env python3
"""Finite and threshold checks for N3-ANA-023 through N3-ANA-025.

Python standard library only.

The small-n checks are exact in support construction and floating-point only in
characteristic-function evaluation. The n=120368 and larger rows verify the
closed-form bounds without enumerating factorial divisor menus.
"""

from __future__ import annotations

import cmath
import math
from typing import Iterable


def factorize(value: int) -> list[tuple[int, int]]:
    factors: list[tuple[int, int]] = []
    remaining = value
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            exponent = 0
            while remaining % divisor == 0:
                remaining //= divisor
                exponent += 1
            factors.append((divisor, exponent))
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        factors.append((remaining, 1))
    return factors


def divisors(value: int) -> list[int]:
    result = [1]
    for prime, exponent in factorize(value):
        next_result: list[int] = []
        for divisor in result:
            for power in range(exponent + 1):
                next_result.append(divisor * prime**power)
        result = next_result
    return sorted(result)


def odd_marker_core(n: int) -> int:
    value = math.factorial(n)
    while value % 2 == 0:
        value //= 2
    if value % 3 != 0:
        raise AssertionError("odd factorial part is not divisible by 3")
    return value // 3


def parameters(n: int) -> tuple[int, int, int, int, int]:
    x_n = math.isqrt(math.factorial(n))
    y_n = x_n // 3
    r_n = math.ceil(4.0 * math.log(n))
    m_n = math.ceil(16.0 * math.log(n) ** 2)
    w_n = (2**r_n - 3) // 3
    return x_n, y_n, r_n, m_n, w_n


def build_layers(n: int) -> list[list[int]]:
    _, y_n, _, m_n, _ = parameters(n)
    cores = divisors(odd_marker_core(n))
    layers: list[list[int]] = []
    for t in range(1, m_n + 1):
        scale = 2 ** (t - 1)
        layers.append([scale * core for core in cores if scale * core <= y_n])
    return layers


def normalized_probabilities(states: Iterable[int], tilt: float) -> list[float]:
    state_list = list(states)
    weights = [math.exp(tilt * state) for state in state_list]
    total = sum(weights)
    return [weight / total for weight in weights]


def coordinate_cf(values: list[int], tilt: float, theta: float) -> complex:
    states = [0] + values
    probabilities = normalized_probabilities(states, tilt)
    return sum(
        probability * cmath.exp(1j * theta * state)
        for probability, state in zip(probabilities, states)
    )


def global_cf(layers: list[list[int]], tilt: float, theta: float) -> complex:
    result = 1.0 + 0.0j
    for values in layers:
        result *= coordinate_cf(values, tilt, theta)
    return result


def first_zero_probability(first_layer: list[int], tilt: float) -> float:
    return 1.0 / (1.0 + sum(math.exp(tilt * value) for value in first_layer))


def check_small_exact_support(n: int) -> None:
    layers = build_layers(n)
    if not layers[0] or 1 not in layers[0] or 3 not in layers[0]:
        raise AssertionError(f"first-layer small states missing for n={n}")

    for t, values in enumerate(layers, start=1):
        scale = 2 ** (t - 1)
        if any(value % scale != 0 for value in values):
            raise AssertionError(f"layer scale failure for n={n}, t={t}")
        if t == 1 and any(value % 2 == 0 for value in values):
            raise AssertionError(f"first layer contains an even nonzero state for n={n}")
        if t >= 2 and any(value % 2 != 0 for value in values):
            raise AssertionError(f"later layer contains an odd state for n={n}, t={t}")

    for tilt in (-1.0e-5, 0.0, 1.0e-5):
        p_zero = first_zero_probability(layers[0], tilt)
        at_pi = global_cf(layers, tilt, math.pi)
        if abs(at_pi - (2.0 * p_zero - 1.0)) > 2.0e-10:
            raise AssertionError(f"pi identity failed for n={n}, tilt={tilt}")

        for u in (-1.2, -0.3, 0.0, 0.4, 1.1):
            later_product = 1.0 + 0.0j
            for values in layers[1:]:
                later_product *= coordinate_cf(values, tilt, u)
            left = global_cf(layers, tilt, math.pi + u) + global_cf(layers, tilt, u)
            right = 2.0 * p_zero * later_product
            if abs(left - right) > 2.0e-9:
                raise AssertionError(
                    f"parity twin identity failed for n={n}, tilt={tilt}, u={u}"
                )

        first_original = normalized_probabilities(layers[0], tilt)
        first_transformed_states = [(value - 1) // 2 for value in layers[0]]
        first_transformed = normalized_probabilities(first_transformed_states, 2.0 * tilt)
        if max(abs(a - b) for a, b in zip(first_original, first_transformed)) > 2.0e-12:
            raise AssertionError(f"first conditional transform failed for n={n}")

        for values in layers[1:6]:
            original = normalized_probabilities([0] + values, tilt)
            transformed = normalized_probabilities(
                [0] + [value // 2 for value in values], 2.0 * tilt
            )
            if max(abs(a - b) for a, b in zip(original, transformed)) > 2.0e-12:
                raise AssertionError(f"later coordinate transform failed for n={n}")

    _, _, _, _, w_n = parameters(n)
    for q in (w_n + 1, w_n + 2, w_n + 7):
        lower = math.ceil((q - w_n - 1) / 2)
        upper = math.floor((q - 1) / 2)
        transformed = set(range(lower, upper + 1))
        direct = {
            (value - 1) // 2
            for value in range(q - w_n, q + 1)
            if value % 2 == 1
        }
        if transformed != direct:
            raise AssertionError(f"window transform failed for n={n}, q={q}")


def log_big_integer(value: int) -> float:
    bit_length = value.bit_length()
    shift = max(0, bit_length - 53)
    mantissa = value >> shift
    return math.log(mantissa) + shift * math.log(2.0)


def threshold_row(n: int) -> tuple[int, int, float, float, float]:
    m_n = n if n % 2 == 1 else n - 1
    m_layers = math.ceil(16.0 * math.log(n) ** 2)
    denominator = 2**m_layers - 1
    l_n = m_n * denominator
    log_l_n = log_big_integer(l_n)

    log_epsilon = math.log(8.0 * m_layers * log_l_n) - log_big_integer(denominator)
    epsilon = 0.0 if log_epsilon < -745.0 else math.exp(log_epsilon)
    p_zero_ceiling = 2.0 * math.exp(epsilon) / (m_n + 1)
    pi_modulus_floor = 1.0 - 2.0 * p_zero_ceiling

    if p_zero_ceiling >= 0.001:
        raise AssertionError(f"zero-state ceiling unexpectedly large for n={n}")
    if pi_modulus_floor <= 0.99:
        raise AssertionError(f"pi modulus floor unexpectedly weak for n={n}")

    return (
        m_n,
        m_layers,
        log_epsilon / math.log(10.0),
        p_zero_ceiling,
        pi_modulus_floor,
    )


def main() -> None:
    for n in (12, 15):
        check_small_exact_support(n)
        print(f"PASS small exact parity and transform checks n={n}")

    print("n m_n M_n log10(epsilon_n) p0_ceiling pi_modulus_floor")
    for n in (120368, 200000, 500000, 1000000):
        m_n, m_layers, log10_epsilon, p_zero, pi_floor = threshold_row(n)
        print(
            f"{n:7d} {m_n:7d} {m_layers:4d} "
            f"{log10_epsilon: .6f} {p_zero: .12e} {pi_floor: .12f}"
        )

    print("PASS: parity twin near-resonance and odd-lattice normalization checks completed")
    print("STATUS: small support construction is exact")
    print("STATUS: characteristic-function equalities are floating-point regressions")
    print("STATUS: threshold rows verify closed-form theorem bounds only")


if __name__ == "__main__":
    main()
