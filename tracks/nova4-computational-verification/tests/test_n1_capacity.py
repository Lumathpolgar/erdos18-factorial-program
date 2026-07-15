import copy
import unittest

from factorial_lab.n1_capacity import (
    CapacityCertificationError,
    audit_n1_capacity_range,
    verify_n1_capacity_audit,
)


class N1CapacityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.audit = audit_n1_capacity_range(3, 10_000)

    def test_exact_transitions_and_thresholds(self):
        self.assertEqual(
            self.audit["first_success"], {"A": 1892, "C": 3, "both": 1892}
        )
        self.assertEqual(
            self.audit["later_failures_after_first_success"]["A"], [1893, 1894, 1895]
        )
        self.assertEqual(self.audit["later_failures_after_first_success"]["C"], [10])
        self.assertEqual(
            [(row["n"], row["A"], row["C"]) for row in self.audit["transitions"]],
            [
                (3, False, True),
                (10, False, False),
                (11, False, True),
                (1892, True, True),
                (1893, False, True),
                (1896, True, True),
            ],
        )

    def test_margin_minima(self):
        minima = self.audit["C_success_interval_minimum_margins"]
        self.assertEqual(minima[0]["interval"], [3, 9])
        self.assertEqual(minima[0]["minimum_certified_at_n"], 6)
        self.assertEqual(minima[1]["interval"], [11, 10_000])
        self.assertEqual(minima[1]["minimum_certified_at_n"], 11)

    def test_replay(self):
        result = verify_n1_capacity_audit(self.audit)
        self.assertEqual(result["status"], "PASS")

    def test_corrupted_checksum_rejected(self):
        corrupted = copy.deepcopy(self.audit)
        corrupted["first_success"]["A"] = 1891
        with self.assertRaises(CapacityCertificationError):
            verify_n1_capacity_audit(corrupted)

    def test_rehashed_false_claim_rejected(self):
        corrupted = copy.deepcopy(self.audit)
        corrupted["later_failures_after_first_success"]["C"] = []
        from factorial_lab.n1_capacity import _sha256_payload
        payload = {k: v for k, v in corrupted.items() if k != "sha256"}
        corrupted["sha256"] = _sha256_payload(payload)
        with self.assertRaises(CapacityCertificationError):
            verify_n1_capacity_audit(corrupted)

    def test_on_disk_capacity_fixtures(self):
        import json
        from pathlib import Path
        valid_path = Path(__file__).parent / "capacity_fixtures" / "valid_n1_capacity_n3_n10000.json"
        corrupt_path = Path(__file__).parent / "capacity_fixtures" / "corrupt_rehashed_threshold.json"
        with valid_path.open() as handle:
            self.assertEqual(verify_n1_capacity_audit(json.load(handle))["status"], "PASS")
        with corrupt_path.open() as handle:
            with self.assertRaises(CapacityCertificationError):
                verify_n1_capacity_audit(json.load(handle))


if __name__ == "__main__":
    unittest.main()
