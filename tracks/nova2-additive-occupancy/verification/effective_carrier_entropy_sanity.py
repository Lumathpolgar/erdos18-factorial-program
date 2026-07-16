#!/usr/bin/env python3
"""Exact algebra checks for N2-ADD-122."""

from fractions import Fraction


def check_case(w: int, y: int, rows: list[tuple[int, int, int]]) -> None:
    f0 = w + 1
    f = f0
    prefix_product = 1
    utilization_product = Fraction(1, 1)

    for scale, count, maximum in rows:
        threshold = f // scale
        assert 0 <= maximum <= count * threshold
        expansion = Fraction(scale * maximum, f)
        utilization = (1 + expansion) / (count + 1)
        assert 0 < utilization <= 1
        prefix_product *= count + 1
        utilization_product *= utilization
        f += scale * maximum

    assert Fraction(f, f0) == prefix_product * utilization_product
    assert (f >= y + 1) == (
        Fraction(prefix_product, 1) * utilization_product
        >= Fraction(y + 1, f0)
    )


def main() -> None:
    check_case(8, 20, [(1, 3, 6), (2, 2, 5)])
    check_case(15, 200, [(1, 8, 16), (2, 4, 20), (4, 2, 24)])
    check_case(31, 1000, [(1, 12, 31), (2, 9, 72), (4, 7, 140)])
    print("PASS N2-ADD-122 effective carrier entropy identities")


if __name__ == "__main__":
    main()
