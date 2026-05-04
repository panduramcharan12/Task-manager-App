from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class Task:
    id: Optional[int]
    title: str
    done: bool = False
    created_at: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
