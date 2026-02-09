#!/bin/bash
set -euo pipefail
DATE=$(date +%F)
REPORT_DIR="/a0/usr/projects/agent_zero/docs/daily-reports"
REPORT="$REPORT_DIR/$DATE.md"
ALERT="$REPORT_DIR/ALERT-$DATE.md"
LOG="$REPORT_DIR/daily-check-$DATE.log"

mkdir -p "$REPORT_DIR"
exec > >(tee -a "$LOG") 2>&1

echo "# Agent Zero Daily Health Check — $DATE"
echo "Timestamp: $(date --iso-8601=seconds)"

FAIL=0

# a. System health check
if python3 /a0/usr/projects/agent_zero/skills/custom/system_health_check.py; then
echo "- System health check: PASS"
else
echo "- System health check: FAIL"; FAIL=1
fi

# b. Registry validation
if python3 /a0/usr/projects/agent_zero/tests/validation/validate_registries.py; then
echo "- Registry validation: PASS"
else
echo "- Registry validation: FAIL"; FAIL=1
fi

# c. Changelog recency (7 days)
CHANGELOG="/a0/usr/projects/agent_zero/docs/changelog.md"
if [ -f "$CHANGELOG" ]; then
  MOD_DAYS=$(( ( $(date +%s) - $(stat -c %Y "$CHANGELOG") ) / 86400 ))
  if [ "$MOD_DAYS" -le 7 ]; then
    echo "- Changelog updated $MOD_DAYS days ago: PASS"
  else
    echo "- Changelog is stale ($MOD_DAYS days): FAIL"; FAIL=1
  fi
else
echo "- Changelog missing: FAIL"; FAIL=1
fi

# d. Count memories and knowledge files
MEM_COUNT=$(ls /a0/usr/projects/agent_zero/knowledge/*.md 2>/dev/null | wc -l)
KNOW_COUNT=$(ls /a0/usr/projects/agent_zero/knowledge/ 2>/dev/null | wc -l)
echo "- Knowledge files: $MEM_COUNT"
echo "- Knowledge dir entries: $KNOW_COUNT"

echo "\n# Summary"
if [ "$FAIL" -eq 0 ]; then
echo "All checks passed."
else
echo "One or more checks FAILED. See above."
  touch "$ALERT"
fi

# Write report
cp "$LOG" "$REPORT"
