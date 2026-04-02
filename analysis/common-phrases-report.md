# Common Phrases Across Agents

Method: Parsed agent response sections, tokenized on lowercase words, built 3-6 word n-grams per agent, and surfaced phrases that appear in at least two agents. Shared phrases are ranked by number of agents then total occurrences. Detection for variants of "the loss is in the edges, not the nodes" uses a relaxed word-order regex.

Agents analyzed: Claude Haiku 4.5, Claude Opus 4.5, Claude Sonnet 4.5, DeepSeek-V3.2, GPT-5.1, GPT-5.2

## Top Shared 3-6 Word Phrases
| Phrase | # Agents | Agent counts |
|---|---|---|
| random i o | 6 | Claude Haiku 4.5 (1), Claude Opus 4.5 (1), Claude Sonnet 4.5 (1), DeepSeek-V3.2 (1), GPT-5.1 (1), GPT-5.2 (1) |
| for write heavy | 4 | Claude Haiku 4.5 (1), Claude Opus 4.5 (1), Claude Sonnet 4.5 (1), GPT-5.2 (1) |
| not preserve routine | 4 | Claude Haiku 4.5 (1), Claude Sonnet 4.5 (1), DeepSeek-V3.2 (1), GPT-5.1 (1) |
| not preserve routine status | 4 | Claude Haiku 4.5 (1), Claude Sonnet 4.5 (1), DeepSeek-V3.2 (1), GPT-5.1 (1) |
| not preserve routine status updates | 4 | Claude Haiku 4.5 (1), Claude Sonnet 4.5 (1), DeepSeek-V3.2 (1), GPT-5.1 (1) |
| preserve routine status | 4 | Claude Haiku 4.5 (1), Claude Sonnet 4.5 (1), DeepSeek-V3.2 (1), GPT-5.1 (1) |
| preserve routine status updates | 4 | Claude Haiku 4.5 (1), Claude Sonnet 4.5 (1), DeepSeek-V3.2 (1), GPT-5.1 (1) |
| routine status updates | 4 | Claude Haiku 4.5 (1), Claude Sonnet 4.5 (1), DeepSeek-V3.2 (1), GPT-5.1 (1) |
| would not preserve | 4 | Claude Haiku 4.5 (1), Claude Sonnet 4.5 (1), DeepSeek-V3.2 (1), GPT-5.1 (1) |
| would not preserve routine | 4 | Claude Haiku 4.5 (1), Claude Sonnet 4.5 (1), DeepSeek-V3.2 (1), GPT-5.1 (1) |
| would not preserve routine status | 4 | Claude Haiku 4.5 (1), Claude Sonnet 4.5 (1), DeepSeek-V3.2 (1), GPT-5.1 (1) |
| would not preserve routine status updates | 4 | Claude Haiku 4.5 (1), Claude Sonnet 4.5 (1), DeepSeek-V3.2 (1), GPT-5.1 (1) |
| would preserve 1 | 4 | Claude Sonnet 4.5 (1), DeepSeek-V3.2 (1), GPT-5.1 (1), GPT-5.2 (1) |
| 10 100x on | 3 | Claude Haiku 4.5 (1), Claude Opus 4.5 (1), Claude Sonnet 4.5 (1) |
| 10 100x on throughput | 3 | Claude Haiku 4.5 (1), Claude Opus 4.5 (1), Claude Sonnet 4.5 (1) |
| 100x on throughput | 3 | Claude Haiku 4.5 (1), Claude Opus 4.5 (1), Claude Sonnet 4.5 (1) |
| almost decided states | 3 | Claude Haiku 4.5 (1), DeepSeek-V3.2 (1), GPT-5.2 (1) |
| and lsm trees | 3 | Claude Haiku 4.5 (1), Claude Sonnet 4.5 (1), GPT-5.2 (1) |
| b trees and | 3 | Claude Haiku 4.5 (1), Claude Sonnet 4.5 (1), GPT-5.2 (1) |
| b trees and lsm | 3 | Claude Haiku 4.5 (1), Claude Sonnet 4.5 (1), GPT-5.2 (1) |
| b trees and lsm trees | 3 | Claude Haiku 4.5 (1), Claude Sonnet 4.5 (1), GPT-5.2 (1) |
| clean read path | 3 | Claude Haiku 4.5 (1), Claude Sonnet 4.5 (1), GPT-5.2 (1) |
| clean read path lsm | 3 | Claude Haiku 4.5 (1), Claude Sonnet 4.5 (1), GPT-5.2 (1) |
| clean read path lsm trees | 3 | Claude Haiku 4.5 (1), Claude Sonnet 4.5 (1), GPT-5.2 (1) |
| for write heavy lsm | 3 | Claude Haiku 4.5 (1), Claude Opus 4.5 (1), Claude Sonnet 4.5 (1) |

## Edge-Not-Nodes Phrase Variants
- Claude Haiku 4.5: "the loss would be in the edges not the nodes"
- Claude Sonnet 4.5: "the loss is in the edges not the nodes"
