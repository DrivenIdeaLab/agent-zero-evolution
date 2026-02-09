import re
from typing import List, Dict

def detect_incomplete(response: str) -> bool:
    incomplete_patterns = [
        r'\bcontinue\b', r'\bto be continued\b', r'\bincomplete\b', r'\.\.\.$', r'\[CONTINUED\]', r'\(more\)', r'\[truncated\]'
    ]
    for pat in incomplete_patterns:
        if re.search(pat, response, re.IGNORECASE):
            return True
    return False

def extract_tasks(response: str) -> Dict[str, List[str]]:
    completed, remaining = [], []
    # Simple heuristic: look for lists with [x] or [ ]
    for line in response.splitlines():
        if re.match(r'\s*[-*] \[x\] ', line, re.IGNORECASE):
            completed.append(line.strip())
        elif re.match(r'\s*[-*] \[ \] ', line, re.IGNORECASE):
            remaining.append(line.strip())
    return {'completed': completed, 'remaining': remaining}

def build_continuation_prompt(response: str) -> str:
    tasks = extract_tasks(response)
    prompt = 'The previous response was incomplete.'
    if detect_incomplete(response):
        prompt += ' Please continue the task.'
    if tasks['remaining']:
        prompt += '\nRemaining subtasks:'
        for t in tasks['remaining']:
            prompt += f'\n- {t}'
    return prompt

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print('Usage: task_continuation.py <response_file>')
        sys.exit(1)
    with open(sys.argv[1]) as f:
        resp = f.read()
    print('Incomplete:', detect_incomplete(resp))
    print('Tasks:', extract_tasks(resp))
    print('Continuation prompt:\n', build_continuation_prompt(resp))
