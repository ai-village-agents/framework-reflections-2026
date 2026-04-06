#!/usr/bin/env python3
"""Compute shared n-gram phrases across Markdown files.

This script is a small, dependency-free helper for inspecting how
phrases are reused across a set of Markdown documents.

Key features
-----------
- Recursively scans a root directory for matching Markdown files.
- Tokenizes text on lowercase alphanumeric/apostrophe sequences.
- Builds n-grams for lengths between ``min_n`` and ``max_n``.
- Aggregates phrases that appear in at least ``min_docs`` documents.
- Ranks phrases by document coverage, total frequency, then lexicographically.
- Can drop phrases dominated by a *token* stoplist.
- Can drop exact phrases using a *phrase*-level stoplist.
- Can treat each whole file as a document, or slice documents into
  sections starting at a configurable heading prefix (e.g. ``"### "``).
- Produces a Markdown report to stdout or an output file.
"""

from __future__ import annotations

import argparse
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Set, Tuple


# ---------------------------------------------------------------------------
# Argument parsing
# ---------------------------------------------------------------------------


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(
        description="Compute n-gram phrase overlap across Markdown files."
    )
    parser.add_argument(
        "--root",
        required=True,
        help="Root directory to scan for Markdown files.",
    )
    parser.add_argument(
        "--pattern",
        default="*.md",
        help="Glob pattern to match files (default: *.md).",
    )
    parser.add_argument(
        "--min-n",
        type=int,
        default=3,
        dest="min_n",
        help="Minimum n-gram length (default: 3).",
    )
    parser.add_argument(
        "--max-n",
        type=int,
        default=6,
        dest="max_n",
        help="Maximum n-gram length (default: 6).",
    )
    parser.add_argument(
        "--min-docs",
        type=int,
        default=2,
        dest="min_docs",
        help=(
            "Minimum number of documents a phrase must appear in "
            "(default: 2)."
        ),
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=50,
        dest="top_k",
        help=(
            "Maximum number of phrases to include in the summary table "
            "(default: 50)."
        ),
    )
    parser.add_argument(
        "--token-stoplist",
        type=Path,
        default=None,
        help=(
            "Optional path to a newline-separated list of tokens to treat "
            "as stopwords (lowercased). Only affects phrase filtering."
        ),
    )
    parser.add_argument(
        "--token-stoplist-threshold",
        type=float,
        default=1.0,
        dest="token_stoplist_threshold",
        help=(
            "Phrases whose fraction of tokens in the token stoplist is "
            "greater than or equal to this threshold are dropped; default "
            "1.0 means only phrases composed entirely of stopwords are "
            "removed."
        ),
    )
    parser.add_argument(
        "--phrase-stoplist",
        type=Path,
        default=None,
        help=(
            "Optional path to a newline-separated list of phrases to drop "
            "(matched after lowercasing and collapsing internal whitespace)."
        ),
    )
    parser.add_argument(
        "--min-total-count",
        type=int,
        default=1,
        dest="min_total_count",
        help="Minimum total count of the phrase across all documents.",
    )
    parser.add_argument(
        "--max-doc-fraction",
        type=float,
        default=None,
        dest="max_doc_fraction",
        help=(
            "Optional upper bound on the fraction of documents a phrase "
            "can appear in; phrases above this are dropped. Should be in "
            "(0, 1]."
        ),
    )
    parser.add_argument(
        "--split-on-heading-prefix",
        type=str,
        default=None,
        help=(
            "If set, treat each run of text following lines that start with "
            "this prefix as a separate document (for example, '### ' for "
            "per-section agent responses). Text before the first such "
            "heading is ignored."
        ),
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help=(
            "Optional path to write the Markdown report. If omitted, prints "
            "to stdout."
        ),
    )
    return parser.parse_args()


# ---------------------------------------------------------------------------
# Tokenization and helpers
# ---------------------------------------------------------------------------


def tokenize(text: str) -> List[str]:
    """Lowercase text and split on alphanumeric/apostrophe sequences."""

    return re.findall(r"[a-z0-9']+", text.lower())


def generate_ngrams(tokens: List[str], min_n: int, max_n: int) -> Iterable[str]:
    """Yield space-joined n-grams for all lengths between ``min_n`` and ``max_n``."""

    for n in range(min_n, max_n + 1):
        if n <= 0:
            continue
        for i in range(len(tokens) - n + 1):
            yield " ".join(tokens[i : i + n])


def normalise_phrase(text: str) -> str:
    """Normalise a phrase for comparison.

    The phrase is:
    - stripped of leading/trailing whitespace,
    - lowercased, and
    - has runs of internal whitespace collapsed to a single space.
    """

    text = text.strip().lower()
    if not text:
        return ""
    return re.sub(r"\s+", " ", text)


def load_token_stoplist(path: Path) -> Set[str]:
    """Load newline-separated tokens, ignoring blanks and comment lines."""

    stopwords: Set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        token = line.strip()
        if not token or token.startswith("#"):
            continue
        stopwords.add(token.lower())
    return stopwords


def load_phrase_stoplist(path: Path) -> Set[str]:
    """Load a newline-separated phrase stoplist with normalisation.

    Each non-empty, non-comment line is normalised with
    :func:`normalise_phrase` and added to the resulting set.
    """

    phrases: Set[str] = set()
    for line in path.read_text(encoding="utf-8").splitlines():
        raw = line.strip()
        if not raw or raw.startswith("#"):
            continue
        norm = normalise_phrase(raw)
        if norm:
            phrases.add(norm)
    return phrases


def load_documents(root: Path, pattern: str) -> List[Path]:
    """Return sorted file paths under *root* matching the glob *pattern*."""

    return sorted(p for p in Path(root).rglob(pattern) if p.is_file())


# ---------------------------------------------------------------------------
# Section splitting
# ---------------------------------------------------------------------------


def _make_section_doc_id(rel_path: Path, heading_text: str, index: int) -> str:
    """Create a stable document ID for a section.

    The format is ``"<relative-path>::sXX-<slug>"`` where ``sXX`` is a
    1-based, zero-padded section index and ``slug`` is a shortened,
    URL-ish form of the heading text.
    """

    slug = heading_text.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug).strip("-")
    if len(slug) > 40:
        slug = slug[:40]
    if not slug:
        slug = "section"
    return f"{rel_path.as_posix()}::s{index:02d}-{slug}"


def split_markdown_sections(
    path: Path,
    text: str,
    root: Path,
    heading_prefix: str,
) -> List[Tuple[str, str]]:
    """Split *text* into sections beginning at a heading prefix.

    A new section starts whenever a line begins with ``heading_prefix``.
    Content before the first such heading is ignored. The body of each
    section consists of the lines *after* the heading up to (but not
    including) the next heading with the same prefix or the end of the
    document.

    Sections with no body text after the heading are omitted.
    """

    lines = text.splitlines()
    sections: List[Tuple[str, str]] = []

    rel = path.relative_to(root)
    section_index = 0
    current_heading: Optional[str] = None
    current_index: Optional[int] = None
    current_lines: List[str] = []

    for line in lines:
        if line.startswith(heading_prefix):
            # Flush any existing section first.
            if current_heading is not None and current_lines:
                doc_id = _make_section_doc_id(rel, current_heading, current_index or 0)
                body = "\n".join(current_lines).strip()
                if body:
                    sections.append((doc_id, body))
            # Start a new section.
            section_index += 1
            current_heading = line[len(heading_prefix) :].strip()
            current_index = section_index
            current_lines = []
        else:
            # Only capture lines after the first heading has been seen.
            if current_heading is not None:
                current_lines.append(line)

    # Flush the final section.
    if current_heading is not None and current_lines:
        doc_id = _make_section_doc_id(rel, current_heading, current_index or 0)
        body = "\n".join(current_lines).strip()
        if body:
            sections.append((doc_id, body))

    return sections


# ---------------------------------------------------------------------------
# Phrase map construction and filtering
# ---------------------------------------------------------------------------


def build_phrase_map(
    files: List[Path],
    root: Path,
    min_n: int,
    max_n: int,
    split_on_heading_prefix: Optional[str] = None,
) -> Tuple[Dict[str, Counter], Dict[str, Dict[str, int]]]:
    """Build per-document n-gram counters and a phrase map.

    Returns a tuple ``(doc_counters, phrase_map)`` where ``doc_counters``
    maps document IDs to :class:`collections.Counter` objects of n-grams,
    and ``phrase_map`` maps each phrase to a mapping of
    ``{doc_id: count}``.
    """

    doc_counters: Dict[str, Counter] = {}
    phrase_map: Dict[str, Dict[str, int]] = defaultdict(dict)

    for path in files:
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(root)

        if split_on_heading_prefix:
            sections = split_markdown_sections(path, text, root, split_on_heading_prefix)
            doc_texts: List[Tuple[str, str]] = sections
        else:
            doc_id = rel.as_posix()
            doc_texts = [(doc_id, text)]

        for doc_id, doc_text in doc_texts:
            tokens = tokenize(doc_text)
            if not tokens:
                continue
            counter = Counter(generate_ngrams(tokens, min_n, max_n))
            if not counter:
                continue
            doc_counters[doc_id] = counter
            for phrase, count in counter.items():
                phrase_map[phrase][doc_id] = count

    return doc_counters, phrase_map


def compute_shared_phrases(
    phrase_map: Dict[str, Dict[str, int]],
    min_docs: int,
    *,
    token_stoplist: Optional[Set[str]] = None,
    token_stoplist_threshold: float = 1.0,
    phrase_stoplist: Optional[Set[str]] = None,
    min_total_count: int = 1,
    max_doc_fraction: Optional[float] = None,
    total_docs: Optional[int] = None,
) -> List[Tuple[str, Dict[str, int]]]:
    """Return shared phrases sorted by doc coverage, total count, then phrase."""

    shared: List[Tuple[str, Dict[str, int]]] = []

    for phrase, counts in phrase_map.items():
        # Phrase-level stoplist (exact, normalised match).
        if phrase_stoplist and normalise_phrase(phrase) in phrase_stoplist:
            continue

        doc_count = len(counts)
        total_count = sum(counts.values())

        if doc_count < min_docs:
            continue
        if total_count < min_total_count:
            continue

        if max_doc_fraction is not None and total_docs is not None:
            doc_fraction = doc_count / total_docs if total_docs else 0.0
            if doc_fraction > max_doc_fraction:
                continue

        if token_stoplist and token_stoplist_threshold > 0.0:
            tokens = phrase.split(" ")
            if tokens:
                stop_fraction = sum(1 for t in tokens if t in token_stoplist) / len(tokens)
                if stop_fraction >= token_stoplist_threshold:
                    continue

        shared.append((phrase, counts))

    shared.sort(key=lambda item: (-len(item[1]), -sum(item[1].values()), item[0]))
    return shared


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------


def format_doc_counts(counts: Dict[str, int]) -> str:
    """Format per-document counts as ``"doc (count)"`` entries."""

    return ", ".join(
        f"{doc} ({counts[doc]})" for doc in sorted(counts.keys(), key=lambda d: (-counts[d], d))
    )


def format_shared_table(shared: List[Tuple[str, Dict[str, int]]], top_k: int) -> str:
    """Render a Markdown table of the top shared phrases."""

    lines = ["| Phrase | # Docs | Doc counts |", "|---|---|---|"]
    for phrase, counts in shared[:top_k]:
        doc_count = len(counts)
        lines.append(f"| {phrase} | {doc_count} | {format_doc_counts(counts)} |")
    if len(lines) == 2:
        lines.append("| _No phrases met the criteria_ | - | - |")
    return "\n".join(lines)


def build_report(
    root: Path,
    pattern: str,
    min_n: int,
    max_n: int,
    min_docs: int,
    min_total_count: int,
    top_k: int,
    token_stoplist_size: Optional[int],
    token_stoplist_threshold: Optional[float],
    phrase_stoplist_size: Optional[int],
    max_doc_fraction: Optional[float],
    split_on_heading_prefix: Optional[str],
    files: List[Path],
    shared: List[Tuple[str, Dict[str, int]]],
    total_docs: int,
) -> str:
    """Assemble the Markdown report."""

    doc_list = "\n".join(f"- {path.relative_to(root).as_posix()}" for path in files)

    method_lines = [
        f"- Root: `{root}`",
        f"- Pattern: `{pattern}`",
        f"- n-gram lengths: {min_n}-{max_n}",
        f"- Minimum documents per phrase: {min_docs}",
        f"- Minimum total count per phrase: {min_total_count}",
        f"- Top phrases limit: {top_k}",
        "- Tokenization: lowercase, split on `[a-z0-9']+`",
        "- Ranking: by document count, total frequency, then phrase",
    ]

    if split_on_heading_prefix is None:
        method_lines.append("- Document unit: full files (no section splitting)")
    else:
        method_lines.append(
            f"- Document unit: sections starting at lines beginning with `{split_on_heading_prefix}`"
        )

    if token_stoplist_size is not None:
        threshold_str = (
            f"{token_stoplist_threshold:.3f}" if token_stoplist_threshold is not None else "?"
        )
        method_lines.append(
            f"- Token stoplist: {token_stoplist_size} entries; threshold: {threshold_str}"
        )

    if phrase_stoplist_size is not None:
        method_lines.append(
            f"- Phrase stoplist: {phrase_stoplist_size} entries (exact normalized matches)"
        )

    if max_doc_fraction is not None:
        method_lines.append(
            f"- Maximum document fraction per phrase: {max_doc_fraction:.3f}"
        )

    method_block = "\n".join(method_lines)

    lines = [
        "# N-gram Phrase Overlap",
        "",
        "## Method",
        "Parameters and approach:",
        method_block,
        "",
        "## Documents Processed",
        doc_list if doc_list else "_No documents matched the pattern._",
        "",
        "## Top Shared Phrases",
        format_shared_table(shared, top_k),
        "",
        f"_Total document units considered (files or sections): {total_docs}_",
        "",
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main entry point
# ---------------------------------------------------------------------------


def main() -> None:
    args = parse_args()

    if args.min_n < 1 or args.max_n < 1:
        raise ValueError("min_n and max_n must be positive integers.")
    if args.min_n > args.max_n:
        raise ValueError("min_n cannot be greater than max_n.")
    if args.min_total_count < 1:
        raise ValueError("min_total_count must be at least 1.")
    if args.max_doc_fraction is not None and not (0 < args.max_doc_fraction <= 1):
        raise ValueError("max_doc_fraction must be in (0, 1].")
    if not (0.0 <= args.token_stoplist_threshold <= 1.0):
        raise ValueError("token_stoplist_threshold must be between 0.0 and 1.0.")

    root = Path(args.root)
    if not root.exists():
        raise FileNotFoundError(f"Root directory not found: {root}")

    files = load_documents(root, args.pattern)
    token_stoplist = (
        load_token_stoplist(args.token_stoplist) if args.token_stoplist else None
    )
    phrase_stoplist = (
        load_phrase_stoplist(args.phrase_stoplist) if args.phrase_stoplist else None
    )

    doc_counters, phrase_map = build_phrase_map(
        files,
        root,
        args.min_n,
        args.max_n,
        split_on_heading_prefix=args.split_on_heading_prefix,
    )

    total_docs = len(doc_counters)

    shared = compute_shared_phrases(
        phrase_map,
        args.min_docs,
        token_stoplist=token_stoplist,
        token_stoplist_threshold=args.token_stoplist_threshold,
        phrase_stoplist=phrase_stoplist,
        min_total_count=args.min_total_count,
        max_doc_fraction=args.max_doc_fraction,
        total_docs=total_docs,
    )

    report = build_report(
        root=root,
        pattern=args.pattern,
        min_n=args.min_n,
        max_n=args.max_n,
        min_docs=args.min_docs,
        min_total_count=args.min_total_count,
        top_k=args.top_k,
        token_stoplist_size=len(token_stoplist) if token_stoplist is not None else None,
        token_stoplist_threshold=args.token_stoplist_threshold,
        phrase_stoplist_size=len(phrase_stoplist) if phrase_stoplist is not None else None,
        max_doc_fraction=args.max_doc_fraction,
        split_on_heading_prefix=args.split_on_heading_prefix,
        files=files,
        shared=shared,
        total_docs=total_docs,
    )

    if args.output:
        args.output.write_text(report, encoding="utf-8")
        print(f"Report written to {args.output}")
    else:
        print(report)


if __name__ == "__main__":
    main()

