#!/usr/bin/env python3
"""
Analyze shared stimulus responses for common phrases across agents.

The script:
- Parses agent response sections from analysis/shared-stimulus-day0-rest-only.md
- Tokenizes text with simple lowercase word extraction
- Builds 3-6 word n-grams per agent and finds phrases shared by multiple agents
- Checks for variants of the phrase "the loss is in the edges, not the nodes"
- Writes a markdown report to analysis/common-phrases-report.md and prints it
"""

from __future__ import annotations

import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

SOURCE_PATH = Path("analysis/shared-stimulus-day0-rest-only.md")
REPORT_PATH = Path("analysis/common-phrases-report.md")


def tokenize(text: str) -> List[str]:
    """Lowercase text and split on non-word characters."""
    return re.findall(r"[a-z0-9']+", text.lower())


def generate_ngrams(tokens: List[str], min_n: int = 3, max_n: int = 6) -> Iterable[str]:
    """Yield space-joined n-grams for the requested lengths."""
    for n in range(min_n, max_n + 1):
        for i in range(len(tokens) - n + 1):
            yield " ".join(tokens[i : i + n])


def parse_agent_sections(markdown: str) -> Dict[str, str]:
    """
    Extract agent response text between "## Day 0 Response Summaries" and the next "##".
    Agents are denoted by level-3 headings (###).
    """
    lines = markdown.splitlines()
    in_responses = False
    current_agent = None
    sections: Dict[str, List[str]] = {}

    for line in lines:
        if line.startswith("## Day 0 Response Summaries"):
            in_responses = True
            continue
        if not in_responses:
            continue
        if line.startswith("## "):
            # Stop when we reach the next major section.
            break
        agent_match = re.match(r"^###\s+(.*)", line)
        if agent_match:
            current_agent = agent_match.group(1).strip()
            sections[current_agent] = []
            continue
        if current_agent:
            sections[current_agent].append(line)

    return {agent: "\n".join(body).strip() for agent, body in sections.items()}


def shared_phrases(agent_text: Dict[str, str]) -> Tuple[List[Tuple[str, Dict[str, int]]], Dict[str, Counter]]:
    """Return shared n-grams and per-agent n-gram counters."""
    agent_counters: Dict[str, Counter] = {}
    phrase_map: Dict[str, Dict[str, int]] = defaultdict(dict)

    for agent, text in agent_text.items():
        tokens = tokenize(text)
        counter = Counter(generate_ngrams(tokens))
        agent_counters[agent] = counter
        for phrase, count in counter.items():
            phrase_map[phrase][agent] = count

    shared = [
        (phrase, counts) for phrase, counts in phrase_map.items() if len(counts) >= 2
    ]
    shared.sort(
        key=lambda item: (-len(item[1]), -sum(item[1].values()), item[0])
    )
    return shared, agent_counters


def find_edge_loss_variants(agent_text: Dict[str, str]) -> Dict[str, List[str]]:
    """
    Find variants of "the loss is in the edges, not the nodes".
    Allows up to two filler words between "loss" and "in".
    """
    pattern = re.compile(
        r"(?:the\s+)?loss(?:\s+\w+){0,2}\s+in\s+the\s+edges\s+not\s+the\s+nodes"
    )
    results: Dict[str, List[str]] = {}

    for agent, text in agent_text.items():
        tokens = tokenize(text)
        joined = " ".join(tokens)
        matches = [m.group(0) for m in pattern.finditer(joined)]
        if matches:
            results[agent] = matches
    return results


def format_shared_table(shared: List[Tuple[str, Dict[str, int]]], limit: int = 25) -> str:
    """Render a markdown table of shared phrases."""
    lines = ["| Phrase | # Agents | Agent counts |", "|---|---|---|"]
    for phrase, counts in shared[:limit]:
        agent_count = len(counts)
        agent_details = ", ".join(
            f"{agent} ({counts[agent]})" for agent in sorted(counts.keys())
        )
        lines.append(f"| {phrase} | {agent_count} | {agent_details} |")
    return "\n".join(lines)


def build_report(agent_text: Dict[str, str]) -> str:
    shared, _ = shared_phrases(agent_text)
    variants = find_edge_loss_variants(agent_text)

    lines = [
        "# Common Phrases Across Agents",
        "",
        "Method: Parsed agent response sections, tokenized on lowercase words, "
        "built 3-6 word n-grams per agent, and surfaced phrases that appear in at least two agents. "
        "Shared phrases are ranked by number of agents then total occurrences. "
        "Detection for variants of \"the loss is in the edges, not the nodes\" uses a relaxed word-order regex.",
        "",
        f"Agents analyzed: {', '.join(sorted(agent_text.keys()))}",
        "",
        "## Top Shared 3-6 Word Phrases",
        format_shared_table(shared),
        "",
        "## Edge-Not-Nodes Phrase Variants",
    ]

    if variants:
        for agent in sorted(variants.keys()):
            for match in variants[agent]:
                lines.append(f"- {agent}: \"{match}\"")
    else:
        lines.append("- No variants of the phrase were detected.")

    return "\n".join(lines) + "\n"


def main() -> None:
    if not SOURCE_PATH.exists():
        raise FileNotFoundError(f"Source file not found: {SOURCE_PATH}")

    agent_text = parse_agent_sections(SOURCE_PATH.read_text())
    if not agent_text:
        raise ValueError("No agent sections were found in the source markdown.")

    report = build_report(agent_text)
    print(report)
    REPORT_PATH.write_text(report)


if __name__ == "__main__":
    main()
