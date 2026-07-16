#!/usr/bin/env python3
"""Fail-closed checks for N1-FIN-008 and N1-STR-024 finite data."""

from __future__ import annotations

import math
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def parse(path: Path) -> tuple[dict[str, str], list[dict[str, str]]]:
    scalars: dict[str, str] = {}
    rows: list[dict[str, str]] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        if raw.startswith("layer="):
            rows.append(dict(field.split("=", 1) for field in raw.split(",")))
        elif "=" in raw:
            key, value = raw.split("=", 1)
            scalars[key] = value
    return scalars, rows


def exact_checks(path: Path, expected_n: int) -> tuple[dict[str, str], list[dict[str, str]]]:
    scalars, rows = parse(path)
    assert int(scalars["n"]) == expected_n
    assert scalars["result_class"] == "finite certificate"
    assert scalars["reaches_full_endpoint"] == "true"
    assert int(scalars["layers_used"]) == len(rows)
    assert int(scalars["term_bound"]) == int(scalars["r"]) + len(rows)

    counts = [int(row["connected_count"]) for row in rows]
    product = math.prod(count + 1 for count in counts)
    assert product == int(scalars["connected_prefix_product"])

    y = int(scalars["Y"])
    w = int(scalars["W"])
    requirement = (y + w + 1) // (w + 1)
    assert requirement == int(scalars["finite_requirement_ceiling"])
    assert product // requirement == int(scalars["product_floor_ratio"])

    occupied = int(scalars["occupied_through"])
    assert occupied - y == int(scalars["margin"])
    assert int(rows[-1]["connected_count"]) == int(scalars["emitted_until_certificate"])
    return scalars, rows


def without_partition(path: Path) -> list[str]:
    return [
        line
        for line in path.read_text(encoding="utf-8").splitlines()
        if not line.startswith((
            "mitm_partition_mask=",
            "runtime_wall_seconds=",
            "maximum_resident_set_kib=",
        ))
    ]


def main() -> None:
    expected = {
        51: (3034386005338, 120.322026488584),
        52: (866765166748, 97.645052132052),
        53: (3743726317282, 124.609364763243),
    }

    files = {
        51: ROOT / "full_core_n51_mitm_overlap.txt",
        52: ROOT / "full_core_n52_mitm.txt",
        53: ROOT / "full_core_n53_mitm.txt",
    }

    for n, path in files.items():
        scalars, rows = exact_checks(path, n)
        product = int(scalars["connected_prefix_product"])
        requirement = int(scalars["finite_requirement_ceiling"])
        root_surplus = math.exp((math.log(product) - math.log(requirement)) / len(rows))
        expected_floor, expected_root = expected[n]
        assert int(scalars["product_floor_ratio"]) == expected_floor
        assert math.isclose(root_surplus, expected_root, rel_tol=2e-13)
        print(f"PASS exact n={n}")

    primary = ROOT / "full_core_n53_mitm.txt"
    alternate = ROOT / "full_core_n53_mitm_mask414.txt"
    exact_checks(alternate, 53)
    assert without_partition(primary) == without_partition(alternate)
    assert parse(primary)[0]["mitm_partition_mask"] == "350"
    assert parse(alternate)[0]["mitm_partition_mask"] == "414"
    print("PASS alternate partition n=53")

    roots = [expected[n][1] for n in (51, 52, 53)]
    assert roots[1] < roots[0] and roots[2] > roots[1]
    print("PASS finite non-monotonicity diagnostic")
    print("PASS all normalized meet-in-the-middle checks")


if __name__ == "__main__":
    main()
