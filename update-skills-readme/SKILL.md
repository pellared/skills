---
name: update-skills-readme
description: Update the top-level skills README by listing all user-facing skill folders in this repository and excluding .system. Use when the root README.md should be created, refreshed, or kept in sync as skills are added, removed, or renamed.
license: MIT
---

# Update Skills README

Use this skill when the top-level `README.md` in the skills repository needs to be created or refreshed.

## Goal

Keep the root `README.md` in sync with the user-facing skills in this repository.

## Default behavior

- Update `/home/ropajak/.codex/skills/README.md`.
- Include every skill directory in the repository root except hidden directories and `.system`.
- Treat a directory as a skill only if it contains `SKILL.md`.
- Link to each skill's `SKILL.md`.
- Link to the skill's local `README.md` only if that file exists.
- Preserve the current repository framing around agent skills and `agentskills.io`.

## Workflow

1. Discover skill directories in `/home/ropajak/.codex/skills`.
2. Exclude `.system` and any directory without `SKILL.md`.
3. Read each `SKILL.md` frontmatter and extract:
   - `name`
   - `description`
4. Rebuild the root `README.md` so it contains:
   - a short introduction
   - an "Available Skills" section
   - one subsection per skill
5. Keep the output deterministic by sorting skills by directory name.

## Preferred implementation

Use the bundled script:

```bash
python3 /home/ropajak/.codex/skills/update-skills-readme/scripts/update_skills_readme.py
```

## Output shape

For each skill, include:

- heading with the skill name in backticks
- one-sentence description from `SKILL.md`
- bullet linking to `SKILL.md`
- bullet linking to `README.md` when present

## Safety checks

- Do not list internal skills under `.system`.
- Do not invent skills that do not have `SKILL.md`.
- If the generated output would remove a skill unexpectedly, re-check the directory scan before writing.
