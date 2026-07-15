from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from factorial_lab.certificates import (  # noqa: E402
    CertificateError,
    load_certificate,
    verify_representation_certificate,
)


class FixtureTests(unittest.TestCase):
    def test_valid_fixture_passes(self) -> None:
        path = Path(__file__).parent / "fixtures" / "valid_n6_target10.json"
        self.assertEqual(
            verify_representation_certificate(load_certificate(path))["status"], "PASS"
        )

    def test_every_corrupted_fixture_fails(self) -> None:
        for path in sorted((Path(__file__).parent / "fixtures").glob("corrupt_*.json")):
            with self.subTest(path=path.name):
                with self.assertRaises(CertificateError):
                    verify_representation_certificate(load_certificate(path))


if __name__ == "__main__":
    unittest.main()
