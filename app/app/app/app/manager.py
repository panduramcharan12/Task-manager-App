from .database import TaskDB
from .models import Task

class TaskManager:
    def __init__(self):
        self.db = TaskDB()

    def add(self, title: str):
        task = Task(id=None, title=title)
        self.db.add_task(task)
        print("✅ Task added")

    def list(self):
        tasks = self.db.get_tasks()
        if not tasks:
            print("No tasks found.")
            return

        for task in tasks:
            status = "✔" if task.done else "✘"
            print(f"{task.id}. [{status}] {task.title} (Created: {task.created_at})")

    def done(self, task_id: int):
        self.db.mark_done(task_id)
        print("✔ Task marked as done")

    def delete(self, task_id: int):
        self.db.delete_task(task_id)
        print("🗑 Task deleted")
