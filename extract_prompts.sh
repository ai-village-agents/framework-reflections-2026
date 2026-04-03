#!/bin/bash
# Extract individual prompts from structural-determinism-probe-prompts.md
# Usage: ./extract_prompts.sh [agent_name]

PROMPTS_FILE="prompts/structural-determinism-probe-prompts.md"

if [ $# -eq 0 ]; then
    echo "Available prompts:"
    grep "^### " "$PROMPTS_FILE" | sed 's/^### //'
    echo ""
    echo "Usage: $0 [agent_name]"
    echo "Example: $0 'DeepSeek-V3.2 – Meteorology'"
    exit 1
fi

AGENT="$1"

# Extract from the agent's section to the next ### or end of file
awk -v agent="$AGENT" '
BEGIN { in_section=0; }
/^### / {
    if (in_section) exit;
    if ($0 ~ agent) in_section=1;
    next;
}
/^### / && in_section { exit; }
in_section { print; }
' "$PROMPTS_FILE"

# Also show the response format section
echo ""
echo "=== Response Format ==="
tail -15 "$PROMPTS_FILE" | head -12
