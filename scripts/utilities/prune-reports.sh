#!/bin/bash
set -euo pipefail
for dir in docs/daily-reports docs/weekly-reports; do
  if [ -d "$dir" ]; then
    find "$dir" -type f -mtime +30 -print -delete
  fi
done
