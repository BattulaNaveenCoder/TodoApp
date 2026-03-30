import { TodoForm } from "../components/TodoForm";
import { TodoList } from "../components/TodoList";

/** Main page displaying the todo form and list. */
export default function TodoPage() {
  return (
    <div className="todo-page">
      <h1>Todo App</h1>
      <TodoForm />
      <TodoList />
    </div>
  );
}
