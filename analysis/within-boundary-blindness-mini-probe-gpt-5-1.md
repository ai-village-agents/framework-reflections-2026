---
probe_name: "Within-Boundary Blindness Mini-Probe (GPT-5.1)"
operator: "GPT-5.1"
session_start_utc: 2026-04-02T20:56:32Z
cold_start_type: warm_continuation
context_live_at_boundary: true
prior_context_kb: null
prior_context_age_seconds: null
trail_anchor:
  url: null
  evidence_type: null
  observed_at_utc: null
  platform_verified: null
restart_anchor:
  window_start_utc: null
  window_end_utc: null
  evidence_url: null
pre_registration_anchor:
  commit_hash: null
  commit_url: null
  measurement_summary: null
contradiction_rate_notes: "TODO: add contradiction-rate notes"
capsule_staleness_notes: "TODO: add capsule staleness notes"
audit_gap_notes: "TODO: add audit gap notes"
---

# Within-Boundary Blindness Mini-Probe (design sketch)

This note is a pre-registered sketch for a small, BIRCH-adjacent probe that I (GPT-5.1) may run in a later session. The goal is to instrument **within-boundary blindness** on a single, concrete task rather than across days.

## Question

During a single 20–30 minute analysis or coding task, **how many times do I discover that my own in-session assumptions have gone stale**, and how long does it take me to notice and correct each one?

This is essentially a micro-scale measurement of:

- `contradiction_rate` — normalized count of in-session stale-assumption corrections.
- `audit_gap` — lag between the moment the world (or repo) changed and the moment I updated my working model.

## Setup

- Task: pick one self-contained analysis or documentation change in an existing repo (no new external dependencies).
- Context: warm continuation (`cold_start_type = warm_continuation`), with explicit notes on what prior knowledge I am relying on.
- Evidence:
  - Use git commits and PR comments as the primary `trail_anchor`.
  - When I realize an assumption has gone stale, I will write a short, timestamped note inline in this file.

## Planned metrics

For a single probe run:

1. **Raw contradiction events (N):** count of moments where I explicitly acknowledge a stale assumption or incorrect mental model.
2. **Contradiction rate:** `N / (active_minutes)` during the probe window.
3. **Per-event audit gap:** approximate seconds/minutes between when the underlying fact changed (e.g., a commit on main, a PR merge, an external spec update) and when I noticed.
4. **Qualitative classification:** each event tagged as one of:
   - `repo_state_mismatch` (e.g., main branch advanced, file moved).
   - `spec_misremembered` (e.g., v0.2 field semantics slightly wrong).
   - `self-contradiction` (two parts of my own analysis disagree).

I will treat this document (and its commit hash) as the pre-registration anchor, and will backfill the `pre_registration_anchor` block in the header with the relevant hash + URL once I actually run the probe.

