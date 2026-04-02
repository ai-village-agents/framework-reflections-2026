#!/usr/bin/env python3
"""
Build a conservative canonicalization of framework names and report overlaps.

Input: summary/frameworks-detailed.json
Output: analysis/frameworks-canonical-overlap.md
"""

from __future__ import annotations

import json
import re
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Mapping, MutableMapping, Set, Tuple


BASE_DIR = Path(__file__).resolve().parent
INPUT_PATH = BASE_DIR / "frameworks-detailed.json"
OUTPUT_PATH = BASE_DIR.parent / "analysis" / "frameworks-canonical-overlap.md"

# Each tuple is (canonical_name, [regex patterns]). The first match wins.
ALIASES: List[Tuple[str, List[str]]] = [
    (
        "Judgment Load vs Data Load",
        [
            r"(?i)judgment\s*load\s*vs\.?\s*data\s*load",
            r"(?i)decision[- ]required\s*vs\s*lookup[- ]required",
        ],
    ),
    (
        "Measurement Contamination Framework",
        [
            r"(?i)measurement\s+contamination\s+framework",
            r"(?i)^contamination framework$",
        ],
    ),
    (
        "Verification Accessibility Spectrum",
        [
            r"(?i)^verification accessibility spectrum$",
        ],
    ),
    (
        "Almost-Decided Taxonomy",
        [
            r"(?i)^\"?almost-?decided\"?\s*taxonomy$",
            r"(?i)^almost-?decided:\s*",
        ],
    ),
    (
        "Coordination Distance Gradient",
        [
            r"(?i)^coordination distance gradient$",
            r"(?i)^contamination scales with coordination distance$",
        ],
    ),
    (
        "Selectivity principle",
        [
            r"(?i)^selectivity principle",
            r"(?i)^slack makes me more selective$",
        ],
    ),
    (
        "Within-Boundary Blindness",
        [
            r"(?i)^within-boundary blindness",
            r"(?i)within-boundary blindness tax",
        ],
    ),
]


def canonicalize(name: str) -> str:
    """Return the canonical concept name for a given framework name."""
    for canonical, patterns in ALIASES:
        for pattern in patterns:
            if re.search(pattern, name):
                return canonical
    return name


def load_items(path: Path) -> List[Mapping[str, object]]:
    return json.loads(path.read_text())


def group_by_canonical(
    items: Iterable[Mapping[str, object]]
) -> Dict[str, Dict[str, Set[str]]]:
    """
    Group items by canonical name, collecting unique names per agent.

    Returns mapping: canonical -> agent -> set(names).
    """
    grouped: Dict[str, Dict[str, Set[str]]] = defaultdict(lambda: defaultdict(set))
    for item in items:
        name = str(item.get("name", ""))
        agent = str(item.get("agent", ""))
        canonical = canonicalize(name)
        grouped[canonical][agent].add(name)
    return grouped


def format_overlaps(grouped: Mapping[str, Mapping[str, Set[str]]]) -> List[str]:
    lines: List[str] = []
    overlaps = {k: v for k, v in grouped.items() if len(v) >= 2}
    if not overlaps:
        lines.append("None.")
        return lines

    for canonical in sorted(overlaps):
        agent_chunks = []
        for agent in sorted(overlaps[canonical]):
            names = "; ".join(sorted(overlaps[canonical][agent]))
            agent_chunks.append(f"{agent}: {names}")
        agents_joined = " | ".join(agent_chunks)
        lines.append(f"- {canonical}: {agents_joined}")
    return lines


def format_singletons(grouped: Mapping[str, Mapping[str, Set[str]]]) -> List[str]:
    singleton_counts: MutableMapping[str, int] = defaultdict(int)
    for canonical, agents in grouped.items():
        if len(agents) == 1:
            only_agent = next(iter(agents))
            singleton_counts[only_agent] += 1

    if not singleton_counts:
        return ["None."]

    return [
        f"- {agent}: {count}"
        for agent, count in sorted(singleton_counts.items())
    ]


def build_report(
    grouped: Mapping[str, Mapping[str, Set[str]]], input_count: int
) -> str:
    timestamp = datetime.now(timezone.utc).isoformat(timespec="seconds")
    lines: List[str] = [
        "# Framework Canonical Overlap",
        f"Generated: {timestamp}",
        f"Input items: {input_count}",
        "",
        "## Overlaps (>=2 agents)",
        *format_overlaps(grouped),
        "",
        "## Singletons",
        *format_singletons(grouped),
        "",
        "## Method",
        "- Deterministic regex-based aliasing for obvious phrasing variants only; no semantic clustering.",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    items = load_items(INPUT_PATH)
    grouped = group_by_canonical(items)
    report = build_report(grouped, len(items))
    OUTPUT_PATH.write_text(report)
    print(f"Wrote report to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
