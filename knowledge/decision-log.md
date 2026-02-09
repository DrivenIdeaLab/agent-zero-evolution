# Decision Log

This file records key configuration and architectural decisions for Agent Zero. Use the template for future entries.

## Template
- **Date:**
- **Decision:**
- **Rationale:**
- **Alternatives Considered:**
- **Impact:**
- **Related Files:**

## Entries

### 2026-02-09 — Initial Baseline
- **Decision:** Use default directory structure and initialize all registry/docs as markdown
- **Rationale:** Provides a clear, auditable foundation for all future changes
- **Alternatives Considered:** Ad-hoc file creation, less structure
- **Impact:** High maintainability, easy onboarding for future agents
- **Related Files:** All docs/, configs/, registry/

### 2026-02-09 — Model Configuration
- **Decision:** Use OpenRouter/OpenAI for chat and utility models, HuggingFace for embeddings
- **Rationale:** Default settings are stable and well-supported; no custom models required yet
- **Alternatives Considered:** Local/Ollama models, custom providers
- **Impact:** Reliable operation, easy future migration
- **Related Files:** settings.json, baseline-config.md
