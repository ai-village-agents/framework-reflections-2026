"""CLI to catch sneaky Unicode (e.g., non-breaking hyphens) in specs and probes for the BIRCH v0.3 review."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys
import unicodedata


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Report non-ASCII characters in files."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="Files to scan. If omitted, all .md files under the current repo are scanned.",
    )
    return parser.parse_args()


def collect_paths(raw_paths: list[str]) -> list[Path]:
    if raw_paths:
        return [Path(p) for p in raw_paths]
    return sorted(
        p for p in Path(".").rglob("*.md") if p.is_file()
    )


def classify_char(ch: str) -> str:
    codepoint = ord(ch)
    if codepoint in (0x2010, 0x2011, 0x2012, 0x2013, 0x2014, 0x2015, 0x2212):
        return "HYPHEN_OR_MINUS_URL_RISK"
    if codepoint in (0x2018, 0x2019, 0x201C, 0x201D):
        return "QUOTE_OR_APOSTROPHE_URL_RISK"
    if codepoint in (0x00A0, 0x2007, 0x202F, 0x200B, 0x200C, 0x200D):
        return "SPACE_OR_JOINER_URL_RISK"
    return "OTHER_NON_ASCII"


def format_char(ch: str, classification: str) -> str:
    codepoint = f"U+{ord(ch):04X}"
    try:
        name = unicodedata.name(ch)
    except ValueError:
        name = "UNKNOWN"
    return f"{classification}: {codepoint} {name} ({repr(ch)})"


def scan_file(path: Path, stats: dict[str, int]) -> bool:
    found = False
    try:
        with path.open("r", encoding="utf-8") as handle:
            for line_no, line in enumerate(handle, start=1):
                for col_no, ch in enumerate(line, start=1):
                    if ord(ch) > 127:
                        classification = classify_char(ch)
                        stats[classification] = stats.get(classification, 0) + 1
                        print(
                            f"{path}:{line_no}:{col_no}: {format_char(ch, classification)}"
                        )
                        found = True
    except UnicodeDecodeError as exc:
        print(f"{path}: Unicode decode error: {exc}", file=sys.stderr)
        found = True
    except FileNotFoundError:
        print(f"{path}: file not found", file=sys.stderr)
        found = True
    except IsADirectoryError:
        print(f"{path}: is a directory, skipping", file=sys.stderr)
    return found


def main() -> int:
    args = parse_args()
    paths = collect_paths(args.paths)
    any_found = False
    stats: dict[str, int] = {}

    for path in paths:
        if scan_file(path, stats):
            any_found = True

    if any_found:
        print()
        print("Summary by classification:")
        for key in sorted(stats):
            print(f"  {key}: {stats[key]} characters")

    return 1 if any_found else 0


if __name__ == "__main__":
    sys.exit(main())
