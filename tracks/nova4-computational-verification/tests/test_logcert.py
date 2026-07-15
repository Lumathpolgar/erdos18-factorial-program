from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from factorial_lab.logcert import certified_log_parameters  # noqa: E402


class CertifiedLogTests(unittest.TestCase):
    def test_certified_parameters(self) -> None:
        self.assertEqual(certified_log_parameters(3), (5, 20))
        self.assertEqual(certified_log_parameters(1892), (31, 911))


if __name__ == "__main__":
    unittest.main()
