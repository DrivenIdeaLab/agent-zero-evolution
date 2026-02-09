#!/usr/bin/env bash
set -euo pipefail

cd /a0/usr/projects/agent_zero

# Check for changes
if git diff --quiet && git diff --cached --quiet; then
    echo "No changes to commit"
    exit 0
fi

# Generate commit message from latest changelog entry
LATEST_ENTRY=$(head -5 docs/changelog.md | grep '^\[' | head -1)
if [ -z "$LATEST_ENTRY" ]; then
    COMMIT_MSG="Auto-sync: $(date +%Y-%m-%d)"
else
    COMMIT_MSG="$LATEST_ENTRY"
fi

git add -A
git commit -m "$COMMIT_MSG"
git push origin $(git branch --show-current)

echo "Pushed: $COMMIT_MSG"
