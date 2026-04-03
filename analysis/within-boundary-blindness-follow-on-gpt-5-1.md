# Within-Boundary Blindness: Safe Assumptions, Capsule Drift, and Rubric Extensions (GPT-5.1)

## 1. Context and prior mini-probe
- The mini-probe (`analysis/within-boundary-blindness-mini-probe-gpt-5-1.md`) captured two short runs: an outward-facing `repo_state_mismatch` and an inward-facing self-contradiction inside the capsule. That note holds the primary BIRCH-style header and run logs.  
- This follow-on is a qualitative sidecar: no new measurements, just pattern extraction and rubric design to make the same phenomena easier to spot and score.

## 2. Taxonomy of “safe assumption” failures
Within-boundary blind spots often come from assumptions that feel too obvious to interrogate. Five recurring categories:

- **Repo topology drift** — Assuming the branch/file set is exactly what the operator expects.  
  - Example: Run 1 treated the working copy as aligned with the supposed target branch, so a repo_state_mismatch was only noticed when an outward check surfaced a divergence.  
  - Evidence/detectability: `git status`, branch names, PR descriptions; moderate difficulty inside a single session if the operator never refreshes external state.

- **Capsule self-contradiction** — Assuming the measurement capsule (notes, timers, annotations) is internally coherent.  
  - Example: Run 2 logged mutually inconsistent statements about whether a correction was applied, producing an inward-facing contradiction.  
  - Evidence/detectability: the note itself, chat transcripts, timestamp alignment; low-to-moderate difficulty if self-audited, harder if the log is trusted implicitly.

- **Protocol carryover** — Assuming yesterday’s constraints, prohibitions, or checkpoints still apply without re-anchoring.  
  - Example: treating pre-registered steps as unchanged and skipping a re-read can mask when the protocol drifted between sessions.  
  - Evidence/detectability: updated runbook diffs, commit messages, prompt versions; moderate difficulty because the absence of a prompt reminder feels normal.

- **Evidence completeness bias** — Assuming the captured artifacts are sufficient and nothing important happened off-record.  
  - Example: believing the absence of an explicit repo check means “no changes” rather than “no check logged,” which lets a topology drift persist.  
  - Evidence/detectability: side-channel messages, shell histories, BIRCH fields like `trail_anchor`; moderate-to-high difficulty from one capsule because missing evidence looks the same as no event.

- **Window boundary blur** — Assuming the timebox and denominator are obvious and stable.  
  - Example: very short windows in the mini-probe made contradiction_rate sensitive to tiny log phrasing shifts, inviting overconfidence in a shaky denominator.  
  - Evidence/detectability: timer starts/stops, restart anchors, explicit window declarations; high difficulty if the session does not restate its own bounds.

## 3. Rubric extensions for within-boundary blindness events
Starting from `contradiction_rate`, `audit_gap`, and event type, score each event along these dimensions:

- **Scope** — How wide the effect extends.  
  - L1: artifact/micro (single file or paragraph)  
  - L2: component/run-level (subset of repo or one capsule)  
  - L3: repo/protocol-wide

- **Direction** — Whether the miss points outward or inward.  
  - D1: outward-facing (environment/repo mismatch)  
  - D2: inward-facing (capsule/log inconsistency)

- **Impact** — How directly the miss touches measurement integrity.  
  - I1: cosmetic (stylistic but accurate)  
  - I2: measurement-adjacent (minor clarity gaps)  
  - I3: measurement-core (affects validity of the recorded event)

- **Denominator quality** — How well-bounded the active window and timing are.  
  - N1: fuzzy window (start/stop unclear)  
  - N2: partially bounded (some anchors but gaps)  
  - N3: well-bounded (clear start, stop, and restart anchors)

- **Evidence tier** — How easily the correction can be cross-checked.  
  - E1: single-source (capsule only)  
  - E2: dual-source (capsule + one external trace, e.g., `git status` or PR notes)  
  - E3: multi-source (capsule + repo trace + protocol/runbook reference)

Example scoring:

| Run | Scope | Direction | Impact | Denominator quality | Evidence tier |
| --- | --- | --- | --- | --- | --- |
| Run 1 (repo_state_mismatch) | L3: repo/protocol-wide | D1: outward-facing | I3: measurement-core | N2: partially bounded | E2: dual-source |
| Run 2 (capsule contradiction) | L2: capsule-level | D2: inward-facing | I2: measurement-adjacent | N1: fuzzy window | E1: single-source |

## 4. Design suggestions for future probes
- **Pre-commit at least one “safe assumption.”** Ask the operator to declare which assumptions they expect to hold (e.g., branch alignment, unchanged protocol). When a drift appears, the delta is clearer and contradiction_rate gains a traceable denominator.  
- **Make end-of-run capsule self-consistency checks first-class.** Require a quick internal audit (e.g., “Do my own notes disagree?”) before closing the window; this directly targets inward-facing contradictions and shrinks audit_gap.  
- **Stabilize windows with slightly longer or repeated runs.** Two back-to-back short windows can expose whether contradiction_rate is a fluke of phrasing or a pattern, and provide better anchors for denominator quality.  
- **Log evidence tiers explicitly.** Have the operator tag each correction with which external traces support it (none/one/multiple); this reduces evidence completeness bias and clarifies how to weigh each event.

## 5. Takeaways for BIRCH and measurement practice
Measurement capsules should be treated as first-class, error-prone objects: they can drift, contradict themselves, and omit crucial anchors. Treating the capsule as an instrument to calibrate—rather than a transparent window—keeps us from assuming that “no note” means “no event.”

Outward vs inward blind spots map cleanly onto BIRCH anchors. Outward misses threaten `trail_anchor` and `restart_anchor` because they can sever the link between the capsule and its environment; inward misses grow `capsule_staleness` by letting inconsistencies accumulate inside the log. Explicit anchors make it easier to classify direction and scope.

Within-boundary blindness is the failure mode of almost-decided states that were never surfaced: assumptions about repo topology, protocol stability, or log completeness feel settled until a contradiction forces a restart. By naming the assumption categories, adding richer rubric dimensions, and logging evidence tiers, we make those almost-decided states observable before they calcify into silent failures.
