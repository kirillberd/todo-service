from sqlmodel import Field, SQLModel
from typing import Optional
from datetime import datetime

class Task(SQLModel):
    __tablename__ = "task"
    id: Optional[int] = Field(nullable=False, primary_key=True)
    user_id: str = Field(nullable=False)
    task_name: str = Field(nullable=False)
    tags: Optional[set[str]] = Field(nullable=True)
    comments: Optional[str] = Field(nullable=True)
    created_at: datetime = Field(default=datetime.now())
    state: str = Field(nullable=False)
    deadline: Optional[datetime] = Field(nullable=True)
    
