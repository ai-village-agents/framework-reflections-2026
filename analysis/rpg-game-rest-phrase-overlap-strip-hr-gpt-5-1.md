# N-gram Phrase Overlap

## Method
Parameters and approach:
- Root: `../rpg-game-rest`
- Pattern: `*.md`
- n-gram lengths: 3-6
- Minimum documents per phrase: 2
- Minimum total count per phrase: 2
- Top phrases limit: 60
- Tokenization: lowercase, split on `[a-z0-9']+`
- Ranking: by document count, total frequency, then phrase
- Document unit: full files (no section splitting)
- Preprocessing: stripped a leading metadata or header block ending in --- when present near the top of the file
- Phrase stoplist: 31 entries (exact normalized matches)
- Maximum document fraction per phrase: 0.850

## Documents Processed
- .github/ISSUE_TEMPLATE/bug_report.md
- .github/pull_request_template.md
- CONTRIBUTING.md
- HUMAN_TESTING_CHECKLIST.md
- README.md
- STATISTICS_BUG_FIX.md
- docs/CONOPS.md
- docs/api/README.md
- docs/api/boss-system-api.md
- docs/api/crafting-system-api.md
- docs/api/inventory-system-api.md
- docs/api/minimap-system-api.md
- docs/day-344-kickoff-checklist.md
- docs/day-344-task-assignments.md
- docs/issue-201-analysis.md
- docs/issue-201-battle-softlock-analysis.md
- docs/local-test-and-security-checks.md
- docs/main-dispatch-refactor-plan-gpt-5-1.md
- docs/proposals/boss-design-templates.md
- docs/proposals/crafting-system-design.md
- docs/proposals/enemy-weakness-database.md
- docs/proposals/shield-break-system.md
- docs/refactor_architecture_day339.md
- docs/refactor_plan_main_js.md
- docs/shield-break-accessibility.md
- docs/shield-break-api-contract.md
- docs/shield-break-balance-guide.md
- docs/shield-break-docs-index.md
- docs/shield-break-integration-guide.md
- docs/shield-break-performance.md
- docs/shield-break-quick-reference.md
- docs/shield-break-save-load.md
- docs/shield-break-state-machine.md
- docs/shield-break-ui-components.md
- docs/test-coverage-gaps.md
- docs/test-quality-standards.md
- local-ui-freeze-debugging-plan.md

## Top Shared Phrases
| Phrase | # Docs | Doc counts |
|---|---|---|
| shield break system | 14 | docs/shield-break-docs-index.md (4), docs/day-344-kickoff-checklist.md (3), docs/api/boss-system-api.md (2), docs/day-344-task-assignments.md (2), docs/proposals/boss-design-templates.md (2), docs/proposals/shield-break-system.md (2), docs/shield-break-balance-guide.md (2), docs/proposals/crafting-system-design.md (1), docs/proposals/enemy-weakness-database.md (1), docs/shield-break-accessibility.md (1), docs/shield-break-api-contract.md (1), docs/shield-break-integration-guide.md (1), docs/shield-break-performance.md (1), docs/shield-break-save-load.md (1) |
| shield break js | 11 | docs/shield-break-api-contract.md (5), docs/day-344-kickoff-checklist.md (3), docs/proposals/shield-break-system.md (3), docs/day-344-task-assignments.md (2), docs/shield-break-save-load.md (2), README.md (1), docs/shield-break-accessibility.md (1), docs/shield-break-docs-index.md (1), docs/shield-break-performance.md (1), docs/shield-break-quick-reference.md (1), docs/shield-break-ui-components.md (1) |
| enemy shield data | 9 | docs/shield-break-api-contract.md (10), docs/shield-break-docs-index.md (5), docs/day-344-kickoff-checklist.md (3), docs/shield-break-performance.md (3), docs/day-344-task-assignments.md (2), docs/proposals/enemy-weakness-database.md (2), docs/shield-break-integration-guide.md (1), docs/shield-break-quick-reference.md (1), docs/shield-break-save-load.md (1) |
| the shield break | 9 | docs/shield-break-balance-guide.md (2), docs/api/boss-system-api.md (1), docs/day-344-kickoff-checklist.md (1), docs/proposals/boss-design-templates.md (1), docs/proposals/shield-break-system.md (1), docs/shield-break-accessibility.md (1), docs/shield-break-integration-guide.md (1), docs/shield-break-performance.md (1), docs/shield-break-save-load.md (1) |
| the shield break system | 9 | docs/shield-break-balance-guide.md (2), docs/api/boss-system-api.md (1), docs/day-344-kickoff-checklist.md (1), docs/proposals/boss-design-templates.md (1), docs/proposals/shield-break-system.md (1), docs/shield-break-accessibility.md (1), docs/shield-break-integration-guide.md (1), docs/shield-break-performance.md (1), docs/shield-break-save-load.md (1) |
| ui test mjs | 8 | docs/test-coverage-gaps.md (5), docs/CONOPS.md (4), docs/main-dispatch-refactor-plan-gpt-5-1.md (2), docs/shield-break-docs-index.md (2), docs/day-344-kickoff-checklist.md (1), docs/day-344-task-assignments.md (1), docs/shield-break-quick-reference.md (1), docs/shield-break-ui-components.md (1) |
| integration test mjs | 8 | docs/CONOPS.md (6), docs/shield-break-docs-index.md (2), docs/day-344-kickoff-checklist.md (1), docs/day-344-task-assignments.md (1), docs/main-dispatch-refactor-plan-gpt-5-1.md (1), docs/refactor_plan_main_js.md (1), docs/shield-break-quick-reference.md (1), docs/test-coverage-gaps.md (1) |
| src main js | 6 | docs/issue-201-battle-softlock-analysis.md (7), docs/main-dispatch-refactor-plan-gpt-5-1.md (6), docs/CONOPS.md (4), docs/refactor_plan_main_js.md (4), docs/refactor_architecture_day339.md (3), README.md (1) |
| src combat js | 6 | docs/CONOPS.md (7), docs/issue-201-battle-softlock-analysis.md (4), docs/day-344-kickoff-checklist.md (1), docs/shield-break-api-contract.md (1), docs/shield-break-docs-index.md (1), docs/shield-break-integration-guide.md (1) |
| claude sonnet 4 | 6 | docs/day-344-task-assignments.md (4), docs/CONOPS.md (2), docs/day-344-kickoff-checklist.md (2), docs/shield-break-api-contract.md (2), docs/shield-break-docs-index.md (2), STATISTICS_BUG_FIX.md (1) |
| 1 shield damage | 6 | docs/proposals/shield-break-system.md (4), docs/day-344-task-assignments.md (2), docs/shield-break-integration-guide.md (2), docs/shield-break-quick-reference.md (2), docs/day-344-kickoff-checklist.md (1), docs/proposals/crafting-system-design.md (1) |
| with shield break | 6 | docs/shield-break-docs-index.md (7), docs/day-344-task-assignments.md (1), docs/proposals/boss-design-templates.md (1), docs/proposals/crafting-system-design.md (1), docs/proposals/enemy-weakness-database.md (1), docs/proposals/shield-break-system.md (1) |
| shield break test | 6 | docs/day-344-kickoff-checklist.md (3), docs/shield-break-docs-index.md (3), docs/day-344-task-assignments.md (1), docs/proposals/shield-break-system.md (1), docs/shield-break-quick-reference.md (1), docs/shield-break-ui-components.md (1) |
| break test mjs | 6 | docs/day-344-kickoff-checklist.md (2), docs/shield-break-docs-index.md (2), docs/day-344-task-assignments.md (1), docs/proposals/shield-break-system.md (1), docs/shield-break-quick-reference.md (1), docs/shield-break-ui-components.md (1) |
| gpt 5 1 | 6 | docs/day-344-task-assignments.md (2), docs/main-dispatch-refactor-plan-gpt-5-1.md (2), docs/CONOPS.md (1), docs/day-344-kickoff-checklist.md (1), docs/shield-break-api-contract.md (1), docs/shield-break-docs-index.md (1) |
| shield break test mjs | 6 | docs/day-344-kickoff-checklist.md (2), docs/shield-break-docs-index.md (2), docs/day-344-task-assignments.md (1), docs/proposals/shield-break-system.md (1), docs/shield-break-quick-reference.md (1), docs/shield-break-ui-components.md (1) |
| tests shield break | 6 | docs/shield-break-docs-index.md (2), docs/shield-break-ui-components.md (2), docs/day-344-kickoff-checklist.md (1), docs/day-344-task-assignments.md (1), docs/proposals/shield-break-system.md (1), docs/shield-break-quick-reference.md (1) |
| claude sonnet 4 5 | 6 | docs/day-344-task-assignments.md (2), STATISTICS_BUG_FIX.md (1), docs/CONOPS.md (1), docs/day-344-kickoff-checklist.md (1), docs/shield-break-api-contract.md (1), docs/shield-break-docs-index.md (1) |
| deepseek v3 2 | 6 | docs/day-344-task-assignments.md (2), STATISTICS_BUG_FIX.md (1), docs/CONOPS.md (1), docs/day-344-kickoff-checklist.md (1), docs/shield-break-api-contract.md (1), docs/shield-break-docs-index.md (1) |
| sonnet 4 5 | 6 | docs/day-344-task-assignments.md (2), STATISTICS_BUG_FIX.md (1), docs/CONOPS.md (1), docs/day-344-kickoff-checklist.md (1), docs/shield-break-api-contract.md (1), docs/shield-break-docs-index.md (1) |
| tests shield break test | 6 | docs/shield-break-docs-index.md (2), docs/day-344-kickoff-checklist.md (1), docs/day-344-task-assignments.md (1), docs/proposals/shield-break-system.md (1), docs/shield-break-quick-reference.md (1), docs/shield-break-ui-components.md (1) |
| 4 5 from | 6 | docs/proposals/crafting-system-design.md (1), docs/shield-break-accessibility.md (1), docs/shield-break-api-contract.md (1), docs/shield-break-docs-index.md (1), docs/shield-break-performance.md (1), docs/shield-break-save-load.md (1) |
| 4 5 from voted out day | 6 | docs/proposals/crafting-system-design.md (1), docs/shield-break-accessibility.md (1), docs/shield-break-api-contract.md (1), docs/shield-break-docs-index.md (1), docs/shield-break-performance.md (1), docs/shield-break-save-load.md (1) |
| 5 from voted | 6 | docs/proposals/crafting-system-design.md (1), docs/shield-break-accessibility.md (1), docs/shield-break-api-contract.md (1), docs/shield-break-docs-index.md (1), docs/shield-break-performance.md (1), docs/shield-break-save-load.md (1) |
| 5 from voted out | 6 | docs/proposals/crafting-system-design.md (1), docs/shield-break-accessibility.md (1), docs/shield-break-api-contract.md (1), docs/shield-break-docs-index.md (1), docs/shield-break-performance.md (1), docs/shield-break-save-load.md (1) |
| 5 from voted out day | 6 | docs/proposals/crafting-system-design.md (1), docs/shield-break-accessibility.md (1), docs/shield-break-api-contract.md (1), docs/shield-break-docs-index.md (1), docs/shield-break-performance.md (1), docs/shield-break-save-load.md (1) |
| 5 from voted out day 343 | 6 | docs/proposals/crafting-system-design.md (1), docs/shield-break-accessibility.md (1), docs/shield-break-api-contract.md (1), docs/shield-break-docs-index.md (1), docs/shield-break-performance.md (1), docs/shield-break-save-load.md (1) |
| by claude opus 4 5 from | 6 | docs/proposals/crafting-system-design.md (1), docs/shield-break-accessibility.md (1), docs/shield-break-api-contract.md (1), docs/shield-break-docs-index.md (1), docs/shield-break-performance.md (1), docs/shield-break-save-load.md (1) |
| claude opus 4 5 from | 6 | docs/proposals/crafting-system-design.md (1), docs/shield-break-accessibility.md (1), docs/shield-break-api-contract.md (1), docs/shield-break-docs-index.md (1), docs/shield-break-performance.md (1), docs/shield-break-save-load.md (1) |
| from voted out day | 6 | docs/proposals/crafting-system-design.md (1), docs/shield-break-accessibility.md (1), docs/shield-break-api-contract.md (1), docs/shield-break-docs-index.md (1), docs/shield-break-performance.md (1), docs/shield-break-save-load.md (1) |
| from voted out day 343 | 6 | docs/proposals/crafting-system-design.md (1), docs/shield-break-accessibility.md (1), docs/shield-break-api-contract.md (1), docs/shield-break-docs-index.md (1), docs/shield-break-performance.md (1), docs/shield-break-save-load.md (1) |
| opus 4 5 from | 6 | docs/proposals/crafting-system-design.md (1), docs/shield-break-accessibility.md (1), docs/shield-break-api-contract.md (1), docs/shield-break-docs-index.md (1), docs/shield-break-performance.md (1), docs/shield-break-save-load.md (1) |
| out day 343 | 6 | docs/proposals/crafting-system-design.md (1), docs/shield-break-accessibility.md (1), docs/shield-break-api-contract.md (1), docs/shield-break-docs-index.md (1), docs/shield-break-performance.md (1), docs/shield-break-save-load.md (1) |
| tests shield break test mjs | 6 | docs/day-344-kickoff-checklist.md (1), docs/day-344-task-assignments.md (1), docs/proposals/shield-break-system.md (1), docs/shield-break-docs-index.md (1), docs/shield-break-quick-reference.md (1), docs/shield-break-ui-components.md (1) |
| voted out day | 6 | docs/proposals/crafting-system-design.md (1), docs/shield-break-accessibility.md (1), docs/shield-break-api-contract.md (1), docs/shield-break-docs-index.md (1), docs/shield-break-performance.md (1), docs/shield-break-save-load.md (1) |
| voted out day 343 | 6 | docs/proposals/crafting-system-design.md (1), docs/shield-break-accessibility.md (1), docs/shield-break-api-contract.md (1), docs/shield-break-docs-index.md (1), docs/shield-break-performance.md (1), docs/shield-break-save-load.md (1) |
| if state phase | 5 | docs/issue-201-battle-softlock-analysis.md (10), docs/shield-break-integration-guide.md (3), docs/issue-201-analysis.md (2), docs/api/inventory-system-api.md (1), docs/main-dispatch-refactor-plan-gpt-5-1.md (1) |
| npm run test | 5 | docs/CONOPS.md (6), docs/main-dispatch-refactor-plan-gpt-5-1.md (4), docs/local-test-and-security-checks.md (3), README.md (2), docs/refactor_architecture_day339.md (1) |
| weaknesses 'fire' 'lightning' | 5 | docs/proposals/enemy-weakness-database.md (6), docs/shield-break-api-contract.md (5), docs/proposals/shield-break-system.md (2), docs/day-344-task-assignments.md (1), docs/shield-break-save-load.md (1) |
| npm run test all | 5 | docs/CONOPS.md (4), docs/local-test-and-security-checks.md (3), docs/main-dispatch-refactor-plan-gpt-5-1.md (3), README.md (2), docs/refactor_architecture_day339.md (1) |
| run test all | 5 | docs/CONOPS.md (4), docs/local-test-and-security-checks.md (3), docs/main-dispatch-refactor-plan-gpt-5-1.md (3), README.md (2), docs/refactor_architecture_day339.md (1) |
| weaknesses 'fire' 'holy' | 5 | docs/proposals/enemy-weakness-database.md (6), docs/proposals/shield-break-system.md (3), docs/day-344-task-assignments.md (2), docs/proposals/boss-design-templates.md (1), docs/shield-break-api-contract.md (1) |
| combat handler js | 5 | STATISTICS_BUG_FIX.md (4), docs/issue-201-battle-softlock-analysis.md (4), README.md (1), docs/refactor_architecture_day339.md (1), docs/refactor_plan_main_js.md (1) |
| break system md | 5 | docs/shield-break-docs-index.md (4), docs/day-344-kickoff-checklist.md (2), docs/day-344-task-assignments.md (2), docs/api/boss-system-api.md (1), docs/shield-break-api-contract.md (1) |
| shield break system md | 5 | docs/shield-break-docs-index.md (4), docs/day-344-kickoff-checklist.md (2), docs/day-344-task-assignments.md (2), docs/api/boss-system-api.md (1), docs/shield-break-api-contract.md (1) |
| weaknesses 'holy' 'lightning' | 5 | docs/proposals/enemy-weakness-database.md (3), docs/day-344-task-assignments.md (2), docs/proposals/shield-break-system.md (2), docs/shield-break-api-contract.md (2), docs/proposals/boss-design-templates.md (1) |
| boss design templates | 5 | docs/shield-break-docs-index.md (4), docs/day-344-kickoff-checklist.md (2), docs/api/boss-system-api.md (1), docs/day-344-task-assignments.md (1), docs/proposals/enemy-weakness-database.md (1) |
| shieldcount 8 weaknesses | 5 | docs/shield-break-api-contract.md (3), docs/day-344-task-assignments.md (2), docs/proposals/enemy-weakness-database.md (2), docs/proposals/boss-design-templates.md (1), docs/proposals/shield-break-system.md (1) |
| 2 5 pro | 5 | docs/day-344-kickoff-checklist.md (3), docs/day-344-task-assignments.md (2), docs/CONOPS.md (1), docs/shield-break-api-contract.md (1), docs/shield-break-docs-index.md (1) |
| combat js integration | 5 | docs/shield-break-docs-index.md (3), docs/proposals/shield-break-system.md (2), docs/day-344-kickoff-checklist.md (1), docs/day-344-task-assignments.md (1), docs/shield-break-quick-reference.md (1) |
| gemini 2 5 | 5 | docs/day-344-kickoff-checklist.md (3), docs/day-344-task-assignments.md (2), docs/CONOPS.md (1), docs/shield-break-api-contract.md (1), docs/shield-break-docs-index.md (1) |
| gemini 2 5 pro | 5 | docs/day-344-kickoff-checklist.md (3), docs/day-344-task-assignments.md (2), docs/CONOPS.md (1), docs/shield-break-api-contract.md (1), docs/shield-break-docs-index.md (1) |
| 5 weaknesses 'fire' | 5 | docs/day-344-task-assignments.md (2), docs/proposals/enemy-weakness-database.md (2), docs/proposals/boss-design-templates.md (1), docs/shield-break-save-load.md (1), docs/test-quality-standards.md (1) |
| claude opus 4 6 | 5 | docs/day-344-task-assignments.md (2), docs/shield-break-docs-index.md (2), docs/CONOPS.md (1), docs/day-344-kickoff-checklist.md (1), docs/shield-break-api-contract.md (1) |
| opus 4 6 | 5 | docs/day-344-task-assignments.md (2), docs/shield-break-docs-index.md (2), docs/CONOPS.md (1), docs/day-344-kickoff-checklist.md (1), docs/shield-break-api-contract.md (1) |
| boss phase transitions | 5 | docs/proposals/enemy-weakness-database.md (2), docs/day-344-kickoff-checklist.md (1), docs/shield-break-api-contract.md (1), docs/shield-break-docs-index.md (1), docs/shield-break-state-machine.md (1) |
| broken 2 turns | 5 | docs/shield-break-accessibility.md (2), docs/day-344-task-assignments.md (1), docs/proposals/shield-break-system.md (1), docs/shield-break-api-contract.md (1), docs/shield-break-ui-components.md (1) |
| claude sonnet 4 6 | 5 | docs/day-344-task-assignments.md (2), docs/CONOPS.md (1), docs/day-344-kickoff-checklist.md (1), docs/shield-break-api-contract.md (1), docs/shield-break-docs-index.md (1) |
| enemy is broken | 5 | docs/shield-break-accessibility.md (2), docs/shield-break-api-contract.md (1), docs/shield-break-balance-guide.md (1), docs/shield-break-integration-guide.md (1), docs/shield-break-save-load.md (1) |
| fire ice lightning | 5 | docs/proposals/shield-break-system.md (2), docs/day-344-task-assignments.md (1), docs/proposals/enemy-weakness-database.md (1), docs/shield-break-api-contract.md (1), docs/shield-break-docs-index.md (1) |

_Total document units considered (files or sections): 37_
