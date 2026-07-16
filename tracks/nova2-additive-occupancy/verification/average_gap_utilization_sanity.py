#!/usr/bin/env python3
"""Exact algebra checks for N2-OBS-109 and N2-ADD-123."""

from fractions import Fraction


def obstruction_case(d: int) -> None:
    assert d >= 4 and d % 2 == 0
    k = d
    f = d
    scale = 1
    gap = d + 2

    dense = [2 * i - 1 for i in range(1, k + 1)]
    packed = [i * d - 1 for i in range(1, k + 1)]

    for seq in (dense, packed):
        gaps = [seq[0]] + [b - a for a, b in zip(seq, seq[1:])]
        assert len(seq) == k
        assert all(x % 2 == 1 for x in seq)
        assert max(gaps) <= d
        assert gap > d and gap % 2 == 0

    eta_dense = Fraction(dense[-1], k * d)
    eta_packed = Fraction(packed[-1], k * d)
    phi = Fraction(scale * d, f)
    b_dense = Fraction(1, 1) + k * eta_dense * phi
    b_dense /= k + 1
    b_packed = Fraction(1, 1) + k * eta_packed * phi
    b_packed /= k + 1

    assert eta_dense == Fraction(2 * d - 1, d * d)
    assert eta_packed == Fraction(d * d - 1, d * d)
    assert b_dense == Fraction(3 * d - 1, d * (d + 1))
    assert b_packed == 1 - Fraction(1, d * (d + 1))
    assert Fraction(gap, d) == 1 + Fraction(2, d)
    assert b_dense < b_packed


def sandwich_case(f: int, scale: int, k: int, maximum: int) -> None:
    d = f // scale
    assert d >= 1 and k >= 1
    assert 0 <= maximum <= k * d

    eta = Fraction(maximum, k * d)
    phi = Fraction(scale * d, f)
    b = (Fraction(1, 1) + k * eta * phi) / (k + 1)

    assert Fraction(d, d + 1) < phi <= 1
    lower = (Fraction(1, 1) + k * eta * Fraction(d, d + 1)) / (k + 1)
    upper = (Fraction(1, 1) + k * eta) / (k + 1)
    assert lower < b <= upper


def main() -> None:
    for d in (4, 10, 100, 1000):
        obstruction_case(d)

    sandwich_case(101, 4, 20, 300)
    sandwich_case(10_003, 32, 500, 100_000)
    sandwich_case(1_000_003, 128, 10_000, 50_000_000)

    print("PASS N2-OBS-109 and N2-ADD-123 exact checks")


if __name__ == "__main__":
    main()
