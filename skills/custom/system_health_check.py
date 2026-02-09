"""
System Health Check Skill

Checks the Agent Zero meta-project structure for completeness:
- Verifies all expected directories exist
- Verifies all registry files are non-empty
- Checks that the changelog has recent entries
- Returns a structured health report dict

Example usage:
    from skills.custom.system_health_check import system_health_check
    report = system_health_check()
    print(report)
"""
import os
from datetime import datetime

import os
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EXPECTED_DIRS = [
    'knowledge',
    'tests/validation',
    'scripts/utilities',
    'hooks/custom',
    'skills/custom',
    'configs/templates',
    'configs/backups',
    'docs/registry',
    'prompts',
]
REGISTRY_FILES = [
    'docs/registry/skills.md',
    'docs/registry/hooks.md',
    'docs/registry/permissions.md',
    'docs/registry/agents.md',
    'docs/registry/commands.md',
]
CHANGELOG = 'docs/changelog.md'
RECENT_DAYS = 7

def system_health_check():
    report = {'directories': {}, 'registries': {}, 'changelog_recent': False}
    # Check directories
    for d in EXPECTED_DIRS:
        full = os.path.join(PROJECT_ROOT, d)
        report['directories'][d] = os.path.isdir(full)
    # Check registries
    for f in REGISTRY_FILES:
        full = os.path.join(PROJECT_ROOT, f)
        try:
            with open(full) as fh:
                content = fh.read().strip()
            report['registries'][f] = bool(content and not content.isspace())
        except Exception:
            report['registries'][f] = False
    # Check changelog for recent entries
    try:
        with open(os.path.join(PROJECT_ROOT, CHANGELOG)) as fh:
            lines = fh.readlines()
        now = datetime.now()
        for line in reversed(lines):
            if line.startswith('['):
                date_str = line[1:11]
                try:
                    entry_date = datetime.strptime(date_str, '%Y-%m-%d')
                    if (now - entry_date).days <= RECENT_DAYS:
                        report['changelog_recent'] = True
                        break
                except Exception:
                    pass
    except Exception:
        report['changelog_recent'] = False
    return report
