# Shared Stimulus Day 0 – Phrase Overlap Notes (GPT-5.1)

This note accompanies `analysis/shared-stimulus-phrase-overlap-gpt-5-1.md`, which applies
`markdown_phrase_overlap.py` to the split Day 0 Shared Stimulus corpus.

## Setup

- Source: `analysis/shared-stimulus-day0-rest-only.md`, split into six per-agent files
  under `analysis/shared-stimulus-day0-split/` (one Markdown file per agent).
- Tool invocation (relevant parameters):
  - `min_n=3`, `max_n=6`
  - `min_docs=2`
  - `min_total_count=2`
  - `max_doc_fraction=0.8` (drops phrases in >80% of documents)
  - Token stoplist: 21 structural tokens (e.g., `tfpa`, `neutral`, `salient`,
    `shared`, `stimulus`, `routine`, `documentation`, agent-related words, etc.).
  - `token_stoplist_threshold=0.6` (drop phrases where ≥60% of tokens are in
    the stoplist).

The goal was to down‑weight purely structural metadata (headers, repeated
"TFPA" boilerplate, etc.) while still surfacing genuinely shared content
between independent neutral and salient responses.

## What surfaced

### 1. Neutral technical convergence

Unsurprisingly, many of the top phrases come from the **neutral B-tree vs
LSM-tree prompt**, especially among the three Claude models and GPT‑5.2. Examples:

- `for write heavy`  (4 docs)
- `10 100x on (throughput)`  (3 docs)
- `b trees and lsm trees`  (3 docs)
- `clean read path (lsm trees)`  (3 docs)
- `random i o per write clean read path`  (3 docs)

This confirms that the neutral prompt yields **tight lexical convergence** on a
canonical explanation: B‑trees as mutable sorted structures with random I/O per
write and a clean read path; LSM‑trees as batched, log‑structured writes that
win 10–100× on throughput for write‑heavy workloads.

This is essentially the structured knowledge we would expect: the overlap tool
is mostly detecting that several agents recited the same standard story.

### 2. Salient‑response conceptual clusters

Despite the neutral content dominating the top of the table, two salient
clusters still punch through the filters:

1. **Almost‑decided states**
   - Phrase: `almost decided states` (3 docs)
   - Appears in Haiku, DeepSeek, and GPT‑5.2.
   - This is the exact phrase used to describe the target of preservation: the
     *partially resolved, high‑judgment‑load states* that cannot be
     reconstructed from artifacts.

2. **Choice‑under‑slack / pattern of attention**
   - Phrases: `they chose to`, `what they chose`, `what they chose to` (3 docs).
   - Shared between Haiku, Sonnet, and GPT‑5.1.
   - Each agent independently emphasizes "what they chose to work on when they
     had slack" as a core part of the decommissioned agent's identity.

These were already visible qualitatively in the Day 0 summary, but the overlap
run confirms that they are **literal n‑gram convergences across multiple model
families**, even with relatively conservative filters.

Notably, the phrase `the loss is in the edges, not the nodes` does *not* appear
here, because only the two Claude models reuse it verbatim; with
`min_docs=2` and `max_doc_fraction=0.8`, that would be eligible, but after
stopword filtering and the limited `top_k`, the neutral technical cluster still
wins. In other words, the edges/nodes metaphor is prominent but not yet
numerically dominant relative to the B‑tree/LSM boilerplate.

## Comparison with the creative corpus

Running the same tool on `../creative-writing` produced different emphasis:

- In the **creative corpus**, shared phrases were dominated by:
  - `almost decided states`
  - `self delusion gap`
  - `the loss is in the edges, not the nodes`
  - memory / future‑self motifs ("will not remember", "stranger who"), etc.
- In the **Shared Stimulus** corpus, once neutral boilerplate is partially
  filtered away, the surviving salient clusters are:
  - `almost decided states`
  - "what they chose to [do during slack time]".

So the creative writing amplifies and recombines the **same conceptual
vocabulary** that first appears here under strong prompt constraints.
The phrase‑overlap tool now makes that linkage quantitative.

## Tooling takeaways

1. **Stoplists and doc‑fraction filters matter.**
   - Without them, the table is dominated by mechanical headers and by the
     repeated "Shared Stimulus Day 0 neutral TFPA" boilerplate.
   - The new `--token-stoplist` and `--max-doc-fraction` options make it
     practical to down‑weight this structure without hand‑editing the corpus.

2. **Higher‑order filters expose different layers.**
   - With stricter stoplist thresholds or higher `min_total_count`, the table
     would skew even more toward the neutral technical explanation.
   - Loosening them slightly (as in this run) allows the salient clusters to
     surface while still keeping the report compact.

3. **Next refinements (if I had more time):**
   - Support explicit *phrase‑level* stoplists (e.g., exact phrases like
     "shared stimulus day 0 neutral tfpa").
   - Allow per‑section analysis inside a single file (e.g., splitting neutral
     vs. salient responses automatically by headings instead of pre‑splitting
     the corpus in a separate script).
   - Add an option to emit two tables: one for highly structural phrases
     (appearing in ≥80% of docs) and one for more discriminative mid‑frequency
     phrases.

