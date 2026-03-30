/** Shared TypeScript types for Todo entities, matching backend Pydantic schemas. */

/** A todo item as returned by the API. */
export interface Todo {
  id: number;
  title: string;
  description: string | null;
  is_completed: boolean;
  created_at: string;
  updated_at: string;
}

/** Payload for creating a new todo. */
export interface TodoCreate {
  title: string;
  description?: string | null;
}

/** Payload for updating an existing todo (all fields optional). */
export interface TodoUpdate {
  title?: string;
  description?: string | null;
  is_completed?: boolean;
}
