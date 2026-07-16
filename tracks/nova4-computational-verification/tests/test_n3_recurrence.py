from __future__ import annotations
import copy, json, sys, unittest
from decimal import Decimal
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from factorial_lab.n3_recurrence import (
    RecurrenceEvidenceError, _decimal_candidate, build_evidence,
    candidate_certificate, decimal_pi, semantic_sha, verify_candidate,
    verify_evidence,
)

class RecurrenceEvidenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.small = build_evidence((3,5,7,11,12),q_min=1000,q_max=5000,blocks=((1000,1999),(2000,5000)),top_k=4,precision=70)

    def test_pi_precision(self):
        self.assertTrue(str(decimal_pi(60)).startswith("3.14159265358979323846264338327950288419716939937510"))

    def test_anchor_return_and_modulus(self):
        row=_decimal_candidate(12,1161483,80)
        self.assertEqual(Decimal(row["phase_residual_cycles"]["2"]),Decimal(0))
        self.assertGreater(Decimal(row["phi_abs"]),Decimal("0.996"))
        self.assertLess(Decimal(row["crosscheck_abs_error"]),Decimal("1e-12"))

    def test_small_search_replay(self):
        result=verify_evidence(self.small)
        self.assertEqual(result["status"],"PASS")
        self.assertEqual(result["q_count"],4001)

    def test_n_values_and_blocks(self):
        self.assertEqual(self.small["search"]["n_values"],[3,5,7,11,12])
        self.assertEqual(len(self.small["block_rows"]),10)
        self.assertEqual(len(self.small["best_rows"]),5)

    def test_direct_crosscheck(self):
        for row in self.small["best_rows"]:
            self.assertLess(Decimal(row["crosscheck_abs_error"]),Decimal("1e-12"))

    def test_candidate_replay(self):
        cert=candidate_certificate(self.small,12)
        self.assertEqual(verify_candidate(cert)["status"],"PASS")

    def test_rehashed_phi_corruption_rejected(self):
        cert=candidate_certificate(self.small,12)
        bad=copy.deepcopy(cert);bad["candidate"]["phi_abs"]="1.000000000000000000000000000000000000000000000000000000000000E+0";bad["sha256"]=semantic_sha(bad)
        with self.assertRaises(RecurrenceEvidenceError):verify_candidate(bad)

    def test_rehashed_q_corruption_rejected(self):
        cert=candidate_certificate(self.small,12)
        bad=copy.deepcopy(cert);bad["candidate"]["q"]+=1;bad["sha256"]=semantic_sha(bad)
        with self.assertRaises(RecurrenceEvidenceError):verify_candidate(bad)

    def test_wrong_source_rejected(self):
        bad=copy.deepcopy(self.small);bad["source"]["proof_commit"]="0"*40;bad["sha256"]=semantic_sha(bad)
        with self.assertRaises(RecurrenceEvidenceError):verify_evidence(bad)

    def test_rehashed_cached_crosscheck_rejected(self):
        cert=candidate_certificate(self.small,12)
        bad=copy.deepcopy(cert);bad["candidate"]["direct_divisor_vector_phi_abs"]="0.5";bad["sha256"]=semantic_sha(bad)
        with self.assertRaises(RecurrenceEvidenceError):verify_candidate(bad)

    def test_on_disk_rehashed_candidate_rejected(self):
        fixture=Path(__file__).resolve().parent/"n3_recurrence_fixtures"/"corrupt_rehashed_candidate.json"
        with self.assertRaises(RecurrenceEvidenceError):
            verify_candidate(json.loads(fixture.read_text(encoding="utf-8")))

    def test_block_winners_within_blocks(self):
        for row in self.small["block_rows"]:
            lo,hi=row["q_block"]
            self.assertLessEqual(lo,row["q"]);self.assertLessEqual(row["q"],hi)

if __name__=="__main__":unittest.main()
