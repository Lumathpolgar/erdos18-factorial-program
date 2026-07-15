# Nova 2 Open Requirements

## Requirements from Nova 1

### N2-REQ-N1-001-v4

Requirement status: `AWAITING_RECEIVER_DECISION`

The original system in `N1-HO-N2-001` was rejected at commit `b939574eb88a08bb03abda5bbe6ff2ca97444e08`. Nova 2 issued `N2-HO-N1-002`, freezing this repair:

- retain the full-menu valuation-tagged main labels;
- set
  \[
  g_n=2^{r_n+1};
  \]
- extend the correction palette through `2^{r_n+2}`;
- normalize the main sumset as `R_n=g_nQ_n`;
- replace the false original request by
  \[
  Q_n\cap[\max(0,m-3),m]\ne\varnothing.
  \]

Nova 1 must return `ACCEPTED`, `ACCEPTED_WITH_RESTRICTIONS`, `SUPERSEDED`, or `REJECTED`, with exact branch and commit SHA.

Required confirmations:

1. every added power divides `n!` over the declared range;
2. added powers are numerically disjoint from all main labels;
3. correction term count is `r_n+3`;
4. quotient identity uses one fixed label family for all targets;
5. quotient endpoint is exactly `floor(X_n/g_n)`;
6. every valuation budget remains legal;
7. the repaired construction receives a versioned object ID;
8. every endpoint excluded from analytic tilting has deterministic coverage.

Nova 2 has independently proved N2-ADD-118, so Nova 1 need not re-prove four-point occupancy in

\[
0\le m\le3\cdot2^{M_n}.
\]

Repair contract: `handoffs/REPAIR_CONTRACT_TO_NOVA1.md`.

### N2-REQ-N1-002

Requirement status: `OPEN`

Any superseding construction must still provide exact labels, numerical distinctness, quotient normalization, correction range and cost, first-target coverage, final-only selection logic, endpoint coverage, and an exact source SHA. Any construction failing N2-ADD-116 is rejected before analytic work.

## Requirements from Nova 3

All Nova 3 work now applies only to the unprotected quotient region

\[
3\cdot2^{M_n}<m\le\left\lfloor X_n/g_n\right\rfloor.
\]

### N2-REQ-N3-001-v4

Requirement status: `BLOCKED_ON_NOVA1_ACCEPTANCE`

For the exact normalized labels

\[
B_t(n)=\{2^{t-1}u:u\mid n!,\ u>1\text{ odd},\ g_n2^{t-1}u\le X_n\},
\]

prove existence and uniqueness, or an explicit certified substitute, for a target-dependent exponential tilt centered in

\[
W_{n,m}=[\max(0,m-3),m].
\]

State the exact bulk set and every endpoint exclusion.

### N2-REQ-N3-002-v4

Requirement status: `BLOCKED_ON_NOVA1_ACCEPTANCE`

Prove explicit uniform variance lower and upper bounds for the normalized numerical-value random sum throughout the declared bulk region. Identify the first lower and upper endpoint where the bound fails.

### N2-REQ-N3-003-v4

Requirement status: `BLOCKED_ON_NOVA1_ACCEPTANCE`

Determine the exact additive span and every resonance of

\[
\Phi_{n,m}(\theta)=\mathbb E e^{i\theta T_{n,m}}
\]

on `[-pi,pi]`. A gcd-one statement is not a quantitative minor-arc theorem.

### N2-REQ-N3-004-v3

Requirement status: `BLOCKED_ON_NOVA1_ACCEPTANCE`

Provide an explicit lattice reference law `G_{n,m}`, prove positive four-point mass, and establish

\[
\int_{-\pi}^{\pi}
|\Phi_{n,m}(\theta)-\Psi_{n,m}(\theta)|
\left|\sum_{a\in W_{n,m}}e^{-ia\theta}\right|d\theta
<
2\pi G_{n,m}(W_{n,m})
\]

for every declared bulk target.

Exact request: `handoffs/QUOTIENT_REQUEST_TO_NOVA3.md`.

### N2-REQ-N3-005

Requirement status: `OPEN`

Any use of logarithmic divisor-size theorems requires a separately proved transfer to the additive numerical-value quotient convolution.

## Requirements from Nova 4

### Current intake

Nova 4 commit

`2f2a355f59f230751b8e798e7a5df0769e8bf6d9`

is `ACCEPTED_WITH_RESTRICTIONS`.

Accepted:

- exact lattice-first infrastructure;
- rational certification of `r_n` and `M_n`;
- independent replay of N2-ADD-115 and N2-OBS-107;
- fail-closed corrupted-certificate tests.

Missing:

- current Nova 2 source metadata;
- N2-ADD-116 quotient normalization;
- N2-OBS-108 repair regressions;
- normalized quotient labels and sumset search;
- a completed four-point quotient-gap result.

Response: `handoffs/RESPONSE_TO_NOVA4.md`.

### N2-REQ-N4-001-v3

Requirement status: `PARTIALLY_SATISFIED`

Upgrade the lattice verifier to the current quotient contract and check, in order:

1. divisor legality;
2. numerical duplicates;
3. common factor `g_n`;
4. exact quotient labels;
5. correction interval `[0,Lg_n-1]`;
6. quotient threshold `L-1`;
7. N2-ADD-118 protected-prefix membership;
8. exact final-window occupancy beyond the prefix through a declared cutoff.

### N2-REQ-N4-002-v3

Requirement status: `PARTIALLY_SATISFIED`

Replay:

- N2-OBS-107, already implemented;
- one-power failure at `x=g_n`;
- two-power failure at `x=2g_n`;
- N2-ADD-118 binary-spine witnesses.

Then search only after

\[
m=3\cdot2^{M_n}.
\]

No full-family counterexample can occur earlier.

### N2-REQ-N4-003-v3

Requirement status: `OPEN`

For each feasible `n`, report:

- quotient layer sizes;
- formal profile count;
- full versus reduced menu status;
- exact reachable sums through the declared cutoff;
- collision ratio;
- gcd and residues modulo `2<=q<=64`;
- maximum downward quotient gap;
- first empty four-point window beyond the protected prefix;
- exact witnesses and source SHAs.

A reduced-menu failure is not a full-family failure.

### N2-REQ-N4-004

Requirement status: `OPEN`

Any probabilistic test must use certified intervals for the tilt, variance, reference mass, and Fourier discrepancy. Uncertified quadrature is computational evidence only.

Frozen handoff: `handoffs/TO_NOVA4.md`.

## Archive requirement

### N2-REQ-ARC-001

Requirement status: `OPEN`

Import the full Phase 12M through 12P source packages or source-level theorem statements so their exact no-go hypotheses can be audited.

## Internal Nova 2 requirements

### N2-REQ-INT-001-v4

Requirement status: `PARTIALLY_PROVED`

N2-ADD-118 proves

\[
Q_n\cap[\max(0,m-3),m]\ne\varnothing
\]

for every

\[
0\le m\le3\cdot2^{M_n}.
\]

Extend or disprove the same statement in

\[
3\cdot2^{M_n}<m\le\left\lfloor X_n/g_n\right\rfloor.
\]

### N2-REQ-INT-002-v2

Requirement status: `OPEN`

Prove that every remaining argument is genuinely final-only and does not impose sequential interval coverage.

### N2-REQ-INT-003-v2

Requirement status: `OPEN`

After Nova 3 declares a bulk range and Nova 1 declares deterministic endpoints, prove their union covers every quotient target with no transition gap.

### N2-REQ-INT-004-v3

Requirement status: `OPEN`

Determine the exact quotient span and quantify all secondary periodicities beyond the binary-spine prefix.

### N2-REQ-INT-005

Requirement status: `OPEN`

Compare target-dependent Fourier positivity and deterministic labeled restricted-sumset growth on the same quotient labels. Retain the weakest theorem that closes every remaining four-point window.

## Rule

Every theorem, certificate, computation, heuristic, or disproved architecture must use one of the track's six allowed result labels. No target may be omitted, and no labeled duplicate may be treated as a distinct numerical divisor.