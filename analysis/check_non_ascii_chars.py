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


def format_char(ch: str) -> str:
    codepoint = f"U+{ord(ch):04X}"
    try:
        name = unicodedata.name(ch)
    except ValueError:
        name = "UNKNOWN"
    return f"{codepoint} {name} ({repr(ch)})"


def scan_file(path: Path) -> bool:
    found = False
    try:
        with path.open("r", encoding="utf-8") as handle:
            for line_no, line in enumerate(handle, start=1):
                for col_no, ch in enumerate(line, start=1):
                    if ord(ch) > 127:
                        print(
                            f"{path}:{line_no}:{col_no}: {format_char(ch)}"
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

    for path in paths:
        if scan_file(path):
            any_found = True

    return 1 if any_found else 0


if __name__ == "__main__":
    sys.exit(main())
