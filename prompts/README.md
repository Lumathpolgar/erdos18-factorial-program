# Four-Nova Production Launch Prompts

## Use these prompts

The earlier `prompts/*_START.md` files are superseded. Do not launch the Novas from those files.

Use the full production prompts under `prompts/production/`.

## Shared mode

Use the same mode for all four conversations:

`Mode: Math`

The mode is only the reasoning mode. The actual repository, branch, scope, phases, deliverables, Git workflow, and first checkpoint are fully specified inside each production prompt.

## Repository

- Repository: `Lumathpolgar/erdos18-factorial-program`
- URL: `https://github.com/Lumathpolgar/erdos18-factorial-program`
- Base branch: `main`

## Prompt assignment

### Nova 1: Factorial Structure and Reduction

Paste the complete contents of:

`prompts/production/NOVA1_PRODUCTION_PROMPT.md`

Working branch:

`nova/factorial-structure`

Nova 1 must reconstruct the baseline, build the factorial divisor atlas, develop two complete structural candidates, choose a preferred route, issue exact theorem requests to the other tracks, commit, push, and open a draft PR.

### Nova 2: Additive Occupancy and Global Sumsets

Paste the complete contents of:

`prompts/production/NOVA2_PRODUCTION_PROMPT.md`

Working branch:

`nova/additive-occupancy`

Nova 2 must reconstruct the additive no-go results, formalize four occupancy models, prove or disprove independent toy theorems, select a preferred global route, freeze a candidate occupancy theorem, commit, push, and open a draft PR.

### Nova 3: Analytic Divisor Density

Paste the complete contents of:

`prompts/production/NOVA3_PRODUCTION_PROMPT.md`

Working branch:

`nova/analytic-density`

Nova 3 must reconstruct the analytic baseline, build the factorial divisor scale map, validate primary sources line by line, formulate three exact candidate analytic theorems, prove, weaken, or obstruct the best route, commit, push, and open a draft PR.

### Nova 4: Computation, Falsification, and Verification

Paste the complete contents of:

`prompts/production/NOVA4_PRODUCTION_PROMPT.md`

Working branch:

`nova/computational-verification`

Nova 4 must build the exact verification core, corrupted-certificate tests, two independent search or bound methods, the initial exact dataset, the cross-track request queue, commit, push, and open a draft PR.

## Launch procedure

1. Start four separate Nova conversations.
2. Set each conversation to `Mode: Math`.
3. Paste one complete production prompt into each conversation.
4. Do not shorten, summarize, combine, or paraphrase the prompt.
5. Give each Nova access to GitHub.
6. Let each Nova work only on its assigned branch.
7. Require each Nova to report the pushed commit SHA and draft PR after its first substantive checkpoint.

## Shared target

All four tracks support the same open objective:

\[
h(n!) < (\log n)^{O(1)}.
\]

The current sufficient local target is:

\[
H_{n!}\!\left(\lfloor\sqrt{n!}\rfloor+1\right)=O((\log n)^2).
\]

The problem is not solved. No Nova may promote a conditional theorem, finite certificate, computation, heuristic, or partial route into a solution claim.