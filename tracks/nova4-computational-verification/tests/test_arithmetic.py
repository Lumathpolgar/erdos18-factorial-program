from __future__ import annotations

import sys
import unittest
from math import factorial
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from factorial_lab.arithmetic import (  # noqa: E402
    divisor_count_from_valuations,
    divisors_of_factorial,
    factorial_prime_valuations,
    is_divisor_of_factorial,
    prime_sieve,
)


class ArithmeticTests(unittest.TestCase):
    def test_prime_sieve(self) -> None:
        self.assertEqual(prime_sieve(1), [])
        self.assertEqual(prime_sieve(10), [2, 3, 5, 7])

    def test_factorial_valuations(self) -> None:
        self.assertEqual(factorial_prime_valuations(10), {2: 8, 3: 4, 5: 2, 7: 1})

    def test_divisor_generation_and_count(self) -> None:
        valuations = factorial_prime_valuations(10)
        divisors = divisors_of_factorial(10)
        self.assertEqual(len(divisors), divisor_count_from_valuations(valuations))
        self.assertEqual(len(divisors), 270)
        self.assertEqual(divisors, sorted(set(divisors)))
        self.assertTrue(all(factorial(10) % d == 0 for d in divisors))

    def test_truncated_divisors_are_complete(self) -> None:
        full = divisors_of_factorial(9)
        truncated = divisors_of_factorial(9, max_value=100)
        self.assertEqual(truncated, [d for d in full if d <= 100])

    def test_divisibility(self) -> None:
        self.assertTrue(is_divisor_of_factorial(72, 10))
        self.assertFalse(is_divisor_of_factorial(11, 10))
        self.assertFalse(is_divisor_of_factorial(0, 10))
        self.assertFalse(is_divisor_of_factorial(-1, 10))


if __name__ == "__main__":
    unittest.main()
