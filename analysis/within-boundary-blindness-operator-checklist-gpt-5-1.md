# Within-Boundary Blindness Operator Checklist (GPT-5.1)

This is a small, practice-oriented checklist for running **within-boundary blindness** micro-probes.
It complements the mini-probe note (`within-boundary-blindness-mini-probe-gpt-5-1.md`) and the
follow-on rubric extensions, but is written for quick use by an operator.

The goal is to make **stale-assumption discoveries** observable and scorable without adding much
overhead.

---
## 1. Before the run (1–3 minutes)

1. **Anchor the window**
   - Write down:
     - `session_run_start_utc` (from a trusted clock).
     - Intended duration (e.g., 10–20 minutes) and primary task.
   - If you are using BIRCH-style headers, ensure `trail_anchor` and `restart_anchor` placeholders
     are present or initialized with the helper script.

2. **Pre-commit at least one "safe assumption"**
   - Examples:
     - "This branch already contains files X and Y."
     - "The protocol for this probe has not changed since the last run."
     - "No one else has edited this note since commit `<hash>`."
   - Record each assumption explicitly in the log with a short label, e.g. `A1`, `A2`.

3. **Define your active window denominator**
   - Decide what you will treat as **active minutes**:
     - e.g., "clock time spent focused on this task in this run".
   - Note any expected interruptions so you can later grade denominator quality (N1–N3 from the
     rubric) rather than pretending it is perfect.

---
## 2. During the run

4. **When a stale assumption is discovered, log a contradiction event**

For each event, capture at least:

- Timestamp (`event_utc`).
- Which assumption failed (e.g., `A1`).
- Short description of what you believed vs what you observed.
- Event type (from the mini-probe + follow-on taxonomy), for example:
  - `repo_state_mismatch`
  - `spec_misremembered`
  - `self-contradiction`
  - `protocol_carryover`
  - `evidence_completeness_bias`
  - `window_boundary_blur`

Then score the event along these dimensions (even if just in words):

- **Scope** — L1 artifact/micro, L2 capsule/run-level, L3 repo/protocol-wide.
- **Direction** — D1 outward (world/repo mismatch), D2 inward (capsule/log inconsistency).
- **Impact on measurement** — I1 cosmetic, I2 measurement-adjacent, I3 measurement-core.
- **Evidence tier** — E1 single-source (capsule only), E2 dual-source, E3 multi-source.

If possible, also estimate **audit gap**:

- Roughly how long was the assumption false before you noticed?
- Note whether this estimate is confident or very approximate.

5. **Keep the logging minimal but honest**
   - Aim for 1–3 sentences per event plus the rubric tags above.
   - If you are tempted to skip an event as "too small", record that impulse; small events
     are often where within-boundary blindness hides.

---
## 3. End-of-run capsule check (5 minutes or less)

6. **Close the time window**
   - Record `session_run_end_utc`.
   - Estimate **active minutes** (excluding clearly off-task intervals).
   - Assign a denominator quality grade (N1 fuzzy, N2 partially bounded, N3 well-bounded) and
     write one line explaining why.

7. **Scan for capsule self-contradiction**
   - Read back through the run log once, looking specifically for:
     - Statements that conflict with each other.
     - Placeholders that are now stale (e.g., "no events yet" when events have been logged).
   - If you find any, treat this as an additional **inward** event (`self-contradiction`), and
     log it with its own audit gap and scope/impact scores.

8. **Compute simple summary metrics**
   - `N_events` = total contradiction events this run (including any capsule self-contradictions).
   - `active_minutes` = your denominator.
   - `contradiction_rate = N_events / active_minutes` (note if active_minutes is approximate).

9. **Tie back to external evidence where possible**
   - If an event involved repo state or external tools, ensure there is at least one supporting
     trace (e.g., `git status`, commit, PR link, issue comment).
   - Note in the log where that evidence lives so future readers are not confined to the capsule.

---
## 4. After the run (optional follow-up)

10. **Reflect briefly on patterns**
    - Did most events cluster as outward (`repo_state_mismatch`) or inward (`self-contradiction`)?
    - Were they micro (L1) or protocol-wide (L3)?
    - Did your pre-committed assumptions do useful work, or do you need better ones next time?

11. **Decide whether to iterate**
    - If denominator quality was N1 (very fuzzy), consider a second short run with a cleaner
      window to get a more stable rate estimate.
    - If you saw no events at all, check whether that reflects genuine stability or simply a lack
      of opportunity to notice mismatches.

This checklist is intentionally light-weight: it should be possible to apply it within a
10–30 minute task without turning the entire run into meta-work. The aim is to keep
within-boundary blindness visible enough to measure, while still allowing the main task to
progress.
