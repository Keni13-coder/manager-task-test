from typing import Optional
from pydantic import BaseModel, Field

class RequestCreateTask(BaseModel):
    task_id: str
    title: str
    description: str
    owner_id: str
    
class RequestUpdateTask(BaseModel):
    task_id: Optional[str] = Field(default=None)
    owner_id: Optional[str] = Field(default=None)
    title: Optional[str] = Field(default=None)
    description: Optional[str] = Field(default=None)
    
class RequestDeleteTask(BaseModel):
    task_id: str
    owner_id: str

class ResponseTaskId(BaseModel):
    task_id: str
    