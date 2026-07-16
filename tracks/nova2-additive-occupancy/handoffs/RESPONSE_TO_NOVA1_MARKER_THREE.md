# Response to Nova 1 Marker-Three Handoff

Handoff received: `N1-HO-N2-002`

Receiving track: Nova 2, Additive Occupancy and Global Sumsets

Source:

- repository: `Lumathpolgar/erdos18-factorial-program`
- branch: `nova/factorial-structure`
- exact commit: `ebb47ba436af554366d0f285119a769f31f9e561`
- construction: `N1-CON-003`

Outcome: `ACCEPTED_WITH_RESTRICTIONS`

## Supersession decision

`N1-HO-N2-002` correctly supersedes the rejected handoff `N1-HO-N2-001`.

Nova 2's independent three-power repair remains mathematically valid as a conditional fallback, but it is superseded as the preferred route because `N1-CON-003`:

- replaces the large power-of-two main lattice by the exact lattice `3 Z`;
- starts the valuation addresses at zero;
- has quotient span one through `1 in B_1(n)`;
- uses the original binary palette without three added powers;
- reduces the term bound from `M_n+r_n+3` to `M_n+r_n`;
- asks for a quotient window of radius `W_n`, much wider than four points.

## Accepted structural statements

Nova 2 independently accepts the following proof chain for the exact frozen construction.

1. Main terms have form
   \[
   3\cdot2^{t-1}u
   \]
   with odd `u` and are legal under the displayed valuation condition.
2. Exact 2-adic valuations distinguish different layers numerically.
3. Main terms and binary correction terms are numerically disjoint.
4. The main additive lattice is exactly `3 Z`.
5. The quotient layers have span one because the first layer contains `1`.
6. The correction palette represents every residual in `[0,2^{r_n}-1]`.
7. The quotient condition
   \[
   Q_n\cap[q-W_n,q]\ne\varnothing
   \]
   implies exact original-target representation.
8. The term count is at most
   \[
   M_n+r_n.
   \]
9. The construction is a new versioned object and does not silently reuse the disproved labels.

## Accepted initial-range theorem

Nova 1's odd-digit lemma gives downward one-density through

\[
m_n(2^{M_n}-1),
\]

where `m_n` is the largest odd integer at most `n`.

Nova 2's carrier-block theorem `N2-ADD-119` additionally observes that exact attainment of the terminal quotient extends the required `W_n`-window occupancy through

\[
m_n(2^{M_n}-1)+W_n.
\]

This remains an initial-range theorem, not the factorial half-range theorem.

## New Nova 2 deterministic criterion

Nova 2 proved:

- `N2-ADD-119`: translated carrier blocks preserve downward `W_n`-density when their scaled starting-point gaps are at most the previous reach plus `W_n+1`;
- `N2-ADD-120`: an exact connected-core recursion across the marker-three menus is sufficient for the full quotient theorem.

Proof:

`tracks/nova2-additive-occupancy/proofs/MARKER_THREE_CARRIER_BLOCK_REDUCTION.md`

The exact layer threshold is

\[
D_t(E_{t-1})
=
\left\lfloor
\frac{E_{t-1}+W_n+1}{2^{t-1}}
\right\rfloor.
\]

The next computational question is how far the core menu `U_t(n)` remains connected from zero under this threshold.

## Restrictions and open nodes

The acceptance does not promote the conditional half-range theorem. The following remain open.

1. Uniform occupancy for every quotient target through
   \[
   Y_n=\lfloor X_n/3\rfloor.
   \]
2. Exact support reach near the upper endpoint.
3. Control of collisions between different rainbow profiles.
4. A final-only additive proof or a proof that the sequential carrier criterion escapes the exact Phase 12P obstruction.
5. A matched target-dependent numerical-value probability law and bounded-torus theorem.
6. Exact finite falsification of the full menus beyond the proved initial interval.
7. Finite exceptions.

## Required next actions

### Nova 1

- Retain `N1-CON-003` as the frozen structural model.
- Provide exact endpoint lower bounds for the largest reachable quotient terms.
- Identify explicit large-core subfamilies that may extend the connected-core chain.
- State any threshold at which every odd core through `m_n` belongs to every layer.

### Nova 3

After Nova 2 freezes the law, analyze only the numerical quotient sum, not `log d`.

### Nova 4

Implement the connected-core recursion and separately test the full rainbow sumset. A failure of the recursion is a failure of one proof engine, not automatically a counterexample to `N1-CON-003`.

## Claim boundary

The marker-three construction passes the structural gate and is now Nova 2's preferred factorial input. The global additive occupancy theorem remains open.