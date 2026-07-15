"""Rigorous rational bounds for logarithmic integer parameters."""

from __future__ import annotations

from fractions import Fraction
from typing import Any


class LogCertificationError(ValueError):
    """Raised when an exact logarithmic ceiling cannot be certified."""


def _require_int(name: str, value: Any, *, minimum: int | None = None) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise LogCertificationError(f"{name} must be an integer")
    if minimum is not None and value < minimum:
        raise LogCertificationError(f"{name} must be at least {minimum}")
    return value


def _ceil_fraction(value: Fraction) -> int:
    return -((-value.numerator) // value.denominator)


def _atanh_log_bounds(
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


def natural_log_bounds(n: int, *, terms: int = 24) -> tuple[Fraction, Fraction]:
    """Return rigorous rational lower and upper bounds for log(n)."""
    n = _require_int("n", n, minimum=1)
    terms = _require_int("terms", terms, minimum=1)
    if n == 1:
        return Fraction(0), Fraction(0)
    exponent = n.bit_length() - 1
    scale = 1 << exponent
    ln2_lower, ln2_upper = _atanh_log_bounds(2, 1, terms)
    ratio_lower, ratio_upper = _atanh_log_bounds(n, scale, terms)
    return (
        exponent * ln2_lower + ratio_lower,
        exponent * ln2_upper + ratio_upper,
    )


def certified_log_parameters(n: int) -> tuple[int, int]:
    """Certify r=ceil(4 log n) and M=ceil(16 (log n)^2)."""
    n = _require_int("n", n, minimum=1)
    for terms in (8, 12, 16, 24, 32, 48, 64, 96):
        lower, upper = natural_log_bounds(n, terms=terms)
        r_values = (_ceil_fraction(4 * lower), _ceil_fraction(4 * upper))
        m_values = (
            _ceil_fraction(16 * lower * lower),
            _ceil_fraction(16 * upper * upper),
        )
        if r_values[0] == r_values[1] and m_values[0] == m_values[1]:
            return r_values[0], m_values[0]
    raise LogCertificationError(f"could not certify logarithmic parameters for n={n}")


def factorial_at_least(n: int, threshold: int) -> bool:
    """Return whether n! >= threshold without building needless large integers."""
    n = _require_int("n", n, minimum=0)
    threshold = _require_int("threshold", threshold, minimum=1)
    product = 1
    for value in range(2, n + 1):
        product *= value
        if product >= threshold:
            return True
    return product >= threshold
