from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class User(BaseModel):
    username: str
    hashed_password: str

class UserInDB(User):
    pass

class UserCreate(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class TaskStatus(str):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"

class Task(BaseModel):
    id: str
    title: str
    description: str
    status: str = Field(default=TaskStatus.TODO)
    createdAt: datetime
    updatedAt: datetime

class TaskCreate(BaseModel):
    title: str
    description: str
    status: Optional[str] = TaskStatus.TODO

class TaskUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[str]