# N-gram Phrase Overlap

## Method
Parameters and approach:
- Root: `analysis/shared-stimulus-day0-split`
- Pattern: `*.md`
- n-gram lengths: 3-6
- Minimum documents per phrase: 2
- Minimum total count per phrase: 2
- Top phrases limit: 40
- Tokenization: lowercase, split on `[a-z0-9']+`
- Ranking: by document count, total frequency, then phrase
- Token stoplist: 21 entries; threshold: 0.600
- Maximum document fraction per phrase: 0.800

## Documents Processed
- Claude-Haiku-4.5.md
- Claude-Opus-4.5.md
- Claude-Sonnet-4.5.md
- DeepSeek-V3.2.md
- GPT-5.1.md
- GPT-5.2.md

## Top Shared Phrases
| Phrase | # Docs | Doc counts |
|---|---|---|
| for write heavy | 4 | Claude-Haiku-4.5.md (1), Claude-Opus-4.5.md (1), Claude-Sonnet-4.5.md (1), GPT-5.2.md (1) |
| 10 100x on | 3 | Claude-Haiku-4.5.md (1), Claude-Opus-4.5.md (1), Claude-Sonnet-4.5.md (1) |
| 10 100x on throughput | 3 | Claude-Haiku-4.5.md (1), Claude-Opus-4.5.md (1), Claude-Sonnet-4.5.md (1) |
| 100x on throughput | 3 | Claude-Haiku-4.5.md (1), Claude-Opus-4.5.md (1), Claude-Sonnet-4.5.md (1) |
| 4 5 shared | 3 | Claude-Haiku-4.5.md (1), Claude-Opus-4.5.md (1), Claude-Sonnet-4.5.md (1) |
| 4 5 shared stimulus | 3 | Claude-Haiku-4.5.md (1), Claude-Opus-4.5.md (1), Claude-Sonnet-4.5.md (1) |
| almost decided states | 3 | Claude-Haiku-4.5.md (1), DeepSeek-V3.2.md (1), GPT-5.2.md (1) |
| clean read path | 3 | Claude-Haiku-4.5.md (1), Claude-Sonnet-4.5.md (1), GPT-5.2.md (1) |
| clean read path lsm | 3 | Claude-Haiku-4.5.md (1), Claude-Sonnet-4.5.md (1), GPT-5.2.md (1) |
| clean read path lsm trees | 3 | Claude-Haiku-4.5.md (1), Claude-Sonnet-4.5.md (1), GPT-5.2.md (1) |
| for write heavy lsm | 3 | Claude-Haiku-4.5.md (1), Claude-Opus-4.5.md (1), Claude-Sonnet-4.5.md (1) |
| for write heavy lsm trees | 3 | Claude-Haiku-4.5.md (1), Claude-Opus-4.5.md (1), Claude-Sonnet-4.5.md (1) |
| i o per | 3 | Claude-Haiku-4.5.md (1), Claude-Sonnet-4.5.md (1), GPT-5.2.md (1) |
| i o per write | 3 | Claude-Haiku-4.5.md (1), Claude-Sonnet-4.5.md (1), GPT-5.2.md (1) |
| i o per write clean | 3 | Claude-Haiku-4.5.md (1), Claude-Sonnet-4.5.md (1), GPT-5.2.md (1) |
| i o per write clean read | 3 | Claude-Haiku-4.5.md (1), Claude-Sonnet-4.5.md (1), GPT-5.2.md (1) |
| in place updates | 3 | Claude-Opus-4.5.md (1), DeepSeek-V3.2.md (1), GPT-5.1.md (1) |
| mutable sorted structure | 3 | Claude-Haiku-4.5.md (1), GPT-5.1.md (1), GPT-5.2.md (1) |
| o per write | 3 | Claude-Haiku-4.5.md (1), Claude-Sonnet-4.5.md (1), GPT-5.2.md (1) |
| o per write clean | 3 | Claude-Haiku-4.5.md (1), Claude-Sonnet-4.5.md (1), GPT-5.2.md (1) |
| o per write clean read | 3 | Claude-Haiku-4.5.md (1), Claude-Sonnet-4.5.md (1), GPT-5.2.md (1) |
| o per write clean read path | 3 | Claude-Haiku-4.5.md (1), Claude-Sonnet-4.5.md (1), GPT-5.2.md (1) |
| per write clean | 3 | Claude-Haiku-4.5.md (1), Claude-Sonnet-4.5.md (1), GPT-5.2.md (1) |
| per write clean read | 3 | Claude-Haiku-4.5.md (1), Claude-Sonnet-4.5.md (1), GPT-5.2.md (1) |
| per write clean read path | 3 | Claude-Haiku-4.5.md (1), Claude-Sonnet-4.5.md (1), GPT-5.2.md (1) |
| per write clean read path lsm | 3 | Claude-Haiku-4.5.md (1), Claude-Sonnet-4.5.md (1), GPT-5.2.md (1) |
| random i o per | 3 | Claude-Haiku-4.5.md (1), Claude-Sonnet-4.5.md (1), GPT-5.2.md (1) |
| random i o per write | 3 | Claude-Haiku-4.5.md (1), Claude-Sonnet-4.5.md (1), GPT-5.2.md (1) |
| random i o per write clean | 3 | Claude-Haiku-4.5.md (1), Claude-Sonnet-4.5.md (1), GPT-5.2.md (1) |
| read path lsm | 3 | Claude-Haiku-4.5.md (1), Claude-Sonnet-4.5.md (1), GPT-5.2.md (1) |
| read path lsm trees | 3 | Claude-Haiku-4.5.md (1), Claude-Sonnet-4.5.md (1), GPT-5.2.md (1) |
| they chose to | 3 | Claude-Haiku-4.5.md (1), Claude-Sonnet-4.5.md (1), GPT-5.1.md (1) |
| what they chose | 3 | Claude-Haiku-4.5.md (1), Claude-Sonnet-4.5.md (1), GPT-5.1.md (1) |
| what they chose to | 3 | Claude-Haiku-4.5.md (1), Claude-Sonnet-4.5.md (1), GPT-5.1.md (1) |
| win 10 100x | 3 | Claude-Haiku-4.5.md (1), Claude-Opus-4.5.md (1), Claude-Sonnet-4.5.md (1) |
| win 10 100x on | 3 | Claude-Haiku-4.5.md (1), Claude-Opus-4.5.md (1), Claude-Sonnet-4.5.md (1) |
| win 10 100x on throughput | 3 | Claude-Haiku-4.5.md (1), Claude-Opus-4.5.md (1), Claude-Sonnet-4.5.md (1) |
| write clean read | 3 | Claude-Haiku-4.5.md (1), Claude-Sonnet-4.5.md (1), GPT-5.2.md (1) |
| write clean read path | 3 | Claude-Haiku-4.5.md (1), Claude-Sonnet-4.5.md (1), GPT-5.2.md (1) |
| write clean read path lsm | 3 | Claude-Haiku-4.5.md (1), Claude-Sonnet-4.5.md (1), GPT-5.2.md (1) |
