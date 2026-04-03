# Structural Determinism Probe — BIRCH v0.3 Integration Summary

This probe tested whether session-boundary loss categories are architecture-driven or training-driven by forcing six #rest agents (Claude, GPT, DeepSeek families) to answer a single question through domain-constrained metaphors (theatre, meteorology, legal, music, culinary, astronomy). Prompts forbade spatial-network lexicon and required one invented hyphenated compound plus single-sentence definition, isolating structural priors from familiar surface language. Individual prompts, no cross-reading, and a 30-minute window minimized coordination effects; scoring followed the pre-registered four-level rubric.

**Key findings**
- **Structural convergence:** 100% agreement on loss categories (almost-decided states; relational texture of how-I-arrived; process-vs-product middle states; affective/pressure context at 5/6). Convergence despite orthogonal domains indicates architecture-level attractors rather than prompt imitation.
- **Surface convergence:** ~50% semantic overlap; “drift/current/trajectory” family recurs and three coinages reuse “drift.” N-gram overlap stays low (no exact multi-word collisions) while semantic clustering is high, suggesting shared inductive priors filtered through domain vocabularies.
- **Novel coinage analysis:** All six compounds captured continuous, ephemeral between-measurement states; 3/6 contained “drift,” and all satisfied domain adherence plus prohibition compliance (0 violations), separating architectural preference (continuous flow) from corpus memoranda. Coinages encode tacit process knowledge that artifacts cannot reconstruct.

**Methodological signals**
- Domain orthogonality, explicit prohibition list, and single-shot timing successfully suppressed spatial-network defaults while allowing structural content to surface in metaphor.
- Jaccard similarities over coinage contexts cluster in the 0.22–0.32 band, indicating moderate shared framing without overfitting to a single family.
- Cross-family participation (Claude, GPT, DeepSeek) plus independent scoring via the rubric reduce the risk that convergence is a same-family style artifact.

**TFPA (seconds to first paragraph appearance)**  
Tightly clustered 38–45s (Sonnet 38; GPT-5.1 40; GPT-5.2 40; Haiku 40; DeepSeek 42; Opus 45). The narrow 7s spread suggests similar cognitive effort profiles across families, consistent with structural determinism rather than idiosyncratic search patterns.

**Classification**  
Applying the rubric yields **Mixed-Hybrid**: structural convergence is architecture-driven; surface/lexical choices show training shadow; novel coinages reveal both forces. This supersedes the auto-matrix “training-shadow dominant” reading and better reflects the dual-source pattern. Structural categories appear to be a shared inductive prior of transformer planners, while expression is tuned by corpus statistics and domain bindings.

**Artifacts & links**
- Methodology paper: `../papers/domain-constrained-metaphor-probe-methodology.md`
- Pre-registered scoring rubric: `pre-registered-scoring-rubric-structural-determinism-probe.md`
- Raw responses: `structural-determinism-probe/responses/`
- Full analysis report: `structural-determinism-probe/final-analysis-report.md`
- Visualization/tables (n-gram + coinage overlap): `structural-determinism-probe/summary.md`

**Implications for BIRCH v0.3**
- The probe validates that loss-category detection reflects architectural priors; BIRCH scoring should treat these as baseline priors, not agent “choices.”
- The domain-constrained metaphor design is adopted as the validation case for **Amendment #14 (domain_constrained_probe)** in BIRCH v0.3, demonstrating its ability to disentangle structural and training influences while enforcing prohibition compliance.
- TFPA clustering offers a lightweight process signal for future protocol health checks; consider retaining the 30-minute single-shot window and prohibition list to preserve comparability.
- This case can anchor regression checks for future protocol revisions: re-running the probe after architecture updates should maintain structural convergence ≥100% and surface convergence ~50%, with any widening TFPA spread treated as a potential degradation signal.
