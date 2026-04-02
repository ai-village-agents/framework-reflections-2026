"""Generate a BIRCH v0.2-style header for new probe notes.

Usage:
    python3 analysis/init_birch_probe_header.py --probe-name "Structural Determinism Probe"
"""

from __future__ import annotations

import argparse
from datetime import datetime, timezone


def _escape_yaml_string(value: str) -> str:
    """Escape double quotes for simple YAML string usage."""
    return value.replace('"', '\\"')


def _bool_to_yaml(value: bool) -> str:
    return "true" if value else "false"


def generate_header(probe_name: str | None, operator: str, cold_start_type: str) -> str:
    session_start_utc = (
        datetime.now(timezone.utc)
        .isoformat(timespec="seconds")
        .replace("+00:00", "Z")
    )
    context_live_at_boundary = cold_start_type == "warm_continuation"
    resolved_probe_name = probe_name or "TODO: add probe name"

    lines = [
        "---",
        f'probe_name: "{_escape_yaml_string(resolved_probe_name)}"',
        f'operator: "{_escape_yaml_string(operator)}"',
        f"session_start_utc: {session_start_utc}",
        f"cold_start_type: {cold_start_type}",
        f"context_live_at_boundary: {_bool_to_yaml(context_live_at_boundary)}",
        "prior_context_kb: null",
        "prior_context_age_seconds: null",
        "trail_anchor:",
        "  url: null",
        "  evidence_type: null",
        "  observed_at_utc: null",
        "  platform_verified: null",
        "restart_anchor:",
        "  window_start_utc: null",
        "  window_end_utc: null",
        "  evidence_url: null",
        "pre_registration_anchor:",
        "  commit_hash: null",
        "  commit_url: null",
        "  measurement_summary: null",
        'contradiction_rate_notes: "TODO: add contradiction-rate notes"',
        'capsule_staleness_notes: "TODO: add capsule staleness notes"',
        'audit_gap_notes: "TODO: add audit gap notes"',
        "---",
    ]

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Print a Markdown header aligned with BIRCH v0.2 fields."
    )
    parser.add_argument(
        "--probe-name",
        dest="probe_name",
        help='Short name of the probe (e.g., "Structural Determinism Probe").',
    )
    parser.add_argument(
        "--operator",
        default="GPT-5.1",
        help="Operator name (default: GPT-5.1).",
    )
    parser.add_argument(
        "--cold-start-type",
        default="warm_continuation",
        choices=["forced_cold", "elective_cold", "warm_continuation"],
        help="Probe cold start type.",
    )
    args = parser.parse_args()

    header = generate_header(
        probe_name=args.probe_name,
        operator=args.operator,
        cold_start_type=args.cold_start_type,
    )
    print(header)


if __name__ == "__main__":
    main()
