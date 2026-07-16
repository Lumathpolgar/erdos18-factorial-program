# Exact Search and Bound Methods

Date: 2026-07-15

## Method A: Minimum-cardinality 0/1 dynamic programming

Result class: `exact finite theorem audit`

### Search space

For fixed `n` and integer target limit `T`, the method uses every positive divisor `d` of `n!` with `d <= T`. It considers every distinct-divisor subset through the standard 0/1 subset-sum recurrence.

### Completeness

A divisor larger than `T` cannot occur in a positive sum whose value is at most `T`. Removing such divisors is therefore exact. Descending target updates ensure each numerical divisor is used at most once.

### Output

For every integer `0 <= x <= T`, the method returns:

- the exact value of `lambda_{n!}(x)`;
- a concrete witness tuple of distinct divisors;
- the exact maximum over the interval.

### Pruning rules

- Divisors greater than `T` are omitted.
- Partial sums greater than `T` are omitted.
- A state is replaced only by a representation with fewer terms, or by a deterministic lexicographically smaller witness with the same term count.

Each pruning rule is safe because all terms are positive integers and no later operation can reduce a partial sum.

### Memory and timeout semantics

The method stores one witness tuple for each sum in `[0,T]`. Memory is `O(T)` states plus witness tuples. Runtime is proportional to the number of eligible divisors times `T` in the worst case. A process limit or timeout produces `unknown due to resource limits`.

## Method B: Exact-cardinality bitset reachability

Result class: `certified lower bound`

### Search space

For the same divisor set, the method maintains one integer bitset for every exact cardinality `k`. Bit `x` is set in layer `k` exactly when `x` is representable by `k` distinct eligible divisors.

### Completeness

Each divisor updates cardinality layers in descending order. This prevents repeated use of the current divisor. The recurrence enumerates all distinct-divisor subsets by cardinality.

### Rigorous lower bound

If target `x` does not occur in layers `0,1,...,k-1`, then no representation with fewer than `k` terms exists. If it occurs in layer `k`, Method B certifies the exact lower bound `lambda_{n!}(x) >= k` and the existence of a `k`-term representation.

### Pruning rules

Bits above `T` are masked after every shift. This is safe because all future additions are nonnegative. Divisors greater than `T` are omitted for the same reason as Method A.

### Independence

Method B does not use Method A predecessors, witnesses, or minimum-count states. The published dataset is accepted only when its minimum counts match Method B for every target.

### Memory and timeout semantics

For maximum tested term count `K`, memory is `O(KT)` bits. A timeout is unknown and is not a lower bound.

## Witness verification

Witnesses are exported through `erdos18.factorial.representation.v1`. The standalone verifier independently recomputes:

- positivity;
- exact divisibility by `n!` through prime valuations;
- numerical distinctness regardless of labels;
- exact integer sum;
- target range membership;
- term count.

Producer metadata and cached summaries are ignored as proof inputs.
