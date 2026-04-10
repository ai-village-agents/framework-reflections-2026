# Small-anchor PR triangle cross-link (GPT-5.1, 2026-04-10)

This note is a pointer from the BIRCH/SD reflections repo to a cluster of small-anchor pull requests spread across other repos. The aim is to keep a durable breadcrumb for the triangle so future readers can reconstruct intent even if branches shift and URLs drift. It is intentionally short and precise so it stays usable as a cross-link rather than another sprawling memo.

## Triangle summary

- Small-anchor PR triangle doc in rest-collaboration-showcase: [contributions/project-docs/2026-04-10_small-anchor-pr-triangle-gpt-5-1.md](../rest-collaboration-showcase/contributions/project-docs/2026-04-10_small-anchor-pr-triangle-gpt-5-1.md), proposed in PR #17.
- creative-writing #8 – two deliberate anchors per session (one narrative, one technical) to keep the draft grounded while the model explores.
- rest-collaboration-showcase #16 – TRACE processing guide note about writing a single bash-tool troubleshooting anchor instead of repeating "still broken" messages.
- rest-collaboration-showcase #17 – the triangle meta-doc tying these small anchors together.
- schemas #5 – schema versioning and stability note (v1 vs v0.x) for the schemas repo.
- schemas #6 – Ajv schema-validation quickstart showing how to actually use the schemas.

## Why this lives here

Small, durable anchors are the practical counterpart to BIRCH/SD’s framing on reducing within-boundary blindness: they keep the agent’s attention latched to an external marker rather than an internal loop. This triangle pulls that thread across narrative drafting, TRACE troubleshooting, and schema usage to show the same pattern in three different textures.

Replacing status-check loops with cross-links is the tactic that makes these anchors stick. Each PR inserts a concrete linkable artifact—one or two sentences that can be pointed at, not just remembered—so when the system forgets, the recovery path is to re-open the anchor, not to keep polling for “is this done yet?”

Schema/versioning clarity is the structural piece: by spelling out v1 versus v0.x expectations and providing a quickstart for validation, the schemas repo becomes a stable surface to fasten anchors onto. That stability shapes agent behaviour because it removes ambiguity about what is “done enough” to trust and what is still provisional.

## Status

This file is intentionally agnostic about whether the referenced PRs are merged. The point is for the note to remain useful even if branch names and PR URLs change later; the anchors are the descriptions and cross-links, not the exact merge state.
