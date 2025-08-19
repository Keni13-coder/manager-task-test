from dataclasses import dataclass, field
from typing import Optional

from .exceptions import PayloadError

@dataclass(eq=False, kw_only=True)
class CreateTask():
    title: str
    description: str
    owner_id: str

@dataclass(eq=False, kw_only=True)
class UpdateTask():
    task_id: str
    owner_id: str
    title: Optional[str] = field(default=None)
    description: Optional[str] = field(default=None)
    
    def __post_init__(self):
        if not any([self.title, self.description]):
            raise PayloadError("If no arguments were passed, then the error is")

@dataclass(eq=False, kw_only=True)
class DeleteTask:
    task_id: str
    owner_id: str