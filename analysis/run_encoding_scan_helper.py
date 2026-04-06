"""Thin helper to run the non-ASCII scanner with a friendlier summary.

Usage:
    python3 analysis/run_encoding_scan_helper.py PATH [PATH...]

This simply delegates to analysis/check_non_ascii_chars.py but
adds a short human-oriented header describing what the classifications
mean in the context of BIRCH v0.3 spec review.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run the non-ASCII scanner and print a short explanation of "
            "risk classifications (hyphen/quote/space URL risks vs other Unicode)."
        )
    )
    parser.add_argument(
        "paths",
        nargs="+",
        help="Files to scan (e.g., BIRCH specs or diffs).",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    print("[encoding-scan] Using analysis/check_non_ascii_chars.py")
    print("[encoding-scan] Classifications: HYPHEN_OR_MINUS_URL_RISK, "
          "QUOTE_OR_APOSTROPHE_URL_RISK, SPACE_OR_JOINER_URL_RISK, OTHER_NON_ASCII")
    print("[encoding-scan] URL/anchor breakage risk mostly lives in the first three classes; "
          "OTHER_NON_ASCII is often math/typography.")
    print()

    script = ROOT / "analysis" / "check_non_ascii_chars.py"
    cmd = [sys.executable, str(script), *args.paths]
    try:
        return subprocess.call(cmd)
    except FileNotFoundError:
        print(f"Could not find scanner at {script}", file=sys.stderr)
        return 1


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
