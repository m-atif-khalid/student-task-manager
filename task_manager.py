"""Core logic for the Student Task Manager."""

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Task title cannot be empty.")
        task = {"id": self.next_id, "title": title.strip(), "completed": False}
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_tasks(self):
        return self.tasks.copy()

    def complete_task(self, task_id):
        task = self._find_task(task_id)
        if task is None:
            return False
        task["completed"] = True
        return True

    def delete_task(self, task_id):
        task = self._find_task(task_id)
        if task is None:
            return False
        self.tasks.remove(task)
        return True

    def _find_task(self, task_id):
        try:
            task_id = int(task_id)
        except (TypeError, ValueError):
            return None
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None
    def complete_task(self, task_id):
    task = self._find_task(task_id)

    if task is None:
        return False

    task["completed"] = True
    return True
