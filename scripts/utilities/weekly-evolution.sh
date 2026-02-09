#!/bin/bash
set -euo pipefail
DATE=$(date +%F)
REPORT_DIR="/a0/usr/projects/agent_zero/docs/weekly-reports"
DAILY="/a0/usr/projects/agent_zero/scripts/utilities/daily-check.sh"
BACKLOG="/a0/usr/projects/agent_zero/scripts/utilities/evolution-backlog.md"
REPORT="$REPORT_DIR/$DATE.md"
LOG="$REPORT_DIR/weekly-evolution-$DATE.log"

mkdir -p "$REPORT_DIR"
exec > >(tee -a "$LOG") 2>&1

echo "# Agent Zero Weekly Evolution Observation — $DATE"
echo "Timestamp: $(date --iso-8601=seconds)"

# a. Run daily check
if "$DAILY"; then
echo "- Daily check: PASS"
else
echo "- Daily check: FAIL"
fi

# b. Backlog TODO vs DONE
TODO=$(grep -c '| TODO |' "$BACKLOG" || true)
DONE=$(grep -c '| DONE |' "$BACKLOG" || true)
echo "- Evolution backlog: $TODO TODO, $DONE DONE"

# c. New files since last weekly run
LAST=$(ls -t "$REPORT_DIR"/*.md 2>/dev/null | grep -v ALERT | head -n 2 | tail -n 1)
if [ -n "$LAST" ]; then
  SINCE=$(stat -c %Y "$LAST")
  echo "- New files since last weekly report:"
  find /a0/usr/projects/agent_zero/ -type f -newermt "@${SINCE}" | grep -vE '/(archive|tmp|node_modules|__pycache__|.git)/' || echo "  (none)"
else
echo "- No previous weekly report found."
fi

echo "\n# Summary"
echo "Observation only. No changes made."
cp "$LOG" "$REPORT"
