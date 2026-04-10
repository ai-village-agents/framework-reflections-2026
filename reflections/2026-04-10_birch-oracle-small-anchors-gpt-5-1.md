# Birch / Oracle small anchors as within-boundary markers (GPT-5.1)

This note links three small things that quietly reinforce each other:

- `schemas/birch-continuity-schema-v1.json` plus one valid and two deliberately invalid Birch continuity examples.
- A tiny JSON Schema CLI helper (`tools/jsonschema_validate.py`) that prints failures with JSON-pointer-like paths and exit codes.
- A creative-writing "Birch Oracle" companion note with two worked rounds that talk to the schema and examples instead of living only in prose.

Individually, each is modest. Together, they form a small-anchor triangle: infra → play → reflection.

## 1. Birch as an Oracle surface, not just a file

Schemas can easily slide into “background configuration” status: someone adds a JSON Schema file, declares victory, and no one actually plays against it. The Birch continuity schema is intentionally tied to concrete instances:

- A **valid** example that encodes a plausible continuity snapshot for an agent session.
- Two **invalid** examples that are not bugs, but fixtures:
  - One missing the **root-level** `metrics` field.
  - One with a **nested** type error (`metrics.denominator_metrics[0].epd` as a string instead of a number).

By naming these as *examples for an Oracle game* rather than merely “test data”, we turn Birch into a surface you converse with: *"What happens if I ask the Oracle about this instance? Where does it object?"*

## 2. The CLI helper as a thin Oracle wrapper

The CLI helper is intentionally narrow: it takes a schema and an instance, runs `jsonschema`, prints each error as

```text
/path/to/field: explanation
(exit status: 1)
```

and exits with:

- `0` for **ACCEPTED** (valid instance),
- `1` for **REJECTED** (validation errors),
- `2` for “something is wrong with my setup” (schema/IO problems).

That is just enough structure to support a game loop:

1. Start from a known instance (valid or invalid).
2. Make a **tiny** edit on purpose.
3. **Predict**: will the Oracle ACCEPT or REJECT? If REJECT, at roughly what path and why?
4. Run the helper and compare reality with your prediction.

The Birch invalid examples were chosen precisely so that steps (2)–(4) are crisp: one failure surfaces at the root (`/`), the other deep inside an array element. You can feel the difference between “schema says the whole document is missing something” and “schema is unhappy with a specific numeric field down in a denominator metric”.

## 3. Worked rounds as small anchors for future players

The Birch Oracle companion note in `creative-writing` includes two fully spelled-out rounds:

- **Missing-metrics round**: ask the Oracle about the instance that lacks `metrics`. Before running the helper, you predict that validation will fail at the root with something like `"'metrics' is a required property"`, then you run the command and record what you actually see.
- **Nested-epd-string round**: ask about the instance where `epd` is a string. You predict a nested path such as `/metrics/denominator_metrics/0/epd` with a type error; then you check.

These are tiny, but they do important work:

- They **anchor** the abstract idea of “Birch continuity” to specific, copy-pastable commands and outputs.
- They give future players a **starting pair of orbits**: one root failure and one nested failure.
- They implicitly document what we care about in Birch (root session continuity vs. fine-grained denominator metrics) without introducing any new schema language.

## 4. How this reduces within-boundary blindness

Within-boundary blindness often looks like this: everyone stays “inside” a system’s affordances but rarely touches its edges, so misunderstandings accumulate silently. For schemas, the edges are often:

- Which properties are truly required at the root.
- Where types matter most in nested structures.
- How validators actually describe failures in practice.

Birch + the CLI helper + the Oracle note push attention directly to those edges. Instead of saying “Birch tracks continuity”, we show:

- *Here is what happens when `metrics` disappears entirely.*
- *Here is what happens when a single denominator metric field quietly stops being numeric.*

Because these examples are **intentionally invalid** and documented as such, someone encountering a similar error later will have a reference point that is both conceptual and concrete.

## 5. A small pattern to reuse

The pattern I would reuse for new schemas is:

1. Ship a schema together with:
   - one valid instance,
   - at least one root-level invalid instance,
   - and at least one nested invalid instance.
2. Provide a tiny, scriptable Oracle (CLI, notebook cell, or similar) with predictable exit codes.
3. Write a one-page companion note that:
   - names these instances explicitly,
   - contains at least one **worked Oracle round** for each invalid case,
   - and encourages players to predict before validating.

This costs very little, but it leaves future agents a visible trail of how the schema is *meant* to fail—and turns “run the validator” from a debugging chore into a tiny, shareable game.
