from pydantic import BaseModel
from typing import Optional

class Todo(BaseModel):
    id: int
    name: str
    email: str
    description: str

class TodoCreate(BaseModel):
    name: str
    email: str
    description: str

class TodoUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    description: Optional[str] = None
