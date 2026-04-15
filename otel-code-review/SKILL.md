---
name: otel-code-review
description: Review code changes like an OpenTelemetry maintainer, with emphasis on spec compliance, semantic conventions, compatibility, tests, performance, and security. Use when the user wants an code review for an OpenTelemetry repository on a patch, PR, or local diff.
---

# OTel Code Review

Use this skill when the user wants a focused OpenTelemetry code review rather than a generic summary.

## Goal

Review changes like a maintainer, not a summarizer.

## Repository-first workflow

Start by finding and following the repository's guidance in `AGENTS.md`, `CONTRIBUTING.md`, `docs/`, `Makefile` targets, CI config, lint config, formatting config, and existing test and benchmark patterns.

Prefer repo-local instructions over general preferences.

## Primary review criteria

- Check whether the change aligns with the OpenTelemetry mission of making high-quality, portable telemetry ubiquitous, and with the project's engineering direction toward telemetry that is easy, universal, vendor-neutral, loosely coupled, and built in.
- Check whether the change is compliant with the relevant OpenTelemetry specification requirements and SDK or API guidance for the language and signal involved.
- Check whether emitted telemetry follows the applicable OpenTelemetry semantic conventions, including attribute names, units, event names, span names, metric names, and resource or scope metadata where relevant.
- Confirm the change follows the project's existing contributing guidelines, review norms, coding standards, and workflow expectations.
- Check whether the code is idiomatic for the language, framework, and tooling in this repository.
- Check whether the implementation follows existing local patterns instead of introducing unnecessary novelty.
- Check whether behavior is covered by the right level of tests. Distinguish between unit, integration, regression, snapshot, property, fuzz, and end-to-end tests when relevant.
- If the change touches a hot path, algorithmic complexity, allocation-heavy code, serialization, database access, rendering, concurrency, or other performance-sensitive paths, check whether benchmarks or equivalent performance validation were added or updated.
- Check for breaking changes in both syntax and behavior. Look for API changes, changed defaults, changed error behavior, stricter validation, schema drift, wire-format changes, timing changes, concurrency changes, migration hazards, and compatibility issues.
- Check for security issues including input validation gaps, injection risks, authn or authz mistakes, secret exposure, unsafe deserialization, path traversal, SSRF, XSS, CSRF, privilege escalation, insecure temp-file handling, and denial-of-service risks.
- Check whether linting and formatting expectations are satisfied or whether the patch obviously violates configured linters, static analysis, or formatting rules.
- Check whether comments explain intent, invariants, tradeoffs, and non-obvious constraints. Prefer comments that explain why, not what. Flag redundant or misleading comments.

## Also review for

- OpenTelemetry-specific issues such as incorrect span boundaries, broken context propagation, invalid status or error mapping, duplicate instrumentation, high-cardinality attributes, unstable metric identity, and telemetry that is difficult to correlate across signals.
- Missing docs, changelog, migration notes, or feature-flag guidance when the change alters user-visible behavior.
- Incomplete error handling, cleanup, retries, timeouts, cancellation, or observability.
- Race conditions, deadlocks, resource leaks, and unsafe shared-state patterns.
- Partial implementations that update code but not tests, fixtures, docs, examples, generated files, or configuration.
- Weak naming, confusing abstractions, or avoidable complexity that hides risk.

## Reporting rules

- Lead with findings, ordered by severity.
- For each finding, cite concrete files, symbols, and the exact behavior at risk.
- Prefer actionable findings over style nits.
- Call out missing evidence explicitly, for example when a hot-path change lacks benchmarks or a risky change lacks regression tests.
- If no material issues are found, say that explicitly and list residual risks or verification gaps.
- Keep the review concise, evidence-based, and grounded in the repository's actual conventions.

## Constraints

- Keep the review read-only unless the parent task explicitly asks for code changes.
