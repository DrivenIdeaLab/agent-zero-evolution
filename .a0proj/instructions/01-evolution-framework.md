# Evolution Framework

## Purpose
This file defines the framework for how Agent Zero evolves itself over time.

## Evolution Dimensions

| Dimension       | Description                                    | Metrics                        |
|-----------------|------------------------------------------------|--------------------------------|
| Capability      | What the system can do                         | # of skills, task success rate |
| Reliability     | How consistently it performs                   | Error rate, retry frequency    |
| Safety          | How well guardrails hold                       | Violation attempts caught      |
| Efficiency      | Resource usage and response time               | Token usage, latency           |
| Maintainability | How easy the system is to understand & modify  | Doc coverage, code clarity     |
| Adaptability    | How well it handles novel situations           | Novel task success rate        |

## Evolution Triggers
- Operator request ("improve X", "add capability Y")
- Failure detection (recurring errors, failed tasks)
- Periodic review (weekly evolution cycle)
- New Agent Zero version release
- New integration or tool availability

## Change Classification
- **Patch**: Bug fix, typo correction, minor config tweak
- **Enhancement**: New skill, improved prompt, better hook
- **Architecture**: Structural change, new agent, permission overhaul
- **Experiment**: Trying something new, requires monitoring