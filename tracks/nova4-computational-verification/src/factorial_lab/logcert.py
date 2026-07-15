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


def _certified_scaled_log_leq(n: int, k: int, *, square: bool) -> bool:
    """Certify 4 log(n)<=k or 16 log(n)^2<=k with adaptive rational bounds."""
    n = _require_int("n", n, minimum=1)
    k = _require_int("k", k, minimum=0)
    for terms in (8, 12, 16, 24, 32, 48, 64, 96):
        lower, upper = natural_log_bounds(n, terms=terms)
        if square:
            low_value = 16 * lower * lower
            high_value = 16 * upper * upper
        else:
            low_value = 4 * lower
            high_value = 4 * upper
        if high_value <= k:
            return True
        if low_value > k:
            return False
    raise LogCertificationError(
        f"could not certify scaled logarithm comparison for n={n}, k={k}"
    )


def _parameter_upper_boundaries(n_max: int, *, square: bool) -> list[int]:
    """Return upper[k]=max n<=n_max with f(n)<=k for monotone f."""
    n_max = _require_int("n_max", n_max, minimum=1)
    r_max, m_max = certified_log_parameters(n_max)
    k_max = m_max if square else r_max
    upper = [0] * (k_max + 1)
    lo_floor = 0
    for k in range(k_max + 1):
        lo = lo_floor
        hi = n_max
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if _certified_scaled_log_leq(mid, k, square=square):
                lo = mid
            else:
                hi = mid - 1
        upper[k] = lo
        lo_floor = lo
        if lo == n_max:
            for rest in range(k + 1, k_max + 1):
                upper[rest] = n_max
            break
    return upper


def certified_log_parameter_tables(n_max: int) -> tuple[list[int], list[int]]:
    """Build exact r_n and M_n tables from certified monotone thresholds."""
    n_max = _require_int("n_max", n_max, minimum=1)
    r_upper = _parameter_upper_boundaries(n_max, square=False)
    m_upper = _parameter_upper_boundaries(n_max, square=True)
    r_values = [0] * (n_max + 1)
    m_values = [0] * (n_max + 1)

    def fill(values: list[int], upper: list[int]) -> None:
        previous = 0
        for k, boundary in enumerate(upper):
            if boundary > previous:
                for n in range(previous + 1, boundary + 1):
                    values[n] = k
                previous = boundary
            if previous == n_max:
                break
        if previous != n_max:
            raise LogCertificationError("parameter boundary table did not cover full range")

    fill(r_values, r_upper)
    fill(m_values, m_upper)
    for values in (r_values, m_values):
        prior = None
        for n in range(1, n_max + 1):
            if values[n] != prior:
                r, m = certified_log_parameters(n)
                expected = m if values is m_values else r
                if values[n] != expected:
                    raise LogCertificationError(f"transition table mismatch at n={n}")
                prior = values[n]
    return r_values, m_values
