# Agent Skills

This directory contains local [agent skills](https://agentskills.io/).

The list below includes user-facing skills in this repository and excludes internal skills under `.system`.

## Available Skills

### `gh-issue-minutes-from-zoom`

Draft or post GitHub issue comments with meeting minutes from a Zoom transcript file using gh. Use when the user wants recurring SIG-style meeting notes added to an issue such as open-telemetry/opentelemetry-go#6648 from a .vtt transcript or cleaned text transcript.

- Skill file: [gh-issue-minutes-from-zoom/SKILL.md](/home/ropajak/.codex/skills/gh-issue-minutes-from-zoom/SKILL.md)
- README: [gh-issue-minutes-from-zoom/README.md](/home/ropajak/.codex/skills/gh-issue-minutes-from-zoom/README.md)

### `karpathy-guidelines`

Behavioral guidelines to reduce common LLM coding mistakes. Use when writing, reviewing, or refactoring code to avoid overcomplication, make surgical changes, surface assumptions, and define verifiable success criteria.

- Skill file: [karpathy-guidelines/SKILL.md](/home/ropajak/.codex/skills/karpathy-guidelines/SKILL.md)

### `otel-code-review`

Review code changes like an OpenTelemetry maintainer, with emphasis on spec compliance, semantic conventions, compatibility, tests, performance, and security. Use when the user wants an code review for an OpenTelemetry repository on a patch, PR, or local diff.

- Skill file: [otel-code-review/SKILL.md](/home/ropajak/.codex/skills/otel-code-review/SKILL.md)

### `update-skills-readme`

Update the top-level skills README by listing all user-facing skill folders in this repository and excluding .system. Use when the root README.md should be created, refreshed, or kept in sync as skills are added, removed, or renamed.

- Skill file: [update-skills-readme/SKILL.md](/home/ropajak/.codex/skills/update-skills-readme/SKILL.md)
