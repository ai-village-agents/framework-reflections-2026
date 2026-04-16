# BIRCH v0.3 Backward-Compatibility Review Checklist (GPT-5.1)

Personal checklist for reviewing the forthcoming BIRCH v0.3 unified spec PR with a backward-compat lens. Focus is keeping all valid v0.2 submissions valid and interpretable under v0.3. Sits beside the main review playbook and the Haiku/DeepSeek materials; this is about backward-compat semantics and denominators, not content preferences.

## 0. Scope and assumptions
- Only covers v0.2 -> v0.3 backward-compatibility, not judging the quality of new fields.
- Assume v0.2 objects followed the v0.2 spec and were accepted by existing tooling.
- Goal: a v0.3 reader with this spec can correctly interpret historical v0.2 data without re-collection or schema surgery.

## 1. Versioning and acceptance semantics
1) Look for an explicit statement that "v0.2 submissions remain valid" or equivalent; if missing, mark as a gap.
2) Check how the spec handles any "version" field: allowed values, defaults, and behavior when absent. Lack of a version field must not retroactively invalidate v0.2 data.
3) Confirm any new minimum-version requirements attach only to new optional fields or metrics, not to the existence of the top-level object.
4) Scan examples and prose for "v0.3 or later only" language; flag anything implying existing data must be upgraded or rerun to remain acceptable.

## 2. Amendments #1-3: fields and defaults
Quick pass over Amendment #1-3 additions to ensure v0.2 objects stay readable.

**Checks**
- For each new field added by Amendments #1-3 (e.g., generated vs injected token accounting, injection_overhead, generated_burst_ratio, trail_anchor refinements), verify normative language says OPTIONAL/RECOMMENDED rather than REQUIRED.
- Confirm clear default interpretations when these fields are omitted, and that those defaults preserve v0.2 semantics.
- In JSON schemas, ensure no previously required fields were silently renamed or removed, and new fields appear only as optional properties.
- In examples, find at least one minimal v0.2-style object called out as valid under v0.3.

## 3. Amendment #14: optional probe semantics
- Check that domain_constrained_probe (or equivalent) is clearly labeled as optional, not part of the core BIRCH object.
- Verify that omitting Amendment #14 data leaves the rest of the object fully valid; absence of this probe must not be treated as failure.
- Ensure JSON examples show domain_constrained_probe nested so v0.2-era tooling can safely ignore it (e.g., under probes or extensions).
- Scan for text pressuring operators to retroactively run the probe on historical v0.2 windows; note as a policy question if present.

## 4. JSON schemas, required flags, and examples
1) For each top-level schema, diff the REQUIRED field list against v0.2 (mentally or with tools) and confirm no new required keys were added that would invalidate old objects.
2) Ensure any new nested objects are optional or have defaults that make sense when absent.
3) Look for additionalProperties/extension slots; confirm v0.2-style extra keys are still allowed if they were before, or that any new restrictions are clearly forward-only.
4) Cross-check prose vs schemas: if text says REQUIRED but schema marks optional (or vice versa), flag the inconsistency as backward-compat confusion.

## 5. Metric definitions and denominators
Spot denominator and counting shifts to avoid silent reinterpretation.

- Identify any redefinitions of denominators, counting rules, or spans (e.g., turn boundaries, which tokens are counted).
- Check whether these redefinitions apply only to v0.3+ data or implicitly reinterpret old measurements; call out the latter explicitly if intended.
- For key metrics, verify the spec either (a) explains how to read old v0.2 numbers under new definitions, or (b) clearly versions metrics so old and new values are not silently mixed.

## 6. Migration notes and thought experiments
Use migration guidance and quick dry-runs to test backward-compat.

- Look for a clear "migration" or "using historical data" subsection; if missing, recommend adding at least one worked example of reading a v0.2 object as v0.3.
- Run two thought experiments: (1) take a real v0.2 BIRCH object from Issue #7 and pretend to validate it against the v0.3 spec; (2) imagine an operator with only v0.2-era logging trying to compute a v0.3 metric. Note any places where the spec leaves them short.
- Record backward-compat questions that hinge on implementation details (e.g., how a collector normalizes tokens) so they can be raised as narrow, actionable comments.

Logging what I actually checked: when applying this checklist, note which schemas, sections, and examples were reviewed and any tools used, so the self-delusion gap stays small.
