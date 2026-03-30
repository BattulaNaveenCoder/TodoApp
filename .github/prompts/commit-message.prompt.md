---
description: "Generate a conventional commit message for staged changes"
agent: "agent"
---

Analyze the currently staged git changes (`git diff --staged`) and generate a conventional commit message.

## Format

```
<type>(<scope>): <subject>
```

**Types:** feat, fix, docs, refactor, test, chore, style, perf
**Scope:** api, web, or the specific module name
**Subject:** imperative mood, lowercase, no period, max 72 characters

## Rules

- If changes span multiple concerns, suggest separate commits.
- Output ONLY the commit message(s), nothing else.
- For multi-line bodies, add a blank line after the subject.
