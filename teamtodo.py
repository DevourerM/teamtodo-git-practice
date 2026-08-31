"""TeamTodo - Git/GitHub 多人协作课程的起始项目。

重要：main 分支故意只提供基础功能。
Issue #1、#2、#6 会要求你逐步扩展它。
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


@dataclass
class Task:
    title: str
    done: bool = False
    priority:str = 'normal'    #优先级


class TodoList:
    def __init__(self, tasks: Iterable[Task] | None = None) -> None:
        self.tasks = list(tasks or [])

    def add(self, title: str , priority:str) -> Task:
        title = title.strip()
        if not title:
            raise ValueError("任务标题不能为空")
        if not priority in ['normal' , 'hard' , 'easy']:
            raise ValueError("难度输入有误")
        task = Task(title=title , priority=priority)
        self.tasks.append(task)
        return task

    def complete(self, index: int) -> Task:
        task = self._get(index)
        task.done = True
        return task

    def delete(self, index: int) -> Task:
        self._validate_index(index)
        return self.tasks.pop(index)

    def pending(self) -> list[Task]:
        return [task for task in self.tasks if not task.done]

    def completed(self) -> list[Task]:
        return [task for task in self.tasks if task.done]

    def _get(self, index: int) -> Task:
        self._validate_index(index)
        return self.tasks[index]

    def _validate_index(self, index: int) -> None:
        if index < 0 or index >= len(self.tasks):
            raise IndexError("任务编号不存在")


def load_tasks(path: str | Path) -> TodoList:
    path = Path(path)
    if not path.exists():
        return TodoList()

    data = json.loads(path.read_text(encoding="utf-8"))
    return TodoList(Task(**item) for item in data)


def save_tasks(todo: TodoList, path: str | Path) -> None:
    path = Path(path)
    data = [asdict(task) for task in todo.tasks]
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def print_tasks(todo: TodoList) -> None:
    print("\n--- 当前任务 ---")
    if not todo.tasks:
        print("还没有任务。")
        return

    for i, task in enumerate(todo.tasks, start=1):
        marker = "x" if task.done else " "
        print(f"{i}. [{marker}] [{task.priority.upper()}] {task.title}")


def ask_index(prompt: str) -> int:
    raw = input(prompt).strip()
    return int(raw) - 1


def main() -> None:
    data_file = Path("teamtodo_data.json")
    todo = load_tasks(data_file)

    while True:
        print(
            "\n=== TeamTodo ===\n"
            "1. 查看任务\n"
            "2. 新建任务\n"
            "3. 完成任务\n"
            "4. 删除任务\n"
            "0. 退出"
        )

        choice = input("请选择：").strip()

        try:
            if choice == "1":
                print_tasks(todo)
            elif choice == "2":
                title = input("任务标题：")
                priority = input("任务难度：")
                todo.add(title ,priority)
                save_tasks(todo, data_file)
                print("已添加任务。")
            elif choice == "3":
                print_tasks(todo)
                index = ask_index("要完成第几个任务：")
                todo.complete(index)
                save_tasks(todo, data_file)
                print("任务已完成。")
            elif choice == "4":
                print_tasks(todo)
                index = ask_index("要删除第几个任务：")
                removed = todo.delete(index)
                save_tasks(todo, data_file)
                print(f"已删除：{removed.title}")
            elif choice == "0":
                print("再见。")
                break
            else:
                print("请输入 0~4。")
        except (ValueError, IndexError) as exc:
            print(f"操作失败：{exc}")


if __name__ == "__main__":
    main()
