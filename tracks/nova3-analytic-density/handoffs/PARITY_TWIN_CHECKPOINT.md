# Parity Twin Checkpoint

Checkpoint ID: `N3-CHK-007`

Date: 2026-07-15

Branch: `nova/analytic-density`

## Imported current heads

- Nova 1: `nova/factorial-structure@1b81ec74f907d57d520bcf6c51f2e6e71f0474a7`
- Nova 2: `nova/additive-occupancy@e443674f86b2ee3c7037ac94ee47f6b8a4b3b29f`

## New theorem package

- `N3-ANA-023`: parity twin near-resonance and aggregate-dispersion collapse at `pi`
- `N3-ANA-024`: parity mismatch obstruction for reference laws
- `N3-ANA-025`: exact odd-lattice normalization with common tilt `2 lambda`
- `N3-FIN-007`: finite parity and transformed-law verifier
- `N3-COMP-006`: selected large parity-zero and `pi` modulus scales

## Core commits

- initial proof: `70b08c43f8ecf64751ce36534c1558c3577010c3`
- proof formatting correction: `a1625416075f71a170ca17f1f67114ca8ded9c49`
- verifier: `39ba9e699bff049c607e9ec256513e36ebcfeb82`
- Nova 2 handoff: `bb3f26013df869080af7ab6bac5f812bacdaf702`
- Nova 4 handoff: `80af9e4dad28c530613403668fe2b6f265b065c0`
- candidate correction: `6f9cb4cc419eb5481afa88edd22e494b4c5f54c7`
- theorem registry: `29c14a566c702bac4f7af1cfde39695440e37657`
- status: `1980a99bf6ee644fef127ff527f1420fe5a40933`
- open requirements: `d1e42e7864bacba069918da08324be5cf36cc8d4`
- preferred route: `4830b6afa9418bee10b18a7689d502659697c7cd`
- README: `6dd6d545e5cec62940b04cf98491f77aa2aef669`

## Verification command

```text
python3 tracks/nova3-analytic-density/proofs/parity_twin_sanity.py
```

## Exact route decision

The unnormalized zero-only major-arc plan is rejected. The preferred route is:

1. condition on the odd component;
2. subtract one and divide by two;
3. retain common tilt `2 lambda`;
4. use the transformed interval `J_{n,q}`;
5. audit every transformed secondary resonance;
6. prove transformed aggregate dispersion or a transformed weighted integral estimate;
7. retain collision multiplicity in the reference law.

## Claim boundary

This checkpoint does not prove quotient occupancy, the factorial half-range theorem, or Erdős Problem 18.
