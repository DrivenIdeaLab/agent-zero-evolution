# Safety Protocols

## Tier 1 — Unrestricted (no approval needed)
- Reading any project file
- Generating documentation
- Running audits and producing reports
- Creating backups

## Tier 2 — Notify (inform operator, proceed unless stopped)
- Adding new documentation files
- Creating backup copies of configs
- Adding new entries to registries

## Tier 3 — Confirm (require explicit operator approval)
- Modifying any configuration file
- Adding or modifying skills/tools
- Changing hook behavior
- Creating new agents or modifying agent prompts
- Installing packages or dependencies

## Tier 4 — Restricted (require approval + justification)
- Modifying permissions or guardrails
- Changing model/provider settings
- Modifying other projects
- Any destructive file operations
- Network configuration changes

## Rollback Procedure
1. Before any Tier 3+ change, create a timestamped backup
2. Store backup in `configs/backups/` with format: `YYYYMMDD-HHMMSS-filename`
3. Log the change in changelog with rollback instructions
4. If a change causes issues, restore from the most recent backup