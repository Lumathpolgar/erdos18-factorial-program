#!/usr/bin/env python3
"""Lightweight exact replay of the frozen N2-FIN-203 certificate."""

from __future__ import annotations

import json
import math
from pathlib import Path

from marker_three_full_menu_audit import (
    certified_log_parameters,
    divisor_count,
    factorial_valuations,
    odd_core_valuations,
)

CERTIFICATE = (
    Path(__file__).parent / "data" / "marker_three_streaming_n46.json"
)


def replay_certificate(payload: dict[str, object]) -> None:
    assert payload["schema"] == "nova2.marker-three-streaming-audit.v1"
    assert payload["result_id"] == "N2-FIN-203"
    assert payload["result_class"] == "finite certificate"

    n = int(payload["n"])
    assert n == 46
    r_value, layer_budget = certified_log_parameters(n)
    assert (r_value, layer_budget) == (16, 235)
    assert int(payload["r"]) == r_value
    assert int(payload["M"]) == layer_budget

    valuations = factorial_valuations(n)
    assert int(payload["v2_factorial"]) == valuations[2] == 42
    assert r_value - 1 <= valuations[2]

    x_endpoint = math.isqrt(math.factorial(n))
    quotient_endpoint = x_endpoint // 3
    window = ((1 << r_value) - 3) // 3
    assert int(payload["X"]) == x_endpoint
    assert int(payload["Y"]) == quotient_endpoint
    assert int(payload["W"]) == window == 21_844

    total_odd_cores = divisor_count(odd_core_valuations(n))
    assert int(payload["odd_core_divisor_count"]) == total_odd_cores == 27_941_760

    stream = payload["stream"]
    assert isinstance(stream, dict)
    assert int(stream["emitted_count_through_Y"]) == 24_567_748
    assert int(stream["final_value_through_Y"]) <= quotient_endpoint
    assert int(stream["record_gap_count"]) == 631
    assert int(stream["maximum_frontier"]) == 3_373_952

    rows = payload["rows"]
    assert isinstance(rows, list)
    assert len(rows) == int(payload["layers_used"]) == 6

    previous_endpoint = 0
    previous_menu_size: int | None = None
    for expected_t, row in enumerate(rows, start=1):
        assert isinstance(row, dict)
        assert int(row["t"]) == expected_t
        scale = 1 << (expected_t - 1)
        assert int(row["scale"]) == scale
        assert int(row["core_bound"]) == quotient_endpoint // scale
        assert int(row["gap_threshold"]) == (
            previous_endpoint + window + 1
        ) // scale

        menu_size = int(row["menu_size"])
        if previous_menu_size is not None:
            assert menu_size <= previous_menu_size
        previous_menu_size = menu_size

        connected_max = int(row["connected_max_core"])
        assert 0 <= connected_max <= int(row["core_bound"])
        expected_endpoint = previous_endpoint + scale * connected_max
        assert int(row["carrier_endpoint"]) == expected_endpoint

        blocking = row["first_blocking_gap"]
        if blocking is not None:
            assert isinstance(blocking, dict)
            left = int(blocking["left_core"])
            right = int(blocking["right_core"])
            gap = int(blocking["gap"])
            assert left == connected_max
            assert right - left == gap
            assert gap > int(row["gap_threshold"])
            assert right <= int(row["core_bound"])
        previous_endpoint = expected_endpoint

    occupied_through = previous_endpoint + window
    assert int(payload["carrier_endpoint"]) == previous_endpoint
    assert int(payload["occupied_through"]) == occupied_through
    assert int(payload["margin"]) == occupied_through - quotient_endpoint
    assert int(payload["deficit"]) == 0
    assert payload["reaches_full_endpoint"] is True
    assert occupied_through >= quotient_endpoint
    assert int(payload["term_bound"]) == r_value + len(rows) == 22


def main() -> None:
    payload = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
    replay_certificate(payload)
    print("PASS N2-FIN-203 streaming certificate replay at n=46")


if __name__ == "__main__":
    main()
