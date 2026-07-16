from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from factorial_lab.lattice import LatticeCertificateError  # noqa: E402
from factorial_lab.n2_audit import (  # noqa: E402
    audit_n2_obs_107_range,
    generate_n2_obs_107_certificate,
    verify_n2_obs_107_certificate,
)


class N2RegressionTests(unittest.TestCase):
    def test_first_admissible_regression_parameter(self) -> None:
        audit = audit_n2_obs_107_range(3, 2000)
        self.assertEqual(audit["first_target_in_half_range_n"], 9)
        self.assertEqual(audit["first_side_condition_n"], 1892)
        self.assertEqual(audit["first_admissible_failure_n"], 1892)
        self.assertEqual(
            [row["n"] for row in audit["later_failures_after_first_admissible"]],
            [1893, 1894, 1895],
        )

    def test_frozen_obstruction_replays(self) -> None:
        result = verify_n2_obs_107_certificate(generate_n2_obs_107_certificate(1892))
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["audit_outcome"], "ACCEPTED")
        self.assertEqual(result["recomputed"]["window"], [1, 2**31])
        self.assertEqual(result["recomputed"]["common_divisor"], 2**32)

    def test_corrupted_cached_field_is_rejected(self) -> None:
        certificate = generate_n2_obs_107_certificate(1892)
        certificate["claimed"]["common_divisor"] //= 2
        with self.assertRaises(LatticeCertificateError):
            verify_n2_obs_107_certificate(certificate)

    def test_wrong_source_sha_is_rejected(self) -> None:
        certificate = generate_n2_obs_107_certificate(1892)
        certificate["source"]["nova1_frozen_commit"] = "0" * 40
        with self.assertRaises(LatticeCertificateError):
            verify_n2_obs_107_certificate(certificate)

    def test_nonadmissible_parameter_is_rejected(self) -> None:
        with self.assertRaises(LatticeCertificateError):
            verify_n2_obs_107_certificate(generate_n2_obs_107_certificate(1891))


if __name__ == "__main__":
    unittest.main()
