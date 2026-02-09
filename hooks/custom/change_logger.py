"""
Change Logger Hook

Monitors key project files for modifications. When triggered, appends a changelog entry with timestamp, file changed, and change type.

Example usage:
    from hooks.custom.change_logger import log_change
    log_change('/a0/usr/projects/agent_zero/docs/changelog.md', 'test')
"""
import os
from datetime import datetime

def log_change(file_path, change_type):
    """Append a change entry to the changelog."""
    changelog = '/a0/usr/projects/agent_zero/docs/changelog.md'
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    rel_path = os.path.relpath(file_path, '/a0/usr/projects/agent_zero')
    entry = f"[{now}] [AUTO] {rel_path} {change_type}\n"
    with open(changelog, 'a') as f:
        f.write(entry)
