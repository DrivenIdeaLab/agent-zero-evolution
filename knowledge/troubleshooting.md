# Troubleshooting Patterns

This file documents common and anticipated troubleshooting patterns for this Agent Zero installation.

## Patterns
- **Missing config/registry files:** Check for typos or incomplete scaffolding; re-run project initialization if needed
- **No agent/system prompt files:** Add prompt files to the appropriate directory and update registry
- **Permissions/guardrails not enforced:** Create a permissions config in configs/ and document policies
- **Skills/hooks not recognized:** Ensure files are in the correct custom/ directory and have valid Python/markdown structure
- **Registry out of sync:** Run the validation script in tests/validation/ to check for missing or extra entries
- **Settings not loading:** Restore from the latest backup in configs/backups/
- **Docker/Environment issues:** Confirm Docker is running, correct ports are mapped, and dependencies are installed

## General Advice
- Always back up configs before making changes
- Use the changelog and evolution log to track all modifications
- Refer to baseline-config.md for parameter defaults
