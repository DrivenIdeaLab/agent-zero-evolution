# Lessons Learned

This file captures insights and best practices from the initial setup and baseline process.

- Scaffolding a clear directory and documentation structure accelerates onboarding and future audits
- Maintaining a baseline snapshot (config, docs, changelog) is critical for safe evolution
- Registry files and architecture docs should always reflect the actual state of the system
- Backups should be timestamped and stored in a dedicated directory
- Known gaps (missing prompts, permissions, commands) should be explicitly documented for future improvement
- Self-contained knowledge files make future agents more effective, even with no prior memory


## 2026-02-09 — Real Implementation Validation
- Directory existence issues can cause false negatives in health checks.
- Registry validation scripts must check for and remove placeholder/empty rows.
- Persistent f-string and docstring syntax errors are best fixed by rewriting the file with minimal, correct code.
- Terminal-based file writing can resolve hidden newline/quote issues in Python scripts.
