/** React Query hooks for Todo CRUD operations. */

import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import type { TodoCreate, TodoUpdate } from "../types/todo";
import {
  createTodo,
  deleteTodo,
  fetchTodos,
  updateTodo,
} from "../services/todoService";

/** Query key for the todos list. */
const TODOS_KEY = ["todos"] as const;

/** Fetch all todos. */
export function useTodos() {
  return useQuery({
    queryKey: TODOS_KEY,
    queryFn: fetchTodos,
  });
}

/** Create a new todo and invalidate the list. */
export function useCreateTodo() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: (payload: TodoCreate) => createTodo(payload),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: TODOS_KEY });
    },
  });
}

/** Update an existing todo and invalidate the list. */
export function useUpdateTodo() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: ({ id, payload }: { id: number; payload: TodoUpdate }) =>
      updateTodo(id, payload),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: TODOS_KEY });
    },
  });
}

/** Delete a todo and invalidate the list. */
export function useDeleteTodo() {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: (id: number) => deleteTodo(id),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: TODOS_KEY });
    },
  });
}
