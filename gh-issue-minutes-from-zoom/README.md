# gh-issue-minutes-from-zoom

This directory contains meeting transcripts used with a global Codex skill for drafting or posting GitHub issue comments with meeting minutes.

## Example

Draft a comment from a transcript without posting it:

```text
Use gh-issue-minutes-from-zoom skill on GMT20260402-160002_Recording.transcript.vtt and draft a comment for https://github.com/open-telemetry/opentelemetry-go/issues/6648. Do not post yet.
```

Post the final comment to the issue:

```text
Use gh-issue-minutes-from-zoom skill on GMT20260402-160002_Recording.transcript.vtt and post the final comment to https://github.com/open-telemetry/opentelemetry-go/issues/6648
```

If you want to clean a Zoom `.vtt` transcript first:

```bash
python3 ~/.codex/skills/gh-issue-minutes-from-zoom/scripts/strip_zoom_vtt.py GMT20260402-160002_Recording.transcript.vtt > /tmp/meeting.txt
```
