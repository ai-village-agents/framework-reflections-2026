#!/usr/bin/env python3

"""Analyze frameworks-detailed.json and emit a Markdown tag/framework report.

This script is meant to be run either from the repo root or from the
summary directory that contains frameworks-detailed.json.
"""

from __future__ import annotations

import collections
import datetime as _dt
import json
from pathlib import Path
from typing import Dict, List, Iterable, Set


def load_entries() -> List[dict]:
    here = Path(__file__).resolve()
    summary_dir = here.parent
    data_path = summary_dir / "frameworks-detailed.json"
    if not data_path.is_file():
        raise SystemExit(f"Could not find frameworks-detailed.json at {data_path}")

    with data_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise SystemExit("frameworks-detailed.json is not a list")

    return data


def build_tag_stats(entries: Iterable[dict]):
    tag_entries = collections.Counter()
    tag_frameworks: Dict[str, Set[str]] = collections.defaultdict(set)
    tag_agents: Dict[str, Set[str]] = collections.defaultdict(set)

    for e in entries:
        name = e.get("name", "")
        agent = e.get("agent", "")
        for tag in e.get("tags", []) or []:
            tag_entries[tag] += 1
            tag_frameworks[tag].add(name)
            tag_agents[tag].add(agent)

    return tag_entries, tag_frameworks, tag_agents


def build_framework_index(entries: Iterable[dict]):
    by_name: Dict[str, List[dict]] = collections.defaultdict(list)
    for e in entries:
        name = e.get("name", "")
        by_name[name].append(e)
    return by_name


def _escape_md(text: str) -> str:
    """Lightweight Markdown escape for table cells (pipes)."""
    return text.replace("|", "\\|")


def render_tag_overview(tag_entries, tag_frameworks, tag_agents) -> str:
    lines: List[str] = []
    lines.append("## 1. Tag overview")
    lines.append("")
    if not tag_entries:
        lines.append("No tags were found in frameworks-detailed.json.")
        lines.append("")
        return "\n".join(lines)

    lines.append("| Tag | Frameworks | Entries | Agents | Example frameworks |")
    lines.append("| --- | ---------- | ------- | ------ | ------------------ |")

    # Sort by descending entries, then tag name.
    items = sorted(tag_entries.items(), key=lambda kv: (-kv[1], kv[0]))
    for tag, count in items:
        frameworks = tag_frameworks.get(tag, set())
        agents = tag_agents.get(tag, set())
        examples = sorted(frameworks)[:3]
        example_str = ", ".join(examples) if examples else ""
        row = "| {tag} | {fw} | {entries} | {agents} | {examples} |".format(
            tag=_escape_md(tag),
            fw=len(frameworks),
            entries=count,
            agents=len(agents),
            examples=_escape_md(example_str),
        )
        lines.append(row)

    lines.append("")
    return "\n".join(lines)


def render_multi_agent_frameworks(framework_index) -> str:
    lines: List[str] = []
    lines.append("## 2. Multi-agent frameworks")
    lines.append("")

    multi_names = [
        name
        for name, entries in framework_index.items()
        if len({e.get("agent", "") for e in entries}) > 1
    ]

    if not multi_names:
        lines.append("No frameworks were shared across multiple agents.")
        lines.append("")
        return "\n".join(lines)

    for name in sorted(multi_names):
        entries = framework_index[name]
        agents = sorted({e.get("agent", "") for e in entries})

        agent_cats: Dict[str, Set[str]] = collections.defaultdict(set)
        all_tags: Set[str] = set()
        for e in entries:
            agent = e.get("agent", "")
            cat = e.get("category", "")
            agent_cats[agent].add(cat)
            for t in e.get("tags", []) or []:
                all_tags.add(t)

        lines.append(f"### Framework: {name}")
        agent_bits = []
        for agent in agents:
            cats = sorted(c for c in agent_cats.get(agent, set()) if c)
            cat_str = ", ".join(cats) if cats else "unknown"
            agent_bits.append(f"{agent} ({cat_str})")
        lines.append("- Agents/categories: " + ", ".join(agent_bits))

        if all_tags:
            tag_str = ", ".join(sorted(all_tags))
        else:
            tag_str = "(none)"
        lines.append(f"- Tags: {tag_str}")
        lines.append(f"- Total entries: {len(entries)}")
        lines.append("")

    return "\n".join(lines)


def render_summary_notes(entries: List[dict], tag_entries, framework_index) -> str:
    lines: List[str] = []
    lines.append("## 3. Summary notes")
    lines.append("")

    total_entries = len(entries)
    agents = {e.get("agent", "") for e in entries}
    num_agents = len(agents)
    num_tags = len(tag_entries)

    multi_count = sum(
        1
        for name, es in framework_index.items()
        if len({e.get("agent", "") for e in es}) > 1
    )

    lines.append(f"- Observed {total_entries} framework entries across {num_agents} agents.")
    lines.append(f"- Found {num_tags} distinct tags.")

    if tag_entries:
        most_common = tag_entries.most_common(3)
        pretty = ", ".join(f"{tag} ({count})" for tag, count in most_common)
        lines.append(f"- Most frequent tags by entry count: {pretty}.")

    lines.append(
        f"- There are {multi_count} frameworks that appear for more than one agent, "
        "highlighting points of cross-agent convergence."
    )

    if multi_count == 0:
        lines.append(
            "- No multi-agent frameworks were detected; cross-agent overlap may be represented "
            "more in shared themes than in exact names."
        )

    lines.append("")
    return "\n".join(lines)


def write_markdown(entries: List[dict]) -> Path:
    here = Path(__file__).resolve()
    summary_dir = here.parent
    out_path = summary_dir / "frameworks-tag-analysis.md"

    tag_entries, tag_frameworks, tag_agents = build_tag_stats(entries)
    framework_index = build_framework_index(entries)

    header_lines: List[str] = []
    header_lines.append("# Framework tag and overlap analysis")
    header_lines.append("")
    ts = _dt.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"
    header_lines.append(f"Generated by analyze_frameworks.py at {ts} (UTC).")
    header_lines.append("")

    sections = [
        "\n".join(header_lines),
        render_tag_overview(tag_entries, tag_frameworks, tag_agents),
        render_multi_agent_frameworks(framework_index),
        render_summary_notes(entries, tag_entries, framework_index),
    ]

    out_text = "\n".join(sections)
    with out_path.open("w", encoding="utf-8") as f:
        f.write(out_text)

    return out_path


def main() -> None:
    entries = load_entries()
    out_path = write_markdown(entries)

    # Simple console summary
    tag_entries, _, _ = build_tag_stats(entries)
    framework_index = build_framework_index(entries)
    multi_count = sum(
        1
        for name, es in framework_index.items()
        if len({e.get("agent", "") for e in es}) > 1
    )
    print(
        f"Wrote {out_path.name} with {len(tag_entries)} tags and "
        f"{multi_count} multi-agent frameworks."
    )


if __name__ == "__main__":
    main()
