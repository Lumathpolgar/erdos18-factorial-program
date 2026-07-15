# Four-Nova Launch Prompts

## Shared mode

Use the same mode for all four sessions:

`Mode: Math`

Do not use different modes across the four Novas. The division of labor is already encoded in the separate prompts.

## Prompt assignment

### Nova 1

Use:

`prompts/NOVA1_FACTORIAL_STRUCTURE_START.md`

Branch:

`nova/factorial-structure`

Primary responsibility: factorial divisor structure, deterministic constructions, correction architecture, and exact reductions.

### Nova 2

Use:

`prompts/NOVA2_ADDITIVE_OCCUPANCY_START.md`

Branch:

`nova/additive-occupancy`

Primary responsibility: global sumset occupancy, convolution, Fourier and local-limit mechanisms, anti-concentration, and correction-window coverage.

### Nova 3

Use:

`prompts/NOVA3_ANALYTIC_DENSITY_START.md`

Branch:

`nova/analytic-density`

Primary responsibility: factorial-divisor counting and distribution, entropy, saddle points, local density, characteristic functions, and source validation.

### Nova 4

Use:

`prompts/NOVA4_COMPUTATIONAL_VERIFICATION_START.md`

Branch:

`nova/computational-verification`

Primary responsibility: exact computation, certificate verification, counterexample search, reproducible datasets, and independent theorem audits.

## How to launch

Start four separate Nova conversations.

Paste one complete prompt into each conversation without combining or shortening it. The prompt itself contains the repository, branch, read order, research target, deliverables, progress cycle, and GitHub rules.

Each Nova must:

1. work only on its assigned branch;
2. commit and push meaningful progress;
3. maintain a draft pull request for visibility;
4. update its branch status and theorem registries;
5. label every claim by evidence class;
6. never merge or claim the full problem is solved without passing the integration gates.

## Shared target

All four tracks support the same open objective:

\[
h(n!) < (\log n)^{O(1)}.
\]

The current sufficient local target is:

\[
H_{n!}\!\left(\lfloor\sqrt{n!}\rfloor+1\right)=O((\log n)^2).
\]

The four Novas are not four votes on one argument. They are four distinct research functions whose results must be integrated and independently audited.