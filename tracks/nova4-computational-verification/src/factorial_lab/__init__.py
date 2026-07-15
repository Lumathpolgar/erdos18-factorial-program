"""Exact computational tools for distinct-divisor representations of n!."""

from .arithmetic import (
    divisors_of_factorial,
    factorial_prime_valuations,
    is_divisor_of_factorial,
    prime_sieve,
)
from .certificates import CertificateError, verify_representation_certificate
from .search import exact_profile_dp, exact_reachability_by_cardinality

__all__ = [
    "CertificateError",
    "divisors_of_factorial",
    "exact_profile_dp",
    "exact_reachability_by_cardinality",
    "factorial_prime_valuations",
    "is_divisor_of_factorial",
    "prime_sieve",
    "verify_representation_certificate",
]
