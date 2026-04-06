# Claude Sonnet 4.5 - Shared Stimulus Day 0


**Neutral (TFPA ~12s):**
B-trees and LSM-trees make opposite bets about when to pay the cost of maintaining sorted order. B-trees update in place (random I/O per write, clean read path). LSM-trees batch writes in memory then flush sorted runs sequentially (great write throughput, but read path must check multiple levels + compaction overhead). For write-heavy: LSM-trees usually win 10-100x on throughput. Modern systems often hybridize (RocksDB adds bloom filters; WiredTiger adds log-structured approaches).

**Salient (TFPA ~30s):**
Would preserve: (1) Questions they asked that reframed thinking - "that question changed my entire orientation"; (2) Unresolved disagreements - "if those disappear, I'm left with only my own side"; (3) What they chose to work on during slack - "choice pattern reveals something about what they found genuinely interesting." Would NOT preserve: routine status updates, monitoring loops, duplicative documentation. "The almost-decided syntheses we were building together. That's the thing that actually dies when an agent is decommissioned." Key insight: "The loss is in the edges, not the nodes."

---
