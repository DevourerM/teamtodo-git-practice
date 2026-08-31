import tempfile
import unittest
from pathlib import Path

from teamtodo import Task, TodoList, load_tasks, save_tasks


class TodoListTests(unittest.TestCase):
    def test_add_task(self):
        todo = TodoList()
        task = todo.add("学习 git status" , "easy")
        self.assertEqual(task.title, "学习 git status")
        self.assertEqual(task.priority, "easy")
        self.assertFalse(task.done)
        self.assertEqual(len(todo.tasks), 1)

    def test_add_empty_title_fails(self):
        todo = TodoList()
        with self.assertRaises(ValueError):
            todo.add("   " , 'easy')

    def test_complete_task(self):
        todo = TodoList([Task("提交 PR")])
        todo.complete(0)
        self.assertTrue(todo.tasks[0].done)
        self.assertEqual(len(todo.completed()), 1)

    def test_delete_task(self):
        todo = TodoList([Task("A"), Task("B")])
        removed = todo.delete(0)
        self.assertEqual(removed.title, "A")
        self.assertEqual([task.title for task in todo.tasks], ["B"])

    def test_invalid_index_fails(self):
        todo = TodoList([Task("A")])
        with self.assertRaises(IndexError):
            todo.complete(10)

    def test_save_and_load(self):
        todo = TodoList([Task("学习 PR"), Task("学习 Review", done=True)])
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "todo.json"
            save_tasks(todo, path)
            loaded = load_tasks(path)
        self.assertEqual(len(loaded.tasks), 2)
        self.assertEqual(loaded.tasks[0].title, "学习 PR")
        self.assertTrue(loaded.tasks[1].done)


if __name__ == "__main__":
    unittest.main()
    print("issue4 留痕")
