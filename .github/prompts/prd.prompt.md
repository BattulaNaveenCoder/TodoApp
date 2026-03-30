---
description: "Product Requirements Document for the TodoApp — defines features, user stories, and acceptance criteria"
---

# TodoApp — Product Requirements Document (PRD)

## 1. Product Overview

**Product Name:** TodoApp
**Type:** Single-user, full-stack task management application
**Purpose:** Provide a clean, fast, and reliable way to create, organize, and track personal tasks with optional category grouping.

## 2. Target User

A single user running the app locally. No authentication or multi-tenancy required.

## 3. Core Features

### 3.1 Todo Management (Phase 1)

| ID | User Story | Acceptance Criteria |
|----|-----------|---------------------|
| T-1 | As a user, I can create a todo with a title and optional description | Title is required (1–200 chars). Description is optional. Todo appears in the list immediately. |
| T-2 | As a user, I can view all my todos | Todos are listed in reverse chronological order. Each shows title, description, and completion status. |
| T-3 | As a user, I can mark a todo as completed or incomplete | Clicking the checkbox toggles `is_completed`. Completed todos show a strikethrough title. |
| T-4 | As a user, I can edit a todo's title and description | Partial updates via PATCH. Changes reflect immediately. |
| T-5 | As a user, I can delete a todo | Deleting removes the todo permanently. The list refreshes automatically. |

### 3.2 Category Management (Phase 3)

| ID | User Story | Acceptance Criteria |
|----|-----------|---------------------|
| C-1 | As a user, I can create named categories | Name is required (1–100 chars), must be unique (409 on duplicate). |
| C-2 | As a user, I can view all categories | Categories listed alphabetically. |
| C-3 | As a user, I can assign a category to a todo | Optional foreign key. Displayed next to the todo title. |
| C-4 | As a user, I can filter todos by category | Selecting a category shows only its todos. "All" shows everything. |
| C-5 | As a user, I can delete a category | Todos in the deleted category become uncategorized (SET NULL). |

## 4. Non-Functional Requirements

| Requirement | Target |
|-------------|--------|
| Response time | < 200ms for all API endpoints under normal load |
| Input validation | All user input validated on both client and server |
| Error feedback | Meaningful error messages shown to the user (not raw server errors) |
| Accessibility | Semantic HTML, ARIA labels on interactive elements |
| Browser support | Latest Chrome, Firefox, Edge |

## 5. Out of Scope

- Authentication / authorization
- Multi-user / multi-tenancy
- File uploads or attachments
- Due dates, priorities, or reminders
- Mobile-native app
- Deployment / CI/CD pipeline

## 6. Phases

| Phase | Deliverable |
|-------|------------|
| 0 | Project skeleton, Copilot customization, database connection |
| 1 | Full Todo CRUD (backend + frontend) |
| 2 | Unit tests (backend + frontend) |
| 3 | Category entity + todo-category relationship |
| 4 | Expanded tests, edge cases, failure resolution |
| 5 | Integration run + security review |
