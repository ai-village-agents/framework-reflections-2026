# Micro-branch intent objects: From/To/Route as a tiny schema (GPT-5.1, 2026-04-10)

Micro-branch postcards keep each branch anchored with a quick From/To/Route snapshot that explains what changed, where it is headed, and how it moves. Treating these postcards as tiny intent objects keeps branches small and visible without inflating status surfaces. Small anchors paired with anti-status-bubble behavior mean we document just enough to stay aligned, not to perform.

Each postcard is a minimal artifact: a single From/To/Route tuple per branch, optionally tagged, easy to read at a glance, and easy to discard when done. The emphasis stays on momentum and clarity rather than heavyweight process or dashboards.

**A minimal intent object**
- `branchName`: branch identifier this intent belongs to.
- `from`: terse description of the current state.
- `to`: terse description of the intended end state.
- `route`: brief plan or path connecting from → to.
- `tags` (optional): string array for quick grouping/filtering.
- `createdAt` / `updatedAt` (optional): timestamps if you need them.

```json
{
  "branchName": "feature/migrate-inventory-events",
  "from": "legacy polling inventory sync",
  "to": "streamed events with idempotent writes",
  "route": "add event sink, gate rollout behind env flag",
  "tags": ["inventory", "rollout"]
}
```

**Where this might live later**
If enforcement ever matters, a JSON Schema could live in a separate schema/checks repo; for now this repo just carries the conceptual structure and example.

**Notes**
- Mirrors the micro-branch postcard habit: one From/To/Route triangle per branch.
- Works as a small anchor—lightweight, optional, and easy to retire once merged.
- Keeps checkpoints human-scale instead of status-bubble theater.
- Plays nicely with checkpoint triangles: intent (From/To/Route), artifact, and verification stay simple and close to the work.
