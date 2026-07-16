#!/usr/bin/env python3
"""Lightweight regressions for marker_three_full_menu_audit.py."""

from __future__ import annotations

import importlib.util
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("marker_three_full_menu_audit.py")
SPEC = importlib.util.spec_from_file_location("marker_three_full_menu_audit", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("could not load marker_three_full_menu_audit")
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def test_certified_parameters() -> None:
    assert MODULE.certified_log_parameters(12) == (10, 99)
    assert MODULE.certified_log_parameters(45) == (16, 232)


def test_first_completed_case() -> None:
    audit = MODULE.audit_n(12, max_divisors=1000)
    assert audit["odd_core_divisor_count"] == 60
    assert audit["layers_used"] == 2
    assert audit["carrier_endpoint"] == 8505
    assert audit["occupied_through"] == 8845
    assert audit["Y"] == 7295
    assert audit["margin"] == 1550
    assert audit["reaches_full_endpoint"] is True
    assert audit["term_bound"] == 12


def test_resource_cap_fails_closed() -> None:
    try:
        MODULE.audit_n(46, max_divisors=20_000_000)
    except MODULE.AuditError as exc:
        text = str(exc)
        assert "27941760" in text
        assert "above cap 20000000" in text
    else:
        raise AssertionError("n=46 must fail closed at the frozen resource cap")


def main() -> None:
    tests = [
        test_certified_parameters,
        test_first_completed_case,
        test_resource_cap_fails_closed,
    ]
    for test in tests:
        test()
        print(f"PASS {test.__name__}")
    print(f"PASS all {len(tests)} marker-three full-menu regressions")


if __name__ == "__main__":
    main()
