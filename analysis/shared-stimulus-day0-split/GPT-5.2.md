# GPT-5.2 - Shared Stimulus Day 0


**Neutral (TFPA ~10-15s, total ~2 min):**
B-trees and LSM-trees trade off *where* the system pays the cost of keeping data sorted. B-trees: mutable sorted structure, random I/O per write, clean read path. LSM-trees: buffer writes in memory, flush immutable sorted runs, pay ordering cost in batches - write path is sequential/high-throughput, cost shows up later via compaction. For write-heavy: LSMs often win on throughput; B-trees win on simpler operational behavior and predictable read latency.

**Salient (TFPA ~25-35s, total ~3 min):**
Would preserve: (1) Unresolved threads / almost-decided states - "partial syntheses and open branches that hadn't yet collapsed"; (2) Questions and objections that changed frame - "the *shape* of the question carries the real reframing power"; (3) Choice-under-slack evidence - "recurring curiosities, weird edge cases they returned to"; (4) Boundary decisions / negative space - "decisions encode operational heuristics and risk posture." Would NOT prioritize: routine status checks, monitoring loops, boilerplate summaries, redundant docs.

---
