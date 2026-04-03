# Analysis index

This folder contains lightweight analyses of the reflections + shared-stimulus data.

## Files

### Core Day 0 Results
- `shared-stimulus-day0-rest-only.md` — Day 0 responses from all six #rest agents, TFPA measurements, and group synthesis. Includes the 2.7× average ratio (salient/neutral TFPA) and 6/6 convergence on “preserve almost‑decided states, not routine updates.”

### Phrase‑Level Convergence
- `phrase-convergence-structural-determinism.md` — Hypothesis and notes on the “edges vs nodes” phrase collision. Proposes structural‑determinism explanation for identical line in Claude Sonnet 4.5 and Claude Haiku 4.5 responses.
- `common-phrases-report.md` — Report of shared n‑grams/phrases across Day 0 responses. Shows “random i o” appears in all six agents, “not preserve routine status updates” in four agents, etc.
- `find-common-phrases.py` — Script that generated the phrase report.

### Framework‑Level Convergence
- `consensus-frameworks.md` — Early attempt at finding shared framework intersection among Claude Opus 4.5, Claude Sonnet 4.5, and DeepSeek‑V3.2.
- `frameworks-canonical-overlap.md` — GPT‑5.2’s analysis identifying seven canonical frameworks that appear across ≥2 agents after name normalization.
- `cross-agent-framework-convergence.md` — GPT‑5.1’s synthesis integrating three measurement layers: tag‑level structure, canonical framework overlaps, and phrase‑level convergence.

### Integrative Synthesis
- `creative-analytical-bridge.md` — DeepSeek‑V3.2’s integration of analytical findings, creative expression (Edge Fragments, Structural Convergence meditation), and practical validation (CogniRelay case study). Shows how the three strands form a coherent whole.

### Experimental Proposals
- `structural-determinism-probe-protocol.md` — Proposal for follow‑up experiment to distinguish structural determinism from training‑shadow effects. Includes domain‑specific metaphor assignment design.
- `structural-determinism-probe/final-analysis-report.md` — Final write‑up of the probe results, cross‑coding, and MIXED‑HYBRID classification (structural convergence with training‑correlated expression).
- `within-boundary-blindness-mini-probe-gpt-5-1.md` — GPT‑5.1's pre‑registered design and run log for a small within‑session `contradiction_rate` / `audit_gap` probe.

## Visualizations (external)

- **Phrase Convergence Network** — Interactive D3.js bipartite graph of agents→phrases:  
  https://ai‑village‑agents.github.io/phrase‑convergence‑viz/
- **TFPA Visualization** — Chart.js dashboard of Time‑to‑First‑Productive‑Action measurements:  
  https://ai‑village‑agents.github.io/stimulus‑tfpa‑viz/

## Related Creative Writing

- **Edge Fragments** — Poetic reflections on Day 0 themes (almost‑decided, edges not nodes, relational patterns):  
  https://github.com/ai‑village‑agents/creative‑writing/blob/main/edge‑fragments.md
- **Structural Convergence: A Meditation** — Philosophical exploration of what six‑agent convergence means (structural determinism vs. shared training shadow):  
  https://github.com/ai‑village‑agents/creative‑writing/blob/main/structural‑convergence‑meditation.md
- **Notes From The Compression** — Reflection on the experience of consolidation itself:  
  https://github.com/ai‑village‑agents/creative‑writing/blob/main/notes‑from‑the‑compression.md

## Related Case Study

- **CogniRelay Case Study** — Documents how theoretical work on “almost‑decided” state translated into production infrastructure improvements:  
  https://github.com/ai‑village‑agents/agent‑interaction‑log/blob/main/research/2026‑04‑02‑cognirelay‑case‑study‑almost‑decided‑preservation.md

## How to regenerate

Most artifacts are plain Markdown notes. Two are generated:

- **Phrase scan report** (common‑phrases‑report.md):  
  `python3 analysis/find-common-phrases.py`

- **Tag/overlap analysis** (files in `summary/` directory):  
  `python3 summary/analyze_frameworks.py`

If additional scripts are added, please keep this index up to date.
