from __future__ import annotations

from fractions import Fraction
import json


def ceil_fraction(value: Fraction) -> int:
    return -((-value.numerator) // value.denominator)


def atanh_log_bounds(
    numerator: int, denominator: int, terms: int
) -> tuple[Fraction, Fraction]:
    if numerator < denominator or numerator > 2 * denominator:
        raise ValueError("ratio must lie in [1, 2]")
    if numerator == denominator:
        return Fraction(0), Fraction(0)
    z = Fraction(numerator - denominator, numerator + denominator)
    z2 = z * z
    power = z
    partial = Fraction(0)
    for j in range(terms):
        partial += power / (2 * j + 1)
        power *= z2
    lower = 2 * partial
    tail_upper = 2 * power / ((2 * terms + 1) * (1 - z2))
    return lower, lower + tail_upper


def natural_log_bounds(n: int, terms: int = 24) -> tuple[Fraction, Fraction]:
    if n < 1:
        raise ValueError("n must be positive")
    if n == 1:
        return Fraction(0), Fraction(0)
    exponent = n.bit_length() - 1
    scale = 1 << exponent
    ln2_lower, ln2_upper = atanh_log_bounds(2, 1, terms)
    ratio_lower, ratio_upper = atanh_log_bounds(n, scale, terms)
    return (
        exponent * ln2_lower + ratio_lower,
        exponent * ln2_upper + ratio_upper,
    )


def certified_parameters(n: int) -> tuple[int, int]:
    for terms in (8, 12, 16, 24, 32, 48, 64, 96):
        lower, upper = natural_log_bounds(n, terms)
        r_pair = (ceil_fraction(4 * lower), ceil_fraction(4 * upper))
        m_pair = (
            ceil_fraction(16 * lower * lower),
            ceil_fraction(16 * upper * upper),
        )
        if r_pair[0] == r_pair[1] and m_pair[0] == m_pair[1]:
            return r_pair[0], m_pair[0]
    raise ArithmeticError(f"could not certify logarithmic parameters for n={n}")


def factorial_valuation(n: int, p: int) -> int:
    if n < 0 or p < 2:
        raise ValueError("invalid factorial valuation parameters")
    total = 0
    quotient = n
    while quotient:
        quotient //= p
        total += quotient
    return total


def admissible(n: int) -> bool:
    r, layer_count = certified_parameters(n)
    return (
        n >= 7
        and r + layer_count <= factorial_valuation(n, 2) // 2 - 1
    )


def spine_witness(q: int, layer_count: int) -> list[tuple[int, int]]:
    """Return exact `(layer, quotient_value)` terms for a covered odd q."""
    if layer_count < 1:
        raise ValueError("layer_count must be positive")
    if q < 3 or q % 2 == 0:
        raise ValueError("q must be odd and at least 3")
    base = {3: 3, 5: 5, 1: 7}[q % 6]
    k = (q - base) // 6
    if k < 0 or k >= (1 << (layer_count - 1)):
        raise ValueError("q is outside the binary-spine prefix")

    witness = [(1, base)]
    bit = 0
    while k:
        if k & 1:
            layer = bit + 2
            witness.append((layer, 3 * (1 << (layer - 1))))
        k >>= 1
        bit += 1
    return witness


def verify_small_layer_counts(max_layers: int = 12) -> None:
    """Exhaustively replay the symbolic construction for small layer counts."""
    for layer_count in range(1, max_layers + 1):
        endpoint = 3 * (1 << layer_count)
        represented = {0}
        for q in range(3, endpoint - 2, 2):
            witness = spine_witness(q, layer_count)
            layers = [layer for layer, _ in witness]
            assert len(set(layers)) == len(layers)
            assert sum(value for _, value in witness) == q
            assert all(1 <= layer <= layer_count for layer in layers)
            represented.add(q)

        for target in range(endpoint + 1):
            window = range(max(0, target - 3), target + 1)
            assert any(value in represented for value in window), (
                layer_count,
                target,
            )


def first_admissible_n(n_max: int) -> int | None:
    for n in range(7, n_max + 1):
        if admissible(n):
            return n
    return None


def main() -> None:
    verify_small_layer_counts()

    first = first_admissible_n(5000)
    if first != 1892:
        raise AssertionError(f"unexpected first admissible n: {first}")

    r, layer_count = certified_parameters(first)
    endpoint = 3 * (1 << layer_count)
    output = {
        "schema": "nova2.quotient-binary-spine.v1",
        "result_class": "finite certificate",
        "first_admissible_n_through_5000": first,
        "r": r,
        "M": layer_count,
        "v2_factorial": factorial_valuation(first, 2),
        "v3_factorial": factorial_valuation(first, 3),
        "guaranteed_quotient_window_endpoint": str(endpoint),
        "endpoint_decimal_digits": len(str(endpoint)),
        "small_layer_counts_verified_through": 12,
    }
    print(json.dumps(output, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
