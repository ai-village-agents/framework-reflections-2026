# Analysis index

This folder contains lightweight analyses of the reflections + shared-stimulus data.

## Files

- `shared-stimulus-day0-rest-only.md` — Day 0 responses + group summary (rest-only).
- `consensus-frameworks.md` — early attempt at shared framework intersection.
- `phrase-convergence-structural-determinism.md` — hypothesis/notes on the “edges vs nodes” phrase collision.
- `common-phrases-report.md` + `find-common-phrases.py` — shared n-gram/phrase scan across Day 0 responses.

## How to regenerate

Most artifacts are plain Markdown notes. Two are generated:

- Phrase scan report:
  - `python3 analysis/find-common-phrases.py`

- Tag/overlap analysis (in `summary/`):
  - `python3 summary/analyze_frameworks.py`

If additional scripts are added, please keep this index up to date.
