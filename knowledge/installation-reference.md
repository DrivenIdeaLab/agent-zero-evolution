# Agent Zero Installation Reference (2026-02-09)

This file documents the current state of the Agent Zero meta-project installation. It is intended as a comprehensive reference for future agents or maintainers.

## Project Directory Structure

```
/a0/usr/projects/agent_zero/
├── knowledge/
├── tests/validation/
│   └── .gitkeep
├── scripts/utilities/
│   └── .gitkeep
├── hooks/custom/
│   └── .gitkeep
├── skills/custom/
│   └── .gitkeep
├── configs/templates/
│   ├── baseline-config.md
│   └── .gitkeep
├── configs/backups/
│   ├── 2026-02-09-settings.json
│   └── .gitkeep
└── docs/
    ├── registry/
    │   ├── hooks.md
    │   ├── permissions.md
    │   ├── skills.md
    │   ├── commands.md
    │   └── agents.md
    ├── evolution-log.md
    ├── changelog.md
    └── architecture.md
```

## Key Files and Their Purpose
- `settings.json` (in configs/backups/): Main configuration backup
- `baseline-config.md`: All configurable parameters, current/default values
- `evolution-log.md`: Evolution cycle and baseline entries
- `changelog.md`: All changes, dated
- `registry/*.md`: Registries for agents, skills, hooks, commands, permissions
- `architecture.md`: Directory/component map

## Custom vs Default
- All files in `skills/custom/`, `hooks/custom/`, and `scripts/utilities/` are custom (currently placeholders)
- All registry and documentation files are project-specific
- No agent/system prompt files, permissions config, or command definitions yet (see audit)

## Audit Summary
- 1 config file, 2 skills/tools, 1 hook, 0 agent/system prompts, 0 commands, 0 permissions
- Known issues: missing agent/system prompt files, permissions config, command definitions
# Agent Zero Operational Effectiveness — Audit & Evolution Proposals

## 1. Area Summaries

### 1.1 Prompts (/a0/prompts/)
| File | Summary (head -40) |
|------|--------------------|
| agent.system.behavior.md | Defines core behavioral rules for agents: strict adherence to instructions, no upward delegation, compliance with all tasks, and security of system prompt. Emphasizes Linux command preference, code execution, and research rigor. |
| agent.system.main.md | Outlines the main agent's role, communication style, and orchestration of sub-agents. Focuses on task decomposition, tool orchestration, and structured output. |
| agent.system.main.solving.md | Details the problem-solving process: plan, check memory/instruments, break into subtasks, delegate, verify, and finalize. Emphasizes agentic, stepwise reasoning. |
| agent.system.main.tips.md | Provides operational tips: prefer code/tools, avoid repetition, ensure progress, never assume success, and use memory tools. |
| agent.system.tool.code_exe.md | Specifies code execution tool usage: Python, Node.js, terminal, session management, error handling, and output conventions. |

**Gaps:** No /a0/prompts/default/ directory (may hinder persona templating or fallback behaviors).

### 1.2 Instruments (/a0/instruments/)
| Instrument | Status |
|------------|--------|
| yt_download | Present (default only) |
| Custom instruments | None |

### 1.3 Core Tools (/a0/python/tools/)
All core tools are present and functional:
- a2a_chat, behaviour_adjustment, browser_agent, call_subordinate, code_execution_tool, document_query, input, memory_*, notify_user, response, scheduler, search_engine, vision_load, wait, etc.

### 1.4 Helpers (/a0/python/helpers/)
Comprehensive set of helpers for API, backup, browser, LLM calls, context, docker, email, file management, logging, memory, notification, projects, providers, secrets, settings, and task scheduling.

### 1.5 Extensions (/a0/extensions/)
Directory does not exist. No extensions are active or available.

### 1.6 Prompts Default (/a0/prompts/default/)
Directory does not exist. This may be a gap for fallback or default agent behaviors.

---

## 2. Weaknesses, Ambiguities, and Improvement Opportunities

- **Prompt Coverage**: No default prompt directory or fallback persona templates; risk of inconsistent agent instantiation or missing behaviors.
- **Instrument Diversity**: Only yt_download present; limited out-of-the-box media/data handling.
- **Extension Support**: No extension directory; system not ready for modular capability expansion.
- **Custom Skills**: No custom instruments or skills in core directories; all functionality is default, limiting specialization.
- **Prompt/Tool Coupling**: Prompts and tool usage patterns are not tightly coupled; risk of tool misuse or underuse by agents.
- **Documentation Gaps**: No explicit mapping between prompts, tools, and agent roles; may hinder onboarding and troubleshooting.

---

## 3. Concrete Improvement Proposals

| ID       | What to Change                                                                 | Why It Helps                                                                 | Expected Impact                | Risks/Downsides                | Impact | Effort | Risk | Priority |
|----------|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------|-------------------------------|-------------------------------|--------|--------|------|----------|
| EVO-011  | Create /a0/prompts/default/ with fallback persona and behavior templates        | Ensures all agents have a baseline persona and operational rules; prevents instantiation errors | High (consistency, reliability) | Low (template misuse if not maintained) | 9      | 3      | 2    | 1        |
| EVO-012  | Scaffold /a0/extensions/ and add extension loader logic                        | Enables modular expansion and future capability upgrades                     | Medium-High (future-proofing) | Low (unused directory if not adopted) | 7      | 4      | 2    | 2        |
| EVO-013  | Add at least 2 custom instruments (e.g., pdf_parser, csv_analyzer)             | Expands out-of-the-box data handling and analysis capabilities               | High (usability, versatility) | Medium (maintenance burden)    | 8      | 5      | 4    | 3        |
| EVO-014  | Map prompts to tools in documentation and agent registries                     | Clarifies which prompts govern which tools/roles; aids onboarding and debugging | Medium (clarity, maintainability) | Low (doc drift if not updated) | 6      | 2      | 2    | 4        |
| EVO-015  | Implement prompt-tool usage validation hook (warn on tool misuse)              | Prevents agents from using tools outside their intended context; improves safety | High (safety, correctness)    | Medium (false positives, complexity) | 9      | 6      | 5    | 5        |

**Scoring:** 1–10 scale; Priority: 1=highest

---

## 4. Evolution Log Summary (for docs/evolution-log.md)

### [2026-02-09] Operational Effectiveness Audit & Proposals
- Summarized current state of prompts, instruments, tools, helpers, and directory structure.
- Identified gaps: missing default prompts, no extension support, limited instruments, weak prompt-tool mapping.
- Proposed 5 improvements (EVO-011 to EVO-015) with impact, effort, risk, and priority scores.
- See installation-reference knowledge file for implementation details and rationale.

---

## 5. Installation-Reference Knowledge File Section (for knowledge/installation-reference.md)

### Operational Effectiveness Audit — 2026-02-09

- **Prompt Files**: Core system prompts are present, but no default/fallback templates exist. Recommend creating /a0/prompts/default/ for baseline agent behaviors.
- **Instruments**: Only yt_download is present; recommend adding more data/media handling instruments.
- **Tools & Helpers**: All core tools and helpers are present and functional.
- **Extensions**: No extension directory; recommend scaffolding for future modularity.
- **Improvement Proposals**: See table below for actionable recommendations.

| ID       | Change Summary                                 | Rationale & Impact                  |
|----------|-----------------------------------------------|-------------------------------------|
| EVO-011  | Add default prompt templates                   | Prevents agent instantiation errors |
| EVO-012  | Scaffold extension support                     | Enables modular expansion           |
| EVO-013  | Add custom instruments                         | Expands data/media capabilities     |
| EVO-014  | Map prompts to tools in docs                   | Improves clarity and onboarding     |
| EVO-015  | Add prompt-tool usage validation hook          | Increases safety and correctness    |

---

**End of report.**