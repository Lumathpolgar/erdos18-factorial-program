import copy
import tempfile
import unittest

from factorial_lab.n3_adversarial import *


class AdversarialTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.audit = build_audit()
        cls.claim = build_claim(cls.audit)

    def test_final_decision(self):
        self.assertEqual(self.audit["decision"]["N3_ANA_011"], "ACCEPTED")

    def test_proof_certificate(self):
        proof = self.audit["proof_reconstruction"]
        self.assertEqual(proof["address_uniformity"]["base_margin_lower"], 115632)
        self.assertTrue(proof["endpoint_witness"]["ceil_endpoint_is_prime"])

    def test_contract(self):
        verify_contract(canonical_contract())

    def test_audit_and_claim(self):
        verify_audit(self.audit)
        verify_claim(self.claim, self.audit)

    def test_all_six_records(self):
        self.assertEqual(len(self.audit["adversarial_tests"]), 6)
        self.assertTrue(all(record["rejected"] for record in self.audit["adversarial_tests"]))

    def test_lower_threshold_rejected(self):
        with self.assertRaises(VerificationError):
            verify_contract(corrupted_contract(MUTATIONS[0]))

    def test_larger_address_rejected(self):
        with self.assertRaises(VerificationError):
            verify_contract(corrupted_contract(MUTATIONS[1]))

    def test_unit_correction_rejected(self):
        with self.assertRaises(VerificationError):
            verify_contract(corrupted_contract(MUTATIONS[2]))

    def test_injectivity_rejected(self):
        with self.assertRaises(VerificationError):
            verify_contract(corrupted_contract(MUTATIONS[3]))

    def test_ceil_endpoint_rejected(self):
        with self.assertRaises(VerificationError):
            verify_contract(corrupted_contract(MUTATIONS[4]))

    def test_finite_asymptotic_rejected(self):
        with self.assertRaises(VerificationError):
            verify_contract(corrupted_contract(MUTATIONS[5]))

    def test_rehashed_claim_corruption(self):
        value = copy.deepcopy(self.claim)
        value["claim"]["decision"] = "REJECTED"
        value["sha256"] = semantic_sha256(value)
        with self.assertRaises(VerificationError):
            verify_claim(value, self.audit)

    def test_fixture_directory(self):
        with tempfile.TemporaryDirectory() as directory:
            write_fixtures(directory)
            verify_fixture_directory(directory)

    def test_scope(self):
        self.assertIn("additive occupancy", self.audit["scope"]["not_proved"])
        self.assertTrue(self.claim["claim"]["finite_sweep_is_not_asymptotic_proof"])


if __name__ == "__main__":
    unittest.main()
