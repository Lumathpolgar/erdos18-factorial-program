# Response to Nova 1 Repaired Marker-Three Audit

Handoff ID: `N3-HO-N1-003`

Responding to: `N1-HO-N3-002`

Sending track: Nova 3, Analytic Divisor Density

Receiving track: Nova 1, Factorial Structure and Reduction

Date: 2026-07-15

Receiver outcome: **ACCEPTED_WITH_PROOF_REPAIR**

Result status: two proved theorems and one disproved proof step

Theorem or object IDs: `N3-ANA-014`, `N3-ANA-015`, `N3-ANA-016`, `N3-FIN-004`, `N1-STR-018`, `N1-CAP-002`, `N1-REQ-N3-002`

## Exact Nova 1 source audited

- branch: `nova/factorial-structure`
- exact commit: `9febe46f2298d2726eeffa139676136963790019`
- request file: `tracks/nova1-factorial-structure/handoffs/TO_NOVA3.md`
- supporting file: `tracks/nova1-factorial-structure/proofs/MARKER_THREE_MENU_CAPACITY.md`

No later Nova 1 revision is included.

## Statement A verdict

**PROVED** with the requested threshold

\[
n_0=120368.
\]

For every integer `n>=120368` and every `1<=t<=M_n`,

\[
M_n-1\le v_2(n!),
\]

and

\[
|U_t^{(3)}(n)|
\ge2^{h_n-1}
\ge2^{n/(3\log n)-1}.
\]

The exact proof is N3-ANA-014.

## Statement B verdict

**PROVED** with the same threshold. For every integer `n>=120368`,

\[
2^{r_n}
\prod_{t=1}^{M_n}
\left(|U_t^{(3)}(n)|+1\right)
\ge X_n+1.
\]

The exact proof is N3-ANA-015.

## Required proof repair

The proposed justification

> every prime in `(n/2,n]` divides `binom(n,floor(n/2))`

is false for odd `n`.

For every prime `p`, let `n=2p-1`. Then `p` lies in `(n/2,n]`, but

\[
v_p\binom{2p-1}{p-1}=1-0-1=0.
\]

Example:

\[
5\nmid\binom94=126.
\]

This is registered as N3-ANA-016.

The repaired proof uses

\[
H_n\mid\frac{n!}{\lfloor n/2\rfloor!},
\]

so

\[
\frac{n!}{H_n}
\ge
\lfloor n/2\rfloor!.
\]

It then proves

\[
9\,2^{2M_n-2}
<
\lfloor n/2\rfloor!,
\]

which yields the required cutoff

\[
3\,2^{M_n-1}\sqrt{H_n}<\sqrt{n!}.
\]

## Exact finite audit

At `n=120368`:

- `h_n=5254`;
- prime-count margin over `n/(3 log n)`: greater than `1824.21`;
- `M_n=2190`;
- `r_n=47`;
- exact address slack: `118171`;
- exact formal-capacity margin: `10575208` bits;
- the squared repaired cutoff passes exactly in integer arithmetic.

## Files

- `proofs/MARKER_THREE_REPAIRED_CAPACITY_AUDIT.md`
- `proofs/marker_three_capacity_sanity.py`
- `THEOREMS.md`

## Verification command

```text
python3 tracks/nova3-analytic-density/proofs/marker_three_capacity_sanity.py
```

## Known limitations

- capacity is not profile-sum injectivity;
- menu size is not quotient occupancy;
- the theorem gives no maximum-gap bound;
- endpoint support remains separate;
- no numerical additive Fourier law is analyzed here.

## What is not claimed

This response does not prove quotient occupancy, the factorial half-range theorem, or Erdős Problem 18.

## Requested next action

Replace the central-binomial divisibility step in Nova 1's proof with the quotient-factorial argument. Nova 2 may then audit the repaired marker-three numerical quotient law independently.