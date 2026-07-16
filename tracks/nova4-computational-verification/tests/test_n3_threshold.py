from pathlib import Path
import unittest

from factorial_lab.n3_threshold import *


class ThresholdSweepTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.audit = build_audit()
        cls.claim = build_claim(cls.audit)

    def test_range(self):
        self.assertEqual(self.audit["range"]["integer_count"], 879633)

    def test_prime_minimum(self):
        self.assertEqual(self.audit["minima"]["prime_margin"]["row"]["n"], 120370)

    def test_legendre_minimum(self):
        self.assertEqual(
            self.audit["minima"]["legendre_lower_bound_margin"]["row"]["n"],
            131071,
        )

    def test_address_minimum(self):
        self.assertEqual(
            self.audit["minima"]["address_slack"]["minimizing_n"],
            [120368, 120369, 120370, 120371],
        )

    def test_capacity_minimum(self):
        self.assertEqual(
            self.audit["minima"]["capacity_margin_bits"]["row"]["n"], 120370
        )

    def test_parameters(self):
        self.assertEqual(certified_log_parameters(120368), (47, 2190))

    def test_valuation_dual(self):
        self.assertEqual(
            valuation_two_legendre(1_000_000),
            valuation_two_digit_sum(1_000_000),
        )

    def test_verify(self):
        verify_audit(self.audit)
        verify_claim(self.claim, self.audit)

    def test_committed_corrupt_rehashed_fixture(self):
        fixture = (
            Path(__file__).parent
            / "n3_threshold_fixtures"
            / "corrupt_rehashed_minimum_slack.json"
        )
        corrupted = load_json(fixture)
        with self.assertRaises(VerificationError):
            verify_claim(corrupted, self.audit)

    def test_wrong_range(self):
        with self.assertRaises(ValueError):
            build_audit(120367, 1_000_000)

    def test_finite_only(self):
        self.assertTrue(self.claim["claim"]["finite_only"])

    def test_floor_endpoint(self):
        self.assertEqual(
            self.audit["range"]["endpoint_semantics"],
            "pi(n/2)=pi(floor(n/2))",
        )


if __name__ == "__main__":
    unittest.main()
