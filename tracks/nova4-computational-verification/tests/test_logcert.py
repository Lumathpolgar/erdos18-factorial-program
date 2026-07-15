from __future__ import annotations

import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from factorial_lab.logcert import certified_log_parameters, certified_log_parameter_tables  # noqa: E402


class CertifiedLogTests(unittest.TestCase):
    def test_certified_parameters(self) -> None:
        self.assertEqual(certified_log_parameters(3), (5, 20))
        self.assertEqual(certified_log_parameters(1892), (31, 911))

    def test_parameter_tables_match_individual_certificates(self):
        r_values, m_values = certified_log_parameter_tables(10_000)
        for n in [1, 2, 3, 10, 11, 1892, 1893, 1896, 9999, 10000]:
            self.assertEqual((r_values[n], m_values[n]), certified_log_parameters(n))


if __name__ == "__main__":
    unittest.main()
