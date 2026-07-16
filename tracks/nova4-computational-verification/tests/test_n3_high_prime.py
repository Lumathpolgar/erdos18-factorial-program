import copy
import json
import math
import unittest
from pathlib import Path

from factorial_lab.n3_high_prime import (
    VerificationError,
    build_audit,
    build_claim_008,
    build_claim_009,
    corrupted_claims_008,
    corrupted_claims_009,
    semantic_sha256,
    tail_statistics,
    verify_audit,
    verify_claim_008,
    verify_claim_009,
)


class HighPrimeAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.audit = build_audit()
        cls.claim_008 = build_claim_008(cls.audit)
        cls.claim_009 = build_claim_009(cls.audit)

    def test_decisions(self):
        self.assertEqual(self.audit["decisions"]["N3_ANA_008"], "ACCEPTED")
        self.assertEqual(
            self.audit["decisions"]["N3_ANA_009"],
            "ACCEPTED_WITH_EXTERNAL_BERRY_ESSEEN_DEPENDENCY",
        )

    def test_half_span_normalization(self):
        row = tail_statistics(10_000, 50)
        self.assertAlmostEqual(float(row["full_span"]), 2.0 * float(row["theorem_half_span_M"]))
        self.assertAlmostEqual(float(row["full_span_over_B"]), 2.0 * float(row["M_over_B"]))

    def test_admissible_path(self):
        for row in self.audit["finite_diagnostics"]["rows"]:
            self.assertTrue(row["admissible_2y_le_sqrt_n"])

    def test_ratio_decreases_on_diagnostic_path(self):
        ratios = [float(row["M_over_B"]) for row in self.audit["finite_diagnostics"]["rows"]]
        self.assertEqual(ratios, sorted(ratios, reverse=True))
        self.assertLess(ratios[-1], 0.12)

    def test_variance_scale_positive(self):
        for row in self.audit["finite_diagnostics"]["rows"]:
            self.assertGreater(float(row["variance_over_n2_logy_over_y"]), 0.08)

    def test_phi2_constant(self):
        expected = math.exp(-2.0) / math.sqrt(2.0 * math.pi)
        actual = float(self.audit["N3_ANA_009"]["explicit_constants"]["phi_2_decimal"])
        self.assertAlmostEqual(actual, expected, places=15)

    def test_verify_all(self):
        verify_audit(self.audit)
        verify_claim_008(self.claim_008, self.audit)
        verify_claim_009(self.claim_009, self.audit)

    def test_all_generated_008_corruptions_rejected(self):
        for name, item in corrupted_claims_008(self.claim_008).items():
            with self.subTest(name=name):
                with self.assertRaises(VerificationError):
                    verify_claim_008(item, self.audit)

    def test_all_generated_009_corruptions_rejected(self):
        for name, item in corrupted_claims_009(self.claim_009).items():
            with self.subTest(name=name):
                with self.assertRaises(VerificationError):
                    verify_claim_009(item, self.audit)

    def test_committed_fixtures_rejected(self):
        fixture_dir = Path(__file__).parent / "n3_high_prime_fixtures"
        files = sorted(fixture_dir.glob("*.json"))
        self.assertEqual(len(files), 8)
        for path in files:
            item = json.loads(path.read_text(encoding="utf-8"))
            with self.subTest(path=path.name):
                with self.assertRaises(VerificationError):
                    if "008-final-claim" in item.get("schema", ""):
                        verify_claim_008(item, self.audit)
                    else:
                        verify_claim_009(item, self.audit)

    def test_wrong_source_rejected(self):
        item = copy.deepcopy(self.claim_008)
        item["source"]["proof_file_blob_sha"] = "0" * 40
        item["sha256"] = semantic_sha256(item)
        with self.assertRaises(VerificationError):
            verify_claim_008(item, self.audit)

    def test_wrong_evidence_rejected(self):
        item = copy.deepcopy(self.claim_009)
        item["evidence_sha256"] = "0" * 64
        item["sha256"] = semantic_sha256(item)
        with self.assertRaises(VerificationError):
            verify_claim_009(item, self.audit)

    def test_scope_guards(self):
        excluded = self.audit["scope_excludes"]
        self.assertIn("additive occupancy", excluded)
        self.assertIn("Erdos Problem 18", excluded)
        self.assertTrue(self.audit["N3_ANA_009"]["semantic_guards"]["coarse_windows_only"])


if __name__ == "__main__":
    unittest.main()
