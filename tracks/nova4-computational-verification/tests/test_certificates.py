from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from factorial_lab.certificates import (  # noqa: E402
    CertificateError,
    certificate_sha256,
    dump_certificate,
    make_representation_certificate,
    verify_representation_certificate,
)


class CertificateTests(unittest.TestCase):
    def setUp(self) -> None:
        self.valid = make_representation_certificate(
            n=6,
            target=10,
            divisors=[4, 6],
            max_terms=2,
            labels=["left", "right"],
            target_range=(0, 11),
        )

    def test_valid_certificate(self) -> None:
        result = verify_representation_certificate(self.valid)
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["values"], [4, 6])

    def test_duplicate_numerical_values_rejected_even_with_labels(self) -> None:
        bad = copy.deepcopy(self.valid)
        bad["target"] = 8
        bad["terms"] = [
            {"label": "packet-A", "value": 4},
            {"label": "packet-B", "value": 4},
        ]
        with self.assertRaisesRegex(CertificateError, "repeated numerical"):
            verify_representation_certificate(bad)

    def test_illegal_divisor_rejected(self) -> None:
        bad = copy.deepcopy(self.valid)
        bad["target"] = 15
        bad["target_range"]["upper_exclusive"] = 16
        bad["terms"][1]["value"] = 11
        with self.assertRaisesRegex(CertificateError, "do not divide"):
            verify_representation_certificate(bad)

    def test_wrong_sum_rejected(self) -> None:
        bad = copy.deepcopy(self.valid)
        bad["target"] = 9
        with self.assertRaisesRegex(CertificateError, "sum mismatch"):
            verify_representation_certificate(bad)

    def test_term_bound_rejected(self) -> None:
        bad = copy.deepcopy(self.valid)
        bad["max_terms"] = 1
        with self.assertRaisesRegex(CertificateError, "exceeds"):
            verify_representation_certificate(bad)

    def test_target_range_rejected(self) -> None:
        bad = copy.deepcopy(self.valid)
        bad["target_range"]["upper_exclusive"] = 10
        with self.assertRaisesRegex(CertificateError, "outside"):
            verify_representation_certificate(bad)

    def test_cached_fields_are_recomputed(self) -> None:
        bad = copy.deepcopy(self.valid)
        bad["claimed_sum"] = 999
        with self.assertRaisesRegex(CertificateError, "claimed_sum"):
            verify_representation_certificate(bad)

    def test_serialization_is_deterministic(self) -> None:
        shuffled = copy.deepcopy(self.valid)
        shuffled["terms"].reverse()
        self.assertEqual(certificate_sha256(self.valid), certificate_sha256(shuffled))
        with tempfile.TemporaryDirectory() as directory:
            first = Path(directory) / "first.json"
            second = Path(directory) / "second.json"
            self.assertEqual(
                dump_certificate(self.valid, first), dump_certificate(shuffled, second)
            )
            self.assertEqual(first.read_bytes(), second.read_bytes())
            json.loads(first.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
