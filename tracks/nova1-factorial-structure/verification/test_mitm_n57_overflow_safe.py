#!/usr/bin/env python3
"""Regression checks for N1-STR-027, N1-FIN-012, and N1-DIS-007/008."""
from __future__ import annotations

from decimal import Decimal, getcontext
from pathlib import Path

getcontext().prec = 100
ROOT = Path(__file__).resolve().parent


def parse(path: Path):
    top: dict[str, str] = {}
    layers: list[dict[str, str]] = []
    for line in path.read_text().splitlines():
        if line.startswith("layer="):
            layers.append(dict(part.split("=", 1) for part in line.split(",")))
        elif "=" in line:
            key, value = line.split("=", 1)
            top[key] = value
    return top, layers


def mathematical_projection(top, layers):
    ignored = {
        "schema",
        "mitm_partition_mask",
        "mitm_rows",
        "mitm_columns",
        "maximum_heap",
    }
    return ({k: v for k, v in top.items() if k not in ignored}, layers)


def check_expected(path: Path, n: int, counts: list[int], term_bound: int, margin: int):
    top, layers = parse(path)
    assert int(top["n"]) == n
    assert [int(row["connected_count"]) for row in layers] == counts
    assert int(top["term_bound"]) == term_bound
    assert int(top["margin"]) == margin
    assert top["reaches_full_endpoint"] == "true"
    return top, layers


def main() -> None:
    primary_top, primary_layers = check_expected(
        ROOT / "full_core_n57_safe_mask6.txt",
        57,
        [93284, 1968508, 21512180, 115705564, 322620612, 543303166, 565913305],
        24,
        5864341952037941548771786716193021624,
    )
    alternate_top, alternate_layers = check_expected(
        ROOT / "full_core_n57_safe_mask424.txt",
        57,
        [93284, 1968508, 21512180, 115705564, 322620612, 543303166, 565913305],
        24,
        5864341952037941548771786716193021624,
    )
    assert mathematical_projection(primary_top, primary_layers) == mathematical_projection(alternate_top, alternate_layers)
    print("PASS safe dual-partition n=57")

    y = Decimal(primary_top["Y"])
    w = Decimal(primary_top["W"])
    f6 = Decimal(primary_layers[5]["carrier_endpoint"]) + w + 1
    f7 = Decimal(primary_top["carrier_endpoint"]) + w + 1
    assert f6 < y + 1 <= f7
    print("PASS seven-layer necessity and sufficiency n=57")

    ratio = Decimal(primary_layers[2]["first_blocking_gap"]) / Decimal(primary_layers[2]["gap_threshold"])
    assert ratio > Decimal("1.108")
    print("PASS 1.108 candidate counterexample")

    source = (ROOT / "marker_three_mitm_checkpoint_u128.cpp").read_text()
    assert "cur>lim/p" in source
    assert "A[root]<=Y/B[nc]" in source
    assert "checkpoint=loaded" in source
    print("PASS overflow guards and checkpoint source audit")

    print("PASS all n=57 overflow-safe carrier checks")


if __name__ == "__main__":
    main()
