import { useDeleteTodo, useUpdateTodo } from "../hooks/useTodos";
import type { Todo } from "../types/todo";

interface TodoItemProps {
  todo: Todo;
}

/** Renders a single todo with toggle and delete actions. */
export function TodoItem({ todo }: TodoItemProps) {
  const updateTodo = useUpdateTodo();
  const deleteTodo = useDeleteTodo();

  const handleToggle = () => {
    updateTodo.mutate({
      id: todo.id,
      payload: { is_completed: !todo.is_completed },
    });
  };

  const handleDelete = () => {
    deleteTodo.mutate(todo.id);
  };

  return (
    <li className={`todo-item ${todo.is_completed ? "completed" : ""}`}>
      <label className="todo-label">
        <input
          type="checkbox"
          checked={todo.is_completed}
          onChange={handleToggle}
          disabled={updateTodo.isPending}
        />
        <span className="todo-title">{todo.title}</span>
      </label>
      {todo.description && (
        <p className="todo-description">{todo.description}</p>
      )}
      <button
        className="todo-delete"
        onClick={handleDelete}
        disabled={deleteTodo.isPending}
        aria-label={`Delete ${todo.title}`}
      >
        {deleteTodo.isPending ? "..." : "✕"}
      </button>
    </li>
  );
}
