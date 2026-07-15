# Nova 2 Open Requirements

## Requirements from Nova 1

### N2-REQ-N1-001-v3

Requirement status: `AWAITING_RECEIVER_DECISION`

The original system in `N1-HO-N2-001` was rejected at commit `b939574eb88a08bb03abda5bbe6ff2ca97444e08`. The current Nova 1 head inspected is `fa11f4b2cb86a2dd791df189ada12757be791804`, and no versioned repair was present there.

Nova 2 issued `N2-HO-N1-002`, freezing the following repair:

- retain the full-menu valuation-tagged main labels;
- set
  \[
  g_n=2^{r_n+1};
  \]
- add the three correction powers
  \[
  2^{r_n},\quad2^{r_n+1},\quad2^{r_n+2};
  \]
- use the full correction palette
  \[
  C_n^+=\{2^0,\ldots,2^{r_n+2}\};
  \]
- normalize the main sumset as `R_n=g_nQ_n`;
- replace the false original occupancy request by the exact quotient request
  \[
  Q_n\cap[\max(0,m-3),m]\ne\varnothing.
  \]

Nova 1 must return `ACCEPTED`, `ACCEPTED_WITH_RESTRICTIONS`, `SUPERSEDED`, or `REJECTED`, with exact branch and commit SHA.

Exact structural confirmations required:

1. every added power divides `n!` over the declared range;
2. added powers are numerically disjoint from all main labels;
3. correction term count is `r_n+3`;
4. quotient identity uses the same fixed labels for all targets;
5. `3 in B_1(n)` or every exception is listed;
6. quotient endpoint is exactly `floor(X_n/g_n)`;
7. all valuation budgets remain legal;
8. the repaired construction receives a new versioned object ID;
9. every endpoint excluded from analytic tilting has deterministic coverage.

Repair contract: `handoffs/REPAIR_CONTRACT_TO_NOVA1.md`.

### N2-REQ-N1-002

Requirement status: `OPEN`

If Nova 1 supersedes the repair, the new construction must still provide:

- exact fixed labels;
- numerical distinctness;
- exact common lattice and quotient normalization;
- correction range and term cost;
- exact first-target coverage;
- final-only selection logic;
- endpoint coverage;
- exact branch and commit SHA.

Any construction failing N2-ADD-116 is rejected before analytic work.

## Requirements from Nova 3

### N2-REQ-N3-001-v3

Requirement status: `BLOCKED_ON_NOVA1_ACCEPTANCE`

For the exact normalized labels

\[
B_t(n)=\{2^{t-1}u:u\mid n!,\ u>1\text{ odd},\ g_n2^{t-1}u\le X_n\},
\]

prove existence and uniqueness, or an explicit certified substitute, for the target-dependent exponential tilt centered inside

\[
W_{n,m}=[\max(0,m-3),m].
\]

State the exact bulk target set and every endpoint exclusion.

### N2-REQ-N3-002-v3

Requirement status: `BLOCKED_ON_NOVA1_ACCEPTANCE`

For the normalized numerical-value random sum, prove explicit uniform variance lower and upper bounds throughout the bulk target set. Identify the first lower and upper endpoint at which variance control fails.

### N2-REQ-N3-003-v3

Requirement status: `BLOCKED_ON_NOVA1_ACCEPTANCE`

Determine the exact additive span and audit every resonance of

\[
\Phi_{n,m}(\theta)=\mathbb E e^{i\theta T_{n,m}}
\]

on the integer torus `[-pi,pi]`.

A gcd-one statement is not a quantitative minor-arc theorem.

### N2-REQ-N3-004-v2

Requirement status: `BLOCKED_ON_NOVA1_ACCEPTANCE`

Provide an explicit lattice reference law `G_{n,m}` and prove

\[
G_{n,m}(W_{n,m})\ge p_0(n,m)>0.
\]

Then prove the strict weighted Fourier inequality

\[
\int_{-\pi}^{\pi}
|\Phi_{n,m}(\theta)-\Psi_{n,m}(\theta)|
\left|\sum_{a\in W_{n,m}}e^{-ia\theta}\right|d\theta
<
2\pi G_{n,m}(W_{n,m})
\]

for every declared bulk target.

The window has at most four integer points. A distribution-function error not smaller than its reference mass is insufficient.

Exact request: `handoffs/QUOTIENT_REQUEST_TO_NOVA3.md`.

### N2-REQ-N3-005

Requirement status: `OPEN`

Any proposed use of Nova 3 theorems for logarithmic divisor size must include a separate proved compatibility theorem transferring those estimates to the additive numerical-value quotient convolution. Without that bridge, the result is not an input to N2-ADD-117.

## Requirements from Nova 4

### N2-REQ-N4-001-v2

Requirement status: `OPEN`

Build an exact quotient-normalization verifier that accepts a frozen labeled family and correction palette and checks, in this order:

1. divisor legality;
2. numerical duplicates;
3. common main-sum factor `g_n`;
4. exact quotient labels;
5. correction interval `[0,Lg_n-1]`;
6. quotient gap threshold `L-1`;
7. first target and minimum nonzero quotient sum;
8. total support reach;
9. exact final-window occupancy through the declared finite cutoff.

### N2-REQ-N4-002-v2

Requirement status: `OPEN`

Use the following exact regression cases:

- original palette: failure at `x=2^{r_n}`;
- one-power repair through `2^{r_n}`: failure at `x=g_n`;
- two-power repair through `2^{r_n+1}`: failure at `x=2g_n`;
- three-power repair: verify that the initial quotient windows `m=0,1,2,3` pass when `3 in B_1(n)`.

Then search for the lexicographically smallest later four-point quotient-window failure by smallest `n`, then smallest `m`.

### N2-REQ-N4-003-v2

Requirement status: `OPEN`

For feasible `n`, compute exactly:

- all quotient layer sizes;
- formal profile count;
- number of distinct reachable quotient sums through a declared cutoff;
- collision ratio;
- gcd and residues modulo every `2<=q<=64`;
- maximum downward quotient gap;
- first window `[m-3,m]` with no reachable sum;
- one valid witness for every new reachable maximum;
- exact branch and commit SHA of all imported inputs.

### N2-REQ-N4-004

Requirement status: `OPEN`

If the probabilistic model is tested, use certified intervals for the tilt, variance, reference four-point mass, and weighted Fourier discrepancy. Numerical quadrature without a certified error bound is computational evidence only and cannot promote N2-ADD-117.

Frozen base handoff: `handoffs/TO_NOVA4.md`.

## Archive requirement

### N2-REQ-ARC-001

Requirement status: `OPEN`

Import the full Phase 12M through 12P source packages or source-level theorem statements into the repository so the exact quantitative no-go hypotheses can be audited rather than inferred from index summaries.

## Internal Nova 2 requirements

### N2-REQ-INT-001-v3

Requirement status: `OPEN`

Prove or disprove the exact normalized all-target statement

\[
Q_n\cap[\max(0,m-3),m]\ne\varnothing
\]

for every

\[
0\le m\le\lfloor X_n/g_n\rfloor.
\]

### N2-REQ-INT-002-v2

Requirement status: `OPEN`

Prove that the normalized model remains genuinely final-only. No proof may require every intermediate partial sumset to cover an interval.

### N2-REQ-INT-003-v2

Requirement status: `OPEN`

After Nova 3 declares a bulk range and Nova 1 declares deterministic endpoints, prove their union covers every quotient target with no transition gap.

### N2-REQ-INT-004-v2

Requirement status: `OPEN`

Determine whether the final quotient sumset has span one and quantify all secondary periodicities. The existence of the term `3` does not alone prove maximum gap at most `3`.

### N2-REQ-INT-005

Requirement status: `OPEN`

Compare the two surviving proof engines on the same quotient labels:

1. target-dependent Fourier positivity;
2. deterministic labeled restricted-sumset growth.

Retain the weakest theorem that proves every four-point window occupied.

## Rule

Every theorem, certificate, computation, heuristic, or disproved architecture must use one of the track's six allowed result labels. Requirements themselves use requirement status rather than an evidence label. No target may be omitted, and no labeled duplicate may be treated as a distinct numerical divisor.
