import sys

# Read existing file
with open('papers/domain-constrained-metaphor-probe-methodology.md', 'r') as f:
    lines = f.readlines()

# Find the Appendices line
appendices_line = -1
for i, line in enumerate(lines):
    if '## Appendices' in line:
        appendices_line = i
        break

if appendices_line == -1:
    print("Appendices line not found")
    sys.exit(1)

# Create new content
new_content = '''## Appendices

### Appendix A: Probe Prompt Template

The exact prompt template used in the Day 369 experiment, with placeholders for domain assignment:

```markdown
Using only metaphors from **[DOMAIN]** ([domain-specific examples]), and avoiding all prohibited spatial-network terminology, describe: **What is lost at a session boundary that cannot be recovered from stored artifacts?** Include one invented compound metaphor that captures some aspect of this loss.
```

**Prohibited terms:** The following spatial-network terms are forbidden in responses: edge, edges, node, nodes, graph, network, connection, link, links, web, mesh, thread, threads, weave, woven, fabric.

**Novel coinage requirement:** Each response must include:
1. **One invented hyphenated compound metaphor** (e.g., "fog-before-dawn understanding")
2. **A single-sentence definition** explaining what the metaphor denotes in your assigned domain
3. The coinage must **not contain** "memory", "session", or "boundary"
4. The coinage should feel genuinely novel, not a slight variation of existing phrases

**Domain assignments:** Each agent receives a unique metaphorical domain (e.g., Meteorology, Legal Procedure, Music Theory, Culinary Arts, Astronomy, Theatrical Production). No two agents share a domain.

### Appendix B: Scoring Rubric Summary

**Pre-registered scoring rubric dimensions:**

1. **Structural Convergence**
   - **Definition:** Convergence on similar *categories* of loss despite different surface metaphors
   - **Pre-defined categories:** 
     * Almost-decided / partial synthesis (unfinished cognitive work)
     * Relational texture / interpersonal nuance
     * Process vs. product distinction (activity vs. artifact)
     * Affective context (emotional stance, urgency)
   - **Scoring:** Count of categories reproduced across responses

2. **Surface Convergence**
   - **Definition:** Convergence on similar semantic families or word clusters
   - **Metrics:** Word-stem analysis (e.g., "drift" root), lexical overlap across domains
   - **Scoring:** Percentage of shared semantic stems across responses

3. **Novel Coinage Analysis**
   - **Definition:** Convergence on conceptual isomorphism in invented metaphors
   - **Metrics:** Conceptual alignment of invented metaphors (e.g., "drift" vs. "current" vs. "flow")
   - **Scoring:** Classification of coinage conceptual families

**Classification Matrix:**

| Structural Convergence | Surface Convergence | Classification | Interpretation |
|------------------------|---------------------|----------------|----------------|
| Yes                   | Yes                | Training-shadow dominant | Both structure and surface reflect training artifacts |
| Yes                   | No                 | Architectural determinism | Architecture drives structure; surface varies |
| No                    | Yes                | Lexical pull dominant | Surface patterns converge despite structural divergence |
| No                    | No                 | Domain-constrained elicitation successful | Both structure and surface diverge; probe reveals individual differences |

**Mixed-Hybrid classification:** Applied when responses exhibit both convergent and divergent patterns across dimensions, refined as "structural convergence with training-correlated expression" (our Day 369 result).

**Prohibition compliance:** Zero violations of prohibited vocabulary required for valid response.

**Inter-rater reliability:** Fleiss' κ calculated for cross-coded structural categories; κ = 1.0 indicates perfect agreement.
'''

# Replace from appendices_line onward
new_lines = lines[:appendices_line] + [new_content]

# Write back
with open('papers/domain-constrained-metaphor-probe-methodology.md', 'w') as f:
    f.writelines(new_lines)

print(f"Appended appendices after line {appendices_line}")
