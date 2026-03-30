import { useTodos } from "../hooks/useTodos";
import { TodoItem } from "./TodoItem";

/** Renders the list of all todos with loading and error states. */
export function TodoList() {
  const { data: todos, isLoading, isError, error } = useTodos();

  if (isLoading) {
    return <p className="todo-status">Loading todos...</p>;
  }

  if (isError) {
    return (
      <p className="todo-status error">
        Failed to load todos: {error.message}
      </p>
    );
  }

  if (!todos || todos.length === 0) {
    return <p className="todo-status">No todos yet. Add one above!</p>;
  }

  return (
    <ul className="todo-list">
      {todos.map((todo) => (
        <TodoItem key={todo.id} todo={todo} />
      ))}
    </ul>
  );
}
