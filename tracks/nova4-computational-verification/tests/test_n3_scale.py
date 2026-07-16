from __future__ import annotations

import copy
import sys
import unittest
from decimal import Decimal, localcontext
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from factorial_lab.n3_scale import (
    ScaleEvidenceError,
    build_evidence,
    high_prime_tail_row,
    primes_up_to,
    scale_row,
    semantic_sha,
    valuation_factorial,
    verify_evidence,
)


class N3ScaleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.small = build_evidence((50, 100), (2, 5, 10), proxy_prime_limit=10000)

    def test_sieve_and_valuation(self):
        self.assertEqual(primes_up_to(20), [2, 3, 5, 7, 11, 13, 17, 19])
        self.assertEqual(valuation_factorial(100, 2), 97)
        self.assertEqual(valuation_factorial(100, 5), 24)

    def test_scale_row_structure(self):
        row = scale_row(50)
        self.assertEqual(row["prime_count"], 15)
        self.assertGreater(Decimal(row["variance_over_n_squared"]), Decimal(0))
        self.assertGreater(Decimal(row["effective_dimension"]), Decimal(1))

    def test_prime_shares_are_consistent(self):
        row = scale_row(1000)
        shares = [Decimal(row["variance_shares"][str(p)]) for p in (2, 3, 5, 7)]
        with localcontext() as ctx:
            ctx.prec = 80
            self.assertLess(
                abs(sum(shares, Decimal(0)) - Decimal(row["tracked_prime_share_total"])),
                Decimal("1e-45"),
            )
        self.assertLess(sum(shares), Decimal(1))

    def test_tail_uses_theorem_half_span(self):
        row = high_prime_tail_row(1000, 20)
        self.assertEqual(Decimal(row["supplied_script_to_theorem_ratio"]), Decimal(2))
        with localcontext() as ctx:
            ctx.prec = 80
            self.assertLess(
                abs(
                    Decimal(row["supplied_script_span_over_B"])
                    - Decimal(2) * Decimal(row["M_over_B"])
                ),
                Decimal("1e-45"),
            )

    def test_hypothesis_flag(self):
        self.assertTrue(
            high_prime_tail_row(10000, 50)["theorem_hypothesis_2y_le_sqrt_n"]
        )
        self.assertFalse(
            high_prime_tail_row(1000, 20)["theorem_hypothesis_2y_le_sqrt_n"]
        )

    def test_semantic_replay(self):
        result = verify_evidence(self.small)
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(
            result["tail_ratio_script_decision"],
            "NEEDS_REPAIR_FOR_TAIL_RATIO_LABEL",
        )

    def test_rehashed_corrupt_ratio_rejected(self):
        bad = copy.deepcopy(self.small)
        bad["high_prime_tail_rows"][0]["M_over_B"] = "9.0E+0"
        bad["sha256"] = semantic_sha(bad)
        with self.assertRaises(ScaleEvidenceError):
            verify_evidence(bad)

    def test_rehashed_corrupt_share_rejected(self):
        bad = copy.deepcopy(self.small)
        bad["scale_rows"][0]["variance_shares"]["2"] = "0E+0"
        bad["sha256"] = semantic_sha(bad)
        with self.assertRaises(ScaleEvidenceError):
            verify_evidence(bad)

    def test_frozen_script_numeric_crosscheck(self):
        comparison = self.small["supplied_script_comparison"]
        self.assertLess(
            Decimal(comparison["maximum_scale_absolute_difference"]),
            Decimal("1e-14"),
        )

    def test_wrong_source_rejected(self):
        bad = copy.deepcopy(self.small)
        bad["source"]["commit"] = "0" * 40
        bad["sha256"] = semantic_sha(bad)
        with self.assertRaises(ScaleEvidenceError):
            verify_evidence(bad)

    def test_theorem_path_is_admissible_and_decreases_end_to_end(self):
        rows = self.small["theorem_path_rows"]
        self.assertTrue(
            all(row["theorem_hypothesis_2y_le_sqrt_n"] for row in rows)
        )
        self.assertGreater(
            Decimal(rows[0]["M_over_B"]), Decimal(rows[-1]["M_over_B"])
        )

    def test_grid_counts(self):
        self.assertEqual(len(self.small["scale_rows"]), 2)
        self.assertEqual(len(self.small["high_prime_tail_rows"]), 6)
        self.assertEqual(len(self.small["theorem_path_rows"]), 2)


if __name__ == "__main__":
    unittest.main()
