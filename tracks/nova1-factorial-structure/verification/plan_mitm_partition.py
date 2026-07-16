#!/usr/bin/env python3
"""Exact partition planner for the Nova 1 meet-in-the-middle divisor stream."""

from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class Coordinate:
    prime: int
    exponent: int

    @property
    def count(self) -> int:
        return self.exponent + 1


def primes_up_to(n: int) -> list[int]:
    sieve = [True] * (n + 1)
    if n >= 0:
        sieve[0] = False
    if n >= 1:
        sieve[1] = False
    out: list[int] = []
    for p in range(2, n + 1):
        if not sieve[p]:
            continue
        out.append(p)
        if p * p <= n:
            for q in range(p * p, n + 1, p):
                sieve[q] = False
    return out


def valuation_factorial(n: int, p: int) -> int:
    total = 0
    value = n
    while value:
        value //= p
        total += value
    return total


def odd_core_coordinates(n: int) -> list[Coordinate]:
    coordinates: list[Coordinate] = []
    for p in primes_up_to(n):
        if p == 2:
            continue
        exponent = valuation_factorial(n, p)
        if p == 3:
            exponent -= 1
        if exponent > 0:
            coordinates.append(Coordinate(p, exponent))
    return coordinates


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int)
    parser.add_argument("--max-columns", type=int, default=3_000_000)
    parser.add_argument("--limit", type=int, default=10)
    args = parser.parse_args()
    if args.n < 3:
        raise SystemExit("n must be at least 3")
    if args.max_columns < 1:
        raise SystemExit("max-columns must be positive")
    if args.limit < 1:
        raise SystemExit("limit must be positive")

    coordinates = odd_core_coordinates(args.n)
    if len(coordinates) >= 63:
        raise SystemExit("coordinate count exceeds exact mask range")

    total = 1
    for coordinate in coordinates:
        total *= coordinate.count

    candidates: list[tuple[int, int, int]] = []
    for mask in range(1 << len(coordinates)):
        left = 1
        for index, coordinate in enumerate(coordinates):
            if (mask >> index) & 1:
                left *= coordinate.count
        right = total // left
        rows = min(left, right)
        columns = max(left, right)
        if columns <= args.max_columns:
            candidates.append((rows, columns, mask))

    candidates.sort()
    print("schema=nova1.marker-three-mitm-partition-plan.v1")
    print("result_class=finite certificate")
    print(f"n={args.n}")
    print(f"coordinate_count={len(coordinates)}")
    print(f"total_odd_core_divisor_count={total}")
    print(f"max_columns={args.max_columns}")
    print(f"candidate_count={len(candidates)}")
    for rank, (rows, columns, mask) in enumerate(candidates[: args.limit], start=1):
        print(f"rank={rank},mask={mask},rows={rows},columns={columns}")


if __name__ == "__main__":
    main()
