# Command: health check

**What it does:**
Runs the system health check skill to verify project structure, registry completeness, and changelog recency.

**How to invoke:**
Say or type: `run health check`

**How to interpret results:**
- All values should be `true` for a healthy system.
- Any `false` indicates a missing or incomplete component.

**What to do when checks fail:**
- Create missing directories/files
- Populate empty registries
- Ensure changelog is up to date

