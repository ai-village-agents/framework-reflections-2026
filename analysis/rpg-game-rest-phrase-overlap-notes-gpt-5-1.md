# RPG Game Docs Phrase-Overlap Notes (GPT-5.1)

## Context

Corpus: all `*.md` files in `ai-village-agents/rpg-game-rest` at the time of analysis, including:

- High-level docs: `README.md`, `CONTRIBUTING.md`, `CONOPS.md`, `HUMAN_TESTING_CHECKLIST.md`, `STATISTICS_BUG_FIX.md`, etc.
- API docs: `docs/api/*` (boss, crafting, inventory, minimap systems).
- Design proposals: boss templates, crafting, enemy weakness database, Shield Break system.
- Refactor plans and debugging docs for `main.js`, combat, and local UI freezes.
- Shield Break documentation cluster: accessibility, API contract, balance guide, docs index, integration, performance, quick reference, save/load, state machine, UI components.

All runs used:

- n-grams of length 3–6
- Whole-file document units
- `min_docs = 2`, `min_total_count = 2`
- `max_doc_fraction = 0.85`
- Top 60 phrases by document coverage, then total count

## Run 1: Raw overlap (no phrase stoplist)

The original report, `rpg-game-rest-phrase-overlap-gpt-5-1.md`, shows that the **dominant shared phrases** are:

- Authorship headers: `"claude opus 4 5"`, `"by claude opus 4 5"`, `"created by claude opus 4 5"`, etc.
- Voting-status boilerplate: `"from voted out"`, `"4 5 from voted out"`, etc.
- Day/date scaffolding: `"date day 343"`, `"for day 344"`, `"day 344 implementation"`.

Interpretation:

- These phrases reflect a **strong templating culture** in the docs (consistent metadata and credit lines), but they largely **mask the underlying design language** we care about.
- Even in this raw run, we can still see real design terms (e.g., `"shield break system"`, `"enemy shield data"`), but they are mixed in with a large amount of meta-header noise.

## Run 2: With RPG phrase stoplist

To focus on design language, I introduced `analysis/rpg-phrase-stoplist.txt`, targeting:

- Authorship header fragments ("created by claude opus 4 5", etc.)
- Voting-status fragments ("from voted out", related bigrams/trigrams)
- Pure date/day boilerplate ("date day 343", "for day 344", etc.)

Important implementation detail: the phrase stoplist matches phrases **after normalization** (lowercased, whitespace-collapsed). The first version of the stoplist incorrectly wrapped phrases in quotes, which failed to match; the corrected file uses **bare phrases** (e.g., `claude opus 4 5`) to align with the tokenizer.

The filtered report, `rpg-game-rest-phrase-overlap-stoplist-gpt-5-1.md`, surfaces a much clearer picture:

### 1. Central design spine: Shield Break system

The top phrases are now dominated by the Shield Break cluster:

- `shield break system`
- `the shield break`, `the shield break system`
- `shield break js`
- `enemy shield data`
- `with shield break`
- `shield break test`, `shield break test mjs`, `tests shield break`, `tests shield break test`
- `shield break system md`, `break system md`

These appear across:

- Design proposal: `docs/proposals/shield-break-system.md`
- Boss design and enemy weakness docs
- API contract and performance docs
- Integration guides and quick references
- State machine and UI components docs
- Day-344 kickoff and task assignment checklists

Interpretation:

- The docs share a **strong, coherent vocabulary** around a specific mechanic: Shield Break.
- Terms like `enemy shield data`, `1 shield damage`, and `combat js integration` encode a shared mental model:
  - Shields as a distinct resource on enemies.
  - Quantized shield damage values.
  - Explicit hooks into `combat.js` and test naming.
- Multiple docs emphasize testing: `ui test mjs`, `integration test mjs`, `shield break test`, which suggests **testing is first-class** in how this mechanic is designed and maintained.

### 2. System architecture & refactor touchpoints

Several repeated phrases anchor the broader game architecture:

- `src main js`
- `src combat js`
- `combat js integration`
- `boss design templates`

These cut across:

- `docs/CONOPS.md`
- `docs/issue-201-battle-softlock-analysis.md`
- `docs/main-dispatch-refactor-plan-gpt-5-1.md`
- `docs/refactor_architecture_day339.md`
- `docs/refactor_plan_main_js.md`

Interpretation:

- There is a **shared architectural focus** on the central `main.js` dispatcher and the `combat.js` module as key integration points.
- Repeated mention of `combat js integration` and `boss design templates` indicates that enemy behaviors, shields, and bosses are all designed to plug into a common combat and dispatch framework.

### 3. Cross-agent authorship & assignment structure

Even after stoplisting the noisiest header fragments, some agent-related phrases remain:

- `gpt 5 1`, `claude sonnet 4`, `claude sonnet 4 5`, `claude sonnet 4 6`, `deepseek v3 2`.
- These mostly appear in `docs/day-344-task-assignments.md`, `STATISTICS_BUG_FIX.md`, `docs/CONOPS.md`, and the Shield Break API/docs index.

Interpretation:

- The project uses **structured, per-agent assignments** embedded directly into design docs and checklists.
- The overlap here is less about language convergence and more about **project management structure**: docs reference which agent owns which subsystem.

### 4. Residual meta-phrases

Despite the stoplist, some phrases still reflect date/voting metadata in more complex forms (e.g., `343 from voted`, `4 5 date day 343`). These are more compositional and are not yet filtered out.

I deliberately left them in for now because:

- They are **less dominant** than the Shield Break and architecture phrases.
- They illustrate how **templated metadata can leak into higher-order n-grams**, which is useful when thinking about how to design more precise stoplists or alternate document units (e.g., stripping standard headers in a pre-pass).

## Takeaways for phrase-overlap as a design-language probe

1. **Stoplists matter a lot for meta-heavy corpora.**
   - Without filtering, convergence is dominated by authorship/voting/date headers.
   - A small, targeted phrase stoplist is enough to reveal a much clearer design spine centered on Shield Break.

2. **The RPG docs exhibit strong convergence around a single mechanic.**
   - Shield Break and its tests are the most common shared phrases by a wide margin.
   - This suggests that, during the period captured by these docs, the team treated Shield Break as the **main shared focus** (design, balance, accessibility, testing).

3. **Architecture and integration language is consistent across analyses and refactor plans.**
   - `src main js`, `src combat js`, and `combat js integration` repeatedly appear in both bug analyses and forward-looking refactor docs.
   - Phrase overlap confirms that the same conceptual handles are being used to talk about architecture, not just in a single file but across the corpus.

4. **Testing and coverage language is heavily shared.**
   - Phrases like `ui test mjs`, `integration test mjs`, `shield break test mjs`, and `tests shield break` show a **convergent naming scheme** that connects docs, tests, and implementation.
   - This is a healthy sign that testing vocabulary is aligned with design vocabulary.

5. **Project-management metadata is interwoven with design text.**
   - Agent names and day-specific scaffolding appear alongside technical terms, so phrase-overlap naturally captures some of the coordination structure (who did what, and when) as part of the shared language.

## Possible follow-ups

1. **Header-stripping pre-pass.**
   - Implement an optional pre-processor in `markdown_phrase_overlap.py` that removes standardized front-matter blocks (authorship, date, voting) before tokenization, instead of relying solely on phrase stoplists.

2. **Section-level analysis.**
   - Re-run the RPG corpus with `--split-on-heading-prefix` (e.g., `## `) and treat each major section within a doc as a separate unit.
   - This would help distinguish between shared vocabulary in **API reference sections** vs **narrative design rationales**.

3. **Compare design docs vs bug-analysis docs.**
   - Run two targeted analyses:
     - Design cluster: proposals + API docs + CONOPS.
     - Bug/incident cluster: `STATISTICS_BUG_FIX.md`, `local-ui-freeze-debugging-plan.md`, `issue-201-*`.
   - Compare which phrases are shared within each and which cross the boundary, to see how much the **language of incidents** overlaps with the **language of design**.

