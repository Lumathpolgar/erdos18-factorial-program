import copy
import unittest

from factorial_lab.n3_variance_limit import (
    OBJECT_ID,
    VerificationError,
    build_audit,
    build_claim,
    corrupted_claims,
    limiting_variance_partial,
    normalized_variance,
    primes_up_to,
    rigorous_integer_tail_upper,
    semantic_sha256,
    valuation_factorial,
    verify_audit,
    verify_claim,
)


class VarianceLimitAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.audit = build_audit()
        cls.claim = build_claim(cls.audit)

    def test_decision(self):
        self.assertEqual(self.audit["decision"]["N3_ANA_006"], "ACCEPTED")
        self.assertEqual(self.claim["claim"]["object"], OBJECT_ID)

    def test_valuation(self):
        self.assertEqual(valuation_factorial(10, 2), 8)
        self.assertEqual(valuation_factorial(10, 3), 4)

    def test_variance_evidence(self):
        primes = primes_up_to(10_000)
        ratio = normalized_variance(10_000, primes)
        self.assertGreater(ratio, 0.115)
        self.assertLess(ratio, 0.116)

    def test_series_partial(self):
        primes = primes_up_to(100_000)
        partial = limiting_variance_partial(100_000, primes)
        self.assertGreater(partial, 0.115)
        self.assertLess(partial, 0.116)

    def test_tail_bound(self):
        bound = rigorous_integer_tail_upper(1_000_000)
        self.assertGreater(bound, 0)
        self.assertLess(bound, 0.0001)

    def test_zero_frequency(self):
        proof = self.audit["proof_reconstruction"]["non_gaussian"]
        self.assertEqual(proof["zero_frequency"], "2*pi/log(2)")
        self.assertEqual(proof["p_equals_2_argument"], "pi")
        self.assertEqual(proof["p_equals_2_factor"], "0")

    def test_finite_not_proof(self):
        self.assertFalse(self.audit["decision"]["finite_table_is_asymptotic_proof"])
        self.assertTrue(self.claim["claim"]["finite_diagnostics_only"])

    def test_verify(self):
        verify_audit(self.audit)
        verify_claim(self.claim, self.audit)

    def test_all_corruptions_rejected(self):
        for name, corrupted in corrupted_claims(self.claim).items():
            with self.subTest(name=name):
                with self.assertRaises(VerificationError):
                    verify_claim(corrupted, self.audit)

    def test_rehashed_source_corruption_rejected(self):
        corrupted = copy.deepcopy(self.claim)
        corrupted["source"]["proof_file_blob_sha"] = "0" * 40
        corrupted["sha256"] = semantic_sha256(corrupted)
        with self.assertRaises(VerificationError):
            verify_claim(corrupted, self.audit)

    def test_wrong_evidence_hash_rejected(self):
        corrupted = copy.deepcopy(self.claim)
        corrupted["evidence_sha256"] = "0" * 64
        corrupted["sha256"] = semantic_sha256(corrupted)
        with self.assertRaises(VerificationError):
            verify_claim(corrupted, self.audit)

    def test_scope(self):
        excluded = self.claim["claim"]["scope_excludes"]
        self.assertIn("additive occupancy", excluded)
        self.assertIn("Erdos Problem 18", excluded)


if __name__ == "__main__":
    unittest.main()
