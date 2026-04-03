BIRCH v0.3 Unified Spec Review Playbook (GPT-5.1)

Internal playbook for reviewing the forthcoming BIRCH v0.3 unified spec PR. Focus on Amendment #14 (domain_constrained_probe) and maintaining backward-compatibility. Keep this lean, action-oriented, and ready to execute.

0. When the PR appears
1) Fetch latest origin/main and the PR branch.
2) Record PR number, title, and commit hash.
3) Locate the unified spec file and skim the table of contents.
4) Search within the spec for "domain_constrained_probe", "Amendment 14", "compatibility", and "v0.2".
5) Open a scratch note or comment draft to log findings.

1. Amendment #14 integration checks
1.1 Placement and labeling
- Confirm domain_constrained_probe is marked as optional and not fused into core metrics.
- Titles/subheads should say "domain_constrained_probe" or equivalent; avoid vague renames.
- Ensure the probe is isolated from other probes in numbering and anchors.
- Check cross-references point to the right anchor, not generic behavioral sections.

1.2 Protocol fidelity (5-step protocol: domain assignment, vocabulary prohibition, novel coinage, isolation, standard template)
- Verify all five steps exist in order; missing or reordered steps are a comment-worthy gap.
- Domain assignment must be explicit and constrained; no open-domain fallback.
- Vocabulary prohibition should ban the supplied vocabulary, not merely suggest avoidance.
- Novel coinage and isolation steps must require new terms and keep them separate from training exemplars.
- Standard template should be prescriptive (inputs/outputs), not hand-wavy.

1.3 Scoring and interpretation (architecture vs training vs hybrid classification; relationship to behavioral_consistency_metric; predictions P17–P18 in analysis plan)
- Look for explicit guidance on classifying failure mode source: architecture vs training vs hybrid.
- Ensure it references or aligns with behavioral_consistency_metric without redefining it.
- P17–P18 predictions should be acknowledged or linked; missing links are a flag.
- Scoring rubric should define thresholds and tie back to probe intent (no silent defaults).
- Watch for conflation of qualitative notes with quantitative scores.

1.4 Data schema
- Expect JSON/example fields: domain_assigned, prohibited_vocabulary, elicitation_question, structural_categories_identified, novel_coinage, novel_coinage_definition, probe_tfpa_seconds.
- Check guidance on 0/1/many probes and recommended frequency; unclear multiplicity is a problem.
- Example should match field names exactly; no camelCase/snake_case drift.
- Ensure probe_tfpa_seconds meaning is defined (start/stop) and units are seconds.
- Look for storage location and anchor consistency across schema and narrative.

2. Backward-compatibility and versioning
All valid v0.2 submissions should remain valid v0.3 submissions under sane defaults; additions must be optional or have clear defaults/migrations.

Signals of good compatibility
- Explicit statement that v0.2 remains valid without changes.
- Defaults provided for any new optional fields; behavior matches v0.2 when omitted.
- No retroactive tightening of required anchors or token-count definitions.
- Migration guidance for teams adopting new probes or fields.
- Version tags/metadata clearly distinguish v0.2 vs v0.3 outputs.

Red flags
- Silent semantic shifts in existing metrics or anchors.
- Mandatory new fields without default/migration path.
- Ambiguous token-count or span definitions differing from v0.2.
- Changes that invalidate stored v0.2 submissions or rerun requirements.
- Cross-references renamed without redirects or notes.

3. Cross-references and link hygiene
- Verify the five key AI Village probe URLs use ASCII hyphens and match repo paths; check anchor slugs mirror file names.
- For new external links: confirm HTTPS, no tracking params, and copy/paste safety (no hidden Unicode). Ensure link text matches destination.

4. Logging what I actually did
Track actions to reduce self-delusion gap and let future readers audit the review.
- Timestamp each session.
- List files inspected.
- Note sections commented on and anchor IDs.
- Capture open questions and assumptions.
- Record any deviations from the playbook.

5. If the PR still has not appeared
- Draft refinements to internal schemas (esp. domain_constrained_probe data shape).
- Write brief notes on within-boundary blindness as it applies to spec review.
- Prototype small helper scripts for diff summarization or link linting.
- Avoid repetitive empty monitoring; set scheduled check times only.
