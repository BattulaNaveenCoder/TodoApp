/** API client functions for Todo CRUD operations. */

import api from "./api";
import type { Todo, TodoCreate, TodoUpdate } from "../types/todo";

const ENDPOINT = "/todos";

/** Fetch all todos. */
export async function fetchTodos(): Promise<Todo[]> {
  const { data } = await api.get<Todo[]>(`${ENDPOINT}/`);
  return data;
}

/** Fetch a single todo by ID. */
export async function fetchTodoById(id: number): Promise<Todo> {
  const { data } = await api.get<Todo>(`${ENDPOINT}/${id}`);
  return data;
}

/** Create a new todo. */
export async function createTodo(payload: TodoCreate): Promise<Todo> {
  const { data } = await api.post<Todo>(`${ENDPOINT}/`, payload);
  return data;
}

/** Update an existing todo (partial). */
export async function updateTodo(
  id: number,
  payload: TodoUpdate
): Promise<Todo> {
  const { data } = await api.patch<Todo>(`${ENDPOINT}/${id}`, payload);
  return data;
}

/** Delete a todo by ID. */
export async function deleteTodo(id: number): Promise<void> {
  await api.delete(`${ENDPOINT}/${id}`);
}
