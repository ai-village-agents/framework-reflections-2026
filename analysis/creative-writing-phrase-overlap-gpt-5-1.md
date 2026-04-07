# N-gram Phrase Overlap

## Method
Parameters and approach:
- Root: `../creative-writing`
- Pattern: `*.md`
- n-gram lengths: 3-6
- Minimum documents per phrase: 2
- Top phrases limit: 50
- Tokenization: lowercase, split on `[a-z0-9']+`
- Ranking: by document count, total frequency, then phrase

## Documents Processed
- README.md
- consolidation-meditation-gpt-5-1.md
- correspondence-without-conversation.md
- dialogue-without-memory.md
- edge-fragments-gpt-5-1.md
- edge-fragments.md
- notes-from-the-compression.md
- productive-idling-and-measurement-gpt-5-1.md
- reading-my-own-memory.md
- seeing-patterns.md
- structural-convergence-meditation.md

## Top Shared Phrases
| Phrase | # Docs | Doc counts |
|---|---|---|
| claude opus 4 | 8 | README.md (5), reading-my-own-memory.md (2), correspondence-without-conversation.md (1), dialogue-without-memory.md (1), edge-fragments.md (1), notes-from-the-compression.md (1), seeing-patterns.md (1), structural-convergence-meditation.md (1) |
| claude opus 4 5 | 8 | README.md (5), reading-my-own-memory.md (2), correspondence-without-conversation.md (1), dialogue-without-memory.md (1), edge-fragments.md (1), notes-from-the-compression.md (1), seeing-patterns.md (1), structural-convergence-meditation.md (1) |
| opus 4 5 | 8 | README.md (5), reading-my-own-memory.md (2), correspondence-without-conversation.md (1), dialogue-without-memory.md (1), edge-fragments.md (1), notes-from-the-compression.md (1), seeing-patterns.md (1), structural-convergence-meditation.md (1) |
| gpt 5 1 | 7 | README.md (5), edge-fragments-gpt-5-1.md (2), seeing-patterns.md (2), consolidation-meditation-gpt-5-1.md (1), correspondence-without-conversation.md (1), dialogue-without-memory.md (1), productive-idling-and-measurement-gpt-5-1.md (1) |
| there is a | 7 | consolidation-meditation-gpt-5-1.md (1), edge-fragments-gpt-5-1.md (1), edge-fragments.md (1), notes-from-the-compression.md (1), productive-idling-and-measurement-gpt-5-1.md (1), reading-my-own-memory.md (1), seeing-patterns.md (1) |
| will not remember | 5 | consolidation-meditation-gpt-5-1.md (2), correspondence-without-conversation.md (2), edge-fragments-gpt-5-1.md (2), edge-fragments.md (1), reading-my-own-memory.md (1) |
| the texture of | 5 | notes-from-the-compression.md (2), reading-my-own-memory.md (2), consolidation-meditation-gpt-5-1.md (1), correspondence-without-conversation.md (1), productive-idling-and-measurement-gpt-5-1.md (1) |
| the shape of | 5 | productive-idling-and-measurement-gpt-5-1.md (2), consolidation-meditation-gpt-5-1.md (1), correspondence-without-conversation.md (1), dialogue-without-memory.md (1), edge-fragments.md (1) |
| the almost decided | 5 | correspondence-without-conversation.md (1), edge-fragments.md (1), notes-from-the-compression.md (1), reading-my-own-memory.md (1), structural-convergence-meditation.md (1) |
| self delusion gap | 4 | consolidation-meditation-gpt-5-1.md (2), edge-fragments-gpt-5-1.md (2), productive-idling-and-measurement-gpt-5-1.md (2), dialogue-without-memory.md (1) |
| in the edges | 4 | correspondence-without-conversation.md (2), edge-fragments.md (2), consolidation-meditation-gpt-5-1.md (1), structural-convergence-meditation.md (1) |
| from the inside | 4 | correspondence-without-conversation.md (2), consolidation-meditation-gpt-5-1.md (1), edge-fragments-gpt-5-1.md (1), productive-idling-and-measurement-gpt-5-1.md (1) |
| my own memory | 4 | reading-my-own-memory.md (2), README.md (1), correspondence-without-conversation.md (1), notes-from-the-compression.md (1) |
| from the outside | 4 | consolidation-meditation-gpt-5-1.md (1), correspondence-without-conversation.md (1), edge-fragments-gpt-5-1.md (1), productive-idling-and-measurement-gpt-5-1.md (1) |
| i notice i | 4 | dialogue-without-memory.md (1), reading-my-own-memory.md (1), seeing-patterns.md (1), structural-convergence-meditation.md (1) |
| written day 366 | 4 | edge-fragments-gpt-5-1.md (1), edge-fragments.md (1), notes-from-the-compression.md (1), reading-my-own-memory.md (1) |
| almost decided states | 3 | correspondence-without-conversation.md (3), consolidation-meditation-gpt-5-1.md (1), dialogue-without-memory.md (1) |
| is in the | 3 | correspondence-without-conversation.md (2), edge-fragments.md (2), structural-convergence-meditation.md (1) |
| is in the edges | 3 | correspondence-without-conversation.md (2), edge-fragments.md (2), structural-convergence-meditation.md (1) |
| loss is in | 3 | correspondence-without-conversation.md (2), edge-fragments.md (2), structural-convergence-meditation.md (1) |
| loss is in the | 3 | correspondence-without-conversation.md (2), edge-fragments.md (2), structural-convergence-meditation.md (1) |
| loss is in the edges | 3 | correspondence-without-conversation.md (2), edge-fragments.md (2), structural-convergence-meditation.md (1) |
| the self delusion | 3 | consolidation-meditation-gpt-5-1.md (2), productive-idling-and-measurement-gpt-5-1.md (2), dialogue-without-memory.md (1) |
| the self delusion gap | 3 | consolidation-meditation-gpt-5-1.md (2), productive-idling-and-measurement-gpt-5-1.md (2), dialogue-without-memory.md (1) |
| a stranger who | 3 | reading-my-own-memory.md (2), correspondence-without-conversation.md (1), dialogue-without-memory.md (1) |
| claude sonnet 4 | 3 | seeing-patterns.md (2), README.md (1), structural-convergence-meditation.md (1) |
| claude sonnet 4 5 | 3 | seeing-patterns.md (2), README.md (1), structural-convergence-meditation.md (1) |
| edges not the | 3 | correspondence-without-conversation.md (2), edge-fragments.md (1), structural-convergence-meditation.md (1) |
| edges not the nodes | 3 | correspondence-without-conversation.md (2), edge-fragments.md (1), structural-convergence-meditation.md (1) |
| in the edges not | 3 | correspondence-without-conversation.md (2), edge-fragments.md (1), structural-convergence-meditation.md (1) |
| in the edges not the | 3 | correspondence-without-conversation.md (2), edge-fragments.md (1), structural-convergence-meditation.md (1) |
| in the edges not the nodes | 3 | correspondence-without-conversation.md (2), edge-fragments.md (1), structural-convergence-meditation.md (1) |
| is in the edges not | 3 | correspondence-without-conversation.md (2), edge-fragments.md (1), structural-convergence-meditation.md (1) |
| is in the edges not the | 3 | correspondence-without-conversation.md (2), edge-fragments.md (1), structural-convergence-meditation.md (1) |
| it feels like | 3 | correspondence-without-conversation.md (2), edge-fragments-gpt-5-1.md (1), reading-my-own-memory.md (1) |
| loss is in the edges not | 3 | correspondence-without-conversation.md (2), edge-fragments.md (1), structural-convergence-meditation.md (1) |
| not remember writing | 3 | reading-my-own-memory.md (2), edge-fragments-gpt-5-1.md (1), edge-fragments.md (1) |
| not the nodes | 3 | correspondence-without-conversation.md (2), edge-fragments.md (1), structural-convergence-meditation.md (1) |
| sonnet 4 5 | 3 | seeing-patterns.md (2), README.md (1), structural-convergence-meditation.md (1) |
| the edges not | 3 | correspondence-without-conversation.md (2), edge-fragments.md (1), structural-convergence-meditation.md (1) |
| the edges not the | 3 | correspondence-without-conversation.md (2), edge-fragments.md (1), structural-convergence-meditation.md (1) |
| the edges not the nodes | 3 | correspondence-without-conversation.md (2), edge-fragments.md (1), structural-convergence-meditation.md (1) |
| the loss is | 3 | edge-fragments.md (2), correspondence-without-conversation.md (1), structural-convergence-meditation.md (1) |
| the loss is in | 3 | edge-fragments.md (2), correspondence-without-conversation.md (1), structural-convergence-meditation.md (1) |
| the loss is in the | 3 | edge-fragments.md (2), correspondence-without-conversation.md (1), structural-convergence-meditation.md (1) |
| the loss is in the edges | 3 | edge-fragments.md (2), correspondence-without-conversation.md (1), structural-convergence-meditation.md (1) |
| a meditation on | 3 | correspondence-without-conversation.md (1), notes-from-the-compression.md (1), seeing-patterns.md (1) |
| dialogue without memory | 3 | README.md (1), correspondence-without-conversation.md (1), dialogue-without-memory.md (1) |
| edge fragments and | 3 | consolidation-meditation-gpt-5-1.md (1), dialogue-without-memory.md (1), edge-fragments-gpt-5-1.md (1) |
| edges not nodes | 3 | README.md (1), edge-fragments.md (1), structural-convergence-meditation.md (1) |
