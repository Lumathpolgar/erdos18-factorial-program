from __future__ import annotations

import copy
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from factorial_lab.dataset import generate_dataset, verify_dataset  # noqa: E402


class DatasetTests(unittest.TestCase):
    def test_generation_and_replay(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            dataset = generate_dataset(1, 8, certificate_dir=directory)
            result = verify_dataset(dataset)
            self.assertEqual(result["status"], "PASS")
            self.assertEqual(result["records"], 8)
            self.assertEqual(len(list(Path(directory).glob("*.json"))), 8)

    def test_checksum_corruption_rejected(self) -> None:
        dataset = generate_dataset(1, 5)
        bad = copy.deepcopy(dataset)
        bad["records"][0]["H"] += 1
        with self.assertRaisesRegex(ValueError, "checksum"):
            verify_dataset(bad)

    def test_recomputed_greedy_metadata_rejected(self) -> None:
        dataset = generate_dataset(1, 8)
        bad = copy.deepcopy(dataset)
        bad["records"][-1]["greedy_suboptimal_count"] += 1
        from factorial_lab.dataset import dataset_sha256
        bad["sha256"] = dataset_sha256(bad)
        with self.assertRaisesRegex(ValueError, "greedy failure count"):
            verify_dataset(bad)


if __name__ == "__main__":
    unittest.main()
