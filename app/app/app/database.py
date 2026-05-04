import sqlite3
from typing import List
from .models import Task

DB_NAME = "tasks.db"

class TaskDB:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.create_table()

    def create_table(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done INTEGER NOT NULL,
            created_at TEXT NOT NULL
        )
        """)
        self.conn.commit()

    def add_task(self, task: Task):
        self.conn.execute(
            "INSERT INTO tasks (title, done, created_at) VALUES (?, ?, ?)",
            (task.title, int(task.done), task.created_at)
        )
        self.conn.commit()

    def get_tasks(self) -> List[Task]:
        cursor = self.conn.execute("SELECT id, title, done, created_at FROM tasks")
        rows = cursor.fetchall()
        return [Task(id=r[0], title=r[1], done=bool(r[2]), created_at=r[3]) for r in rows]

    def mark_done(self, task_id: int):
        self.conn.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))
        self.conn.commit()

    def delete_task(self, task_id: int):
        self.conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.conn.commit()
