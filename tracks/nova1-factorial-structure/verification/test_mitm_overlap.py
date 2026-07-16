#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def parse(path: Path):
    scalar = {}
    layers = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("layer="):
            row = {}
            for field in line.split(","):
                key, value = field.split("=", 1)
                row[key] = value
            layers.append(row)
        elif "=" in line:
            key, value = line.split("=", 1)
            scalar[key] = value
    return scalar, layers


def test_n51_overlap():
    old_s, old_l = parse(ROOT / "full_core_n51.txt")
    new_s, new_l = parse(ROOT / "full_core_n51_mitm_overlap.txt")
    for key in [
        "n", "r", "M", "v2_factorial", "Y", "W",
        "total_odd_core_divisor_count", "layers_used", "carrier_endpoint",
        "occupied_through", "margin", "reaches_full_endpoint", "term_bound",
        "connected_prefix_product",
    ]:
        assert old_s[key] == new_s[key], (key, old_s[key], new_s[key])
    assert len(old_l) == len(new_l) == 6
    for old, new in zip(old_l, new_l):
        for key in [
            "layer", "scale", "core_bound", "gap_threshold",
            "connected_max_core", "connected_count", "carrier_endpoint",
            "first_blocking_gap",
        ]:
            assert old[key] == new[key], (key, old[key], new[key])
        for key in ["first_blocking_left", "first_blocking_right"]:
            assert old.get(key) == new.get(key), (key, old.get(key), new.get(key))


def test_n52_certificate():
    scalar, layers = parse(ROOT / "full_core_n52_mitm.txt")
    assert scalar["n"] == "52"
    assert scalar["reaches_full_endpoint"] == "true"
    assert scalar["term_bound"] == "22"
    assert scalar["mitm_rows"] == "12420"
    assert scalar["mitm_columns"] == "12480"
    assert scalar["maximum_heap"] == "12420"
    assert scalar["product_floor_ratio"] == "866765166748"
    assert len(layers) == 6
    assert [int(row["connected_count"]) for row in layers] == [
        47281, 847667, 7770345, 34911862, 85166200, 128277372
    ]
    assert int(scalar["occupied_through"]) - int(scalar["Y"]) == int(scalar["margin"])


if __name__ == "__main__":
    test_n51_overlap()
    print("PASS test_n51_overlap")
    test_n52_certificate()
    print("PASS test_n52_certificate")
    print("PASS all 2 meet-in-the-middle checks")
