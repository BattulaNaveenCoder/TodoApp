import { type FormEvent, useState } from "react";
import { useCreateTodo } from "../hooks/useTodos";

/** Form for adding a new todo item. */
export function TodoForm() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const createTodo = useCreateTodo();

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();
    const trimmedTitle = title.trim();
    if (!trimmedTitle) return;

    createTodo.mutate(
      {
        title: trimmedTitle,
        description: description.trim() || null,
      },
      {
        onSuccess: () => {
          setTitle("");
          setDescription("");
        },
      }
    );
  };

  return (
    <form className="todo-form" onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="What needs to be done?"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        maxLength={200}
        required
      />
      <input
        type="text"
        placeholder="Description (optional)"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />
      <button type="submit" disabled={createTodo.isPending}>
        {createTodo.isPending ? "Adding..." : "Add Todo"}
      </button>
    </form>
  );
}
