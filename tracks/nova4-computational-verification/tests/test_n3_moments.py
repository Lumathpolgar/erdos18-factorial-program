from __future__ import annotations
import json, sys, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from factorial_lab.n3_moments import (
    AnalyticAuditError,
    audit_range, certified_floor_delta_over_log_prime,
    certified_floor_scaled_exp, exact_moment_record, first_tight_claim,
    local_ceiling_record, semantic_sha, verify_audit, verify_local_ceiling_claim,
)
from fractions import Fraction

class N3MomentLocalTests(unittest.TestCase):
    def test_exact_small_moment_records(self):
        self.assertEqual(exact_moment_record(2)["tau"],2)
        self.assertEqual(exact_moment_record(12)["tau"],792)
    def test_exact_exp_floors(self):
        self.assertEqual(certified_floor_scaled_exp(1,Fraction(0)),1)
        self.assertEqual(certified_floor_scaled_exp(1,Fraction(1)),2)
        self.assertEqual(certified_floor_scaled_exp(10,Fraction(1,2)),16)
    def test_floor_delta_over_log(self):
        self.assertEqual(certified_floor_delta_over_log_prime(Fraction(2),2),2)
        self.assertEqual(certified_floor_delta_over_log_prime(Fraction(1,2),3),0)
    def test_local_record_n2_has_tight_case(self):
        record=local_ceiling_record(2)
        self.assertGreater(record["windows_checked"],0)
        self.assertIsNotNone(record["first_tight_case"])
    def test_full_range_replay(self):
        audit=audit_range(2,12)
        self.assertEqual(verify_audit(audit)["status"],"PASS")
        self.assertEqual(audit["decisions"]["N3-ANA-004"],"ACCEPTED_FOR_ENUMERATED_RANGE")
    def test_full_range_totals(self):
        audit=audit_range(2,12)
        self.assertEqual(audit["totals"]["divisors_enumerated"],1978)
        self.assertEqual(audit["totals"]["local_windows_checked"],45840)
    def test_on_disk_corrupted_bound_rejected(self):
        path=Path(__file__).resolve().parent/"n3_fixtures"/"corrupt_rehashed_downward_bound.json"
        claim=json.loads(path.read_text())
        with self.assertRaises(AnalyticAuditError): verify_local_ceiling_claim(claim)
    def test_valid_tight_claim(self):
        claim=first_tight_claim(audit_range(2,3))
        self.assertEqual(verify_local_ceiling_claim(claim)["status"],"PASS")
    def test_rehashed_downward_bound_rejected(self):
        claim=first_tight_claim(audit_range(2,2))
        claim["claimed_upper_bound"]-=1
        claim["sha256"]=semantic_sha(claim)
        with self.assertRaises(AnalyticAuditError): verify_local_ceiling_claim(claim)
    def test_rehashed_cached_actual_rejected(self):
        claim=first_tight_claim(audit_range(2,2))
        claim["claim"]["actual"]+=1
        claim["sha256"]=semantic_sha(claim)
        with self.assertRaises(AnalyticAuditError): verify_local_ceiling_claim(claim)

if __name__=="__main__": unittest.main()
