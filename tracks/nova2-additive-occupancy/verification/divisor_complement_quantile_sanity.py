#!/usr/bin/env python3
"""Exact regression for N2-ADD-125, N2-ADD-126, and N2-CMP-207."""

from fractions import Fraction
from math import factorial, isqrt, log10

DATA = {
    51: (124001280, 415146393628852899831187352563934, 21844, 47, [(21845,46990),(31988524,824638),(428597048949,6936398),(18870510190034037,30013231),(2226628053243742477956,70529067),(323412864885270853942840540,101350643)]),
    52: (155001600, 2993663218105571862989260568857358, 21844, 49, [(21845,47281),(31988524,847667),(428597048949,7770345),(25467307873635162,34911862),(3358089676487133175393,85166200),(610353310825031262102720509,128277372)]),
    53: (310003200, 21794197199305714795938830772522725, 21844, 49, [(21845,63547),(43052743,1308251),(736340019964,14186800),(82883567360966919,70586242),(24671918500667380441272,175389561),(8048881421864390371643440948,255794579)]),
    54: (350438400, 160153987475679647486755841698814824, 21844, 50, [(21845,63547),(43052743,1308259),(736340019964,14197074),(82883567360966919,71967365),(27574492272300756906897,185071301),(11575365984580699037980367511,287853491)]),
    55: (452874240, 1187733759619473153677783755951573821, 43689, 50, [(43690,90622),(111931989,1867655),(2911463348807,18700076),(350556503363400841,92180941),(135975582125916386901983,236519444),(70738331415946725049094036929,369103338)]),
}

EXPECTED = {
    51: (-23.023044339, 0.000145487587879522),
    52: (-23.441440572, 0.000123906257046752),
    53: (-24.251906596, 0.0000907853071519960),
    54: (-24.295007937, 0.0000892960011035230),
    55: (-24.783264694, 0.0000740382055592177),
}


def fraction_log10(value: Fraction) -> float:
    return log10(value.numerator) - log10(value.denominator)


def main() -> None:
    for n, (tau, y, w, v2, rows) in DATA.items():
        core = factorial(n) // (3 * (2**v2))
        root = isqrt(core)
        ceil_root = root if root * root == core else root + 1
        product = Fraction(1, 1)
        majority_layers = []

        for layer, (threshold, count) in enumerate(rows, 1):
            span = 2 * count - 1
            if count >= tau // 2 + 1:
                majority_layers.append(layer)
                span = max(span, ceil_root)
            product *= Fraction(threshold + 1 + span, threshold + 1)

        assert majority_layers == [5, 6]
        requirement = Fraction(y + 1, w + 1)
        ratio = product / requirement
        observed_log = fraction_log10(ratio)
        observed_root = 10 ** (observed_log / 6)
        expected_log, expected_root = EXPECTED[n]
        assert abs(observed_log - expected_log) < 5e-10
        assert abs(observed_root - expected_root) < 5e-18

    print("PASS N2-ADD-125 complement identity consequences")
    print("PASS N2-ADD-126 median-hybrid criterion")
    print("PASS N2-CMP-207 exact n=51..55 diagnostics")


if __name__ == "__main__":
    main()
