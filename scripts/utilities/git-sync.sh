#!/bin/bash
set -euo pipefail
MODE="all"
if [[ "${1:-}" == "--reports" ]]; then
  MODE="reports"
fi
if [[ "${1:-}" == "--all" ]]; then
  MODE="all"
fi
if [[ "$MODE" == "reports" ]]; then
  scripts/utilities/prune-reports.sh
  git add docs/daily-reports/ docs/weekly-reports/ 2>/dev/null || true
  if ! git diff --cached --quiet; then
    DATE=$(date +%F)
    git commit -m "[REPORTS] Daily/Weekly reports $DATE"
    git push
  else
    echo "No report changes to commit."
    exit 0
  fi
else
  git add -A
  if ! git diff --cached --quiet; then
    LATEST_MSG=$(tail -n 1 docs/changelog.md 2>/dev/null || echo "[AUTO] Sync commit")
    git commit -m "$LATEST_MSG"
    git push
  else
    echo "No changes to commit."
    exit 0
  fi
fi
