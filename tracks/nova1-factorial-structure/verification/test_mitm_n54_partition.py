#!/usr/bin/env python3
"""Exact replay checks for N1-FIN-009 and normalized finite evidence."""

from __future__ import annotations

from decimal import Decimal, getcontext
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def parse(path: Path) -> dict[str, str]:
    result: dict[str, str] = {}
    layers: list[str] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw:
            continue
        if raw.startswith("layer="):
            layers.append(raw)
            continue
        key, value = raw.split("=", 1)
        result[key] = value
    result["layers"] = "\n".join(layers)
    return result


def assert_equal_partition_outputs(a: dict[str, str], b: dict[str, str]) -> None:
    ignored = {
        "mitm_partition_mask",
        "mitm_rows",
        "mitm_columns",
        "maximum_heap",
        "runtime_wall_seconds",
        "maximum_resident_set_kib",
    }
    keys = (set(a) | set(b)) - ignored
    for key in sorted(keys):
        assert a.get(key) == b.get(key), (key, a.get(key), b.get(key))


def gamma(product: str, requirement: str, layers: int) -> Decimal:
    getcontext().prec = 80
    return (Decimal(product) / Decimal(requirement)) ** (Decimal(1) / Decimal(layers))


def main() -> None:
    primary = parse(ROOT / "full_core_n54_mitm_mask255.txt")
    alternate = parse(ROOT / "full_core_n54_mitm_mask223.txt")
    assert_equal_partition_outputs(primary, alternate)

    expected = {
        "n": "54",
        "r": "16",
        "M": "255",
        "v2_factorial": "50",
        "Y": "160153987475679647486755841698814824",
        "W": "21844",
        "total_odd_core_divisor_count": "350438400",
        "emitted_until_certificate": "287853491",
        "layers_used": "6",
        "margin": "321802717811173461556306445531",
        "reaches_full_endpoint": "true",
        "term_bound": "22",
        "connected_prefix_product": "4525233744675622115970119580522296824224000",
        "finite_requirement_ceiling": "7331379605203920690627413215785",
        "product_floor_ratio": "617241772812",
        "exit_status": "0",
    }
    for key, value in expected.items():
        assert primary[key] == value, (key, primary[key], value)

    counts = [
        "63547",
        "1308259",
        "14197074",
        "71967365",
        "185071301",
        "287853491",
    ]
    for count in counts:
        assert f"connected_count={count}" in primary["layers"]

    table = {
        51: (
            "57666029159716720889778527039222918886144",
            "19004183732151654833196949076",
        ),
        52: (
            "118782467311926842592580351058316666013104",
            "137041117789222790706764045267",
        ),
        53: (
            "3735019895586315708628949327266947558122880",
            "997674396855377193679964787024",
        ),
        54: (
            primary["connected_prefix_product"],
            primary["finite_requirement_ceiling"],
        ),
    }
    values = {n: gamma(product, requirement, 6) for n, (product, requirement) in table.items()}
    assert values[52] < values[51]
    assert values[53] > values[52]
    assert values[54] < values[53]
    assert values[54] > 1

    blocking = {
        51: [(21845, 22172), (31988524, 34637850), (428597048949, 459850891500), (18870510190034037, 20891689328819250), (2226628053243742477956, 2303807699477340078750)],
        52: [(21845, 22172), (31988524, 34637850), (428597048949, 470455762392), (25467307873635162, 26500727429154000), (3358089676487133175393, 3397375259291095762680)],
        53: [(21845, 23042), (43052743, 45654476), (736340019964, 737978943000), (82883567360966919, 84872309090318750), (24671918500667380441272, 26341214674665403012500)],
        54: [(21845, 23042), (43052743, 45654476), (736340019964, 737978943000), (82883567360966919, 91684203427867050), (27574492272300756906897, 27626991957275465455470)],
    }
    maximum = max(
        (Decimal(gap) / Decimal(threshold), n, layer)
        for n, rows in blocking.items()
        for layer, (threshold, gap) in enumerate(rows, start=1)
    )
    assert maximum[1:] == (51, 4)
    assert maximum[0] < Decimal("1.108")

    print("PASS exact n=54")
    print("PASS alternate partition n=54")
    print("PASS exact connected-prefix counts")
    print("PASS normalized non-monotonicity through n=54")
    print("PASS finite first-blocking-gap ratio below 1.108")
    print("PASS all n=54 meet-in-the-middle checks")


if __name__ == "__main__":
    main()
