#!/usr/bin/env python3
"""Fixed-parameter replay for N2-ADD-127, N2-ADD-128, and N2-CMP-208."""

from decimal import Decimal, getcontext
from math import factorial, isqrt

getcontext().prec = 80

KS = {
    51: [46990, 824638, 6936398, 30013231, 70529067, 101350643],
    52: [47281, 847667, 7770345, 34911862, 85166200, 128277372],
    53: [63547, 1308251, 14186800, 70586242, 175389561, 255794579],
    54: [63547, 1308259, 14197074, 71967365, 185071301, 287853491],
    55: [90622, 1867655, 18700076, 92180941, 236519444, 369103338],
}

DS = {
    51: [21845, 31988524, 428597048949, 18870510190034037, 2226628053243742477956, 323412864885270853942840540],
    52: [21845, 31988524, 428597048949, 25467307873635162, 3358089676487133175393, 610353310825031262102720509],
    53: [21845, 43052743, 736340019964, 82883567360966919, 24671918500667380441272, 8048881421864390371643440948],
    54: [21845, 43052743, 736340019964, 82883567360966919, 27574492272300756906897, 11575365984580699037980367511],
    55: [43690, 111931989, 2911463348807, 350556503363400841, 135975582125916386901983, 70738331415946725049094036929],
}

US = {
    51: [63955203, 857162109375, 37740591783019125, 4453237235977294921875, 646823503142488464143203125, 12973323976169836196871966796875],
    52: [63955203, 857162109375, 50934187150221375, 6716153885666392715625, 1220703263560386037072265625, 93551940730324679221030295008125],
    53: [86083641, 1472636987185, 165766398381913875, 49343754117767399915625, 16097738171810280075906440625, 681068651712933962250877357378125],
    54: [86083641, 1472636987185, 165766398381913875, 55148901661034152846875, 23150704394669125775203828125, 5004810589583936002432755707296875],
    55: [223820289, 5822814765625, 701110095263452875, 271950813695329410403125, 141476526856311324181801171875, 37116673993527655709979585017578125],
}

SIGMAS = {
    51: ["0.453731", "0.309920", "0.210133", "0.136511", "0.082347", "0.048317"],
    52: ["0.455220", "0.312600", "0.211366", "0.138182", "0.083732", "0.046115"],
    53: ["0.460935", "0.316984", "0.211826", "0.135723", "0.080581", "0.045968"],
    54: ["0.460939", "0.317065", "0.212394", "0.137014", "0.082705", "0.044822"],
    55: ["0.443781", "0.303923", "0.205510", "0.133587", "0.081183", "0.044491"],
}

Y = {
    51: 415146393628852899831187352563934,
    52: 2993663218105571862989260568857358,
    53: 21794197199305714795938830772522725,
    54: 160153987475679647486755841698814824,
    55: 1187733759619473153677783755951573821,
}
W = {51: 21844, 52: 21844, 53: 21844, 54: 21844, 55: 43689}
TAU = {51: 124001280, 52: 155001600, 53: 310003200, 54: 350438400, 55: 452874240}
EXPECTED = {
    51: (Decimal("0.000542135786332180"), Decimal("-19.5953515442")),
    52: (Decimal("0.000488608023294683"), Decimal("-19.8662364353")),
    53: (Decimal("0.000443191288757114"), Decimal("-20.1204527074")),
    54: (Decimal("0.000438131601230971"), Decimal("-20.1503725273")),
    55: (Decimal("0.000374184125626777"), Decimal("-20.5614878456")),
}


def primes_upto(n: int) -> list[int]:
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for p in range(2, isqrt(n) + 1):
        if sieve[p]:
            for multiple in range(p * p, n + 1, p):
                sieve[multiple] = False
    return [p for p, keep in enumerate(sieve) if keep]


def vp_factorial(n: int, p: int) -> int:
    total = 0
    while n:
        n //= p
        total += n
    return total


def core_exponents(n: int) -> dict[int, int]:
    result = {}
    for p in primes_upto(n):
        if p == 2:
            continue
        exponent = vp_factorial(n, p) - (1 if p == 3 else 0)
        if exponent > 0:
            result[p] = exponent
    return result


def log_z(n: int, sigma: Decimal) -> Decimal:
    total = Decimal(0)
    for p, exponent in core_exponents(n).items():
        log_p = Decimal(p).ln()
        local = sum(
            ((-sigma * Decimal(j) * log_p).exp() for j in range(exponent + 1)),
            Decimal(0),
        )
        total += local.ln()
    return total


def replay(n: int) -> tuple[Decimal, Decimal]:
    v2 = vp_factorial(n, 2)
    core = factorial(n) // (3 * (2 ** v2))
    median = isqrt(core)
    if median * median < core:
        median += 1

    log_product = Decimal(0)
    for k, d, actual_u, sigma_text in zip(KS[n], DS[n], US[n], SIGMAS[n]):
        sigma = Decimal(sigma_text)
        log_rankin = (Decimal(k).ln() - log_z(n, sigma)) / sigma
        assert log_rankin <= Decimal(actual_u).ln(), (n, k, "Rankin bound exceeds exact U")

        candidates = [Decimal(2 * k - 1).ln(), log_rankin]
        if 2 * k > TAU[n]:
            candidates.append(Decimal(median).ln())
        span = max(candidates).exp()
        denominator = Decimal(d + 1)
        log_product += ((denominator + span) / denominator).ln()

    log_ratio = log_product - (Decimal(Y[n] + 1) / Decimal(W[n] + 1)).ln()
    root_ratio = (log_ratio / Decimal(6)).exp()
    log10_ratio = log_ratio / Decimal(10).ln()
    return root_ratio, log10_ratio


def main() -> None:
    tolerance = Decimal("5e-15")
    for n in range(51, 56):
        root, log10_ratio = replay(n)
        expected_root, expected_log = EXPECTED[n]
        assert abs(root - expected_root) < tolerance
        assert abs(log10_ratio - expected_log) < Decimal("5e-10")
        print(f"PASS n={n} root={root:.18E} log10_ratio={log10_ratio:.12f}")
    print("PASS N2-ADD-127 Rankin lower bounds")
    print("PASS N2-ADD-128 carrier product")
    print("PASS N2-CMP-208 fixed-parameter rows")


if __name__ == "__main__":
    main()
