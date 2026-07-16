#!/usr/bin/env python3
from __future__ import annotations

from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PRIMARY = ROOT / "full_core_n55_mitm_mask9.txt"
ALTERNATE = ROOT / "full_core_n55_mitm_mask808.txt"

EXPECTED_COUNTS = [90622, 1867655, 18700076, 92180941, 236519444, 369103338]
EXPECTED_MARGIN = 2071800017139336764535620107907
EXPECTED_PRODUCT = 25470336596566520205304888296679181030522160
EXPECTED_REQUIREMENT = 27185483168218657671727712427365
EXPECTED_RATIO = 936909468886

HISTORICAL_GAPS = {
    (51, 1): (22172, 21845),
    (51, 2): (34637850, 31988524),
    (51, 3): (459850891500, 428597048949),
    (51, 4): (20891689328819250, 18870510190034037),
    (51, 5): (2303807699477340078750, 2226628053243742477956),
    (52, 1): (22172, 21845),
    (52, 2): (34637850, 31988524),
    (52, 3): (470455762392, 428597048949),
    (52, 4): (26500727429154000, 25467307873635162),
    (52, 5): (3397375259291095762680, 3358089676487133175393),
    (53, 1): (23042, 21845),
    (53, 2): (45654476, 43052743),
    (53, 3): (737978943000, 736340019964),
    (53, 4): (84872309090318750, 82883567360966919),
    (53, 5): (26341214674665403012500, 24671918500667380441272),
    (54, 1): (23042, 21845),
    (54, 2): (45654476, 43052743),
    (54, 3): (737978943000, 736340019964),
    (54, 4): (91684203427867050, 82883567360966919),
    (54, 5): (27626991957275465455470, 27574492272300756906897),
}


def parse(path: Path) -> tuple[dict[str, str], list[dict[str, str]]]:
    scalars: dict[str, str] = {}
    layers: list[dict[str, str]] = []
    for raw in path.read_text().splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("layer="):
            row = dict(item.split("=", 1) for item in line.split(","))
            layers.append(row)
        elif "=" in line:
            key, value = line.split("=", 1)
            scalars[key] = value
    return scalars, layers


def mathematical_view(scalars: dict[str, str], layers: list[dict[str, str]]) -> tuple:
    ignored = {
        "mitm_partition_mask",
        "mitm_rows",
        "mitm_columns",
        "maximum_heap",
        "runtime_wall_seconds",
        "maximum_resident_set_kib",
    }
    return tuple(sorted((k, v) for k, v in scalars.items() if k not in ignored)), tuple(
        tuple(sorted(row.items())) for row in layers
    )


def check_effective_identity(scalars: dict[str, str], layers: list[dict[str, str]]) -> None:
    w = int(scalars["W"])
    f_prev = w + 1
    count_product = 1
    utilization_product = Fraction(1, 1)
    growth_product = Fraction(1, 1)

    for row in layers:
        scale = int(row["scale"])
        core = int(row["connected_max_core"])
        count = int(row["connected_count"])
        a = Fraction(scale * core, f_prev)
        b = (1 + a) / (1 + count)
        growth_product *= 1 + a
        utilization_product *= b
        count_product *= 1 + count
        f_prev = int(row["carrier_endpoint"]) + w + 1

    final_f = int(scalars["carrier_endpoint"]) + w + 1
    assert growth_product == Fraction(final_f, w + 1)
    assert Fraction(count_product, 1) * utilization_product == growth_product
    assert count_product == int(scalars["connected_prefix_product"])
    assert final_f >= int(scalars["Y"]) + 1


def main() -> None:
    primary, p_layers = parse(PRIMARY)
    alternate, a_layers = parse(ALTERNATE)

    assert mathematical_view(primary, p_layers) == mathematical_view(alternate, a_layers)
    assert primary["result_class"] == "finite certificate"
    assert int(primary["n"]) == 55
    assert int(primary["r"]) == 17
    assert int(primary["M"]) == 257
    assert int(primary["v2_factorial"]) == 50
    assert int(primary["total_odd_core_divisor_count"]) == 452874240
    assert int(primary["emitted_until_certificate"]) == 369103338
    assert [int(row["connected_count"]) for row in p_layers] == EXPECTED_COUNTS
    assert int(primary["layers_used"]) == 6
    assert int(primary["term_bound"]) == 23
    assert primary["reaches_full_endpoint"] == "true"
    assert int(primary["margin"]) == EXPECTED_MARGIN
    assert int(primary["connected_prefix_product"]) == EXPECTED_PRODUCT
    assert int(primary["finite_requirement_ceiling"]) == EXPECTED_REQUIREMENT
    assert int(primary["product_floor_ratio"]) == EXPECTED_RATIO

    check_effective_identity(primary, p_layers)
    check_effective_identity(alternate, a_layers)

    gaps = dict(HISTORICAL_GAPS)
    for row in p_layers:
        if row["first_blocking_gap"] != "NONE":
            gaps[(55, int(row["layer"]))] = (
                int(row["first_blocking_gap"]),
                int(row["gap_threshold"]),
            )

    winner = max((Fraction(gap, threshold), n, layer, gap, threshold) for (n, layer), (gap, threshold) in gaps.items())
    assert winner[1:] == (51, 4, 20891689328819250, 18870510190034037)
    assert winner[0] < Fraction(277, 250)

    print("PASS exact n=55")
    print("PASS alternate partition n=55")
    print("PASS effective carrier factorization")
    print("PASS term-bound transition from 22 to 23")
    print("PASS finite first-blocking-gap ratio below 1.108 through n=55")
    print("PASS all n=55 effective carrier checks")


if __name__ == "__main__":
    main()
