from __future__ import annotations
import copy
import json
from pathlib import Path
import unittest

from factorial_lab.n3_sources import (
    SourceAuditError,
    build_audit,
    compatibility_claim,
    ford_witness,
    drappeau_tenenbaum_witness,
    ultrafriable_witness,
    semantic_sha,
    verify_audit,
    verify_claim,
)


class SourceAuditTests(unittest.TestCase):
    def test_ford_witness(self):
        row = ford_witness()
        self.assertEqual(row["H_factorial_y_z"], 17)
        self.assertEqual(row["tau_factorial_y_z"], 0)

    def test_drappeau_tenenbaum_scope(self):
        row = drappeau_tenenbaum_witness()
        self.assertTrue(row["factorial_is_in_S_x_y"])
        self.assertFalse(row["source_nonexceptional_certificate_for_factorial"])

    def test_ultrafriable_witness(self):
        row = ultrafriable_witness()
        self.assertEqual(row["v_2_factorial"], 8)
        self.assertFalse(row["common_y_exact_support_possible"])

    def test_audit_replay(self):
        result = verify_audit(build_audit())
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["direct_factorial_sources"], 0)

    def test_claim_replay(self):
        audit = build_audit()
        result = verify_claim(compatibility_claim(audit))
        self.assertEqual(result["status"], "PASS")

    def test_rehashed_false_direct_use_rejected(self):
        audit = build_audit()
        bad = copy.deepcopy(audit)
        bad["sources"][0]["factorial_sequence_selected"] = True
        bad["sources"][0]["direct_factorial_use"] = "ACCEPTED"
        bad["sha256"] = semantic_sha(bad)
        with self.assertRaises(SourceAuditError):
            verify_audit(bad)

    def test_rehashed_exception_removal_rejected(self):
        audit = build_audit()
        bad = copy.deepcopy(audit)
        bad["sources"][1]["quantifier_scope"] = "all y-friable integers"
        bad["sha256"] = semantic_sha(bad)
        with self.assertRaises(SourceAuditError):
            verify_audit(bad)

    def test_rehashed_ultrafriable_equality_rejected(self):
        audit = build_audit()
        bad = copy.deepcopy(audit)
        bad["witnesses"]["ultrafriable_common_cap_mismatch"]["common_y_exact_support_possible"] = True
        bad["sha256"] = semantic_sha(bad)
        with self.assertRaises(SourceAuditError):
            verify_audit(bad)

    def test_wrong_source_commit_rejected(self):
        audit = build_audit()
        bad = copy.deepcopy(audit)
        bad["source"]["handoff_commit"] = "0" * 40
        bad["sha256"] = semantic_sha(bad)
        with self.assertRaises(SourceAuditError):
            verify_audit(bad)

    def test_on_disk_corrupt_fixture_rejected(self):
        path = Path(__file__).parent / "n3_source_fixtures" / "corrupt_rehashed_direct_use.json"
        bad = json.loads(path.read_text(encoding="utf-8"))
        with self.assertRaises(SourceAuditError):
            verify_claim(bad)


if __name__ == "__main__":
    unittest.main()
