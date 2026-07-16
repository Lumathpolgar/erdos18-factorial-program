# Independent audit of Nova 3 request E

Date: 2026-07-16

## Frozen source

- repository: `Lumathpolgar/erdos18-factorial-program`
- branch: `nova/analytic-density`
- superseding handoff: `N3-HO-N4-002`
- handoff commit: `7469dada02fa4caca08ed391ef8b0cb0f1e855b2`
- source-ledger commit: `697e7ed8bdb03f54b2389b2fcdd8b685dadcebc4`
- request: `E`

No later source-ledger revision is included.

## Decisions

| Object | Decision |
|---|---|
| Request E | `ACCEPTED` |
| `N3-SRC-004`, Ford | `SOURCE_SCOPE_CONFIRMED_DIRECT_FACTORIAL_USE_REJECTED` |
| `N3-SRC-005`, Drappeau–Tenenbaum | `SOURCE_SCOPE_CONFIRMED_METHOD_ONLY` |
| `N3-SRC-006`, ultrafriable progressions | `SOURCE_SCOPE_CONFIRMED_DIRECT_FACTORIAL_USE_REJECTED` |
| Any cited source directly selects `n!` | `NO` |

## Ford: ambient integers, not one fixed factorial

Ford defines

```text
tau(m;y,z) = number of divisors d of m with y < d <= z,
H(x,y,z) = number of positive integers m <= x with tau(m;y,z) > 0.
```

The theorem estimates an ambient count over every integer `m<=x`. It is not a theorem about the divisor count of one fixed integer.

The exact finite witness is:

```text
n = 5
N = 5! = 120
interval = (6,7]
H(120,6,7) = 17
tau(120;6,7) = 0
```

The ambient count is positive because the multiples of `7` are counted, while `120` itself has no divisor in `(6,7]`. Therefore an estimate for `H(x,y,z)` cannot be converted into a pointwise lower or upper bound for local divisors of `n!` without a new argument.

## Drappeau–Tenenbaum: almost all friable integers

Theorem 1.1 of arXiv:1604.04204v1 gives the Gaussian divisor-law approximation for all integers in `S(x,y)` except a quantified exceptional subset. Its quantifier is not “every friable integer.”

For example, `10!` is `10`-friable and belongs to `S(10!,10)`, but the theorem does not provide a certificate that this deterministic member lies outside the exceptional set. A conditional density tending to one does not identify a prescribed sparse sequence.

The exact independent exponent-coordinate decomposition is methodologically compatible with the factorial model, but the source theorem itself does not establish a Gaussian law for `n!`.

## Ultrafriable progressions: common prime-power cap

For a common parameter `y`, the source defines `y`-ultrafriable integers by the condition that every prime power occurring in the canonical factorization is at most `y`. Equivalently,

```text
a_p <= floor(log y / log p)
```

for every prime coordinate.

Divisors of `n!` instead obey

```text
a_p <= v_p(n!) = sum_{k>=1} floor(n/p^k),
```

which is a prime-dependent factorial valuation cap.

The mismatch is exact already at `n=10`:

```text
v_2(10!) = 8, so 2^8 = 256 must be allowed.
If y < 256, the divisor 256 of 10! is excluded from U(10!,y).
If y >= 256, the prime 11 is included in U(10!,y), but 11 does not divide 10!.
```

Thus no common parameter `y` makes `U(10!,y)` equal the divisor set of `10!`. Even when the exact factorial divisor set is embedded in a larger ultrafriable set, lower bounds for that larger set do not transfer to the subset.

## Machine-verifiable witnesses

The verifier independently recomputes:

- `H(120,6,7)=17` and `tau(120;6,7)=0`;
- `10!` is `10`-friable, while no source nonexceptionality certificate is present;
- `v_2(10!)=8`, `256|10!`, and `11∤10!`;
- all three direct-factorial-use classifications;
- frozen handoff and source-ledger metadata;
- semantic checksums.

Full audit semantic SHA-256:

```text
a5be7514baa9c327e27fa27fccb7d9de0f687d42515b3e8b1de2c949387b662f
```

Compatibility claim semantic SHA-256:

```text
ae60e9e8758df8113ac249404d8660c5ae4bb5edf02b3aab342c43c47a8124ba
```

## Validation

- 10 new source-compatibility tests pass;
- full audit replay passes;
- valid compatibility claim replay passes;
- a rehashed claim falsely asserting direct factorial applicability is rejected;
- rehashed removal of the friable exceptional-set qualifier is rejected;
- rehashed ultrafriable-set equality is rejected;
- wrong handoff metadata is rejected;
- no timeout or unknown result occurred.

## Scope restriction

This audit confirms source scope and legal comparison direction. It does not reprove the cited analytic theorems, prove a deterministic Gaussian law for factorial divisors, prove local additive occupancy, prove the factorial half-range theorem, or solve Erdős Problem 18.

## Next target

Run request F of `N3-HO-N4-002`: reconstruct Dusart Theorem 6.9 from the primary source and independently derive the explicit prime-interval threshold used by `N3-ANA-010`.
