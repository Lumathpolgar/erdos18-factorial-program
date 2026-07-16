from __future__ import annotations

import copy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from factorial_lab.n3_dusart import (  # noqa: E402
    DERIVED_INTEGER_THRESHOLD,
    HANDOFF_COMMIT,
    LOWER_SOURCE_THRESHOLD,
    SOURCE_LEDGER_COMMIT,
    UPPER_SOURCE_THRESHOLD,
    VerificationError,
    algebra_certificate,
    build_audit,
    build_claim,
    decimal_threshold_witness,
    e_upper_bound,
    exp_lower_at_seven_tenths,
    polynomial_lower_at_four,
    semantic_sha256,
    source_threshold_record,
    verify_audit,
    verify_claim,
)


class DusartAuditTests(unittest.TestCase):
    def test_source_threshold_is_exact_unsupplemented_threshold(self) -> None:
        record = source_threshold_record()
        self.assertEqual(DERIVED_INTEGER_THRESHOLD, 2 * UPPER_SOURCE_THRESHOLD)
        self.assertGreater(DERIVED_INTEGER_THRESHOLD, LOWER_SOURCE_THRESHOLD)
        self.assertEqual(record["derived_integer_threshold"], 120368)
        self.assertFalse(record["predecessor"]["upper_source_hypothesis_holds"])

    def test_taylor_bound_proves_log2_upper(self) -> None:
        self.assertGreater(exp_lower_at_seven_tenths(), 2)
        self.assertEqual(algebra_certificate()["ln2_upper"], "7/10")

    def test_elementary_e_upper_proves_log_threshold(self) -> None:
        self.assertLess(e_upper_bound(), 3)
        cert = algebra_certificate()
        self.assertTrue(cert["threshold_exceeds_e4"]["threshold_greater_than_81"])

    def test_polynomial_lower_bound_is_positive(self) -> None:
        self.assertEqual(str(polynomial_lower_at_four()), "18/5")
        self.assertTrue(algebra_certificate()["Q_lower_increasing_for_L_at_least_4"])

    def test_exact_threshold_prime_count(self) -> None:
        witness = decimal_threshold_witness()
        self.assertEqual(witness["pi_n"], 11330)
        self.assertEqual(witness["pi_floor_n_over_2"], 6076)
        self.assertEqual(witness["exact_upper_half_prime_count"], 5254)
        self.assertTrue(witness["source_hypotheses_hold"])

    def test_valid_audit_replays(self) -> None:
        verify_audit(build_audit())

    def test_valid_claim_replays(self) -> None:
        audit = build_audit()
        verify_claim(build_claim(audit), audit)

    def test_rehashed_threshold_below_source_coverage_is_rejected(self) -> None:
        audit = build_audit()
        bad = copy.deepcopy(audit)
        bad["source_thresholds"]["derived_integer_threshold"] = 120367
        bad["sha256"] = semantic_sha256(bad)
        with self.assertRaises(VerificationError):
            verify_audit(bad)

    def test_rehashed_source_threshold_change_is_rejected(self) -> None:
        audit = build_audit()
        bad = copy.deepcopy(audit)
        bad["source_thresholds"]["upper_bound"]["threshold"] = 60183
        bad["sha256"] = semantic_sha256(bad)
        with self.assertRaises(VerificationError):
            verify_audit(bad)

    def test_rehashed_false_predecessor_coverage_is_rejected(self) -> None:
        claim = build_claim()
        bad = copy.deepcopy(claim)
        bad["claim"]["predecessor_covered_without_supplement"] = True
        bad["sha256"] = semantic_sha256(bad)
        with self.assertRaises(VerificationError):
            verify_claim(bad)

    def test_wrong_frozen_source_metadata_is_rejected(self) -> None:
        audit = build_audit()
        bad = copy.deepcopy(audit)
        bad["source"]["handoff_commit"] = "0" * 40
        bad["sha256"] = semantic_sha256(bad)
        with self.assertRaises(VerificationError):
            verify_audit(bad)
        self.assertNotEqual(HANDOFF_COMMIT, SOURCE_LEDGER_COMMIT)

    def test_committed_corrupted_fixture_is_rejected(self) -> None:
        fixture = ROOT / "tests" / "n3_dusart_fixtures" / "corrupt_rehashed_threshold.json"
        bad = json.loads(fixture.read_text(encoding="utf-8"))
        self.assertEqual(bad["sha256"], semantic_sha256(bad))
        with self.assertRaises(VerificationError):
            verify_claim(bad)


if __name__ == "__main__":
    unittest.main()
