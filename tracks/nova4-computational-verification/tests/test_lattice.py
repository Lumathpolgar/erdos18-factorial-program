from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from factorial_lab.lattice import (  # noqa: E402
    LatticeCertificateError,
    load_lattice_certificate,
    verify_label_family_certificate,
)


FIXTURES = Path(__file__).parent / "lattice_fixtures"


class ExplicitLabelFamilyTests(unittest.TestCase):
    def test_common_gcd_failure(self) -> None:
        certificate = load_lattice_certificate(FIXTURES / "valid_common_gcd_failure.json")
        result = verify_label_family_certificate(certificate)
        self.assertEqual(result["main_gcd"], 32)
        self.assertEqual(result["gcd_gate_first_failure"], 16)
        self.assertEqual(result["smallest_failure"]["condition"], 4)

    def test_gcd_one_does_not_bypass_residue_or_exact_gate(self) -> None:
        certificate = load_lattice_certificate(FIXTURES / "valid_residue_failure_gcd_one.json")
        result = verify_label_family_certificate(certificate)
        self.assertEqual(result["main_gcd"], 1)
        self.assertIsNone(result["gcd_gate_first_failure"])
        self.assertEqual(result["exact_first_window_failure"], 1)

    def test_binary_palette_exact_coverage(self) -> None:
        certificate = load_lattice_certificate(FIXTURES / "valid_binary_coverage.json")
        result = verify_label_family_certificate(certificate)
        self.assertEqual(result["result_class"], "finite certificate")
        self.assertIsNone(result["smallest_failure"])
        self.assertEqual(result["exact_reachable_count"], 16)

    def test_every_corrupted_lattice_fixture_fails(self) -> None:
        for path in sorted(FIXTURES.glob("corrupt_*.json")):
            with self.subTest(path=path.name):
                with self.assertRaises(LatticeCertificateError):
                    verify_label_family_certificate(load_lattice_certificate(path))

    def test_cached_failure_target_is_not_trusted(self) -> None:
        certificate = load_lattice_certificate(FIXTURES / "valid_common_gcd_failure.json")
        certificate = copy.deepcopy(certificate)
        certificate["claimed"]["first_failure_target"] = 17
        with self.assertRaises(LatticeCertificateError):
            verify_label_family_certificate(certificate)


if __name__ == "__main__":
    unittest.main()
