# Command: daily-check

**Description:**
Manually trigger the Agent Zero daily health check and view the latest daily report.

**Usage:**
```bash
bash /a0/usr/projects/agent_zero/scripts/utilities/daily-check.sh
cat /a0/usr/projects/agent_zero/docs/daily-reports/$(date +%F).md
```

**Output:**
- Health check and registry validation results
- Changelog recency
- Knowledge file counts
- Summary and alert if any check fails

**See also:**
- `scripts/utilities/daily-check.sh`
- `docs/daily-reports/`
```

# 7. Update commands registry
CMD_REG='/a0/usr/projects/agent_zero/docs/registry/commands.md'
grep -q 'daily-check' "$CMD_REG" || echo '| daily-check | /a0/usr/projects/agent_zero/scripts/utilities/daily-check.sh | Run daily health check and write report | ✅ |' >> "$CMD_REG"

# 8. Log in changelog
cat >> /a0/usr/projects/agent_zero/docs/changelog.md <<'EOF'
[2026-02-09] [ENHANCEMENT] Automated daily and weekly health/evolution checks: scripts, cron, report dirs, .gitignore, and command docs created.
