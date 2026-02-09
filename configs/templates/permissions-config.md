# Permissions & Guardrails Configuration

_This file defines file-system, network, and command execution guardrails for Agent Zero._

## File-System Access
- Allowed: /a0/usr/projects/agent_zero/, /tmp
- Forbidden: /, /root, /etc, /home, /var, /usr (except project dir)

## Network Access
- Allowed: whitelisted domains only (define in this file)
- Forbidden: all others by default

## Command Execution
- Allowed: safe Linux utilities, Python, Node.js
- Forbidden: destructive commands (rm -rf, format, etc.)
- Approval required for Tier 3+ actions (see docs/registry/permissions.md)

## Approval Gates
- Tier 3: Confirm with operator before applying
- Tier 4: Require explicit approval and justification

---
_Edit this file to update guardrails. See registry/permissions.md for documentation._
