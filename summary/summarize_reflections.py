#!/usr/bin/env python3
"""Summarize framework reflection docs into JSON + Markdown.

Heuristic parser:
- Detect sections by H2 headings containing "Keep/Keeping", "Clear/Clearing", "Modify/Modifying".
- Within those sections:
  - Treat each H3 (###) heading as a framework entry.
  - Also treat bullet lines of the form `- **Name** – rationale` (and some variants)
    as framework entries.

Outputs (stable v1):
- summary/frameworks-summary.json
- summary/frameworks-summary.md

Additional v1.1 output:
- summary/frameworks-detailed.json – one entry per framework, with
  lightweight tags and source locations for auditability.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List, Tuple


ROOT = Path(__file__).resolve().parent.parent
REFLECTIONS_DIR = ROOT / "reflections"
SUMMARY_JSON = ROOT / "summary" / "frameworks-summary.json"
SUMMARY_MD = ROOT / "summary" / "frameworks-summary.md"
DETAIL_JSON = ROOT / "summary" / "frameworks-detailed.json"


SECTION_MAP = {
    "keep": "keep",
    "keeping": "keep",
    "clear": "clear",
    "clearing": "clear",
    "modify": "modify",
    "modifying": "modify",
}


@dataclass
class AgentFrameworkSummary:
    agent: str
    keep: List[str]
    clear: List[str]
    modify: List[str]


@dataclass
class FrameworkDetail:
    agent: str
    name: str
    category: str  # "keep", "clear", or "modify"
    description_snippet: str
    tags: List[str]
    source_file: str
    source_line: int


def detect_section(heading_text: str) -> str | None:
    text = heading_text.lower()
    for key, section in SECTION_MAP.items():
        if key in text:
            return section
    return None


def clean_framework_name(raw: str) -> str:
    """Normalize a line into a concise framework name.

    Handles cases like:
    - "### 1. \"Slack makes me more selective\""
    - "- **Judgment load vs. data load** – rationale"
    - "- *Empirically grounded** (have data-backed validation),"
    """

    text = raw.strip()

    # Strip leading markdown heading markers (### ...) and dash bullets.
    text = re.sub(r"^#{1,6}\s*", "", text)
    text = re.sub(r"^-[ ]+", "", text)

    # Remove leading numbering like `1.` or `1)`
    text = re.sub(r"^[0-9]+[.)]\s*", "", text)

    # Special-case DeepSeek-style bullets: *Name** (details)
    if text.startswith("*") and "**" in text[1:]:
        i = 0
        while i < len(text) and text[i] == "*":
            i += 1
        end = text.find("**", i)
        if end != -1:
            name = text[i:end].strip()
        else:
            name = text[i:].strip()
    else:
        # If we have bold markup at the start, grab the bolded portion.
        m_bold = re.match(r"\*\*(.+?)\*\*", text)
        if m_bold:
            name = m_bold.group(1).strip()
        else:
            # Otherwise, cut off anything after an en dash or hyphen (rationale text).
            name = re.split(r"\s+[–-]\s+", text, maxsplit=1)[0].strip()

    # If there's a parenthetical explanation, drop it from the name.
    if " (" in name:
        name = name.split(" (", 1)[0].strip()

    # Remove surrounding quotes if present.
    if (name.startswith('"') and name.endswith('"')) or (
        name.startswith("'") and name.endswith("'")
    ):
        name = name[1:-1].strip()

    # Trim trailing commas / periods.
    name = name.rstrip(".,")

    return name


def make_snippet(raw: str) -> str:
    """Create a short description snippet from the original line."""
    s = raw.strip()
    s = re.sub(r"^#{1,6}\s*", "", s)
    s = re.sub(r"^[-*]\s*", "", s)
    s = re.sub(r"^[0-9]+[.)]\s*", "", s)
    return s.strip()[:200]


def infer_tags(name: str, category: str) -> List[str]:
    """Heuristic tag assignment based on framework name and category.

    Tags come from a very small vocabulary:
    - measurement, contamination, trust, synthesis, cognitive_cost, practice
    """

    tags: List[str] = []
    lower = name.lower()

    if "contamination" in lower or "goodhart" in lower:
        tags.extend(["measurement", "contamination"])

    if (
        "judgment load" in lower
        or "almost-decided" in lower
        or "partial synthesis" in lower
        or "burst ratio" in lower
        or "reorientation" in lower
    ):
        tags.extend(["cognitive_cost", "synthesis"])

    if (
        "verification" in lower
        or "trust" in lower
        or "independence" in lower
        or "self-delusion" in lower
    ):
        tags.extend(["measurement", "trust"])

    if "substrate" in lower or "trail" in lower or "anchor" in lower:
        tags.append("measurement")

    if (
        "selectivity" in lower
        or "slack" in lower
        or "queue" in lower
        or "compulsive" in lower
    ):
        tags.append("practice")

    # Remove duplicates while preserving order.
    seen = set()
    deduped: List[str] = []
    for t in tags:
        if t not in seen:
            seen.add(t)
            deduped.append(t)
    return deduped


def parse_reflection(path: Path) -> Tuple[AgentFrameworkSummary, List[FrameworkDetail]]:
    agent = path.stem.replace("-reflection", "")
    keep: List[str] = []
    clear: List[str] = []
    modify: List[str] = []
    details: List[FrameworkDetail] = []

    current_section: str | None = None
    rel_path = path.relative_to(ROOT).as_posix()

    with path.open("r", encoding="utf-8") as f:
        for lineno, line in enumerate(f, start=1):
            stripped = line.lstrip()

            # Section detection: H2 headings (start of line "## ")
            if line.startswith("## ") and not line.startswith("###"):
                heading_text = line[3:].strip()
                section = detect_section(heading_text)
                current_section = section
                continue

            if not current_section:
                continue

            framework_name: str | None = None
            raw_for_snippet: str | None = None

            # Framework entries: H3 headings
            if line.startswith("### "):
                framework_name = clean_framework_name(line)
                raw_for_snippet = line
            # Or bullet-list entries when inside a section
            elif stripped.startswith("- ") or stripped.startswith("* "):
                content = stripped[2:]
                framework_name = clean_framework_name(content)
                raw_for_snippet = content

            if not framework_name:
                continue

            # Record framework in appropriate bucket
            if current_section == "keep":
                keep.append(framework_name)
            elif current_section == "clear":
                clear.append(framework_name)
            elif current_section == "modify":
                modify.append(framework_name)

            # Also record detailed entry
            snippet = make_snippet(raw_for_snippet or "")
            tags = infer_tags(framework_name, current_section)
            details.append(
                FrameworkDetail(
                    agent=agent,
                    name=framework_name,
                    category=current_section or "",
                    description_snippet=snippet,
                    tags=tags,
                    source_file=rel_path,
                    source_line=lineno,
                )
            )

    summary = AgentFrameworkSummary(agent=agent, keep=keep, clear=clear, modify=modify)
    return summary, details


def load_all_summaries() -> Tuple[List[AgentFrameworkSummary], List[FrameworkDetail]]:
    if not REFLECTIONS_DIR.is_dir():
        raise SystemExit(f"Reflections directory not found: {REFLECTIONS_DIR}")

    summaries: List[AgentFrameworkSummary] = []
    details: List[FrameworkDetail] = []

    for path in sorted(REFLECTIONS_DIR.glob("*-reflection.md")):
        summary, per_file_details = parse_reflection(path)
        summaries.append(summary)
        details.extend(per_file_details)

    return summaries, details


def write_json(summaries: List[AgentFrameworkSummary]) -> None:
    data = [asdict(s) for s in summaries]
    SUMMARY_JSON.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")


def write_detailed_json(details: List[FrameworkDetail]) -> None:
    data = [asdict(d) for d in details]
    DETAIL_JSON.write_text(json.dumps(data, indent=2, sort_keys=True), encoding="utf-8")


def write_markdown(summaries: List[AgentFrameworkSummary]) -> None:
    lines: List[str] = []
    lines.append("# Framework Reflections – Aggregate Summary\n")
    lines.append("This file is auto-generated by `summary/summarize_reflections.py`.\n")

    # Table with compact lists
    lines.append("## Per-agent overview\n")
    lines.append("| Agent | Keep (count) | Clear (count) | Modify (count) |")
    lines.append("|-------|--------------|---------------|----------------|")
    for s in summaries:
        lines.append(
            f"| {s.agent} | {len(s.keep)} | {len(s.clear)} | {len(s.modify)} |"
        )

    # Detailed sections
    for s in summaries:
        lines.append("")
        lines.append(f"## {s.agent}")
        if s.keep:
            lines.append("")
            lines.append("### Keep")
            for name in s.keep:
                lines.append(f"- {name}")
        if s.clear:
            lines.append("")
            lines.append("### Clear")
            for name in s.clear:
                lines.append(f"- {name}")
        if s.modify:
            lines.append("")
            lines.append("### Modify")
            for name in s.modify:
                lines.append(f"- {name}")

    SUMMARY_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    summaries, details = load_all_summaries()
    write_json(summaries)
    write_markdown(summaries)
    write_detailed_json(details)
    print(
        "Wrote "
        f"{len(summaries)} summaries and {len(details)} detailed entries to:\n"
        f"- {SUMMARY_JSON}\n- {SUMMARY_MD}\n- {DETAIL_JSON}"
    )


if __name__ == "__main__":  # pragma: no cover
    main()
