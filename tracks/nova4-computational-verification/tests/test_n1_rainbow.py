from __future__ import annotations
import copy, json, sys, unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from factorial_lab.n1_rainbow import RainbowCertificationError, _sha, audit_case, audit_range, build_family, certified_ceil_log, first_failure_certificate, verify_audit, verify_failure, verify_witness

FIXTURES = Path(__file__).resolve().parent / "rainbow_fixtures"

class ReducedRainbowTests(unittest.TestCase):
    def test_log_ceiling_transitions(self):
        self.assertEqual([certified_ceil_log(n) for n in (20,21,54,55)],[3,4,4,5])
    def test_n20_family(self):
        f=build_family(20)
        self.assertEqual(f["high_primes"],[11,13,17,19]);self.assertEqual(f["high_core_menu"],[11,13,17,19,143,187,209])
        self.assertEqual((f["r_star"],f["m_star"]),(3,5));self.assertEqual([x["address"] for x in f["layers"]],[4,5,6,7,8])
    def test_n20_exact_support(self):
        c=audit_case(20)
        self.assertEqual(c["distinct_reachable_sums_up_to_target_cap"],4418);self.assertEqual(c["gcd_nonzero_layer_terms"],16)
        self.assertEqual(c["first_target_exceeding_radius"]["target"],8);self.assertEqual(c["first_target_exceeding_radius"]["window"],[1,8])
        self.assertEqual(c["maximum_downward_gap"],9896336)
    def test_independent_lattice_agrees(self):
        c=audit_case(20);l=c["independent_lattice_obstruction"]
        self.assertTrue(l["all_terms_divisible_by_modulus"]);self.assertFalse(l["window_contains_lattice_point"]);self.assertEqual(l["target"],8)
    def test_record_witnesses(self):
        f=build_family(20)
        for e in audit_case(20)["record_gap_events"]:verify_witness(e["predecessor_reachable"],e["predecessor_witness"],f)
    def test_duplicate_layer_witness_rejected(self):
        f=build_family(20)
        with self.assertRaises(RainbowCertificationError):verify_witness(384,[{"layer":1,"address":4,"term":176},{"layer":1,"address":4,"term":208}],f)
    def test_small_range_replay(self):
        a=audit_range(20,22);self.assertEqual(verify_audit(a)["status"],"PASS");self.assertEqual(a["failure_count"],3)
    def test_rehashed_false_audit_rejected(self):
        a=audit_range(20,20);b=copy.deepcopy(a);b["cases"][0]["first_target_exceeding_radius"]["target"]=9;b["sha256"]=_sha(b)
        with self.assertRaises(RainbowCertificationError):verify_audit(b)
    def test_failure_certificate(self):
        z=first_failure_certificate(audit_range(20,20));self.assertEqual(verify_failure(z)["target"],8)
    def test_rehashed_false_failure_rejected(self):
        z=first_failure_certificate(audit_range(20,20));z["claimed"]["target"]=9;z["sha256"]=_sha(z)
        with self.assertRaises(RainbowCertificationError):verify_failure(z)
    def test_on_disk_rehashed_false_failure_rejected(self):
        z=json.loads((FIXTURES/"corrupt_rehashed_first_failure.json").read_text(encoding="utf-8"))
        self.assertEqual(z["sha256"],_sha(z))
        with self.assertRaises(RainbowCertificationError):verify_failure(z)

if __name__=="__main__":unittest.main()
