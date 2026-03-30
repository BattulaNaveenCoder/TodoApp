---
description: "Use when writing React TypeScript frontend code. Covers React 18, TanStack Query, and Axios patterns."
applyTo: "web/src/**/*.{ts,tsx}"
---

# TypeScript / React Conventions

- Use functional components with explicit return types.
- Custom hooks in `src/hooks/` — one file per domain (`useTodos.ts`, `useCategories.ts`).
- API call functions in `src/services/` — one file per domain (`todoService.ts`).
- Types and interfaces in `src/types/` — shared DTO types matching backend Pydantic schemas.
- Use React Query (`useQuery`, `useMutation`) for all server state management.
- Invalidate relevant queries after mutations for automatic UI refresh.
- Use the shared Axios instance from `src/services/api.ts` for all HTTP calls.
- Prefer named exports over default exports (except for page components).
- Use `camelCase` for functions/variables, `PascalCase` for components/types/interfaces.
- Keep components small and focused — extract reusable pieces into `src/components/`.
