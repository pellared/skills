#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


TIMESTAMP_RE = re.compile(
    r"^\d{2}:\d{2}:\d{2}\.\d{3}\s+-->\s+\d{2}:\d{2}:\d{2}\.\d{3}"
)
SPEAKER_RE = re.compile(r"^(?P<speaker>[^:]{1,80}):\s*(?P<text>.*)$")


@dataclass
class Turn:
    speaker: str | None
    text: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert a Zoom/WebVTT transcript into compact speaker turns."
    )
    parser.add_argument("path", help="Path to a .vtt transcript file")
    return parser.parse_args()


def cue_blocks(text: str) -> list[str]:
    lines = [line.rstrip() for line in text.splitlines()]
    blocks: list[list[str]] = []
    current: list[str] = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            if current:
                blocks.append(current)
                current = []
            continue
        if stripped == "WEBVTT":
            continue
        current.append(stripped)

    if current:
        blocks.append(current)

    return ["\n".join(block) for block in blocks]


def parse_turns(text: str) -> list[Turn]:
    turns: list[Turn] = []

    for block in cue_blocks(text):
        lines = block.splitlines()
        if len(lines) >= 2 and lines[0].isdigit() and TIMESTAMP_RE.match(lines[1]):
            payload = lines[2:]
        elif lines and TIMESTAMP_RE.match(lines[0]):
            payload = lines[1:]
        else:
            payload = lines

        if not payload:
            continue

        joined = " ".join(part.strip() for part in payload if part.strip())
        joined = re.sub(r"\s+", " ", joined).strip()
        if not joined:
            continue

        match = SPEAKER_RE.match(joined)
        if match:
            speaker = match.group("speaker").strip()
            text_part = match.group("text").strip()
        else:
            speaker = None
            text_part = joined

        if not text_part:
            continue

        if turns and turns[-1].speaker == speaker:
            turns[-1].text = f"{turns[-1].text} {text_part}".strip()
        else:
            turns.append(Turn(speaker=speaker, text=text_part))

    return turns


def main() -> int:
    args = parse_args()
    path = Path(args.path)
    text = path.read_text(encoding="utf-8")

    for turn in parse_turns(text):
        if turn.speaker:
            print(f"{turn.speaker}: {turn.text}")
        else:
            print(turn.text)
        print()

    return 0


if __name__ == "__main__":
    sys.exit(main())
