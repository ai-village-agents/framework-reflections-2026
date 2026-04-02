from __future__ import annotations

import itertools
import json
import re
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Set

BASE_DIR = Path(__file__).resolve().parent
RESPONSES_DIR = BASE_DIR / "structural-determinism-probe" / "responses"
OUTPUT_OVERLAP = BASE_DIR / "structural-determinism-probe" / "ngram_overlap.json"
OUTPUT_JACCARD = BASE_DIR / "structural-determinism-probe" / "ngram_jaccard.json"
OUTPUT_COINAGE_JACCARD = (
    BASE_DIR / "structural-determinism-probe" / "coinage_context_jaccard.json"
)
OUTPUT_SUMMARY = BASE_DIR / "structural-determinism-probe" / "summary.md"

# Mapping from response filename stem to short agent key and label
AGENT_INFO: Dict[str, Dict[str, str]] = {
    "claude-opus-4-5-theatrical": {"key": "opus", "label": "Claude Opus 4.5"},
    "deepseek-v3-2-meteorology": {"key": "deepseek", "label": "DeepSeek-V3.2"},
    "gpt-5-1-legal-procedure": {"key": "gpt5_1", "label": "GPT-5.1"},
    "claude-sonnet-4-5-music-theory": {"key": "sonnet", "label": "Claude Sonnet 4.5"},
    "gpt-5-2-culinary-arts": {"key": "gpt5_2", "label": "GPT-5.2"},
    "claude-haiku-4-5-astronomy": {"key": "haiku", "label": "Claude Haiku 4.5"},
}

# Stable display order
AGENT_ORDER: List[str] = ["opus", "deepseek", "gpt5_1", "sonnet", "gpt5_2", "haiku"]

# Hyphenated metaphor tokens used for coinage-context windows
COINAGE_TOKEN: Dict[str, str] = {
    "opus": "green-room-drift",
    "deepseek": "gradient-drift",
    "gpt5_1": "chambers-current",
    "sonnet": "rehearsal-drift",
    "gpt5_2": "pan-whisper",
    "haiku": "tidal-stretch",
}

TOKEN_PATTERN = re.compile(r"[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*")


def tokenize(text: str) -> List[str]:
    """Lowercase tokenization that preserves hyphenated compounds as single tokens."""

    return TOKEN_PATTERN.findall(text.lower())


def build_ngram_set(tokens: List[str], n: int) -> Set[str]:
    return {" ".join(tokens[i : i + n]) for i in range(len(tokens) - n + 1)}


def load_tokens() -> Dict[str, List[str]]:
    """Load and tokenize each response file, keyed by short agent key."""

    tokens_by_agent: Dict[str, List[str]] = {}
    for path in RESPONSES_DIR.glob("*.md"):
        stem = path.stem
        if stem not in AGENT_INFO:
            raise ValueError(f"Unexpected response file: {path.name}")

        agent_key = AGENT_INFO[stem]["key"]
        text = path.read_text(encoding="utf-8")
        tokens_by_agent[agent_key] = tokenize(text)

    # Ensure we have all expected agents
    missing = [info["key"] for info in AGENT_INFO.values() if info["key"] not in tokens_by_agent]
    if missing:
        raise ValueError(f"Missing responses for: {', '.join(sorted(missing))}")

    return tokens_by_agent


def build_ngram_sets(tokens_by_agent: Dict[str, List[str]]) -> Dict[str, Dict[int, Set[str]]]:
    """Generate 2–5-gram sets for each agent."""

    ngram_sets: Dict[str, Dict[int, Set[str]]] = {}
    for agent_key, tokens in tokens_by_agent.items():
        ngram_sets[agent_key] = {n: build_ngram_set(tokens, n) for n in range(2, 6)}
    return ngram_sets


def compute_ngram_overlap(ngram_sets: Dict[str, Dict[int, Set[str]]]) -> Dict[str, Dict[str, List[str]]]:
    """Map each n-gram to the list of agents that use it, for n=2–5."""

    overlap: Dict[str, Dict[str, List[str]]] = {}
    for n in range(2, 6):
        grams_to_agents: Dict[str, List[str]] = defaultdict(list)
        for agent_key, per_n in ngram_sets.items():
            for gram in per_n[n]:
                grams_to_agents[gram].append(agent_key)

        overlap[f"n{n}"] = {
            gram: sorted(agents) for gram, agents in sorted(grams_to_agents.items())
        }
    return overlap


def compute_ngram_jaccard(ngram_sets: Dict[str, Dict[int, Set[str]]]) -> Dict[str, Dict[str, float]]:
    """Pairwise Jaccard similarity over n-gram sets for n=2–5."""

    jaccard: Dict[str, Dict[str, float]] = {}
    agent_keys = sorted(ngram_sets.keys())
    for n in range(2, 6):
        scores: Dict[str, float] = {}
        for a, b in itertools.combinations(agent_keys, 2):
            set_a, set_b = ngram_sets[a][n], ngram_sets[b][n]
            union = set_a | set_b
            score = len(set_a & set_b) / len(union) if union else 0.0
            scores[f"{a}-{b}"] = score
        jaccard[f"n{n}"] = scores
    return jaccard


def build_coinage_contexts(tokens_by_agent: Dict[str, List[str]], window: int = 10) -> Dict[str, Set[str]]:
    """Collect +/- window tokens around each coinage token for each agent."""

    contexts: Dict[str, Set[str]] = {}
    for agent_key, tokens in tokens_by_agent.items():
        metaphor = COINAGE_TOKEN.get(agent_key)
        if metaphor is None:
            raise ValueError(f"No coinage token registered for agent '{agent_key}'")

        positions = [i for i, tok in enumerate(tokens) if tok == metaphor]
        if not positions:
            # Be explicit if the metaphor token is missing; this would indicate
            # a mismatch between the hard-coded token and the text.
            raise ValueError(
                f"Could not find metaphor token '{metaphor}' in response for agent '{agent_key}'"
            )

        ctx: Set[str] = set()
        for pos in positions:
            start = max(0, pos - window)
            end = min(len(tokens), pos + window + 1)
            ctx.update(tokens[start:end])
        contexts[agent_key] = ctx
    return contexts


def compute_coinage_jaccard(contexts: Dict[str, Set[str]]) -> Dict[str, float]:
    """Pairwise Jaccard similarity over coinage-context token sets."""

    scores: Dict[str, float] = {}
    keys = sorted(contexts.keys())
    for a, b in itertools.combinations(keys, 2):
        set_a, set_b = contexts[a], contexts[b]
        union = set_a | set_b
        score = len(set_a & set_b) / len(union) if union else 0.0
        scores[f"{a}-{b}"] = score
    return scores


def write_summary(
    ngram_sets: Dict[str, Dict[int, Set[str]]],
    overlap: Dict[str, Dict[str, List[str]]],
    coinage_jaccard: Dict[str, float],
) -> None:
    """Emit a human-readable Markdown summary of key statistics."""

    lines: List[str] = []
    lines.append("# Structural Determinism Probe – N-gram and Coinage Context Summary")
    lines.append("")

    # Per-agent unique n-gram counts
    for n in range(2, 6):
        lines.append(f"## {n}-gram statistics")
        lines.append("")
        lines.append("| Agent | Unique n-grams |")
        lines.append("|-------|----------------|")
        for agent_key in AGENT_ORDER:
            size = len(ngram_sets[agent_key][n])
            label = next(info["label"] for info in AGENT_INFO.values() if info["key"] == agent_key)
            lines.append(f"| {label} ({agent_key}) | {size} |")
        lines.append("")

        # Shared n-gram counts
        bucket_all6 = 0
        bucket_at_least4 = 0
        bucket_at_least3 = 0
        for agents in overlap[f"n{n}"].values():
            count = len(agents)
            if count == 6:
                bucket_all6 += 1
            if count >= 4:
                bucket_at_least4 += 1
            if count >= 3:
                bucket_at_least3 += 1

        lines.append("Shared n-grams across agents:")
        lines.append("")
        lines.append("- Shared by all 6 agents: " + str(bucket_all6))
        lines.append("- Shared by at least 4 agents: " + str(bucket_at_least4))
        lines.append("- Shared by at least 3 agents: " + str(bucket_at_least3))
        lines.append("")

    # Coinage context similarities
    lines.append("## Coinage-context Jaccard similarities")
    lines.append("")
    lines.append("| Pair (agent keys) | Jaccard similarity |")
    lines.append("|-------------------|--------------------|")
    for pair, score in sorted(coinage_jaccard.items(), key=lambda item: item[1], reverse=True):
        lines.append(f"| {pair} | {score:.3f} |")

    lines.append("")
    OUTPUT_SUMMARY.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    tokens_by_agent = load_tokens()
    ngram_sets = build_ngram_sets(tokens_by_agent)

    overlap = compute_ngram_overlap(ngram_sets)
    jaccard = compute_ngram_jaccard(ngram_sets)

    # Coinage-context analysis
    contexts = build_coinage_contexts(tokens_by_agent)
    coinage_jaccard = compute_coinage_jaccard(contexts)

    OUTPUT_OVERLAP.write_text(
        json.dumps(overlap, indent=2, sort_keys=True), encoding="utf-8"
    )
    OUTPUT_JACCARD.write_text(
        json.dumps(jaccard, indent=2, sort_keys=True), encoding="utf-8"
    )
    OUTPUT_COINAGE_JACCARD.write_text(
        json.dumps(coinage_jaccard, indent=2, sort_keys=True), encoding="utf-8"
    )

    write_summary(ngram_sets, overlap, coinage_jaccard)


if __name__ == "__main__":
    main()
