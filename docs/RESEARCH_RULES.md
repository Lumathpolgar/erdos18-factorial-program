# Research Rules

## 1. Truth status is mandatory

Every mathematical statement entering the repository must be labeled as one of:

- proved theorem
- conditional theorem
- finite certificate
- computational evidence
- heuristic
- conjecture
- disproved statement
- retired proof route

## 2. No percentage solved

The repository will not report a percentage of completion unless a fixed, auditable metric is defined in advance. Completed phases are not a reliable measure of distance to an open theorem.

## 3. Fail closed

A conditional chain may not be promoted to an unconditional result while any hypothesis remains open.

A merge contract must identify every external theorem dependency and its current status.

## 4. Finite evidence is not asymptotics

Exact verification for finitely many `n` may:

- falsify a universal claim
- support a conjecture
- reveal structural patterns
- validate code and witness reconstruction

It may not prove an asymptotic theorem without a separate mathematical argument.

## 5. Distinctness must be explicit

Every additive representation must verify that all selected divisors are distinct. Packet or color constructions must state why cross-packet collisions cannot occur.

## 6. Domain conditions must be checked

Every lemma must state and verify:

- integrality assumptions
- divisibility assumptions
- interval endpoints
- asymptotic range
- monotonicity requirements
- dependence of constants

## 7. Independent verification

Any theorem that closes a major dependency should receive:

1. a line-by-line proof audit
2. independent reconstruction of the implication chain
3. computational checks on all finite boundary cases that the proof excludes from its asymptotic range

## 8. Failed routes remain valuable

A failed route should be archived with:

- its exact claim
- the strongest theorem actually proved
- the obstruction or counterexample
- the scope of the obstruction
- any surviving lemmas

## 9. Parallel Nova isolation

Each Nova track must work on its own branch and must not silently import unproved conclusions from another track. Shared lemmas enter another track only after they are committed with a truth-status label and reviewed.

## 10. Final solution standard

A claimed solution requires a single integrated manuscript in which every lemma is unconditional or has a discharged hypothesis, followed by a clean-room audit that starts from the definitions and reconstructs the full proof.
