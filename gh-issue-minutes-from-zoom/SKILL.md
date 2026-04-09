---
name: gh-issue-minutes-from-zoom
description: Draft or post GitHub issue comments with meeting minutes from a Zoom transcript file using gh. Use when the user wants recurring SIG-style meeting notes added to an issue such as open-telemetry/opentelemetry-go#6648 from a .vtt transcript or cleaned text transcript.
---

# GH Issue Minutes From Zoom

Use this skill when the user wants a GitHub issue comment created from a Zoom meeting transcript, especially for recurring "meeting notes" issues.

## Default behavior

- Prefer a draft-first workflow. Only post with `gh issue comment` if the user explicitly asks to publish.
- Match the target issue's existing comment style before drafting.
- Treat the transcript as the source of truth. Do not invent decisions, links, or action items.

## Workflow

1. Inspect the target issue and recent comments.

```bash
gh issue view ISSUE_NUMBER --repo OWNER/REPO --comments
```

Pay attention to:

- whether the issue is minutes-only
- the usual section structure
- date formatting
- how related issues and PRs are linked

2. If the transcript is Zoom `.vtt`, normalize it first.

```bash
python3 .codex/skills/gh-issue-minutes-from-zoom/scripts/strip_zoom_vtt.py PATH/TO/MEETING.vtt > /tmp/meeting.txt
```

If the user already provided cleaned text, you can skip this step.

3. Draft a concise markdown comment with the same overall shape as the issue.

Preferred structure for issues like `open-telemetry/opentelemetry-go#6648`:

- `**Date:** YYYY-MM-DD`
- `## Attendees`
- `## Discussions`
- `## Decisions` if there were clear outcomes
- `## Action Items` when owners or follow-ups are explicit

4. Keep the comment useful and conservative.

- Summarize by topic, not by transcript chronology.
- Keep bullets factual and short.
- Mention uncertainty plainly instead of guessing.
- Omit weakly supported claims.
- Include related PRs or issues only when they are stated in the transcript or can be verified from the surrounding issue context.

5. Show the draft to the user unless they asked to post immediately.

If posting is requested, write the comment to a temp file and publish with:

```bash
gh issue comment ISSUE_NUMBER --repo OWNER/REPO --body-file /tmp/issue-comment.md
```

## Drafting guidance

- Derive attendees from people who actively joined the discussion; omit names that are too ambiguous to identify confidently.
- If the transcript contains obvious ASR mistakes, silently normalize only when the meaning is clear.
- Preserve proper names, package names, issue numbers, and PR numbers exactly when known.
- For action items, prefer `- [ ] Owner: task` format.
- If no decisions or action items were made, omit those sections.

## Safety checks

- Run `gh auth status` if GitHub access is uncertain.
- If the issue body says comments must only contain minutes, do not add process chatter.
- Before posting, quickly re-read the draft for names, dates, and accidental hallucinated links.
