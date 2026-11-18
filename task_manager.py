"""
Student Task Manager - Core Domain Model & Business Logic
"""
from typing import List, Optional


class Task:
    """Represents a single task item."""

    def __init__(self, task_id: int, title: str, completed: bool = False):
        self.id = task_id
        self.title = title
        self.completed = completed

    def __str__(self) -> str:
        status_flag = "[✓]" if self.completed else "[ ]"
        return f"{status_flag} #{self.id}: {self.title}"


class TaskManager:
    """Manages collection of tasks, ID allocation, and CRUD operations."""

    def __init__(self):
        self._tasks: List[Task] = []
        self._counter: int = 1

    def add_task(self, title: str) -> Task:
        """Adds a task with input validation rejecting empty or whitespace strings."""
        sanitized_title = title.strip() if title else ""
        if not sanitized_title:
            raise ValueError("Task title cannot be empty or whitespace.")

        new_task = Task(task_id=self._counter, title=sanitized_title)
        self._tasks.append(new_task)
        self._counter += 1
        return new_task

    def get_all_tasks(self) -> List[Task]:
        """Returns all current tasks."""
        return list(self._tasks)

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """Finds a task by its identifier."""
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def complete_task(self, task_id: int) -> bool:
        """Marks a task as completed."""
        task = self.get_task_by_id(task_id)
        if not task:
            raise KeyError(f"Task with ID {task_id} not found.")
        task.completed = True
        return True

    def delete_task(self, task_id: int) -> bool:
        """Deletes a task by ID."""
        task = self.get_task_by_id(task_id)
        if not task:
            raise KeyError(f"Task with ID {task_id} not found.")
        self._tasks.remove(task)
        return True
