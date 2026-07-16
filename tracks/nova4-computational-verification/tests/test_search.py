from __future__ import annotations

import itertools
import sys
import unittest
from math import factorial, isqrt
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from factorial_lab.arithmetic import divisors_of_factorial  # noqa: E402
from factorial_lab.certificates import (  # noqa: E402
    make_representation_certificate,
    verify_representation_certificate,
)
from factorial_lab.search import (  # noqa: E402
    certify_profile_with_bitsets,
    exact_profile_dp,
)


def brute_min_count(divisors: list[int], target: int) -> int:
    for count in range(len(divisors) + 1):
        for subset in itertools.combinations(divisors, count):
            if sum(subset) == target:
                return count
    raise AssertionError(f"target {target} is not represented")


class SearchTests(unittest.TestCase):
    def test_dp_matches_bruteforce_on_small_factorials(self) -> None:
        for n in range(1, 7):
            limit = min(30, isqrt(factorial(n)))
            profile = exact_profile_dp(n, limit)
            divisors = [d for d in divisors_of_factorial(n) if d <= limit]
            for target in range(limit + 1):
                self.assertEqual(
                    profile.lambda_values[target], brute_min_count(divisors, target)
                )

    def test_independent_bitset_optimality(self) -> None:
        for n in range(1, 10):
            profile = exact_profile_dp(n)
            certify_profile_with_bitsets(profile)

    def test_every_dp_witness_replays(self) -> None:
        profile = exact_profile_dp(9)
        for target, witness in enumerate(profile.witnesses):
            certificate = make_representation_certificate(
                n=9,
                target=target,
                divisors=witness,
                max_terms=profile.lambda_values[target],
                target_range=(0, profile.target_limit + 1),
            )
            verify_representation_certificate(certificate)


if __name__ == "__main__":
    unittest.main()
