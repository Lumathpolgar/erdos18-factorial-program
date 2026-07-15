# Problem Statement

## Erdős Problem 18, factorial formulation

For a practical number `N`, define `h(N)` to be the least integer such that every integer `x` with

```text
1 <= x < N
```

can be represented as a sum of at most `h(N)` distinct positive divisors of `N`.

The direct target of this repository is:

> Prove that there are absolute constants `C` and `K` such that, for all sufficiently large `n`,
>
> ```text
> h(n!) <= K (log n)^C.
> ```

Equivalently,

```text
h(n!) < (log n)^{O(1)}.
```

## Working local notation

For a positive integer `N` and real `X >= 1`, define

```text
H_N(X)
```

to be the smallest `k` such that every integer in the relevant interval below `X` has a representation as a sum of at most `k` distinct divisors of `N`. Each theorem must state the precise interval convention it uses.

## Current sufficient theorem

The completed conditional endgame reduces the main objective to a direct factorial half-range theorem:

```text
H_{n!}(floor(sqrt(n!)) + 1) = O((log n)^2).
```

Under the audited Track B conversion, this implies

```text
h(n!) = O((log n)^3).
```

## Stronger historical route

The earlier Track A program attempted to prove a stronger local theorem for

```text
L_m = lcm(1, 2, ..., m),
```

namely

```text
H_{L_m}(floor(L_m^(1/3)) + 1) = O(log m).
```

That theorem remains open. The direct factorial program does not assume it.

## Required standard of proof

A final solution must include:

- exact definitions and quantifiers
- valid asymptotic ranges
- explicit constants or a justified asymptotic constant regime
- distinctness of all selected divisors
- treatment of all boundary intervals
- a proof that finite exceptions are covered
- independent reconstruction or audit of every critical implication
