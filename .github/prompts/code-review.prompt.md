---
description: "Run a pre-PR code review on changed files"
agent: "agent"
---

Review all changed files (vs the `main` branch) for the following issues:

1. **Architecture violations** — layer boundary crossings, missing DI, direct DB access from routes
2. **Missing type hints** (Python) or **TypeScript types** (frontend)
3. **Missing error handling** or input validation
4. **Security issues** — SQL injection, XSS, hardcoded secrets, unvalidated input
5. **Missing or incorrect Pydantic schemas** — raw ORM objects returned to client
6. **Unused imports or dead code**
7. **Naming convention violations** — snake_case (Python), camelCase/PascalCase (TypeScript)
8. **Missing docstrings** on public functions

For each issue found, report:
- **File**: path
- **Line**: number
- **Severity**: error | warning | info
- **Issue**: description
- **Fix**: suggested resolution

If no issues are found, confirm the code is ready for merge.
