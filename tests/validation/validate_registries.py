"""
Registry Table Validator

Checks that each registry .md file:
- Has a proper markdown table structure
- Has no empty or placeholder rows
- Reports pass/fail per registry

Run: python tests/validation/validate_registries.py
"""
import os

import os
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
REGISTRIES = [
    'docs/registry/skills.md',
    'docs/registry/hooks.md',
    'docs/registry/permissions.md',
    'docs/registry/agents.md',
    'docs/registry/commands.md',
]
def validate_table(path):
    with open(path) as f:
        lines = [line.strip() for line in f if line.strip()]
    # Find table header and separator
    header_idx = next((i for i, l in enumerate(lines) if l.startswith('|')), None)
    sep_idx = header_idx + 1 if header_idx is not None and len(lines) > header_idx+1 and set(lines[header_idx+1].replace('|','').strip()) <= {'-',' '} else None
    if header_idx is None or sep_idx is None:
        return False, 'Missing or malformed table header/separator'
    # Check for empty/placeholder rows
    for l in lines[sep_idx+1:]:
        if l.count('|') < 2:
            continue
        cells = [c.strip() for c in l.split('|')[1:-1]]
        if any(c in ('', 'TODO', 'TBD', '...') for c in cells):
            return False, f'Empty or placeholder cell in row: {l}'
    return True, 'OK'
if __name__ == '__main__':
    for reg in REGISTRIES:
        full = os.path.join(PROJECT_ROOT, reg)
        if not os.path.exists(full):
            print(f'{reg}: MISSING')
            continue
        ok, msg = validate_table(full)
        print(f'{reg}: {"PASS" if ok else "FAIL"} - {msg}')
