# Naming Conventions

## Files
- Use kebab-case: `my-custom-skill.py`
- Prefix with category when useful: `hook-on-message-log.py`
- Documentation files: lowercase with hyphens

## Agents
- Use descriptive role names: `research-agent`, `code-reviewer`
- Prefix sub-agents: `sub-data-analyst`

## Skills / Tools
- Function names: snake_case (`fetch_web_content`)
- Class names: PascalCase (`WebContentFetcher`)
- Skill files: match primary function name

## Memory Tags
- Use hierarchical tags: `config/models`, `skill/web-scraping`
- Prefix system memories: `sys/...`
- Prefix project memories: `proj/...`

## Changelog Entries
- Format: `[YYYY-MM-DD] [PATCH|ENHANCEMENT|ARCHITECTURE|EXPERIMENT] Description`