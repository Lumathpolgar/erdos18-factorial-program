"""Exact subset-sum search and independent cardinality bounds."""

from __future__ import annotations

from dataclasses import dataclass
from math import factorial, isqrt
from typing import Iterable

from .arithmetic import divisors_of_factorial


@dataclass(frozen=True)
class ExactProfile:
    n: int
    target_limit: int
    eligible_divisors: tuple[int, ...]
    lambda_values: tuple[int, ...]
    witnesses: tuple[tuple[int, ...], ...]

    @property
    def H(self) -> int:
        return max(self.lambda_values)


def exact_profile_dp(n: int, target_limit: int | None = None) -> ExactProfile:
    """Compute exact minimum term counts and witnesses by 0/1 dynamic programming.

    Search space: every subset of positive divisors d | n! with d <= target_limit.
    Completeness: divisors larger than the target limit cannot occur in a positive sum
    not exceeding that limit. Descending target updates enforce one use per divisor.
    """
    if isinstance(n, bool) or not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")
    if target_limit is None:
        target_limit = isqrt(factorial(n))
    if isinstance(target_limit, bool) or not isinstance(target_limit, int) or target_limit < 0:
        raise ValueError("target_limit must be a nonnegative integer")

    divisors = tuple(divisors_of_factorial(n, max_value=max(1, target_limit)))
    witnesses: list[tuple[int, ...] | None] = [None] * (target_limit + 1)
    witnesses[0] = ()

    for divisor in divisors:
        if divisor > target_limit:
            continue
        for total in range(target_limit, divisor - 1, -1):
            prefix = witnesses[total - divisor]
            if prefix is None:
                continue
            candidate = prefix + (divisor,)
            current = witnesses[total]
            if current is None or len(candidate) < len(current) or (
                len(candidate) == len(current) and candidate < current
            ):
                witnesses[total] = candidate

    missing = [target for target, witness in enumerate(witnesses) if witness is None]
    if missing:
        raise RuntimeError(
            f"exact profile has unrepresented targets; first missing target is {missing[0]}"
        )

    final_witnesses = tuple(witness for witness in witnesses if witness is not None)
    lambda_values = tuple(len(witness) for witness in final_witnesses)
    return ExactProfile(
        n=n,
        target_limit=target_limit,
        eligible_divisors=divisors,
        lambda_values=lambda_values,
        witnesses=final_witnesses,
    )


def exact_reachability_by_cardinality(
    divisors: Iterable[int], target_limit: int, max_terms: int
) -> tuple[int, ...]:
    """Compute exact-k reachable sums as Python-integer bitsets.

    This is independent of the min-count DP representation. For each divisor, layers
    are updated in descending cardinality, so each numerical divisor is used at most once.
    Bits above target_limit are masked away, a safe pruning because all later additions
    are nonnegative.
    """
    if target_limit < 0 or max_terms < 0:
        raise ValueError("target_limit and max_terms must be nonnegative")
    mask = (1 << (target_limit + 1)) - 1
    exact = [0] * (max_terms + 1)
    exact[0] = 1
    processed = 0
    for divisor in sorted(set(divisors)):
        if divisor <= 0:
            raise ValueError("divisors must be positive")
        if divisor > target_limit:
            continue
        processed += 1
        upper = min(max_terms, processed)
        for k in range(upper, 0, -1):
            exact[k] |= (exact[k - 1] << divisor) & mask
    return tuple(exact)


def minimum_counts_from_bitsets(
    exact_by_cardinality: tuple[int, ...], target_limit: int
) -> tuple[int, ...]:
    result: list[int] = []
    for target in range(target_limit + 1):
        count = next(
            (k for k, bits in enumerate(exact_by_cardinality) if (bits >> target) & 1),
            None,
        )
        if count is None:
            raise RuntimeError(f"target {target} not reached within supplied max_terms")
        result.append(count)
    return tuple(result)


def certify_profile_with_bitsets(profile: ExactProfile) -> None:
    """Raise if independent exact-cardinality reachability disagrees with the DP profile."""
    exact = exact_reachability_by_cardinality(
        profile.eligible_divisors, profile.target_limit, profile.H
    )
    independent = minimum_counts_from_bitsets(exact, profile.target_limit)
    if independent != profile.lambda_values:
        for target, (left, right) in enumerate(zip(profile.lambda_values, independent)):
            if left != right:
                raise AssertionError(
                    f"optimality disagreement at target {target}: DP={left}, bitset={right}"
                )
        raise AssertionError("optimality methods disagree")


def descending_greedy(
    divisors: Iterable[int], target: int, *, presorted_ascending: bool = False
) -> tuple[int, ...] | None:
    """Largest-available-divisor-first representation, or None if it gets stuck.

    With presorted_ascending=True, the caller promises a strictly increasing sequence.
    Residuals decrease, so binary search can skip every divisor that is too large while
    preserving the exact descending greedy rule.
    """
    from bisect import bisect_right

    if target < 0:
        raise ValueError("target must be nonnegative")
    ordered = tuple(divisors) if presorted_ascending else tuple(sorted(set(divisors)))
    if any(d <= 0 for d in ordered):
        raise ValueError("divisors must be positive")
    if any(left >= right for left, right in zip(ordered, ordered[1:])):
        raise ValueError("presorted divisors must be strictly increasing")

    residual = target
    chosen: list[int] = []
    upper = len(ordered)
    while residual > 0:
        index = bisect_right(ordered, residual, 0, upper) - 1
        if index < 0:
            return None
        divisor = ordered[index]
        chosen.append(divisor)
        residual -= divisor
        upper = index
    return tuple(sorted(chosen))
