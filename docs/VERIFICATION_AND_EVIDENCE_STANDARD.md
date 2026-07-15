# Verification and Evidence Standard

## Result classes

### PROVED

A complete mathematical proof is present, all dependencies are proved or explicitly accepted, and the result survives independent reconstruction.

### CONDITIONAL

The implication is proved, but at least one named hypothesis remains open.

### FINITE_CERTIFICATE

An exact statement is proved for a finite parameter range by a reproducible certificate or exhaustive computation.

### COMPUTATIONAL_EVIDENCE

A reproducible experiment supports a conjecture but does not exhaust the claimed asymptotic range.

### HEURISTIC

A model, analogy, probabilistic prediction, or informal estimate guides research but is not a theorem.

### DISPROVED

A counterexample or theorem rules out the stated claim.

### OPEN

The claim is neither proved nor disproved.

## Mathematical review checklist

Every critical result must be checked for:

- exact quantifiers;
- endpoint conventions;
- hidden monotonicity assumptions;
- distinctness of divisors;
- collisions between layers or palettes;
- use of integer versus real complementary scales;
- uniformity in the target variable;
- valid asymptotic ranges;
- circularity;
- finite exceptions;
- whether external theorems are quoted with matching hypotheses.

## Computational requirements

Every program used as evidence must include:

- deterministic entry point or recorded random seed;
- dependency and language version information;
- documented input and output format;
- assertions for divisor legality and distinctness;
- exact arithmetic whenever feasible;
- checksums or stable identifiers for large datasets;
- tests that deliberately feed invalid certificates;
- fail-closed behavior.

A verifier must not trust precomputed summary fields when it can recompute them from the certificate.

## Exact certificate requirements

A representation certificate for target `x` must list selected divisors and verify:

```text
all d divide n!
all d are positive
all d are numerically distinct
sum(d) = x
number of terms <= claimed bound
```

An interval certificate must additionally establish completeness over every target in the stated interval.

## Independent reconstruction

For a theorem on the final proof path, the reviewer should reconstruct the argument from the theorem statement and dependencies before reading the author's proof details. Discrepancies must be logged.

## External results

Any imported theorem must record:

- author and source;
- exact theorem number or statement;
- version or publication information;
- hypotheses as used;
- a short proof of compatibility with repository notation.

## Failed tests

A failed verifier, missing dependency, timeout, or numerical overflow blocks promotion. It must not be described as a pass with qualifications.

## Publication threshold

A candidate solution is publication-ready only when:

1. the proof chain is closed;
2. all imported results are verified;
3. finite exceptions are handled;
4. independent reviewers reproduce the proof;
5. code and certificates pass from a clean environment;
6. the final manuscript clearly distinguishes new results from known results.
