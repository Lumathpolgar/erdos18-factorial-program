"""Exact computational tools for distinct-divisor representations of n!."""

from .arithmetic import (
    divisors_of_factorial,
    factorial_prime_valuations,
    is_divisor_of_factorial,
    prime_sieve,
)
from .certificates import CertificateError, verify_representation_certificate
from .search import exact_profile_dp, exact_reachability_by_cardinality
from .lattice import verify_label_family_certificate
from .logcert import certified_log_parameters
from .n2_audit import audit_n2_obs_107_range, verify_n2_obs_107_certificate

__all__ = [
    "CertificateError",
    "divisors_of_factorial",
    "exact_profile_dp",
    "exact_reachability_by_cardinality",
    "factorial_prime_valuations",
    "is_divisor_of_factorial",
    "prime_sieve",
    "verify_representation_certificate",
    "audit_n2_obs_107_range",
    "certified_log_parameters",
    "verify_label_family_certificate",
    "verify_n2_obs_107_certificate",
]
