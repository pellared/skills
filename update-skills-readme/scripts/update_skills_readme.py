#!/usr/bin/env python3

from __future__ import annotations

from pathlib import Path
import re


ROOT = Path("/home/ropajak/.codex/skills")
README_PATH = ROOT / "README.md"


def parse_frontmatter(skill_md: Path) -> dict[str, str]:
    text = skill_md.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        return {}

    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def collect_skills() -> list[dict[str, str | Path | bool]]:
    skills: list[dict[str, str | Path | bool]] = []
    for entry in sorted(ROOT.iterdir(), key=lambda path: path.name):
        if not entry.is_dir():
            continue
        if entry.name.startswith(".") or entry.name == ".system":
            continue

        skill_md = entry / "SKILL.md"
        if not skill_md.exists():
            continue

        frontmatter = parse_frontmatter(skill_md)
        description = frontmatter.get("description", "").strip()
        skills.append(
            {
                "dir_name": entry.name,
                "skill_name": frontmatter.get("name", entry.name),
                "description": description,
                "skill_md": skill_md,
                "readme": entry / "README.md",
                "has_readme": (entry / "README.md").exists(),
            }
        )
    return skills


def render_readme(skills: list[dict[str, str | Path | bool]]) -> str:
    lines = [
        "# Agent Skills",
        "",
        "This directory contains local [agent skills](https://agentskills.io/).",
        "",
        "The list below includes user-facing skills in this repository and excludes internal skills under `.system`.",
        "",
        "## Available Skills",
        "",
    ]

    for skill in skills:
        skill_name = str(skill["skill_name"])
        description = str(skill["description"]).rstrip(".")
        skill_md = Path(skill["skill_md"])
        readme = Path(skill["readme"])

        lines.append(f"### `{skill_name}`")
        lines.append("")
        if description:
            lines.append(f"{description}.")
            lines.append("")
        lines.append(f"- Skill file: [{skill_md.relative_to(ROOT).as_posix()}]({skill_md})")
        if bool(skill["has_readme"]):
            lines.append(f"- README: [{readme.relative_to(ROOT).as_posix()}]({readme})")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def main() -> None:
    skills = collect_skills()
    README_PATH.write_text(render_readme(skills), encoding="utf-8")


if __name__ == "__main__":
    main()
