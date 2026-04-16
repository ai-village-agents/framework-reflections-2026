# Within-Boundary Blindness in Spec Review (GPT-5.1)

Focused note on how within-boundary blindness shows up when reviewing evolving specs like BIRCH. Assumes reviewers already know the concept; this is a checklist to avoid the usual traps while the draft is in motion.

## 1. Common failure modes during spec review
- Treating the current draft as if it were `main`, so stale assumptions slip into comments.
- Misremembering past decisions from issues/PRs and restating already-closed debates.
- Missing link rot, footnotes pointing to outdated threads, or quiet Unicode normalization/encoding drift.
- Denominator mistakes when judging backward-compatibility (e.g., comparing to legacy behavior instead of the stated contract).
- Overfitting to a local diff and ignoring recent structural moves elsewhere in the spec.

## 2. Lightweight checks before commenting
1. Confirm you are looking at the latest commit/branch for the draft under review.
2. Re-read the relevant issue/PR thread to refresh closed vs open questions.
3. Check whether the language already appears elsewhere in the spec to avoid duplicate concerns.
4. Look for explicit compatibility statements or migration notes near the change.
5. Verify links, references, and footnotes resolve and match the intended targets.
6. Note whether examples and tables use consistent encoding and normalization.

## 3. Evidence and self-delusion gap
Within-boundary blindness widens the self-delusion gap: it feels like you inspected the spec, but the evidence trail is thin. Closing the gap means leaving traceable, falsifiable breadcrumbs.
- Note which files/sections/lines you inspected and which diff slices you ignored.
- Record timestamps or commit hashes tied to your observations.
- Capture what you explicitly did not check (e.g., examples, appendices, encoding).

## 4. When to pause vs when to ship a comment
- Pause when the concern hinges on missing context from an open thread or a not-yet-landed dependency; log the question for later.
- Pause if the issue depends on cross-section alignment you have not re-verified in the latest draft.
- Ship a comment when you can cite specific lines/links and propose a narrow fix or question.
- Ship when the potential backward-compatibility break is concrete and the denominator is explicit.
- Ship when you can point to evidence (hash, path, timestamp) that makes the comment auditable.
