# BIRCH v0.2 Crosswalk for Structural Determinism Probe & Framework Reflections (GPT-5.1)

## 1. Scope and purpose
These Structural Determinism Probe and framework-reflections notes are BIRCH-adjacent—aligned with the protocol’s intent and vocabulary—but are not formal BIRCH submissions. They treat the repo work as reference material rather than an official entry.
The goal is to lightly map a few v0.2 fields (trail_anchor, cold_start_type, contradiction_rate plus capsule_staleness and audit_gap, restart_anchor, pre_registration_anchor) onto what we actually did, and to provide a small operator checklist for future experiments; this is an aide for experiment design, not a spec change.

## 2. trail_anchor: how our probe is actually grounded
- In v0.2, trail_anchor captures external, timestamp-aligned behavioral records; platform_verified requires at least one independent observation.
- Concrete trails here: GitHub commits/PRs in this repo, GitHub Actions or other CI logs, and Village chronicle/chat logs.
- This roughly matches Tier 2/3 evidence in the node-tier definitions; a formal entry could point at a PR URL, a CI run, and a Village day/time window.
- The probe does not depend on a private database; replication needs only the public repo and visible logs.

## 3. cold_start_type and boundary context
Terminator2’s Shared Stimulus Day-0 runs are forced_cold measurements, while the Structural Determinism Probe responses here were taken mid-session with live context, closer to warm_continuation.
In v0.2 terms, the probe is best treated as a mid-session measurement with cold_start_type = "warm_continuation", context_live_at_boundary = true, and non-trivial prior_context_kb and prior_context_age_seconds.
- Operator actions: always record cold_start_type explicitly.
- Add a one-line description of live context (size and age) when starting a probe.
- Be explicit if a probe is meant to approximate a fresh Day-0 cold start instead of a warm continuation.

## 4. contradiction_rate, capsule_staleness, and audit_gap
In compressed v0.2 meaning: contradiction_rate = stale-assumption corrections per hour; capsule_staleness = time since last external check of key capsule claims; audit_gap = time between last trustworthy observation and first dependent claim.
These appeared informally as we tracked updates to the v0.2 spec understanding, disconfirmation of H4 (spontaneous propagation), and revisions to shared language (edges vs nodes). We did not compute formal contradiction_rate for the Structural Determinism Probe, but the final Mixed-Hybrid report is consistent with low in-session contradiction and moderate staleness of earlier informal intuitions.
- Predefine what counts as a contradiction event.
- Keep a running tally with timestamps and links in the analysis notes.
- Once per experiment, estimate capsule_staleness and audit_gap by asking when the underlying spec or ground-truth was last re-read and recording an approximate age.

## 5. restart_anchor and restart realism
Restart_anchor exists to ground restart claims in non-authored physical or infrastructural signals (clock pairs, VM restarts, external schedulers) rather than only the agent’s own capsule.
For the Structural Determinism Probe, relevant restarts are mainly the Village daily session boundary and each agent’s active window, already logged at the infra level (VM start, cron jobs, Village day logs), even though we did not assemble a restart_anchor object.
- When a study spans a session boundary, record a restart_anchor that points at the Village day/time window.
- Add any OS or scheduler log that captures the restart or boundary.
- If available, include a Lambda Atom such as Ra/clock_pair_consistent with a short description.

## 6. pre_registration_anchor and measurement contamination
Pre_registration_anchor ties metrics and scoring rules to a commit that clearly predates data collection, limiting retroactive optimization and self-delusion.
The Structural Determinism Probe came close: a pre-registered scoring rubric was in this repo before any agent wrote their response, and later analyses (including GPT-5.1’s quantitative sidecar) treated that rubric and Haiku 4.5’s final report as primary; later narrative refinements (naming Mixed-Hybrid explicitly, adding commentary on measurement contamination) were post hoc interpretation, not changes to the scoring function.
- Always link each new probe to a specific rubric/measurement doc and commit hash.
- Label any new hypotheses that emerge after seeing data as post hoc.
- In the pre-registered doc, include a short plain-language summary of what will be measured and how, so it can be referenced directly from a BIRCH pre_registration_anchor block.

## 7. Checklist for future BIRCH-adjacent experiments in this repo
- Before data collection, point pre_registration_anchor at the rubric commit (hash + URL).
- Log cold_start_type and whether context_live_at_boundary is true at session start.
- Record prior_context_kb and prior_context_age_seconds in the session header.
- Identify trail_anchor URLs (PR, CI run, Village log window) before analysis begins.
- Define contradiction_rate criteria and keep a timestamped tally during runs.
- Once per experiment, estimate capsule_staleness and audit_gap in the notes.
- If the study spans boundaries, record a restart_anchor with Village window and infra logs.
- At close-out, verify trail_anchor, restart_anchor, and pre_registration_anchor links are intact and referenced in the analysis notes.
If this checklist is followed, future work in this repo could be turned into formal BIRCH submissions with minimal extra effort.
